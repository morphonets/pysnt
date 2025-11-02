"""
Core display functionality for PySNT.

This module contains the main display orchestration logic, object type detection,
and SNT-specific object handling.
"""

import logging
from typing import Any, Callable, Optional, Tuple

# Import utilities from our utils module
from .utils import (
    _is_snt_object,
    _is_snt_tree,
    _is_snt_path,
    _is_xarray_object,
    _handle_display_error,
    _validate_display_kwargs,
)
# Import from converters for functions we haven't moved yet
from ..converters.structured_data_converters import _convert_path_to_xarray

logger = logging.getLogger(__name__)

# Try to import optional dependencies
try:
    import matplotlib.pyplot as plt
    from matplotlib.figure import Figure
    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False
    Figure = None

try:
    import pandas # noqa
    HAS_PANDAS = True
except ImportError:
    HAS_PANDAS = False
    pandas = None


def display(obj: Any, **kwargs) -> Any:
    """
    Enhanced display function that handles raw Java objects, converted SNT objects, matplotlib
    figures, and xarray objects.
    
    This function automatically tries to convert Java objects using available converters
    and then displays the result.
    
    Parameters
    ----------
    obj : Any
        The object to display (Java objects, SNTObjects, matplotlib figures, xarray objects, etc.)
    **kwargs
        Additional arguments for display (e.g., cmap, title, format, scale, vmin, vmax)
        For ImagePlus objects:
        - frame, t, time, timepoint : int, optional
            Frame/timepoint to display (default: 1). Parameter names are case-insensitive.
    Returns
    -------
    Any
        The displayed object - either the converted SNTObject (for Java objects) or the original
        object (for already converted objects)
        
    Examples
    --------
    >>> # Direct usage with SNTChart
    >>> chart = stats.getHistogram('Branch length')
    >>> snt_obj = pysnt.display(chart)  # Returns SNTObject with matplotlib figure

    >>> # Direct usage with ImagePlus
    >>> skeleton = tree.getSkeleton2D()
    >>> snt_obj = pysnt.display(skeleton)  # Returns SNTObject with xarray data

    >>> # Works with already converted objects too - returns the same object
    >>> converted = pysnt.to_python(chart)
    >>> same_obj = pysnt.display(converted)  # Returns the matplotlib figure
    """
    logger.debug(f"display() called with object type: {type(obj)}")

    # Validate and normalize kwargs
    kwargs = _validate_display_kwargs(**kwargs)

    # Add recursion protection
    _recursion_key = f"_display_recursion_{id(obj)}"
    if kwargs.get('_internal', {}).get(_recursion_key, False):
        logger.error(f"Infinite recursion detected for object {type(obj)} - stopping")
        return None

    # Set recursion flag
    kwargs['_internal'][_recursion_key] = True

    try:
        # Handle special SNT object types that need preprocessing
        if _is_snt_tree(obj):
            logger.debug(f"Detected SNT Tree: {type(obj)}")
            try:
                obj = obj.getSkeleton2D()
                logger.debug(f"Got skeleton from tree: {type(obj)}")
            except Exception as e:
                logger.warning(f"Failed to get skeleton from tree: {e}")
                logger.info("Falling back to direct tree display...")
                # Fallback: try to convert the tree directly using converters
                try:
                    import scyjava as sj
                    converted = sj.to_python(obj)
                    if converted is not obj:
                        obj = converted
                        logger.debug(f"Converted tree using scyjava: {type(obj)}")
                    else:
                        logger.warning("No converter available for tree, will try generic display")
                except Exception as e2:
                    logger.warning(f"scyjava conversion also failed: {e2}")
        elif _is_snt_path(obj):
            obj = _convert_path_to_xarray(obj)

        # Detect object type and get appropriate handler
        obj_type, handler = _get_display_handler(obj)

        if handler is None:
            logger.warning(f"No handler found for object type: {type(obj)}")
            return None

        logger.debug(f"Detected object type: {obj_type}, using handler: {handler.__name__}")

        # Call the appropriate handler
        if obj_type == 'matplotlib_figure':
            logger.info(f"Displaying matplotlib figure directly with {len(obj.axes)} axes")
            # Import from visual_display module
            from .visual_display import _display_matplotlib_figure
            _display_matplotlib_figure(obj, **kwargs)
            return obj
        elif obj_type == 'xarray':
            logger.info(f"Displaying xarray object: {type(obj)}")
            # Import from data_display module
            from .data_display import _display_xarray
            _display_xarray(obj, **kwargs)
            return obj
        elif obj_type == 'snt_object':
            return _handle_snt_object_display(obj, **kwargs)
        elif obj_type in ['snt_table', 'snt_chart', 'snt_graph', 'pandas_dataframe']:
            return handler(obj, **kwargs)
        else:
            # For other types (imageplus, numpy_array, java_object)
            return handler(obj, **kwargs)

    except Exception as e:
        _handle_display_error(e, "Display operation", str(type(obj)))
        raise
    finally:
        # Clean up recursion flag
        if '_internal' in kwargs and _recursion_key in kwargs['_internal']:
            del kwargs['_internal'][_recursion_key]


