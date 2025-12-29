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


# =============================================================================
# Helper Functions
# =============================================================================

def _add_metadata(kwargs, **metadata_updates):
    """
    Add metadata to kwargs dictionary, creating the metadata dict if needed.

    Parameters
    ----------
    kwargs : dict
        The kwargs dictionary to update
    **metadata_updates
        Key-value pairs to add to metadata

    Returns
    -------
    dict
        Copy of kwargs with updated metadata
    """
    kwargs = kwargs.copy()
    if 'metadata' not in kwargs:
        kwargs['metadata'] = {}
    kwargs['metadata'].update(metadata_updates)
    return kwargs


def _is_java_type(obj, *type_names):
    """
    Check if object is one of the given Java type names.

    Parameters
    ----------
    obj : Any
        Object to check
    *type_names : str
        Type name strings to check for (e.g., 'ImgPlus', 'ImagePlus')

    Returns
    -------
    bool
        True if object's type string contains any of the given names
    """
    type_str = str(type(obj))
    return any(name in type_str for name in type_names)


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


# =============================================================================
# Generic Conversion and Display Helpers
# =============================================================================

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
    custom_titles = kwargs.get('panel_titles', None)

    for i, obj in enumerate(obj_list):
        try:
            converted = converter_func(obj, **kwargs)

            if converted is None:
                logger.warning(f"Failed to convert {obj_type_name} {i + 1} - got None")
                continue

            if isinstance(converted, dict) and converted.get('error') is not None:
                logger.warning(f"Failed to convert {obj_type_name} {i + 1}: {converted.get('error')}")
                continue

            # Extract figure and title
            figure = converted['data'] if isinstance(converted, dict) and 'data' in converted else converted

            # Get title - use custom title if provided, otherwise try to extract from object
            if custom_titles and i < len(custom_titles):
                title = custom_titles[i]
            else:
                title = _extract_title(obj, f"{obj_type_name} {i + 1}")

            figures.append(figure)
            titles.append(title)
            logger.debug(f"Successfully converted {obj_type_name} {i + 1}: {title}")

        except Exception as e:
            logger.warning(f"Failed to convert {obj_type_name} {i + 1}: {e}")
            continue

    return figures, titles


def _extract_title(obj, default_title):
    """Extract title from an object using common methods."""
    try:
        if hasattr(obj, 'getTitle'):
            return obj.getTitle()
        elif hasattr(obj, 'getChart') and hasattr(obj.getChart(), 'getTitle'):
            return obj.getChart().getTitle()
    except Exception:
        pass
    return default_title


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

    title = kwargs.get('title', None)
    combined_figure = _combine_matplotlib_figures(figures, titles, title or "", **kwargs)

    if combined_figure is None:
        logger.error(f"Failed to combine {obj_type_name} objects into multi-panel figure")
        return None

    panel_layout = kwargs.get('panel_layout', 'auto')
    metadata = {
        f'{obj_type_name.lower()}_count': obj_count,
        'displayed_count': len(figures),
        'panel_layout': panel_layout,
        'title': title
    }

    logger.info(f"Successfully created multi-panel figure with {len(figures)} {obj_type_name} objects")
    return _create_converter_result(combined_figure, f'{obj_type_name}_List', **metadata)


def _limit_list_size(obj_list, obj_type_name, max_panels=20):
    """Limit list size and log warning if truncated."""
    if len(obj_list) > max_panels:
        logger.warning(f"{obj_type_name} list has {len(obj_list)} items, limiting to {max_panels}")
        return obj_list[:max_panels]
    return obj_list


def _display_typed_list(obj_list, converter_func, type_name, show=True, **kwargs):
    """
    Generic handler for displaying lists of homogeneous objects.

    Parameters
    ----------
    obj_list : list
        List of objects to display
    converter_func : callable
        Function to convert individual objects to figures
    type_name : str
        Name of the object type for logging
    show : bool
        Whether to display immediately
    **kwargs
        Additional display arguments

    Returns
    -------
    SNTObject
        Combined multi-panel figure result
    """
    max_panels = kwargs.get('max_panels', 20)
    obj_list = _limit_list_size(obj_list, type_name, max_panels)

    logger.info(f"Converting {len(obj_list)} {type_name} objects")
    figures, titles = _convert_objects_to_figures(obj_list, converter_func, type_name, **kwargs)
    return _create_combined_figure(figures, titles, type_name, len(obj_list), **kwargs)


