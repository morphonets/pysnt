"""
Docstring enhancement system for integrating JavaDoc into existing Python classes.

This module provides tools to enhance existing Python class docstrings with 
rich JavaDoc information while preserving the existing structure and patterns.
"""

import ast
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Any

from .config import config
from .logging_setup import get_logger

logger = get_logger('docstring_enhancer')


@dataclass
class EnhancedDocstring:
    """Enhanced docstring with JavaDoc integration."""
    original_docstring: str
    enhanced_docstring: str
    class_name: str
    package: str
    javadoc_description: str
    key_methods: List[Dict[str, str]]
    usage_examples: List[str]
    see_also_links: List[str]


class DocstringEnhancer:
    """Enhances existing Python docstrings with JavaDoc information."""
    
    def __init__(self):
        """Initialize the docstring enhancer."""
        self.logger = logger
        self.src_dir = config.project_root / "src"
        self.enhanced_json_dir = config.get_path('output.docs_dir') / 'enhanced_json'
        
        # Load enhanced JSON data
        self.enhanced_data = self._load_enhanced_json_data()
    
    def _load_enhanced_json_data(self) -> Dict[str, Any]:
        """Load enhanced JSON data for all classes."""
        enhanced_data = {}
        
        if not self.enhanced_json_dir.exists():
            self.logger.warning(f"Enhanced JSON directory not found: {self.enhanced_json_dir}")
            return enhanced_data
        
        for json_file in self.enhanced_json_dir.glob("*_enhanced.json"):
            try:
                import json
                with open(json_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                
                class_name = data.get('class_name', json_file.stem.replace('_enhanced', ''))
                enhanced_data[class_name] = data
                
            except Exception as e:
                self.logger.warning(f"Failed to load {json_file}: {e}")
        
        self.logger.info(f"Loaded enhanced data for {len(enhanced_data)} classes")
        return enhanced_data
    
    def enhance_python_file(self, python_file: Path, dry_run: bool = False) -> Dict[str, Any]:
        """
        Enhance docstrings in a Python file with JavaDoc information.
        
        Args:
            python_file: Path to the Python file to enhance
            dry_run: If True, don't modify files, just return what would be changed
            
        Returns:
            Dictionary with enhancement results
        """
        self.logger.info(f"Enhancing docstrings in {python_file}")
        
        try:
            # Read the file
            with open(python_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Parse the AST to find classes
            tree = ast.parse(content)
            
            # Find class definitions and their docstrings
            enhancements = []
            modified_content = content
            
            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef):
                    class_name = node.name
                    
                    # Check if we have enhanced data for this class
                    if class_name in self.enhanced_data:
                        enhancement = self._enhance_class_docstring(
                            class_name, 
                            content, 
                            node,
                            self.enhanced_data[class_name]
                        )
                        
                        if enhancement:
                            enhancements.append(enhancement)
                            # Apply the enhancement to the content
                            modified_content = modified_content.replace(
                                enhancement.original_docstring,
                                enhancement.enhanced_docstring
                            )
            
            # Write the enhanced content if not dry run
            if not dry_run and enhancements:
                with open(python_file, 'w', encoding='utf-8') as f:
                    f.write(modified_content)
                
                self.logger.info(f"Enhanced {len(enhancements)} docstrings in {python_file}")
            
            return {
                'file': str(python_file),
                'enhancements': len(enhancements),
                'enhanced_classes': [e.class_name for e in enhancements],
                'dry_run': dry_run
            }
            
        except Exception as e:
            self.logger.error(f"Failed to enhance {python_file}: {e}")
            return {
                'file': str(python_file),
                'error': str(e),
                'enhancements': 0
            }
    
    def _enhance_class_docstring(self, class_name: str, file_content: str, 
                               class_node: ast.ClassDef, enhanced_data: Dict[str, Any]) -> Optional[EnhancedDocstring]:
        """Enhance a single class docstring."""
        
        # Extract the original docstring
        original_docstring = self._extract_docstring_from_content(file_content, class_node)
        if not original_docstring:
            return None
        
        # Get JavaDoc information
        javadoc_description = enhanced_data.get('javadoc_description', '')
        methods = enhanced_data.get('methods', [])
        
        # Generate key methods summary
        key_methods = self._generate_key_methods_summary(methods)
        
        # Generate usage examples
        usage_examples = self._generate_usage_examples(class_name, methods)
        
        # Create enhanced docstring
        enhanced_docstring = self._create_enhanced_docstring(
            original_docstring,
            class_name,
            enhanced_data.get('package', ''),
            javadoc_description,
            key_methods,
            usage_examples
        )
        
        return EnhancedDocstring(
            original_docstring=original_docstring,
            enhanced_docstring=enhanced_docstring,
            class_name=class_name,
            package=enhanced_data.get('package', ''),
            javadoc_description=javadoc_description,
            key_methods=key_methods,
            usage_examples=usage_examples,
            see_also_links=[]
        )
    
    def _extract_docstring_from_content(self, content: str, class_node: ast.ClassDef) -> Optional[str]:
        """Extract the docstring from file content using AST node information."""
        lines = content.split('\n')
        
        # Find the class definition line
        class_line = class_node.lineno - 1  # AST uses 1-based line numbers
        
        # Look for docstring after class definition
        for i in range(class_line + 1, min(class_line + 20, len(lines))):
            line = lines[i].strip()
            if line.startswith('"""') or line.startswith("'''"):
                # Found start of docstring, extract it
                quote_type = '"""' if line.startswith('"""') else "'''"
                
                # Single line docstring
                if line.count(quote_type) >= 2:
                    return line
                
                # Multi-line docstring
                docstring_lines = [line]
                for j in range(i + 1, len(lines)):
                    docstring_lines.append(lines[j])
                    if quote_type in lines[j]:
                        break
                
                return '\n'.join(docstring_lines)
        
        return None
    
    def _generate_key_methods_summary(self, methods: List[Dict[str, Any]]) -> List[Dict[str, str]]:
        """Generate a summary of key methods from enhanced method data."""
        key_methods = []
        
        # Sort methods by category and importance
        categorized_methods = {}
        for method in methods:
            category = method.get('category', 'Utilities')
            if category not in categorized_methods:
                categorized_methods[category] = []
            categorized_methods[category].append(method)
        
        # Select key methods from each category
        priority_categories = ['Analysis', 'I/O Operations', 'Visualization', 'Getters', 'Setters']
        
        for category in priority_categories:
            if category in categorized_methods:
                # Take top 2-3 methods from each important category
                for method in categorized_methods[category][:2]:
                    if method.get('javadoc_description'):
                        signature = self._get_method_signature(method)
                        description = method.get('javadoc_description', '').split('.')[0] + '.'
                        
                        key_methods.append({
                            'signature': signature,
                            'description': description
                        })
        
        # Add a few utility methods if we don't have enough
        if len(key_methods) < 5 and 'Utilities' in categorized_methods:
            for method in categorized_methods['Utilities'][:3]:
                if len(key_methods) >= 8:  # Limit total methods
                    break
                    
                signature = self._get_method_signature(method)
                description = method.get('javadoc_description', method.get('documentation', ''))
                if description:
                    description = description.split('.')[0] + '.'
                    key_methods.append({
                        'signature': signature,
                        'description': description
                    })
        
        return key_methods[:8]  # Limit to 8 key methods
    
    def _get_method_signature(self, method: Dict[str, Any]) -> str:
        """Extract a clean method signature."""
        overloads = method.get('overloads', [])
        if overloads:
            signature = overloads[0].get('signature', '')
            # Clean up the signature for display
            if ' -> ' in signature:
                # Extract just the method part (before the return type)
                signature = signature.split(' -> ')[0]
            # Extract the parameters part (everything after the first '(')
            if '(' in signature:
                params_part = signature.split('(', 1)[1]
                return f"``{method.get('name', '')}({params_part}``"
            return f"``{method.get('name', '')}()``"
        
        return f"``{method.get('name', '')}()``"
    
    def _generate_usage_examples(self, class_name: str, methods: List[Dict[str, Any]]) -> List[str]:
        """Generate usage examples for the class."""
        examples = []
        
        # Look for methods with existing examples
        for method in methods:
            method_examples = method.get('examples', [])
            if method_examples:
                for example in method_examples[:2]:  # Limit examples
                    if example.strip():
                        examples.append(example.strip())
        
        # If no examples found, generate basic ones
        if not examples:
            # Generate basic instantiation example
            examples.append(f"{class_name.lower()} = {class_name}()")
            
            # Add a method call example if we have methods
            if methods:
                first_method = methods[0]
                method_name = first_method.get('name', 'method')
                examples.append(f"result = {class_name.lower()}.{method_name}()")
        
        return examples[:3]  # Limit to 3 examples
    
    def _create_enhanced_docstring(self, original_docstring: str, class_name: str, 
                                 package: str, javadoc_description: str,
                                 key_methods: List[Dict[str, str]], 
                                 usage_examples: List[str]) -> str:
        """Create the enhanced docstring."""
        
        # Parse the original docstring to preserve existing structure
        lines = original_docstring.split('\n')
        
        # Find where to insert enhanced content
        # Look for the JavaDoc link section
        javadoc_link_index = -1
        for i, line in enumerate(lines):
            if 'See `' in line and '_javadoc`_' in line:
                javadoc_link_index = i
                break
        
        # Build enhanced content
        enhanced_sections = []
        
        # Add JavaDoc description if available
        if javadoc_description and javadoc_description.strip():
            enhanced_sections.append("    **JavaDoc Description**:")
            enhanced_sections.append(f"    {javadoc_description}")
            enhanced_sections.append("")
        
        # Add key methods if available
        if key_methods:
            enhanced_sections.append("    **Key Methods**:")
            enhanced_sections.append("")
            for method in key_methods:
                enhanced_sections.append(f"    * {method['signature']} - {method['description']}")
            enhanced_sections.append("")
        
        # Add usage examples if available
        if usage_examples:
            enhanced_sections.append("    **Usage Examples**:")
            enhanced_sections.append("")
            enhanced_sections.append("    .. code-block:: python")
            enhanced_sections.append("")
            for example in usage_examples:
                enhanced_sections.append(f"        {example}")
            enhanced_sections.append("")
        
        # Insert enhanced content before JavaDoc link
        if javadoc_link_index > 0 and enhanced_sections:
            # Insert enhanced content before the JavaDoc link
            enhanced_lines = (
                lines[:javadoc_link_index] + 
                enhanced_sections + 
                lines[javadoc_link_index:]
            )
        else:
            # Append enhanced content before the closing quotes
            closing_quote_index = -1
            for i in range(len(lines) - 1, -1, -1):
                if '"""' in lines[i] or "'''" in lines[i]:
                    closing_quote_index = i
                    break
            
            if closing_quote_index > 0 and enhanced_sections:
                enhanced_lines = (
                    lines[:closing_quote_index] + 
                    enhanced_sections + 
                    lines[closing_quote_index:]
                )
            else:
                enhanced_lines = lines
        
        return '\n'.join(enhanced_lines)
    
    def enhance_all_python_files(self, dry_run: bool = False) -> Dict[str, Any]:
        """Enhance all Python files in the source directory."""
        results = {
            'files_processed': 0,
            'files_enhanced': 0,
            'total_enhancements': 0,
            'enhanced_files': [],
            'errors': []
        }
        
        # Find all Python files in the source directory
        python_files = list(self.src_dir.rglob("*.py"))
        
        for python_file in python_files:
            # Skip __pycache__ and other non-source files
            if '__pycache__' in str(python_file) or '.pyc' in str(python_file):
                continue
            
            results['files_processed'] += 1
            
            try:
                file_result = self.enhance_python_file(python_file, dry_run)
                
                if file_result.get('enhancements', 0) > 0:
                    results['files_enhanced'] += 1
                    results['total_enhancements'] += file_result['enhancements']
                    results['enhanced_files'].append(file_result)
                
                if 'error' in file_result:
                    results['errors'].append(file_result)
                    
            except Exception as e:
                self.logger.error(f"Error processing {python_file}: {e}")
                results['errors'].append({
                    'file': str(python_file),
                    'error': str(e)
                })
        
        self.logger.info(f"Enhanced {results['files_enhanced']} files with {results['total_enhancements']} total enhancements")
        return results


def main():
    """Main entry point for docstring enhancement."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Enhance Python docstrings with JavaDoc information')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be changed without modifying files')
    parser.add_argument('--file', type=Path, help='Enhance a specific file')
    parser.add_argument('--verbose', '-v', action='store_true', help='Enable verbose logging')
    
    args = parser.parse_args()
    
    if args.verbose:
        import logging
        logging.getLogger('docstring_enhancer').setLevel(logging.DEBUG)
    
    enhancer = DocstringEnhancer()
    
    if args.file:
        result = enhancer.enhance_python_file(args.file, args.dry_run)
        print(f"Enhanced {result.get('enhancements', 0)} docstrings in {args.file}")
    else:
        results = enhancer.enhance_all_python_files(args.dry_run)
        print(f"Processed {results['files_processed']} files")
        print(f"Enhanced {results['files_enhanced']} files with {results['total_enhancements']} total enhancements")
        
        if results['errors']:
            print(f"Encountered {len(results['errors'])} errors")


if __name__ == "__main__":
    main()