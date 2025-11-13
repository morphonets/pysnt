"""
Javadoc HTML parser for extracting method and class documentation.
"""

import re
from pathlib import Path
from typing import Dict, List, Optional, Any
from dataclasses import dataclass
from bs4 import BeautifulSoup, Tag

from .logging_setup import get_logger

logger = get_logger('javadoc_parser')

# The package patterns to parse javadocs
packages_to_try = [
    'sc.fiji.snt',
    'sc.fiji.snt.analysis',
    'sc.fiji.snt.annotation',
    'sc.fiji.snt.filter',
    'sc.fiji.snt.gui',
    'sc.fiji.snt.io',
    'sc.fiji.snt.plugin',
    'sc.fiji.snt.tracing',
    'sc.fiji.snt.util',
    'sc.fiji.snt.viewer'
]

@dataclass
class ParameterDoc:
    """Parameter documentation from JavaDoc."""
    name: str
    description: str
    type_hint: Optional[str] = None


@dataclass
class MethodDocumentation:
    """JavaDoc-extracted method documentation."""
    name: str
    signature: str
    description: str
    parameters: List[ParameterDoc]
    return_description: str
    return_type: str
    examples: List[str]
    deprecated: bool
    since_version: Optional[str]
    see_also: List[str]
    throws: Dict[str, str]  # exception_type -> description
    modifiers: List[str]
    overrides: Optional[str] = None


@dataclass
class FieldDocumentation:
    """JavaDoc-extracted field documentation."""
    name: str
    type_name: str
    description: str
    deprecated: bool
    since_version: Optional[str]
    modifiers: List[str]


@dataclass
class ConstructorDocumentation:
    """JavaDoc-extracted constructor documentation."""
    signature: str
    description: str
    parameters: List[ParameterDoc]
    throws: Dict[str, str]
    deprecated: bool
    since_version: Optional[str]
    modifiers: List[str]


@dataclass
class ClassDocumentation:
    """Complete JavaDoc documentation for a class."""
    class_name: str
    package: str
    description: str
    inheritance: Dict[str, List[str]]  # 'extends', 'implements'
    methods: List[MethodDocumentation]
    fields: List[FieldDocumentation]
    constructors: List[ConstructorDocumentation]
    nested_classes: List[str]
    deprecated: bool
    since_version: Optional[str]
    see_also: List[str]


