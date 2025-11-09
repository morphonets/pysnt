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

# Import from converters for functions we haven't imported
from ..converters.structured_data_converters import _convert_path_to_xarray, _is_snt_table, _convert_snt_table, _extract_imageplus_metadata
from ..converters.chart_converters import _is_snt_chart, _convert_snt_chart
from ..converters.graph_converters import _is_snt_graph, _convert_snt_graph
from ..converters.core import _create_converter_result
from .visual_display import _combine_matplotlib_figures

logger = logging.getLogger(__name__)


def handle_display_errors(operation_name: str):
    """
    Decorator to handle common display operation errors.
    
    Parameters
    ----------
    operation_name : str
        Name of the operation for error messages
        
    Returns
    -------
    decorator function that handles exceptions
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                logger.error(f"Failed to {operation_name}: {e}")
                traceback.print_exc()
                return None
        return wrapper
    return decorator


def _convert_objects_to_figures(obj_list, converter_func, obj_type_name, **kwargs):
    """
    Generic function to convert a list of objects to matplotlib figures.
    
    Parameters
    ----------
    obj_list : list
        List of objects to convert
    converter_func : callable
        Function to convert individual objects
    obj_type_name : str
        Name of object type for logging
    **kwargs
        Additional arguments for conversion (including 'panel_titles' for custom titles)
        
    Returns
    -------
    tuple
        (figures, titles) where figures is list of matplotlib figures
        and titles is list of corresponding titles
    """
    figures = []
    titles = []
    
    # Get custom titles if provided
    custom_titles = kwargs.get('panel_titles', None)
    
    for i, obj in enumerate(obj_list):
        try:
            # Convert individual object
            converted = converter_func(obj, **kwargs)
            
            if converted is None:
                logger.warning(f"Failed to convert {obj_type_name} {i+1} - got None")
                continue
                
            if isinstance(converted, dict) and converted.get('error') is not None:
                logger.warning(f"Failed to convert {obj_type_name} {i+1}: {converted.get('error')}")
                continue
            
            # Extract figure and title
            if isinstance(converted, dict) and 'data' in converted:
                figure = converted['data']
            else:
                figure = converted
                
            # Get title - use custom title if provided, otherwise try to extract from object
            if custom_titles and i < len(custom_titles):
                title = custom_titles[i]
            else:
                try:
                    if hasattr(obj, 'getTitle'):
                        title = obj.getTitle()
                    elif hasattr(obj, 'getChart') and hasattr(obj.getChart(), 'getTitle'):
                        title = obj.getChart().getTitle()
                    else:
                        title = f"{obj_type_name} {i+1}"
                except Exception:
                    title = f"{obj_type_name} {i+1}"
            
            figures.append(figure)
            titles.append(title)
            
            logger.debug(f"Successfully converted {obj_type_name} {i+1}: {title}")
            
        except Exception as e:
            logger.warning(f"Failed to convert {obj_type_name} {i+1}: {e}")
            continue
    
    return figures, titles


def _convert_viewer2d_to_chart(viewer2d, **kwargs):
    """Convert a Viewer2D object to an SNTChart."""
    # Get chart from Viewer2D
    chart = viewer2d.getChart()
    if chart is None:
        return None
    
    # Convert chart to matplotlib figure
    return _convert_snt_chart(chart, **kwargs)


def _convert_imageplus_to_xarray(imageplus, index, **kwargs):
    """Convert a single ImagePlus to xarray data with metadata."""
    from ..util import ImpUtils
    from ..core import ij
    
    # Extract metadata first
    metadata = _extract_imageplus_metadata(imageplus, **kwargs)
    
    # Convert ImagePlus to xarray using the same method as _display_imageplus
    frame = int(metadata.get('frame', 1))
    
    try:
        converted_imp = ImpUtils.convertToSimple2D(imageplus, frame)
    except (TypeError, AttributeError) as e:
        logger.debug(f"ImpUtils.convertToSimple2D failed for ImagePlus {index+1}: {e}")
        # Fallback: try direct conversion without ImpUtils
        converted_imp = imageplus
    
    # Use ij().py.from_java() to convert to xarray
    xarray_data = ij().py.from_java(converted_imp)
    
    if xarray_data is None:
        logger.warning(f"Failed to convert ImagePlus {index+1} to xarray - got None")
        return None, None, None
    
    # Get image title
    try:
        image_title = imageplus.getTitle() if hasattr(imageplus, 'getTitle') else f'Image {index+1}'
    except Exception:
        image_title = f'Image {index+1}'
    
    logger.debug(f"Successfully converted ImagePlus {index+1}: {image_title}")
    return xarray_data, metadata, image_title


def _calculate_figure_size(aspect_ratios, panel_layout, num_panels):
    """Calculate optimal figure size based on aspect ratios and layout."""
    avg_aspect = sum(aspect_ratios) / len(aspect_ratios)
    # Constrain aspect ratio to reasonable bounds
    avg_aspect = max(0.5, min(2.0, avg_aspect))
    
    if panel_layout == 'vertical' or panel_layout == (num_panels, 1):
        return (6 * avg_aspect, 4 * num_panels)
    else:
        return (4 * avg_aspect * num_panels, 4)


def _plot_image_panel(ax, xarray_data, metadata, image_title, **kwargs):
    """Plot a single image panel."""
    try:
        is_rgb = metadata.get('is_rgb', False)
        if is_rgb:
            im = ax.imshow(xarray_data.values, aspect='equal')
        else:
            cmap = kwargs.get('cmap', 'gray')
            im = ax.imshow(xarray_data.values, cmap=cmap, aspect='equal')
            if kwargs.get('add_colorbar', False):
                import matplotlib.pyplot as plt
                plt.colorbar(im, ax=ax)
        
        ax.set_title(image_title)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_aspect('equal', adjustable='box')
        
        # Remove spines (boxes) around each panel
        for spine in ax.spines.values():
            spine.set_visible(False)
        
        return True
    except Exception as e:
        logger.warning(f"Failed to plot panel: {e}")
        ax.text(0.5, 0.5, f'{image_title}\n(Plot Error)', 
               ha='center', va='center', transform=ax.transAxes)
        ax.set_title(image_title)
        
        # Remove spines even for error panels
        for spine in ax.spines.values():
            spine.set_visible(False)
        
        return False


def _apply_figure_layout(fig, title, **kwargs):
    """Apply layout settings to figure."""
    if title:
        fig.suptitle(title)
    
    use_tight_layout = kwargs.get('tight_layout', True)
    if use_tight_layout:
        try:
            pad = kwargs.get('pad', 1.08)
            import matplotlib.pyplot as plt
            import warnings
            with warnings.catch_warnings():
                warnings.simplefilter("ignore", UserWarning)
                plt.tight_layout(pad=pad)
            return
        except Exception as e:
            logger.debug(f"tight_layout failed: {e}, using subplots_adjust instead")
    
    # Manual spacing control
    import matplotlib.pyplot as plt
    plt.subplots_adjust(
        left=kwargs.get('left', 0.02),
        right=kwargs.get('right', 0.98),
        top=kwargs.get('top', 0.95 if title else 0.98),
        bottom=kwargs.get('bottom', 0.02),
        hspace=kwargs.get('hspace', 0.1),
        wspace=kwargs.get('wspace', 0.05)
    )


def _create_combined_figure(figures, titles, obj_type_name, obj_count, **kwargs):
    """
    Generic function to create a combined multi-panel figure.
    
    Parameters
    ----------
    figures : list
        List of matplotlib figures to combine
    titles : list
        List of titles for each panel
    obj_type_name : str
        Name of object type for metadata
    obj_count : int
        Original number of objects
    **kwargs
        Additional arguments including title, panel_layout
        
    Returns
    -------
    SNTObject
        Combined figure result
    """
    if not figures:
        logger.error(f"No {obj_type_name} objects could be converted successfully")
        return None
    
    logger.info(f"Successfully converted {len(figures)} {obj_type_name} objects, creating multi-panel figure")
    
    # Combine figures into multi-panel display
    title = kwargs.get('title', None)
    combined_figure = _combine_matplotlib_figures(figures, titles, title or "", **kwargs)
    
    if combined_figure is None:
        logger.error(f"Failed to combine {obj_type_name} objects into multi-panel figure")
        return None
    
    # Create result metadata
    panel_layout = kwargs.get('panel_layout', 'auto')
    metadata = {
        f'{obj_type_name.lower()}_count': obj_count,
        'displayed_count': len(figures),
        'panel_layout': panel_layout,
        'title': title
    }
    
    logger.info(f"Successfully created multi-panel figure with {len(figures)} {obj_type_name} objects")
    return _create_converter_result(combined_figure, f'{obj_type_name}_List', **metadata)


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
    Display any supported object type in the most appropriate way.
    
    Handles Java objects, SNT objects, matplotlib figures, xarray objects, 
    Viewer2D/3D objects, and lists. Automatically converts Java objects 
    and creates multi-panel displays for lists.
    
    Parameters
    ----------
    obj : Any
        Object to display (Java objects, SNTObjects, matplotlib figures, xarray objects, 
        Viewer2D/3D objects, lists, etc.)
    **kwargs
        Display arguments (cmap, title, figsize, orthoview, panel_layout, max_panels, etc.)
        
    Returns
    -------
    Any
        The displayed object (converted SNTObject, chart, snapshot, or original object)

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
            obj = _tree_to_chart(obj)

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


def _tree_to_chart(obj):
    try:
        from ..viewer import Viewer2D
        viewer = Viewer2D()
        viewer.add(obj)
        if obj.getLabel():
            viewer.setTitle(obj.getLabel())
        logger.debug(f"Got Viewer2D from tree: {type(viewer)}")
        obj = viewer.getChart()
    except Exception as e:
        logger.warning(f"Failed to get skeleton from tree: {e}")
        logger.info("Trying alternative skeleton extraction methods...")
        # skeleton = None
        # try:
        #     # Try alternative methods to get skeleton2D
        #     skeleton = obj.getSkeleton2D()
        #     logger.debug(f"Got skeleton using getSkeleton2D(): {type(skeleton)}")
        # except Exception as e2:
        #     logger.debug(f"Alternative skeleton extraction failed: {e2}")
        # if skeleton is not None:
        #     obj = skeleton
        #     logger.info(f"Successfully extracted skeleton using alternative method: {type(obj)}")
    return obj


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


@handle_display_errors("display SNTTable")
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


@handle_display_errors("display SNTChart")
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


@handle_display_errors("display SNTGraph")
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
    Handle display of lists of supported objects as multi-panel figures.
    
    Parameters
    ----------
    obj_list : list or tuple
        List of objects to display
    **kwargs
        Display arguments
        
    Returns
    -------
    Any
        Display result
    """
    logger.debug(f"Processing list of {len(obj_list)} objects")
    
    if not obj_list:
        logger.warning("Empty list provided to display")
        return None
    
    # Check object types in the list
    chart_objects = []
    viewer2d_objects = []
    imageplus_objects = []
    tree_objects = []
    other_objects = []
    
    for i, obj in enumerate(obj_list):
        if _is_snt_chart(obj):
            chart_objects.append(obj)
        elif _is_viewer2d(obj):
            viewer2d_objects.append(obj)
        elif str(type(obj)).find('ImagePlus') != -1:
            imageplus_objects.append(obj)
        elif _is_snt_tree(obj):
            tree_objects.append(obj)
        else:
            other_objects.append((i, type(obj).__name__))
    
    # Handle pure lists of supported objects
    if chart_objects and not viewer2d_objects and not imageplus_objects and not tree_objects and not other_objects:
        # Pure SNTChart list - use multi-panel display
        logger.info(f"Detected list of {len(chart_objects)} SNTChart objects")
        return _display_snt_chart_list(chart_objects, **kwargs)
    elif viewer2d_objects and not chart_objects and not imageplus_objects and not tree_objects and not other_objects:
        # Pure Viewer2D list - use multi-panel display
        logger.info(f"Detected list of {len(viewer2d_objects)} Viewer2D objects")
        return _display_viewer2d_list(viewer2d_objects, **kwargs)
    elif imageplus_objects and not chart_objects and not viewer2d_objects and not tree_objects and not other_objects:
        # Pure ImagePlus list - use multi-panel display
        logger.info(f"Detected list of {len(imageplus_objects)} ImagePlus objects")
        return _display_imageplus_list(imageplus_objects, **kwargs)
    elif tree_objects and not chart_objects and not viewer2d_objects and not imageplus_objects and not other_objects:
        # Pure Tree list - use multi-panel display
        logger.info(f"Detected list of {len(tree_objects)} Tree objects")
        return _display_tree_list(tree_objects, **kwargs)
    elif (chart_objects or viewer2d_objects or imageplus_objects or tree_objects) and other_objects:
        # Mixed list - warn and display supported objects
        supported_count = len(chart_objects) + len(viewer2d_objects) + len(imageplus_objects) + len(tree_objects)
        logger.warning(f"Mixed object list detected. Displaying {supported_count} supported objects, "
                      f"ignoring {len(other_objects)} other objects: {[name for _, name in other_objects]}")
        
        # Prioritize charts > viewer2d > imageplus > trees if multiple types are present
        if chart_objects:
            return _display_snt_chart_list(chart_objects, **kwargs)
        elif viewer2d_objects:
            return _display_viewer2d_list(viewer2d_objects, **kwargs)
        elif imageplus_objects:
            return _display_imageplus_list(imageplus_objects, **kwargs)
        else:
            return _display_tree_list(tree_objects, **kwargs)
    elif (chart_objects and viewer2d_objects) or (chart_objects and imageplus_objects) or (viewer2d_objects and imageplus_objects):
        # Mixed supported objects - prioritize charts > viewer2d > imageplus
        if chart_objects:
            logger.warning(f"Mixed list detected. Displaying {len(chart_objects)} SNTChart objects, "
                          f"ignoring other supported objects.")
            return _display_snt_chart_list(chart_objects, **kwargs)
        elif viewer2d_objects:
            logger.warning(f"Mixed list detected. Displaying {len(viewer2d_objects)} Viewer2D objects, "
                          f"ignoring ImagePlus objects.")
            return _display_viewer2d_list(viewer2d_objects, **kwargs)
    else:
        # No supported objects for list display
        logger.warning(f"List contains no supported objects for multi-panel display. "
                      f"Object types: {[type(obj).__name__ for obj in obj_list]}")
        logger.info("Falling back to individual display of first object")
        return display(obj_list[0], **kwargs)


