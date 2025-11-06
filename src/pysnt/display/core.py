"""
Core display functionality for PySNT.

This module contains the main display orchestration logic, object type detection,
and SNT-specific object handling.
"""

import logging
import traceback
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
from ..converters.structured_data_converters import _convert_path_to_xarray, _is_snt_table, _convert_snt_table, _extract_imageplus_metadata
from ..converters.chart_converters import _is_snt_chart, _convert_snt_chart
from ..converters.graph_converters import _is_snt_graph, _convert_snt_graph
from ..converters.core import _create_converter_result
from .visual_display import _combine_matplotlib_figures

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
    figures, xarray objects, Viewer2D/3D objects, and lists of supported objects.
    
    This function automatically tries to convert Java objects using available converters
    and then displays the result. For lists, it creates multi-panel displays.
    For Viewer3D objects, it takes a snapshot and displays the RGB image.
    For Viewer2D objects, it retrieves the underlying SNTChart and displays it.
    Lists of SNTChart objects and Viewer2D objects are supported for multi-panel display.
    
    Parameters
    ----------
    obj : Any
        The object to display (Java objects, SNTObjects, matplotlib figures, xarray objects, 
        Viewer2D/3D objects, lists of supported objects, etc.)
    **kwargs
        Additional arguments for display (e.g., cmap, title, format, scale, vmin, vmax, 
        add_colorbar, figsize)
        
        For ImagePlus objects:
        
        - frame, t, time, timepoint : int, optional
          Frame/timepoint to display (default: 1). Parameter names are case-insensitive.
        
        For Viewer2D objects:
        
        - title : str, optional
          Title for the chart display (default: uses chart's title)
        - Standard chart display parameters (cmap, figsize, etc.)
        
        For Viewer3D objects:
        
        - title : str, optional
          Title for the snapshot display (default: "3D Viewer Snapshot")
        - add_colorbar : bool, optional
          Whether to add colorbar (default: False for RGB snapshots)
        - figsize : tuple, optional
          Figure size for display
        
        For lists of objects:
        
        - panel_layout : str or tuple, optional
          Layout for panels ('auto', 'horizontal', 'vertical', or (rows, cols)) (default: 'auto')
        - max_panels : int, optional
          Maximum number of panels to display (default: 20)
    Returns
    -------
    Any
        The displayed object - either the converted SNTObject (for Java objects), the chart
        (for Viewer2D objects), the snapshot ImagePlus (for Viewer3D objects), or the 
        original object (for already converted objects)
        
    Examples
    --------
    >>> # Direct usage with SNTChart
    >>> chart = stats.getHistogram('Branch length')
    >>> snt_obj = pysnt.display(chart)  # Returns SNTObject with matplotlib figure

    >>> # Direct usage with ImagePlus
    >>> skeleton = tree.getSkeleton2D()
    >>> snt_obj = pysnt.display(skeleton)  # Returns SNTObject with xarray data

    >>> # Direct usage with Viewer2D
    >>> viewer2d = Viewer2D()
    >>> viewer2d.add(tree)
    >>> chart = pysnt.display(viewer2d)  # Returns SNTChart from viewer

    >>> # Direct usage with Viewer3D
    >>> viewer3d = Viewer3D(False, "headless")
    >>> viewer3d.add(tree)
    >>> snapshot = pysnt.display(viewer3d, title="3D Scene")  # Returns snapshot ImagePlus

    >>> # Works with already converted objects too - returns the same object
    >>> converted = pysnt.to_python(chart)
    >>> same_obj = pysnt.display(converted)  # Returns the matplotlib figure
    
    >>> # Display list of SNTChart objects as multi-panel figure
    >>> charts = [stats.getHistogram('Branch length'), stats.getHistogram('Branch order')]
    >>> snt_obj = pysnt.display(charts)  # Returns SNTObject with combined matplotlib figure
    
    >>> # Display list of Viewer2D objects as multi-panel figure
    >>> viewer2d_1 = Viewer2D()
    >>> viewer2d_1.add(tree1)
    >>> viewer2d_2 = Viewer2D()
    >>> viewer2d_2.add(tree2)
    >>> snt_obj = pysnt.display([viewer2d_1, viewer2d_2])  # Returns SNTObject with combined matplotlib figure
    """
    logger.debug(f"display() called with object type: {type(obj)}")

    # Check if obj is a list of supported objects
    if isinstance(obj, (list, tuple)):
        return _display_object_list(obj, **kwargs)

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
                skeleton = obj.getSkeleton2D()
                logger.debug(f"Got skeleton from tree: {type(skeleton)}")
                obj = skeleton
            except Exception as e:
                logger.warning(f"Failed to get skeleton from tree: {e}")
                logger.info("Trying alternative skeleton extraction methods...")
                
                # Try alternative methods to get skeleton
                skeleton = None
                try:
                    # Method 1: Check if object has getSkeleton method (without 2D)
                    if hasattr(obj, 'getSkeleton'):
                        skeleton = obj.getSkeleton()
                        logger.debug(f"Got skeleton using getSkeleton(): {type(skeleton)}")
                    # Method 2: Try to access skeleton via different attribute names
                    elif hasattr(obj, 'skeleton'):
                        skeleton = obj.skeleton
                        logger.debug(f"Got skeleton via .skeleton attribute: {type(skeleton)}")
                except Exception as e2:
                    logger.debug(f"Alternative skeleton extraction failed: {e2}")
                
                if skeleton is not None:
                    obj = skeleton
                    logger.info(f"Successfully extracted skeleton using alternative method: {type(obj)}")
                else:
                    logger.warning("All skeleton extraction methods failed, falling back to scyjava conversion")
                    # Final fallback: try to convert the tree directly using converters
                    try:
                        import scyjava as sj
                        converted = sj.to_python(obj)
                        if converted is not obj:
                            obj = converted
                            logger.debug(f"Converted tree using scyjava: {type(obj)}")
                        else:
                            logger.warning("No converter available for tree, will try generic display")
                    except Exception as e3:
                        logger.warning(f"scyjava conversion also failed: {e3}")
        # Special case: Handle ImagePlus objects that might be skeletons from trees
        elif str(type(obj)).find('ImagePlus') != -1:
            # Check if this ImagePlus might be a skeleton (has "Skel" in title)
            try:
                title = obj.getTitle() if hasattr(obj, 'getTitle') else ""
                if title.startswith('Skel'):
                    logger.debug(f"Detected ImagePlus skeleton: {title}")
                    # This is likely a skeleton, let it be processed as ImagePlus
                    # The ImagePlus handler will extract proper metadata including binary detection
                else:
                    logger.debug(f"Regular ImagePlus: {title}")
            except Exception as e:
                logger.debug(f"Could not get ImagePlus title: {e}")
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
    if _is_snt_table(obj):
        return 'snt_table', _display_snt_table

    # Check for SNTChart objects
    if _is_snt_chart(obj):
        return 'snt_chart', _display_snt_chart

    # Check for SNTGraph objects
    if _is_snt_graph(obj):
        return 'snt_graph', _display_snt_graph

    # Check for Viewer3D objects
    if _is_viewer3d(obj):
        return 'viewer3d', _display_viewer3d

    # Check for Viewer2D objects
    if _is_viewer2d(obj):
        return 'viewer2d', _display_viewer2d

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
    """Attempt to display a raw Java object by trying available converters."""
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


def _display_object_list(obj_list: list, **kwargs) -> Any:
    """
    Handle display of lists of supported objects.
    
    Currently supports lists of SNTChart objects and Viewer2D objects, which are displayed as multi-panel figures.
    
    Parameters
    ----------
    obj_list : list or tuple
        List of objects to display
    **kwargs
        Additional display arguments
        
    Returns
    -------
    Any
        The result of the display operation
    """
    logger.debug(f"Processing list of {len(obj_list)} objects")
    
    if not obj_list:
        logger.warning("Empty list provided to display")
        return None
    
    # Check object types in the list
    from ..converters.chart_converters import _is_snt_chart
    
    chart_objects = []
    viewer2d_objects = []
    other_objects = []
    
    for i, obj in enumerate(obj_list):
        if _is_snt_chart(obj):
            chart_objects.append(obj)
        elif _is_viewer2d(obj):
            viewer2d_objects.append(obj)
        else:
            other_objects.append((i, type(obj).__name__))
    
    # Handle pure lists of supported objects
    if chart_objects and not viewer2d_objects and not other_objects:
        # Pure SNTChart list - use multi-panel display
        logger.info(f"Detected list of {len(chart_objects)} SNTChart objects")
        return _display_snt_chart_list(chart_objects, **kwargs)
    elif viewer2d_objects and not chart_objects and not other_objects:
        # Pure Viewer2D list - use multi-panel display
        logger.info(f"Detected list of {len(viewer2d_objects)} Viewer2D objects")
        return _display_viewer2d_list(viewer2d_objects, **kwargs)
    elif (chart_objects or viewer2d_objects) and other_objects:
        # Mixed list - warn and display supported objects
        supported_count = len(chart_objects) + len(viewer2d_objects)
        logger.warning(f"Mixed object list detected. Displaying {supported_count} supported objects, "
                      f"ignoring {len(other_objects)} other objects: {[name for _, name in other_objects]}")
        
        # Prioritize charts over viewer2d if both are present
        if chart_objects:
            return _display_snt_chart_list(chart_objects, **kwargs)
        else:
            return _display_viewer2d_list(viewer2d_objects, **kwargs)
    elif chart_objects and viewer2d_objects and not other_objects:
        # Mixed supported objects - prioritize charts
        logger.warning(f"Mixed list of {len(chart_objects)} SNTChart and {len(viewer2d_objects)} Viewer2D objects. "
                      f"Displaying SNTChart objects only.")
        return _display_snt_chart_list(chart_objects, **kwargs)
    else:
        # No supported objects for list display
        logger.warning(f"List contains no supported objects for multi-panel display. "
                      f"Object types: {[type(obj).__name__ for obj in obj_list]}")
        logger.info("Falling back to individual display of first object")
        return display(obj_list[0], **kwargs)


def _display_snt_chart_list(chart_list: list, **kwargs) -> Any:
    """
    Display a list of SNTChart objects as a multi-panel matplotlib figure.
    
    This function converts each SNTChart to a matplotlib figure and combines them
    into a single multi-panel display using the existing combined chart logic.
    
    Parameters
    ----------
    chart_list : list
        List of SNTChart objects to display
    **kwargs
        Additional display arguments:
        - panel_layout : str or tuple, layout for panels (default: 'auto')
        - max_panels : int, maximum number of panels (default: 20)
        - title : str, overall figure title (default: auto-generated)
        
    Returns
    -------
    Any
        SNTObject containing the combined matplotlib figure
    """
    from ..converters.chart_converters import _convert_snt_chart
    from ..converters.core import _create_converter_result
    
    try:
        # Get parameters
        max_panels = kwargs.get('max_panels', 20)
        title = kwargs.get('title', None)  # No default overall title
        
        # Limit number of charts
        if len(chart_list) > max_panels:
            logger.warning(f"Chart list has {len(chart_list)} items, limiting to {max_panels}")
            chart_list = chart_list[:max_panels]
        
        logger.info(f"Converting {len(chart_list)} SNTChart objects to matplotlib figures")
        
        # Convert each chart to matplotlib figure
        figures = []
        chart_titles = []
        
        for i, chart in enumerate(chart_list):
            try:
                # Convert individual chart
                converted = _convert_snt_chart(chart, **kwargs)
                
                if converted.get('error') is not None:
                    logger.warning(f"Failed to convert chart {i+1}: {converted.get('error')}")
                    continue
                
                figure = converted['data']
                figures.append(figure)
                
                # Get chart title
                try:
                    chart_title = chart.getTitle() if hasattr(chart, 'getTitle') else f"Chart {i+1}"
                except Exception:
                    chart_title = f"Chart {i+1}"
                chart_titles.append(chart_title)
                
            except Exception as e:
                logger.warning(f"Failed to convert chart {i+1}: {e}")
                continue
        
        if not figures:
            logger.error("No charts could be converted successfully")
            return None
        
        logger.info(f"Successfully converted {len(figures)} charts, creating multi-panel figure")
        
        # Combine figures into multi-panel display
        from .visual_display import _combine_matplotlib_figures
        combined_figure = _combine_matplotlib_figures(figures, chart_titles, title or "", **kwargs)
        
        if combined_figure is None:
            logger.error("Failed to combine charts into multi-panel figure")
            return None
        
        # Create result
        metadata = {
            'chart_count': len(chart_list),
            'displayed_count': len(figures),
            'panel_layout': kwargs.get('panel_layout', 'auto'),
            'title': title
        }
        
        logger.info(f"Successfully created multi-panel figure with {len(figures)} charts")
        return _create_converter_result(combined_figure, 'SNTChart_List', **metadata)
        
    except Exception as e:
        logger.error(f"Failed to display SNTChart list: {e}")
        import traceback
        traceback.print_exc()
        return None


def _display_viewer2d_list(viewer2d_list: list, **kwargs) -> Any:
    """
    Display a list of Viewer2D objects as a multi-panel matplotlib figure.
    
    This function gets the chart from each Viewer2D object and combines them
    into a single multi-panel display using the existing combined chart logic.
    
    Parameters
    ----------
    viewer2d_list : list
        List of Viewer2D objects to display
    **kwargs
        Additional display arguments:
        - panel_layout : str or tuple, layout for panels (default: 'auto')
        - max_panels : int, maximum number of panels (default: 20)
        - title : str, overall figure title (default: auto-generated)
        
    Returns
    -------
    Any
        SNTObject containing the combined matplotlib figure
    """
    from ..converters.chart_converters import _convert_snt_chart
    from ..converters.core import _create_converter_result
    
    try:
        # Get parameters
        max_panels = kwargs.get('max_panels', 20)
        title = kwargs.get('title', None)  # No default overall title
        
        # Limit number of viewers
        if len(viewer2d_list) > max_panels:
            logger.warning(f"Viewer2D list has {len(viewer2d_list)} items, limiting to {max_panels}")
            viewer2d_list = viewer2d_list[:max_panels]
        
        logger.info(f"Extracting charts from {len(viewer2d_list)} Viewer2D objects")
        
        # Extract charts from each Viewer2D and convert to matplotlib figures
        figures = []
        chart_titles = []
        
        for i, viewer2d in enumerate(viewer2d_list):
            try:
                # Get chart from Viewer2D
                chart = viewer2d.getChart()
                
                if chart is None:
                    logger.warning(f"Viewer2D {i+1} returned None chart")
                    continue
                
                # Convert chart to matplotlib figure
                converted = _convert_snt_chart(chart, **kwargs)
                
                if converted.get('error') is not None:
                    logger.warning(f"Failed to convert chart from Viewer2D {i+1}: {converted.get('error')}")
                    continue
                
                figure = converted['data']
                figures.append(figure)
                
                # Get chart title
                try:
                    chart_title = chart.getTitle() if hasattr(chart, 'getTitle') else f"Viewer2D {i+1}"
                except Exception:
                    chart_title = f"Viewer2D {i+1}"
                chart_titles.append(chart_title)
                
            except Exception as e:
                logger.warning(f"Failed to process Viewer2D {i+1}: {e}")
                continue
        
        if not figures:
            logger.error("No charts could be extracted from Viewer2D objects")
            return None
        
        logger.info(f"Successfully extracted {len(figures)} charts from Viewer2D objects, creating multi-panel figure")
        
        # Combine figures into multi-panel display
        from .visual_display import _combine_matplotlib_figures
        combined_figure = _combine_matplotlib_figures(figures, chart_titles, title or "", **kwargs)
        
        if combined_figure is None:
            logger.error("Failed to combine Viewer2D charts into multi-panel figure")
            return None
        
        # Create result
        metadata = {
            'viewer2d_count': len(viewer2d_list),
            'displayed_count': len(figures),
            'panel_layout': kwargs.get('panel_layout', 'auto'),
            'title': title
        }
        
        logger.info(f"Successfully created multi-panel figure with {len(figures)} Viewer2D charts")
        return _create_converter_result(combined_figure, 'Viewer2D_List', **metadata)
        
    except Exception as e:
        logger.error(f"Failed to display Viewer2D list: {e}")
        import traceback
        traceback.print_exc()
        return None


# Handler registration system

def _is_viewer3d(obj) -> bool:
    """
    Check if object is a Viewer3D.
    
    Parameters
    ----------
    obj : Any
        Object to check
        
    Returns
    -------
    bool
        True if object is a Viewer3D, False otherwise
    """
    # Check by class name to avoid import issues
    class_name = str(type(obj))
    return 'Viewer3D' in class_name and hasattr(obj, 'snapshot')


def _display_viewer3d(obj, **kwargs):
    """
    Handler function for Viewer3D display.
    
    This function takes a snapshot of the 3D viewer and displays the resulting
    RGB ImagePlus using the standard ImagePlus display pipeline.
    
    Parameters
    ----------
    obj : Viewer3D
        The Viewer3D object to display
    **kwargs : dict
        Additional keyword arguments for display
        
    Returns
    -------
    ImagePlus or None
        The snapshot ImagePlus if successful, None otherwise
    """
    logger.info("Detected Viewer3D object - taking snapshot...")
    
    try:
        # Take a snapshot of the 3D viewer
        snapshot = obj.snapshot()
        
        if snapshot is None:
            logger.error("Viewer3D.snapshot() returned None")
            return None
        
        logger.info(f"Successfully captured Viewer3D snapshot: {snapshot}")
        
        # Add metadata to indicate this came from a Viewer3D
        kwargs_with_metadata = kwargs.copy()
        if 'metadata' not in kwargs_with_metadata:
            kwargs_with_metadata['metadata'] = {}
        
        kwargs_with_metadata['metadata'].update({
            'source_type': 'Viewer3D',
            'is_rgb': True,  # Viewer3D snapshots are typically RGB
            'viewer3d_snapshot': True
        })
        
        # Set default title if not provided
        if 'title' not in kwargs_with_metadata:
            kwargs_with_metadata['title'] = "3D Viewer Snapshot"
        
        # Display the snapshot using the ImagePlus display pipeline
        from .data_display import _display_imageplus
        _display_imageplus(snapshot, **kwargs_with_metadata)
        
        # Return the original snapshot ImagePlus
        return snapshot
        
    except Exception as e:
        logger.error(f"Failed to display Viewer3D: {e}")
        import traceback
        traceback.print_exc()
        return None


def _is_viewer2d(obj) -> bool:
    """
    Check if object is a Viewer2D.
    
    Parameters
    ----------
    obj : Any
        Object to check
        
    Returns
    -------
    bool
        True if object is a Viewer2D, False otherwise
    """
    # Check by class name to avoid import issues
    class_name = str(type(obj))
    return 'Viewer2D' in class_name and hasattr(obj, 'getChart')


def _display_viewer2d(obj, **kwargs):
    """
    Handler function for Viewer2D display.
    
    This function gets the chart from the 2D viewer and displays it using
    the standard SNTChart display pipeline.
    
    Parameters
    ----------
    obj : Viewer2D
        The Viewer2D object to display
    **kwargs : dict
        Additional keyword arguments for display
        
    Returns
    -------
    SNTChart or None
        The chart from the Viewer2D if successful, None otherwise
    """
    logger.info("Detected Viewer2D object - getting chart...")
    
    try:
        # Get the chart from the 2D viewer
        chart = obj.getChart()
        
        if chart is None:
            logger.error("Viewer2D.getChart() returned None")
            return None
        
        logger.info(f"Successfully retrieved Viewer2D chart: {chart}")
        
        # Add metadata to indicate this came from a Viewer2D
        kwargs_with_metadata = kwargs.copy()
        if 'metadata' not in kwargs_with_metadata:
            kwargs_with_metadata['metadata'] = {}
        
        kwargs_with_metadata['metadata'].update({
            'source_type': 'Viewer2D',
            'viewer2d_chart': True
        })
        
        # Set default title if not provided
        if 'title' not in kwargs_with_metadata:
            try:
                chart_title = chart.getTitle() if hasattr(chart, 'getTitle') else "2D Viewer"
                kwargs_with_metadata['title'] = chart_title
            except:
                kwargs_with_metadata['title'] = "2D Viewer"
        
        # Display the chart using the SNTChart display pipeline
        _display_snt_chart(chart, **kwargs_with_metadata)
        
        # Return the original chart
        return chart
        
    except Exception as e:
        logger.error(f"Failed to display Viewer2D: {e}")
        import traceback
        traceback.print_exc()
        return None
