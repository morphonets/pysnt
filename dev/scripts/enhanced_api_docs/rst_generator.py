"""
RST documentation generator for the enhanced API documentation system.
Generates Sphinx-compatible RST files using the template system.
"""

import re
from pathlib import Path
from typing import Dict, List, Optional, Any, Tuple
from datetime import datetime

from .rst_templates import RSTTemplateEngine
from .json_enhancer import EnhancedJSONStubData
from .cross_reference_builder import CrossReferenceBuilder
from .sphinx_integration import SphinxIntegrator
from .config import config
from .logging_setup import get_logger

logger = get_logger('rst_generator')


class SphinxRSTGenerator:
    """Generates Sphinx-compatible RST documentation from enhanced JSON data."""
    
    def __init__(self):
        """Initialize the RST generator."""
        self.logger = logger
        self.template_engine = RSTTemplateEngine()
        self.cross_reference_builder = CrossReferenceBuilder()
        self.sphinx_integrator = SphinxIntegrator()
        self.output_dir = config.get_path('output.docs_dir')
        self.class_pages_dir = config.get_path('output.class_pages_dir')
        
        # Ensure output directories exist
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.class_pages_dir.mkdir(parents=True, exist_ok=True)
        
        # Configuration
        self.include_examples = config.get('generation.include_examples', True)
        self.include_deprecated = config.get('generation.include_deprecated', False)
        self.cross_reference_depth = config.get('generation.cross_reference_depth', 2)
        self.categories = config.get('generation.categories', [
            'Getters', 'Setters', 'Analysis', 'I/O Operations', 
            'Visualization', 'Utilities', 'Static Methods'
        ])
    
    def generate_class_page(self, enhanced_stub: EnhancedJSONStubData, 
                          all_stubs: Optional[Dict[str, EnhancedJSONStubData]] = None) -> Tuple[str, Path]:
        """
        Generate RST documentation page for a single class.
        
        Args:
            enhanced_stub: Enhanced JSON stub data for the class
            all_stubs: All enhanced stub data for cross-reference generation
            
        Returns:
            Tuple of (generated RST content, output file path)
        """
        self.logger.debug(f"Generating class page for {enhanced_stub.class_name}")
        
        # Prepare class data for template
        class_data = self._prepare_class_data(enhanced_stub, all_stubs)
        
        # Generate RST content
        rst_content = self.template_engine.render_class_page(class_data)
        
        # Determine output file path
        output_file = self.class_pages_dir / f"{enhanced_stub.class_name}.rst"
        
        self.logger.info(f"Generated class page for {enhanced_stub.class_name}")
        return rst_content, output_file
    
    def generate_and_write_class_page(self, enhanced_stub: EnhancedJSONStubData, 
                                    all_stubs: Optional[Dict[str, EnhancedJSONStubData]] = None) -> Path:
        """
        Generate and write RST documentation page for a single class.
        
        Args:
            enhanced_stub: Enhanced JSON stub data for the class
            all_stubs: All enhanced stub data for cross-reference generation
            
        Returns:
            Path to the written RST file
        """
        rst_content, output_file = self.generate_class_page(enhanced_stub, all_stubs)
        
        # Write RST content to file
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(rst_content)
            self.logger.info(f"Wrote class documentation to {output_file}")
        except Exception as e:
            self.logger.error(f"Failed to write class documentation for {enhanced_stub.class_name}: {e}")
            raise
        
        return output_file
    
    def generate_all_class_pages(self, enhanced_stubs: Dict[str, EnhancedJSONStubData]) -> Dict[str, Path]:
        """
        Generate RST documentation pages for all classes.
        
        Args:
            enhanced_stubs: Dictionary of class names to enhanced stub data
            
        Returns:
            Dictionary mapping class names to their RST file paths
        """
        self.logger.info(f"Generating documentation pages for {len(enhanced_stubs)} classes")
        
        generated_files = {}
        
        for class_name, enhanced_stub in enhanced_stubs.items():
            try:
                output_file = self.generate_and_write_class_page(enhanced_stub, enhanced_stubs)
                generated_files[class_name] = output_file
            except Exception as e:
                self.logger.error(f"Failed to generate page for {class_name}: {e}")
                # Continue with other classes
                continue
        
        self.logger.info(f"Successfully generated {len(generated_files)} class documentation pages")
        return generated_files
    
    def generate_method_index(self, enhanced_stubs: Dict[str, EnhancedJSONStubData]) -> Tuple[str, Path]:
        """
        Generate comprehensive method index page.
        
        Args:
            enhanced_stubs: Dictionary of class names to enhanced stub data
            
        Returns:
            Tuple of (generated RST content, output file path)
        """
        self.logger.debug("Generating method index")
        
        # Collect and organize all methods
        index_data = self._prepare_method_index_data(enhanced_stubs)
        
        # Generate RST content
        rst_content = self.template_engine.render_method_index(index_data)
        
        # Output file path
        output_file = config.get_path('output.index_file')
        
        self.logger.info("Generated method index")
        return rst_content, output_file
    
    def generate_category_pages(self, enhanced_stubs: Dict[str, EnhancedJSONStubData]) -> Dict[str, Tuple[str, Path]]:
        """
        Generate category-specific method pages.
        
        Args:
            enhanced_stubs: Dictionary of class names to enhanced stub data
            
        Returns:
            Dictionary mapping category names to (RST content, file path) tuples
        """
        self.logger.debug("Generating category pages")
        
        category_pages = {}
        category_data = self._organize_methods_by_category(enhanced_stubs)
        
        for category, methods_by_class in category_data.items():
            if not methods_by_class:
                continue
            
            # Prepare category data
            category_info = {
                'description': self._get_category_description(category),
                'methods_by_class': methods_by_class
            }
            
            # Generate RST content
            rst_content = self.template_engine.render_category_index(category, category_info)
            
            # Output file path
            safe_category = self._sanitize_filename(category)
            output_file = self.output_dir / f"category_{safe_category}.rst"
            
            category_pages[category] = (rst_content, output_file)
        
        self.logger.info(f"Generated {len(category_pages)} category pages")
        return category_pages
    
    def generate_toctree_index(self, enhanced_stubs: Dict[str, EnhancedJSONStubData]) -> Tuple[str, Path]:
        """
        Generate main index page with toctree for all generated documentation.
        
        Args:
            enhanced_stubs: Dictionary of class names to enhanced stub data
            
        Returns:
            Tuple of (generated RST content, output file path)
        """
        self.logger.debug("Generating main toctree index")
        
        # Organize classes by package
        packages = self._organize_classes_by_package(enhanced_stubs)
        
        # Generate toctree RST
        rst_content = self._generate_toctree_rst(packages, enhanced_stubs)
        
        # Output file path
        output_file = self.output_dir / "index.rst"
        
        self.logger.info("Generated main toctree index")
        return rst_content, output_file
    
    def generate_cross_references(self, enhanced_stub: EnhancedJSONStubData, 
                                all_stubs: Dict[str, EnhancedJSONStubData]) -> str:
        """
        Generate cross-reference section for a class.
        
        Args:
            enhanced_stub: Enhanced stub data for the target class
            all_stubs: All enhanced stub data for cross-reference resolution
            
        Returns:
            Generated RST content for cross-references
        """
        cross_ref_data = self.cross_reference_builder.build_comprehensive_cross_references(enhanced_stub, all_stubs)
        return self.template_engine.render_cross_references(cross_ref_data)
    
    def _prepare_class_data(self, enhanced_stub: EnhancedJSONStubData, 
                          all_stubs: Optional[Dict[str, EnhancedJSONStubData]] = None) -> Dict[str, Any]:
        """Prepare class data for template rendering."""
        # Filter methods based on configuration and organize by category
        method_categories = {}
        for method in enhanced_stub.methods:
            if not self.include_deprecated and method.deprecated:
                continue
            
            method_data = self._prepare_method_data(method)
            category = method.category
            
            if category not in method_categories:
                method_categories[category] = []
            method_categories[category].append(method_data)
        
        # Sort methods within each category by name
        for category in method_categories:
            method_categories[category].sort(key=lambda m: m['name'])
        
        # Filter and prepare fields
        filtered_fields = []
        for field in enhanced_stub.fields:
            if isinstance(field, dict):
                if not self.include_deprecated and field.get('deprecated', False):
                    continue
                # Enhance field data with additional information
                field_data = self._prepare_field_data(field)
                filtered_fields.append(field_data)
        
        # Filter and prepare constructors
        filtered_constructors = []
        for constructor in enhanced_stub.constructors:
            if isinstance(constructor, dict):
                constructor_data = self._prepare_constructor_data(constructor)
                filtered_constructors.append(constructor_data)
        
        # Prepare inheritance information
        inheritance_info = self._prepare_inheritance_data(enhanced_stub.inheritance)
        
        # Generate cross-references if all_stubs is provided
        cross_references = ""
        if all_stubs:
            cross_ref_data = self.cross_reference_builder.build_comprehensive_cross_references(enhanced_stub, all_stubs)
            cross_references = self.template_engine.render_cross_references(cross_ref_data)
        
        class_data = {
            'class_name': enhanced_stub.class_name,
            'package': enhanced_stub.package,
            'javadoc_description': enhanced_stub.javadoc_description or "",
            'class_description': enhanced_stub.javadoc_description or f"Documentation for {enhanced_stub.class_name} class.",
            'inheritance': inheritance_info,
            'deprecated': enhanced_stub.deprecated,
            'since_version': enhanced_stub.since_version,
            'see_also': enhanced_stub.see_also or [],
            'nested_classes': enhanced_stub.nested_classes or [],
            'method_categories': method_categories,
            'fields': filtered_fields,
            'constructors': filtered_constructors,
            'has_methods': len(method_categories) > 0,
            'has_fields': len(filtered_fields) > 0,
            'has_constructors': len(filtered_constructors) > 0,
            'cross_references': cross_references,
            'generation_timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        return class_data
    
    def _prepare_method_data(self, method) -> Dict[str, Any]:
        """Prepare method data for template rendering."""
        # Handle both enhanced method objects and dictionaries
        if hasattr(method, '__dict__'):
            method_dict = {
                'name': method.name,
                'javadoc_description': method.javadoc_description or "",
                'category': method.category,
                'deprecated': method.deprecated,
                'since_version': method.since_version,
                'see_also': method.see_also or [],
                'examples': method.examples if self.include_examples and method.examples else [],
                'overloads': [],
                'has_description': bool(method.javadoc_description),
                'has_examples': bool(method.examples) and self.include_examples
            }
            
            # Process overloads
            for overload in method.overloads:
                overload_dict = {
                    'signature': overload.signature,
                    'return_type': overload.return_type,
                    'java_return_type': overload.java_return_type,
                    'return_description': overload.return_description or "",
                    'throws': overload.throws or {},
                    'params': [],
                    'has_params': len(overload.params) > 0,
                    'has_return_description': bool(overload.return_description),
                    'has_throws': bool(overload.throws)
                }
                
                # Process parameters
                for param in overload.params:
                    param_dict = {
                        'name': param.name,
                        'type': param.type,
                        'java_type': param.java_type,
                        'description': param.description or "",
                        'has_description': bool(param.description)
                    }
                    overload_dict['params'].append(param_dict)
                
                method_dict['overloads'].append(overload_dict)
            
            return method_dict
        else:
            # Handle dictionary format (fallback)
            return {
                'name': method.get('name', 'Unknown'),
                'javadoc_description': method.get('javadoc_description', ''),
                'category': method.get('category', 'Utilities'),
                'deprecated': method.get('deprecated', False),
                'since_version': method.get('since_version'),
                'see_also': method.get('see_also', []),
                'examples': method.get('examples', []) if self.include_examples else [],
                'overloads': method.get('overloads', []),
                'has_description': bool(method.get('javadoc_description')),
                'has_examples': bool(method.get('examples')) and self.include_examples
            }
    
    def _prepare_field_data(self, field: Dict[str, Any]) -> Dict[str, Any]:
        """Prepare field data for template rendering."""
        return {
            'name': field.get('name', 'Unknown'),
            'type': field.get('type', 'Unknown'),
            'java_type': field.get('java_type', field.get('type', 'Unknown')),
            'description': field.get('description', ''),
            'deprecated': field.get('deprecated', False),
            'static': field.get('static', False),
            'final': field.get('final', False),
            'visibility': field.get('visibility', 'public'),
            'has_description': bool(field.get('description'))
        }
    
    def _prepare_constructor_data(self, constructor: Dict[str, Any]) -> Dict[str, Any]:
        """Prepare constructor data for template rendering."""
        # Handle constructor overloads if present
        overloads = constructor.get('overloads', [])
        if not overloads and 'signature' in constructor:
            # Single constructor, wrap in overloads format
            overloads = [constructor]
        
        prepared_overloads = []
        for overload in overloads:
            overload_data = {
                'signature': overload.get('signature', ''),
                'params': [],
                'description': overload.get('description', ''),
                'has_params': len(overload.get('params', [])) > 0,
                'has_description': bool(overload.get('description'))
            }
            
            # Process parameters
            for param in overload.get('params', []):
                param_data = {
                    'name': param.get('name', 'Unknown'),
                    'type': param.get('type', 'Unknown'),
                    'java_type': param.get('java_type', param.get('type', 'Unknown')),
                    'description': param.get('description', ''),
                    'has_description': bool(param.get('description'))
                }
                overload_data['params'].append(param_data)
            
            prepared_overloads.append(overload_data)
        
        return {
            'name': constructor.get('name', 'Constructor'),
            'overloads': prepared_overloads,
            'description': constructor.get('description', ''),
            'deprecated': constructor.get('deprecated', False),
            'has_description': bool(constructor.get('description')),
            'has_overloads': len(prepared_overloads) > 0
        }
    
    def _prepare_inheritance_data(self, inheritance: Dict[str, List[str]]) -> Dict[str, Any]:
        """Prepare inheritance data for template rendering."""
        if not inheritance:
            inheritance = {'extends': [], 'implements': []}
        
        return {
            'extends': inheritance.get('extends', []),
            'implements': inheritance.get('implements', []),
            'has_extends': len(inheritance.get('extends', [])) > 0,
            'has_implements': len(inheritance.get('implements', [])) > 0,
            'has_inheritance': len(inheritance.get('extends', [])) > 0 or len(inheritance.get('implements', [])) > 0
        }
    
    def _prepare_method_index_data(self, enhanced_stubs: Dict[str, EnhancedJSONStubData]) -> Dict[str, Any]:
        """Prepare data for method index generation."""
        all_methods = []
        method_categories = {category: [] for category in self.categories}
        methods_by_return_type = {}
        
        for class_name, enhanced_stub in enhanced_stubs.items():
            for method in enhanced_stub.methods:
                # Skip deprecated methods if configured
                if not self.include_deprecated and method.deprecated:
                    continue
                
                # Create method entry for index
                method_entry = {
                    'name': method.name,
                    'class_name': class_name,
                    'category': method.category,
                    'short_description': self._get_short_description(method.javadoc_description),
                    'signature': method.overloads[0].signature if method.overloads else '',
                    'return_type': method.overloads[0].return_type if method.overloads else 'void'
                }
                
                all_methods.append(method_entry)
                
                # Organize by category
                category = method.category
                if category in method_categories:
                    method_categories[category].append(method_entry)
                
                # Organize by return type
                return_type = method_entry['return_type']
                if return_type not in methods_by_return_type:
                    methods_by_return_type[return_type] = []
                methods_by_return_type[return_type].append(method_entry)
        
        return {
            'all_methods': all_methods,
            'method_categories': method_categories,
            'methods_by_return_type': methods_by_return_type
        }
    
    def _organize_methods_by_category(self, enhanced_stubs: Dict[str, EnhancedJSONStubData]) -> Dict[str, Dict[str, List]]:
        """Organize methods by category and class."""
        category_data = {}
        
        for class_name, enhanced_stub in enhanced_stubs.items():
            for method in enhanced_stub.methods:
                # Skip deprecated methods if configured
                if not self.include_deprecated and method.deprecated:
                    continue
                
                category = method.category
                if category not in category_data:
                    category_data[category] = {}
                
                if class_name not in category_data[category]:
                    category_data[category][class_name] = []
                
                method_data = self._prepare_method_data(method)
                category_data[category][class_name].append(method_data)
        
        return category_data
    
    def _organize_classes_by_package(self, enhanced_stubs: Dict[str, EnhancedJSONStubData]) -> Dict[str, List[str]]:
        """Organize classes by package for toctree generation."""
        packages = {}
        
        for class_name, enhanced_stub in enhanced_stubs.items():
            package = enhanced_stub.package
            if package not in packages:
                packages[package] = []
            packages[package].append(class_name)
        
        # Sort classes within each package
        for package in packages:
            packages[package].sort()
        
        return packages
    
    def _generate_toctree_rst(self, packages: Dict[str, List[str]], 
                            enhanced_stubs: Dict[str, EnhancedJSONStubData]) -> str:
        """Generate main toctree RST content."""
        rst_lines = [
            "Enhanced API Documentation",
            "=" * 25,
            "",
            "This section provides comprehensive API documentation for SNT classes,",
            "enhanced with JavaDoc descriptions and organized by functionality.",
            "",
            ".. contents:: Quick Navigation",
            "   :local:",
            "   :depth: 2",
            "",
            "Method Index",
            "------------",
            "",
            "* :doc:`method_index` - Comprehensive searchable method index",
            ""
        ]
        
        # Add category pages
        category_data = self._organize_methods_by_category(enhanced_stubs)
        if category_data:
            rst_lines.extend([
                "Methods by Category",
                "-------------------",
                ""
            ])
            
            for category in sorted(category_data.keys()):
                safe_category = self._sanitize_filename(category)
                rst_lines.append(f"* :doc:`category_{safe_category}` - {category} methods")
            
            rst_lines.append("")
        
        # Add classes by package
        rst_lines.extend([
            "Classes by Package",
            "------------------",
            "",
            ".. toctree::",
            "   :maxdepth: 2",
            "   :caption: API Classes",
            ""
        ])
        
        for package in sorted(packages.keys()):
            rst_lines.append(f"   Package: {package}")
            rst_lines.append(f"   {'=' * (len(package) + 9)}")
            rst_lines.append("")
            
            for class_name in packages[package]:
                rst_lines.append(f"   classes/{class_name}")
            
            rst_lines.append("")
        
        # Add footer
        rst_lines.extend([
            "----",
            "",
            f"*Documentation generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*"
        ])
        
        return "\n".join(rst_lines)
    

    

    
    def _get_short_description(self, description: str, max_length: int = 100) -> str:
        """Get short description for index pages."""
        if not description:
            return "No description available"
        
        # Remove HTML tags and clean up
        clean_desc = re.sub(r'<[^>]+>', '', description)
        clean_desc = re.sub(r'\s+', ' ', clean_desc).strip()
        
        # Truncate if too long
        if len(clean_desc) > max_length:
            clean_desc = clean_desc[:max_length].rsplit(' ', 1)[0] + '...'
        
        return clean_desc
    
    def _get_category_description(self, category: str) -> str:
        """Get description for method categories."""
        descriptions = {
            'Getters': 'Methods that retrieve values or properties from objects.',
            'Setters': 'Methods that modify values or properties of objects.',
            'Analysis': 'Methods that perform calculations, measurements, or statistical analysis.',
            'I/O Operations': 'Methods that handle input/output operations, file loading, and data import/export.',
            'Visualization': 'Methods that create visual representations, plots, or graphical displays.',
            'Static Methods': 'Static utility methods that can be called without object instances.',
            'Utilities': 'General utility methods and helper functions.'
        }
        return descriptions.get(category, f'Methods in the {category} category.')
    
    def _sanitize_filename(self, filename: str) -> str:
        """Sanitize filename for file system compatibility."""
        # Replace spaces and special characters
        sanitized = re.sub(r'[^\w\-_.]', '_', filename)
        sanitized = re.sub(r'_+', '_', sanitized)
        return sanitized.lower()
    
    def validate_rst_syntax(self, rst_content: str) -> Tuple[bool, List[str]]:
        """
        Validate RST syntax for common issues.
        
        Args:
            rst_content: RST content to validate
            
        Returns:
            Tuple of (is_valid, list_of_issues)
        """
        issues = []
        lines = rst_content.split('\n')
        
        # Check for common RST issues
        for i, line in enumerate(lines, 1):
            # Check for inconsistent heading underlines (only for significant mismatches)
            if line and all(c in '=-~^"' for c in line) and len(line) > 3:
                if i > 1:
                    prev_line = lines[i-2]
                    # Skip if previous line is empty (could be a horizontal rule)
                    if prev_line.strip() == '':
                        continue
                    # Only flag if the difference is significant (more than 1 character)
                    if abs(len(line) - len(prev_line)) > 1:
                        issues.append(f"Line {i}: Heading underline length doesn't match title")
            
            # Check for malformed directives
            if line.strip().startswith('.. ') and '::' not in line and 'deprecated::' not in line:
                issues.append(f"Line {i}: Possible malformed directive")
            
            # Check for unescaped special characters in text
            if '`' in line and not line.strip().startswith('.. '):
                # Simple check for unmatched backticks
                backtick_count = line.count('`')
                if backtick_count % 2 != 0:
                    issues.append(f"Line {i}: Unmatched backticks")
        
        return len(issues) == 0, issues
    
    def validate_class_page_completeness(self, enhanced_stub: EnhancedJSONStubData, 
                                       rst_content: str) -> Tuple[bool, List[str]]:
        """
        Validate that the generated class page includes all required elements.
        
        Args:
            enhanced_stub: Enhanced JSON stub data for the class
            rst_content: Generated RST content
            
        Returns:
            Tuple of (is_complete, list_of_missing_elements)
        """
        missing_elements = []
        
        # Check for class name as title
        if enhanced_stub.class_name not in rst_content:
            missing_elements.append("Class name not found in title")
        
        # Check for package information
        if enhanced_stub.package and enhanced_stub.package not in rst_content:
            missing_elements.append("Package information missing")
        
        # Check for class description if available
        if enhanced_stub.javadoc_description and enhanced_stub.javadoc_description not in rst_content:
            missing_elements.append("Class description missing")
        
        # Check for inheritance information if available
        if enhanced_stub.inheritance:
            if enhanced_stub.inheritance.get('extends') and 'Extends:' not in rst_content:
                missing_elements.append("Inheritance (extends) information missing")
            if enhanced_stub.inheritance.get('implements') and 'Implements:' not in rst_content:
                missing_elements.append("Inheritance (implements) information missing")
        
        # Check for methods organization by category
        method_categories = {}
        for method in enhanced_stub.methods:
            category = method.category
            if category not in method_categories:
                method_categories[category] = []
            method_categories[category].append(method)
        
        for category in method_categories:
            if category not in rst_content:
                missing_elements.append(f"Method category '{category}' not found")
        
        # Check for constructors if available
        if enhanced_stub.constructors and 'Constructors' not in rst_content:
            missing_elements.append("Constructor section missing")
        
        # Check for fields if available
        if enhanced_stub.fields and 'Fields' not in rst_content:
            missing_elements.append("Fields section missing")
        
        return len(missing_elements) == 0, missing_elements
    
    def get_generation_statistics(self, enhanced_stubs: Dict[str, EnhancedJSONStubData]) -> Dict[str, Any]:
        """
        Get statistics about the documentation generation.
        
        Args:
            enhanced_stubs: Dictionary of enhanced stub data
            
        Returns:
            Dictionary with generation statistics
        """
        stats = {
            'total_classes': len(enhanced_stubs),
            'total_methods': 0,
            'methods_with_javadoc': 0,
            'methods_with_examples': 0,
            'deprecated_methods': 0,
            'categories': {category: 0 for category in self.categories},
            'packages': set(),
            'classes_with_javadoc': 0
        }
        
        for enhanced_stub in enhanced_stubs.values():
            stats['packages'].add(enhanced_stub.package)
            
            if enhanced_stub.javadoc_description:
                stats['classes_with_javadoc'] += 1
            
            for method in enhanced_stub.methods:
                stats['total_methods'] += 1
                
                if method.javadoc_description:
                    stats['methods_with_javadoc'] += 1
                
                if method.examples:
                    stats['methods_with_examples'] += 1
                
                if method.deprecated:
                    stats['deprecated_methods'] += 1
                
                category = method.category
                if category in stats['categories']:
                    stats['categories'][category] += 1
        
        stats['packages'] = len(stats['packages'])
        return stats
    
    def generate_cross_reference_report(self, enhanced_stubs: Dict[str, EnhancedJSONStubData]) -> Dict[str, Any]:
        """
        Generate comprehensive cross-reference report.
        
        Args:
            enhanced_stubs: Dictionary of enhanced stub data
            
        Returns:
            Dictionary with cross-reference statistics and quality metrics
        """
        return self.cross_reference_builder.generate_cross_reference_report(enhanced_stubs)
    
    def ensure_sphinx_integration(self) -> bool:
        """
        Ensure generated RST files are properly integrated with Sphinx.
        
        Returns:
            True if integration successful, False otherwise
        """
        self.logger.info("Ensuring Sphinx integration for enhanced API documentation")
        
        try:
            # Validate Sphinx compatibility
            is_compatible, issues = self.sphinx_integrator.validate_sphinx_compatibility()
            if not is_compatible:
                self.logger.error("Sphinx compatibility validation failed:")
                for issue in issues:
                    self.logger.error(f"  - {issue}")
                return False
            
            # Ensure integration
            success = self.sphinx_integrator.ensure_sphinx_integration()
            if success:
                self.logger.info("Sphinx integration completed successfully")
            else:
                self.logger.error("Sphinx integration failed")
            
            return success
            
        except Exception as e:
            self.logger.error(f"Error during Sphinx integration: {e}")
            return False
    
    def validate_generated_documentation(self, enhanced_stubs: Dict[str, EnhancedJSONStubData]) -> Tuple[bool, Dict[str, Any]]:
        """
        Validate all generated documentation for completeness and Sphinx compatibility.
        
        Args:
            enhanced_stubs: Dictionary of enhanced stub data
            
        Returns:
            Tuple of (is_valid, validation_report)
        """
        self.logger.info("Validating generated documentation")
        
        validation_report = {
            'total_classes': len(enhanced_stubs),
            'validated_classes': 0,
            'sphinx_compatible': False,
            'cross_references_valid': False,
            'issues': [],
            'warnings': []
        }
        
        try:
            # Validate each class page
            for class_name, enhanced_stub in enhanced_stubs.items():
                class_file = self.class_pages_dir / f"{class_name}.rst"
                
                if not class_file.exists():
                    validation_report['issues'].append(f"Class file missing: {class_name}.rst")
                    continue
                
                # Read and validate RST content
                with open(class_file, 'r', encoding='utf-8') as f:
                    rst_content = f.read()
                
                # Validate RST syntax
                is_valid_syntax, syntax_issues = self.validate_rst_syntax(rst_content)
                if not is_valid_syntax:
                    validation_report['issues'].extend([f"{class_name}: {issue}" for issue in syntax_issues])
                
                # Validate completeness
                is_complete, missing_elements = self.validate_class_page_completeness(enhanced_stub, rst_content)
                if not is_complete:
                    validation_report['warnings'].extend([f"{class_name}: {element}" for element in missing_elements])
                
                # Validate cross-references
                is_valid_refs, ref_issues = self.sphinx_integrator.validate_cross_references(rst_content)
                if not is_valid_refs:
                    validation_report['issues'].extend([f"{class_name}: {issue}" for issue in ref_issues])
                
                validation_report['validated_classes'] += 1
            
            # Validate Sphinx integration
            integration_status = self.sphinx_integrator.get_integration_status()
            validation_report['sphinx_compatible'] = integration_status['sphinx_compatible']
            validation_report['cross_references_valid'] = integration_status['cross_references_valid']
            validation_report['issues'].extend(integration_status['issues'])
            
            # Overall validation result
            is_valid = (
                len(validation_report['issues']) == 0 and
                validation_report['sphinx_compatible'] and
                validation_report['validated_classes'] == validation_report['total_classes']
            )
            
            self.logger.info(f"Documentation validation completed: {validation_report['validated_classes']}/{validation_report['total_classes']} classes validated")
            if validation_report['issues']:
                self.logger.warning(f"Found {len(validation_report['issues'])} validation issues")
            if validation_report['warnings']:
                self.logger.info(f"Found {len(validation_report['warnings'])} warnings")
            
            return is_valid, validation_report
            
        except Exception as e:
            validation_report['issues'].append(f"Validation error: {e}")
            self.logger.error(f"Error during documentation validation: {e}")
            return False, validation_report