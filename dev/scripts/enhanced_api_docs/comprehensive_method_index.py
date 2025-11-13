"""
Combines all method index components into a unified system.
"""

import json
from pathlib import Path
from typing import Dict, List, Optional, Any, Tuple
from datetime import datetime

from .method_index_generator import MethodIndexGenerator
from .method_search_filter import MethodSearchFilter, SearchQuery, FilterCriteria, SearchType, FilterType
from .json_enhancer import EnhancedJSONStubData
from .config import config
from .logging_setup import get_logger

logger = get_logger('method_index')


class ComprehensiveMethodIndexSystem:
    """
    Method index system that integrates all components.
    Provides searchable method indexes with filtering and usage examples.
    """
    
    def __init__(self):
        """Initialize the method index system."""
        self.logger = logger
        self.index_generator = MethodIndexGenerator()
        self.search_filter = MethodSearchFilter()
        self.output_dir = config.get_path('output.docs_dir')
        
        # Ensure output directory exists
        self.output_dir.mkdir(parents=True, exist_ok=True)
    
    def generate_complete_index_system(self, enhanced_stubs: Dict[str, EnhancedJSONStubData]) -> Dict[str, Any]:
        """
        Generate complete method index system with all features.
        
        Args:
            enhanced_stubs: Dictionary of class names to enhanced stub data
            
        Returns:
            Dictionary with all generated files and metadata
        """
        self.logger.info("Generating complete method index system")
        
        results = {
            'generated_files': {},
            'metadata': {},
            'statistics': {},
            'search_data': {},
            'examples_data': {}
        }
        
        try:
            # 1. Generate searchable index
            self.logger.info("Step 1: Generating searchable index")
            rst_content, index_file, search_metadata = self.index_generator.generate_enhanced_searchable_index(enhanced_stubs)
            
            # Write main index file
            with open(index_file, 'w', encoding='utf-8') as f:
                f.write(rst_content)
            
            results['generated_files']['main_index'] = index_file
            results['search_data'] = search_metadata
            
            # 2. Generate category-specific indexes
            self.logger.info("Step 2: Generating category-specific indexes")
            category_indexes = self.index_generator.generate_category_indexes(enhanced_stubs)
            
            category_files = {}
            for category, (rst_content, output_file) in category_indexes.items():
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(rst_content)
                category_files[category] = output_file
            
            results['generated_files']['category_indexes'] = category_files
            
            # 3. Generate filtered indexes for common use cases
            self.logger.info("Step 3: Generating filtered indexes")
            filtered_indexes = self._generate_common_filtered_indexes(enhanced_stubs)
            results['generated_files']['filtered_indexes'] = filtered_indexes
            
            # 4. Generate searchable data files
            self.logger.info("Step 4: Generating searchable data files")
            searchable_data = self.index_generator.generate_searchable_index_data(enhanced_stubs)
            
            # Write searchable data as JSON
            search_data_file = self.output_dir / 'method_search_data.json'
            with open(search_data_file, 'w', encoding='utf-8') as f:
                json.dump(searchable_data, f, indent=2, ensure_ascii=False)
            
            results['generated_files']['search_data'] = search_data_file
            
            # 5. Generate statistics and metadata
            self.logger.info("Step 5: Generating statistics and metadata")
            statistics = self.index_generator.generate_index_statistics(enhanced_stubs)
            results['statistics'] = statistics
            
            # Write statistics
            stats_file = self.output_dir / 'method_index_statistics.json'
            with open(stats_file, 'w', encoding='utf-8') as f:
                json.dump(statistics, f, indent=2, ensure_ascii=False)
            
            results['generated_files']['statistics'] = stats_file
            
            # 6. Generate navigation index
            self.logger.info("Step 6: Generating navigation index")
            navigation_rst = self._generate_navigation_index(results)
            navigation_file = self.output_dir / 'index.rst'
            
            with open(navigation_file, 'w', encoding='utf-8') as f:
                f.write(navigation_rst)
            
            results['generated_files']['navigation_index'] = navigation_file
            
            # 7. Generate metadata summary
            results['metadata'] = {
                'generation_timestamp': datetime.now().isoformat(),
                'total_methods': statistics['total_methods'],
                'total_classes': len(enhanced_stubs),
                'documented_methods': statistics['documented_methods'],
                'methods_with_examples': statistics['methods_with_examples'],
                'categories': list(statistics['categories'].keys()),
                'files_generated': len(results['generated_files']),
                'search_index_size': search_metadata.get('total_methods', 0)
            }
            
            self.logger.info(f"Successfully generated complete method index system with {len(results['generated_files'])} files")
            return results
            
        except Exception as e:
            self.logger.error(f"Error generating complete index system: {e}")
            raise
    
    def search_methods_interactive(self, enhanced_stubs: Dict[str, EnhancedJSONStubData],
                                 query: str = "",
                                 class_filter: Optional[str] = None,
                                 category_filter: Optional[str] = None,
                                 return_type_filter: Optional[str] = None,
                                 include_deprecated: bool = False,
                                 max_results: int = 50) -> List[Dict[str, Any]]:
        """
        Interactive method search with multiple filter options.
        
        Args:
            enhanced_stubs: Dictionary of enhanced stub data
            query: Search query string
            class_filter: Filter by class name (partial match)
            category_filter: Filter by category (exact match)
            return_type_filter: Filter by return type (partial match)
            include_deprecated: Whether to include deprecated methods
            max_results: Maximum number of results to return
            
        Returns:
            List of matching methods with relevance scores
        """
        self.logger.debug(f"Interactive search: query='{query}', filters=class:{class_filter}, category:{category_filter}, return_type:{return_type_filter}")
        
        # Create method entries
        method_entries = self.index_generator._create_method_entries(enhanced_stubs)
        
        # Create filters
        filters = []
        if class_filter:
            filters.append(FilterCriteria(FilterType.CLASS, class_filter, "contains"))
        if category_filter:
            filters.append(FilterCriteria(FilterType.CATEGORY, category_filter, "equals"))
        if return_type_filter:
            filters.append(FilterCriteria(FilterType.RETURN_TYPE, return_type_filter, "contains"))
        if not include_deprecated:
            filters.append(FilterCriteria(FilterType.DEPRECATED, False, "equals"))
        
        # Create search query
        search_query = None
        if query.strip():
            search_query = SearchQuery(
                query=query,
                search_type=SearchType.PARTIAL,
                case_sensitive=False,
                search_fields=['method_name', 'class_name', 'category', 'description', 'return_type']
            )
        
        # Perform search and filtering
        search_results = self.search_filter.search_and_filter(method_entries, search_query, filters)
        
        # Limit results
        limited_results = search_results[:max_results]
        
        # Convert to serializable format
        results = []
        for result in limited_results:
            method_entry = result.method_entry
            results.append({
                'method_name': method_entry.method_name,
                'class_name': method_entry.class_name,
                'full_class_name': method_entry.full_class_name,
                'category': method_entry.category,
                'description': method_entry.short_description,
                'signature': method_entry.signature,
                'return_type': method_entry.return_type,
                'parameters': method_entry.parameters,
                'deprecated': method_entry.deprecated,
                'has_examples': len(method_entry.examples) > 0,
                'relevance_score': result.relevance_score,
                'matched_fields': result.matched_fields
            })
        
        self.logger.info(f"Interactive search returned {len(results)} results")
        return results
    

    def _generate_common_filtered_indexes(self, enhanced_stubs: Dict[str, EnhancedJSONStubData]) -> Dict[str, Path]:
        """Generate commonly used filtered indexes."""
        filtered_indexes = {}
        
        # Common filters
        common_filters = [
            ('analysis_methods', None, None, 'Analysis'),
            ('io_methods', None, None, 'I/O Operations'),
            ('visualization_methods', None, None, 'Visualization'),
            ('getter_methods', None, None, 'Getters'),
            ('setter_methods', None, None, 'Setters'),
            ('string_returning_methods', None, 'String', None),
            ('list_returning_methods', None, 'List', None),
            ('boolean_returning_methods', None, 'boolean', None)
        ]
        
        for filter_name, class_filter, return_type_filter, category_filter in common_filters:
            try:
                rst_content, output_file = self.index_generator.generate_filtered_index(
                    enhanced_stubs, class_filter, return_type_filter, category_filter
                )
                
                # Rename file to match filter
                actual_output_file = self.output_dir / f"{filter_name}.rst"
                with open(actual_output_file, 'w', encoding='utf-8') as f:
                    f.write(rst_content)
                
                filtered_indexes[filter_name] = actual_output_file
                
            except Exception as e:
                self.logger.warning(f"Failed to generate filtered index {filter_name}: {e}")
        
        return filtered_indexes
    
    def _generate_navigation_index(self, results: Dict[str, Any]) -> str:
        """Generate navigation index RST content."""
        rst_lines = [
            "Enhanced API Method Documentation",
            "================================",
            "",
            "Welcome to the API method documentation system. This section provides",
            "comprehensive documentation for all SNT methods with examples and tutorials.",
            "",
            ".. contents:: Navigation",
            "   :local:",
            "   :depth: 2",
            ""
        ]
        
        # Statistics summary
        metadata = results.get('metadata', {})
        rst_lines.extend([
            "Documentation Overview",
            "----------------------",
            "",
            f"* **Total Methods:** {metadata.get('total_methods', 0)}",
            f"* **Classes Documented:** {metadata.get('total_classes', 0)}",
            f"* **Methods with JavaDoc:** {metadata.get('documented_methods', 0)}",
            f"* **Methods with Examples:** {metadata.get('methods_with_examples', 0)}",
            f"* **Categories:** {len(metadata.get('categories', []))}",
            ""
        ])
        
        # Main indexes
        rst_lines.extend([
            "Main Indexes",
            "------------",
            "",
            ".. toctree::",
            "   :maxdepth: 1",
            "",
            "   method_index",
            ""
        ])
        
        # Category indexes
        category_files = results['generated_files'].get('category_indexes', {})
        if category_files:
            rst_lines.extend([
                "Methods by Category",
                "-------------------",
                "",
                "Browse methods organized by functionality:",
                "",
                ".. toctree::",
                "   :maxdepth: 1",
                ""
            ])
            
            for category, file_path in category_files.items():
                filename = file_path.stem
                rst_lines.append(f"   {filename}")
            
            rst_lines.append("")
        
        # Filtered indexes
        filtered_files = results['generated_files'].get('filtered_indexes', {})
        if filtered_files:
            rst_lines.extend([
                "Specialized Indexes",
                "-------------------",
                "",
                "Pre-filtered indexes for common use cases:",
                "",
                ".. toctree::",
                "   :maxdepth: 1",
                ""
            ])
            
            for filter_name, file_path in filtered_files.items():
                filename = file_path.stem
                display_name = filter_name.replace('_', ' ').title()
                rst_lines.append(f"   {filename}")
            
            rst_lines.append("")
        
        # Search and examples data
        rst_lines.extend([
            "Search and Examples Data",
            "------------------------",
            "",
            "For developers building search interfaces or working with the method data:",
            "",
            "* :download:`Method Search Data <method_search_data.json>` - JSON data for search functionality",
            "* :download:`Usage Examples Data <method_examples_data.json>` - Integrated examples and tutorials",
            "* :download:`Index Statistics <method_index_statistics.json>` - Statistics",
            ""
        ])
        
        # Usage guide
        rst_lines.extend([
            "How to Use This Documentation",
            "-----------------------------",
            "",
            "**Finding Methods:**",
            "",
            "1. **Browse by Category** - Use category indexes to find methods by functionality",
            "2. **Search by Name** - Use the main method index and browser search",
            "3. **Filter by Return Type** - Find methods that return specific data types",
            "4. **Look for Examples** - Methods with ✓ in the Examples column have code samples",
            "",
            "**Understanding Method Information:**",
            "",
            "* **Signature** - Complete method signature with parameter types",
            "* **Description** - JavaDoc description explaining what the method does",
            "* **Parameters** - Detailed parameter information with descriptions",
            "* **Return Value** - What the method returns and its description",
            "* **Examples** - Code examples showing how to use the method",
            "* **Tutorials** - Links to notebooks and guides using the method",
            "",
            "**Method Categories:**",
            ""
        ])
        
        # Add category descriptions
        categories = metadata.get('categories', [])
        for category in categories:
            description = self.index_generator._get_category_description(category)
            rst_lines.append(f"* **{category}** - {description}")
        
        rst_lines.extend([
            "",
            "----",
            "",
            f"*Documentation generated on {metadata.get('generation_timestamp', 'unknown')}*"
        ])
        
        return "\n".join(rst_lines)
    

    def validate_generated_indexes(self, results: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """
        Validate all generated index files.
        
        Args:
            results: Results from generate_complete_index_system
            
        Returns:
            Tuple of (is_valid, list_of_issues)
        """
        issues = []
        
        # Check that all files were generated
        generated_files = results.get('generated_files', {})
        
        required_files = ['main_index', 'navigation_index', 'search_data', 'statistics']
        for required_file in required_files:
            if required_file not in generated_files:
                issues.append(f"Missing required file: {required_file}")
            else:
                file_path = generated_files[required_file]
                if not file_path.exists():
                    issues.append(f"Generated file does not exist: {file_path}")
                elif file_path.stat().st_size == 0:
                    issues.append(f"Generated file is empty: {file_path}")
        
        # Validate JSON files
        json_files = ['search_data', 'examples_data', 'statistics']
        for json_file in json_files:
            if json_file in generated_files:
                try:
                    with open(generated_files[json_file], 'r', encoding='utf-8') as f:
                        json.load(f)
                except json.JSONDecodeError as e:
                    issues.append(f"Invalid JSON in {json_file}: {e}")
        
        # Check metadata completeness
        metadata = results.get('metadata', {})
        required_metadata = ['generation_timestamp', 'total_methods', 'total_classes']
        for required_meta in required_metadata:
            if required_meta not in metadata:
                issues.append(f"Missing metadata: {required_meta}")
        
        is_valid = len(issues) == 0
        return is_valid, issues