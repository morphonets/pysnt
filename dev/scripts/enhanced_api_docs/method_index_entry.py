"""
Method index entry data structure.
Represents a single method entry in the searchable index.
"""

import re
from dataclasses import dataclass

from .json_enhancer import EnhancedMethodInfo


@dataclass
class MethodIndexEntry:
    """Represents a single method entry in the index."""
    
    def __init__(self, method: EnhancedMethodInfo, class_name: str, package: str):
        """Initialize method index entry."""
        self.method_name = method.name
        self.class_name = class_name
        self.package = package
        self.full_class_name = f"{package}.{class_name}" if package else class_name
        self.category = method.category
        self.javadoc_description = method.javadoc_description or ""
        self.short_description = self._create_short_description(method.javadoc_description)
        self.deprecated = method.deprecated
        self.since_version = method.since_version
        self.examples = method.examples or []
        
        # Extract signature and type information from first overload
        if method.overloads:
            first_overload = method.overloads[0]
            self.signature = first_overload.signature
            self.return_type = first_overload.return_type
            self.java_return_type = first_overload.java_return_type
            self.parameters = [(p.name, p.type, p.description) for p in first_overload.params]
            self.parameter_types = [p.type for p in first_overload.params]
            self.return_description = first_overload.return_description
        else:
            self.signature = f"{method.name}()"
            self.return_type = "void"
            self.java_return_type = "void"
            self.parameters = []
            self.parameter_types = []
            self.return_description = ""
        
        # Create searchable text
        self.searchable_text = self._create_searchable_text()
    
    def _create_short_description(self, description: str, max_length: int = 120) -> str:
        """Create short description for index display."""
        if not description:
            return "No description available"
        
        # Remove HTML tags and clean up
        clean_desc = re.sub(r'<[^>]+>', '', description)
        clean_desc = re.sub(r'\s+', ' ', clean_desc).strip()
        
        # Truncate if too long
        if len(clean_desc) > max_length:
            clean_desc = clean_desc[:max_length].rsplit(' ', 1)[0] + '...'
        
        return clean_desc
    
    def _create_searchable_text(self) -> str:
        """Create searchable text combining all relevant information."""
        searchable_parts = [
            self.method_name,
            self.class_name,
            self.package,
            self.category,
            self.javadoc_description,
            self.return_type,
            ' '.join(self.parameter_types),
            ' '.join([param[0] for param in self.parameters])  # parameter names
        ]
        
        return ' '.join(filter(None, searchable_parts)).lower()
    
    def matches_search(self, query: str) -> bool:
        """Check if this method matches a search query."""
        if not query:
            return True
        
        query_lower = query.lower()
        return query_lower in self.searchable_text
    
    def matches_filters(self, class_filter: str = None,
                       return_type_filter: str = None,
                       category_filter: str = None,
                       include_deprecated: bool = True) -> bool:
        """Check if this method matches the given filters."""
        if not include_deprecated and self.deprecated:
            return False
        
        if class_filter and class_filter.lower() not in self.class_name.lower():
            return False
        
        if return_type_filter and return_type_filter.lower() not in self.return_type.lower():
            return False
        
        if category_filter and category_filter.lower() != self.category.lower():
            return False
        
        return True
    
    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization."""
        return {
            'method_name': self.method_name,
            'class_name': self.class_name,
            'package': self.package,
            'full_class_name': self.full_class_name,
            'category': self.category,
            'short_description': self.short_description,
            'signature': self.signature,
            'return_type': self.return_type,
            'java_return_type': self.java_return_type,
            'parameters': self.parameters,
            'parameter_types': self.parameter_types,
            'deprecated': self.deprecated,
            'since_version': self.since_version,
            'has_examples': len(self.examples) > 0
        }