# =============================================================================
# Optional Dependencies
# =============================================================================

try:
    import matplotlib.pyplot as plt
    from matplotlib.figure import Figure

    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False
    Figure = None

try:
    import pandas

    HAS_PANDAS = True
except ImportError:
    HAS_PANDAS = False
    pandas = None


# =============================================================================
# Type Detection for List Display
# =============================================================================

def _classify_objects_for_list_display(obj_list):
    """
    Classify objects in a list by their type for multi-panel display.

    Parameters
    ----------
    obj_list : list
        List of objects to classify

    Returns
    -------
    dict
        Dictionary mapping type names to lists of objects
    """
    classified = {
        'chart': [],
        'viewer2d': [],
        'imgplus': [],
        'imageplus': [],
        'tree': [],
        'figure': [],
        'other': []
    }

    for i, obj in enumerate(obj_list):
        if _is_snt_chart(obj):
            classified['chart'].append(obj)
        elif _is_viewer2d(obj):
            classified['viewer2d'].append(obj)
        elif _is_java_type(obj, 'ImgPlus'):
            classified['imgplus'].append(obj)
        elif _is_java_type(obj, 'ImagePlus'):
            classified['imageplus'].append(obj)
        elif _is_snt_tree(obj):
            classified['tree'].append(obj)
        elif HAS_MATPLOTLIB and isinstance(obj, Figure):
            classified['figure'].append(obj)
        else:
            classified['other'].append((i, type(obj).__name__))

    return classified


def _get_single_type_handler(classified):
    """
    Get the handler for a list containing only one type of displayable object.

    Parameters
    ----------
    classified : dict
        Classification result from _classify_objects_for_list_display

    Returns
    -------
    tuple or None
        (type_name, objects, handler_func) if single type, None if mixed
    """
    # Priority order for display handlers
    type_handlers = [
        ('chart', _display_snt_chart_list),
        ('viewer2d', _display_viewer2d_list),
        ('imgplus', _display_imgplus_list),
        ('imageplus', _display_imageplus_list),
        ('tree', _display_tree_list),
        ('figure', _display_matplotlib_figure_list),
    ]

    # Find which types have objects
    populated = [(name, classified[name], handler)
                 for name, handler in type_handlers
                 if classified[name]]

    # Check if it's a pure single-type list (no other types, no unknown objects)
    if len(populated) == 1 and not classified['other']:
        return populated[0]

    return None


def _get_priority_handler(classified):
    """
    Get the highest-priority handler for a mixed list.

    Parameters
    ----------
    classified : dict
        Classification result from _classify_objects_for_list_display

    Returns
    -------
    tuple or None
        (type_name, objects, handler_func) for highest priority type with objects
    """
    # Priority order
    type_handlers = [
        ('chart', _display_snt_chart_list),
        ('viewer2d', _display_viewer2d_list),
        ('imgplus', _display_imgplus_list),
        ('imageplus', _display_imageplus_list),
        ('figure', _display_matplotlib_figure_list),
        ('tree', _display_tree_list),
    ]

    for name, handler in type_handlers:
        if classified[name]:
            return (name, classified[name], handler)

    return None


# =============================================================================
# Image Conversion Helpers
# =============================================================================

def _convert_viewer2d_to_chart(viewer2d, **kwargs):
    """Convert a Viewer2D object to an SNTChart."""
    chart = viewer2d.getChart()
    if chart is None:
        return None
    return _convert_snt_chart(chart, **kwargs)


def _convert_imageplus_to_xarray(imageplus, index, **kwargs):
    """Convert a single ImagePlus to xarray data with metadata."""
    from ..util import ImpUtils
    from ..core import ij

    metadata = _extract_imageplus_metadata(imageplus, **kwargs)
    frame = int(metadata.get('frame', 1))

    try:
        converted_imp = ImpUtils.convertToSimple2D(imageplus, frame)
    except (TypeError, AttributeError) as e:
        logger.debug(f"ImpUtils.convertToSimple2D failed for ImagePlus {index + 1}: {e}")
        converted_imp = imageplus

    xarray_data = ij().py.from_java(converted_imp)

    if xarray_data is None:
        logger.warning(f"Failed to convert ImagePlus {index + 1} to xarray - got None")
        return None, None, None

    try:
        image_title = imageplus.getTitle() if hasattr(imageplus, 'getTitle') else f'Image {index + 1}'
    except Exception:
        image_title = f'Image {index + 1}'

    logger.debug(f"Successfully converted ImagePlus {index + 1}: {image_title}")
    return xarray_data, metadata, image_title