@handle_display_errors("display SNTChart list")
def _display_snt_chart_list(chart_list: list, **kwargs) -> Any:
    """Display a list of SNTChart objects as a multi-panel matplotlib figure."""
    # Limit number of charts
    max_panels = kwargs.get('max_panels', 20)
    if len(chart_list) > max_panels:
        logger.warning(f"Chart list has {len(chart_list)} items, limiting to {max_panels}")
        chart_list = chart_list[:max_panels]
    
    logger.info(f"Converting {len(chart_list)} SNTChart objects to matplotlib figures")
    
    # Use common conversion logic
    figures, titles = _convert_objects_to_figures(chart_list, _convert_snt_chart, "SNTChart", **kwargs)
    
    # Use common figure combination logic
    return _create_combined_figure(figures, titles, "SNTChart", len(chart_list), **kwargs)


@handle_display_errors("display Viewer2D list")
def _display_viewer2d_list(viewer2d_list: list, **kwargs) -> Any:
    """Display a list of Viewer2D objects as a multi-panel matplotlib figure."""
    # Limit number of viewers
    max_panels = kwargs.get('max_panels', 20)
    if len(viewer2d_list) > max_panels:
        logger.warning(f"Viewer2D list has {len(viewer2d_list)} items, limiting to {max_panels}")
        viewer2d_list = viewer2d_list[:max_panels]
    
    logger.info(f"Extracting charts from {len(viewer2d_list)} Viewer2D objects")
    
    # Use common conversion logic with Viewer2D-specific converter
    figures, titles = _convert_objects_to_figures(viewer2d_list, _convert_viewer2d_to_chart, "Viewer2D", **kwargs)
    
    # Use common figure combination logic
    return _create_combined_figure(figures, titles, "Viewer2D", len(viewer2d_list), **kwargs)


