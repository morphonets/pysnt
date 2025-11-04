"""
Core utilities and base classes for the converters module.

This module provides the foundation layer for all converter functionality,
including constants, factory functions, helper utilities, and base classes.
It has no internal dependencies and only imports external libraries.
"""

import logging
import os
import tempfile
from contextlib import contextmanager
from typing import Any, Dict, List, Optional, TypedDict, Type


try:
    import cairosvg  # noqa

    HAS_CAIROSVG = True
except ImportError:
    HAS_CAIROSVG = False
    cairosvg = None

try:
    import fitz  # noqa

    HAS_FITZ = True
except ImportError:
    HAS_FITZ = False
    fitz = None

try:
    import pandas as pd  # noqa

    HAS_PANDAS = True
except ImportError:
    HAS_PANDAS = False
    pd = None

# Lazy import for pandasgui to avoid initialization issues in PyCharm console
HAS_PANDASGUI = None  # Will be determined on first use
_pandasgui_show = None  # Cached import


def _get_pandasgui_show():
    """
    Lazy import of pandasgui.show to avoid initialization issues.
    
    Returns
    -------
    callable or None
        The pandasgui.show function if available, None otherwise
    """
    global HAS_PANDASGUI, _pandasgui_show
    
    if HAS_PANDASGUI is None:  # First time check
        try:
            from pandasgui import show as pandasgui_show
            HAS_PANDASGUI = True
            _pandasgui_show = pandasgui_show
        except (ImportError, AttributeError):
            # AttributeError can occur in PyCharm console where IPython magic methods aren't available
            HAS_PANDASGUI = False
            _pandasgui_show = None
    
    return _pandasgui_show


def has_pandasgui():
    """
    Check if pandasgui is available without triggering import.
    
    Returns
    -------
    bool
        True if pandasgui is available, False otherwise
    """
    return _get_pandasgui_show() is not None

try:
    import networkx as nx  # noqa

    HAS_NETWORKX = True
except ImportError:
    HAS_NETWORKX = False
    nx = None


logger = logging.getLogger(__name__)

# Constants for common default values
DEFAULT_CMAP = "gray_r"
DEFAULT_NODE_SIZE = 300
DEFAULT_NODE_COLOR = "lightblue"
DEFAULT_DPI = 300
DEFAULT_FIGSIZE = None
DEFAULT_SCALE = 1.0
DEFAULT_MAX_PANELS = 6
DEFAULT_PANEL_LAYOUT = "auto"

# Common parameter names for frame/time extraction
FRAME_PARAM_NAMES = ["frame", "t", "time", "timepoint"]

# Common error messages
ERROR_MISSING_NETWORKX = (
    "NetworkX is required for graph operations. Install with: pip install networkx"
)
ERROR_MISSING_PANDAS = (
    "pandas is required for table operations. Install with: pip install pandas"
)
ERROR_MISSING_CAIROSVG = (
    "cairosvg is required for SVG conversion. Install with: pip install cairosvg"
)
ERROR_MISSING_FITZ = (
    "PyMuPDF is required for PDF conversion. Install with: pip install PyMuPDF"
)

# Internal parameter names to exclude from matplotlib kwargs
INTERNAL_PARAMS = {"_internal", "cmap", "title", "add_colorbar", "metadata", "is_rgb"}


class SNTObject(TypedDict):
    """A structured container for SNT converted objects.

    This TypedDict defines the structure for python converted objects that
    encapsulate converted data along with its type information, metadata,
    and potential convertion error state.

    Attributes:
        type: The Python type of the data being stored.
        data: The actual converted data.
        metadata: A dictionary containing additional information about the
            converted object (e.g., source identifiers or processing flags).
        error: An exception object if an error occurred during object convertion
            (which typically means data is None), None otherwise.
    """

    type: Type
    data: Any
    metadata: Dict[str, Any]
    error: Optional[Exception]


def _create_snt_object(
    data_type: Type,
    data: Any = None,
    metadata: Optional[Dict[str, Any]] = None,
    error: Optional[Exception] = None,
) -> SNTObject:
    """
    Factory function for creating standardized SNTObject dictionaries.

    Parameters
    ----------
    data_type : Type
        The type of the data being stored
    data : Any, optional
        The actual data object
    metadata : dict, optional
        Metadata dictionary
    error : Exception, optional
        Error that occurred during conversion

    Returns
    -------
    SNTObject
        Standardized SNTObject dictionary
    """
    if metadata is None:
        metadata = {}
    result: SNTObject = {
        "type": data_type,
        "data": data,
        "metadata": metadata,
        "error": error,
    }
    # noinspection PyTypeChecker
    return result


def _create_converter_result(
    data: Any, source_type: str, **metadata_kwargs
) -> "SNTObject":
    """
    Create standardized converter result with common metadata.

    Parameters
    ----------
    data : Any
        The converted data object
    source_type : str
        Type of the source object (e.g., 'ImagePlus', 'SNTGraph')
    **metadata_kwargs
        Additional metadata fields

    Returns
    -------
    SNTObject
        Standardized converter result
    """
    metadata = {"source_type": source_type, **metadata_kwargs}

    return _create_snt_object(data_type=type(data), data=data, metadata=metadata)


