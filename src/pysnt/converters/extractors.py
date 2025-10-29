"""
Graph vertex and edge attribute extraction functionality.

This module handles extraction of attributes from graph vertices and edges,
including:
- Base extractor classes (VertexExtractor, EdgeExtractor)
- Concrete extractor implementations for different data types
- Extractor registries for automatic type detection
- Type detection functions for vertices and edges
- Color attribute extraction utilities

Dependencies: core.py
"""

from typing import Any, Dict, List, Optional

from .core import logger, _extract_color_attributes, _get_java_class_name


class VertexExtractor:
    """Base class for vertex attribute extraction."""
    
    def extract_attributes(self, vertex: Any, requested_attrs: List[str]) -> Dict[str, Any]:
        """Extract attributes from a vertex object."""
        raise NotImplementedError
    
    def get_default_attributes(self) -> List[str]:
        """Get default attributes to extract for this vertex type."""
        raise NotImplementedError
    
    def get_display_position(self, vertex: Any) -> Optional[tuple]:
        """Get (x, y) position for display, or None if not available."""
        return None


class EdgeExtractor:
    """Base class for edge attribute extraction."""

    def extract_attributes(self, edge: Any, requested_attrs: List[str]) -> Dict[str, Any]:
        """Extract attributes from an edge object."""
        raise NotImplementedError

    def get_default_attributes(self) -> List[str]:
        """Get default attributes to extract for this edge type."""
        raise NotImplementedError

class SWCPointExtractor(VertexExtractor):
    """Extractor for SWCPoint vertices."""
    
    def extract_attributes(self, vertex: Any, requested_attrs: List[str]) -> Dict[str, Any]:
        """Extract attributes from SWCPoint vertex."""
        attrs = {}
        
        # Direct field access (JPype handles type conversion)
        direct_fields = ["x", "y", "z", "radius", "type", "id", "parent"]
        
        # Methods that return objects needing special handling (python -> Java mapping)
        methods = {"annotation": "getAnnotation", "color": "getColor"}
        
        for attr in requested_attrs:
            try:
                # Direct field access
                if attr in direct_fields and hasattr(vertex, attr):
                    attrs[attr] = getattr(vertex, attr)
                
                # Method-based access for complex objects
                elif attr in methods and hasattr(vertex, methods[attr]):
                    method = getattr(vertex, methods[attr])
                    value = method()
                    
                    if value is not None:
                        if attr == "annotation": # Handle BrainAnnotation object
                            attrs[attr] = value  # Store the BrainAnnotation object itself
                            try: # Also extract common BrainAnnotation attributes
                                if hasattr(value, 'id'):
                                    attrs['annotation_id'] = value.id()
                                if hasattr(value, 'name'):
                                    attrs['annotation_name'] = value.name()
                                if hasattr(value, 'acronym'):
                                    attrs['annotation_acronym'] = value.acronym()
                            except Exception as e:
                                logger.debug(f"Could not extract BrainAnnotation details: {e}")
                        
                        elif attr == "color":
                            # Extract color attributes using enhanced helper
                            color_attrs = _extract_color_attributes(value, "color")
                            attrs.update(color_attrs)
                        
                        else:
                            attrs[attr] = value
                
                # Handle nested attribute requests (e.g., 'annotation_id', 'color_rgb')
                elif '_' in attr:
                    base_attr, sub_attr = attr.split('_', 1)
                    if base_attr in methods and hasattr(vertex, methods[base_attr]):
                        method = getattr(vertex, methods[base_attr])
                        obj = method()

                        if obj is not None:
                            if base_attr == "annotation": # Extract specific BrainAnnotation attribute
                                if sub_attr == 'id':
                                    attrs[attr] = obj.id()
                                elif sub_attr == 'name':
                                    attrs[attr] = obj.name()
                                elif sub_attr == 'acronym':
                                    attrs[attr] = obj.acronym()
                            
                            elif base_attr == "color":
                                # Extract specific Color attribute using enhanced helper
                                color_attrs = _extract_color_attributes(obj, "color")
                                if sub_attr == 'rgb' and 'color_rgb' in color_attrs:
                                    attrs[attr] = color_attrs['color_rgb']
                                elif sub_attr == 'hex' and 'color_hex' in color_attrs:
                                    attrs[attr] = color_attrs['color_hex']
                
            except Exception as e:
                logger.debug(f"Could not extract attribute '{attr}' from SWCPoint: {e}")
        
        return attrs
    
    def get_default_attributes(self) -> List[str]:
        """Default SWCPoint attributes."""
        return ['x', 'y', 'z', 'radius', 'type', 'id', 'parent', 'annotation_id', 'annotation_name', 'color_hex']
    
    def get_display_position(self, vertex: Any) -> Optional[tuple]:
        """Get (x, y, z) position from SWCPoint."""
        try:
            return vertex.x, vertex.y, vertex.z
        except Exception as e:
            logger.debug(f"Could not extract position from SWCPoint: {e}")
        return None


