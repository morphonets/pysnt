"""
RST template system for the enhanced API documentation generation.
Provides Jinja2-based templates for generating Sphinx-compatible RST files.
"""

import re
from datetime import datetime
from typing import Dict, List, Any

from jinja2 import Environment, BaseLoader

from .logging_setup import get_logger

logger = get_logger('rst_templates')


class RSTTemplateLoader(BaseLoader):
    """Custom Jinja2 loader for RST templates."""
    
    def __init__(self):
        """Initialize the template loader with built-in templates."""
        self.templates = self._load_builtin_templates()
    
    def get_source(self, environment: Environment, template: str):
        """Get template source for Jinja2."""
        if template not in self.templates:
            raise FileNotFoundError(f"Template '{template}' not found")
        
        source = self.templates[template]
        return source, None, lambda: True
    
    def list_templates(self):
        """List available templates."""
        return list(self.templates.keys())
    
    def _load_builtin_templates(self) -> Dict[str, str]:
        """Load built-in RST templates."""
        return {
            'class_page': self._get_class_page_template(),
            'method_section': self._get_method_section_template(),
            'constructor_section': self._get_constructor_section_template(),
            'field_section': self._get_field_section_template(),
            'method_index': self._get_method_index_template(),
            'category_index': self._get_category_index_template(),
            'cross_reference': self._get_cross_reference_template()
        }
    
    def _get_class_page_template(self) -> str:
        """Template for individual class documentation pages."""
        return '''{{ class_name }}
{{ "=" * class_name|length }}

.. currentmodule:: {{ package }}

{% if class_description %}
{{ class_description }}

{% endif %}

{% if inheritance.has_inheritance %}
**Inheritance:**

{% if inheritance.has_extends %}
* **Extends:** {% for parent in inheritance.extends %}:class:`{{ parent }}`{% if not loop.last %}, {% endif %}{% endfor %}

{% endif %}
{% if inheritance.has_implements %}
* **Implements:** {% for interface in inheritance.implements %}:class:`{{ interface }}`{% if not loop.last %}, {% endif %}{% endfor %}

{% endif %}
{% endif %}

{% if deprecated %}
.. deprecated:: {{ since_version or "Unknown" }}
   This class is deprecated.

{% endif %}

**Package:** ``{{ package }}``

{% if has_constructors %}
Constructors
============

{% for constructor in constructors %}
{% if constructor.has_overloads %}
{% for overload in constructor.overloads %}
.. method:: {{ class_name }}({% for param in overload.params %}{{ param.name }}{% if not loop.last %}, {% endif %}{% endfor %})

{% if overload.has_description %}
   {{ overload.description | indent(3) }}
{% endif %}

   **Signature:** ``{{ overload.signature }}``

{% if overload.has_params %}
   **Parameters:**

{% for param in overload.params %}
   * **{{ param.name }}** (``{{ param.type }}``){% if param.has_description %}: {{ param.description }}{% endif %}
{% endfor %}
{% endif %}

{% endfor %}
{% endif %}
{% endfor %}

{% endif %}

{% if has_fields %}
Fields
======

{% for field in fields %}
.. attribute:: {{ field.name }}

{% if field.has_description %}
   {{ field.description | indent(3) }}
{% endif %}

   **Type:** ``{{ field.type }}``
   
   **Visibility:** {{ field.visibility }}{% if field.static %}, static{% endif %}{% if field.final %}, final{% endif %}

{% if field.deprecated %}
   .. deprecated::
      This field is deprecated.
{% endif %}

{% endfor %}

{% endif %}

{% if has_methods %}
Methods
=======

{% for category, methods in method_categories.items() %}
{% if methods %}
{{ category }}
{{ "-" * category|length }}

{% for method in methods %}
.. method:: {{ method.name }}({% if method.overloads %}{% for param in method.overloads[0].params %}{{ param.name }}{% if not loop.last %}, {% endif %}{% endfor %}{% endif %})

{% if method.has_description %}
   {{ method.javadoc_description | indent(3) }}
{% endif %}

{% if method.deprecated %}
   .. deprecated:: {{ method.since_version or "Unknown" }}
      This method is deprecated.

{% endif %}

{% for overload in method.overloads %}
   **Signature:** ``{{ overload.signature }}``

{% if overload.has_params %}
   **Parameters:**

{% for param in overload.params %}
   * **{{ param.name }}** (``{{ param.type }}``){% if param.has_description %}: {{ param.description }}{% endif %}
{% endfor %}
{% endif %}

{% if overload.has_return_description %}
   **Returns:** (``{{ overload.return_type }}``) {{ overload.return_description }}
{% else %}
   **Returns:** ``{{ overload.return_type }}``
{% endif %}

{% if overload.has_throws %}
   **Throws:**

{% for exception, description in overload.throws.items() %}
   * **{{ exception }}**: {{ description }}
{% endfor %}
{% endif %}

{% if not loop.last %}

{% endif %}
{% endfor %}

{% if method.has_examples %}
   **Examples:**

{% for example in method.examples %}
   .. code-block:: java

      {{ example | indent(6) }}
{% endfor %}
{% endif %}

{% if method.see_also %}
   **See Also:**

{% for ref in method.see_also %}
   * :meth:`{{ ref }}`
{% endfor %}
{% endif %}

{% endfor %}

{% endif %}
{% endfor %}

{% endif %}

{% if see_also %}
See Also
========

{% for ref in see_also %}
* :class:`{{ ref }}`
{% endfor %}

{% endif %}

{% if nested_classes %}
Nested Classes
==============

{% for nested in nested_classes %}
* :class:`{{ nested }}`
{% endfor %}

{% endif %}

{% if cross_references %}
{{ cross_references }}
{% endif %}

----

*Generated from JavaDoc and reflection data on {{ generation_timestamp }}*
'''
    
    def _get_method_section_template(self) -> str:
        """Template for method sections within class pages."""
        return '''{{ category }}
{{ "-" * category|length }}

{% for method in methods %}
.. automethod:: {{ method.name }}

{% if method.javadoc_description %}
   {{ method.javadoc_description | indent(3) }}
{% endif %}

{% if method.deprecated %}
   .. deprecated:: {{ method.since_version or "Unknown" }}
      This method is deprecated.
{% endif %}

{% for overload in method.overloads %}
   **Signature:** ``{{ overload.signature }}``
   
{% if overload.params %}
   **Parameters:**
   
{% for param in overload.params %}
   * **{{ param.name }}** (``{{ param.type }}``){% if param.description %}: {{ param.description }}{% endif %}
{% endfor %}
{% endif %}

{% if overload.return_description %}
   **Returns:** {{ overload.return_description }}
{% endif %}

{% if overload.throws %}
   **Throws:**
   
{% for exception, description in overload.throws.items() %}
   * **{{ exception }}**: {{ description }}
{% endfor %}
{% endif %}

{% endfor %}

{% if method.examples %}
   **Examples:**
   
{% for example in method.examples %}
   .. code-block:: java
   
      {{ example | indent(6) }}
{% endfor %}
{% endif %}

{% if method.see_also %}
   **See Also:**
   
{% for ref in method.see_also %}
   * :meth:`{{ ref }}`
{% endfor %}
{% endif %}

{% endfor %}
'''
    
    def _get_constructor_section_template(self) -> str:
        """Template for constructor sections."""
        return '''Constructors
------------

{% for constructor in constructors %}
.. automethod:: {{ constructor.name }}

{% if constructor.description %}
   {{ constructor.description | indent(3) }}
{% endif %}

{% if constructor.overloads %}
{% for overload in constructor.overloads %}
   **Signature:** ``{{ overload.signature }}``
   
{% if overload.params %}
   **Parameters:**
   
{% for param in overload.params %}
   * **{{ param.name }}** (``{{ param.type }}``){% if param.description %}: {{ param.description }}{% endif %}
{% endfor %}
{% endif %}

{% endfor %}
{% endif %}

{% endfor %}
'''
    
    def _get_field_section_template(self) -> str:
        """Template for field sections."""
        return '''Fields
------

{% for field in fields %}
.. autoattribute:: {{ field.name }}

{% if field.description %}
   {{ field.description | indent(3) }}
{% endif %}

   **Type:** ``{{ field.type }}``

{% if field.deprecated %}
   .. deprecated::
      This field is deprecated.
{% endif %}

{% endfor %}
'''
    
    def _get_method_index_template(self) -> str:
        """Template for comprehensive method index."""
        return '''Method Index
============

This page provides a comprehensive index of all methods available in the SNT API, organized by functionality and searchable by name, return type, and category.

.. contents:: Quick Navigation
   :local:
   :depth: 2

{% for category, methods in method_categories.items() %}
{% if methods %}
{{ category }}
{{ "-" * category|length }}

.. list-table::
   :header-rows: 1
   :widths: 30 40 30

   * - Method
     - Class
     - Description
{% for method in methods %}
   * - :meth:`{{ method.class_name }}.{{ method.name }}`
     - :class:`{{ method.class_name }}`
     - {{ method.short_description or "No description available" }}
{% endfor %}

{% endif %}
{% endfor %}

Search by Return Type
---------------------

{% for return_type, methods in methods_by_return_type.items() %}
{% if methods %}
{{ return_type }}
{{ "^" * return_type|length }}

{% for method in methods %}
* :meth:`{{ method.class_name }}.{{ method.name }}` - {{ method.short_description or "No description" }}
{% endfor %}

{% endif %}
{% endfor %}

All Methods Alphabetically
---------------------------

{% for letter, methods in methods_alphabetical.items() %}
{% if methods %}
{{ letter }}
{{ "^" * letter|length }}

{% for method in methods %}
* :meth:`{{ method.class_name }}.{{ method.name }}` ({{ method.class_name }}) - {{ method.short_description or "No description" }}
{% endfor %}

{% endif %}
{% endfor %}

----

*Index generated on {{ generation_timestamp }}*
'''
    
    def _get_category_index_template(self) -> str:
        """Template for category-specific method index."""
        return '''{{ category }} Methods
{{ "=" * (category|length + 8) }}

This page lists all methods in the **{{ category }}** category.

{% if description %}
{{ description }}
{% endif %}

.. contents:: Methods in this Category
   :local:

{% for class_name, methods in methods_by_class.items() %}
{{ class_name }}
{{ "-" * class_name|length }}

{% for method in methods %}
.. automethod:: {{ class_name }}.{{ method.name }}

{% if method.javadoc_description %}
   {{ method.javadoc_description | indent(3) }}
{% endif %}

   **Signature:** ``{{ method.signature }}``

{% if method.examples %}
   **Example:**
   
   .. code-block:: java
   
      {{ method.examples[0] | indent(6) }}
{% endif %}

{% endfor %}

{% endfor %}

----

*Category index generated on {{ generation_timestamp }}*
'''
    
    def _get_cross_reference_template(self) -> str:
        """Template for cross-reference sections."""
        return '''{% if related_methods %}
Related Methods
---------------

{% for method in related_methods %}
* :meth:`{{ method.class_name }}.{{ method.name }}` - {{ method.short_description or "Related method" }}{% if method.relationship %} ({{ method.relationship.replace('_', ' ').title() }}){% endif %}
{% endfor %}
{% endif %}

{% if related_classes %}
Related Classes
---------------

{% for class_ref in related_classes %}
* :class:`{{ class_ref.name }}` - {{ class_ref.description or "Related class" }}{% if class_ref.relationship %} ({{ class_ref.relationship.replace('_', ' ').title() }}){% endif %}
{% endfor %}
{% endif %}

{% if package_navigation and package_navigation.total_classes > 1 %}
Package Navigation
------------------

**Package:** ``{{ package_navigation.package }}`` ({{ package_navigation.current_position }} of {{ package_navigation.total_classes }} classes)

{% if package_navigation.previous_class %}
* **Previous:** :class:`{{ package_navigation.previous_class.name }}`
{% endif %}
{% if package_navigation.next_class %}
* **Next:** :class:`{{ package_navigation.next_class.name }}`
{% endif %}

**All classes in this package:**

{% for class_name in package_navigation.all_classes %}
{% if class_name == package_navigation.all_classes[package_navigation.current_position - 1] %}
* **{{ class_name }}** (current)
{% else %}
* :class:`{{ class_name }}`
{% endif %}
{% endfor %}
{% endif %}

{% if internal_links %}
Documentation Navigation
------------------------

{% for link in internal_links %}
* `{{ link.title }} <{{ link.url }}>`_ - {{ link.description }}
{% endfor %}
{% endif %}

{% if tutorial_links %}
Tutorials and Examples
----------------------

{% for tutorial in tutorial_links %}
* `{{ tutorial.title }} <{{ tutorial.url }}>`_ - {{ tutorial.description }}
{% endfor %}
{% endif %}

{% if external_links %}
External Documentation
----------------------

{% for link in external_links %}
* `{{ link.title }} <{{ link.url }}>`_{% if link.type == 'javadoc' %} (Official JavaDoc){% elif link.type == 'related_javadoc' %} (Related JavaDoc){% elif link.type == 'package_javadoc' %} (Package JavaDoc){% endif %}
{% endfor %}
{% endif %}

{% if method_cross_references %}
Method Cross-References
-----------------------

{% for method_name, refs in method_cross_references.items() %}
**{{ method_name }}:**

{% for ref in refs %}
* {{ ref.description }} - :meth:`{{ ref.class_name }}.{{ ref.method_name }}`
{% endfor %}
{% endfor %}
{% endif %}
'''


