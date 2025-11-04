"""
Display utilities for PySNT.

This module contains shared utilities, helper functions, configuration
parameter extraction, error handling patterns, and type checking utilities
used across the display system.
"""

import logging
from typing import Any, Dict

# Import shared utilities from core
from ..converters.core import (
    _setup_matplotlib_interactive,
    _create_standard_figure,
    DEFAULT_CMAP,
    DEFAULT_NODE_COLOR,
    DEFAULT_NODE_SIZE,
    ERROR_MISSING_NETWORKX,
    _extract_color_attributes,
)

logger = logging.getLogger(__name__)

# Global display handler registry
_DISPLAY_HANDLERS = {}

# Try to import optional dependencies
try:
    import xarray # noqa
    HAS_XARRAY = True
except ImportError:
    HAS_XARRAY = False
    xarray = None

def _get_pandasgui_show():
    """
    Lazy import of pandasgui.show to avoid initialization issues.
    
    Returns
    -------
    callable or None
        pandasgui.show function if available, None otherwise
    """
    try:
        import pandasgui # noqa
        return pandasgui.show
    except ImportError:
        return None


def _has_pandasgui():
    """Check if pandasgui is available using lazy import."""
    return _get_pandasgui_show() is not None


def _is_snt_object(obj: Any) -> bool:
    """Check if object is an SNTObject (TypedDict with required keys)."""
    return (isinstance(obj, dict) and 
            'type' in obj and 'data' in obj and 'metadata' in obj and 'error' in obj)


def _is_snt_tree(obj: Any) -> bool:
    """
    Check if object is an SNT Tree.
    
    This function checks for SNT Tree objects while avoiding false positives
    with ImagePlus objects that might have 'Tree' in their title.
    """
    type_str = str(type(obj))
    
    # Must contain 'Tree' in the type name (specifically SNT Tree classes)
    if not any(pattern in type_str for pattern in ['Tree', 'tree']):
        return False
    
    # Must NOT be an ImagePlus (to avoid false positives)
    #if 'ImagePlus' in type_str:
    #    return False
    
    # Must NOT be a basic Python object
    if type_str.startswith('<class \'__main__.') or type_str.startswith('<class \'builtins.'):
        return False
    
    # Should have tree-like methods (at least one of these)
    tree_methods = ['getSkeleton2D', 'getSkeleton', 'getNodes', 'getPaths']
    has_tree_method = any(hasattr(obj, method) for method in tree_methods)
    
    # Additional check: should be a Java object (SNT trees are Java objects)
    is_java_object = 'java class' in type_str or hasattr(obj, '__class__') and hasattr(obj.__class__, '__name__')
    
    logger.debug(f"Tree detection for {type_str}: has_tree_method={has_tree_method}, is_java_object={is_java_object}")
    
    return has_tree_method and is_java_object


def _is_snt_path(obj: Any) -> bool:
    """Check if object is an SNT Path."""
    return str(type(obj)).find('Path') != -1 and hasattr(obj, 'getNodes')


def _is_xarray_object(obj: Any) -> bool:
    """Check if object is an xarray DataArray or Dataset."""
    if not HAS_XARRAY:
        return False
    return isinstance(obj, (xarray.Dataset, xarray.DataArray))


def _extract_display_config(**kwargs) -> Dict[str, Any]:
    """
    Extract common display configuration parameters with defaults.
    
    This utility consolidates the repeated pattern of extracting configuration
    parameters from kwargs with fallbacks to pysnt configuration options.
    
    Parameters
    ----------
    **kwargs
        Keyword arguments that may contain display configuration
        
    Returns
    -------
    Dict[str, Any]
        Dictionary containing extracted configuration parameters
    """
    from ..config import get_option
    
    config = {}
    
    # Table/DataFrame display options
    if 'table_mode' in kwargs or 'max_rows' in kwargs or 'max_cols' in kwargs or 'precision' in kwargs:
        config.update({
            'table_mode': kwargs.get('table_mode', get_option('display.table_mode')),
            'max_rows': kwargs.get('max_rows', get_option('display.max_rows')),
            'max_cols': kwargs.get('max_cols', get_option('display.max_columns')),
            'precision': kwargs.get('precision', get_option('display.precision')),
        })
    
    # Plotting options
    if 'figsize' in kwargs:
        config['figsize'] = kwargs.get('figsize', get_option('plotting.figure_size'))
    
    # GUI options
    if 'use_gui' in kwargs:
        config['use_gui'] = kwargs.get('use_gui', False)
        config['gui_safe_mode'] = get_option('display.gui_safe_mode')
    
    # Visual options
    config.update({
        'cmap': kwargs.get('cmap', DEFAULT_CMAP),
        'title': kwargs.get('title', None),
    })
    
    return config


