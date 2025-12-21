"""
Tree conversion utilities for PySNT.

This module provides functions to convert SNT Tree objects into Python data structures.
"""

import logging
import numpy as np
from typing import Any, Optional

from .core import _create_converter_result

logger = logging.getLogger(__name__)


def _is_snt_tree(obj) -> bool:
    """
    Check if object is an SNT Tree.
    
    Parameters
    ----------
    obj : Any
        Object to check
        
    Returns
    -------
    bool
        True if object is an SNT Tree, False otherwise
    """
    try:
        return hasattr(obj, 'getRoot') and hasattr(obj, 'getNodes') and hasattr(obj, 'setRadii')
    except (AttributeError, TypeError, RuntimeError):
        return False


def _convert_tree_to_points(tree, **kwargs) -> Optional[dict]:
    """
    Convert an SNT Tree to an SNTObject dictionary containing node coordinates.
    
    This is the internal converter function used by scyjava's conversion system.
    For direct usage, use tree_to_points() instead.
    
    Parameters
    ----------
    tree : Tree
        SNT Tree object
    **kwargs
        Additional conversion arguments (currently unused)
        
    Returns
    -------
    dict or None
        SNTObject dictionary with structure:
        {
            'data': numpy.ndarray,     # Array of shape (N, 3) with XYZ coordinates
            'metadata': dict,          # Conversion metadata (node_count, tree_label, etc.)
            'original_type': 'Tree',   # Original object type
            'error': None or str       # Error message if conversion failed
        }
        Returns None if conversion fails completely.
        
    Examples
    --------
    >>> import pysnt
    >>> pysnt.initialize()
    >>> service = pysnt.SNTService()
    >>> tree = service.demoTree('fractal')
    >>> points = pysnt.to_python(tree)  # Returns numpy array via converter
    >>> print(points.shape)  # (N, 3) for N nodes
    """
    try:
        logger.debug(f"Converting Tree to points array: {tree}")
        
        # Get all nodes from the tree
        nodes = tree.getNodes()
        if not nodes or len(nodes) == 0:
            logger.warning("Tree has no nodes")
            return _create_converter_result(
                np.empty((0, 3)), 
                'Tree', 
                error="Tree has no nodes"
            )
        
        # Extract XYZ coordinates from each node
        points = np.array([[n.getX(), n.getY(), n.getZ()] for n in nodes])
        
        logger.info(f"Successfully converted Tree to points array: shape {points.shape}")
        
        # Create metadata
        metadata = {
            'node_count': len(nodes),
            'tree_label': tree.getLabel() if hasattr(tree, 'getLabel') else None,
            'conversion_type': 'tree_to_points',
            'coordinate_system': 'xyz'
        }
        
        return _create_converter_result(points, 'Tree', **metadata)
        
    except Exception as e:
        logger.error(f"Failed to convert Tree to points: {e}")
        return _create_converter_result(
            None, 
            'Tree', 
            error=f"Tree conversion failed: {e}"
        )


def tree_to_points(tree):
    """
    Extract node coordinates from a Tree as a numpy array.
    
    This is a convenience function that extracts the numpy array directly.
    Tree objects are also automatically converted when using pysnt.to_python(),
    which returns the same numpy array.
    
    Parameters
    ----------
    tree : Tree
        PySNT Tree object
        
    Returns
    -------
    np.ndarray
        Array of shape (N, 3) containing XYZ coordinates
        
    Examples
    --------
    >>> from pysnt.converters import tree_to_points
    >>> points = tree_to_points(tree)
    >>> print(points.shape)  # (N, 3)
    
    >>> # Automatic conversion via pysnt.to_python() returns the same array:
    >>> points = pysnt.to_python(tree)  # Same numpy array result
    >>> print(points.shape)  # (N, 3)
    
    Notes
    -----
    The difference between this function and pysnt.to_python(tree):
    - tree_to_points(tree): Returns numpy array directly
    - pysnt.to_python(tree): Also returns numpy array (via registered converter)
    - _convert_tree_to_points(tree): Returns SNTObject dict (internal use only)
    """
    if not _is_snt_tree(tree):
        raise ValueError("Object is not an SNT Tree")
    
    result = _convert_tree_to_points(tree)
    if result and result.get('error') is None:
        return result['data']
    else:
        error_msg = result.get('error', 'Unknown error') if result else 'Conversion failed'
        raise RuntimeError(f"Tree conversion failed: {error_msg}")