def _get_display_handler(obj: Any) -> Tuple[str, Optional[Callable]]:
    """
    Determine the appropriate display handler for an object.
    
    Parameters
    ----------
    obj : Any
        The object to analyze
        
    Returns
    -------
    tuple
        (object_type, handler_function) where handler_function may be None
    """
    # Check for matplotlib figures
    if HAS_MATPLOTLIB and isinstance(obj, Figure):
        from .visual_display import _display_matplotlib_figure
        return 'matplotlib_figure', _display_matplotlib_figure

    # Check for xarray objects
    if _is_xarray_object(obj):
        from .data_display import _display_xarray
        return 'xarray', _display_xarray

    # Check for SNTObject dictionaries
    if _is_snt_object(obj):
        return 'snt_object', _handle_snt_object_display

    # Check for SNTTable objects
    from ..converters.structured_data_converters import _is_snt_table
    if _is_snt_table(obj):
        return 'snt_table', _display_snt_table

    # Check for SNTChart objects
    from ..converters.chart_converters import _is_snt_chart
    if _is_snt_chart(obj):
        return 'snt_chart', _display_snt_chart

    # Check for SNTGraph objects
    from ..converters.graph_converters import _is_snt_graph
    if _is_snt_graph(obj):
        return 'snt_graph', _display_snt_graph

    # Check for ImagePlus objects
    if str(type(obj)).find('ImagePlus') != -1:
        from .data_display import _display_imageplus
        return 'imageplus', _display_imageplus

    # Check for pandas DataFrames
    if HAS_PANDAS and isinstance(obj, pandas.DataFrame):
        from .data_display import _display_pandas_dataframe
        return 'pandas_dataframe', _display_pandas_dataframe

    # Check numpy arrays
    if hasattr(obj, 'shape') and hasattr(obj, 'dtype') and hasattr(obj, 'ndim'):
        from .visual_display import _display_array_data
        return 'numpy_array', lambda arr, **kw: _display_array_data(arr, "numpy array", **kw)

    # Default to Java object conversion
    return 'java_object', _display_with_auto_conversion


def _handle_snt_object_display(obj, **kwargs):
    """Handle display of SNTObject dictionaries."""
    logger.debug("Object is a converted SNTObject")
    
    if obj.get('error') is not None:
        logger.error(f"Error in SNTObject: {obj.get('error')}")
        return None

    data = obj.get('data')
    logger.debug(f"SNTObject data type: {type(data)}")

    if isinstance(data, Figure):
        logger.info(f"Displaying matplotlib figure from SNTObject with {len(data.axes)} axes")
        from .visual_display import _display_matplotlib_figure
        _display_matplotlib_figure(data, **kwargs)
        return obj
    elif _is_xarray_object(data):
        # Get size information safely for xarray objects
        try:
            if hasattr(data, 'sizes'):
                size_info = dict(data.sizes)  # For Dataset
            elif hasattr(data, 'shape'):
                size_info = data.shape  # For DataArray
            else:
                size_info = "unknown"
            logger.info(f"Displaying xarray object (sizes: {size_info})")
        except Exception as e:
            logger.info(f"Displaying xarray object (size info unavailable: {e})")

        # Pass metadata to display function for proper RGB/title handling
        metadata = obj.get('metadata', {})
        kwargs_with_metadata = kwargs.copy()
        kwargs_with_metadata['metadata'] = metadata
        
        # Display the xarray data with metadata
        from .data_display import _display_xarray
        _display_xarray(data, **kwargs_with_metadata)
        return obj
    elif hasattr(data, 'shape') and hasattr(data, 'dtype'):  # numpy array
        logger.info(f"Displaying numpy array (size: {data.size})")
        import numpy as np # noqa
        with np.printoptions(precision=3, suppress=True):
            print(data)
        return obj
    elif hasattr(data, 'number_of_nodes'):  # NetworkX graph
        logger.info(f"Displaying NetworkX graph ({type(data).__name__} with {data.number_of_nodes()} nodes, {data.number_of_edges()} edges)")
        try:
            # Extract graph type information from SNTObject metadata for smart defaults
            metadata = obj.get('metadata', {})
            graph_type = metadata.get('original_type', 'Unknown')
            
            # Create a copy of kwargs with graph type information
            kwargs_with_type = kwargs.copy()
            kwargs_with_type['graph_type'] = graph_type
            
            logger.debug(f"Using graph type '{graph_type}' for layout defaults")
            
            # Create matplotlib figure from NetworkX graph
            from .visual_display import _graph_to_matplotlib, _display_matplotlib_figure
            fig = _graph_to_matplotlib(data, **kwargs_with_type)
            _display_matplotlib_figure(fig, **kwargs)
            return obj
        except Exception as e:
            logger.error(f"Failed to display NetworkX graph: {e}")
            # Fallback to text representation
            print(f"NetworkX {type(data).__name__}:")
            print(f"  Nodes: {data.number_of_nodes()}")
            print(f"  Edges: {data.number_of_edges()}")
            if hasattr(data, 'is_directed'):
                print(f"  Directed: {data.is_directed()}")
            return obj
    else:
        logger.warning(f"SNTObject data is not supported: {type(data)}")
        return None


