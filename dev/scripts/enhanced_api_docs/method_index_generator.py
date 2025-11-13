"""
method index generator for the enhanced API documentation system.
Creates searchable indexes of all methods across all classes.
"""

import re
from pathlib import Path
from typing import Dict, List, Optional, Any, Tuple
from datetime import datetime
from collections import defaultdict

from .json_enhancer import EnhancedJSONStubData
from .rst_templates import RSTTemplateEngine
from .method_index_entry import MethodIndexEntry
from .config import config
from .logging_setup import get_logger

logger = get_logger('method_index_generator')





class MethodIndexGenerator:
    """Generates comprehensive searchable method indexes."""
    
    def __init__(self):
        """Initialize the method index generator."""
        self.logger = logger
        self.template_engine = RSTTemplateEngine()
        # Removed unused components: search_filter, examples_integrator
        self.output_dir = config.get_path('output.docs_dir')
        self.include_deprecated = config.get('generation.include_deprecated', False)
        self.categories = config.get('generation.categories', [
            'Getters', 'Setters', 'Analysis', 'I/O Operations', 
            'Visualization', 'Utilities', 'Static Methods'
        ])
        
        # Ensure output directory exists
        self.output_dir.mkdir(parents=True, exist_ok=True)
    
    def generate_comprehensive_index(self, enhanced_stubs: Dict[str, EnhancedJSONStubData]) -> Tuple[str, Path]:
        """
        Generate comprehensive method index with all methods across all classes.
        
        Args:
            enhanced_stubs: Dictionary of class names to enhanced stub data
            
        Returns:
            Tuple of (generated RST content, output file path)
        """
        self.logger.info(f"Generating comprehensive method index for {len(enhanced_stubs)} classes")
        
        # Create method index entries
        method_entries = self._create_method_entries(enhanced_stubs)
        
        # Organize methods for index
        index_data = self._organize_methods_for_index(method_entries)
        
        # Generate RST content
        rst_content = self._generate_comprehensive_index_rst(index_data)
        
        # Output file path
        output_file = config.get_path('output.index_file')
        
        self.logger.info(f"Generated comprehensive method index with {len(method_entries)} methods")
        return rst_content, output_file
    
    def generate_searchable_index_data(self, enhanced_stubs: Dict[str, EnhancedJSONStubData]) -> Dict[str, Any]:
        """
        Generate searchable index data for JavaScript integration.
        
        Args:
            enhanced_stubs: Dictionary of class names to enhanced stub data
            
        Returns:
            Dictionary with searchable method data
        """
        self.logger.debug("Generating searchable index data")
        
        # Create method index entries
        method_entries = self._create_method_entries(enhanced_stubs)
        
        # Create searchable data structure
        searchable_data = {
            'methods': [entry.to_dict() for entry in method_entries],
            'categories': list(set(entry.category for entry in method_entries)),
            'classes': list(set(entry.class_name for entry in method_entries)),
            'return_types': list(set(entry.return_type for entry in method_entries)),
            'packages': list(set(entry.package for entry in method_entries if entry.package)),
            'generation_timestamp': datetime.now().isoformat(),
            'total_methods': len(method_entries),
            'deprecated_methods': sum(1 for entry in method_entries if entry.deprecated)
        }
        
        # Sort lists for consistent output
        for key in ['categories', 'classes', 'return_types', 'packages']:
            searchable_data[key].sort()
        
        self.logger.info(f"Generated searchable data for {len(method_entries)} methods")
        return searchable_data
    
    def generate_filtered_index(self, enhanced_stubs: Dict[str, EnhancedJSONStubData],
                               class_filter: Optional[str] = None,
                               return_type_filter: Optional[str] = None,
                               category_filter: Optional[str] = None) -> Tuple[str, Path]:
        """
        Generate filtered method index based on specified criteria.
        
        Args:
            enhanced_stubs: Dictionary of class names to enhanced stub data
            class_filter: Filter by class name (partial match)
            return_type_filter: Filter by return type (partial match)
            category_filter: Filter by category (exact match)
            
        Returns:
            Tuple of (generated RST content, output file path)
        """
        self.logger.debug(f"Generating filtered index: class={class_filter}, return_type={return_type_filter}, category={category_filter}")
        
        # Create method index entries
        method_entries = self._create_method_entries(enhanced_stubs)
        
        # Apply filters
        filtered_entries = [
            entry for entry in method_entries
            if entry.matches_filters(class_filter, return_type_filter, category_filter, self.include_deprecated)
        ]
        
        # Organize filtered methods
        index_data = self._organize_methods_for_index(filtered_entries)
        
        # Generate RST content with filter information
        rst_content = self._generate_filtered_index_rst(index_data, class_filter, return_type_filter, category_filter)
        
        # Create output filename based on filters
        filter_parts = []
        if class_filter:
            filter_parts.append(f"class_{self._sanitize_filename(class_filter)}")
        if return_type_filter:
            filter_parts.append(f"return_{self._sanitize_filename(return_type_filter)}")
        if category_filter:
            filter_parts.append(f"category_{self._sanitize_filename(category_filter)}")
        
        filename = f"method_index_{'_'.join(filter_parts)}.rst" if filter_parts else "method_index_filtered.rst"
        output_file = self.output_dir / filename
        
        self.logger.info(f"Generated filtered index with {len(filtered_entries)} methods")
        return rst_content, output_file
    
    def generate_category_indexes(self, enhanced_stubs: Dict[str, EnhancedJSONStubData]) -> Dict[str, Tuple[str, Path]]:
        """
        Generate separate index pages for each method category.
        
        Args:
            enhanced_stubs: Dictionary of class names to enhanced stub data
            
        Returns:
            Dictionary mapping category names to (RST content, file path) tuples
        """
        self.logger.info("Generating category-specific indexes")
        
        # Create method index entries
        method_entries = self._create_method_entries(enhanced_stubs)
        
        # Group by category
        methods_by_category = defaultdict(list)
        for entry in method_entries:
            methods_by_category[entry.category].append(entry)
        
        category_indexes = {}
        
        for category, entries in methods_by_category.items():
            if not entries:
                continue
            
            # Organize methods for this category
            category_data = self._organize_category_methods(entries, category)
            
            # Generate RST content
            rst_content = self._generate_category_index_rst(category, category_data)
            
            # Output file path
            safe_category = self._sanitize_filename(category)
            output_file = self.output_dir / f"category_{safe_category}.rst"
            
            category_indexes[category] = (rst_content, output_file)
        
        self.logger.info(f"Generated {len(category_indexes)} category indexes")
        return category_indexes
    
    def _create_method_entries(self, enhanced_stubs: Dict[str, EnhancedJSONStubData]) -> List[MethodIndexEntry]:
        """Create method index entries from enhanced stub data."""
        method_entries = []
        
        for class_name, enhanced_stub in enhanced_stubs.items():
            for method in enhanced_stub.methods:
                # Skip deprecated methods if configured
                if not self.include_deprecated and method.deprecated:
                    continue
                
                entry = MethodIndexEntry(method, class_name, enhanced_stub.package)
                method_entries.append(entry)
        
        return method_entries
    
    def _organize_methods_for_index(self, method_entries: List[MethodIndexEntry]) -> Dict[str, Any]:
        """Organize method entries for comprehensive index generation."""
        # Group by category
        methods_by_category = defaultdict(list)
        for entry in method_entries:
            methods_by_category[entry.category].append(entry)
        
        # Sort methods within each category
        for category in methods_by_category:
            methods_by_category[category].sort(key=lambda e: (e.class_name, e.method_name))
        
        # Group by return type
        methods_by_return_type = defaultdict(list)
        for entry in method_entries:
            methods_by_return_type[entry.return_type].append(entry)
        
        # Sort methods within each return type
        for return_type in methods_by_return_type:
            methods_by_return_type[return_type].sort(key=lambda e: (e.class_name, e.method_name))
        
        # Group by class
        methods_by_class = defaultdict(list)
        for entry in method_entries:
            methods_by_class[entry.class_name].append(entry)
        
        # Sort methods within each class
        for class_name in methods_by_class:
            methods_by_class[class_name].sort(key=lambda e: e.method_name)
        
        # Alphabetical grouping
        methods_alphabetical = defaultdict(list)
        for entry in method_entries:
            first_letter = entry.method_name[0].upper()
            methods_alphabetical[first_letter].append(entry)
        
        # Sort methods within each letter
        for letter in methods_alphabetical:
            methods_alphabetical[letter].sort(key=lambda e: (e.method_name, e.class_name))
        
        return {
            'all_methods': sorted(method_entries, key=lambda e: (e.method_name, e.class_name)),
            'methods_by_category': dict(methods_by_category),
            'methods_by_return_type': dict(methods_by_return_type),
            'methods_by_class': dict(methods_by_class),
            'methods_alphabetical': dict(sorted(methods_alphabetical.items())),
            'total_methods': len(method_entries),
            'categories': sorted(methods_by_category.keys()),
            'return_types': sorted(methods_by_return_type.keys()),
            'classes': sorted(methods_by_class.keys())
        }
    
    def _organize_category_methods(self, method_entries: List[MethodIndexEntry], category: str) -> Dict[str, Any]:
        """Organize method entries for category-specific index."""
        # Group by class
        methods_by_class = defaultdict(list)
        for entry in method_entries:
            methods_by_class[entry.class_name].append(entry)
        
        # Sort methods within each class
        for class_name in methods_by_class:
            methods_by_class[class_name].sort(key=lambda e: e.method_name)
        
        return {
            'category': category,
            'description': self._get_category_description(category),
            'methods_by_class': dict(methods_by_class),
            'total_methods': len(method_entries),
            'classes': sorted(methods_by_class.keys())
        }
    
    def _generate_comprehensive_index_rst(self, index_data: Dict[str, Any]) -> str:
        """Generate RST content for comprehensive method index."""
        rst_lines = [
            "Method Index",
            "============",
            "",
            "This page provides a comprehensive searchable index of all methods available in the SNT API.",
            f"Total methods: **{index_data['total_methods']}**",
            ""
        ]
        
        # Alphabetical index
        rst_lines.extend([
            "Alphabetical Index",
            "------------------",
            ""
        ])
        
        for letter in sorted(index_data['methods_alphabetical'].keys()):
            methods = index_data['methods_alphabetical'][letter]
            rst_lines.extend([
                f"{letter}",
                "^" * len(letter),
                ""
            ])
            
            for method in methods:
                # Create link to detailed doc file with anchor to specific method
                # Convert class name to lowercase for file naming (e.g., Tree -> tree_doc.rst)
                class_lower = method.class_name.lower()
                doc_file = f"../pysnt/{class_lower}_doc"
                # Create anchor for the method (sanitize method name for HTML anchor)
                method_anchor = method.method_name.lower().replace('_', '-')
                method_link = f"`{method.class_name}.{method.method_name} <{doc_file}.html#{method_anchor}>`_"
                rst_lines.append(f"* {method_link} - {method.short_description}")
            
            rst_lines.append("")
        
        # Footer
        rst_lines.extend([
            "----",
            "",
            f"*Method index generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*"
        ])
        
        return "\n".join(rst_lines)
    
    def _generate_filtered_index_rst(self, index_data: Dict[str, Any],
                                   class_filter: Optional[str],
                                   return_type_filter: Optional[str],
                                   category_filter: Optional[str]) -> str:
        """Generate RST content for filtered method index."""
        # Create filter description
        filter_parts = []
        if class_filter:
            filter_parts.append(f"class containing '{class_filter}'")
        if return_type_filter:
            filter_parts.append(f"return type containing '{return_type_filter}'")
        if category_filter:
            filter_parts.append(f"category '{category_filter}'")
        
        filter_desc = ", ".join(filter_parts) if filter_parts else "no filters"
        
        rst_lines = [
            "Filtered Method Index",
            "====================",
            "",
            f"Methods filtered by: {filter_desc}",
            f"Total matching methods: **{index_data['total_methods']}**",
            ""
        ]
        
        # Show all matching methods
        rst_lines.extend([
            "Matching Methods",
            "----------------",
            ""
        ])
        
        if index_data['all_methods']:
            rst_lines.extend([
                ".. list-table::",
                "   :header-rows: 1",
                "   :widths: 25 25 15 35",
                "",
                "   * - Method",
                "     - Class",
                "     - Return Type",
                "     - Description"
            ])
            
            for method in index_data['all_methods']:
                class_link = f":class:`{method.class_name}`"
                method_link = f":meth:`{method.class_name}.{method.method_name}`"
                description = method.short_description.replace('\n', ' ')
                
                rst_lines.append(f"   * - {method_link}")
                rst_lines.append(f"     - {class_link}")
                rst_lines.append(f"     - ``{method.return_type}``")
                rst_lines.append(f"     - {description}")
        else:
            rst_lines.append("No methods match the specified filters.")
        
        rst_lines.extend([
            "",
            "----",
            "",
            f"*Filtered index generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*"
        ])
        
        return "\n".join(rst_lines)
    
    def _generate_category_index_rst(self, category: str, category_data: Dict[str, Any]) -> str:
        """Generate RST content for category-specific index."""
        rst_lines = [
            f"{category} Methods",
            "=" * (len(category) + 8),
            "",
            category_data['description'],
            "",
            f"Total methods in this category: **{category_data['total_methods']}**",
            "",
            ".. contents:: Classes in this Category",
            "   :local:",
            ""
        ]
        
        # Methods by class
        for class_name in category_data['classes']:
            methods = category_data['methods_by_class'][class_name]
            
            rst_lines.extend([
                f"{class_name}",
                "-" * len(class_name),
                ""
            ])
            
            for method in methods:
                method_link = f":meth:`{class_name}.{method.method_name}`"
                rst_lines.extend([
                    f".. method:: {method.method_name}({', '.join([p[0] for p in method.parameters])})",
                    ""
                ])
                
                if method.javadoc_description:
                    rst_lines.extend([
                        f"   {method.javadoc_description}",
                        ""
                    ])
                
                rst_lines.extend([
                    f"   **Signature:** ``{method.signature}``",
                    ""
                ])
                
                if method.parameters:
                    rst_lines.extend([
                        "   **Parameters:**",
                        ""
                    ])
                    for param_name, param_type, param_desc in method.parameters:
                        desc_text = f": {param_desc}" if param_desc else ""
                        rst_lines.append(f"   * **{param_name}** (``{param_type}``){desc_text}")
                    rst_lines.append("")
                
                if method.return_description:
                    rst_lines.extend([
                        f"   **Returns:** (``{method.return_type}``) {method.return_description}",
                        ""
                    ])
                else:
                    rst_lines.extend([
                        f"   **Returns:** ``{method.return_type}``",
                        ""
                    ])
                
                if method.examples:
                    rst_lines.extend([
                        "   **Example:**",
                        "",
                        "   .. code-block:: java",
                        ""
                    ])
                    for line in method.examples[0].split('\n'):
                        rst_lines.append(f"      {line}")
                    rst_lines.append("")
            
            rst_lines.append("")
        
        rst_lines.extend([
            "----",
            "",
            f"*Category index generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*"
        ])
        
        return "\n".join(rst_lines)
    
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
        sanitized = re.sub(r'[^\w\-_.]', '_', filename)
        sanitized = re.sub(r'_+', '_', sanitized)
        return sanitized.lower()
    
    def generate_index_statistics(self, enhanced_stubs: Dict[str, EnhancedJSONStubData]) -> Dict[str, Any]:
        """
        Generate statistics about the method index.
        
        Args:
            enhanced_stubs: Dictionary of class names to enhanced stub data
            
        Returns:
            Dictionary with index statistics
        """
        method_entries = self._create_method_entries(enhanced_stubs)
        
        # Count by category
        category_counts = defaultdict(int)
        for entry in method_entries:
            category_counts[entry.category] += 1
        
        # Count by return type
        return_type_counts = defaultdict(int)
        for entry in method_entries:
            return_type_counts[entry.return_type] += 1
        
        # Count by class
        class_counts = defaultdict(int)
        for entry in method_entries:
            class_counts[entry.class_name] += 1
        
        # Count methods with documentation
        documented_methods = sum(1 for entry in method_entries if entry.javadoc_description)
        methods_with_examples = sum(1 for entry in method_entries if entry.examples)
        deprecated_methods = sum(1 for entry in method_entries if entry.deprecated)
        
        return {
            'total_methods': len(method_entries),
            'documented_methods': documented_methods,
            'methods_with_examples': methods_with_examples,
            'deprecated_methods': deprecated_methods,
            'documentation_coverage': round(documented_methods / len(method_entries) * 100, 1) if method_entries else 0,
            'categories': dict(category_counts),
            'return_types': dict(return_type_counts),
            'classes': dict(class_counts),
            'top_categories': sorted(category_counts.items(), key=lambda x: x[1], reverse=True)[:5],
            'top_return_types': sorted(return_type_counts.items(), key=lambda x: x[1], reverse=True)[:10],
            'most_methods_per_class': sorted(class_counts.items(), key=lambda x: x[1], reverse=True)[:10]
        }
    
    def generate_enhanced_searchable_index(self, enhanced_stubs: Dict[str, EnhancedJSONStubData]) -> Tuple[str, Path, Dict[str, Any]]:
        """
        Generate enhanced searchable method index with all features integrated.
        
        Args:
            enhanced_stubs: Dictionary of class names to enhanced stub data
            
        Returns:
            Tuple of (RST content, output file path, search metadata)
        """
        self.logger.info("Generating enhanced searchable method index")
        
        # Create method index entries
        method_entries = self._create_method_entries(enhanced_stubs)
        
        # Organize methods for comprehensive display
        index_data = self._organize_methods_for_index(method_entries)
        
        # Add minimal metadata (removed complex search and examples integration)
        index_data['search_metadata'] = {
            'total_searchable_methods': len(method_entries)
        }
        
        # Generate simplified RST content
        rst_content = self._generate_enhanced_searchable_rst(index_data)
        
        # Output file path
        output_file = config.get_path('output.index_file')
        
        self.logger.info(f"Generated simplified method index with {len(method_entries)} methods")
        return rst_content, output_file, {
            'total_methods': len(method_entries)
        }
    
    def _generate_enhanced_searchable_rst(self, index_data: Dict[str, Any]) -> str:
        """Generate enhanced RST content."""
        rst_lines = [
            "Method Index",
            "============",
            "",
            "This page provides an index of all methods available in the SNT API.",
            "",
            f"Total methods: **{index_data['total_methods']}** across **{len(index_data['classes'])}** classes.",
            ""
        ]

        # Alphabetical index with enhanced information
        rst_lines.extend([
            "",
        ])
        
        for letter in sorted(index_data['methods_alphabetical'].keys()):
            methods = index_data['methods_alphabetical'][letter]
            rst_lines.extend([
                f"{letter}",
                "^" * len(letter),
                ""
            ])
            
            for method in methods:
                method_key = f"{method.class_name}.{method.method_name}"
                
                # Create link to detailed doc file with anchor to specific method
                # Convert class name to lowercase for file naming (e.g., Tree -> tree_doc.rst)
                class_lower = method.class_name.lower()
                doc_file = f"../pysnt/{class_lower}_doc"
                # Create anchor for the method (sanitize method name for HTML anchor)
                method_anchor = method.method_name.lower().replace('_', '-')
                method_link = f"`{method.class_name}.{method.method_name} <{doc_file}.html#{method_anchor}>`_"
                
                # Enhanced information (removed redundant class name in parentheses)
                info_parts = []
                if method.deprecated:
                    info_parts.append("*deprecated*")
                if method.examples:
                    info_parts.append("*has examples*")
                
                info_str = " ".join(info_parts)
                if info_str:
                    rst_lines.append(f"* {method_link} {info_str} - {method.short_description}")
                else:
                    rst_lines.append(f"* {method_link} - {method.short_description}")
            
            rst_lines.append("")

        # Footer with metadata
        rst_lines.extend([
            "See Also",
            "--------",
            "* :doc:`API Documentation </api_auto/index>`",
            "* :doc:`Class Index </api_auto/class_index>`",
            "* :doc:`Constants Index </api_auto/constants_index>`",
        ])

        return "\n".join(rst_lines)