def _handle_display_error(error: Exception, operation: str, obj_type: str = "object") -> None:
    """
    Standardized error handling for display operations.
    
    This utility consolidates the repeated pattern of error logging and
    traceback printing used throughout the display system.
    
    Parameters
    ----------
    error : Exception
        The exception that occurred
    operation : str
        Description of the operation that failed (e.g., "SNTTable display")
    obj_type : str, default "object"
        Type of object being displayed for context
    """
    logger.error(f"{operation} failed: {error}")
    
    # Import traceback here to avoid import overhead when not needed
    import traceback
    traceback.print_exc()


def _validate_display_kwargs(**kwargs) -> Dict[str, Any]:
    """
    Validate and normalize display keyword arguments.
    
    Parameters
    ----------
    **kwargs
        Display keyword arguments to validate
        
    Returns
    -------
    Dict[str, Any]
        Validated and normalized keyword arguments
    """
    validated = kwargs.copy()
    
    # Ensure recursion protection exists
    if '_internal' not in validated:
        validated['_internal'] = {}
    
    # Validate figsize if provided
    if 'figsize' in validated:
        figsize = validated['figsize']
        if not (isinstance(figsize, (tuple, list)) and len(figsize) == 2):
            logger.warning(f"Invalid figsize {figsize}, using default")
            validated.pop('figsize')
    
    # Validate boolean options
    bool_options = ['use_gui', 'with_labels', 'add_colorbar', 'case_sensitive']
    for option in bool_options:
        if option in validated and not isinstance(validated[option], bool):
            logger.warning(f"Converting {option} to boolean")
            validated[option] = bool(validated[option])
    
    return validated


def _hide_axis_decorations(ax, hide_axis_completely=False):
    """
    Hide all axis decorations (ticks, labels, spines).

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        The matplotlib axis to clean up
    hide_axis_completely : bool, default False
        If True, calls ax.axis('off') to completely hide the axis including borders.
        If False, only hides individual decorations but keeps axis frame.
        
    Examples
    --------
    >>> fig, ax = plt.subplots()
    >>> ax.imshow(image_data)
    >>> _hide_axis_decorations(ax)  # Clean but keep frame
    >>> _hide_axis_decorations(ax, hide_axis_completely=True)  # Completely clean
    """
    if hide_axis_completely:
        # Completely turn off axis - removes all borders and decorations
        ax.axis('off')
    else:
        # Hide individual decorations but keep axis frame
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_xlabel('')
        ax.set_ylabel('')
        for spine in ax.spines.values():
            spine.set_visible(False)


def _setup_clean_axis(ax, title=None, show_title=True, hide_axis_completely=False):
    """
    Setup axis with clean formatting and optional title.
    
    Parameters
    ----------
    ax : matplotlib.axes.Axes
        The matplotlib axis to setup
    title : str, optional
        Title to set on the axis
    show_title : bool, default True
        Whether to show the title if provided
    hide_axis_completely : bool, default False
        Whether to completely hide the axis (removes borders for combined charts)
        
    Examples
    --------
    >>> fig, ax = plt.subplots()
    >>> ax.imshow(image_data)
    >>> _setup_clean_axis(ax, "My Image", show_title=True)
    >>> _setup_clean_axis(ax, None, show_title=False, hide_axis_completely=True)
    """
    _hide_axis_decorations(ax, hide_axis_completely=hide_axis_completely)
    if show_title and title:
        ax.set_title(title, fontsize=10, pad=5)


def _apply_standard_layout(fig, show_overall_title=False, show_panel_titles=False, 
                          overall_title=None):
    """
    Apply standardized layout with consistent spacing for display figures.
    
    Parameters
    ----------
    fig : matplotlib.figure.Figure
        The figure to apply layout to
    show_overall_title : bool, default False
        Whether an overall title is being displayed
    show_panel_titles : bool, default False
        Whether individual panel titles are being displayed
    overall_title : str, optional
        Overall title text (only used if show_overall_title=True)
        
    Examples
    --------
    >>> fig, axes = plt.subplots(2, 2)
    >>> # ... populate subplots ...
    >>> _apply_standard_layout(fig, show_panel_titles=True)
    """
    # Set overall title if requested
    if show_overall_title and overall_title:
        fig.suptitle(overall_title, fontsize=14, fontweight='normal')
        top_margin = 0.93
    else:
        top_margin = 0.98
    
    # Adjust spacing based on panel titles
    if show_panel_titles:
        # Need more vertical space for panel titles
        hspace = 0.25
    else:
        # Minimal space without panel titles
        hspace = 0.05
    
    # Apply tight layout with appropriate spacing
    import matplotlib.pyplot as plt
    plt.subplots_adjust(left=0.02, right=0.98, top=top_margin, bottom=0.02, 
                       hspace=hspace, wspace=0.05)