# =============================================================================
# Figure Layout Helpers
# =============================================================================

def _calculate_figure_size(aspect_ratios, panel_layout, num_panels):
    """Calculate optimal figure size based on aspect ratios and layout."""
    avg_aspect = sum(aspect_ratios) / len(aspect_ratios)
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

        for spine in ax.spines.values():
            spine.set_visible(False)

        return True
    except Exception as e:
        logger.warning(f"Failed to plot panel: {e}")
        ax.text(0.5, 0.5, f'{image_title}\n(Plot Error)',
                ha='center', va='center', transform=ax.transAxes)
        ax.set_title(image_title)
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

    import matplotlib.pyplot as plt
    plt.subplots_adjust(
        left=kwargs.get('left', 0.02),
        right=kwargs.get('right', 0.98),
        top=kwargs.get('top', 0.95 if title else 0.98),
        bottom=kwargs.get('bottom', 0.02),
        hspace=kwargs.get('hspace', 0.1),
        wspace=kwargs.get('wspace', 0.05)
    )


# =============================================================================
# Main Display Function
# =============================================================================

def display(obj: Any, show: bool = True, **kwargs) -> Any:
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
    show : bool, default True
        Whether to display the figure immediately. If False, creates the figure
        but doesn't show it (useful for chaining: fig1 = pysnt.display(obj, show=False))
    **kwargs
        Display arguments including:
        - cmap: str, colormap for grayscale images
        - title: str, display title
        - figsize: tuple, figure size
        - orthoview: bool, for 3D viewers
        - panel_layout: str, layout for multi-panel displays
        - max_panels: int, maximum panels to display
        - origin: str, origin for image display ('upper', 'lower', 'auto')

    Returns
    -------
    Any
        Return value depends on input type
    """
    logger.debug(f"display() called with object type: {type(obj)}")

    # Check if obj is a list of supported objects
    if isinstance(obj, (list, tuple)):
        return _display_object_list(obj, show=show, **kwargs)

    # Validate and normalize kwargs
    kwargs = _validate_display_kwargs(**kwargs)

    # Add recursion protection
    _recursion_key = f"_display_recursion_{id(obj)}"
    if kwargs.get('_internal', {}).get(_recursion_key, False):
        logger.error(f"Infinite recursion detected for object {type(obj)} - stopping")
        return None

    kwargs['_internal'][_recursion_key] = True

    try:
        # Handle special SNT object types that need preprocessing
        if _is_snt_tree(obj):
            logger.debug(f"Detected SNT Tree: {type(obj)}")
            obj = _tree_to_chart(obj)
        elif _is_java_type(obj, 'ImagePlus'):
            # Check if this ImagePlus might be a skeleton
            try:
                title = obj.getTitle() if hasattr(obj, 'getTitle') else ""
                if title.startswith('Skel'):
                    logger.debug(f"Detected ImagePlus skeleton: {title}")
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
            from .visual_display import _display_matplotlib_figure
            _display_matplotlib_figure(obj, show=show, **kwargs)
            return obj
        elif obj_type == 'xarray':
            logger.info(f"Displaying xarray object: {type(obj)}")
            from .data_display import _display_xarray
            _display_xarray(obj, show=show, **kwargs)
            return obj
        elif obj_type == 'snt_object':
            return _handle_snt_object_display(obj, show=show, **kwargs)
        else:
            return handler(obj, show=show, **kwargs)

    except Exception as e:
        _handle_display_error(e, "Display operation", str(type(obj)))
        raise
    finally:
        if '_internal' in kwargs and _recursion_key in kwargs['_internal']:
            del kwargs['_internal'][_recursion_key]


def _tree_to_chart(obj):
    """Convert a Tree object to a chart via Viewer2D."""
    try:
        from ..viewer import Viewer2D
        viewer = Viewer2D()
        viewer.add(obj)
        if obj.getLabel():
            viewer.setTitle(obj.getLabel())
        logger.debug(f"Got Viewer2D from tree: {type(viewer)}")
        return viewer.getChart()
    except Exception as e:
        logger.warning(f"Failed to get skeleton from tree: {e}")
        logger.info("Trying alternative skeleton extraction methods...")
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

    # Check for ImgPlus objects (before ImagePlus check since ImgPlus is more specific)
    if _is_java_type(obj, 'ImgPlus'):
        return 'imgplus', _display_imgplus

    # Check for ImagePlus objects
    if _is_java_type(obj, 'ImagePlus'):
        from .data_display import _display_imageplus
        return 'imageplus', _display_imageplus

    # Check for pandas DataFrames
    if HAS_PANDAS and isinstance(obj, pandas.DataFrame):
        from .data_display import _display_pandas_dataframe
        return 'pandas_dataframe', _display_pandas_dataframe

    # Check for NetworkX graphs (direct, not wrapped in SNTObject)
    if hasattr(obj, 'number_of_nodes') and hasattr(obj, 'number_of_edges'):
        return 'networkx_graph', _display_networkx_graph

    # Check for ImgLib2 RandomAccessibleInterval objects
    if hasattr(obj, 'numDimensions') and hasattr(obj, 'dimension') and not _is_java_type(obj, 'ImgPlus'):
        logger.debug(f"Detected ImgLib2 object: {type(obj)}")
        return 'imglib2_rai', _display_imglib2_rai

    # Check numpy arrays
    if hasattr(obj, 'shape') and hasattr(obj, 'dtype') and hasattr(obj, 'ndim'):
        logger.debug(f"Detected numpy-like object: {type(obj)}")
        from .visual_display import _display_array_data
        return 'numpy_array', lambda arr, show=True, **kw: _display_array_data(arr, "numpy array", show=show, **kw)

    # Default to Java object conversion
    return 'java_object', _display_with_auto_conversion


# =============================================================================
# SNT Object Display Handlers
# =============================================================================

def _handle_snt_object_display(obj, show: bool = True, **kwargs):
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
        _display_matplotlib_figure(data, show=show, **kwargs)
        return obj
    elif _is_xarray_object(data):
        try:
            if hasattr(data, 'sizes'):
                size_info = dict(data.sizes)
            elif hasattr(data, 'shape'):
                size_info = data.shape
            else:
                size_info = "unknown"
            logger.info(f"Displaying xarray object (sizes: {size_info})")
        except Exception as e:
            logger.info(f"Displaying xarray object (size info unavailable: {e})")

        metadata = obj.get('metadata', {})
        kwargs_with_metadata = kwargs.copy()
        kwargs_with_metadata['metadata'] = metadata

        from .data_display import _display_xarray
        _display_xarray(data, show=show, **kwargs_with_metadata)
        return obj
    elif hasattr(data, 'shape') and hasattr(data, 'dtype'):  # numpy array
        logger.info(f"Displaying numpy array (size: {data.size})")
        import numpy as np
        with np.printoptions(precision=3, suppress=True):
            print(data)
        return obj
    elif hasattr(data, 'number_of_nodes'):  # NetworkX graph
        logger.info(
            f"Displaying NetworkX graph ({type(data).__name__} with {data.number_of_nodes()} nodes, {data.number_of_edges()} edges)")
        try:
            metadata = obj.get('metadata', {})
            graph_type = metadata.get('original_type', 'Unknown')
            kwargs_with_type = kwargs.copy()
            kwargs_with_type['graph_type'] = graph_type

            logger.debug(f"Using graph type '{graph_type}' for layout defaults")

            from .visual_display import _graph_to_matplotlib, _display_matplotlib_figure
            fig = _graph_to_matplotlib(data, **kwargs_with_type)
            _display_matplotlib_figure(fig, show=show, **kwargs)
            return obj
        except Exception as e:
            logger.error(f"Failed to display NetworkX graph: {e}")
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
def _display_snt_table(obj, show: bool = True, **kwargs):
    """Handler function for SNTTable display."""
    logger.info("Detected SNTTable object - converting and displaying...")
    converted = _convert_snt_table(obj, **kwargs)

    if converted.get('error') is not None:
        logger.error(f"SNTTable conversion failed: {converted.get('error')}")
        return None

    return _handle_snt_object_display(converted, show=show, **kwargs)


@handle_display_errors("display SNTChart")
def _display_snt_chart(obj, show: bool = True, **kwargs):
    """Handler function for SNTChart display."""
    logger.info("Detected SNTChart object - converting and displaying...")
    converted = _convert_snt_chart(obj, **kwargs)

    if converted.get('error') is not None:
        logger.error(f"SNTChart conversion failed: {converted.get('error')}")
        return None

    return _handle_snt_object_display(converted, show=show, **kwargs)


@handle_display_errors("display SNTGraph")
def _display_snt_graph(obj, show: bool = True, **kwargs):
    """Handler function for SNTGraph display."""
    logger.info("Detected SNTGraph object - converting and displaying...")
    converted = _convert_snt_graph(obj, **kwargs)

    if converted.get('error') is not None:
        logger.error(f"SNTGraph conversion failed: {converted.get('error')}")
        return None

    return _handle_snt_object_display(converted, show=show, **kwargs)


# =============================================================================
# Viewer Display Handlers
# =============================================================================

def _is_viewer3d(obj) -> bool:
    """Check if object is a Viewer3D."""
    class_name = str(type(obj))
    return 'Viewer3D' in class_name and hasattr(obj, 'snapshot')


def _is_viewer2d(obj) -> bool:
    """Check if object is a Viewer2D."""
    class_name = str(type(obj))
    return 'Viewer2D' in class_name and hasattr(obj, 'getChart')


@handle_display_errors("display Viewer3D")
def _display_viewer3d(obj, show: bool = True, **kwargs):
    """Handler function for Viewer3D display."""
    orthoview = kwargs.pop('orthoview', False)

    if orthoview:
        logger.info("Detected Viewer3D object with orthoview=True - capturing orthogonal views...")
        return _display_viewer3d_orthoview(obj, show=show, **kwargs)

    logger.info("Detected Viewer3D object - taking snapshot...")

    snapshot = obj.snapshot()
    from ..util import ImpUtils
    ImpUtils.crop(snapshot, 0 if obj.isDarkModeOn() else 255)

    if snapshot is None:
        logger.error("Viewer3D.snapshot() returned None")
        return None

    logger.info(f"Successfully captured Viewer3D snapshot: {snapshot}")

    kwargs = _add_metadata(kwargs, source_type='Viewer3D', is_rgb=True, viewer3d_snapshot=True)

    if 'title' not in kwargs:
        kwargs['title'] = "3D Viewer Snapshot"

    from .data_display import _display_imageplus
    _display_imageplus(snapshot, show=show, **kwargs)

    return snapshot


@handle_display_errors("display Viewer3D orthogonal views")
def _display_viewer3d_orthoview(obj, show: bool = True, **kwargs):
    """Display Viewer3D with orthogonal views (xy, xz, yz)."""
    result = []
    view_modes = ["xy", "xz", "yz"]
    view_titles = kwargs.get('view_titles', ["XY View", "XZ View", "YZ View"])

    logger.info("Capturing orthogonal views: xy, xz, yz")
    for view_mode, view_title in zip(view_modes, view_titles):
        try:
            snapshot = obj.snapshot(view_mode)
            if snapshot is None:
                logger.warning(f"Viewer3D.snapshot() returned None for {view_mode} view")
                continue

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

    ortho_kwargs = kwargs.copy()
    if 'panel_layout' not in ortho_kwargs:
        ortho_kwargs['panel_layout'] = 'horizontal' if len(result) == 3 else 'auto'

    display_result = _display_imageplus_list(result, show=show, **ortho_kwargs)
    return display_result


@handle_display_errors("display Viewer2D")
def _display_viewer2d(obj, show: bool = True, **kwargs):
    """Handler function for Viewer2D display."""
    logger.info("Detected Viewer2D object - getting chart...")

    chart = obj.getChart()

    if chart is None:
        logger.error("Viewer2D.getChart() returned None")
        return None

    logger.info(f"Successfully retrieved Viewer2D chart: {chart}")

    kwargs = _add_metadata(kwargs, source_type='Viewer2D', viewer2d_chart=True)

    return _display_snt_chart(chart, show=show, **kwargs)


# =============================================================================
# Image Display Handlers
# =============================================================================

@handle_display_errors("display ImgLib2 RandomAccessibleInterval")
def _display_imglib2_rai(obj, show: bool = True, **kwargs):
    """Handler function for RandomAccessibleInterval display."""
    logger.info("Detected RandomAccessibleInterval object - converting to ImagePlus for display...")

    import scyjava
    ImgUtils = scyjava.jimport("sc.fiji.snt.util.ImgUtils")
    title = kwargs.get('title', "RAI")
    imageplus = ImgUtils.raiToImp(obj, title)

    if imageplus is None:
        logger.error("ImgUtils.raiToImp() returned None")
        return None

    kwargs = _add_metadata(kwargs, source_type='RandomAccessibleInterval', rai_conversion=True)

    from .data_display import _display_imageplus
    return _display_imageplus(imageplus, show=show, **kwargs)


@handle_display_errors("display ImgPlus")
def _display_imgplus(obj, show: bool = True, **kwargs):
    """Handler function for ImgPlus display."""
    logger.info("Detected ImgPlus object - converting to ImagePlus for display...")

    import scyjava
    ImgUtils = scyjava.jimport("sc.fiji.snt.util.ImgUtils")
    imageplus = ImgUtils.toImagePlus(obj)

    if imageplus is None:
        logger.error("ImgUtils.toImagePlus() returned None")
        return None

    kwargs = _add_metadata(kwargs, source_type='ImgPlus', imgplus_conversion=True)

    from .data_display import _display_imageplus
    return _display_imageplus(imageplus, show=show, **kwargs)


@handle_display_errors("display NetworkX graph")
def _display_networkx_graph(graph, show: bool = True, **kwargs):
    """Handler function for direct NetworkX graph display."""
    logger.info(
        f"Displaying NetworkX graph ({type(graph).__name__} with {graph.number_of_nodes()} nodes, {graph.number_of_edges()} edges)")

    if 'graph_type' not in kwargs:
        kwargs['graph_type'] = 'Unknown'

    from .visual_display import _graph_to_matplotlib, _display_matplotlib_figure
    fig = _graph_to_matplotlib(graph, **kwargs)
    _display_matplotlib_figure(fig, show=show, **kwargs)

    return graph


# =============================================================================
# Auto-conversion and Fallback
# =============================================================================

def _display_with_auto_conversion(obj: Any, show: bool = True, **kwargs) -> Any:
    """Attempt to display a raw Java object by trying available converters."""
    logger.debug(f"Attempting auto-conversion for {type(obj)}")

    try:
        import scyjava as sj

        logger.debug("Trying scyjava.to_python() with registered converters...")
        converted = sj.to_python(obj)

        if converted is not None and converted != obj:
            logger.debug(f"Successfully converted {type(obj)} to {type(converted)}")
            return display(converted, **kwargs)
        else:
            logger.debug("scyjava.to_python() returned None or same object")

    except Exception as e:
        logger.debug(f"Auto-conversion failed: {e}")

    return _display_generic_object(obj, **kwargs)


def _display_generic_object(obj: Any, **kwargs) -> Any:
    """Enhanced fallback display function for any Python object."""
    logger.info(f"Using generic display for {type(obj)}")

    print(f"Object type: {type(obj)}")
    print(f"Object: {obj}")

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


# =============================================================================
# List Display Functions
# =============================================================================

def _display_object_list(obj_list: list, show: bool = True, **kwargs) -> Any:
    """
    Handle display of lists of supported objects as multi-panel figures.

    Automatically extracts matplotlib figures from SNTObject dictionaries
    to support seamless chaining like: pysnt.display([pysnt.display(obj1), pysnt.display(obj2)])
    """
    logger.debug(f"Processing list of {len(obj_list)} objects")

    if not obj_list:
        logger.warning("Empty list provided to display")
        return None

    # Auto-extract data from SNTObject dictionaries for seamless chaining
    processed_list, source_types = _preprocess_object_list(obj_list)

    # Classify objects by type
    classified = _classify_objects_for_list_display(processed_list)

    # Try to find a single-type handler
    single_type = _get_single_type_handler(classified)
    if single_type:
        type_name, objects, handler = single_type
        logger.info(f"Detected list of {len(objects)} {type_name} objects")

        # Special handling for matplotlib figures to pass source types
        if type_name == 'figure':
            return handler(objects, figure_source_types=source_types, show=show, **kwargs)
        return handler(objects, show=show, **kwargs)

    # Handle mixed lists
    if classified['other']:
        # Has unsupported objects - warn and use priority handler
        supported_count = sum(
            len(classified[t]) for t in ['chart', 'viewer2d', 'imgplus', 'imageplus', 'tree', 'figure'])
        logger.warning(f"Mixed object list detected. Displaying {supported_count} supported objects, "
                       f"ignoring {len(classified['other'])} other objects: {[name for _, name in classified['other']]}")

    priority = _get_priority_handler(classified)
    if priority:
        type_name, objects, handler = priority
        logger.warning(f"Mixed list detected. Displaying {len(objects)} {type_name} objects, ignoring others.")

        if type_name == 'figure':
            return handler(objects, figure_source_types=source_types, show=show, **kwargs)
        return handler(objects, show=show, **kwargs)

    # No supported objects
    logger.warning(f"List contains no supported objects for multi-panel display. "
                   f"Object types: {[type(obj).__name__ for obj in obj_list]}")
    logger.info("Falling back to individual display of first object")
    return display(obj_list[0], **kwargs)


def _preprocess_object_list(obj_list):
    """
    Preprocess object list, extracting data from SNTObject dictionaries.

    Returns
    -------
    tuple
        (processed_list, source_types)
    """
    processed_list = []
    source_types = []

    for i, obj in enumerate(obj_list):
        if isinstance(obj, dict) and 'data' in obj and 'type' in obj:
            source_type = obj.get('metadata', {}).get('source_type', 'Unknown')
            logger.debug(f"Auto-extracting data from SNTObject dictionary at index {i} (source_type: {source_type})")
            processed_list.append(obj['data'])
            source_types.append(source_type)
        else:
            processed_list.append(obj)
            source_types.append('Unknown')

    return processed_list, source_types


# =============================================================================
# Typed List Display Handlers
# =============================================================================

@handle_display_errors("display SNTChart list")
def _display_snt_chart_list(chart_list: list, show: bool = True, **kwargs) -> Any:
    """Display a list of SNTChart objects as a multi-panel matplotlib figure."""
    return _display_typed_list(chart_list, _convert_snt_chart, "SNTChart", show, **kwargs)


@handle_display_errors("display Viewer2D list")
def _display_viewer2d_list(viewer2d_list: list, show: bool = True, **kwargs) -> Any:
    """Display a list of Viewer2D objects as a multi-panel matplotlib figure."""
    return _display_typed_list(viewer2d_list, _convert_viewer2d_to_chart, "Viewer2D", show, **kwargs)


@handle_display_errors("display Tree list")
def _display_tree_list(tree_list: list, show: bool = True, **kwargs) -> Any:
    """Display a list of Tree objects as a multi-panel matplotlib figure."""
    max_panels = kwargs.get('max_panels', 20)
    tree_list = _limit_list_size(tree_list, "Tree", max_panels)

    logger.info(f"Converting {len(tree_list)} Tree objects to 2D skeletons")

    displayable_list = []
    for i, tree in enumerate(tree_list):
        try:
            dis_tree = _tree_to_chart(tree)
            if dis_tree is not None:
                displayable_list.append(dis_tree)
                logger.debug(f"Successfully converted Tree {i + 1} to skeleton: {tree.getLabel()}")
            else:
                logger.warning(f"Tree {i + 1} conversion returned None")
        except Exception as e:
            logger.warning(f"Failed to convert Tree {i + 1} to skeleton: {e}")
            continue

    if not displayable_list:
        logger.error("No Tree objects could be converted to skeletons")
        return None

    logger.info(f"Successfully converted {len(displayable_list)} trees, displaying as multi-panel figure")
    return _display_snt_chart_list(displayable_list, show=show, **kwargs)


@handle_display_errors("display ImgPlus list")
def _display_imgplus_list(imgplus_list: list, show: bool = True, **kwargs) -> Any:
    """Display a list of ImgPlus objects as a multi-panel matplotlib figure."""
    max_panels = kwargs.get('max_panels', 20)
    imgplus_list = _limit_list_size(imgplus_list, "ImgPlus", max_panels)

    logger.info(f"Converting {len(imgplus_list)} ImgPlus objects to ImagePlus for display")

    import scyjava
    ImgUtils = scyjava.jimport("sc.fiji.snt.util.ImgUtils")

    imageplus_list = []
    for i, imgplus in enumerate(imgplus_list):
        try:
            imageplus = ImgUtils.toImagePlus(imgplus)
            if imageplus is not None:
                try:
                    name = imgplus.getName() if hasattr(imgplus, 'getName') else f"ImgPlus {i + 1}"
                    imageplus.setTitle(name)
                except Exception:
                    imageplus.setTitle(f"ImgPlus {i + 1}")

                imageplus_list.append(imageplus)
                logger.debug(f"Successfully converted ImgPlus {i + 1} to ImagePlus")
            else:
                logger.warning(f"ImgUtils.toImagePlus() returned None for ImgPlus {i + 1}")
        except Exception as e:
            logger.warning(f"Failed to convert ImgPlus {i + 1}: {e}")
            continue

    if not imageplus_list:
        logger.error("No ImgPlus objects could be converted to ImagePlus")
        return None

    logger.info(f"Successfully converted {len(imageplus_list)} ImgPlus objects, displaying as ImagePlus list")

    kwargs = _add_metadata(kwargs, source_type='ImgPlus_List', imgplus_conversion=True,
                           original_count=len(imgplus_list))

    return _display_imageplus_list(imageplus_list, show=show, **kwargs)


@handle_display_errors("display matplotlib Figure list")
def _display_matplotlib_figure_list(figure_list: list, figure_source_types: list = None, show: bool = True,
                                    **kwargs) -> Any:
    """Display a list of matplotlib Figure objects as a multi-panel figure."""
    title = kwargs.get('title', None)

    logger.info(f"Creating multi-panel figure from {len(figure_list)} matplotlib Figure objects")

    custom_titles = kwargs.get('panel_titles', None)
    titles = []

    for i, fig in enumerate(figure_list):
        if custom_titles and i < len(custom_titles):
            titles.append(custom_titles[i])
        elif hasattr(fig, '_suptitle') and fig._suptitle:
            titles.append(fig._suptitle.get_text())
        else:
            titles.append(f"Figure {i + 1}")

    from .visual_display import _combine_matplotlib_figures

    if figure_source_types:
        kwargs['figure_source_types'] = figure_source_types

    combined_figure = _combine_matplotlib_figures(figure_list, titles, title or "", **kwargs)

    if combined_figure is None:
        logger.error("Failed to combine matplotlib figures into multi-panel figure")
        return None

    panel_layout = kwargs.get('panel_layout', 'auto')
    metadata = {
        'figure_count': len(figure_list),
        'panel_layout': panel_layout,
        'title': title
    }

    logger.info(f"Successfully created multi-panel figure with {len(figure_list)} matplotlib figures")
    return _create_converter_result(combined_figure, 'matplotlib_figure_list', **metadata)


@handle_display_errors("display ImagePlus list")
def _display_imageplus_list(imageplus_list: list, show: bool = True, **kwargs) -> Any:
    """Display a list of ImagePlus objects as a multi-panel matplotlib figure."""
    max_panels = kwargs.get('max_panels', 20)
    title = kwargs.get('title', None)
    panel_layout = kwargs.get('panel_layout', 'auto')

    imageplus_list = _limit_list_size(imageplus_list, "ImagePlus", max_panels)

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
            logger.warning(f"Failed to convert ImagePlus {i + 1}: {e}")
            continue

    if not xarray_data_list:
        logger.error("No ImagePlus objects could be converted successfully")
        return None

    # Create multi-panel figure
    import matplotlib.pyplot as plt
    from .utils import _create_subplot_grid

    num_panels = len(xarray_data_list)

    aspect_ratios = [(xarray_data.shape[-1] / xarray_data.shape[-2]) for xarray_data, _ in xarray_data_list]
    figsize = kwargs.get('figsize') or _calculate_figure_size(aspect_ratios, panel_layout, num_panels)

    fig, axes, (rows, cols) = _create_subplot_grid(num_panels, panel_layout, figsize)

    logger.debug(f"Created {rows}x{cols} grid for {num_panels} panels")

    # Plot each image
    for i, ((xarray_data, metadata), image_title) in enumerate(zip(xarray_data_list, image_titles)):
        if i < len(axes):
            _plot_image_panel(axes[i], xarray_data, metadata, image_title, **kwargs)

    # Hide unused subplots
    for i in range(num_panels, len(axes)):
        axes[i].set_visible(False)

    _apply_figure_layout(fig, title, **kwargs)

    result_metadata = {
        'imageplus_count': len(imageplus_list),
        'displayed_count': num_panels,
        'panel_layout': (rows, cols),
        'title': title
    }

    logger.info(f"Successfully created multi-panel figure with {num_panels} ImagePlus objects")
    return _create_converter_result(fig, 'ImagePlus_List', **result_metadata)