class JavaDocHTMLParser:
    """Parses JavaDoc HTML files to extract method and class documentation."""
    
    def __init__(self, javadoc_root: Path):
        """Initialize with path to extracted JavaDoc directory."""
        self.logger = logger
        self.javadoc_root = self._find_actual_javadoc_root(javadoc_root)
    
    def _find_actual_javadoc_root(self, extract_dir: Path) -> Path:
        """Find the actual JavaDoc root directory (handles nested ZIP structure)."""
        if not extract_dir.exists():
            self.logger.warning(f"JavaDoc extract directory does not exist: {extract_dir}")
            return extract_dir
        
        # Check if files are directly in extract_dir
        if (extract_dir / 'index.html').exists():
            self.logger.info(f"Found JavaDoc root at: {extract_dir}")
            return extract_dir
        
        # Look for nested directories that contain index.html
        for item in extract_dir.iterdir():
            if item.is_dir() and not item.name.startswith('.') and item.name != '__MACOSX':
                if (item / 'index.html').exists():
                    self.logger.info(f"Found JavaDoc root in subdirectory: {item}")
                    return item
                # Check one more level deep
                for subitem in item.iterdir():
                    if subitem.is_dir() and not subitem.name.startswith('.') and subitem.name != '__MACOSX':
                        if (subitem / 'index.html').exists():
                            self.logger.info(f"Found JavaDoc root in nested subdirectory: {subitem}")
                            return subitem
        
        self.logger.warning(f"Could not find JavaDoc root with index.html in {extract_dir}")
        return extract_dir
    
    def parse_all_classes(self, class_names: Optional[List[str]] = None) -> Dict[str, ClassDocumentation]:
        """
        Parse JavaDoc for multiple classes.
        
        Args:
            class_names: List of class names to parse. If None, attempts to find all available classes.
            
        Returns:
            Dictionary mapping class names to ClassDocumentation objects
        """
        parsed_classes = {}
        
        if class_names is None:
            # Find all HTML files in the JavaDoc directory
            class_names = self._discover_available_classes()
        
        self.logger.info(f"Parsing JavaDoc for {len(class_names)} classes...")
        
        for class_name in class_names:
            try:
                class_doc = None
                for i, package in enumerate(packages_to_try):
                    # Use silent mode for all attempts except the last one
                    silent = (i < len(packages_to_try) - 1)
                    class_doc = self.parse_class(class_name, package, silent=silent)
                    if class_doc:
                        self.logger.debug(f"✓ Parsed {class_name} from {package}")
                        break
                
                if class_doc:
                    parsed_classes[class_name] = class_doc
                else:
                    self.logger.warning(f"⚠ Could not find JavaDoc for {class_name} in any package")
                    
            except Exception as e:
                self.logger.error(f"✗ Failed to parse {class_name}: {e}")
                continue
        
        self.logger.info(f"Successfully parsed {len(parsed_classes)} out of {len(class_names)} classes")
        return parsed_classes
    
    def _discover_available_classes(self) -> List[str]:
        """Discover all available class HTML files in the JavaDoc directory."""
        class_names = []
        
        # Recursively find all .html files
        for html_file in self.javadoc_root.rglob('*.html'):
            # Skip index files and other non-class files
            if html_file.name in ['index.html', 'package-summary.html', 'package-tree.html', 
                                  'package-use.html', 'overview-summary.html', 'overview-tree.html',
                                  'deprecated-list.html', 'index-all.html', 'help-doc.html']:
                continue
            
            # Extract class name from filename
            class_name = html_file.stem
            
            # Skip if it looks like a package file
            if class_name.startswith('package-') or class_name.endswith('-summary'):
                continue
            
            class_names.append(class_name)
        
        # Remove duplicates and sort
        class_names = sorted(list(set(class_names)))
        self.logger.info(f"Discovered {len(class_names)} potential class files")
        
        return class_names

    def parse_class(self, class_name: str, package: str = 'sc.fiji.snt', silent: bool = False) -> Optional[ClassDocumentation]:
        """
        Parse JavaDoc for a specific class.
        
        Args:
            class_name: Name of the Java class
            package: Java package name (default: sc.fiji.snt)
            silent: If True, don't log warnings for missing files (useful when trying multiple packages)
            
        Returns:
            ClassDocumentation object if successful, None otherwise
        """
        # Convert package name to file path
        package_path = package.replace('.', '/')
        html_file = self.javadoc_root / package_path / f'{class_name}.html'
        
        if not html_file.exists():
            if not silent:
                self.logger.warning(f"JavaDoc HTML file not found: {html_file}")
            else:
                self.logger.debug(f"JavaDoc HTML file not found: {html_file}")
            return None
        
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                html_content = f.read()
            
            soup = BeautifulSoup(html_content, 'html.parser')
            
            # Extract class-level information
            class_doc = ClassDocumentation(
                class_name=class_name,
                package=package,
                description=self._extract_class_description(soup),
                inheritance=self._extract_inheritance_info(soup),
                methods=self._extract_method_docs(soup),
                fields=self._extract_field_docs(soup),
                constructors=self._extract_constructor_docs(soup),
                nested_classes=self._extract_nested_classes(soup),
                deprecated=self._is_deprecated(soup),
                since_version=self._extract_since_version(soup),
                see_also=self._extract_see_also(soup)
            )
            
            self.logger.info(f"Successfully parsed JavaDoc for {class_name}: "
                           f"{len(class_doc.methods)} methods, "
                           f"{len(class_doc.constructors)} constructors, "
                           f"{len(class_doc.fields)} fields")
            
            return class_doc
            
        except Exception as e:
            self.logger.error(f"Failed to parse JavaDoc for {class_name}: {e}")
            return None
    
    def _extract_class_description(self, soup: BeautifulSoup) -> str:
        """Extract class overview description from JavaDoc HTML."""
        # Look for the class description in the type signature section
        type_signature_section = soup.find('div', class_='type-signature')
        if type_signature_section:
            # The description is usually in a div with class 'block' after the type signature
            description_div = type_signature_section.find_next_sibling('div', class_='block')
            if description_div:
                return self.clean_javadoc_content(str(description_div))
        
        # Fallback: look for any div with class 'block' in the main content
        block_divs = soup.find_all('div', class_='block')
        if block_divs:
            return self.clean_javadoc_content(str(block_divs[0]))
        
        return ""
    
    def _extract_inheritance_info(self, soup: BeautifulSoup) -> Dict[str, List[str]]:
        """Extract inheritance information (extends, implements)."""
        inheritance = {'extends': [], 'implements': []}
        
        # Look for inheritance info in the type signature
        type_signature = soup.find('div', class_='type-signature')
        if type_signature:
            extends_implements = type_signature.find('span', class_='extends-implements')
            if extends_implements:
                text = extends_implements.get_text()
                
                # Extract extends information
                extends_match = re.search(r'extends\s+([^implements]+)', text)
                if extends_match:
                    extends_text = extends_match.group(1).strip()
                    # Extract class names from links
                    extends_links = extends_implements.find_all('a')
                    for link in extends_links:
                        if 'extends' in text[:text.find(link.get_text())]:
                            inheritance['extends'].append(link.get_text())
                
                # Extract implements information
                implements_match = re.search(r'implements\s+(.+)', text)
                if implements_match:
                    implements_text = implements_match.group(1).strip()
                    # Extract interface names from links
                    implements_links = extends_implements.find_all('a')
                    for link in implements_links:
                        if 'implements' in text[:text.find(link.get_text())]:
                            inheritance['implements'].append(link.get_text())
        
        return inheritance
    
    def _extract_method_docs(self, soup: BeautifulSoup) -> List[MethodDocumentation]:
        """Extract method documentation from JavaDoc HTML."""
        methods = []
        
        # Find the method details section
        method_details = soup.find('section', {'class': 'method-details', 'id': 'method-detail'})
        if not method_details:
            self.logger.debug("No method details section found")
            return methods
        
        # Find all method detail sections
        method_sections = method_details.find_all('section', class_='detail')
        
        for section in method_sections:
            try:
                method_doc = self._parse_method_section(section)
                if method_doc:
                    methods.append(method_doc)
            except Exception as e:
                self.logger.warning(f"Failed to parse method section: {e}")
                continue
        
        return methods
    
    def _parse_method_section(self, section: Tag) -> Optional[MethodDocumentation]:
        """Parse a single method section from JavaDoc HTML."""
        # Extract method name from the h3 tag
        h3_tag = section.find('h3')
        if not h3_tag:
            return None
        
        method_name = h3_tag.get_text().strip()
        
        # Extract method signature
        signature_div = section.find('div', class_='member-signature')
        if not signature_div:
            return None
        
        signature_text = signature_div.get_text()
        
        # Parse modifiers, return type, and parameters from signature
        modifiers, return_type, parameters = self._parse_method_signature(signature_text)
        
        # Extract method description
        description = ""
        block_div = section.find('div', class_='block')
        if block_div:
            description = self.clean_javadoc_content(str(block_div))
        
        # Extract parameter documentation
        param_docs = self._extract_parameter_docs(section)
        
        # Extract return documentation
        return_desc = self._extract_return_docs(section)
        
        # Extract throws documentation
        throws_docs = self._extract_throws_docs(section)
        
        # Extract other metadata
        deprecated = self._is_method_deprecated(section)
        since_version = self._extract_method_since(section)
        see_also = self._extract_method_see_also(section)
        overrides = self._extract_overrides_info(section)
        
        # Extract code examples from description
        examples = self._extract_code_examples(block_div) if block_div else []
        
        return MethodDocumentation(
            name=method_name,
            signature=signature_text.strip(),
            description=description,
            parameters=param_docs,
            return_description=return_desc,
            return_type=return_type,
            examples=examples,
            deprecated=deprecated,
            since_version=since_version,
            see_also=see_also,
            throws=throws_docs,
            modifiers=modifiers,
            overrides=overrides
        )
    
    def _parse_method_signature(self, signature_text: str) -> tuple[List[str], str, List[str]]:
        """Parse method signature to extract modifiers, return type, and parameters."""
        # Clean up the signature text
        signature_text = re.sub(r'\s+', ' ', signature_text.strip())
        
        # Extract modifiers (public, private, static, etc.)
        modifiers = []
        modifier_pattern = r'\b(public|private|protected|static|final|abstract|synchronized|native|strictfp)\b'
        modifier_matches = re.findall(modifier_pattern, signature_text)
        modifiers.extend(modifier_matches)
        
        # Extract return type and method name
        # Pattern to match: [modifiers] return_type method_name(parameters)
        signature_pattern = r'(?:(?:public|private|protected|static|final|abstract|synchronized|native|strictfp)\s+)*(\S+)\s+(\w+)\s*\((.*?)\)'
        match = re.search(signature_pattern, signature_text)
        
        return_type = "void"
        parameters = []
        
        if match:
            return_type = match.group(1)
            param_text = match.group(3)
            
            # Parse parameters
            if param_text.strip():
                # Split parameters by comma, but be careful with generics
                param_parts = self._split_parameters(param_text)
                parameters = [p.strip() for p in param_parts if p.strip()]
        
        return modifiers, return_type, parameters
    
    def _split_parameters(self, param_text: str) -> List[str]:
        """Split parameter text by commas, handling generics properly."""
        parameters = []
        current_param = ""
        bracket_depth = 0
        
        for char in param_text:
            if char == '<':
                bracket_depth += 1
            elif char == '>':
                bracket_depth -= 1
            elif char == ',' and bracket_depth == 0:
                parameters.append(current_param.strip())
                current_param = ""
                continue
            
            current_param += char
        
        if current_param.strip():
            parameters.append(current_param.strip())
        
        return parameters
    
    def _extract_parameter_docs(self, section: Tag) -> List[ParameterDoc]:
        """Extract parameter documentation from method section."""
        param_docs = []
        
        # Look for parameter documentation in dl.notes
        notes_dl = section.find('dl', class_='notes')
        if notes_dl:
            # Find Parameters section
            dt_tags = notes_dl.find_all('dt')
            for dt in dt_tags:
                if dt.get_text().strip() == 'Parameters:':
                    # Get the next dd tag which contains parameter descriptions
                    dd = dt.find_next_sibling('dd')
                    if dd:
                        # Parameters are usually in code tags followed by descriptions
                        code_tags = dd.find_all('code')
                        for code_tag in code_tags:
                            param_name = code_tag.get_text().strip()
                            # Get description text after the code tag
                            description = ""
                            next_element = code_tag.next_sibling
                            while next_element and next_element.name != 'code':
                                if hasattr(next_element, 'get_text'):
                                    description += next_element.get_text()
                                elif isinstance(next_element, str):
                                    description += next_element
                                next_element = next_element.next_sibling
                            
                            description = self._normalize_formatting(description)
                            if description.startswith(' - '):
                                description = description[3:]
                            
                            param_docs.append(ParameterDoc(
                                name=param_name,
                                description=description.strip()
                            ))
        
        return param_docs
    
    def _extract_return_docs(self, section: Tag) -> str:
        """Extract return value documentation from method section."""
        notes_dl = section.find('dl', class_='notes')
        if notes_dl:
            dt_tags = notes_dl.find_all('dt')
            for dt in dt_tags:
                if dt.get_text().strip() == 'Returns:':
                    dd = dt.find_next_sibling('dd')
                    if dd:
                        return self.clean_javadoc_content(str(dd))
        return ""
    
    def _extract_throws_docs(self, section: Tag) -> Dict[str, str]:
        """Extract throws/exceptions documentation from method section."""
        throws_docs = {}
        
        notes_dl = section.find('dl', class_='notes')
        if notes_dl:
            dt_tags = notes_dl.find_all('dt')
            for dt in dt_tags:
                if dt.get_text().strip() == 'Throws:':
                    dd = dt.find_next_sibling('dd')
                    if dd:
                        # Throws documentation usually has code tags for exception types
                        code_tags = dd.find_all('code')
                        for code_tag in code_tags:
                            exception_type = code_tag.get_text().strip()
                            # Get description after the code tag
                            description = ""
                            next_element = code_tag.next_sibling
                            while next_element and next_element.name != 'code':
                                if hasattr(next_element, 'get_text'):
                                    description += next_element.get_text()
                                elif isinstance(next_element, str):
                                    description += next_element
                                next_element = next_element.next_sibling
                            
                            description = self._normalize_formatting(description)
                            if description.startswith(' - '):
                                description = description[3:]
                            
                            throws_docs[exception_type] = description.strip()
        
        return throws_docs
    
    def _is_method_deprecated(self, section: Tag) -> bool:
        """Check if method is deprecated."""
        # Look for @Deprecated annotation or deprecated text
        signature_div = section.find('div', class_='member-signature')
        if signature_div and '@Deprecated' in signature_div.get_text():
            return True
        
        # Check in notes section
        notes_dl = section.find('dl', class_='notes')
        if notes_dl:
            dt_tags = notes_dl.find_all('dt')
            for dt in dt_tags:
                if 'deprecated' in dt.get_text().lower():
                    return True
        
        return False
    
    def _extract_method_since(self, section: Tag) -> Optional[str]:
        """Extract @since version information from method section."""
        notes_dl = section.find('dl', class_='notes')
        if notes_dl:
            dt_tags = notes_dl.find_all('dt')
            for dt in dt_tags:
                if dt.get_text().strip() == 'Since:':
                    dd = dt.find_next_sibling('dd')
                    if dd:
                        return self._normalize_formatting(dd.get_text()).strip()
        return None
    
    def _extract_method_see_also(self, section: Tag) -> List[str]:
        """Extract @see also references from method section."""
        see_also = []
        
        notes_dl = section.find('dl', class_='notes')
        if notes_dl:
            dt_tags = notes_dl.find_all('dt')
            for dt in dt_tags:
                if dt.get_text().strip() == 'See Also:':
                    dd = dt.find_next_sibling('dd')
                    if dd:
                        # See also references are usually in links
                        links = dd.find_all('a')
                        for link in links:
                            see_also.append(link.get_text().strip())
        
        return see_also
    
    def _extract_overrides_info(self, section: Tag) -> Optional[str]:
        """Extract method override information."""
        notes_dl = section.find('dl', class_='notes')
        if notes_dl:
            dt_tags = notes_dl.find_all('dt')
            for dt in dt_tags:
                if dt.get_text().strip() == 'Overrides:':
                    dd = dt.find_next_sibling('dd')
                    if dd:
                        return self._normalize_formatting(dd.get_text()).strip()
        return None
    
    def _extract_code_examples(self, block_div: Tag) -> List[str]:
        """Extract code examples from method description."""
        examples = []
        
        # Look for <pre> tags which usually contain code examples
        pre_tags = block_div.find_all('pre')
        for pre in pre_tags:
            code_text = pre.get_text().strip()
            if code_text:
                examples.append(code_text)
        
        # Look for <code> blocks that might contain examples
        code_tags = block_div.find_all('code')
        for code in code_tags:
            code_text = code.get_text().strip()
            # Only include longer code snippets as examples
            if len(code_text) > 50 and '\n' in code_text:
                examples.append(code_text)
        
        return examples
    
    def _clean_html_content(self, raw_text: str) -> str:
        """Clean and normalize HTML content for documentation."""
        if not raw_text:
            return ""
        
        # Remove extra whitespace and normalize line breaks
        text = re.sub(r'\s+', ' ', raw_text.strip())
        
        # Remove common HTML artifacts
        text = text.replace('\u00a0', ' ')  # Non-breaking space
        text = text.replace('\n', ' ')
        text = text.replace('\r', ' ')
        
        # Clean up multiple spaces
        text = re.sub(r' +', ' ', text)
        
        return text.strip()
    
    def clean_javadoc_content(self, raw_html: str) -> str:
        """
        Advanced cleaning and normalization of JavaDoc HTML content.
        Handles special JavaDoc tags, preserves code examples, and normalizes formatting.
        """
        if not raw_html:
            return ""
        
        # Parse HTML to handle tags properly
        soup = BeautifulSoup(raw_html, 'html.parser')
        
        # Extract and preserve code examples before cleaning
        code_blocks = self._extract_and_preserve_code_blocks(soup)
        
        # Handle special JavaDoc tags
        cleaned_text = self._process_javadoc_tags(soup)
        
        # Normalize whitespace and formatting
        cleaned_text = self._normalize_formatting(cleaned_text)
        
        # Restore code examples
        cleaned_text = self._restore_code_blocks(cleaned_text, code_blocks)
        
        return cleaned_text
    
    def _extract_and_preserve_code_blocks(self, soup: BeautifulSoup) -> Dict[str, str]:
        """Extract and preserve code blocks during cleaning."""
        code_blocks = {}
        placeholder_counter = 0
        
        # Find all code-related tags
        code_tags = soup.find_all(['pre', 'code'])
        
        for tag in code_tags:
            # Only preserve multi-line code blocks or significant code snippets
            code_text = tag.get_text()
            if len(code_text) > 20 or '\n' in code_text:
                placeholder = f"__CODE_BLOCK_{placeholder_counter}__"
                code_blocks[placeholder] = code_text
                tag.replace_with(placeholder)
                placeholder_counter += 1
        
        return code_blocks
    
    def _process_javadoc_tags(self, soup: BeautifulSoup) -> str:
        """Process special JavaDoc tags (@param, @return, @deprecated, @since, etc.)."""
        text = soup.get_text()
        
        # Handle @param tags - these should already be processed in HTML structure, but we might find inline references
        text = re.sub(r'@param\s+(\w+)', r'Parameter \1:', text)
        
        # Handle @return tags
        text = re.sub(r'@return\s+', 'Returns: ', text)
        
        # Handle @deprecated tags
        text = re.sub(r'@deprecated\s+', 'Deprecated: ', text)
        
        # Handle @since tags
        text = re.sub(r'@since\s+', 'Since: ', text)
        
        # Handle @see tags
        text = re.sub(r'@see\s+', 'See: ', text)
        
        # Handle @throws/@exception tags
        text = re.sub(r'@(?:throws|exception)\s+(\w+)', r'Throws \1:', text)
        
        # Handle @author tags
        text = re.sub(r'@author\s+', 'Author: ', text)
        
        # Handle @version tags
        text = re.sub(r'@version\s+', 'Version: ', text)
        
        return text
    
    def _normalize_formatting(self, text: str) -> str:
        """Normalize whitespace, line breaks, and formatting."""
        if not text:
            return ""
        
        # Replace various whitespace characters with regular spaces
        text = re.sub(r'[\u00a0\u2000-\u200b\u2028\u2029]', ' ', text)
        
        # Normalize line breaks - preserve paragraph breaks but remove single line breaks
        text = re.sub(r'\n\s*\n', '\n\n', text)  # Preserve paragraph breaks
        text = re.sub(r'(?<!\n)\n(?!\n)', ' ', text)  # Convert single line breaks to spaces
        
        # Clean up multiple spaces
        text = re.sub(r' +', ' ', text)
        
        # Clean up multiple line breaks (max 2)
        text = re.sub(r'\n{3,}', '\n\n', text)
        
        # Remove leading/trailing whitespace from each line
        lines = text.split('\n')
        lines = [line.strip() for line in lines]
        text = '\n'.join(lines)
        
        # Remove empty lines at start and end
        text = text.strip()
        
        return text
    
    def _restore_code_blocks(self, text: str, code_blocks: Dict[str, str]) -> str:
        """Restore preserved code blocks to the cleaned text."""
        for placeholder, code_content in code_blocks.items():
            # Format code blocks nicely
            formatted_code = self._format_code_block(code_content)
            text = text.replace(placeholder, formatted_code)
        
        return text
    
    def _format_code_block(self, code_content: str) -> str:
        """Format a code block for documentation."""
        if not code_content:
            return ""
        
        # Clean up the code content
        code_content = code_content.strip()
        
        # If it's a single line, format as inline code
        if '\n' not in code_content and len(code_content) < 80:
            return f"`{code_content}`"
        
        # Multi-line code block
        lines = code_content.split('\n')
        # Remove common leading whitespace
        min_indent = float('inf')
        for line in lines:
            if line.strip():  # Skip empty lines
                indent = len(line) - len(line.lstrip())
                min_indent = min(min_indent, indent)
        
        if min_indent != float('inf') and min_indent > 0:
            lines = [line[min_indent:] if line.strip() else line for line in lines]
        
        formatted_code = '\n'.join(lines)
        return f"\n```\n{formatted_code}\n```\n"
    
    def extract_javadoc_metadata(self, soup: BeautifulSoup) -> Dict[str, Any]:
        """Extract metadata from JavaDoc tags and annotations."""
        metadata = {
            'deprecated': False,
            'since_version': None,
            'author': None,
            'version': None,
            'see_also': [],
            'annotations': []
        }
        
        # Look for deprecated information
        deprecated_elements = soup.find_all(text=re.compile(r'@deprecated|Deprecated', re.IGNORECASE))
        if deprecated_elements:
            metadata['deprecated'] = True
        
        # Look for @since information
        since_pattern = re.compile(r'@since\s+([\d.]+)', re.IGNORECASE)
        since_matches = soup.find_all(text=since_pattern)
        if since_matches:
            match = since_pattern.search(since_matches[0])
            if match:
                metadata['since_version'] = match.group(1)
        
        # Look for @author information
        author_pattern = re.compile(r'@author\s+(.+)', re.IGNORECASE)
        author_matches = soup.find_all(text=author_pattern)
        if author_matches:
            match = author_pattern.search(author_matches[0])
            if match:
                metadata['author'] = match.group(1).strip()
        
        # Look for @version information
        version_pattern = re.compile(r'@version\s+(.+)', re.IGNORECASE)
        version_matches = soup.find_all(text=version_pattern)
        if version_matches:
            match = version_pattern.search(version_matches[0])
            if match:
                metadata['version'] = match.group(1).strip()
        
        # Extract @see references
        see_links = soup.find_all('a')
        for link in see_links:
            href = link.get('href', '')
            text = link.get_text().strip()
            if text and (href or text.startswith('#')):
                metadata['see_also'].append(text)
        
        # Look for annotations (like @Override, @Deprecated)
        annotation_pattern = re.compile(r'@(\w+)', re.IGNORECASE)
        text_content = soup.get_text()
        annotations = annotation_pattern.findall(text_content)
        metadata['annotations'] = list(set(annotations))  # Remove duplicates
        
        return metadata
    
    def _extract_field_docs(self, soup: BeautifulSoup) -> List[FieldDocumentation]:
        """Extract field documentation from JavaDoc HTML."""
        fields = []
        
        # Find the field details section
        field_details = soup.find('section', {'class': 'field-details', 'id': 'field-detail'})
        if field_details:
            # Find all field detail sections
            field_sections = field_details.find_all('section', class_='detail')
            
            for section in field_sections:
                try:
                    field_doc = self._parse_field_section(section)
                    if field_doc:
                        fields.append(field_doc)
                except Exception as e:
                    self.logger.warning(f"Failed to parse field section: {e}")
                    continue
        
        # Also check for inherited fields in field summary
        field_summary = soup.find('section', {'class': 'field-summary', 'id': 'field-summary'})
        if field_summary:
            inherited_fields = self._extract_inherited_fields(field_summary)
            fields.extend(inherited_fields)
        
        return fields
    
    def _parse_field_section(self, section: Tag) -> Optional[FieldDocumentation]:
        """Parse a single field section from JavaDoc HTML."""
        # Extract field name from the h3 tag
        h3_tag = section.find('h3')
        if not h3_tag:
            return None
        
        field_name = h3_tag.get_text().strip()
        
        # Extract field signature
        signature_div = section.find('div', class_='member-signature')
        if not signature_div:
            return None
        
        signature_text = signature_div.get_text()
        
        # Parse modifiers and type from signature
        modifiers, type_name = self._parse_field_signature(signature_text)
        
        # Extract field description
        description = ""
        block_div = section.find('div', class_='block')
        if block_div:
            description = self.clean_javadoc_content(str(block_div))
        
        # Extract metadata
        deprecated = self._is_field_deprecated(section)
        since_version = self._extract_field_since(section)
        
        return FieldDocumentation(
            name=field_name,
            type_name=type_name,
            description=description,
            deprecated=deprecated,
            since_version=since_version,
            modifiers=modifiers
        )
    
    def _parse_field_signature(self, signature_text: str) -> tuple[List[str], str]:
        """Parse field signature to extract modifiers and type."""
        # Clean up the signature text
        signature_text = re.sub(r'\s+', ' ', signature_text.strip())
        
        # Extract modifiers
        modifiers = []
        modifier_pattern = r'\b(public|private|protected|static|final|volatile|transient)\b'
        modifier_matches = re.findall(modifier_pattern, signature_text)
        modifiers.extend(modifier_matches)
        
        # Extract type - usually the last word before the field name
        # Pattern: [modifiers] type field_name
        parts = signature_text.split()
        type_name = "Object"  # Default
        
        # Find the type (skip modifiers)
        for i, part in enumerate(parts):
            if part not in ['public', 'private', 'protected', 'static', 'final', 'volatile', 'transient']:
                type_name = part
                break
        
        return modifiers, type_name
    
    def _extract_inherited_fields(self, field_summary: Tag) -> List[FieldDocumentation]:
        """Extract inherited field information from field summary."""
        inherited_fields = []
        
        # Look for inherited fields sections
        inherited_sections = field_summary.find_all('div', class_='inherited-list')
        
        for section in inherited_sections:
            h3_tag = section.find('h3')
            if h3_tag and 'inherited' in h3_tag.get_text().lower():
                # Extract field names from code tags
                code_tags = section.find_all('code')
                for code_tag in code_tags:
                    links = code_tag.find_all('a')
                    for link in links:
                        field_name = link.get_text().strip()
                        if field_name:
                            inherited_fields.append(FieldDocumentation(
                                name=field_name,
                                type_name="inherited",
                                description=f"Inherited from {h3_tag.get_text()}",
                                deprecated=False,
                                since_version=None,
                                modifiers=["inherited"]
                            ))
        
        return inherited_fields
    
    def _is_field_deprecated(self, section: Tag) -> bool:
        """Check if field is deprecated."""
        signature_div = section.find('div', class_='member-signature')
        if signature_div and '@Deprecated' in signature_div.get_text():
            return True
        return False
    
    def _extract_field_since(self, section: Tag) -> Optional[str]:
        """Extract @since version information from field section."""
        notes_dl = section.find('dl', class_='notes')
        if notes_dl:
            dt_tags = notes_dl.find_all('dt')
            for dt in dt_tags:
                if dt.get_text().strip() == 'Since:':
                    dd = dt.find_next_sibling('dd')
                    if dd:
                        return self._normalize_formatting(dd.get_text()).strip()
        return None
    
    def _extract_constructor_docs(self, soup: BeautifulSoup) -> List[ConstructorDocumentation]:
        """Extract constructor documentation from JavaDoc HTML."""
        constructors = []
        
        # Find the constructor details section
        constructor_details = soup.find('section', {'class': 'constructor-details', 'id': 'constructor-detail'})
        if not constructor_details:
            self.logger.debug("No constructor details section found")
            return constructors
        
        # Find all constructor detail sections
        constructor_sections = constructor_details.find_all('section', class_='detail')
        
        for section in constructor_sections:
            try:
                constructor_doc = self._parse_constructor_section(section)
                if constructor_doc:
                    constructors.append(constructor_doc)
            except Exception as e:
                self.logger.warning(f"Failed to parse constructor section: {e}")
                continue
        
        return constructors
    
    def _parse_constructor_section(self, section: Tag) -> Optional[ConstructorDocumentation]:
        """Parse a single constructor section from JavaDoc HTML."""
        # Extract constructor signature
        signature_div = section.find('div', class_='member-signature')
        if not signature_div:
            return None
        
        signature_text = signature_div.get_text()
        
        # Parse modifiers and parameters from signature
        modifiers, parameters = self._parse_constructor_signature(signature_text)
        
        # Extract constructor description
        description = ""
        block_div = section.find('div', class_='block')
        if block_div:
            description = self.clean_javadoc_content(str(block_div))
        
        # Extract parameter documentation
        param_docs = self._extract_parameter_docs(section)
        
        # Extract throws documentation
        throws_docs = self._extract_throws_docs(section)
        
        # Extract metadata
        deprecated = self._is_method_deprecated(section)  # Reuse method logic
        since_version = self._extract_method_since(section)  # Reuse method logic
        
        return ConstructorDocumentation(
            signature=signature_text.strip(),
            description=description,
            parameters=param_docs,
            throws=throws_docs,
            deprecated=deprecated,
            since_version=since_version,
            modifiers=modifiers
        )
    
    def _parse_constructor_signature(self, signature_text: str) -> tuple[List[str], List[str]]:
        """Parse constructor signature to extract modifiers and parameters."""
        # Clean up the signature text
        signature_text = re.sub(r'\s+', ' ', signature_text.strip())
        
        # Extract modifiers
        modifiers = []
        modifier_pattern = r'\b(public|private|protected)\b'
        modifier_matches = re.findall(modifier_pattern, signature_text)
        modifiers.extend(modifier_matches)
        
        # Extract parameters from parentheses
        param_match = re.search(r'\((.*?)\)', signature_text)
        parameters = []
        
        if param_match:
            param_text = param_match.group(1)
            if param_text.strip():
                # Split parameters by comma, handling generics
                param_parts = self._split_parameters(param_text)
                parameters = [p.strip() for p in param_parts if p.strip()]
        
        return modifiers, parameters
    
    def _extract_nested_classes(self, soup: BeautifulSoup) -> List[str]:
        """Extract nested class information."""
        nested_classes = []
        
        # Find the nested class summary section
        nested_summary = soup.find('section', {'class': 'nested-class-summary', 'id': 'nested-class-summary'})
        if nested_summary:
            # Look for class names in the summary table
            summary_table = nested_summary.find('div', class_='summary-table')
            if summary_table:
                # Find all class links
                class_links = summary_table.find_all('a', class_='type-name-link')
                for link in class_links:
                    class_name = link.get_text().strip()
                    if class_name:
                        nested_classes.append(class_name)
        
        return nested_classes
    
    def _is_deprecated(self, soup: BeautifulSoup) -> bool:
        """Check if class is deprecated."""
        # Look for @Deprecated annotation in class signature
        type_signature = soup.find('div', class_='type-signature')
        if type_signature and '@Deprecated' in type_signature.get_text():
            return True
        
        # Look for deprecated text in class description
        block_divs = soup.find_all('div', class_='block')
        for block in block_divs:
            if 'deprecated' in block.get_text().lower():
                return True
        
        # Check for deprecated in notes
        notes_sections = soup.find_all('dl', class_='notes')
        for notes in notes_sections:
            dt_tags = notes.find_all('dt')
            for dt in dt_tags:
                if 'deprecated' in dt.get_text().lower():
                    return True
        
        return False
    
    def _extract_since_version(self, soup: BeautifulSoup) -> Optional[str]:
        """Extract @since version information from class."""
        # Look for @since in class-level notes
        notes_sections = soup.find_all('dl', class_='notes')
        for notes in notes_sections:
            dt_tags = notes.find_all('dt')
            for dt in dt_tags:
                if dt.get_text().strip() == 'Since:':
                    dd = dt.find_next_sibling('dd')
                    if dd:
                        return self._normalize_formatting(dd.get_text()).strip()
        
        # Look for @since in text content
        text_content = soup.get_text()
        since_match = re.search(r'@since\s+([\d.]+)', text_content, re.IGNORECASE)
        if since_match:
            return since_match.group(1)
        
        return None
    
    def _extract_see_also(self, soup: BeautifulSoup) -> List[str]:
        """Extract @see also references from class."""
        see_also = []
        
        # Look for @see in class-level notes
        notes_sections = soup.find_all('dl', class_='notes')
        for notes in notes_sections:
            dt_tags = notes.find_all('dt')
            for dt in dt_tags:
                if dt.get_text().strip() == 'See Also:':
                    dd = dt.find_next_sibling('dd')
                    if dd:
                        # See also references are usually in links
                        links = dd.find_all('a')
                        for link in links:
                            see_also.append(link.get_text().strip())
        
        # Look for related class links in inheritance section
        inheritance_info = self._extract_inheritance_info(soup)
        see_also.extend(inheritance_info.get('extends', []))
        see_also.extend(inheritance_info.get('implements', []))
        
        return list(set(see_also))  # Remove duplicates
    
    def validate_parsing(self, class_doc: ClassDocumentation) -> Dict[str, Any]:
        """
        Validate the completeness and quality of parsed documentation.
        
        Returns:
            Dictionary with validation results and statistics
        """
        validation = {
            'valid': True,
            'warnings': [],
            'statistics': {
                'methods_with_descriptions': 0,
                'methods_with_parameters': 0,
                'methods_with_return_docs': 0,
                'constructors_with_descriptions': 0,
                'fields_with_descriptions': 0,
                'total_methods': len(class_doc.methods),
                'total_constructors': len(class_doc.constructors),
                'total_fields': len(class_doc.fields)
            }
        }
        
        # Validate class description
        if not class_doc.description.strip():
            validation['warnings'].append("Class has no description")
        
        # Validate methods
        for method in class_doc.methods:
            if method.description.strip():
                validation['statistics']['methods_with_descriptions'] += 1
            
            if method.parameters:
                validation['statistics']['methods_with_parameters'] += 1
                # Check if parameters have descriptions
                for param in method.parameters:
                    if not param.description.strip():
                        validation['warnings'].append(f"Method {method.name} parameter {param.name} has no description")
            
            if method.return_description.strip():
                validation['statistics']['methods_with_return_docs'] += 1
        
        # Validate constructors
        for constructor in class_doc.constructors:
            if constructor.description.strip():
                validation['statistics']['constructors_with_descriptions'] += 1
        
        # Validate fields
        for field in class_doc.fields:
            if field.description.strip():
                validation['statistics']['fields_with_descriptions'] += 1
        
        # Calculate completion percentages
        if validation['statistics']['total_methods'] > 0:
            method_desc_pct = (validation['statistics']['methods_with_descriptions'] / 
                             validation['statistics']['total_methods']) * 100
            validation['statistics']['method_description_percentage'] = round(method_desc_pct, 1)
        
        if validation['statistics']['total_constructors'] > 0:
            constructor_desc_pct = (validation['statistics']['constructors_with_descriptions'] / 
                                  validation['statistics']['total_constructors']) * 100
            validation['statistics']['constructor_description_percentage'] = round(constructor_desc_pct, 1)
        
        # Set overall validity
        if len(validation['warnings']) > 10:  # Too many warnings
            validation['valid'] = False
        
        return validation