def _create_error_result(
    data_type: Type, error: Exception, source_type: str = None
) -> "SNTObject":
    """
    Create standardized error result for failed conversions.

    Parameters
    ----------
    data_type : Type
        The expected type of the data
    error : Exception
        The error that occurred
    source_type : str, optional
        Type of the source object

    Returns
    -------
    SNTObject
        Standardized error result
    """
    metadata = {}
    if source_type:
        metadata["source_type"] = source_type

    return _create_snt_object(
        data_type=data_type, data=None, metadata=metadata, error=error
    )


def _extract_frame_parameter(kwargs: Dict[str, Any]) -> int:
    """
    Extract frame parameter from kwargs with standard logic.

    Parameters
    ----------
    kwargs : dict
        Keyword arguments that may contain frame parameters

    Returns
    -------
    int
        Frame number (default: 1)
    """
    kwargs_lower = {k.lower(): v for k, v in kwargs.items()}
    for key in FRAME_PARAM_NAMES:
        if key in kwargs_lower:
            try:
                return int(kwargs_lower[key])
            except (ValueError, TypeError):
                continue
    return 1


def _filter_matplotlib_kwargs(
    kwargs: Dict[str, Any], additional_exclude: Optional[List[str]] = None
) -> Dict[str, Any]:
    """
    Filter kwargs for matplotlib functions, excluding internal parameters.

    Parameters
    ----------
    kwargs : dict
        Original keyword arguments
    additional_exclude : list, optional
        Additional parameter names to exclude

    Returns
    -------
    dict
        Filtered kwargs suitable for matplotlib functions
    """
    exclude_params = INTERNAL_PARAMS.copy()
    if additional_exclude:
        exclude_params.update(additional_exclude)

    return {k: v for k, v in kwargs.items() if k not in exclude_params}


def _create_standard_error_message(
    operation: str, error: Exception, obj_type: str = None
) -> str:
    """
    Create standardized error message format.

    Parameters
    ----------
    operation : str
        The operation that failed
    error : Exception
        The exception that occurred
    obj_type : str, optional
        Type of object being processed

    Returns
    -------
    str
        Formatted error message
    """
    if obj_type:
        return f"Failed to {operation} {obj_type}: {error}"
    return f"Failed to {operation}: {error}"


def _setup_matplotlib_interactive():
    """
    Centralized matplotlib interactive mode setup.

    Returns
    -------
    matplotlib.pyplot
        The pyplot module with interactive mode configured
    """
    from ..config import get_option
    import matplotlib.pyplot as plt

    if get_option("pyplot.ion") and not plt.isinteractive():
        plt.ion()
    return plt


@contextmanager
def _matplotlib_context(figsize=None, dpi=None, **kwargs):
    """
    Context manager for matplotlib setup with automatic cleanup.

    Parameters
    ----------
    figsize : tuple, optional
        Figure size (width, height) in inches
    dpi : int, optional
        Figure DPI
    **kwargs
        Additional matplotlib configuration

    Yields
    ------
    matplotlib.pyplot
        Configured pyplot module
    """
    plt = _setup_matplotlib_interactive()

    # Store original settings
    original_settings = {}
    if dpi is not None:
        original_settings["figure.dpi"] = plt.rcParams.get("figure.dpi")
        plt.rcParams["figure.dpi"] = dpi
    if figsize is not None:
        original_settings["figure.figsize"] = plt.rcParams.get("figure.figsize")
        plt.rcParams["figure.figsize"] = figsize

    # Apply additional matplotlib configuration from kwargs
    for key, value in kwargs.items():
        if key in plt.rcParams:
            original_settings[key] = plt.rcParams.get(key)
            plt.rcParams[key] = value

    try:
        yield plt
    finally:
        # Restore original settings
        for key, value in original_settings.items():
            plt.rcParams[key] = value


def _create_standard_figure(
    data=None,
    title=None,
    figsize=None,
    dpi=None,
    cmap=None,
    add_colorbar=True,
    is_rgb=False,
    **kwargs,
):
    """
    Create a standardized matplotlib figure with common patterns.

    Parameters
    ----------
    data : array-like, optional
        Image data to display
    title : str, optional
        Figure title
    figsize : tuple, optional
        Figure size (width, height) in inches
    dpi : int, optional
        Figure DPI
    cmap : str, optional
        Colormap name (ignored for RGB images)
    add_colorbar : bool, default True
        Whether to add a colorbar (ignored for RGB images)
    is_rgb : bool, default False
        Whether the data is RGB/RGBA
    **kwargs
        Additional arguments for imshow

    Returns
    -------
    tuple
        (figure, axes, image) where image is None if no data provided
    """
    with _matplotlib_context(figsize=figsize, dpi=dpi) as plt:
        fig, ax = plt.subplots(figsize=figsize)

        if title:
            ax.set_title(title)

        im = None
        if data is not None:
            # Set colormap based on image type
            if is_rgb:
                cmap = None  # No colormap for RGB images
            else:
                cmap = cmap or DEFAULT_CMAP

            # Filter kwargs for imshow
            imshow_kwargs = _filter_matplotlib_kwargs(
                kwargs, ["figsize", "dpi", "add_colorbar", "is_rgb"]
            )

            im = ax.imshow(data, cmap=cmap, **imshow_kwargs)

            # Add colorbar only for non-RGB images
            if add_colorbar and not is_rgb and cmap is not None:
                plt.colorbar(im, ax=ax)

        return fig, ax, im


