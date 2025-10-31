"""
Display module for PySNT converters.

This module handles the display of converted objects, providing visualization functionality,
including:
- Main display functions and handler dispatch
- Specific display handlers for different object types
- Display utility functions for matplotlib and graph visualization
- Dataset display functions for xarray objects
- Array display functions and dataframe visualization
- Display handler registration system

Dependencies: core.py, chart_converters.py, structured_data_converters.py, graph_converters.py
"""

from typing import Any, Callable, Dict, List, Optional, Tuple
from pprint import pprint

import numpy as np  # noqa

# Import core utilities
from .core import (
    logger, _setup_matplotlib_interactive, _create_standard_figure,
    DEFAULT_CMAP, DEFAULT_NODE_COLOR, DEFAULT_NODE_SIZE, ERROR_MISSING_NETWORKX,
    _extract_color_attributes
)
# Import converter modules for type checking
from .structured_data_converters import _convert_path_to_xarray, _extract_imageplus_metadata

# Try to import optional dependencies
try:
    import matplotlib.pyplot as plt
    from matplotlib.figure import Figure
    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False
    Figure = None

try:
    import xarray # noqa
    HAS_XARRAY = True
except ImportError:
    HAS_XARRAY = False
    xarray = None

try:
    import networkx as nx # noqa
    HAS_NETWORKX = True
except ImportError:
    HAS_NETWORKX = False
    nx = None

try:
    import pandas # noqa
    HAS_PANDAS = True
except ImportError:
    HAS_PANDAS = False
    pandas = None

# Import lazy pandasgui function from core
from .core import _get_pandasgui_show


def _has_pandasgui():
    """Check if pandasgui is available using lazy import."""
    return _get_pandasgui_show() is not None


def _is_snt_object(obj: Any) -> bool:
    """Check if object is an SNTObject (TypedDict with required keys)."""
    return (isinstance(obj, dict) and 
            'type' in obj and 'data' in obj and 'metadata' in obj and 'error' in obj)


def _is_snt_tree(obj: Any) -> bool:
    """Check if object is an SNT Tree."""
    return str(type(obj)).find('Tree') != -1 and hasattr(obj, 'getSkeleton2D')


def _is_snt_path(obj: Any) -> bool:
    """Check if object is an SNT Path."""
    return str(type(obj)).find('Path') != -1 and hasattr(obj, 'getNodes')


def _is_xarray_object(obj: Any) -> bool:
    """Check if object is an xarray DataArray or Dataset."""
    if not HAS_XARRAY:
        return False
    return isinstance(obj, (xarray.Dataset, xarray.DataArray))


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
        return 'matplotlib_figure', _display_matplotlib_figure

    # Check for xarray objects
    if _is_xarray_object(obj):
        return 'xarray', _display_xarray

    # Check for SNTObject dictionaries
    if _is_snt_object(obj):
        return 'snt_object', _handle_snt_object_display

    # Check for SNTTable objects
    from .structured_data_converters import _is_snt_table
    if _is_snt_table(obj):
        return 'snt_table', _display_snt_table

    # Check for SNTChart objects
    from .chart_converters import _is_snt_chart
    if _is_snt_chart(obj):
        return 'snt_chart', _display_snt_chart

    # Check for SNTGraph objects
    from .graph_converters import _is_snt_graph
    if _is_snt_graph(obj):
        return 'snt_graph', _display_snt_graph

    # Check for ImagePlus objects
    if str(type(obj)).find('ImagePlus') != -1:
        return 'imageplus', _display_imageplus

    # Check for pandas DataFrames
    if HAS_PANDAS and isinstance(obj, pandas.DataFrame):
        return 'pandas_dataframe', _display_pandas_dataframe

    # Check numpy arrays
    if hasattr(obj, 'shape') and hasattr(obj, 'dtype') and hasattr(obj, 'ndim'):
        return 'numpy_array', lambda arr, **kw: _display_array_data(arr, "numpy array", **kw)

    # Default to Java object conversion
    return 'java_object', _display_with_auto_conversion


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

    # Add recursion protection
    _recursion_key = f"_display_recursion_{id(obj)}"
    if hasattr(kwargs, '_internal') and kwargs.get('_internal', {}).get(_recursion_key, False):
        logger.error(f"Infinite recursion detected for object {type(obj)} - stopping")
        return None

    # Set recursion flag
    if '_internal' not in kwargs:
        kwargs['_internal'] = {}
    kwargs['_internal'][_recursion_key] = True

    try:
        if _is_snt_tree(obj):
            obj = obj.getSkeleton2D()
        elif _is_snt_path(obj):
            from .. import Tree
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
            handler(obj, **kwargs)
            return obj
        elif obj_type == 'xarray':
            logger.info(f"Displaying xarray object: {type(obj)}")
            handler(obj, **kwargs)
            return obj
        elif obj_type == 'snt_object':
            return _handle_snt_object_display(obj, **kwargs)
        elif obj_type == 'snt_table':
            return handler(obj, **kwargs)
        elif obj_type == 'snt_chart':
            return handler(obj, **kwargs)
        elif obj_type == 'snt_graph':
            return handler(obj, **kwargs)
        elif obj_type == 'pandas_dataframe':
            return handler(obj, **kwargs)
        else:
            # For other types (imageplus, numpy_array, java_object)
            return handler(obj, **kwargs)

    except Exception as e:
        logger.error(f"Display failed: {e}")
        raise
    finally:
        # Clean up recursion flag
        if '_internal' in kwargs and _recursion_key in kwargs['_internal']:
            del kwargs['_internal'][_recursion_key]


def _handle_snt_object_display(obj, **kwargs):
    """Handle display of SNTObject dictionaries."""
    logger.debug("Object is a converted SNTObject")
    if obj.get('error') is not None:
        logger.error(f"Error in SNTObject: {obj['error']}")
        return None

    data = obj.get('data')
    logger.debug(f"SNTObject data type: {type(data)}")

    if isinstance(data, Figure):
        logger.info(f"Displaying matplotlib figure from SNTObject with {len(data.axes)} axes")
        _display_matplotlib_figure(data, **kwargs)
        return obj
    elif isinstance(data, (xarray.Dataset, xarray.DataArray)):
        # Get size information safely for xarray objects
        try:
            if hasattr(data, 'sizes'):
                size_info = dict(data.sizes)  # For Dataset
            elif hasattr(data, 'size'):
                size_info = data.size  # For DataArray
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
        _display_xarray(data, **kwargs_with_metadata)
        return obj
    elif isinstance(data, np.ndarray):
        logger.info(f"Displaying numpy array (size: {data.size})")
        with np.printoptions(precision=3, suppress=True):
            print(data)
        return obj
    elif HAS_NETWORKX and isinstance(data, (nx.Graph, nx.DiGraph, nx.MultiGraph, nx.MultiDiGraph)):
        logger.info(f"Displaying NetworkX graph ({type(data).__name__} with {data.number_of_nodes()} nodes, {data.number_of_edges()} edges)")
        try:
            # Extract graph type information from SNTObject metadata for smart defaults
            metadata = obj.get('metadata', {})
            
            # Determine graph type from metadata
            graph_type = 'Unknown'
            if 'vertex_type' in metadata and 'edge_type' in metadata:
                vertex_type = metadata['vertex_type']
                edge_type = metadata['edge_type']
                
                # Map vertex/edge types to original graph types
                if vertex_type == 'SWCPoint' and edge_type == 'SWCWeightedEdge':
                    graph_type = 'DirectedWeightedGraph'
                elif vertex_type == 'BrainAnnotation' and edge_type == 'AnnotationWeightedEdge':
                    graph_type = 'AnnotationGraph'
                else:
                    graph_type = f"{vertex_type}_{edge_type}"

            # Pass graph type for smart layout defaults
            kwargs_with_type = kwargs.copy()
            kwargs_with_type['graph_type'] = graph_type
            
            logger.debug(f"Using graph type '{graph_type}' for layout defaults")
            
            # Create matplotlib figure from NetworkX graph
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


def _display_snt_object(obj, **kwargs):
    """Handler function for SNTObject display (for dispatch table)."""
    return _handle_snt_object_display(obj, **kwargs)


