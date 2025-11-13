"""
Structured Integration System - Creates organized JavaDoc integration following a specific pattern.

This module implements the structured approach where:
1. Docstrings get enhanced with JavaDoc descriptions and links to detailed docs
2. Detailed documentation files follow consistent naming (e.g., pysnt.tree_doc.rst)
3. Clear organization with proper cross-references back to main API
"""

import json
import re
from pathlib import Path
from typing import Dict, List, Optional, Any
from .config import config
from .logging_setup import get_logger

logger = get_logger('structured_integration')


class StructuredIntegrationManager:
    """Manages structured integration of JavaDoc documentation."""
    
    def __init__(self):
        """Initialize the structured integration manager."""
        self.enhanced_data = {}
        self.integration_stats = {
            'docstrings_enhanced': 0,
            'detailed_docs_created': 0,
            'classes_processed': 0,
            'cross_references_added': 0
        }
    
    def create_structured_integration(self) -> bool:
        """
        Create structured integration following the specified pattern.
        
        Returns:
            True if integration succeeded, False otherwise
        """
        logger.info("Starting structured JavaDoc integration")
        
        try:
            # Step 1: Load enhanced documentation data
            if not self._load_enhanced_data():
                return False
            
            # Step 2: Enhance docstrings with JavaDoc descriptions and links
            self._enhance_docstrings_with_links()
            
            # Step 3: Create detailed documentation files
            self._create_detailed_documentation_files()
            
            # Step 4: Update cross-references
            self._update_cross_references()
            
            # Report results
            self._report_integration_results()
            
            return True
            
        except Exception as e:
            logger.error(f"Structured integration failed: {e}")
            return False
    
    def _load_enhanced_data(self) -> bool:
        """Load enhanced documentation data from JSON files."""
        logger.info("Loading enhanced documentation data...")
        
        try:
            enhanced_dir = config.get_path('output.docs_dir') / 'enhanced_json'
            if not enhanced_dir.exists():
                logger.error(f"Enhanced documentation directory not found: {enhanced_dir}")
                return False
            
            json_files = list(enhanced_dir.glob('*_enhanced.json'))
            for json_file in json_files:
                try:
                    with open(json_file, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                    
                    class_name = data.get('class_name', json_file.stem.replace('_enhanced', ''))
                    self.enhanced_data[class_name] = data
                    
                except Exception as e:
                    logger.warning(f"Failed to load {json_file}: {e}")
            
            logger.info(f"Loaded enhanced data for {len(self.enhanced_data)} classes")
            self.integration_stats['classes_processed'] = len(self.enhanced_data)
            return len(self.enhanced_data) > 0
            
        except Exception as e:
            logger.error(f"Failed to load enhanced data: {e}")
            return False
    
    def _enhance_docstrings_with_links(self):
        """Enhance docstrings with JavaDoc descriptions and links to detailed docs."""
        logger.info("Enhancing docstrings with JavaDoc descriptions and links...")
        
        # Create a docstring enhancement file that can be imported to enhance classes at runtime
        self._create_docstring_enhancement_file()
        
        # Also try to enhance any directly defined classes
        for class_name, class_data in self.enhanced_data.items():
            self._enhance_class_docstring(class_name, class_data)
    
    def _enhance_class_docstring(self, class_name: str, class_data: Dict[str, Any]):
        """Enhance a specific class docstring."""
        logger.info(f"Enhancing docstring for {class_name}")
        
        # Find the Python file containing this class
        python_file = self._find_class_file(class_name)
        if not python_file:
            logger.warning(f"Could not find Python file for {class_name}")
            return
        
        try:
            content = python_file.read_text(encoding='utf-8')
            original_content = content
            
            # Create enhanced docstring
            enhanced_docstring = self._create_enhanced_docstring(class_name, class_data)
            
            # For DynamicPlaceholder classes, we need to modify the docstring assignment
            # Look for the pattern where docstring is assigned to DynamicPlaceholder.__doc__
            content = self._inject_enhanced_docstring_for_dynamic_class(content, class_name, enhanced_docstring)
            
            # Write back if changes were made
            if content != original_content:
                python_file.write_text(content, encoding='utf-8')
                self.integration_stats['docstrings_enhanced'] += 1
                logger.debug(f"Enhanced docstring in {python_file}")
                
        except Exception as e:
            logger.error(f"Failed to enhance docstring for {class_name}: {e}")
    
    def _find_class_file(self, class_name: str) -> Optional[Path]:
        """Find the Python file containing a specific class."""
        project_root = config.project_root
        
        # Get package information to determine likely location
        package_info = self._get_package_info(class_name)
        python_module = package_info['python_module']
        
        # Determine search paths based on package
        search_paths = []
        
        if python_module == 'pysnt':
            # Main package classes
            search_paths = [
                'src/pysnt/__init__.py',
                'src/pysnt/core.py',
            ]
        else:
            # Subpackage classes
            subpackage = python_module.replace('pysnt.', '')
            search_paths = [
                f'src/pysnt/{subpackage}/__init__.py',
                'src/pysnt/__init__.py',  # Some classes might be imported in main
                'src/pysnt/core.py',
            ]
        
        # Add common fallback locations
        search_paths.extend([
            'src/pysnt/analysis/__init__.py',
            'src/pysnt/util/__init__.py',
            'src/pysnt/viewer/__init__.py',
            'src/pysnt/tracing/__init__.py',
            'src/pysnt/gui/__init__.py',
            'src/pysnt/io/__init__.py',
            'src/pysnt/converters/__init__.py',
            'src/pysnt/display/__init__.py',
        ])
        
        # Search for the class in these files
        for search_path in search_paths:
            file_path = project_root / search_path
            if file_path.exists():
                try:
                    content = file_path.read_text(encoding='utf-8')
                    # Look for class definition or class name in quotes (for imports)
                    if f'class {class_name}' in content or f'"{class_name}"' in content or f"'{class_name}'" in content:
                        return file_path
                except Exception as e:
                    logger.debug(f"Error reading {file_path}: {e}")
                    continue
        
        logger.warning(f"Could not find Python file for class {class_name}")
        return None
    
    def _create_enhanced_docstring(self, class_name: str, class_data: Dict[str, Any]) -> str:
        """Create an enhanced docstring with JavaDoc description and link."""
        # Get JavaDoc description from the enhanced RST file
        javadoc_desc = self._get_class_javadoc_description(class_name)
        
        # Create the detailed doc filename
        detailed_doc_link = self._get_detailed_doc_link(class_name)
        
        # Get actual package for JavaDoc URL
        package_info = self._get_package_info(class_name)
        package_path = package_info['package'].replace('.', '/')
        javadoc_url = f"https://javadoc.scijava.org/SNT/index.html?{package_path}/{class_name}.html"
        
        # Check if we have a proper JavaDoc description (not fallback)
        has_javadoc = not javadoc_desc.startswith('Enhanced documentation for')
        
        if has_javadoc:
            # New format: Just JavaDoc description + link to detailed docs
            enhanced_docstring = f'''"""
    {javadoc_desc}
    
    **All Methods and Attributes:** See `{class_name} detailed documentation <{detailed_doc_link}>`_.
    """'''
        else:
            # Fallback format for classes without JavaDoc descriptions
            enhanced_docstring = f'''"""
    SNT class with method signatures.
    
    Available for direct import after JVM initialization.
    Call pysnt.initialize() before using this class.
    
    **All Methods and Attributes:** See `{class_name} detailed documentation <{detailed_doc_link}>`_.
    
    See `{class_name} JavaDoc <{javadoc_url}>`_.
    """'''
        
        return enhanced_docstring
    
    def _get_class_javadoc_description(self, class_name: str) -> str:
        """Get the JavaDoc description for a class from the enhanced JSON file."""
        try:
            # Find the enhanced JSON file for this class
            enhanced_json_dir = config.project_root / 'docs' / 'pysnt' / 'enhanced_json'
            json_filename = f"{class_name}_enhanced.json"
            json_file = enhanced_json_dir / json_filename
            
            if not json_file.exists():
                logger.debug(f"Enhanced JSON file not found: {json_file}")
                return f"Enhanced documentation for {class_name} class."
            
            # Read the enhanced JSON file
            import json
            with open(json_file, 'r', encoding='utf-8') as f:
                enhanced_data = json.load(f)
            
            # Get the javadoc_description field
            javadoc_desc = enhanced_data.get('javadoc_description')
            
            if javadoc_desc and javadoc_desc.strip():
                return javadoc_desc.strip()
            else:
                return f"Enhanced documentation for {class_name} class."
                
        except Exception as e:
            logger.warning(f"Failed to extract JavaDoc description for {class_name}: {e}")
            return f"Enhanced documentation for {class_name} class."
    
    def _get_detailed_doc_name(self, class_name: str) -> str:
        """Get the detailed documentation filename for a class."""
        # Convert class name to documentation filename
        # Examples:
        # Tree -> pysnt.tree_doc
        # SWCPoint -> pysnt.util.swcpoint_doc
        # TreeStatistics -> pysnt.analysis.treestatistics_doc
        
        class_name_lower = class_name.lower()
        
        # Map classes to their package locations based on Java package structure
        package_info = self._get_package_info(class_name)
        python_module = package_info['python_module']
        
        # Convert to documentation name
        if python_module == 'pysnt':
            doc_name = f'pysnt.{class_name_lower}_doc'
        else:
            # For subpackages like pysnt.analysis, pysnt.util, etc.
            subpackage = python_module.replace('pysnt.', '')
            doc_name = f'pysnt.{subpackage}.{class_name_lower}_doc'
        
        # Handle special cases for specific classes
        package_mapping = {
            'tree': 'pysnt.tree_doc',
            'path': 'pysnt.path_doc',
            'snt': 'pysnt.snt_doc',
            'pathandfillmanager': 'pysnt.pathandfillmanager_doc',
            'treestatistics': 'pysnt.analysis.treestatistics_doc',
            'pathstatistics': 'pysnt.analysis.pathstatistics_doc',
            'swcpoint': 'pysnt.util.swcpoint_doc',
            'pointinimage': 'pysnt.util.pointinimage_doc',
            'viewer2d': 'pysnt.viewer.viewer2d_doc',
            'viewer3d': 'pysnt.viewer.viewer3d_doc',
            'tracerthread': 'pysnt.tracing.tracerthread_doc',
            'searchthread': 'pysnt.tracing.searchthread_doc',
        }
        
        return package_mapping.get(class_name_lower, doc_name)
    
    def _inject_enhanced_docstring_for_dynamic_class(self, content: str, class_name: str, enhanced_docstring: str) -> str:
        """Inject enhanced docstring for DynamicPlaceholder classes."""
        # Look for the pattern where docstring is assigned in create_dynamic_placeholder_class
        # We need to find where DynamicPlaceholder.__doc__ is set and replace it
        
        # First, check if this class is created via create_dynamic_placeholder_class
        if f'create_dynamic_placeholder_class(' in content and class_name in content:
            # This is likely in common_module.py where classes are created
            # We need to modify the docstring template in create_dynamic_placeholder_class
            return self._modify_dynamic_placeholder_docstring_template(content, enhanced_docstring)
        
        # Otherwise, look for direct class definitions
        return self._inject_enhanced_docstring(content, class_name, enhanced_docstring)
    
    def _modify_dynamic_placeholder_docstring_template(self, content: str, enhanced_docstring: str) -> str:
        """Modify the docstring template in create_dynamic_placeholder_class function."""
        # For now, we'll create a separate approach - modify the docstring after class creation
        # This is more complex and would require runtime modification
        # Let's use a simpler approach: create a separate docstring enhancement file
        return content
    
    def _create_docstring_enhancement_file(self):
        """Create a Python file that can enhance docstrings at runtime."""
        logger.info("Creating docstring enhancement file...")
        
        # Create the enhancement file content
        enhancement_content = '''"""
Runtime docstring enhancement for PySNT classes.

This module provides enhanced docstrings with JavaDoc descriptions and links
to detailed documentation for all PySNT classes.
"""

def enhance_class_docstrings():
    """Enhance docstrings for all PySNT classes with JavaDoc information."""
    import sys
    
    # Enhanced docstrings for all classes
    enhanced_docstrings = {
'''
        
        # Add enhanced docstrings for all classes
        for class_name, class_data in self.enhanced_data.items():
            enhanced_docstring = self._create_enhanced_docstring(class_name, class_data)
            # Escape the docstring for Python code
            escaped_docstring = repr(enhanced_docstring)
            enhancement_content += f'        "{class_name}": {escaped_docstring},\n'
        
        enhancement_content += '''    }
    
    # Apply enhanced docstrings to classes in pysnt modules
    _apply_enhanced_docstrings(enhanced_docstrings)

def _apply_enhanced_docstrings(enhanced_docstrings):
    """Apply enhanced docstrings to classes in loaded modules."""
    import sys
    
    # List of modules to check for classes
    module_names = [
        'pysnt',
        'pysnt.analysis', 
        'pysnt.util',
        'pysnt.viewer',
        'pysnt.tracing',
        'pysnt.gui',
        'pysnt.io',
        'pysnt.converters',
        'pysnt.display'
    ]
    
    for module_name in module_names:
        if module_name in sys.modules:
            module = sys.modules[module_name]
            
            for class_name, enhanced_docstring in enhanced_docstrings.items():
                if hasattr(module, class_name):
                    class_obj = getattr(module, class_name)
                    if hasattr(class_obj, '__doc__'):
                        class_obj.__doc__ = enhanced_docstring
                        #print(f"Enhanced docstring for {module_name}.{class_name}")

# Auto-enhance when this module is imported
enhance_class_docstrings()
'''
        
        # Write the enhancement file
        enhancement_file = config.project_root / 'src' / 'pysnt' / '_docstring_enhancements.py'
        enhancement_file.write_text(enhancement_content, encoding='utf-8')
        logger.info(f"Created docstring enhancement file: {enhancement_file}")
        
        # Also create an __init__.py modification to import the enhancements
        self._modify_init_to_import_enhancements()
    
    def _modify_init_to_import_enhancements(self):
        """Modify __init__.py files to import docstring enhancements."""
        logger.info("Modifying __init__.py to import docstring enhancements...")
        
        # Add import to main pysnt __init__.py
        init_file = config.project_root / 'src' / 'pysnt' / '__init__.py'
        
        try:
            content = init_file.read_text(encoding='utf-8')
            
            # Check if enhancement import already exists
            if '_docstring_enhancements' not in content:
                # Add import at the end of the file, before __all__ if it exists
                if '__all__ = [' in content:
                    # Insert before __all__
                    content = content.replace(
                        '__all__ = [',
                        '# Import docstring enhancements\ntry:\n    from . import _docstring_enhancements\nexcept ImportError:\n    pass  # Enhancements not available\n\n__all__ = ['
                    )
                else:
                    # Add at the end
                    content += '\n\n# Import docstring enhancements\ntry:\n    from . import _docstring_enhancements\nexcept ImportError:\n    pass  # Enhancements not available\n'
                
                init_file.write_text(content, encoding='utf-8')
                logger.info("Added docstring enhancement import to __init__.py")
            else:
                logger.info("Docstring enhancement import already exists in __init__.py")
                
        except Exception as e:
            logger.error(f"Failed to modify __init__.py: {e}")
    
    def _inject_enhanced_docstring(self, content: str, class_name: str, enhanced_docstring: str) -> str:
        """Inject enhanced docstring into Python file content."""
        # Look for existing class definition with docstring
        class_pattern = rf'class {class_name}[^:]*:\s*"""[^"]*"""'
        
        if re.search(class_pattern, content, re.DOTALL):
            # Replace existing docstring
            content = re.sub(class_pattern, 
                           lambda m: m.group(0).split('"""')[0] + enhanced_docstring,
                           content, flags=re.DOTALL)
        else:
            # Look for class definition without docstring and add one
            class_def_pattern = rf'(class {class_name}[^:]*:\s*)'
            if re.search(class_def_pattern, content):
                content = re.sub(class_def_pattern, 
                               rf'\1{enhanced_docstring}\n    ',
                               content)
        
        return content
    
    def _create_detailed_documentation_files(self):
        """Create detailed documentation files for each class."""
        logger.info("Creating detailed documentation files...")
        
        docs_dir = config.get_path('output.docs_dir')
        
        for class_name, class_data in self.enhanced_data.items():
            try:
                detailed_doc = self._create_detailed_doc_content(class_name, class_data)
                doc_filename = self._get_detailed_doc_filename(class_name)
                doc_path = docs_dir / doc_filename
                
                # Create directory if needed
                doc_path.parent.mkdir(parents=True, exist_ok=True)
                
                # Write the detailed documentation
                doc_path.write_text(detailed_doc, encoding='utf-8')
                self.integration_stats['detailed_docs_created'] += 1
                logger.debug(f"Created detailed doc: {doc_path}")
                
            except Exception as e:
                logger.error(f"Failed to create detailed doc for {class_name}: {e}")
    
    def _get_detailed_doc_filename(self, class_name: str) -> str:
        """Get the detailed documentation filename for a class."""
        # Use simple flat filename in api_auto directory
        class_name_lower = class_name.lower()
        return f"{class_name_lower}_doc.rst"
    
    def _create_detailed_doc_content(self, class_name: str, class_data: Dict[str, Any]) -> str:
        """Create detailed documentation content for a class."""
        # Get JavaDoc description from enhanced RST file
        javadoc_desc = self._get_class_javadoc_description(class_name)
        # Handle both dictionary and EnhancedJSONStubData objects
        if hasattr(class_data, 'methods'):
            methods = class_data.methods
        else:
            methods = class_data.get('methods', [])
        
        # Get package information
        package_info = self._get_package_info(class_name)
        
        # Add toctree for navigation to all API modules
        # Check if inject_toctree is enabled in config
        inject_toctree = config.get('sphinx.inject_toctree', True)
        
        if inject_toctree:
            toctree_maxdepth = config.get('sphinx.toctree_maxdepth', 3)
            toctree_caption = config.get('sphinx.toctree_caption', 'Complete API Reference')
            toctree_hidden = config.get('sphinx.toctree_hidden', True)
            
            hidden_option = "\n   :hidden:" if toctree_hidden else ""
            
            toctree_content = f"""
.. toctree::
   :maxdepth: {toctree_maxdepth}
   :caption: {toctree_caption}{hidden_option}

   ../api_auto/index
   ../api_auto/pysnt
   ../api_auto/pysnt.analysis
   ../api_auto/pysnt.analysis.graph
   ../api_auto/pysnt.analysis.growth
   ../api_auto/pysnt.analysis.sholl
   ../api_auto/pysnt.analysis.sholl.gui
   ../api_auto/pysnt.analysis.sholl.math
   ../api_auto/pysnt.analysis.sholl.parsers
   ../api_auto/pysnt.annotation
   ../api_auto/pysnt.converters
   ../api_auto/pysnt.converters.chart_converters
   ../api_auto/pysnt.converters.core
   ../api_auto/pysnt.converters.enhancement
   ../api_auto/pysnt.converters.extractors
   ../api_auto/pysnt.converters.graph_converters
   ../api_auto/pysnt.converters.structured_data_converters
   ../api_auto/pysnt.core
   ../api_auto/pysnt.display
   ../api_auto/pysnt.display.core
   ../api_auto/pysnt.display.data_display
   ../api_auto/pysnt.display.utils
   ../api_auto/pysnt.display.visual_display
   ../api_auto/pysnt.gui
   ../api_auto/pysnt.gui.cmds
   ../api_auto/pysnt.io
   ../api_auto/pysnt.tracing
   ../api_auto/pysnt.tracing.artist
   ../api_auto/pysnt.tracing.cost
   ../api_auto/pysnt.tracing.heuristic
   ../api_auto/pysnt.tracing.image
   ../api_auto/pysnt.util
   ../api_auto/pysnt.viewer
   ../api_auto/pysnt.common_module
   ../api_auto/pysnt.config
   ../api_auto/pysnt.gui_utils
   ../api_auto/pysnt.java_utils
   ../api_auto/pysnt.setup_utils
   ../api_auto/method_index
   ../api_auto/class_index
   ../api_auto/constants_index

"""
        else:
            toctree_content = ""
        
        content = f"""
``{class_name}`` Class Documentation
{'=' * (len(class_name) + 21)}

{toctree_content}
**Package:** ``{package_info['package']}``

{javadoc_desc}

"""
        
        # Add related classes section if available
        related_classes = self._get_related_classes(class_name, class_data)
        if related_classes:
            content += """
Related Classes
---------------

"""
            for related_class in related_classes:
                content += f"* :class:`{related_class}`\n"
            content += "\n"
        
        # Add fields section
        # Handle both dictionary and EnhancedJSONStubData objects
        if hasattr(class_data, 'fields'):
            fields = class_data.fields
        else:
            fields = class_data.get('fields', [])
        if fields:
            content += """
Fields
------

"""
            for field in fields:
                # Handle both dictionary and field objects
                if hasattr(field, 'name'):
                    field_name = field.name
                    field_type = field.type
                    field_desc = field.javadoc_description or 'No description available.'
                else:
                    field_name = field.get('name', 'unknown')
                    field_type = field.get('type', 'unknown')
                    field_desc = field.get('javadoc_description', 'No description available.')
                
                content += f"""
**{field_name}** : ``{field_type}``
    {field_desc}

"""
        
        # Add methods section organized by category
        if methods:
            content += """
Methods
-------

"""
            # Group methods by category using intelligent categorization
            categorized_methods = self._categorize_methods(methods)
            
            # Add methods by category
            for category, category_methods in categorized_methods.items():
                content += f"""
{category} Methods
{'~' * (len(category) + 8)}

"""
                for method in category_methods:
                    # Handle both dictionary and EnhancedMethodInfo objects
                    if hasattr(method, 'name'):
                        method_name = method.name
                        method_desc = method.javadoc_description or 'No description available.'
                    else:
                        method_name = method.get('name', 'unknown')
                        method_desc = method.get('javadoc_description', 'No description available.')
                    
                    # Get method signature if available
                    signature = self._get_method_signature(method)
                    
                    content += f"""
.. py:method:: {signature}

   {method_desc}

"""
        
        # Add return link to main API
        api_link = self._get_main_api_link(class_name)
        package_api_link = self._get_package_api_link(class_name)
        # The links are already relative, no conversion needed
        relative_package_link = package_api_link
        relative_api_link = api_link
        
        # Get actual package for JavaDoc URL
        package_info = self._get_package_info(class_name)
        package_path = package_info['package'].replace('.', '/')
        javadoc_url = f"https://javadoc.scijava.org/SNT/index.html?{package_path}/{class_name}.html"
        
        content += f"""
See Also
--------

* `Package API <{relative_package_link}>`_
* `{class_name} JavaDoc <{javadoc_url}>`_
* :doc:`Class Index </api_auto/class_index>`
* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
"""
        
        return content
    
    def _get_package_info(self, class_name: str) -> Dict[str, str]:
        """Get package information for a class."""
        # Get package from enhanced data if available
        if class_name in self.enhanced_data:
            enhanced_data = self.enhanced_data[class_name]
            if hasattr(enhanced_data, 'package'):
                package = enhanced_data.package
            else:
                package = enhanced_data.get('package', 'sc.fiji.snt')
        else:
            # Fallback to default package
            package = 'sc.fiji.snt'
        
        return {
            'package': package,
            'python_module': self._java_package_to_python_module(package)
        }
    
    def _java_package_to_python_module(self, java_package: str) -> str:
        """Convert Java package name to Python module name."""
        # sc.fiji.snt.analysis -> pysnt.analysis
        if java_package.startswith('sc.fiji.snt'):
            if java_package == 'sc.fiji.snt':
                return 'pysnt'
            else:
                # Replace sc.fiji.snt with pysnt, keeping any subpackages
                return java_package.replace('sc.fiji.snt', 'pysnt')
        return 'pysnt'
    
    def _get_related_classes(self, class_name: str, class_data: Dict[str, Any]) -> List[str]:
        """Get related classes (interfaces, superclasses) that are part of SNT."""
        related = []
        
        # Look for inheritance information in the class data
        if hasattr(class_data, 'inheritance'):
            inheritance = class_data.inheritance or {}
        else:
            inheritance = class_data.get('inheritance', {})
        
        # Add interfaces
        interfaces = inheritance.get('interfaces', [])
        for interface in interfaces:
            if 'snt' in interface.lower():  # Only SNT-related interfaces
                interface_name = interface.split('.')[-1]
                if interface_name in self.enhanced_data:
                    related.append(interface_name)
        
        # Add superclasses
        superclass = inheritance.get('superclass', '')
        if superclass and 'snt' in superclass.lower():
            superclass_name = superclass.split('.')[-1]
            if superclass_name in self.enhanced_data:
                related.append(superclass_name)
        
        return related
    
    def _categorize_methods(self, methods: List[Dict]) -> Dict[str, List[Dict]]:
        """Categorize methods by type for better organization."""
        categories = {
            'Utilities': [],
            'Getters': [],
            'Setters': [],
            'Analysis': [],
            'Visualization': [],
            'I/O Operations': [],
            'Other': []
        }
        
        logger = get_logger(__name__)
        logger.debug(f"Categorizing {len(methods)} methods")
        
        for i, method in enumerate(methods):
            # Handle both dictionary and EnhancedMethodInfo objects
            if hasattr(method, 'name'):
                method_name = method.name
            else:
                method_name = method.get('name') if hasattr(method, 'get') else None
            
            logger.debug(f"Processing method {i}: {method_name} (type: {type(method)})")
            
            # Ensure method_name is a string
            if not method_name or not isinstance(method_name, str):
                logger.debug(f"Skipping method {i} - invalid name: {method_name}")
                categories['Other'].append(method)
                continue
                
            method_name_lower = method_name.lower()
            # Remove 'static ' prefix for categorization but preserve it in the name
            clean_name = method_name_lower.replace('static ', '')
            
            # Additional safety check for clean_name
            if not clean_name:
                categories['Other'].append(method)
                continue
            
            # Getters (including static getters) - prioritize this over other categories
            if clean_name.startswith('get') or clean_name.startswith('is') or clean_name.startswith('has'):
                categories['Getters'].append(method)
            # Setters (including static setters)
            elif clean_name.startswith('set'):
                categories['Setters'].append(method)
            # Analysis methods (including static analysis methods)
            elif any(keyword in clean_name for keyword in ['analyze', 'compute', 'calculate', 'measure', 'statistics']):
                categories['Analysis'].append(method)
            # Visualization methods (including static visualization methods)
            elif any(keyword in clean_name for keyword in ['show', 'display', 'render', 'plot', 'draw', 'view']):
                categories['Visualization'].append(method)
            # I/O Operations (including static I/O methods like fromFile, listFromDir)
            # Be more specific about I/O operations to avoid false positives
            elif (clean_name.startswith('load') or clean_name.startswith('save') or 
                  clean_name.startswith('read') or clean_name.startswith('write') or 
                  clean_name.startswith('export') or clean_name.startswith('import') or
                  clean_name.endswith('file') or clean_name.startswith('fromfile') or 
                  clean_name.startswith('listfromdir') or clean_name.endswith('fromdir') or
                  'fromfile' in clean_name or 'listfromdir' in clean_name):
                categories['I/O Operations'].append(method)
            # Utility methods (including static utility methods)
            elif any(keyword in clean_name for keyword in ['clone', 'copy', 'clear', 'reset', 'validate', 'check']):
                categories['Utilities'].append(method)
            else:
                categories['Other'].append(method)
        
        # Remove empty categories
        return {k: v for k, v in categories.items() if v}

    def _get_method_signature(self, method: Any) -> str:
        """Get a clean method signature for documentation."""
        # Handle both dictionary and EnhancedMethodInfo objects
        if hasattr(method, 'name'):
            method_name = method.name
            overloads = method.overloads
        else:
            method_name = method.get('name', 'unknown')
            overloads = method.get('overloads', [])
        
        if overloads:
            # Use the first overload signature
            if hasattr(overloads[0], 'signature'):
                signature = overloads[0].signature
            else:
                signature = overloads[0].get('signature', '')
            if signature:
                # Clean up the signature for Python documentation
                if ' -> ' in signature:
                    # Extract just the method part (before the return type)
                    method_part = signature.split(' -> ')[0]
                    # The method_part already includes the closing parenthesis
                    return method_part
                return signature
        
        # Fallback to simple signature
        return f"{method_name}()"
    
    def _get_main_api_link(self, class_name: str) -> str:
        """Get the link back to the main API documentation."""
        # Get package information to determine API location
        package_info = self._get_package_info(class_name)
        python_module = package_info['python_module']
        
        # Files are in docs/pysnt/, so we need to go up one level to reach api_auto
        api_auto_path = "../api_auto"
        
        # Convert Python module to API documentation path
        if python_module == 'pysnt':
            base_link = f'{api_auto_path}/pysnt'
        else:
            # For subpackages, use the module path
            base_link = f"{api_auto_path}/{python_module}"
        
        return f"{base_link}#{class_name}"
    
    def _get_package_api_link(self, class_name: str) -> str:
        """Get the link to the package API documentation."""
        # Get package information to determine API location
        package_info = self._get_package_info(class_name)
        python_module = package_info['python_module']
        
        # Files are in docs/pysnt/, so we need to go up one level to reach api_auto
        api_auto_path = "../api_auto"
        
        # Convert Python module to API documentation path
        if python_module == 'pysnt':
            return f'{api_auto_path}/pysnt.html#pysnt.{class_name}'
        else:
            # For subpackages, use the module path
            return f"{api_auto_path}/{python_module}.html#{python_module}.{class_name}"
    
    def _get_detailed_doc_link(self, class_name: str) -> str:
        """Get the link to the detailed documentation file."""
        detailed_doc_filename = self._get_detailed_doc_filename(class_name)
        # Convert file path to web path (remove .rst extension, convert to HTML)
        web_path = detailed_doc_filename.replace('.rst', '.html').replace('/', '/')
        return f"/{web_path}"
    
    def _update_cross_references(self):
        """Update cross-references in the main API documentation."""
        logger.info("Updating cross-references in main API documentation...")
        
        # This would update the main API pages to include links to detailed docs
        # For now, we'll focus on the docstring enhancement and detailed doc creation
        pass
    
    def _report_integration_results(self):
        """Report integration results."""
        logger.info("Structured Integration Results:")
        logger.info(f"  - Classes processed: {self.integration_stats['classes_processed']}")
        logger.info(f"  - Docstrings enhanced: {self.integration_stats['docstrings_enhanced']}")
        logger.info(f"  - Detailed docs created: {self.integration_stats['detailed_docs_created']}")
        logger.info(f"  - Cross-references added: {self.integration_stats['cross_references_added']}")


def create_structured_integration() -> bool:
    """
    Convenience function to create structured integration.
    
    Returns:
        True if integration succeeded, False otherwise
    """
    manager = StructuredIntegrationManager()
    return manager.create_structured_integration()