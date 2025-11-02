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