def _display_snt_table(obj, **kwargs):
    """
    Handler function for SNTTable display.
    
    This function converts an SNTTable to xarray Dataset and then displays it
    using the appropriate display method based on configuration.
    
    Parameters
    ----------
    obj : SNTTable
        The SNTTable object to display
    **kwargs : dict
        Additional keyword arguments for display
        
    Returns
    -------
    Any
        The result of the display operation
    """
    logger.info("Detected SNTTable object - converting and displaying...")
    
    try:
        # Convert SNTTable to SNTObject containing xarray Dataset
        from .structured_data_converters import _convert_snt_table
        converted = _convert_snt_table(obj, **kwargs)
        
        if converted.get('error') is not None:
            logger.error(f"SNTTable conversion failed: {converted['error']}")
            return None
            
        # Display the converted SNTObject
        return _handle_snt_object_display(converted, **kwargs)
        
    except Exception as e:
        logger.error(f"SNTTable display failed: {e}")
        import traceback
        traceback.print_exc()
        return None


def _display_snt_chart(obj, **kwargs):
    """
    Handler function for SNTChart display.
    
    This function converts an SNTChart to matplotlib Figure and then displays it.
    
    Parameters
    ----------
    obj : SNTChart
        The SNTChart object to display
    **kwargs : dict
        Additional keyword arguments for display
        
    Returns
    -------
    Any
        The result of the display operation
    """
    logger.info("Detected SNTChart object - converting and displaying...")
    
    try:
        # Convert SNTChart to SNTObject containing matplotlib Figure
        from .chart_converters import _convert_snt_chart
        converted = _convert_snt_chart(obj, **kwargs)
        
        if converted.get('error') is not None:
            logger.error(f"SNTChart conversion failed: {converted['error']}")
            return None
            
        # Display the converted SNTObject
        return _handle_snt_object_display(converted, **kwargs)
        
    except Exception as e:
        logger.error(f"SNTChart display failed: {e}")
        import traceback
        traceback.print_exc()
        return None


def _display_snt_graph(obj, **kwargs):
    """
    Handler function for SNTGraph display.
    
    This function converts an SNTGraph to NetworkX Graph and then displays it
    as a matplotlib figure.
    
    Parameters
    ----------
    obj : SNTGraph
        The SNTGraph object to display
    **kwargs : dict
        Additional keyword arguments for display
        
    Returns
    -------
    Any
        The result of the display operation
    """
    logger.info("Detected SNTGraph object - converting and displaying...")
    
    try:
        # Convert SNTGraph to SNTObject containing NetworkX Graph
        from .graph_converters import _convert_snt_graph
        converted = _convert_snt_graph(obj, **kwargs)
        
        if converted.get('error') is not None:
            logger.error(f"SNTGraph conversion failed: {converted['error']}")
            return None
            
        # Display the converted SNTObject
        return _handle_snt_object_display(converted, **kwargs)
        
    except Exception as e:
        logger.error(f"SNTGraph display failed: {e}")
        import traceback
        traceback.print_exc()
        return None


def _display_pandas_dataframe(df, **kwargs):
    """
    Handler function for pandas DataFrame display.
    
    This function displays a pandas DataFrame using the configured display method
    (PandasGUI, console, etc.) based on the display.table_mode setting.
    
    Parameters
    ----------
    df : pandas.DataFrame
        The DataFrame to display
    **kwargs : dict
        Additional keyword arguments for display
        
    Returns
    -------
    pandas.DataFrame
        The original DataFrame
    """
    from ..config import get_option
    
    logger.info(f"Detected pandas DataFrame - displaying with shape {df.shape}")
    
    try:
        # Get display mode from configuration
        table_mode = kwargs.get('table_mode', get_option('display.table_mode')).lower()
        
        # Map table mode to display parameters
        if table_mode == 'pandasgui':
            kwargs['use_gui'] = True
        elif table_mode == 'basic':
            kwargs['use_gui'] = False
        else:
            # For other modes (summary, distribution, etc.), use GUI if available
            kwargs['use_gui'] = _has_pandasgui()
        
        # Use the existing DataFrame display function
        success = _show_pandasgui_dataframe(df, title=kwargs.get('title', 'DataFrame'), **kwargs)
        
        if not success:
            # Fallback to console display
            from ..config import get_option
            max_rows = kwargs.get('max_rows', get_option('display.max_rows'))
            max_cols = kwargs.get('max_cols', get_option('display.max_columns'))
            precision = kwargs.get('precision', get_option('display.precision'))
            
            with pandas.option_context('display.max_rows', max_rows,
                                     'display.max_columns', max_cols,
                                     'display.precision', precision,
                                     'display.width', None):
                print("pandas.DataFrame:")
                print(df)
                print(f"Shape: {df.shape}")
                if hasattr(df, 'describe'):
                    print("\nSummary statistics:")
                    print(df.describe())
        
        return df
        
    except Exception as e:
        logger.error(f"pandas DataFrame display failed: {e}")
        # Fallback to simple print
        print("pandas.DataFrame:")
        print(df)
        return df


def _display_imageplus(obj, **kwargs):
    """
    Handler function for ImagePlus display.
    
    This function extracts ImagePlus metadata and then converts to xarray
    for display with proper RGB/title handling.

    Parameters
    ----------
    obj : ImagePlus
        The ImagePlus object to display
    **kwargs : dict
        Additional keyword arguments:
        - frame, t, time, timepoint : int, optional
            Frame/timepoint to display (default: 1). Parameter names are case-insensitive.
        - title : str, optional
            Title for the display

    Returns
    -------
    xarray or None
        Converted xarray object if successful, None otherwise
    """
    logger.info("Detected ImagePlus object - extracting metadata and converting...")
    try:
        from ..util import ImpUtils
        from ..core import ij
        
        # Extract metadata first (before conversion to avoid recursion)
        metadata = _extract_imageplus_metadata(obj, **kwargs)
        
        # Convert ImagePlus to xarray using existing utilities
        # This bypasses the scyjava converter system to avoid recursion
        logger.debug("Converting ImagePlus to xarray using ImpUtils...")
        frame = int(metadata.get('frame', 1))
        converted_imp = ImpUtils.convertToSimple2D(obj, frame)
        
        # Use ij().py.from_java() but with recursion protection
        logger.debug("Converting to xarray using ij().py.from_java()...")
        xarray_data = ij().py.from_java(converted_imp)
        
        if xarray_data is None:
            logger.error("Failed to convert ImagePlus to xarray - got None")
            return None
        
        # Update metadata with actual xarray information
        metadata['original_shape'] = getattr(xarray_data, 'shape', None)
        metadata['dtype'] = str(getattr(xarray_data, 'dtype', 'unknown'))
        
        # Add metadata to kwargs for display functions
        kwargs_with_metadata = kwargs.copy()
        kwargs_with_metadata['metadata'] = metadata
        
        # Display the xarray data with metadata
        logger.info(f"Displaying ImagePlus '{metadata.get('image_title', 'Unknown')}' "
                   f"({'RGB' if metadata.get('is_rgb', False) else 'grayscale'})")
        _display_xarray(xarray_data, **kwargs_with_metadata)
        
        return xarray_data

    except Exception as e:
        logger.error(f"ImagePlus display failed: {e}")
        import traceback
        traceback.print_exc()
        return None


