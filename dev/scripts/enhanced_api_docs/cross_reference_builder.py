"""
Cross-reference builder for the enhanced API documentation system.
Builds cross-references between classes, methods, and external resources.
"""

import re
from typing import Dict, List, Optional, Any

from .config import config
from .json_enhancer import EnhancedJSONStubData, EnhancedMethodInfo
from .logging_setup import get_logger

logger = get_logger('cross_reference_builder')


class CrossReferenceBuilder:
    """Builds comprehensive cross-references for enhanced API documentation."""
    
    def __init__(self):
        """Initialize the cross-reference builder."""
        self.logger = logger
        self.javadoc_base_url = config.get('javadoc.base_url', '')
        self.cross_reference_depth = config.get('generation.cross_reference_depth', 2)
        
        # Tutorial mappings - could be made configurable
        self.tutorial_mappings = self._load_tutorial_mappings()
        
        # Method similarity patterns for finding related methods
        self.similarity_patterns = {
            'analysis': [
                r'.*[Aa]nalyz', r'.*[Cc]alculat', r'.*[Mm]easur', r'.*[Cc]omput',
                r'.*[Ss]tatistic', r'.*[Mm]etric', r'.*[Ee]valuat'
            ],
            'visualization': [
                r'^draw[A-Z]', r'^render[A-Z]', r'^display[A-Z]', r'^show[A-Z]',
                r'^plot[A-Z]', r'^paint[A-Z]', r'.*[Cc]olor', r'.*[Vv]iew'
            ],
            'io_operations': [
                r'^load[A-Z]', r'^save[A-Z]', r'^read[A-Z]', r'^write[A-Z]',
                r'^import[A-Z]', r'^export[A-Z]', r'.*[Ff]ile', r'.*[Dd]irectory',
                r'.*[Ff]older'
            ],
            'getters': [
                r'^get[A-Z]', r'^is[A-Z]', r'^has[A-Z]', r'^can[A-Z]'
            ],
            'setters': [
                r'^set[A-Z]', r'^add[A-Z]', r'^remove[A-Z]', r'^clear[A-Z]'
            ]
        }
    
    def build_comprehensive_cross_references(self, enhanced_stub: EnhancedJSONStubData, 
                                           all_stubs: Dict[str, EnhancedJSONStubData]) -> Dict[str, Any]:
        """
        Build cross-reference data for a class.
        
        Args:
            enhanced_stub: Enhanced stub data for the target class
            all_stubs: All enhanced stub data for cross-reference resolution
            
        Returns:
            Dictionary containing all cross-reference data
        """
        self.logger.debug(f"Building cross-references for {enhanced_stub.class_name}")
        
        cross_ref_data = {
            'related_methods': self._find_related_methods(enhanced_stub, all_stubs),
            'related_classes': self._find_related_classes(enhanced_stub, all_stubs),
            'internal_links': self._build_internal_navigation_links(enhanced_stub, all_stubs),
            'tutorial_links': self._build_tutorial_links(enhanced_stub),
            'external_links': self._build_external_javadoc_links(enhanced_stub, all_stubs),
            'method_cross_references': self._build_method_cross_references(enhanced_stub, all_stubs),
            'package_navigation': self._build_package_navigation(enhanced_stub, all_stubs)
        }
        
        self.logger.info(f"Built cross-references for {enhanced_stub.class_name}: "
                        f"{len(cross_ref_data['related_methods'])} related methods, "
                        f"{len(cross_ref_data['related_classes'])} related classes")
        
        return cross_ref_data
    
    def _find_related_methods(self, enhanced_stub: EnhancedJSONStubData, 
                            all_stubs: Dict[str, EnhancedJSONStubData]) -> List[Dict[str, Any]]:
        """Find methods related to those in the current class."""
        related_methods = []
        seen_methods = set()
        
        # Find methods referenced in see_also
        for method in enhanced_stub.methods:
            for see_ref in method.see_also:
                related_method = self._resolve_see_also_reference(see_ref, all_stubs)
                if related_method and related_method['key'] not in seen_methods:
                    related_methods.append(related_method)
                    seen_methods.add(related_method['key'])
        
        # Find methods with similar functionality
        similar_methods = self._find_similar_methods_by_pattern(enhanced_stub, all_stubs)
        for method in similar_methods:
            if method['key'] not in seen_methods:
                related_methods.append(method)
                seen_methods.add(method['key'])
        
        # Find methods that return or accept instances of this class
        type_related_methods = self._find_type_related_methods(enhanced_stub, all_stubs)
        for method in type_related_methods:
            if method['key'] not in seen_methods:
                related_methods.append(method)
                seen_methods.add(method['key'])
        
        # Sort by relevance score
        related_methods.sort(key=lambda m: m.get('relevance_score', 0), reverse=True)
        
        # Limit to avoid clutter
        return related_methods[:10]
    
    def _find_related_classes(self, enhanced_stub: EnhancedJSONStubData, 
                            all_stubs: Dict[str, EnhancedJSONStubData]) -> List[Dict[str, Any]]:
        """Find classes related to the current class."""
        related_classes = []
        seen_classes = set()
        
        # Find classes from inheritance relationships
        inheritance_classes = self._find_inheritance_related_classes(enhanced_stub, all_stubs)
        for cls in inheritance_classes:
            if cls['name'] not in seen_classes:
                related_classes.append(cls)
                seen_classes.add(cls['name'])
        
        # Find classes from see_also references
        see_also_classes = self._find_see_also_classes(enhanced_stub, all_stubs)
        for cls in see_also_classes:
            if cls['name'] not in seen_classes:
                related_classes.append(cls)
                seen_classes.add(cls['name'])
        
        # Find classes in the same package
        package_classes = self._find_same_package_classes(enhanced_stub, all_stubs)
        for cls in package_classes:
            if cls['name'] not in seen_classes:
                related_classes.append(cls)
                seen_classes.add(cls['name'])
        
        # Find classes with similar functionality
        similar_classes = self._find_functionally_similar_classes(enhanced_stub, all_stubs)
        for cls in similar_classes:
            if cls['name'] not in seen_classes:
                related_classes.append(cls)
                seen_classes.add(cls['name'])
        
        # Sort by relevance
        related_classes.sort(key=lambda c: c.get('relevance_score', 0), reverse=True)
        
        return related_classes[:8]  # Limit to avoid clutter
    
    def _build_internal_navigation_links(self, enhanced_stub: EnhancedJSONStubData, 
                                       all_stubs: Dict[str, EnhancedJSONStubData]) -> List[Dict[str, Any]]:
        """Build internal documentation navigation links."""
        internal_links = []
        
        # Link to method index
        internal_links.append({
            'title': 'Method Index',
            'url': '../method_index.html',
            'description': 'Browse all methods by category and functionality',
            'type': 'navigation'
        })
        
        # Link to package overview
        same_package_classes = [
            name for name, stub in all_stubs.items() 
            if stub.package == enhanced_stub.package and name != enhanced_stub.class_name
        ]
        
        if same_package_classes:
            internal_links.append({
                'title': f'Package {enhanced_stub.package}',
                'url': f'../index.html#{self._sanitize_anchor(enhanced_stub.package)}',
                'description': f'Browse {len(same_package_classes)} other classes in this package',
                'type': 'package'
            })
        
        # Links to category pages for methods in this class
        class_categories = set(method.category for method in enhanced_stub.methods)
        for category in sorted(class_categories):
            safe_category = self._sanitize_filename(category)
            internal_links.append({
                'title': f'{category} Methods',
                'url': f'../category_{safe_category}.html',
                'description': f'Browse all {category.lower()} methods across all classes',
                'type': 'category'
            })
        
        # Link to main API documentation index
        internal_links.append({
            'title': 'API Documentation Home',
            'url': '../index.html',
            'description': 'Return to main API documentation index',
            'type': 'navigation'
        })
        
        return internal_links
    
    def _build_tutorial_links(self, enhanced_stub: EnhancedJSONStubData) -> List[Dict[str, Any]]:
        """Build links to relevant tutorials and examples."""
        tutorial_links = []
        
        # Check for direct class name matches
        if enhanced_stub.class_name in self.tutorial_mappings:
            tutorial_links.extend(self.tutorial_mappings[enhanced_stub.class_name])
        
        # Check for pattern-based matches
        class_name_lower = enhanced_stub.class_name.lower()
        
        # Visualization classes
        if any(pattern in class_name_lower for pattern in ['viewer', 'display', 'render', 'plot']):
            tutorial_links.append({
                'title': 'Visualization Examples',
                'url': '../notebooks/index.html#visualization',
                'description': 'Learn about visualization and display capabilities',
                'type': 'tutorial',
                'relevance': 'visualization'
            })
        
        # Analysis classes
        if any(pattern in class_name_lower for pattern in ['analyzer', 'statistics', 'metric', 'measure']):
            tutorial_links.append({
                'title': 'Analysis Tutorials',
                'url': '../notebooks/index.html#analysis',
                'description': 'Tutorials on morphological analysis techniques',
                'type': 'tutorial',
                'relevance': 'analysis'
            })
        
        # I/O classes
        if any(pattern in class_name_lower for pattern in ['loader', 'importer', 'reader', 'writer']):
            tutorial_links.append({
                'title': 'Data Import/Export Examples',
                'url': '../notebooks/index.html#io',
                'description': 'Examples of loading and importing neuronal data',
                'type': 'tutorial',
                'relevance': 'io'
            })
        
        # Tree-related classes
        if 'tree' in class_name_lower:
            tutorial_links.append({
                'title': 'Tree Analysis Workflows',
                'url': '../notebooks/01_single_cell_analysis.html',
                'description': 'Single-cell analysis examples',
                'type': 'tutorial',
                'relevance': 'tree_analysis'
            })
        
        # Add general getting started link if no specific tutorials found
        if not tutorial_links:
            tutorial_links.append({
                'title': 'Getting Started Guide',
                'url': '../quickstart.html',
                'description': 'Basic usage examples and getting started information',
                'type': 'guide',
                'relevance': 'general'
            })
        
        # Add notebook index for all classes
        tutorial_links.append({
            'title': 'All Tutorials and Examples',
            'url': '../notebooks/index.html',
            'description': 'Browse all available tutorials and example notebooks',
            'type': 'index',
            'relevance': 'general'
        })
        
        return tutorial_links
    
    def _build_external_javadoc_links(self, enhanced_stub: EnhancedJSONStubData, 
                                    all_stubs: Dict[str, EnhancedJSONStubData]) -> List[Dict[str, Any]]:
        """Build links to external JavaDoc documentation."""
        external_links = []
        
        if not self.javadoc_base_url:
            return external_links
        
        # Link to this class's JavaDoc
        package_path = enhanced_stub.package.replace('.', '/')
        javadoc_url = f"{self.javadoc_base_url}{package_path}/{enhanced_stub.class_name}.html"
        external_links.append({
            'title': f"JavaDoc for {enhanced_stub.class_name}",
            'url': javadoc_url,
            'type': 'javadoc',
            'description': 'Official JavaDoc documentation for this class'
        })
        
        # Links to related class JavaDocs (from inheritance)
        if enhanced_stub.inheritance:
            for parent_class in enhanced_stub.inheritance.get('extends', []):
                if parent_class in all_stubs:
                    parent_stub = all_stubs[parent_class]
                    parent_package_path = parent_stub.package.replace('.', '/')
                    parent_javadoc_url = f"{self.javadoc_base_url}{parent_package_path}/{parent_class}.html"
                    external_links.append({
                        'title': f"JavaDoc for {parent_class} (Parent)",
                        'url': parent_javadoc_url,
                        'type': 'related_javadoc',
                        'description': f'JavaDoc for parent class {parent_class}'
                    })
            
            for interface in enhanced_stub.inheritance.get('implements', []):
                if interface in all_stubs:
                    interface_stub = all_stubs[interface]
                    interface_package_path = interface_stub.package.replace('.', '/')
                    interface_javadoc_url = f"{self.javadoc_base_url}{interface_package_path}/{interface}.html"
                    external_links.append({
                        'title': f"JavaDoc for {interface} (Interface)",
                        'url': interface_javadoc_url,
                        'type': 'related_javadoc',
                        'description': f'JavaDoc for implemented interface {interface}'
                    })
        
        # Link to package overview in JavaDoc
        package_javadoc_url = f"{self.javadoc_base_url}{package_path}/package-summary.html"
        external_links.append({
            'title': f"Package {enhanced_stub.package} JavaDoc",
            'url': package_javadoc_url,
            'type': 'package_javadoc',
            'description': f'JavaDoc overview for package {enhanced_stub.package}'
        })
        
        return external_links
    
    def _build_method_cross_references(self, enhanced_stub: EnhancedJSONStubData, 
                                     all_stubs: Dict[str, EnhancedJSONStubData]) -> Dict[str, List[Dict[str, Any]]]:
        """Build method-specific cross-references."""
        method_cross_refs = {}
        
        for method in enhanced_stub.methods:
            method_refs = []
            
            # Find overridden methods
            if enhanced_stub.inheritance:
                for parent_class in enhanced_stub.inheritance.get('extends', []):
                    if parent_class in all_stubs:
                        parent_method = self._find_method_in_class(all_stubs[parent_class], method.name)
                        if parent_method:
                            method_refs.append({
                                'type': 'overrides',
                                'class_name': parent_class,
                                'method_name': method.name,
                                'description': f'Overrides method from {parent_class}',
                                'link': f"{parent_class}.html#{method.name}"
                            })
            
            # Find methods that call this method (based on see_also references)
            for class_name, stub in all_stubs.items():
                if class_name == enhanced_stub.class_name:
                    continue
                
                for other_method in stub.methods:
                    for see_ref in other_method.see_also:
                        if (see_ref == f"{enhanced_stub.class_name}.{method.name}" or 
                            see_ref == method.name):
                            method_refs.append({
                                'type': 'referenced_by',
                                'class_name': class_name,
                                'method_name': other_method.name,
                                'description': f'Referenced by {class_name}.{other_method.name}',
                                'link': f"{class_name}.html#{other_method.name}"
                            })
            
            if method_refs:
                method_cross_refs[method.name] = method_refs
        
        return method_cross_refs
    
    def _build_package_navigation(self, enhanced_stub: EnhancedJSONStubData, 
                                all_stubs: Dict[str, EnhancedJSONStubData]) -> Dict[str, Any]:
        """Build package-level navigation information."""
        package_classes = [
            name for name, stub in all_stubs.items() 
            if stub.package == enhanced_stub.package
        ]
        
        # Find current class position in alphabetical order
        sorted_classes = sorted(package_classes)
        current_index = sorted_classes.index(enhanced_stub.class_name)
        
        navigation = {
            'package': enhanced_stub.package,
            'total_classes': len(package_classes),
            'current_position': current_index + 1,
            'previous_class': None,
            'next_class': None,
            'all_classes': sorted_classes
        }
        
        if current_index > 0:
            navigation['previous_class'] = {
                'name': sorted_classes[current_index - 1],
                'link': f"{sorted_classes[current_index - 1]}.html"
            }
        
        if current_index < len(sorted_classes) - 1:
            navigation['next_class'] = {
                'name': sorted_classes[current_index + 1],
                'link': f"{sorted_classes[current_index + 1]}.html"
            }
        
        return navigation
    
    def _resolve_see_also_reference(self, see_ref: str, 
                                  all_stubs: Dict[str, EnhancedJSONStubData]) -> Optional[Dict[str, Any]]:
        """Resolve a see_also reference to a method."""
        if '.' in see_ref:
            class_ref, method_ref = see_ref.rsplit('.', 1)
            if class_ref in all_stubs:
                method = self._find_method_in_class(all_stubs[class_ref], method_ref)
                if method:
                    return {
                        'class_name': class_ref,
                        'name': method.name,
                        'short_description': self._get_short_description(method.javadoc_description),
                        'category': method.category,
                        'internal_link': f"classes/{class_ref}.html#{method_ref}",
                        'relevance_score': 10,  # High relevance for explicit references
                        'key': f"{class_ref}.{method.name}",
                        'relationship': 'see_also'
                    }
        return None
    
    def _find_similar_methods_by_pattern(self, enhanced_stub: EnhancedJSONStubData, 
                                       all_stubs: Dict[str, EnhancedJSONStubData]) -> List[Dict[str, Any]]:
        """Find methods with similar patterns across all classes."""
        similar_methods = []
        
        # Get method patterns from current class
        class_patterns = set()
        for method in enhanced_stub.methods:
            for pattern_type, patterns in self.similarity_patterns.items():
                for pattern in patterns:
                    if re.search(pattern, method.name, re.IGNORECASE):
                        class_patterns.add(pattern_type)
        
        # Find methods in other classes with same patterns
        max_per_pattern = 2
        for pattern_type in class_patterns:
            found_count = 0
            for class_name, stub in all_stubs.items():
                if class_name == enhanced_stub.class_name or found_count >= max_per_pattern:
                    continue
                
                for method in stub.methods:
                    if method.deprecated:
                        continue
                    
                    for pattern in self.similarity_patterns[pattern_type]:
                        if re.search(pattern, method.name, re.IGNORECASE):
                            similar_methods.append({
                                'class_name': class_name,
                                'name': method.name,
                                'short_description': self._get_short_description(method.javadoc_description),
                                'category': method.category,
                                'internal_link': f"classes/{class_name}.html#{method.name}",
                                'relevance_score': 6,
                                'key': f"{class_name}.{method.name}",
                                'relationship': f'similar_{pattern_type}'
                            })
                            found_count += 1
                            break
                    
                    if found_count >= max_per_pattern:
                        break
        
        return similar_methods
    
    def _find_type_related_methods(self, enhanced_stub: EnhancedJSONStubData, 
                                 all_stubs: Dict[str, EnhancedJSONStubData]) -> List[Dict[str, Any]]:
        """Find methods that return or accept instances of this class."""
        type_related = []
        class_name = enhanced_stub.class_name
        
        for other_class_name, stub in all_stubs.items():
            if other_class_name == class_name:
                continue
            
            for method in stub.methods:
                if method.deprecated:
                    continue
                
                # Check return types
                for overload in method.overloads:
                    if class_name in overload.return_type or class_name in overload.java_return_type:
                        type_related.append({
                            'class_name': other_class_name,
                            'name': method.name,
                            'short_description': self._get_short_description(method.javadoc_description),
                            'category': method.category,
                            'internal_link': f"classes/{other_class_name}.html#{method.name}",
                            'relevance_score': 8,
                            'key': f"{other_class_name}.{method.name}",
                            'relationship': f'returns_{class_name}'
                        })
                        break
                    
                    # Check parameter types
                    for param in overload.params:
                        if class_name in param.type or class_name in param.java_type:
                            type_related.append({
                                'class_name': other_class_name,
                                'name': method.name,
                                'short_description': self._get_short_description(method.javadoc_description),
                                'category': method.category,
                                'internal_link': f"classes/{other_class_name}.html#{method.name}",
                                'relevance_score': 7,
                                'key': f"{other_class_name}.{method.name}",
                                'relationship': f'accepts_{class_name}'
                            })
                            break
        
        return type_related
    
    def _find_inheritance_related_classes(self, enhanced_stub: EnhancedJSONStubData, 
                                        all_stubs: Dict[str, EnhancedJSONStubData]) -> List[Dict[str, Any]]:
        """Find classes related through inheritance."""
        related_classes = []
        
        if not enhanced_stub.inheritance:
            return related_classes
        
        # Parent classes
        for parent_class in enhanced_stub.inheritance.get('extends', []):
            if parent_class in all_stubs:
                related_classes.append({
                    'name': parent_class,
                    'description': f"Parent class of {enhanced_stub.class_name}",
                    'package': all_stubs[parent_class].package,
                    'internal_link': f"classes/{parent_class}.html",
                    'relationship': 'extends',
                    'relevance_score': 10
                })
        
        # Implemented interfaces
        for interface in enhanced_stub.inheritance.get('implements', []):
            if interface in all_stubs:
                related_classes.append({
                    'name': interface,
                    'description': f"Interface implemented by {enhanced_stub.class_name}",
                    'package': all_stubs[interface].package,
                    'internal_link': f"classes/{interface}.html",
                    'relationship': 'implements',
                    'relevance_score': 9
                })
        
        # Child classes
        for class_name, stub in all_stubs.items():
            if stub.inheritance:
                if enhanced_stub.class_name in stub.inheritance.get('extends', []):
                    related_classes.append({
                        'name': class_name,
                        'description': f"Subclass of {enhanced_stub.class_name}",
                        'package': stub.package,
                        'internal_link': f"classes/{class_name}.html",
                        'relationship': 'subclass',
                        'relevance_score': 8
                    })
                elif enhanced_stub.class_name in stub.inheritance.get('implements', []):
                    related_classes.append({
                        'name': class_name,
                        'description': f"Implements {enhanced_stub.class_name}",
                        'package': stub.package,
                        'internal_link': f"classes/{class_name}.html",
                        'relationship': 'implementer',
                        'relevance_score': 7
                    })
        
        return related_classes
    
    def _find_see_also_classes(self, enhanced_stub: EnhancedJSONStubData, 
                             all_stubs: Dict[str, EnhancedJSONStubData]) -> List[Dict[str, Any]]:
        """Find classes from see_also references."""
        related_classes = []
        
        for see_ref in enhanced_stub.see_also:
            if see_ref in all_stubs:
                related_classes.append({
                    'name': see_ref,
                    'description': self._get_short_description(all_stubs[see_ref].javadoc_description),
                    'package': all_stubs[see_ref].package,
                    'internal_link': f"classes/{see_ref}.html",
                    'relationship': 'see_also',
                    'relevance_score': 9
                })
        
        return related_classes
    
    def _find_same_package_classes(self, enhanced_stub: EnhancedJSONStubData, 
                                 all_stubs: Dict[str, EnhancedJSONStubData]) -> List[Dict[str, Any]]:
        """Find classes in the same package."""
        related_classes = []
        
        same_package_classes = [
            (name, stub) for name, stub in all_stubs.items() 
            if (stub.package == enhanced_stub.package and 
                name != enhanced_stub.class_name)
        ]
        
        # Limit to most relevant classes in package
        for class_name, stub in same_package_classes[:5]:
            related_classes.append({
                'name': class_name,
                'description': self._get_short_description(stub.javadoc_description) or f"Class in package {stub.package}",
                'package': stub.package,
                'internal_link': f"classes/{class_name}.html",
                'relationship': 'same_package',
                'relevance_score': 5
            })
        
        return related_classes
    
    def _find_functionally_similar_classes(self, enhanced_stub: EnhancedJSONStubData, 
                                         all_stubs: Dict[str, EnhancedJSONStubData]) -> List[Dict[str, Any]]:
        """Find classes with similar functionality based on method categories."""
        similar_classes = []
        
        # Get method categories from current class
        class_categories = set(method.category for method in enhanced_stub.methods)
        
        for class_name, stub in all_stubs.items():
            if class_name == enhanced_stub.class_name:
                continue
            
            # Calculate category overlap
            other_categories = set(method.category for method in stub.methods)
            overlap = class_categories.intersection(other_categories)
            
            if len(overlap) >= 2:  # Require at least 2 shared categories
                similarity_score = len(overlap) / len(class_categories.union(other_categories))
                
                similar_classes.append({
                    'name': class_name,
                    'description': self._get_short_description(stub.javadoc_description) or f"Similar functionality to {enhanced_stub.class_name}",
                    'package': stub.package,
                    'internal_link': f"classes/{class_name}.html",
                    'relationship': 'similar_functionality',
                    'relevance_score': int(similarity_score * 10),
                    'shared_categories': list(overlap)
                })
        
        # Sort by similarity and limit
        similar_classes.sort(key=lambda c: c['relevance_score'], reverse=True)
        return similar_classes[:3]
    
    def _find_method_in_class(self, enhanced_stub: EnhancedJSONStubData, method_name: str) -> Optional[EnhancedMethodInfo]:
        """Find a method by name in a class."""
        for method in enhanced_stub.methods:
            if method.name == method_name:
                return method
        return None
    
    def _get_short_description(self, description: str, max_length: int = 100) -> str:
        """Get short description for cross-references."""
        if not description:
            return "No description available"
        
        # Remove HTML tags and clean up
        clean_desc = re.sub(r'<[^>]+>', '', description)
        clean_desc = re.sub(r'\s+', ' ', clean_desc).strip()
        
        # Truncate if too long
        if len(clean_desc) > max_length:
            clean_desc = clean_desc[:max_length].rsplit(' ', 1)[0] + '...'
        
        return clean_desc
    
    def _sanitize_filename(self, filename: str) -> str:
        """Sanitize filename for file system compatibility."""
        sanitized = re.sub(r'[^\w\-_.]', '_', filename)
        sanitized = re.sub(r'_+', '_', sanitized)
        return sanitized.lower()
    
    def _sanitize_anchor(self, text: str) -> str:
        """Sanitize text for use as HTML anchor."""
        return re.sub(r'[^\w\-_.]', '-', text).lower()
    
    def _load_tutorial_mappings(self) -> Dict[str, List[Dict[str, Any]]]:
        """Load tutorial mappings for classes."""
        return {
            'Tree': [
                {
                    'title': 'Single Cell Analysis Tutorial',
                    'url': '../notebooks/01_single_cell_analysis.html',
                    'description': 'Learn how to analyze individual neuronal trees',
                    'type': 'tutorial',
                    'relevance': 'tree_analysis'
                }
            ],
            'TreeStatistics': [
                {
                    'title': 'Tree Statistics and Analysis',
                    'url': '../notebooks/02_hemisphere_analysis.html', 
                    'description': 'Statistical analysis of neuronal morphology',
                    'type': 'tutorial',
                    'relevance': 'statistics'
                }
            ],
            'ConvexHull': [
                {
                    'title': 'Convex Hull Analysis',
                    'url': '../notebooks/2_convex_hull.html',
                    'description': 'Computing and analyzing convex hulls of neuronal structures',
                    'type': 'tutorial',
                    'relevance': 'geometry'
                }
            ],
            'Viewer3D': [
                {
                    'title': 'Visualization Examples',
                    'url': '../notebooks/index.html#visualization',
                    'description': 'Interactive 3D visualization tutorials',
                    'type': 'tutorial',
                    'relevance': 'visualization'
                }
            ],
            'ShollAnalyzer': [
                {
                    'title': 'Sholl Analysis Tutorial',
                    'url': '../notebooks/index.html#sholl',
                    'description': 'Performing Sholl analysis on neuronal data',
                    'type': 'tutorial',
                    'relevance': 'analysis'
                }
            ],
            'PathManager': [
                {
                    'title': 'Path Management Examples',
                    'url': '../notebooks/index.html#paths',
                    'description': 'Managing and manipulating neuronal paths',
                    'type': 'tutorial',
                    'relevance': 'path_management'
                }
            ]
        }
    
    def generate_cross_reference_report(self, all_stubs: Dict[str, EnhancedJSONStubData]) -> Dict[str, Any]:
        """Generate a report on cross-reference coverage and quality."""
        report = {
            'summary': {
                'total_classes': len(all_stubs),
                'classes_with_inheritance': 0,
                'classes_with_see_also': 0,
                'total_cross_references': 0,
                'broken_references': 0
            },
            'inheritance_network': {},
            'reference_quality': {},
            'coverage_by_package': {}
        }
        
        for class_name, stub in all_stubs.items():
            cross_refs = self.build_comprehensive_cross_references(stub, all_stubs)
            
            # Count inheritance relationships
            if stub.inheritance and (stub.inheritance.get('extends') or stub.inheritance.get('implements')):
                report['summary']['classes_with_inheritance'] += 1
            
            # Count see_also references
            if stub.see_also:
                report['summary']['classes_with_see_also'] += 1
            
            # Count total cross-references
            total_refs = (len(cross_refs['related_methods']) + 
                         len(cross_refs['related_classes']) +
                         len(cross_refs['tutorial_links']))
            report['summary']['total_cross_references'] += total_refs
            
            # Store per-class quality metrics
            report['reference_quality'][class_name] = {
                'related_methods': len(cross_refs['related_methods']),
                'related_classes': len(cross_refs['related_classes']),
                'tutorial_links': len(cross_refs['tutorial_links']),
                'external_links': len(cross_refs['external_links']),
                'total_references': total_refs
            }
            
            # Package coverage
            package = stub.package
            if package not in report['coverage_by_package']:
                report['coverage_by_package'][package] = {
                    'classes': 0,
                    'total_references': 0,
                    'avg_references_per_class': 0
                }
            
            report['coverage_by_package'][package]['classes'] += 1
            report['coverage_by_package'][package]['total_references'] += total_refs
        
        # Calculate averages
        for package_data in report['coverage_by_package'].values():
            if package_data['classes'] > 0:
                package_data['avg_references_per_class'] = (
                    package_data['total_references'] / package_data['classes']
                )
        
        return report