@handle_display_errors("display Tree list")
def _display_tree_list(tree_list: list, **kwargs) -> Any:
    """Display a list of Tree objects as a multi-panel matplotlib figure."""
    # Limit number of trees
    max_panels = kwargs.get('max_panels', 20)
    if len(tree_list) > max_panels:
        logger.warning(f"Tree list has {len(tree_list)} items, limiting to {max_panels}")
        tree_list = tree_list[:max_panels]
    
    logger.info(f"Converting {len(tree_list)} Tree objects to 2D skeletons")
    
    # Convert each tree to ImagePlus (2D skeleton)
    displayable_list = []
    for i, tree in enumerate(tree_list):
        try:
            dis_tree = _tree_to_chart(tree)
            if dis_tree is not None:
                displayable_list.append(dis_tree)
                logger.debug(f"Successfully converted Tree {i+1} to skeleton: {tree.getLabel()}")
            else:
                logger.warning(f"Tree {i+1} getSkeleton2D() returned None")
        except Exception as e:
            logger.warning(f"Failed to convert Tree {i+1} to skeleton: {e}")
            continue
    
    if not displayable_list:
        logger.error("No Tree objects could be converted to skeletons")
        return None
    
    logger.info(f"Successfully converted {len(displayable_list)} trees, displaying as multi-panel figure")
    
    # Use the ImagePlus list display function
    return _display_snt_chart_list(displayable_list, **kwargs)