def _display_xarray(xarr: Any, **kwargs) -> None:
    """
    Display a xarray DataArray or Dataset using matplotlib.
    
    This function handles xarray objects (from ImagePlus conversions or SNTTable conversions)
    and displays them using xarray's built-in plotting capabilities or matplotlib.
    
    Parameters
    ----------
    xarr : xarray.DataArray or xarray.Dataset
        The xarray object to display
    **kwargs
        Additional arguments for display (e.g., cmap, title, vmin, vmax)
        
    Returns
    -------
    None
        This function performs display as a side effect
    """
    plt = _setup_matplotlib_interactive()

    logger.debug(f"Displaying xarray object: {type(xarr)}")

    try:
        # Get display parameters
        cmap = kwargs.get('cmap', DEFAULT_CMAP)
        title = kwargs.get('title', None)

        # Handle xarray Dataset (from SNTTable) vs DataArray (from ImagePlus)
        if str(type(xarr)).find('Dataset') != -1:
            logger.debug("Detected xarray Dataset - displaying as table/data summary")
            _display_xarray_dataset(xarr, **kwargs)
            return None

        # Method 1: Try xarray's built-in plot method for DataArray
        try:
            logger.debug("Trying xarray.plot() method...")

            # Check for metadata-based RGB detection (most reliable)
            metadata = kwargs.get('metadata', {})
            is_rgb = metadata.get('is_rgb', False)
            
            # Use metadata title if available and no title override provided
            if not title and 'image_title' in metadata:
                title = metadata['image_title']
            
            # Fallback to shape-based detection if no metadata available
            if not is_rgb and hasattr(xarr, 'shape') and len(xarr.shape) == 3 and xarr.shape[2] in [3, 4]:
                is_rgb = True
                logger.warning(f"Using fallback RGB detection for xarray shape {xarr.shape}. "
                              f"Consider using metadata-based detection for reliability.")
            
            logger.debug(f"RGB detection result: is_rgb={is_rgb}, metadata_available={bool(metadata)}")

            # Handle different dimensionalities
            if hasattr(xarr, 'ndim'):
                if xarr.ndim == 2:
                    # 2D image - use imshow-style plot
                    xarr.plot(cmap=cmap, add_colorbar=not is_rgb, **kwargs)
                elif xarr.ndim == 3:
                    if is_rgb:
                        # RGB image - plot directly without colormap
                        xarr.plot(add_colorbar=False, **kwargs)
                        if not title:
                            title = metadata.get('image_title', "RGB image")
                    else:
                        # 3D image - plot middle slice
                        middle_slice = xarr.shape[0] // 2
                        xarr[middle_slice].plot(cmap=cmap, add_colorbar=True, **kwargs)
                        if not title:
                            title = f"Slice {middle_slice} of 3D image"
                else:
                    # Higher dimensions - flatten to 2D
                    xarr.plot(cmap=cmap, add_colorbar=not is_rgb, **kwargs)
            else:
                # Fallback - just try to plot
                xarr.plot(cmap=cmap, add_colorbar=not is_rgb, **kwargs)

            # Add title if provided
            if title:
                plt.title(title)

            # Show the plot using unified display system
            if _show_matplotlib_figure():  # Uses current figure automatically
                logger.info("Successfully displayed xarray using xarray.plot()")
            else:
                logger.warning("Failed to display xarray plot")
            return None

        except Exception as e1:
            logger.debug(f"xarray.plot() failed: {e1}")
            logger.debug(f"xarray info - shape: {getattr(xarr, 'shape', 'unknown')}, "
                         f"dims: {getattr(xarr, 'dims', 'unknown')}, "
                         f"dtype: {getattr(xarr, 'dtype', 'unknown')}")

            # Method 2: Convert to numpy and use matplotlib directly
            try:
                logger.debug("Trying matplotlib imshow with numpy conversion...")

                # Convert to numpy array
                if hasattr(xarr, 'values'):
                    img_data = xarr.values
                elif hasattr(xarr, 'data'):
                    img_data = xarr.data
                else:
                    img_data = np.array(xarr)

                logger.debug(f"Converted to numpy array: shape={img_data.shape}, dtype={img_data.dtype}")
                # Use unified array display
                result = _display_array_data(img_data, "xarray", **kwargs)
                if result:
                    logger.info("Successfully displayed xarray using unified array display")
                    return result
                else:
                    logger.warning("Failed to display xarray using unified array display")
                return None

            except Exception as e2:
                logger.debug(f"matplotlib imshow failed: {e2}")

                # Method 3: Fallback - just show info about the object
                logger.warning(f"Could not display xarray object: {type(xarr)}")
                logger.info(f"xarray details:")
                logger.info(f"  - shape: {getattr(xarr, 'shape', 'unknown')}")
                logger.info(f"  - dims: {getattr(xarr, 'dims', 'unknown')}")
                logger.info(f"  - dtype: {getattr(xarr, 'dtype', 'unknown')}")
                logger.info(f"  - ndim: {getattr(xarr, 'ndim', 'unknown')}")
                logger.info(f"Troubleshooting:")
                logger.info(f"  1. Try: xarr.plot() directly")
                logger.info(f"  2. Try: plt.imshow(xarr.values)")
                logger.info(f"  3. Check if data contains NaN or invalid values")
                logger.info(f"Both xarray.plot() and matplotlib.imshow() failed - this may indicate data issues")

    except Exception as e:
        logger.error(f"Failed to display xarray object: {e}")


def _display_matplotlib_figure(fig: Figure, **kwargs) -> None:
    """
    Display a matplotlib figure using the unified display system.
    
    Parameters
    ----------
    fig : matplotlib.figure.Figure
        The figure to display
    **kwargs
        Additional display arguments
        
    Returns
    -------
    None
        This function performs display as a side effect
    """
    import matplotlib

    logger.info(f"Displaying matplotlib figure (backend: {matplotlib.get_backend()})")

    # Use the unified display system
    if _show_matplotlib_figure(fig, **kwargs):
        logger.info("Successfully displayed figure using unified display system")
    else:
        # Fallback methods if unified display fails
        try:
            # Method 2: Use figure's show method directly
            fig.show()
            logger.info("Successfully displayed figure using fig.show()")
        except Exception as e2:
            logger.debug(f"fig.show() failed: {e2}")
            try:
                # Method 3: Force display using canvas manager
                if hasattr(fig.canvas, 'manager') and hasattr(fig.canvas.manager, 'show'):
                    fig.canvas.manager.show()
                    logger.info("Successfully displayed figure using canvas.manager.show()")
                else:
                    # Fallback: draw and flush events
                    fig.canvas.draw()
                    fig.canvas.flush_events()
                    logger.info("Drew figure and flushed events as fallback")
            except Exception as e3:
                logger.debug(f"canvas manager show failed: {e3}")
                # Method 4: Save and display info as fallback
                logger.warning(f"Could not display figure directly. Figure created with {len(fig.axes)} axes.")
                logger.info("Figure is available but display failed - you may need to call plt.show() manually")


def _display_with_auto_conversion(obj: Any, **kwargs) -> Any:
    """
    Attempt to display a raw Java object by trying available converters.
    
    This function loops through available Python converters to find one that
    can handle the object, converts it, and then displays the result.
    
    Parameters
    ----------
    obj : Any
        Raw Java object to convert and display
    **kwargs
        Additional arguments for conversion and display
        
    Returns
    -------
    Any
        The result of the display operation
    """
    import scyjava as sj # noqa

    logger.debug(f"Attempting auto-conversion for {type(obj)}")

    # Special handling of ImagePlus objects
    if str(type(obj)).find('ImagePlus') != -1:
        logger.info("Detected ImagePlus object - attempting _display_imageplus...")
        return _display_imageplus(obj, **kwargs)

    # Try scyjava's built-in conversion system. This uses PySNT's registered converters
    try:
        logger.debug("Trying scyjava.to_python() with registered converters...")
        converted = sj.to_python(obj)
        logger.info(f"scyjava.to_python() succeeded: {type(converted)}")

        # Check if the conversion actually produced something useful
        if converted is obj:
            logger.debug("scyjava.to_python() returned the same object - no conversion occurred")
            raise ValueError("No conversion occurred")

        # Check if it's a xarray object or other displayable type
        if _is_xarray_object(converted):
            logger.debug(f"Converted object is xarray: {type(converted)}")
            _display_xarray(converted, **kwargs)
            return converted
        elif isinstance(converted, Figure):
            logger.debug(f"Converted object is matplotlib figure: {type(converted)}")
            _display_matplotlib_figure(converted, **kwargs)
            return converted
        elif _is_snt_object(converted):
            logger.debug(f"Converted object is SNTObject: {type(converted)}")
            return _display_snt_object(converted, **kwargs)
        else:
            logger.debug(f"Converted object type {type(converted)} is not directly displayable")
            # Check if it might be a numpy array or other image-like data
            if hasattr(converted, 'shape') and hasattr(converted, 'dtype'):
                logger.debug(f"Converted object has array-like properties: shape={converted.shape}")
                try:
                    return _display_array_data(converted, "converted array", **kwargs)
                except Exception as img_e:
                    logger.debug(f"Failed to display as image: {img_e}")

            logger.debug("Continuing to other conversion methods...")

    except Exception as e1:
        logger.debug(f"scyjava.to_python() failed: {e1}")

    # Enhanced fallbacks - try to display something useful about any object
    return _display_generic_object(obj, **kwargs)


