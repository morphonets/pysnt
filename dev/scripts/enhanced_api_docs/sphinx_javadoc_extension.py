"""
Sphinx extension for integrating enhanced Javadoc information into auto-generated documentation.

This extension automatically injects JavaDoc information into Sphinx autodoc output
without modifying the source Python files.
"""

import json
from pathlib import Path
from typing import Dict, Any, List, Optional

from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.application import Sphinx
from sphinx.ext.autodoc import ClassDocumenter
from sphinx.util.docutils import SphinxDirective

from .logging_setup import get_logger

logger = get_logger('sphinx_javadoc_extension')


class JavaDocInfo:
    """Container for JavaDoc information."""
    
    def __init__(self):
        self.enhanced_data = {}
        self._load_enhanced_data()
    
    def _load_enhanced_data(self):
        """Load enhanced JSON data."""
        # Get the docs directory and construct the path to enhanced JSON
        # When running from docs directory, we need to find the correct path
        # Try multiple possible paths
        possible_paths = [
            Path.cwd() / 'api_enhanced' / 'enhanced_json',  # From docs directory
            Path(__file__).parent.parent.parent / 'docs' / 'api_enhanced' / 'enhanced_json',  # From project root
        ]
        
        enhanced_json_dir = None
        for path in possible_paths:
            if path.exists():
                enhanced_json_dir = path
                break
        
        if enhanced_json_dir is None:
            logger.warning(f"Enhanced JSON directory not found in any of the possible paths: {possible_paths}")
            return
        
        for json_file in enhanced_json_dir.glob("*_enhanced.json"):
            try:
                with open(json_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                
                class_name = data.get('class_name', json_file.stem.replace('_enhanced', ''))
                self.enhanced_data[class_name] = data
                
            except Exception as e:
                logger.warning(f"Failed to load {json_file}: {e}")
        
        logger.info(f"Loaded enhanced data for {len(self.enhanced_data)} classes")
    
    def get_class_info(self, class_name: str) -> Optional[Dict[str, Any]]:
        """Get enhanced information for a class."""
        return self.enhanced_data.get(class_name)
    
    def get_method_info(self, class_name: str, method_name: str) -> Optional[Dict[str, Any]]:
        """Get enhanced information for a method."""
        class_info = self.get_class_info(class_name)
        if not class_info:
            return None
        
        methods = class_info.get('methods', [])
        for method in methods:
            if method.get('name') == method_name:
                return method
        
        return None


# Global JavaDoc info instance
javadoc_info = JavaDocInfo()


class JavaDocDirective(SphinxDirective):
    """Directive to insert JavaDoc information."""
    
    has_content = False
    required_arguments = 1
    optional_arguments = 1
    option_spec = {
        'class': directives.unchanged,
        'method': directives.unchanged,
        'format': directives.unchanged,
    }
    
    def run(self):
        """Run the directive."""
        class_name = self.arguments[0]
        method_name = self.options.get('method')
        format_type = self.options.get('format', 'full')
        
        if method_name:
            return self._render_method_info(class_name, method_name, format_type)
        else:
            return self._render_class_info(class_name, format_type)
    
    def _render_class_info(self, class_name: str, format_type: str) -> List[nodes.Node]:
        """Render class JavaDoc information."""
        class_info = javadoc_info.get_class_info(class_name)
        if not class_info:
            return []
        
        result_nodes = []
        
        # JavaDoc description
        javadoc_desc = class_info.get('javadoc_description', '')
        if javadoc_desc:
            desc_section = nodes.section()
            desc_title = nodes.title(text="JavaDoc Description")
            desc_section += desc_title
            
            desc_para = nodes.paragraph()
            desc_para += nodes.Text(javadoc_desc)
            desc_section += desc_para
            
            result_nodes.append(desc_section)
        
        # Key methods
        if format_type in ['full', 'methods']:
            methods = class_info.get('methods', [])
            if methods:
                methods_section = self._create_methods_section(methods)
                result_nodes.append(methods_section)
        
        return result_nodes
    
    def _render_method_info(self, class_name: str, method_name: str, format_type: str) -> List[nodes.Node]:
        """Render method JavaDoc information."""
        method_info = javadoc_info.get_method_info(class_name, method_name)
        if not method_info:
            return []
        
        result_nodes = []
        
        # Method description
        javadoc_desc = method_info.get('javadoc_description', '')
        if javadoc_desc:
            desc_para = nodes.paragraph()
            desc_para += nodes.strong(text="JavaDoc: ")
            desc_para += nodes.Text(javadoc_desc)
            result_nodes.append(desc_para)
        
        # Method examples
        examples = method_info.get('examples', [])
        if examples and format_type in ['full', 'examples']:
            examples_section = self._create_examples_section(examples)
            result_nodes.append(examples_section)
        
        return result_nodes
    
    def _create_methods_section(self, methods: List[Dict[str, Any]]) -> nodes.Node:
        """Create a methods section."""
        section = nodes.section()
        title = nodes.title(text="Key Methods")
        section += title
        
        # Group methods by category
        categorized = {}
        for method in methods:
            category = method.get('category', 'Other')
            if category not in categorized:
                categorized[category] = []
            categorized[category].append(method)
        
        # Create bullet list for each category
        for category, cat_methods in categorized.items():
            if len(cat_methods) == 0:
                continue
                
            cat_title = nodes.subtitle(text=f"{category} Methods")
            section += cat_title
            
            bullet_list = nodes.bullet_list()
            
            for method in cat_methods[:5]:  # Limit to 5 methods per category
                list_item = nodes.list_item()
                
                # Method signature
                method_name = method.get('name', '')
                signature = self._get_method_signature(method)
                
                para = nodes.paragraph()
                para += nodes.literal(text=signature)
                
                # Method description
                desc = method.get('javadoc_description', method.get('documentation', ''))
                if desc:
                    para += nodes.Text(f" - {desc.split('.')[0]}.")
                
                list_item += para
                bullet_list += list_item
            
            section += bullet_list
        
        return section
    
    def _create_examples_section(self, examples: List[str]) -> nodes.Node:
        """Create an examples section."""
        section = nodes.section()
        title = nodes.title(text="Usage Examples")
        section += title
        
        for example in examples[:3]:  # Limit to 3 examples
            code_block = nodes.literal_block(text=example, language='python')
            section += code_block
        
        return section
    
    def _get_method_signature(self, method: Dict[str, Any]) -> str:
        """Get a clean method signature."""
        overloads = method.get('overloads', [])
        if overloads:
            signature = overloads[0].get('signature', '')
            if ' -> ' in signature:
                # Extract just the method part (before the return type)
                # The method_part already includes the closing parenthesis
                return signature.split(' -> ')[0]
            return signature
        
        return f"{method.get('name', '')}()"


class EnhancedClassDocumenter(ClassDocumenter):
    """Enhanced class documenter that includes JavaDoc information."""
    
    def add_content(self, more_content, no_docstring=False):
        """Add content including JavaDoc information."""
        # Get class name first to check if we have enhanced info
        try:
            class_name = self.object.__name__
        except AttributeError:
            # Handle mock objects or objects without __name__
            class_name = getattr(self.object, '__name__', self.name.split('.')[-1])
        
        class_info = javadoc_info.get_class_info(class_name)
        
        if class_info:
            # If we have enhanced info, add only the JavaDoc content
            # Skip the original boilerplate content
            self._add_javadoc_content(class_info)
        else:
            # If no enhanced info, add original content as usual
            try:
                # Sphinx 8.x and newer
                super().add_content(more_content)
            except TypeError:
                # Older Sphinx versions
                super().add_content(more_content, no_docstring)
    
    def _add_javadoc_content(self, class_info: Dict[str, Any]):
        """Add JavaDoc content to the documentation."""
        # Get class name for generating the detailed documentation link
        class_name = class_info.get('class_name', '')
        package = class_info.get('package', '')
        
        # Add JavaDoc description (without heading)
        javadoc_desc = class_info.get('javadoc_description', '')
        if javadoc_desc:
            self.add_line('', '<autodoc>')
            self.add_line(javadoc_desc, '<autodoc>')
            self.add_line('', '<autodoc>')
            
            # Add link to detailed documentation
            if class_name:
                # Convert class name to lowercase and create the link
                class_name_lower = class_name.lower()
                
                # Determine the package path for the link (relative from api_auto directory)
                if 'analysis' in package:
                    doc_link = f'`{class_name} detailed documentation <../pysnt/analysis/{class_name_lower}_doc.html>`_'
                elif 'annotation' in package:
                    doc_link = f'`{class_name} detailed documentation <../pysnt/annotation/{class_name_lower}_doc.html>`_'
                elif 'io' in package:
                    doc_link = f'`{class_name} detailed documentation <../pysnt/io/{class_name_lower}_doc.html>`_'
                elif 'util' in package:
                    doc_link = f'`{class_name} detailed documentation <../pysnt/util/{class_name_lower}_doc.html>`_'
                elif 'viewer' in package:
                    doc_link = f'`{class_name} detailed documentation <../pysnt/viewer/{class_name_lower}_doc.html>`_'
                elif 'tracing' in package:
                    doc_link = f'`{class_name} detailed documentation <../pysnt/tracing/{class_name_lower}_doc.html>`_'
                else:
                    # Root package classes
                    doc_link = f'`{class_name} detailed documentation <../pysnt/{class_name_lower}_doc.html>`_'
                
                self.add_line(f'**All Methods and Attributes:** See {doc_link} for comprehensive information.', '<autodoc>')
                self.add_line('', '<autodoc>')
    



def setup(app: Sphinx) -> Dict[str, Any]:
    """Setup the Sphinx extension."""
    
    # Add the JavaDoc directive
    app.add_directive('javadoc', JavaDocDirective)
    
    # Replace the default class documenter
    app.add_autodocumenter(EnhancedClassDocumenter, override=True)
    
    # Add configuration values
    app.add_config_value('javadoc_enhanced_json_dir', None, 'env')
    app.add_config_value('javadoc_auto_inject', True, 'env')
    
    # Connect to events
    app.connect('builder-inited', on_builder_inited)
    
    return {
        'version': '1.0.0',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }


def on_builder_inited(app: Sphinx):
    """Handle builder initialization."""
    # Reload JavaDoc info when building
    global javadoc_info
    javadoc_info = JavaDocInfo()
    
    logger.info(f"Enhanced JavaDoc Sphinx extension initialized with {len(javadoc_info.enhanced_data)} classes")