@handle_display_errors("display ImagePlus list")
def _display_imageplus_list(imageplus_list: list, **kwargs) -> Any:
    """
    Display a list of ImagePlus objects as a multi-panel matplotlib figure.
    
    Parameters
    ----------
    imageplus_list : list
        List of ImagePlus objects to display
    **kwargs
        Display arguments (panel_layout, max_panels, title, figsize, etc.)
        
    Returns
    -------
    Any
        SNTObject containing the combined matplotlib figure
    """
    try:
        # Get parameters
        max_panels = kwargs.get('max_panels', 20)
        title = kwargs.get('title', None)
        panel_layout = kwargs.get('panel_layout', 'auto')
        
        # Limit number of ImagePlus objects
        if len(imageplus_list) > max_panels:
            logger.warning(f"ImagePlus list has {len(imageplus_list)} items, limiting to {max_panels}")
            imageplus_list = imageplus_list[:max_panels]
        
        logger.info(f"Creating multi-panel figure directly from {len(imageplus_list)} ImagePlus objects")
        
        # Convert each ImagePlus to xarray data
        xarray_data_list = []
        image_titles = []
        
        for i, imageplus in enumerate(imageplus_list):
            try:
                xarray_data, metadata, image_title = _convert_imageplus_to_xarray(imageplus, i, **kwargs)
                if xarray_data is not None:
                    xarray_data_list.append((xarray_data, metadata))
                    image_titles.append(image_title)
            except Exception as e:
                logger.warning(f"Failed to convert ImagePlus {i+1}: {e}")
                continue
        
        if not xarray_data_list:
            logger.error("No ImagePlus objects could be converted successfully")
            return None
        
        # Create multi-panel figure directly (reverted to simple approach)
        import matplotlib.pyplot as plt
        from .utils import _create_subplot_grid
        
        num_panels = len(xarray_data_list)
        
        # Calculate aspect ratios and figure size
        aspect_ratios = [(xarray_data.shape[-1] / xarray_data.shape[-2]) for xarray_data, _ in xarray_data_list]
        figsize = kwargs.get('figsize') or _calculate_figure_size(aspect_ratios, panel_layout, num_panels)
        
        fig, axes, (rows, cols) = _create_subplot_grid(num_panels, panel_layout, figsize)
        
        logger.debug(f"Created {rows}x{cols} grid for {num_panels} panels")
        
        # Plot each image in its subplot
        for i, ((xarray_data, metadata), image_title) in enumerate(zip(xarray_data_list, image_titles)):
            if i < len(axes):
                _plot_image_panel(axes[i], xarray_data, metadata, image_title, **kwargs)
        
        # Hide unused subplots
        for i in range(num_panels, len(axes)):
            axes[i].set_visible(False)
        
        # Apply layout
        _apply_figure_layout(fig, title, **kwargs)
        
        # Create result
        metadata = {
            'imageplus_count': len(imageplus_list),
            'displayed_count': num_panels,
            'panel_layout': (rows, cols),
            'title': title
        }
        
        logger.info(f"Successfully created multi-panel figure with {num_panels} ImagePlus objects")
        return _create_converter_result(fig, 'ImagePlus_List', **metadata)
        
    except Exception as e:
        raise  # Let decorator handle it


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