def _show_matplotlib_figure(fig=None, **kwargs) -> bool: # noqa
    """
    Unified matplotlib figure display with enhanced window management.
    
    This function provides a single, consistent way to display matplotlib figures
    with proper window management, non-blocking behavior, and fallback handling.
    It can work with an existing figure or the current figure.
    
    Parameters
    ----------
    fig : matplotlib.figure.Figure, optional
        The figure to display. If None, uses plt.gcf() to get current figure.
    **kwargs
        Additional display arguments (currently unused but kept for future extensibility)
        
    Returns
    -------
    bool
        True if display succeeded, False otherwise
    """
    import matplotlib
    
    plt = _setup_matplotlib_interactive()

    # Get the figure to display
    if fig is None:
        fig = plt.gcf()  # Get current figure

    logger.debug(f"Showing matplotlib figure with unified display (backend: {matplotlib.get_backend()})")

    try:
        # Make figure current and show
        plt.figure(fig.number)  # Make this figure current
        logger.debug(f"Made figure {fig.number} current")

        # Force drawing and display
        fig.canvas.draw()
        fig.canvas.flush_events()
        logger.debug("Drew figure and flushed events")

        # Show with non-blocking to ensure it appears
        plt.show(block=False)
        logger.debug("Called plt.show(block=False)")

        # Additional attempts to make the window visible
        try:
            # Try to bring window to front
            if hasattr(fig.canvas, 'manager') and hasattr(fig.canvas.manager, 'window'):
                fig.canvas.manager.window.raise_()
                logger.debug("Raised window to front")
        except Exception as e:
            logger.debug(f"Could not raise window: {e}")

        try:
            # Force window to be visible
            if hasattr(fig.canvas, 'manager') and hasattr(fig.canvas.manager, 'show'):
                fig.canvas.manager.show()
                logger.debug("Called manager.show()")
        except Exception as e:
            logger.debug(f"Could not call manager.show(): {e}")

        # Give matplotlib time to create the window
        import time
        time.sleep(0.1)

        logger.debug("Successfully showed figure with unified display")
        return True

    except Exception as e:
        logger.debug(f"Unified display failed: {e}")
        # Fallback to simple show
        try:
            plt.show(block=False)
            return True
        except Exception as e2:
            logger.debug(f"Fallback show failed: {e2}")
            return False


def _get_default_layout_for_graph_type(graph_type: str) -> str:
    """
    Get the default layout algorithm based on the original SNT graph type.

    Layout defaults are retrieved using the PySNT configuration system.
    
    Parameters
    ----------
    graph_type : str
        The type of the original SNT graph ('DirectedWeightedGraph', 'AnnotationGraph', etc.)
        
    Returns
    -------
    str
        Default layout algorithm name from configuration
    """
    from ..config import get_option
    
    # Map graph types to config keys
    config_keys = {
        'DirectedWeightedGraph': 'graph.layout.DirectedWeightedGraph',
        'AnnotationGraph': 'graph.layout.AnnotationGraph', 
        'SWCPoint': 'graph.layout.SWCPoint',
        'BrainAnnotation': 'graph.layout.BrainAnnotation',
    }
    
    # Check for exact matches first
    if graph_type in config_keys:
        return get_option(config_keys[graph_type])
    
    # Check for partial matches (in case of full class names)
    for key, config_key in config_keys.items():
        if key in graph_type:
            return get_option(config_key)
    
    # Default fallback
    return get_option('graph.layout.default')