class BrainAnnotationExtractor(VertexExtractor):
    """Extractor for BrainAnnotation vertices."""
    
    def extract_attributes(self, vertex: Any, requested_attrs: List[str]) -> Dict[str, Any]:
        """Extract attributes from BrainAnnotation vertex."""
        attrs = {}
        
        # Standard BrainAnnotation attributes via methods
        method_attrs = {
            'id': 'id',
            'name': 'name',
            'acronym': 'acronym',
            'color': 'color'
        }
        
        for attr in requested_attrs:
            try:
                # Try method-based access
                if attr in method_attrs and hasattr(vertex, method_attrs[attr]):
                    method = getattr(vertex, method_attrs[attr])
                    value = method()
                    
                    # Handle special cases
                    if attr == 'color' and value is not None:
                        # Convert ColorRGB to hex string or RGB tuple using enhanced helper
                        color_attrs = _extract_color_attributes(value, "color")
                        if color_attrs:
                            attrs.update(color_attrs)
                        else:
                            attrs[attr] = str(value)  # Fallback to string representation
                    else:
                        attrs[attr] = value
                        
                # Try direct attribute access
                elif hasattr(vertex, attr):
                    value = getattr(vertex, attr)
                    attrs[attr] = value
                    
            except Exception as e:
                logger.debug(f"Could not extract attribute '{attr}' from BrainAnnotation: {e}")
        
        # Add hierarchical information if available
        try:
            if hasattr(vertex, 'getParent'):
                parent = vertex.getParent()
                if parent is not None:
                    attrs['parent_id'] = parent.id() if hasattr(parent, 'id') else str(parent)
                    attrs['parent_name'] = parent.name() if hasattr(parent, 'name') else str(parent)
        except Exception as e:
            logger.debug(f"Could not extract parent information: {e}")
        
        return attrs
    
    def get_default_attributes(self) -> List[str]:
        """Default BrainAnnotation attributes."""
        return ['id', 'name', 'acronym', 'color']


class SWCWeightedEdgeExtractor(EdgeExtractor):
    """Extractor for SWCWeightedEdge edges."""
    
    def extract_attributes(self, edge: Any, requested_attrs: List[str]) -> Dict[str, Any]:
        """Extract attributes from SWCWeightedEdge."""
        attrs = {}
        
        for attr in requested_attrs:
            try:
                if attr == 'weight' and hasattr(edge, 'getWeight'):
                    attrs[attr] = edge.getWeight()  # JPype handles double->float conversion
                elif attr == 'length' and hasattr(edge, 'getLength'):
                    attrs[attr] = edge.getLength()  # JPype handles double->float conversion
                elif hasattr(edge, attr):
                    attrs[attr] = getattr(edge, attr)  # Direct access fallback
            except Exception as e:
                logger.debug(f"Could not extract attribute '{attr}' from SWCWeightedEdge: {e}")
        
        return attrs
    
    def get_default_attributes(self) -> List[str]:
        """Default SWCWeightedEdge attributes."""
        return ['weight', 'length']


class AnnotationWeightedEdgeExtractor(EdgeExtractor):
    """Extractor for AnnotationWeightedEdge edges."""
    
    def extract_attributes(self, edge: Any, requested_attrs: List[str]) -> Dict[str, Any]:
        """Extract attributes from AnnotationWeightedEdge."""
        attrs = {}
        
        for attr in requested_attrs:
            try:
                # Both weight and length return the same value (getWeight()) for AnnotationWeightedEdge
                if attr in ['weight', 'length'] and hasattr(edge, 'getWeight'):
                    attrs[attr] = edge.getWeight()  # JPype handles double->float conversion
                elif hasattr(edge, attr):
                    attrs[attr] = getattr(edge, attr)  # Direct access fallback
            except Exception as e:
                logger.debug(f"Could not extract attribute '{attr}' from AnnotationWeightedEdge: {e}")
        
        return attrs
    
    def get_default_attributes(self) -> List[str]:
        """Default AnnotationWeightedEdge attributes."""
        return ['weight', 'length']

# Registry for vertex and edge extractors
_VERTEX_EXTRACTORS = {
    'SWCPoint': SWCPointExtractor(),
    'BrainAnnotation': BrainAnnotationExtractor(),
}

_EDGE_EXTRACTORS = {
    'SWCWeightedEdge': SWCWeightedEdgeExtractor(),
    'AnnotationWeightedEdge': AnnotationWeightedEdgeExtractor(),
}


def _detect_vertex_type(graph: Any) -> str:
    """Detect the vertex type of a SNTGraph."""
    try:
        vertices = graph.vertexSet()
        if vertices:
            # Get first vertex to determine type
            first_vertex = next(iter(vertices))
            vertex_class_name = _get_java_class_name(first_vertex)
            
            # Check for known types
            if 'SWCPoint' in vertex_class_name:
                return 'SWCPoint'
            elif 'BrainAnnotation' in vertex_class_name:
                return 'BrainAnnotation'
            else:
                # Try interface detection for BrainAnnotation
                if (hasattr(first_vertex, 'id') and hasattr(first_vertex, 'name') and 
                    hasattr(first_vertex, 'acronym')):
                    return 'BrainAnnotation'
                
                logger.debug(f"Unknown vertex type: {vertex_class_name}")
                return 'Unknown'
    except Exception as e:
        logger.debug(f"Could not detect vertex type: {e}")
    
    return 'Unknown'


def _detect_edge_type(graph: Any) -> str:
    """Detect the edge type of an SNTGraph."""
    try:
        edges = graph.edgeSet()
        if edges:
            # Get first edge to determine type
            first_edge = next(iter(edges))
            edge_class_name = _get_java_class_name(first_edge)
            
            # Check for known types
            if 'SWCWeightedEdge' in edge_class_name:
                return 'SWCWeightedEdge'
            elif 'AnnotationWeightedEdge' in edge_class_name:
                return 'AnnotationWeightedEdge'
            else:
                logger.debug(f"Unknown edge type: {edge_class_name}")
                return 'Unknown'
    except Exception as e:
        logger.debug(f"Could not detect edge type: {e}")
    
    return 'Unknown'