@handle_display_errors("display Viewer3D")
def _display_viewer3d(obj, **kwargs):
    """
    Handler function for Viewer3D display.
    
    Takes a snapshot and displays the RGB image. If orthoview=True, captures 
    orthogonal views (xy, xz, yz) as a multi-panel figure.
    
    Parameters
    ----------
    obj : Viewer3D
        The Viewer3D object to display
    **kwargs : dict
        Display arguments (orthoview, title, figsize, etc.)
        
    Returns
    -------
    ImagePlus or SNTObject
        Snapshot ImagePlus or combined figure if orthoview=True
    """
    orthoview = kwargs.pop('orthoview', False)
    
    if orthoview:
        logger.info("Detected Viewer3D object with orthoview=True - capturing orthogonal views...")
        return _display_viewer3d_orthoview(obj, **kwargs)
    else:
        logger.info("Detected Viewer3D object - taking snapshot...")
        
        try:
            # Take a snapshot of the 3D viewer
            snapshot = obj.snapshot()
            from ..util import ImpUtils
            ImpUtils.crop(snapshot,  0 if obj.isDarkModeOn() else 255)

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
            raise  # Let decorator handle it


@handle_display_errors("display Viewer3D orthogonal views")
def _display_viewer3d_orthoview(obj, **kwargs):
    """
    Display Viewer3D with orthogonal views (xy, xz, yz).
    
    Parameters
    ----------
    obj : Viewer3D
        The Viewer3D object to display
    **kwargs : dict
        Display arguments
        
    Returns
    -------
    SNTObject
        Combined matplotlib figure with orthogonal views
    """
    try:
        # Capture snapshots from three orthogonal views
        result = []
        view_modes = ["xy", "xz", "yz"]
        view_titles = kwargs.get('view_titles', ["XY View", "XZ View", "YZ View"])
        
        logger.info("Capturing orthogonal views: xy, xz, yz")
        for view_mode, view_title in zip(view_modes, view_titles):
            try:
                # Take cropped snapshot
                snapshot = obj.snapshot(view_mode)
                if snapshot is None:
                    logger.warning(f"Viewer3D.snapshot() returned None for {view_mode} view")
                    continue
                
                # Add title to snapshot for better identification
                snapshot.setTitle(view_title)
                result.append(snapshot)
                logger.debug(f"Successfully captured {view_mode} view snapshot")
                
            except Exception as e:
                logger.warning(f"Failed to capture {view_mode} view: {e}")
                continue

        if not result:
            logger.error("Failed to capture any orthogonal views")
            return None
        
        logger.info(f"Successfully captured {len(result)} orthogonal views")
        
        # Set up kwargs for multi-panel display
        ortho_kwargs = kwargs.copy()
        
        # Don't set a default title - let it be None unless explicitly provided
        
        # Set default panel layout for orthogonal views
        if 'panel_layout' not in ortho_kwargs:
            if len(result) == 3:
                ortho_kwargs['panel_layout'] = 'horizontal'  # 1x3 layout for three views
            else:
                ortho_kwargs['panel_layout'] = 'auto'
        
        # Display the list of snapshots using the ImagePlus list display functionality
        display_result = _display_imageplus_list(result, **ortho_kwargs)
        
        # Return the display result (SNTObject with matplotlib figure) instead of raw ImagePlus list
        # This prevents Jupyter notebooks from printing the raw Java object list
        return display_result
        
    except Exception as e:
        raise  # Let decorator handle it


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


@handle_display_errors("display Viewer2D")
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
        
        # Don't set a default title - let user explicitly provide one if needed
        # The chart's internal title (like "Reconstruction Plotter") is often not desired
        
        # Display the chart using the SNTChart display pipeline and return the result
        return _display_snt_chart(chart, **kwargs_with_metadata)
        
    except Exception as e:
        raise  # Let decorator handle it