def _create_subplot_grid(num_panels, panel_layout='auto', figsize=None, source_figures=None):
    """
    Create standardized subplot grid with aspect ratio preservation.
    
    Parameters
    ----------
    num_panels : int
        Number of panels/subplots needed
    panel_layout : str or tuple, default 'auto'
        Layout specification:
        - 'auto': Calculate optimal grid layout
        - 'horizontal': Single row
        - 'vertical': Single column  
        - (rows, cols): Explicit grid dimensions
    figsize : tuple, optional
        Figure size (width, height). If None, auto-calculated.
    source_figures : list, optional
        List of source figures to analyze for aspect ratio preservation
        
    Returns
    -------
    tuple
        (fig, axes, (rows, cols)) where:
        - fig: matplotlib Figure
        - axes: list of Axes (always flattened for consistency)
        - (rows, cols): actual grid dimensions used
        
    Examples
    --------
    >>> fig, axes, (rows, cols) = _create_subplot_grid(4, 'auto')
    >>> for i, ax in enumerate(axes[:4]):
    ...     ax.plot(data[i])
    ...     _setup_clean_axis(ax, f"Panel {i+1}")
    """
    import math
    import matplotlib.pyplot as plt
    
    # Determine subplot layout
    if isinstance(panel_layout, tuple) and len(panel_layout) == 2:
        rows, cols = panel_layout
    elif panel_layout == 'horizontal':
        rows, cols = 1, num_panels
    elif panel_layout == 'vertical':
        rows, cols = num_panels, 1
    else:  # 'auto'
        # Calculate optimal grid layout
        cols = math.ceil(math.sqrt(num_panels))
        rows = math.ceil(num_panels / cols)
    
    # Calculate figure size with aspect ratio consideration
    if figsize is None:
        # Analyze source figures for aspect ratios if provided
        if source_figures:
            aspect_ratios = []
            for fig in source_figures:
                try:
                    fig_width, fig_height = fig.get_size_inches()
                    aspect_ratios.append(fig_width / fig_height)
                except Exception:
                    aspect_ratios.append(4/3)  # Default fallback
            
            # Use average aspect ratio, but constrain to reasonable bounds
            avg_aspect = sum(aspect_ratios) / len(aspect_ratios)
            avg_aspect = max(0.5, min(2.0, avg_aspect))  # Constrain between 0.5 and 2.0
            
            # Calculate panel size based on average aspect ratio
            panel_height = 3.5  # Base height
            panel_width = panel_height * avg_aspect
        else:
            # Default sizing for unknown content
            panel_width = 4
            panel_height = 3
        
        figsize = (panel_width * cols, panel_height * rows)
    
    # Create figure with tight spacing
    fig, axes = plt.subplots(rows, cols, figsize=figsize, 
                            gridspec_kw={'hspace': 0.1, 'wspace': 0.1})
    
    # Always return axes as a flat list for consistent handling
    if num_panels == 1:
        axes = [axes]
    elif rows == 1 or cols == 1:
        axes = axes.flatten() if hasattr(axes, 'flatten') else [axes]
    else:
        axes = axes.flatten()
    
    return fig, axes, (rows, cols)


# Note: _setup_matplotlib_interactive is imported from converters.core
# and used directly in display functions. No need for additional wrapper.


def register_display_handler(obj_type: str, handler_func):
    """
    Register a custom display handler for a specific SNT object type.
    
    This function allows users to register custom display handlers for specific
    SNT object types. When an object of the registered type is displayed,
    the custom handler will be called instead of the default display logic.
    
    Parameters
    ----------
    obj_type : str
        The SNT object type identifier (e.g., 'SNT_Tree', 'SNT_Path')
    handler_func : Callable[[Dict[str, Any]], None]
        Function that takes an SNTObject dictionary and displays it
        
    Examples
    --------
    >>> def display_my_object(snt_dict):
    ...     print(f"My object: {snt_dict.get('name')}")
    >>> 
    >>> register_display_handler('SNT_MyObject', display_my_object)
    """
    _DISPLAY_HANDLERS[obj_type] = handler_func