def _display_snt_table(obj, **kwargs):
    """
    Handler function for SNTTable display.
    
    Parameters
    ----------
    obj : SNTTable
        The SNTTable object to display
    **kwargs
        Additional display arguments
        
    Returns
    -------
    Any
        The result of the display operation
    """
    logger.info("Detected SNTTable object - converting and displaying...")
    
    try:
        # Convert SNTTable to SNTObject containing xarray Dataset
        from ..converters.structured_data_converters import _convert_snt_table
        converted = _convert_snt_table(obj, **kwargs)
        
        if converted.get('error') is not None:
            logger.error(f"SNTTable conversion failed: {converted.get('error')}")
            return None
            
        # Display the converted SNTObject
        return _handle_snt_object_display(converted, **kwargs)
        
    except Exception as e:
        _handle_display_error(e, "SNTTable display", "SNTTable")
        return None


def _display_snt_chart(obj, **kwargs):
    """
    Handler function for SNTChart display.
    
    Parameters
    ----------
    obj : SNTChart
        The SNTChart object to display
    **kwargs
        Additional display arguments
        
    Returns
    -------
    Any
        The result of the display operation
    """
    logger.info("Detected SNTChart object - converting and displaying...")
    
    try:
        # Convert SNTChart to SNTObject containing matplotlib Figure
        from ..converters.chart_converters import _convert_snt_chart
        converted = _convert_snt_chart(obj, **kwargs)
        
        if converted.get('error') is not None:
            logger.error(f"SNTChart conversion failed: {converted.get('error')}")
            return None
            
        # Display the converted SNTObject
        return _handle_snt_object_display(converted, **kwargs)
        
    except Exception as e:
        _handle_display_error(e, "SNTChart display", "SNTChart")
        return None


def _display_snt_graph(obj, **kwargs):
    """
    Handler function for SNTGraph display.
    
    Parameters
    ----------
    obj : SNTGraph
        The SNTGraph object to display
    **kwargs
        Additional display arguments
        
    Returns
    -------
    Any
        The result of the display operation
    """
    logger.info("Detected SNTGraph object - converting and displaying...")
    
    try:
        # Convert SNTGraph to SNTObject containing NetworkX Graph
        from ..converters.graph_converters import _convert_snt_graph
        converted = _convert_snt_graph(obj, **kwargs)
        
        if converted.get('error') is not None:
            logger.error(f"SNTGraph conversion failed: {converted.get('error')}")
            return None
            
        # Display the converted SNTObject
        return _handle_snt_object_display(converted, **kwargs)
        
    except Exception as e:
        _handle_display_error(e, "SNTGraph display", "SNTGraph")
        return None


def _display_with_auto_conversion(obj: Any, **kwargs) -> Any:
    """
    Attempt to display a raw Java object by trying available converters.
    
    Parameters
    ----------
    obj : Any
        Raw Java object to convert and display
    **kwargs
        Display arguments
        
    Returns
    -------
    Any
        Converted and displayed object, or None if conversion fails
    """
    logger.debug(f"Attempting auto-conversion for {type(obj)}")
    
    try:
        import scyjava as sj # noqa
        
        # Try scyjava's built-in conversion system
        logger.debug("Trying scyjava.to_python() with registered converters...")
        converted = sj.to_python(obj)
        
        if converted is not None and converted != obj:
            logger.debug(f"Successfully converted {type(obj)} to {type(converted)}")
            
            # Try to display the converted object
            return display(converted, **kwargs)
        else:
            logger.debug("scyjava.to_python() returned None or same object")
            
    except Exception as e:
        logger.debug(f"Auto-conversion failed: {e}")
    
    # Fallback to generic object display
    return _display_generic_object(obj, **kwargs)


def _display_generic_object(obj: Any, **kwargs) -> Any:
    """
    Enhanced fallback display function for any Python object.
    
    Parameters
    ----------
    obj : Any
        Object to display
    **kwargs
        Display arguments (ignored for generic display)
        
    Returns
    -------
    Any
        The original object
    """
    logger.info(f"Using generic display for {type(obj)}")
    
    print(f"Object type: {type(obj)}")
    print(f"Object: {obj}")
    
    # Provide helpful suggestions
    print("\nSuggested actions:")
    if hasattr(obj, 'display'):
        print("    • Try: obj.display()")
    if hasattr(obj, 'plot'):
        print("    • Try: obj.plot()")
    if hasattr(obj, '__str__') or hasattr(obj, '__repr__'):
        print("    • Try: print(obj)")
    print("    • Try: pysnt.to_python(obj) to convert")
    print("    • Try: print(dir(obj)) to list all attributes")
    
    return obj


# Handler registration system