def _graph_to_matplotlib(graph, **kwargs) -> Figure:
    """
    Convert a NetworkX graph to a matplotlib figure for display.
    
    Parameters
    ----------
    graph : networkx.Graph
        The NetworkX graph to visualize
    **kwargs
        Additional visualization options:
        - layout: str or dict, layout algorithm or position dict (default: auto-detected by graph type)
        - graph_type: str, original SNT graph type for smart defaults (optional)
        - node_color: str or list, node colors (default: 'lightblue')
        - node_size: int or list, node sizes (default: 500)
        - edge_color: str or list, edge colors (default: 'gray')
        - edge_width: float or list, edge widths (default: 2)
        - with_labels: bool, whether to show node labels (default: True)
        - figsize: tuple, figure size (default: (10, 8))
        - title: str, plot title (default: 'NetworkX Graph')
        - seed: int, random seed for layout (default: 42)
        - use_node_positions: bool, use node spatial coordinates if available (default: True)
        
    Returns
    -------
    matplotlib.figure.Figure
        Figure containing the graph visualization
    """
    if not HAS_NETWORKX:
        raise ImportError(ERROR_MISSING_NETWORKX)
    
    plt = _setup_matplotlib_interactive()
    
    # Get visualization parameters with sensible defaults
    graph_type = kwargs.get('graph_type', 'Unknown')
    default_layout = _get_default_layout_for_graph_type(graph_type)
    layout = kwargs.get('layout', default_layout)
    node_color = kwargs.get('node_color', DEFAULT_NODE_COLOR)
    node_size = kwargs.get('node_size', DEFAULT_NODE_SIZE)
    edge_color = kwargs.get('edge_color', 'gray')
    edge_width = kwargs.get('edge_width', 2)
    with_labels = kwargs.get('with_labels', graph_type != 'DirectedWeightedGraph')
    figsize = kwargs.get('figsize', (10, 8))
    title = kwargs.get('title', graph_type)
    seed = kwargs.get('seed', 42)
    use_node_positions = kwargs.get('use_node_positions', True)
    
    # Create figure
    fig, ax = plt.subplots(figsize=figsize)
    
    try:
        # Determine node positions
        if isinstance(layout, dict):
            # Use provided position dictionary
            pos = layout
        elif layout == 'spatial' or (use_node_positions and layout == 'spring'):
            # Try to use spatial coordinates from SWCPoint nodes
            pos = {}
            has_spatial_coords = False
            
            for node in graph.nodes():
                try:
                    # Try to get coordinates from SWCPoint attributes
                    if 'x' in graph.nodes[node] and 'y' in graph.nodes[node]:
                        # Use node attributes if available
                        x = float(graph.nodes[node]['x'])
                        y = float(graph.nodes[node]['y'])
                        pos[node] = (x, y)
                        has_spatial_coords = True
                except Exception as e:
                    logger.debug(f"Could not extract spatial coordinates from node {node}: {e}")
            
            # Fall back to spring layout if no spatial coordinates found
            if not has_spatial_coords or len(pos) != graph.number_of_nodes():
                logger.debug("No spatial coordinates found, using spring layout")
                pos = nx.spring_layout(graph, seed=seed)
        else:
            # Use specified layout algorithm
            if layout == 'spring':
                pos = nx.spring_layout(graph, seed=seed)
            elif layout == 'circular':
                pos = nx.circular_layout(graph)
            elif layout == 'random':
                pos = nx.random_layout(graph, seed=seed)
            elif layout == 'shell':
                pos = nx.shell_layout(graph)
            elif layout == 'kamada_kawai':
                pos = nx.kamada_kawai_layout(graph)
            elif layout == 'planar':
                try:
                    pos = nx.planar_layout(graph)
                except nx.NetworkXException:
                    logger.warning("Graph is not planar, falling back to spring layout")
                    pos = nx.spring_layout(graph, seed=seed)
            else:
                logger.warning(f"Unknown layout '{layout}', using spring layout")
                pos = nx.spring_layout(graph, seed=seed)
        
        # Handle node colors based on attributes
        if node_color == 'by_type' and graph.number_of_nodes() > 0:
            # Color nodes by SWC type if available
            node_colors = []
            # see Path#getSWCcolor()
            type_colors = {1: 'blue', 2: 'red', 3: 'green', 4: 'cyan', 5: 'yellow', 6: 'orange', 7: 'pink', 8: 'goldenrod'}
            
            for node in graph.nodes():
                try:
                    if hasattr(node, 'getType'):
                        node_type = int(node.getType())
                    elif 'type' in graph.nodes[node]:
                        node_type = int(graph.nodes[node]['type'])
                    else:
                        node_type = 1  # Default
                    
                    node_colors.append(type_colors.get(node_type, 'lightblue'))
                except (AttributeError, TypeError, RuntimeError):
                    node_colors.append('lightblue')
            
            node_color = node_colors
        elif node_color == 'by_annotation' and graph.number_of_nodes() > 0:
            # Color nodes by BrainAnnotation color if available
            node_colors = []
            
            for node in graph.nodes():
                try:
                    # Try to get color from BrainAnnotation
                    if 'color_hex' in graph.nodes[node]:
                        node_colors.append(graph.nodes[node]['color_hex'])
                    elif 'color_rgb' in graph.nodes[node]:
                        rgb = graph.nodes[node]['color_rgb']
                        hex_color = f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"
                        node_colors.append(hex_color)
                    elif hasattr(node, 'color'):
                        color = node.color()
                        color_attrs = _extract_color_attributes(color, "color")
                        if 'color_hex' in color_attrs:
                            node_colors.append(color_attrs['color_hex'])
                        else:
                            node_colors.append('lightblue')
                    else:
                        node_colors.append('lightblue')
                except (AttributeError, TypeError, RuntimeError):
                    node_colors.append('lightblue')
            
            node_color = node_colors
        
        # Handle node sizes based on radius if available
        if node_size == 'by_radius' and graph.number_of_nodes() > 0:
            node_sizes = []
            base_size = 300
            
            for node in graph.nodes():
                try:
                    if hasattr(node, 'getRadius'):
                        radius = float(node.getRadius())
                    elif 'radius' in graph.nodes[node]:
                        radius = float(graph.nodes[node]['radius'])
                    else:
                        radius = 1.0  # Default
                    
                    # Scale radius to reasonable node size
                    node_sizes.append(base_size * max(0.5, radius))
                except (AttributeError, TypeError, RuntimeError):
                    node_sizes.append(base_size)
            
            node_size = node_sizes
        
        # Handle edge widths based on weight if available
        if edge_width == 'by_weight' and graph.number_of_edges() > 0:
            edge_widths = []
            
            for edge in graph.edges():
                try:
                    weight = graph.edges[edge].get('weight', 1.0)
                    # Scale weight to reasonable line width
                    edge_widths.append(max(0.5, min(5.0, float(weight))))
                except (AttributeError, TypeError, RuntimeError):
                    edge_widths.append(2.0)
            
            edge_width = edge_widths
        
        # Draw the graph
        nx.draw(graph, pos,
                node_color=node_color,
                node_size=node_size,
                edge_color=edge_color,
                width=edge_width,
                with_labels=with_labels,
                ax=ax,
                arrows=True,           # Ensure arrows are drawn for directed graphs
                arrowsize=10,          # Smaller arrows to reduce visual clutter
                arrowstyle='->'        # Simple arrow style
                )
        
        # Add title and labels
        ax.set_title(title, fontsize=14, fontweight='normal')
        
        # Add graph statistics as text
        stats_text = f"Nodes: {graph.number_of_nodes()}, Edges: {graph.number_of_edges()}"
        if hasattr(graph, 'is_directed') and graph.is_directed():
            stats_text += " (Directed)"
        
        ax.text(0.02, 0.98, stats_text, transform=ax.transAxes, 
                verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
        
        # Add colorbar for edge weights if they vary
        if isinstance(edge_width, list) and len(set(edge_width)) > 1:
            # Create a simple legend for edge weights
            legend_text = "Edge width ∝ weight"
            ax.text(0.02, 0.02, legend_text, transform=ax.transAxes,
                    verticalalignment='bottom', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
        
        plt.tight_layout()
        
        logger.info(f"Successfully created NetworkX graph visualization with {graph.number_of_nodes()} nodes and {graph.number_of_edges()} edges")
        return fig
        
    except Exception as e:
        logger.error(f"Failed to create graph visualization: {e}")
        # Create a simple error figure
        ax.text(0.5, 0.5, f'Graph visualization failed:\n{str(e)}', 
                ha='center', va='center', transform=ax.transAxes,
                bbox=dict(boxstyle='round', facecolor='red', alpha=0.3))
        ax.set_title(title)
        return fig


def _display_xarray_dataset(dataset: Any, **kwargs) -> Any:
    """
    Display a xarray Dataset (e.g., SNTTable conversion).
    
    This function creates visualizations for tabular data stored in xarray Dataset format,
    including summary statistics, data distribution plots, correlation matrices, and DataFrame display.
    
    Parameters
    ----------
    dataset : xarray.Dataset
        The xarray Dataset to display
    **kwargs
        Additional arguments for display:
        - plot_type: 'auto', 'summary', 'distribution', 'correlation', 'dataframe' (default: uses pysnt.get_option('display.table_mode'))
        - max_vars: Maximum number of variables to display (default: 10)
        - figsize: Figure size (default: uses pysnt.get_option('plotting.figure_size'))
        - title: Plot title (default: 'SNT Table Data')
        - use_gui: Use PandasGUI for DataFrame display (default: False)
        - max_rows: Max rows for DataFrame display (default: uses pysnt.get_option('display.max_rows'))
        - max_cols: Max columns for DataFrame display (default: uses pysnt.get_option('display.max_columns'))
        - precision: Decimal precision for DataFrame display (default: uses pysnt.get_option('display.precision'))
        
    Returns
    -------
    Any
        The result of the display operation
    """
    from ..config import get_option
    
    logger.debug(f"Displaying xarray Dataset: {dataset}")

    try:
        # Get display parameters with config defaults
        plot_type = kwargs.get('plot_type', get_option('display.table_mode')).lower()
        max_vars = kwargs.get('max_vars', 10)
        figsize = kwargs.get('figsize', get_option('plotting.figure_size'))
        title = kwargs.get('title', 'SNT Table Data')

        # Get data variables (exclude coordinates)
        data_vars = list(dataset.data_vars.keys())
        n_vars = len(data_vars)

        logger.info(f"Dataset has {n_vars} data variables: {data_vars[:5]}{'...' if n_vars > 5 else ''}")

        if n_vars == 0:
            logger.warning("Dataset has no data variables to display")
            return False

        # Limit number of variables for display
        display_vars = data_vars[:max_vars] if n_vars > max_vars else data_vars

        # Map table mode to plot type
        if plot_type == 'pandasgui':
            plot_type = 'dataframe'
            kwargs['use_gui'] = True
        elif plot_type == 'basic':
            plot_type = 'dataframe'
            kwargs['use_gui'] = False
        
        # Auto-select plot type based on data
        if plot_type == 'auto':
            if n_vars == 1:
                plot_type = 'distribution'
            elif n_vars <= 4:
                plot_type = 'distribution'
            else:
                plot_type = 'summary'

        # Route to appropriate display function
        if plot_type == 'dataframe':
            return _display_dataset_as_dataframe(dataset, **kwargs)
        elif plot_type == 'summary':
            return _create_dataset_summary_plot(dataset, display_vars, title, figsize)
        elif plot_type == 'distribution':
            return _create_dataset_distribution_plot(dataset, display_vars, title, figsize)
        elif plot_type == 'correlation':
            return _create_dataset_correlation_plot(dataset, display_vars, title, figsize)
        else:
            logger.warning(
                f"Unknown plot_type: {plot_type}. Available options: 'auto', 'summary', 'distribution', 'correlation', 'dataframe', 'pandasgui', 'basic'")
            return False

    except Exception as e:
        logger.error(f"Failed to display xarray Dataset: {e}")
        return False


def _create_dataset_summary_plot(dataset: Any, display_vars: List[str], title: str, figsize: tuple) -> bool:
    """
    Create a summary plot with overview, missing values, statistics, and correlation matrix.
    
    Parameters
    ----------
    dataset : xarray.Dataset
        The dataset to plot
    display_vars : List[str]
        Variables to display
    title : str
        Plot title
    figsize : tuple
        Figure size
        
    Returns
    -------
    bool
        True if successful, False otherwise
    """
    import numpy as np # noqa
    
    plt = _setup_matplotlib_interactive()

    try:
        fig, axes = plt.subplots(2, 2, figsize=figsize)
        fig.suptitle(title, fontsize=14)

        # Plot 1: Data overview (first few variables)
        ax1 = axes[0, 0]
        for i, var in enumerate(display_vars[:4]):
            try:
                data = dataset[var].values
                if np.issubdtype(data.dtype, np.number):
                    ax1.plot(data[:min(100, len(data))], label=var, alpha=0.7)
            except Exception as e:
                logger.debug(f"Could not plot variable {var}: {e}")
        ax1.set_title('Data Overview (first 100 points)')
        ax1.legend()
        ax1.grid(True, alpha=0.3)

        # Plot 2: Data types and missing values
        ax2 = axes[0, 1]
        var_info = []
        missing_counts = []
        for var in display_vars:
            try:
                data = dataset[var].values
                missing = np.sum(pandas.isna(data)) if 'pandas' in str(type(data)) else 0
                var_info.append(f"{var}\n({data.dtype})")
                missing_counts.append(missing)
            except (AttributeError, TypeError, RuntimeError):
                var_info.append(f"{var}\n(unknown)")
                missing_counts.append(0)

        ax2.bar(range(len(var_info)), missing_counts)
        ax2.set_xticks(range(len(var_info)))
        ax2.set_xticklabels(var_info, rotation=45, ha='right')
        ax2.set_title('Missing Values by Variable')
        ax2.set_ylabel('Count')

        # Plot 3: Basic statistics
        ax3 = axes[1, 0]
        stats_text = f"Dataset Summary:\n"
        stats_text += f"Variables: {len(list(dataset.data_vars.keys()))}\n"
        # Use sizes instead of dims to avoid FutureWarning
        dims_info = dict(dataset.sizes) if hasattr(dataset, 'sizes') else dict(dataset.dims)
        stats_text += f"Dimensions: {dims_info}\n"
        stats_text += f"Coordinates: {list(dataset.coords.keys())}\n"

        # Add basic stats for numeric variables
        numeric_vars = []
        for var in display_vars[:3]:
            try:
                data = dataset[var].values
                if np.issubdtype(data.dtype, np.number):
                    mean_val = np.nanmean(data)
                    std_val = np.nanstd(data)
                    stats_text += f"\n{var}:\n  Mean: {mean_val:.3f}\n  Std: {std_val:.3f}"
                    numeric_vars.append(var)
            except (AttributeError, TypeError, RuntimeError):
                pass

        ax3.text(0.05, 0.95, stats_text, transform=ax3.transAxes,
                 verticalalignment='top', fontfamily='monospace', fontsize=9)
        ax3.set_xlim(0, 1)
        ax3.set_ylim(0, 1)
        ax3.axis('off')
        ax3.set_title('Dataset Statistics')

        # Plot 4: Correlation matrix (if multiple numeric variables)
        ax4 = axes[1, 1]
        if len(numeric_vars) > 1:
            try:
                # Create correlation matrix
                corr_data = {}
                for var in numeric_vars[:5]:  # Limit to 5 variables
                    data = dataset[var].values
                    # Flatten multi-dimensional arrays
                    if data.ndim > 1:
                        data = data.flatten()
                    corr_data[var] = data

                import pandas as pd # noqa
                df = pd.DataFrame(corr_data)
                corr_matrix = df.corr()

                im = ax4.imshow(corr_matrix.values, cmap='coolwarm', vmin=-1, vmax=1)
                ax4.set_xticks(range(len(corr_matrix.columns)))
                ax4.set_yticks(range(len(corr_matrix.columns)))
                ax4.set_xticklabels(corr_matrix.columns, rotation=45, ha='right')
                ax4.set_yticklabels(corr_matrix.columns)
                ax4.set_title('Correlation Matrix')

                # Add colorbar
                plt.colorbar(im, ax=ax4, shrink=0.8)

            except Exception as e:
                logger.debug(f"Could not create correlation matrix: {e}")
                ax4.text(0.5, 0.5, 'Correlation matrix\nnot available',
                         ha='center', va='center', transform=ax4.transAxes)
                ax4.axis('off')
        else:
            ax4.text(0.5, 0.5, 'Need multiple\nnumeric variables\nfor correlation',
                     ha='center', va='center', transform=ax4.transAxes)
            ax4.axis('off')

        plt.tight_layout()

        # Use unified display system
        if _show_matplotlib_figure(fig):
            logger.info("Successfully displayed xarray Dataset summary")
            return True
        else:
            logger.warning("Failed to display xarray Dataset summary")
            return False

    except Exception as e:
        logger.error(f"Failed to create summary plot: {e}")
        return False


def _create_dataset_distribution_plot(dataset: Any, display_vars: List[str], title: str, figsize: tuple) -> bool:
    """
    Create distribution plots for dataset variables.
    
    Parameters
    ----------
    dataset : xarray.Dataset
        The dataset to plot
    display_vars : List[str]
        Variables to display
    title : str
        Plot title
    figsize : tuple
        Figure size
        
    Returns
    -------
    bool
        True if successful, False otherwise
    """
    import numpy as np # noqa
    
    plt = _setup_matplotlib_interactive()

    try:
        # Create distribution plots for each variable
        n_plots = min(len(display_vars), 6)  # Max 6 plots
        cols = min(3, n_plots)
        rows = (n_plots + cols - 1) // cols

        fig, axes = plt.subplots(rows, cols, figsize=figsize)
        if n_plots == 1:
            axes = [axes]
        elif rows == 1:
            axes = axes if isinstance(axes, (list, np.ndarray)) else [axes]
        else:
            axes = axes.flatten()

        fig.suptitle(f'{title} - Data Distributions', fontsize=14)

        for i, var in enumerate(display_vars[:n_plots]):
            ax = axes[i]
            try:
                data = dataset[var].values
                if np.issubdtype(data.dtype, np.number):
                    # Numeric data - histogram
                    valid_data = data[~pandas.isna(data)] if 'pandas' in str(type(data)) else data
                    ax.hist(valid_data, bins=30, alpha=0.7, edgecolor='black')
                    ax.set_title(f'{var}\n(μ={np.nanmean(data):.2f}, σ={np.nanstd(data):.2f})')
                else:
                    # Categorical data - value counts
                    unique_vals, counts = np.unique(data, return_counts=True)
                    ax.bar(range(len(unique_vals)), counts)
                    ax.set_xticks(range(len(unique_vals)))
                    ax.set_xticklabels([str(v)[:10] for v in unique_vals], rotation=45)
                    ax.set_title(f'{var}\n({len(unique_vals)} unique values)')

                ax.grid(True, alpha=0.3)

            except Exception as e:
                logger.debug(f"Could not plot distribution for {var}: {e}")
                ax.text(0.5, 0.5, f'Could not plot\n{var}', ha='center', va='center', transform=ax.transAxes)

        # Hide unused subplots
        for i in range(n_plots, len(axes)):
            axes[i].axis('off')

        plt.tight_layout()

        # Use unified display system
        if _show_matplotlib_figure(fig):
            logger.info("Successfully displayed xarray Dataset distributions")
            return True
        else:
            logger.warning("Failed to display xarray Dataset distributions")
            return False

    except Exception as e:
        logger.error(f"Failed to create distribution plot: {e}")
        return False


def _create_dataset_correlation_plot(dataset: Any, display_vars: List[str], title: str, figsize: tuple) -> bool:
    """
    Create a correlation matrix plot for numeric variables.
    
    Parameters
    ----------
    dataset : xarray.Dataset
        The dataset to plot
    display_vars : List[str]
        Variables to display
    title : str
        Plot title
    figsize : tuple
        Figure size
        
    Returns
    -------
    bool
        True if successful, False otherwise
    """
    import numpy as np # noqa
    
    plt = _setup_matplotlib_interactive()

    try:
        # Get numeric variables
        numeric_vars = []
        for var in display_vars:
            try:
                data = dataset[var].values
                if np.issubdtype(data.dtype, np.number):
                    numeric_vars.append(var)
            except (AttributeError, TypeError, RuntimeError):
                pass

        if len(numeric_vars) < 2:
            logger.warning("Need at least 2 numeric variables for correlation plot")
            return False

        # Create correlation matrix
        corr_data = {}
        for var in numeric_vars:
            data = dataset[var].values
            # Flatten multi-dimensional arrays
            if data.ndim > 1:
                data = data.flatten()
            corr_data[var] = data

        import pandas as pd # noqa
        df = pd.DataFrame(corr_data)
        corr_matrix = df.corr()

        # Create plot
        fig, ax = plt.subplots(figsize=figsize)
        im = ax.imshow(corr_matrix.values, cmap='coolwarm', vmin=-1, vmax=1)

        # Set ticks and labels
        ax.set_xticks(range(len(corr_matrix.columns)))
        ax.set_yticks(range(len(corr_matrix.columns)))
        ax.set_xticklabels(corr_matrix.columns, rotation=45, ha='right')
        ax.set_yticklabels(corr_matrix.columns)

        # Add correlation values as text
        for i in range(len(corr_matrix.columns)):
            for j in range(len(corr_matrix.columns)):
                corr_value = corr_matrix.iloc[i, j]
                text_color = "black" if abs(corr_value) < 0.5 else "white"
                ax.text(j, i, f'{corr_value:.2f}',
                        ha="center", va="center",
                        color=text_color)

        ax.set_title(f'{title} - Correlation Matrix')
        plt.colorbar(im, ax=ax, shrink=0.8)
        plt.tight_layout()

        # Use unified display system
        if _show_matplotlib_figure(fig):
            logger.info("Successfully displayed correlation matrix")
            return True
        else:
            logger.warning("Failed to display correlation matrix")
            return False

    except Exception as e:
        logger.error(f"Failed to create correlation plot: {e}")
        return False


def _display_array_data(data, source_type="array", **kwargs):
    """
    Unified array display for numpy arrays, xarray values, etc.
    
    Parameters
    ----------
    data : array-like
        The array data to display (numpy array, xarray values, etc.)
    source_type : str
        Type of source data for logging/metadata
    **kwargs
        Display parameters including:
        - metadata: dict, optional metadata from SNTObject conversion
        - title: str, optional title override
        - is_rgb: bool, optional RGB flag override
        - add_colorbar: bool, whether to add colorbar (default: True for grayscale)
        
    Returns
    -------
    SNTObject or None
        SNTObject with display result or None on failure
    """
    # Handle different dimensionalities
    original_shape = data.shape
    title = kwargs.get('title', None)
    
    # Check for metadata-based RGB detection (most reliable)
    metadata = kwargs.get('metadata', {})
    is_rgb = metadata.get('is_rgb', False)
    
    # Use metadata title if available and no title override provided
    if not title and 'image_title' in metadata:
        title = metadata['image_title']
    
    # If no metadata available, fall back to manual override or shape detection
    if not is_rgb and 'is_rgb' in kwargs:
        is_rgb = kwargs['is_rgb']
    elif not is_rgb and data.ndim == 3 and data.shape[2] in [3, 4]:
        # Fallback: shape-based detection (less reliable)
        is_rgb = True
        logger.warning(f"Using fallback RGB detection based on shape {data.shape}. "
                      f"Consider using metadata-based detection for reliability.")

    if data.ndim == 3:
        if is_rgb:
            # RGB/RGBA data - display as-is
            img_data = data
            logger.debug(f"Displaying RGB/RGBA data: shape={img_data.shape}")
            if not title:
                title = f"RGB {source_type}"
        else:
            # 3D - show middle slice
            middle_slice = data.shape[0] // 2
            img_data = data[middle_slice]
            logger.debug(f"Using middle slice {middle_slice} from 3D data: new shape={img_data.shape}")
            if not title:
                title = f"Slice {middle_slice} of 3D {source_type}"
    elif data.ndim > 3:
        # Higher dimensions - take first 2D slice
        img_data = data
        while img_data.ndim > 2:
            img_data = img_data[0]
        logger.debug(f"Reduced {len(original_shape)}D data to 2D: {original_shape} -> {img_data.shape}")
        if not title:
            title = f"2D slice of {len(original_shape)}D {source_type}"
    elif data.ndim == 2:
        img_data = data
        if not title:
            title = f"2D {source_type}"
    elif data.ndim < 2:
        logger.warning(f"Data has only {data.ndim} dimensions, cannot display as image")
        raise ValueError(f"Cannot display {data.ndim}D data as image")

    # Use the new standardized figure creation
    cmap = kwargs.get('cmap', DEFAULT_CMAP)
    add_colorbar = kwargs.get('add_colorbar', True)
    
    fig, ax, im = _create_standard_figure(
        data=img_data,
        title=title,
        cmap=cmap,
        add_colorbar=add_colorbar,
        is_rgb=is_rgb,
        **kwargs
    )

    # Use unified display system
    if _show_matplotlib_figure(fig):
        logger.info(f"Successfully displayed {source_type} data as {'RGB' if is_rgb else 'grayscale'} image: '{title}'")
        return {
            'type': Figure,
            'data': data,
            'metadata': {
                'source_type': source_type,
                'original_shape': original_shape,
                'displayed_shape': img_data.shape,
                'title': title,
                'is_rgb': is_rgb,
                **metadata  # Include original metadata
            },
            'error': None
        }
    else:
        logger.warning(f"Failed to display {source_type} figure")
        return None


def _display_dataset_as_dataframe(dataset: Any, **kwargs) -> bool:
    """
    Display xarray Dataset as a pandas DataFrame.
    
    Parameters
    ----------
    dataset : xarray.Dataset
        The xarray Dataset to display
    **kwargs
        Additional arguments:
        - use_gui: bool, whether to use PandasGUI (default: False)
        - max_rows: int, max rows for console display (default: uses pysnt.get_option('display.max_rows'))
        - max_cols: int, max columns for console display (default: uses pysnt.get_option('display.max_columns'))
        - precision: int, decimal precision for console display (default: uses pysnt.get_option('display.precision'))
        - title: str, title for PandasGUI window (default: "SNT Dataset")
        
    Returns
    -------
    bool
        True if successful, False otherwise
    """
    from ..config import get_option
    
    try:
        import pandas as pd # noqa

        # Get display parameters with config defaults
        use_gui = kwargs.get('use_gui', False)
        max_rows = kwargs.get('max_rows', get_option('display.max_rows'))
        max_cols = kwargs.get('max_cols', get_option('display.max_columns'))
        precision = kwargs.get('precision', get_option('display.precision'))
        title = kwargs.get('title', 'SNT Dataset')

        # Convert dataset to DataFrame
        df = dataset.to_dataframe()

        if use_gui:
            # Try to display in PandasGUI
            # Filter out parameters that are specific to console display and title (passed separately)
            gui_kwargs = {k: v for k, v in kwargs.items()
                          if k not in ['max_rows', 'max_cols', 'precision', 'use_gui', 'title']}
            if _show_pandasgui_dataframe(df, title=title, **gui_kwargs):
                logger.info("Successfully displayed xarray Dataset in PandasGUI")
                return True
            else:
                logger.warning("PandasGUI display failed, falling back to console display")
                # Fall through to console display

        # Console display (default or fallback)
        with pd.option_context('display.max_rows', max_rows,
                               'display.max_columns', max_cols,
                               'display.precision', precision,
                               'display.width', None):
            print("Dataset as DataFrame:")
            print("=" * 50)
            print(df)
            print("=" * 50)
            print(f"Shape: {df.shape}")
            print(f"Data types:\n{df.dtypes}")

            if hasattr(df, 'describe'):
                print("\nSummary statistics:")
                print(df.describe())

        logger.info("Successfully displayed xarray Dataset as DataFrame")
        return True

    except Exception as e:
        logger.error(f"Failed to display Dataset as DataFrame: {e}")
        return False


def _show_pandasgui_dataframe(df, title="Dataset", **kwargs) -> bool:
    """
    Display a pandas DataFrame using PandasGUI with thread handling.
    
    Parameters
    ----------
    df : pandas.DataFrame
        The DataFrame to display
    title : str
        Title for the PandasGUI window
    **kwargs
        Additional arguments (currently unused)
        
    Returns
    -------
    bool
        True if successful, False otherwise
    """
    if not _has_pandasgui():
        logger.warning("PandasGUI not available. Install with: pip install pandasgui")
        return False

    try:
        import threading
        import time
        import sys
        import os
        
        # Check if we should use safe mode
        from ..config import get_option
        gui_safe_mode = get_option('display.gui_safe_mode')
        
        # Check if we're on macOS
        is_macos = sys.platform == 'darwin'
        
        # Check if we're in the main thread
        is_main_thread = threading.current_thread() is threading.main_thread()
        
        if gui_safe_mode and is_macos and not is_main_thread:
            logger.warning("GUI safe mode enabled on macOS - falling back to console display to avoid threading issues.")
            # Fall back to console display
            with pandas.option_context('display.max_rows', kwargs.get('max_rows', 20),
                                     'display.max_columns', kwargs.get('max_cols', 10),
                                     'display.precision', kwargs.get('precision', 3)):
                print(f"\n{title}:")
                print("=" * 50)
                print(df)
                print("=" * 50)
                print(f"Shape: {df.shape}")
                if hasattr(df, 'describe'):
                    print("\nSummary statistics:")
                    print(df.describe())
            return True

        def show_gui():
            """Show PandasGUI with proper error handling."""
            try:
                # Create a copy of the DataFrame to avoid any threading issues
                df_copy = df.copy()

                # Set Qt application attributes for better compatibility
                try:
                    from PyQt5.QtWidgets import QApplication # noqa
                    from PyQt5.QtCore import Qt # noqa
                    
                    # Set attributes before creating QApplication
                    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
                    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
                except ImportError:
                    pass  # PyQt5 not available, continue anyway

                # Show in PandasGUI with the specified title
                pandasgui_show = _get_pandasgui_show()
                if pandasgui_show is None:
                    raise ImportError("PandasGUI not available")
                gui = pandasgui_show(df_copy, title=title)

                # Keep the GUI alive by running its event loop
                if hasattr(gui, 'app') and hasattr(gui.app, 'exec_'):
                    gui.app.exec_()

            except Exception as e2:
                logger.error(f"PandasGUI error: {e2}")
                # Fall back to console display on error
                logger.info("Falling back to console display")
                with pandas.option_context('display.max_rows', kwargs.get('max_rows', 20),
                                         'display.max_columns', kwargs.get('max_cols', 10),
                                         'display.precision', kwargs.get('precision', 3)):
                    print(f"\n{title} (PandasGUI failed):")
                    print("=" * 50)
                    print(df_copy)
                    print("=" * 50)

        if is_main_thread:
            # We're in the main thread, can run directly
            show_gui()
        else:
            # We're in a background thread, start a daemon thread
            gui_thread = threading.Thread(target=show_gui, daemon=True)
            gui_thread.start()
            
            # Give the GUI a moment to start up
            time.sleep(0.2)

        logger.info(f"Successfully launched PandasGUI for {title}")
        return True

    except Exception as e:
        logger.error(f"Failed to show DataFrame in PandasGUI: {e}")
        # Final fallback to console display
        try:
            with pandas.option_context('display.max_rows', kwargs.get('max_rows', 20),
                                     'display.max_columns', kwargs.get('max_cols', 10),
                                     'display.precision', kwargs.get('precision', 3)):
                print(f"\n{title} (fallback):")
                print("=" * 50)
                print(df)
                print("=" * 50)
            return True
        except Exception as fallback_e:
            logger.error(f"Even console fallback failed: {fallback_e}")
            return False


# Registry for custom display handlers
_DISPLAY_HANDLERS = {}


def register_display_handler(obj_type: str, handler_func: Callable[[Dict[str, Any]], None]):
    """
    Register a custom display handler for a specific SNT object type.
    
    This allows adding custom display logic for new converter types
    without modifying the core display system.
    
    Parameters
    ----------
    obj_type : str
        The object type string (e.g., 'SNT_CustomObject')
    handler_func : callable
        Function that takes (snt_dict, **kwargs) and displays the information
        
    Examples
    --------
    >>> def display_my_object(snt_dict, **kwargs):
    ...     print(f"My object: {snt_dict.get('name')}")
    >>> 
    >>> register_display_handler('SNT_MyObject', display_my_object)
    """
    _DISPLAY_HANDLERS[obj_type] = handler_func
    logger.info(f"Registered display handler for {obj_type}")

def _display_generic_object(obj: Any, **kwargs) -> Any:
    """
    Enhanced fallback display function for any Python object.
    
    This function provides useful display for objects that don't have specialized
    converters, using pprint for structured data and informative summaries for
    other objects.
    
    Parameters
    ----------
    obj : Any
        The object to display
    **kwargs
        Additional display arguments (unused but kept for consistency)
        
    Returns
    -------
    Any
        The original object
    """
    obj_type = type(obj)
    obj_type_name = obj_type.__name__
    
    # Handle common Python data structures with pprint
    if isinstance(obj, (list, tuple, dict, set)):
        print(f"{obj_type_name}:")
        try:
            pprint(obj, width=100, depth=3)
        except Exception as e:
            # Fallback if pprint fails (e.g., with very complex objects)
            print(f"  <{obj_type_name} with {len(obj)} items>")
            logger.debug(f"pprint failed: {e}")
        return obj
    
    # Handle numpy arrays
    elif isinstance(obj, np.ndarray):
        print(f"numpy.ndarray:")
        print(f"  Shape: {obj.shape}")
        print(f"  Dtype: {obj.dtype}")
        print(f"  Size: {obj.size}")
        if obj.size > 0:
            print(f"  Min: {obj.min()}, Max: {obj.max()}")
            if obj.size <= 20:  # Show small arrays completely
                print("  Data:")
                with np.printoptions(precision=3, suppress=True):
                    print(f"    {obj}")
            else:  # Show preview for large arrays
                print("  Preview:")
                with np.printoptions(precision=3, suppress=True):
                    if obj.ndim == 1:
                        print(f"    [{obj[0]}, {obj[1]}, ..., {obj[-2]}, {obj[-1]}]")
                    else:
                        print(f"    {obj.flat[0]}, {obj.flat[1]}, ..., {obj.flat[-2]}, {obj.flat[-1]}")
        return obj
    
    # Handle string representations
    elif isinstance(obj, str):
        if len(obj) <= 200:
            print(f"str: {repr(obj)}")
        else:
            print(f"str (length {len(obj)}): {repr(obj[:100])}...{repr(obj[-50:])}")
        return obj
    
    # Handle callable objects (functions, methods, classes)
    elif callable(obj):
        print(f"Callable {obj_type_name}: {obj}")
        if hasattr(obj, '__doc__') and obj.__doc__:
            doc_lines = obj.__doc__.strip().split('\n')
            print(f"  Documentation: {doc_lines[0]}")
        if hasattr(obj, '__module__'):
            print(f"  Module: {obj.__module__}")
        return obj
    
    # Handle pandas objects if available (check before generic object handling)
    else:
        try:
            import pandas as pd
            if isinstance(obj, (pd.DataFrame, pd.Series)):
                print(f"pandas.{obj_type_name}:")
                print(obj)
                return obj
        except ImportError:
            pass
        
        # Generic object information
        print(f"Object of type: {obj_type}")
        print(f"  Module: {getattr(obj_type, '__module__', 'unknown')}")
        
        # Show string representation if reasonable
        try:
            str_repr = str(obj)
            if len(str_repr) <= 200 and '\n' not in str_repr:
                print(f"  String representation: {str_repr}")
            elif len(str_repr) <= 500:
                lines = str_repr.split('\n')
                if len(lines) <= 5:
                    print(f"  String representation:")
                    for line in lines:
                        print(f"    {line}")
                else:
                    print(f"  String representation: {lines[0]}... ({len(lines)} lines)")
            else:
                print(f"  String representation: <{len(str_repr)} characters>")
        except Exception:
            print("  String representation: <unavailable>")
        
        # Show useful attributes
        attrs = []
        for attr_name in dir(obj):
            if not attr_name.startswith('_'):
                try:
                    attr_value = getattr(obj, attr_name)
                    if not callable(attr_value):
                        attrs.append(attr_name)
                except Exception:
                    pass
        
        if attrs:
            print(f"  Public attributes ({len(attrs)}): {', '.join(attrs[:10])}")
            if len(attrs) > 10:
                print(f"    ... and {len(attrs) - 10} more")
        
        # Show useful methods
        methods = []
        for attr_name in dir(obj):
            if not attr_name.startswith('_'):
                try:
                    attr_value = getattr(obj, attr_name)
                    if callable(attr_value):
                        methods.append(attr_name)
                except Exception:
                    pass
        
        if methods:
            print(f"  Public methods ({len(methods)}): {', '.join(methods[:10])}")
            if len(methods) > 10:
                print(f"    ... and {len(methods) - 10} more")
        
        # Provide helpful suggestions
        print("\n  💡 Suggestions:")
        if hasattr(obj, 'show'):
            print("    • Try: obj.show()")
        if hasattr(obj, 'display'):
            print("    • Try: obj.display()")
        if hasattr(obj, 'plot'):
            print("    • Try: obj.plot()")
        if hasattr(obj, '__str__') or hasattr(obj, '__repr__'):
            print("    • Try: print(obj)")
        print("    • Try: pysnt.to_python(obj) to convert")
        print("    • Try: print(dir(obj)) to list all attributes")
        
        return obj