@contextmanager
def _temp_file(format_type, temp_dir=None, cleanup=True):
    """
    Context manager for temporary files with guaranteed cleanup.

    Parameters
    ----------
    format_type : str
        File format extension (e.g., 'svg', 'pdf', 'png')
    temp_dir : str, optional
        Directory for temporary files
    cleanup : bool, default True
        Whether to clean up the file on exit

    Yields
    ------
    str
        Path to the temporary file
    """
    with tempfile.NamedTemporaryFile(
        suffix=f".{format_type}", delete=False, dir=temp_dir
    ) as temp_file:
        temp_path = temp_file.name

    try:
        yield temp_path
    finally:
        if cleanup and os.path.exists(temp_path):
            try:
                os.unlink(temp_path)
                logger.debug(f"Cleaned up temporary file: {temp_path}")
            except OSError as e:
                logger.debug(f"Could not clean up temporary file {temp_path}: {e}")


@contextmanager
def _temp_directory(temp_dir=None, cleanup=True):
    """
    Context manager for temporary chart directories with guaranteed cleanup.

    Parameters
    ----------
    temp_dir : str, optional
        Parent directory for temporary directory
    cleanup : bool, default True
        Whether to clean up the directory on exit

    Yields
    ------
    str
        Path to the temporary directory
    """
    temp_chart_dir = tempfile.mkdtemp(dir=temp_dir)

    try:
        yield temp_chart_dir
    finally:
        if cleanup:
            try:
                import shutil

                shutil.rmtree(temp_chart_dir, ignore_errors=True)
                logger.debug(f"Cleaned up temporary directory: {temp_chart_dir}")
            except Exception as e:
                logger.debug(
                    f"Could not clean up temporary directory {temp_chart_dir}: {e}"
                )


def _get_java_class_name(obj: Any) -> str:
    """Get the Java class name of an object safely."""
    try:
        # Try multiple ways to get the class name
        if hasattr(obj, "getClass"):
            java_class = obj.getClass()
            if hasattr(java_class, "getName"):
                return java_class.getName()
            elif hasattr(java_class, "getSimpleName"):
                return java_class.getSimpleName()

        # Fallback to Python type string
        type_str = str(type(obj))
        if "java class" in type_str:
            # Extract class name from string like "<java class 'sc.fiji.snt.analysis.SNTTable'>"
            start = type_str.find("'") + 1
            end = type_str.rfind("'")
            if 0 < start < end:
                return type_str[start:end]

        return type_str
    except (AttributeError, TypeError, RuntimeError):
        return str(type(obj))


class JavaTypeDetector:
    """Centralized Java type detection utilities."""

    @staticmethod
    def has_class_name(obj: Any, *names: str) -> bool:
        """Check if object's class name contains any of the given strings."""
        class_name = _get_java_class_name(obj)
        return any(name in class_name for name in names)

    @staticmethod
    def has_methods(obj: Any, *method_names: str) -> bool:
        """Check if object has all specified methods."""
        return all(hasattr(obj, method) for method in method_names)

    @staticmethod
    def matches_pattern(
        obj: Any, class_patterns: List[str], required_methods: List[str]
    ) -> bool:
        """Check if object matches class name pattern AND has required methods."""
        if not JavaTypeDetector.has_class_name(obj, *class_patterns):
            return False
        return JavaTypeDetector.has_methods(obj, *required_methods)


def _extract_color_attributes(color_obj: Any, prefix: str = "color") -> Dict[str, Any]:
    """
    Color extraction with configurable prefix.

    Parameters
    ----------
    color_obj : java.awt.Color
        The Color object to extract attributes from
    prefix : str, default "color"
        Prefix for the attribute keys

    Returns
    -------
    dict
        Dictionary containing '{prefix}_rgb' tuple, '{prefix}_hex' string,
        and '{prefix}' original object, or empty dict if extraction fails
    """
    attrs = {}
    try:
        if (
            color_obj is not None
            and hasattr(color_obj, "getRed")
            and hasattr(color_obj, "getGreen")
            and hasattr(color_obj, "getBlue")
        ):
            r = int(color_obj.getRed())
            g = int(color_obj.getGreen())
            b = int(color_obj.getBlue())
            attrs[f"{prefix}_rgb"] = (r, g, b)
            attrs[f"{prefix}_hex"] = f"#{r:02x}{g:02x}{b:02x}"
            attrs[prefix] = color_obj  # Store original object
    except Exception as e:
        logger.debug(f"Could not extract {prefix} attributes: {e}")

    return attrs
