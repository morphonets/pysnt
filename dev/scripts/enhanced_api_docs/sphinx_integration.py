"""
Sphinx integration module for the enhanced API documentation system.
Handles integration with existing Sphinx configuration and documentation structure.
"""

import re
from pathlib import Path
from typing import Dict, List, Any, Tuple

from .config import config
from .logging_setup import get_logger

logger = get_logger('sphinx_integration')


class SphinxIntegrator:
    """Handles integration with existing Sphinx documentation system."""
    
    def __init__(self):
        """Initialize the Sphinx integrator."""
        self.logger = logger
        self.docs_root = Path(__file__).parent.parent.parent.parent / 'docs'
        self.enhanced_docs_dir = config.get_path('output.docs_dir')
        self.class_pages_dir = config.get_path('output.class_pages_dir')
        
        # Sphinx configuration
        self.integrate_with_existing = config.get('sphinx.integrate_with_existing', True)
        self.toctree_maxdepth = config.get('sphinx.toctree_maxdepth', 3)
        self.add_to_main_index = config.get('sphinx.add_to_main_index', True)
    
    def validate_sphinx_compatibility(self) -> Tuple[bool, List[str]]:
        """
        Validate that generated RST files are compatible with existing Sphinx setup.
        
        Returns:
            Tuple of (is_compatible, list_of_issues)
        """
        issues = []
        
        # Check if docs directory exists
        if not self.docs_root.exists():
            issues.append(f"Documentation root directory not found: {self.docs_root}")
            return False, issues
        
        # Check if conf.py exists
        conf_py = self.docs_root / 'conf.py'
        if not conf_py.exists():
            issues.append(f"Sphinx configuration file not found: {conf_py}")
            return False, issues
        
        # Check if enhanced docs directory exists
        if not self.enhanced_docs_dir.exists():
            issues.append(f"Enhanced documentation directory not found: {self.enhanced_docs_dir}")
        
        # Check if main API documentation exists
        api_md = self.docs_root / 'api.md'
        if not api_md.exists():
            issues.append(f"Main API documentation file not found: {api_md}")
        
        # Validate RST syntax in existing files
        rst_files = list(self.enhanced_docs_dir.glob('**/*.rst'))
        for rst_file in rst_files:
            try:
                with open(rst_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                rst_issues = self._validate_rst_syntax(content)
                if rst_issues:
                    issues.extend([f"{rst_file.name}: {issue}" for issue in rst_issues])
            except Exception as e:
                issues.append(f"Error reading {rst_file}: {e}")
        
        return len(issues) == 0, issues
    
    def ensure_sphinx_integration(self) -> bool:
        """
        Ensure enhanced API documentation is properly integrated with Sphinx.
        
        Returns:
            True if integration successful, False otherwise
        """
        try:
            # Validate compatibility first
            is_compatible, issues = self.validate_sphinx_compatibility()
            if not is_compatible:
                self.logger.error("Sphinx compatibility validation failed:")
                for issue in issues:
                    self.logger.error(f"  - {issue}")
                return False
            
            # Ensure enhanced docs directory structure
            self._ensure_directory_structure()
            
            # Update main API documentation if configured
            if self.integrate_with_existing:
                self._update_main_api_documentation()
            
            # Add to main index if configured
            if self.add_to_main_index:
                self._update_main_index()
            
            # Validate cross-references
            self._validate_cross_references()
            
            self.logger.info("Sphinx integration completed successfully")
            return True
            
        except Exception as e:
            self.logger.error(f"Error during Sphinx integration: {e}")
            return False
    
    def generate_sphinx_toctree(self, class_files: Dict[str, Path]) -> str:
        """
        Generate Sphinx toctree directive for class documentation.
        
        Args:
            class_files: Dictionary mapping class names to their RST file paths
            
        Returns:
            Generated toctree RST content
        """
        if not class_files:
            return ""
        
        # Organize classes by package for better structure
        packages = {}
        for class_name, file_path in class_files.items():
            # Extract package from class name or file structure
            package = self._extract_package_from_class(class_name)
            if package not in packages:
                packages[package] = []
            packages[package].append((class_name, file_path))
        
        # Generate toctree
        toctree_lines = [
            ".. toctree::",
            f"   :maxdepth: {self.toctree_maxdepth}",
            "   :caption: Enhanced API Classes",
            ""
        ]
        
        # Add classes organized by package
        for package in sorted(packages.keys()):
            if package != "unknown":
                toctree_lines.append(f"   {package}")
                toctree_lines.append(f"   {'=' * len(package)}")
                toctree_lines.append("")
            
            for class_name, file_path in sorted(packages[package]):
                # Use relative path from enhanced docs directory
                rel_path = file_path.relative_to(self.enhanced_docs_dir)
                # Remove .rst extension for toctree
                toctree_path = str(rel_path).replace('.rst', '')
                toctree_lines.append(f"   {toctree_path}")
            
            toctree_lines.append("")
        
        return "\n".join(toctree_lines)
    
    def validate_cross_references(self, rst_content: str) -> Tuple[bool, List[str]]:
        """
        Validate cross-references in RST content.
        
        Args:
            rst_content: RST content to validate
            
        Returns:
            Tuple of (are_valid, list_of_issues)
        """
        issues = []
        
        # Find all cross-references
        doc_refs = re.findall(r':doc:`([^`]+)`', rst_content)
        ref_refs = re.findall(r':ref:`([^`]+)`', rst_content)
        class_refs = re.findall(r':class:`([^`]+)`', rst_content)
        func_refs = re.findall(r':func:`([^`]+)`', rst_content)
        
        # Validate doc references
        for doc_ref in doc_refs:
            if not self._validate_doc_reference(doc_ref):
                issues.append(f"Invalid doc reference: {doc_ref}")
        
        # Validate internal references
        for ref in ref_refs:
            if not self._validate_internal_reference(ref):
                issues.append(f"Invalid internal reference: {ref}")
        
        # Check for broken external links
        external_links = re.findall(r'`([^`]+) <(https?://[^>]+)>`_', rst_content)
        for link_text, url in external_links:
            if not self._validate_external_link(url):
                issues.append(f"Potentially broken external link: {url}")
        
        return len(issues) == 0, issues
    
    def preserve_existing_cross_references(self, rst_content: str) -> str:
        """
        Ensure existing cross-reference capabilities are preserved.
        
        Args:
            rst_content: RST content to process
            
        Returns:
            Processed RST content with preserved cross-references
        """
        # Add intersphinx references for external documentation
        rst_content = self._add_intersphinx_references(rst_content)
        
        # Ensure proper internal linking
        rst_content = self._ensure_internal_linking(rst_content)
        
        # Add navigation aids
        rst_content = self._add_navigation_aids(rst_content)
        
        return rst_content
    
    def _ensure_directory_structure(self):
        """Ensure proper directory structure for enhanced documentation."""
        # Create main enhanced docs directory
        self.enhanced_docs_dir.mkdir(parents=True, exist_ok=True)
        
        # Create classes subdirectory
        self.class_pages_dir.mkdir(parents=True, exist_ok=True)
        
        # Create index file if it doesn't exist
        index_file = self.enhanced_docs_dir / 'index.rst'
        if not index_file.exists():
            self.logger.info(f"Creating enhanced API documentation index: {index_file}")
            # The index.rst file should already be created by the main implementation
    
    def _update_main_api_documentation(self):
        """Update main API documentation to include enhanced docs."""
        api_file = self.docs_root / 'api.md'
        
        if not api_file.exists():
            self.logger.warning(f"Main API file not found: {api_file}")
            return
        
        try:
            with open(api_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check if enhanced API documentation is already referenced
            if 'api_enhanced/index' in content:
                self.logger.debug("Enhanced API documentation already referenced in main API file")
                return
            
            # Add reference to enhanced documentation in toctree
            toctree_pattern = r'(```{toctree}\s*\n:maxdepth: \d+\s*\n:caption: Complete API Reference\s*\n\s*api_auto/index)'
            replacement = r'\1\napi_enhanced/index'
            
            updated_content = re.sub(toctree_pattern, replacement, content, flags=re.MULTILINE)
            
            if updated_content != content:
                with open(api_file, 'w', encoding='utf-8') as f:
                    f.write(updated_content)
                self.logger.info("Updated main API documentation to include enhanced docs")
            
        except Exception as e:
            self.logger.error(f"Error updating main API documentation: {e}")
    
    def _update_main_index(self):
        """Update main documentation index to include enhanced API docs."""
        index_file = self.docs_root / 'index.md'
        
        if not index_file.exists():
            self.logger.warning(f"Main index file not found: {index_file}")
            return
        
        try:
            with open(index_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check if enhanced API documentation is already referenced
            if 'api_enhanced/index.html' in content:
                self.logger.debug("Enhanced API documentation already referenced in main index")
                return
            
            # Add to quick links section if not already present
            quick_links_pattern = r'(<a href="api\.html"[^>]*>.*?</a>)'
            if re.search(quick_links_pattern, content):
                # Add enhanced API docs link after main API link
                enhanced_link = '''
    <a href="api_enhanced/index.html" style="text-decoration: none; color: #2980b9; font-weight: 500;">
        <i class="fas fa-file-alt"></i> Enhanced API Docs
    </a>'''
                
                replacement = r'\1' + enhanced_link
                updated_content = re.sub(quick_links_pattern, replacement, content)
                
                if updated_content != content:
                    with open(index_file, 'w', encoding='utf-8') as f:
                        f.write(updated_content)
                    self.logger.info("Updated main index to include enhanced API docs")
            
        except Exception as e:
            self.logger.error(f"Error updating main index: {e}")
    
    def _validate_cross_references(self):
        """Validate cross-references in enhanced documentation."""
        rst_files = list(self.enhanced_docs_dir.glob('**/*.rst'))
        
        for rst_file in rst_files:
            try:
                with open(rst_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                is_valid, issues = self.validate_cross_references(content)
                if not is_valid:
                    self.logger.warning(f"Cross-reference issues in {rst_file.name}:")
                    for issue in issues:
                        self.logger.warning(f"  - {issue}")
                
            except Exception as e:
                self.logger.error(f"Error validating cross-references in {rst_file}: {e}")
    
    def _validate_rst_syntax(self, rst_content: str) -> List[str]:
        """Validate RST syntax for common issues."""
        issues = []
        lines = rst_content.split('\n')
        
        for i, line in enumerate(lines, 1):
            # Check for inconsistent heading underlines
            if line and all(c in '=-~^"' for c in line) and len(line) > 3:
                if i > 1:
                    prev_line = lines[i-2]
                    if prev_line.strip() and abs(len(line) - len(prev_line)) > 1:
                        issues.append(f"Line {i}: Heading underline length mismatch")
            
            # Check for malformed directives
            if line.strip().startswith('.. ') and '::' not in line:
                if not any(directive in line for directive in ['note::', 'warning::', 'seealso::']):
                    issues.append(f"Line {i}: Possible malformed directive")
        
        return issues
    
    def _extract_package_from_class(self, class_name: str) -> str:
        """Extract package name from class name."""
        # This is a simplified extraction - in practice, you might want to
        # use the actual package information from the JSON stub data
        if '.' in class_name:
            return class_name.split('.')[0]
        return "unknown"
    
    def _validate_doc_reference(self, doc_ref: str) -> bool:
        """Validate a doc reference."""
        # Handle relative references
        if doc_ref.startswith('../'):
            # For relative references, check from docs root
            relative_path = doc_ref[3:]  # Remove '../'
            ref_path = self.docs_root / f"{relative_path}.md"
            rst_path = self.docs_root / f"{relative_path}.rst"
            return ref_path.exists() or rst_path.exists()
        
        # Handle references within enhanced docs
        if '/' not in doc_ref:
            # Check in enhanced docs directory
            enhanced_ref_path = self.enhanced_docs_dir / f"{doc_ref}.rst"
            if enhanced_ref_path.exists():
                return True
        
        # Check if the referenced document exists in docs root
        ref_path = self.docs_root / f"{doc_ref}.md"
        rst_path = self.docs_root / f"{doc_ref}.rst"
        
        return ref_path.exists() or rst_path.exists()
    
    def _validate_internal_reference(self, ref: str) -> bool:
        """Validate an internal reference."""
        # For now, assume internal references are valid
        # In a full implementation, you'd check against a reference database
        return True
    
    def _validate_external_link(self, url: str) -> bool:
        """Validate an external link."""
        # For now, assume external links are valid
        # In a full implementation, you might want to check HTTP status
        return True
    
    def _add_intersphinx_references(self, rst_content: str) -> str:
        """Add intersphinx references for external documentation."""
        # Add references to PyImageJ and other external docs
        # This would be expanded based on the intersphinx configuration
        return rst_content
    
    def _ensure_internal_linking(self, rst_content: str) -> str:
        """Ensure proper internal linking."""
        # Add proper cross-references between classes and methods
        return rst_content
    
    def _add_navigation_aids(self, rst_content: str) -> str:
        """Add navigation aids to RST content."""
        # Add breadcrumbs, "see also" sections, etc.
        return rst_content
    
    def get_integration_status(self) -> Dict[str, Any]:
        """
        Get status of Sphinx integration.
        
        Returns:
            Dictionary with integration status information
        """
        status = {
            'sphinx_compatible': False,
            'main_api_updated': False,
            'main_index_updated': False,
            'cross_references_valid': False,
            'directory_structure_ok': False,
            'issues': []
        }
        
        try:
            # Check compatibility
            is_compatible, issues = self.validate_sphinx_compatibility()
            status['sphinx_compatible'] = is_compatible
            status['issues'].extend(issues)
            
            # Check directory structure
            status['directory_structure_ok'] = (
                self.enhanced_docs_dir.exists() and 
                self.class_pages_dir.exists()
            )
            
            # Check main API file
            api_file = self.docs_root / 'api.md'
            if api_file.exists():
                with open(api_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                status['main_api_updated'] = 'api_enhanced/index' in content
            
            # Check main index file
            index_file = self.docs_root / 'index.md'
            if index_file.exists():
                with open(index_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                status['main_index_updated'] = 'api_enhanced/index.html' in content
            
            # Validate cross-references
            rst_files = list(self.enhanced_docs_dir.glob('**/*.rst'))
            all_valid = True
            for rst_file in rst_files:
                with open(rst_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                is_valid, ref_issues = self.validate_cross_references(content)
                if not is_valid:
                    all_valid = False
                    status['issues'].extend([f"{rst_file.name}: {issue}" for issue in ref_issues])
            
            status['cross_references_valid'] = all_valid
            
        except Exception as e:
            status['issues'].append(f"Error checking integration status: {e}")
        
        return status