class RSTTemplateEngine:
    """RST template engine using Jinja2 for generating Sphinx documentation."""
    
    def __init__(self):
        """Initialize the template engine."""
        self.logger = logger
        self.env = Environment(
            loader=RSTTemplateLoader(),
            trim_blocks=True,
            lstrip_blocks=True,
            keep_trailing_newline=True
        )
        
        # Add custom filters
        self.env.filters['rst_escape'] = self._rst_escape
        self.env.filters['rst_link'] = self._rst_link
        self.env.filters['short_description'] = self._short_description
        self.env.filters['indent'] = self._indent_filter
    
    def render_class_page(self, class_data: Dict[str, Any]) -> str:
        """
        Render a complete class documentation page.
        
        Args:
            class_data: Enhanced class data with JavaDoc and reflection info
            
        Returns:
            Rendered RST content for the class page
        """
        template = self.env.get_template('class_page')
        
        # Prepare template context
        context = self._prepare_class_context(class_data)
        
        try:
            rendered = template.render(**context)
            self.logger.debug(f"Rendered class page for {class_data.get('class_name', 'Unknown')}")
            return rendered
        except Exception as e:
            self.logger.error(f"Failed to render class page: {e}")
            raise
    
    def render_method_section(self, category: str, methods: List[Dict[str, Any]]) -> str:
        """
        Render a method section for a specific category.
        
        Args:
            category: Method category name
            methods: List of method data
            
        Returns:
            Rendered RST content for the method section
        """
        template = self.env.get_template('method_section')
        
        context = {
            'category': category,
            'methods': methods
        }
        
        try:
            rendered = template.render(**context)
            self.logger.debug(f"Rendered method section for category: {category}")
            return rendered
        except Exception as e:
            self.logger.error(f"Failed to render method section for {category}: {e}")
            raise
    
    def render_constructor_section(self, constructors: List[Dict[str, Any]]) -> str:
        """
        Render constructor documentation section.
        
        Args:
            constructors: List of constructor data
            
        Returns:
            Rendered RST content for constructors
        """
        template = self.env.get_template('constructor_section')
        
        context = {
            'constructors': constructors
        }
        
        try:
            rendered = template.render(**context)
            self.logger.debug("Rendered constructor section")
            return rendered
        except Exception as e:
            self.logger.error(f"Failed to render constructor section: {e}")
            raise
    
    def render_field_section(self, fields: List[Dict[str, Any]]) -> str:
        """
        Render field documentation section.
        
        Args:
            fields: List of field data
            
        Returns:
            Rendered RST content for fields
        """
        template = self.env.get_template('field_section')
        
        context = {
            'fields': fields
        }
        
        try:
            rendered = template.render(**context)
            self.logger.debug("Rendered field section")
            return rendered
        except Exception as e:
            self.logger.error(f"Failed to render field section: {e}")
            raise
    
    def render_method_index(self, index_data: Dict[str, Any]) -> str:
        """
        Render comprehensive method index page.
        
        Args:
            index_data: Method index data organized by categories and types
            
        Returns:
            Rendered RST content for method index
        """
        template = self.env.get_template('method_index')
        
        context = self._prepare_index_context(index_data)
        
        try:
            rendered = template.render(**context)
            self.logger.debug("Rendered method index")
            return rendered
        except Exception as e:
            self.logger.error(f"Failed to render method index: {e}")
            raise
    
    def render_category_index(self, category: str, category_data: Dict[str, Any]) -> str:
        """
        Render category-specific method index.
        
        Args:
            category: Category name
            category_data: Methods and metadata for the category
            
        Returns:
            Rendered RST content for category index
        """
        template = self.env.get_template('category_index')
        
        context = {
            'category': category,
            'description': category_data.get('description', ''),
            'methods_by_class': category_data.get('methods_by_class', {}),
            'generation_timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        try:
            rendered = template.render(**context)
            self.logger.debug(f"Rendered category index for: {category}")
            return rendered
        except Exception as e:
            self.logger.error(f"Failed to render category index for {category}: {e}")
            raise
    
    def render_cross_references(self, cross_ref_data: Dict[str, Any]) -> str:
        """
        Render cross-reference section.
        
        Args:
            cross_ref_data: Cross-reference data including related methods and classes
            
        Returns:
            Rendered RST content for cross-references
        """
        template = self.env.get_template('cross_reference')
        
        try:
            rendered = template.render(**cross_ref_data)
            self.logger.debug("Rendered cross-references")
            return rendered
        except Exception as e:
            self.logger.error(f"Failed to render cross-references: {e}")
            raise
    
    def _prepare_class_context(self, class_data: Dict[str, Any]) -> Dict[str, Any]:
        """Prepare template context for class page rendering."""
        # Use method_categories directly from class_data if available
        method_categories = class_data.get('method_categories', {})
        
        # If not available, organize methods by category
        if not method_categories and 'methods' in class_data:
            for method in class_data['methods']:
                category = method.get('category', 'Utilities')
                if category not in method_categories:
                    method_categories[category] = []
                method_categories[category].append(method)
        
        context = {
            'class_name': class_data.get('class_name', 'Unknown'),
            'package': class_data.get('package', ''),
            'class_description': class_data.get('javadoc_description', ''),
            'inheritance': class_data.get('inheritance', {'extends': [], 'implements': []}),
            'deprecated': class_data.get('deprecated', False),
            'since_version': class_data.get('since_version'),
            'constructors': class_data.get('constructors', []),
            'fields': class_data.get('fields', []),
            'method_categories': method_categories,
            'see_also': class_data.get('see_also', []),
            'nested_classes': class_data.get('nested_classes', []),
            'has_methods': len(method_categories) > 0,
            'has_fields': len(class_data.get('fields', [])) > 0,
            'has_constructors': len(class_data.get('constructors', [])) > 0,
            'cross_references': class_data.get('cross_references', ''),
            'generation_timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        return context
    
    def _prepare_index_context(self, index_data: Dict[str, Any]) -> Dict[str, Any]:
        """Prepare template context for method index rendering."""
        # Organize methods alphabetically
        methods_alphabetical = {}
        all_methods = index_data.get('all_methods', [])
        
        for method in all_methods:
            first_letter = method.get('name', 'Unknown')[0].upper()
            if first_letter not in methods_alphabetical:
                methods_alphabetical[first_letter] = []
            methods_alphabetical[first_letter].append(method)
        
        # Sort alphabetically
        for letter in methods_alphabetical:
            methods_alphabetical[letter].sort(key=lambda m: m.get('name', ''))
        
        context = {
            'method_categories': index_data.get('method_categories', {}),
            'methods_by_return_type': index_data.get('methods_by_return_type', {}),
            'methods_alphabetical': dict(sorted(methods_alphabetical.items())),
            'generation_timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        return context
    
    def _rst_escape(self, text: str) -> str:
        """Escape special RST characters."""
        if not text:
            return ""
        
        # Escape RST special characters
        text = text.replace('\\', '\\\\')
        text = text.replace('`', '\\`')
        text = text.replace('*', '\\*')
        text = text.replace('_', '\\_')
        text = text.replace('|', '\\|')
        
        return text
    
    def _rst_link(self, text: str, target: str) -> str:
        """Create RST link."""
        return f"`{text} <{target}>`_"
    
    def _short_description(self, description: str, max_length: int = 100) -> str:
        """Create short description for index pages."""
        if not description:
            return "No description available"
        
        # Remove HTML tags if any
        clean_desc = re.sub(r'<[^>]+>', '', description)
        
        # Truncate if too long
        if len(clean_desc) > max_length:
            clean_desc = clean_desc[:max_length].rsplit(' ', 1)[0] + '...'
        
        return clean_desc
    
    def _indent_filter(self, text: str, spaces: int = 3) -> str:
        """Indent text by specified number of spaces."""
        if not text:
            return ""
        
        indent = ' ' * spaces
        lines = text.split('\n')
        indented_lines = [indent + line if line.strip() else line for line in lines]
        
        return '\n'.join(indented_lines)
    
    def get_available_templates(self) -> List[str]:
        """Get list of available templates."""
        return self.env.loader.list_templates()
    
    def validate_template_syntax(self, template_name: str) -> bool:
        """
        Validate template syntax.
        
        Args:
            template_name: Name of template to validate
            
        Returns:
            True if template syntax is valid, False otherwise
        """
        try:
            template = self.env.get_template(template_name)
            # Try to render with minimal context to check syntax
            minimal_context = {
                'class_name': 'TestClass',
                'package': 'test.package',
                'class_description': 'Test description',
                'inheritance': {'extends': [], 'implements': []},
                'deprecated': False,
                'since_version': None,
                'constructors': [],
                'fields': [],
                'method_categories': {},
                'see_also': [],
                'nested_classes': [],
                'generation_timestamp': '2024-01-01 00:00:00',
                'category': 'Test',
                'methods': [],
                'description': 'Test description',
                'methods_by_class': {},
                'method_categories': {},
                'methods_by_return_type': {},
                'methods_alphabetical': {},
                'related_methods': [],
                'related_classes': [],
                'external_links': []
            }
            template.render(**minimal_context)
            return True
        except Exception as e:
            self.logger.error(f"Template {template_name} has syntax errors: {e}")
            return False