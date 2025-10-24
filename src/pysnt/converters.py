"""
SNT object converters for PySNT.

This module provides custom converters that transform SNT Java objects into 
Python equivalents (matplotlib figures, xarray datasets, etc.) and handles
their display and visualization.
"""

import logging
import os
import tempfile
from io import BytesIO
from typing import Any, Callable, Dict, List, Optional, TypedDict, Type

import numpy
import pandas
import xarray

try:
    import cairosvg

    HAS_CAIROSVG = True
except ImportError:
    HAS_CAIROSVG = False
    cairosvg = None

try:
    import fitz

    HAS_FITZ = True
except ImportError:
    HAS_FITZ = False
    fitz = None

try:
    import pandas as pd

    HAS_PANDAS = True
except ImportError:
    HAS_PANDAS = False
    pd = None

try:
    from pandasgui import show as pandasgui_show

    HAS_PANDASGUI = True
except ImportError:
    HAS_PANDASGUI = False
    pandasgui_show = None

import matplotlib.image as mpimg
import numpy as np
import scyjava as sj
from matplotlib.figure import Figure

logger = logging.getLogger(__name__)


class SNTObject(TypedDict):
    """A structured container for SNT converted objects.

    This TypedDict defines the structure for python converted objects that
    encapsulate converted data along with its type information, metadata,
    and potential convertion error state.

    Attributes:
        type: The Python type of the data being stored.
        data: The actual converted data.
        metadata: A dictionary containing additional information about the
            converted object (e.g., source identifiers, or processing flags).
        error: An exception object if an error occurred during object convertion,
            None otherwise.
    """
    type: Type
    data: Any
    metadata: Dict[str, Any]
    error: Optional[Exception]


def _get_java_class_name(obj: Any) -> str:
    """Get the Java class name of an object safely."""
    try:
        # Try multiple ways to get the class name
        if hasattr(obj, 'getClass'):
            java_class = obj.getClass()
            if hasattr(java_class, 'getName'):
                return java_class.getName()
            elif hasattr(java_class, 'getSimpleName'):
                return java_class.getSimpleName()

        # Fallback to Python type string
        type_str = str(type(obj))
        if 'java class' in type_str:
            # Extract class name from string like "<java class 'sc.fiji.snt.analysis.SNTTable'>"
            start = type_str.find("'") + 1
            end = type_str.rfind("'")
            if 0 < start < end:
                return type_str[start:end]

        return type_str
    except Exception:
        return str(type(obj))


# SNT Object Converters
def _is_snt_object(obj) -> bool:
    """Check if object is a valid SNTObject."""
    obj_type, _ = _get_display_handler(obj)
    return obj_type == 'snt_object'


def _is_tree_object(obj) -> bool:
    """Check if object is an SNT Tree."""
    try:
        return hasattr(obj, 'getRoot') and hasattr(obj, 'getNodes') and hasattr(obj, 'setRadii')
    except (AttributeError, TypeError, RuntimeError):
        return False

def _is_path_object(obj) -> bool:
    """Check if object is an SNT Path."""
    try:
        return hasattr(obj, 'findJunctions') and hasattr(obj, 'getCanvasOffset') and hasattr(obj, 'getFitted')
    except (AttributeError, TypeError, RuntimeError):
        return False


def _is_snt_chart_object(obj) -> bool:
    """Check if object is an SNT Chart."""
    try:
        # Check if it's a Java object with show() method and looks like a chart
        return (
                hasattr(obj, 'show') and
                hasattr(obj, 'save') and
                (hasattr(obj, 'getChart') or hasattr(obj, 'getFrame'))
        )
    except (AttributeError, TypeError, RuntimeError):
        return False


def _is_gui_object(obj) -> bool:
    """Check if object is a Java GUI object (typically a Swing/AWT class) that should
    have enhanced setVisible() method."""
    try:
        # Check if it's a Java object with setVisible() method
        return (
                hasattr(obj, 'setVisible') and
                (hasattr(obj, 'getFrame') or hasattr(obj, 'show') or
                 hasattr(obj, 'pack') or hasattr(obj, 'setTitle') or
                 str(type(obj)).find('UI') != -1 or str(type(obj)).find('Frame') != -1 or
                 str(type(obj)).find('Dialog') != -1 or str(type(obj)).find('Window') != -1)
        )
    except (AttributeError, TypeError, RuntimeError):
        return False


def _is_xarray_object(obj) -> bool:
    """Check if object is an xarray DataArray or Dataset."""
    obj_type, _ = _get_display_handler(obj)
    return obj_type == 'xarray'

def _is_snt_chart(obj: Any) -> bool:
    """Check if object is an SNT Chart."""
    try:
        # Check for SNTChart methods
        return hasattr(obj, 'show') and hasattr(obj, 'save') and (hasattr(obj, 'getChart') or hasattr(obj, 'getFrame'))
    except (AttributeError, TypeError, RuntimeError):  # java errors can cause RuntimeError, etc.
        return False


def _is_snt_table(obj: Any) -> bool:
    """Check if object is an SNT Table."""
    try:
        # First check: Must be specifically an SNTTable class
        #  We must be specific to avoid catching generic collections
        obj_class_name = _get_java_class_name(obj)
        logger.debug(f"SNTTable predicate: Checking class '{obj_class_name}'")

        # Must contain 'SNTTable' in the class name (handles full package names)
        if 'SNTTable' not in obj_class_name:
            logger.debug(f"SNTTable predicate: REJECT - class name doesn't contain 'SNTTable'")
            return False

        # Second check: Must have SNTTable-specific methods
        # SNTTable has these methods that distinguish it from generic collections
        snt_table_methods = [
            'getColumnCount',  # Table dimension method
            'getRowCount',  # Table dimension method
            'getColumnHeader',  # SNTTable-specific header method
        ]
        has_all_methods = all(hasattr(obj, method) for method in snt_table_methods)
        if not has_all_methods:
            return False

        logger.debug(f"SNTTable predicate: MATCH for {obj_class_name}")
        return True

    except (AttributeError, TypeError, RuntimeError) as e:
        logger.debug(f"SNTTable predicate: FAILED for {type(obj)} - {e}")
        return False


def _convert_snt_chart(chart: Any, **kwargs) -> SNTObject:
    """
    Convert SNTChart to SNTObject containing a matplotlib figure.
    
    This converter handles both single charts and combined charts (multipanel).
    The converter works by exporting the SNTChart (typically a vector-based format),
    and importing it as a matplotlib figure.

    Parameters
    ----------
    chart : SNT Chart
        The chart object to convert
    **kwargs
        Additional conversion options:
        - format: 'svg', 'pdf', or 'png' (default: uses pysnt.get_option('display.chart_format'))
        - temp_dir: directory for temporary files (default: system temp)
        - scale: scaling factor (default: 1.0)
        - max_panels: maximum number of panels to detect when handling combined (multi-panel) charts (default: 20)
        - panel_layout: 'auto', 'horizontal', 'vertical', or tuple (rows, cols) (default: 'auto')

    Returns
    -------
    dict
        Dictionary (SNTObject TypedDict) containing chart information and matplotlib figure
    """
    from .config import get_option

    # Create result SNTObject dictionary
    result: SNTObject = {
        'type': Figure,
        'data': None,
        'metadata': {},
        'error': None
    }

    try:
        # Get conversion options with config defaults
        format_type = kwargs.get('format', get_option('display.chart_format')).lower()
        temp_dir = kwargs.get('temp_dir', None)
        scale = kwargs.get('scale', 1.0)
        max_panels = kwargs.get('max_panels', 20)
        panel_layout = kwargs.get('panel_layout', 'auto')

        # Check if this is a combined chart
        is_combined = chart.isCombined()
        logger.debug(f"Chart isCombined: {is_combined}")

        if is_combined:
            # Handle combined chart with multiple panels
            logger.info(f"Processing combined chart")
            result['data'] = _convert_combined_snt_chart(chart, format_type, temp_dir, scale, max_panels, panel_layout)

        else:
            # Handle single chart or forced single processing
            result['data'] = _convert_single_snt_chart(chart, format_type, temp_dir, scale)

        # Get chart metadata if available
        try:
            result['metadata']['format'] = format_type
            result['metadata']['scale'] = scale
            result['metadata']['is_combined'] = is_combined
            result['metadata']['title'] = chart.getTitle()
            if hasattr(chart, 'containsValidData'):
                result['metadata']['containsValidData'] = chart.containsValidData()
            if hasattr(chart, 'isLegendVisible'):
                result['metadata']['isLegendVisible'] = chart.isLegendVisible()
        except Exception as e:
            logger.debug(f"Could not extract chart metadata: {e}")

        if result['data'] is not None:
            logger.info(
                f"Successfully converted SNTChart ({'combined' if is_combined else 'single'}) to matplotlib figure")
        else:
            raise ValueError("Chart conversion produced no data")

        return result # type: ignore

    except Exception as e:
        logger.error(f"Failed to convert SNTChart: {e}")
        result['error'] = e
        return result # type: ignore


def _convert_path_to_xarray(path: Any):
    """Convert SNT Path object to xarray Dataset."""
    import xarray as xr
    import numpy as np

    # Collect all coordinates at once
    coords = [(node.x, node.y, node.z) for node in path.getNodes()]
    coords_array = np.array(coords)

    # Create xarray Dataset
    ds = xr.Dataset(
        {
            "x": (["node"], coords_array[:, 0]),
            "y": (["node"], coords_array[:, 1]),
            "z": (["node"], coords_array[:, 2]),
        },
        coords={"node": np.arange(len(coords))},
    )
    return ds


def _convert_single_snt_chart(chart: Any, format_type: str, temp_dir: str, scale: float) -> Figure:
    """
    Convert a single SNTChart to matplotlib figure.
    
    Parameters
    ----------
    chart : SNT Chart
        The chart object to convert
    format_type : str
        File format ('svg', 'pdf', 'png')
    temp_dir : str
        Temporary directory path
    scale : float
        Scaling factor
        
    Returns
    -------
    matplotlib.figure.Figure
        The converted matplotlib figure
    """
    # Create temporary file
    with tempfile.NamedTemporaryFile(
            suffix=f'.{format_type}',
            delete=False,
            dir=temp_dir
    ) as temp_file:
        temp_path = temp_file.name

    try:
        # Save chart using appropriate method
        if format_type == 'svg':
            chart.saveAsSVG(temp_path, scale)
        elif format_type == 'pdf':
            chart.saveAsPDF(temp_path, scale)
        else:  # PNG format
            chart.saveAsPNG(temp_path, scale)

        # Verify file was created and has content
        if not os.path.exists(temp_path):
            raise FileNotFoundError(f"Chart file was not created: {temp_path}")
        
        file_size = os.path.getsize(temp_path)
        if file_size == 0:
            raise ValueError(f"Chart file is empty: {temp_path} (size: {file_size} bytes)")
        
        logger.debug(f"Chart file created successfully: {temp_path} (size: {file_size} bytes)")

        # Convert to matplotlib figure
        if format_type == 'svg':
            fig = _svg_to_matplotlib(svg_file=temp_path, dpi=300, figsize=None, background='None')
        elif format_type == 'pdf':
            fig = _pdf_to_matplotlib(pdf_file=temp_path, dpi=300, figsize=None)
        else:  # PNG
            fig = _png_to_matplotlib(png_file=temp_path, figsize=None)

        return fig

    finally:
        # Clean up temp file
        try:
            if os.path.exists(temp_path):
                os.unlink(temp_path)
        except OSError:
            pass


def _convert_combined_snt_chart(chart: Any, format_type: str, temp_dir: str, scale: float, max_panels: int,
                                panel_layout: str) -> Figure:
    """
    Convert a combined (multipanel) SNTChart to matplotlib figure.
    
    Combined charts save multiple files (one per panel). This function detects
    all panel files and assembles them into a single matplotlib figure with subplots.
    
    Parameters
    ----------
    chart : SNT Chart
        The combined chart object to convert
    format_type : str
        File format ('svg', 'pdf', 'png')
    temp_dir : str
        Temporary directory path
    scale : float
        Scaling factor
    max_panels : int
        Maximum number of panels to detect
    panel_layout : str or tuple
        Layout for panels ('auto', 'horizontal', 'vertical', or (rows, cols))
        
    Returns
    -------
    matplotlib.figure.Figure
        The assembled multipanel matplotlib figure
    """
    import matplotlib.pyplot as plt
    import glob
    import os
    
    # Ensure matplotlib is in interactive mode based on configuration
    from .config import get_option
    if get_option('pyplot.ion') and not plt.isinteractive():
        plt.ion()

    # Create temporary directory for panel files
    temp_chart_dir = tempfile.mkdtemp(dir=temp_dir)
    base_name = "combined_chart"
    temp_path = os.path.join(temp_chart_dir, f"{base_name}.{format_type}")
    logger.debug(f"Created temp directory: {temp_chart_dir}")
    logger.debug(f"Base temp path: {temp_path}")

    panel_files = []

    try:
        # Save combined chart - this will create multiple files
        if format_type == 'svg':
            chart.saveAsSVG(temp_path, scale)
        elif format_type == 'pdf':
            chart.saveAsPDF(temp_path, scale)
        else:  # PNG format
            chart.saveAsPNG(temp_path, scale)

        logger.debug(f"Chart saved to: {temp_path}")

        # List all files in the temp directory to see what was created
        try:
            contents = os.listdir(temp_chart_dir)
            logger.debug(f"Files created in temp directory: {len(contents)}")
            for content in contents:
                full_path = os.path.join(temp_chart_dir, content)
                logger.debug(
                    f"  - {content} (size: {os.path.getsize(full_path) if os.path.exists(full_path) else 'N/A'})")
        except Exception as e:
            logger.debug(f"Could not list temp directory contents: {e}")

        # Detect panel files created by the save operation
        # First, try to find all files with the format extension
        all_files = glob.glob(os.path.join(temp_chart_dir, f"*.{format_type}"))
        logger.debug(f"All {format_type} files found: {all_files}")

        # Try specific patterns
        patterns = [
            f"{base_name}-*.{format_type}",  # combined_chart-1.png, combined_chart-2.png, used by SNT
            # f"{base_name}_*.{format_type}",    # combined_chart_1.png, combined_chart_2.png
            # f"{base_name}*.{format_type}",     # combined_chart1.png, combined_chart2.png
        ]

        logger.debug(f"Searching for panel files with base_name='{base_name}', format='{format_type}'")

        for i, pattern in enumerate(patterns):
            full_pattern = os.path.join(temp_chart_dir, pattern)
            found_files = glob.glob(full_pattern)
            logger.debug(f"Pattern {i + 1}: '{pattern}' -> full: '{full_pattern}' -> found: {found_files}")
            if found_files:
                panel_files.extend(found_files)
                logger.info(f"Successfully found {len(found_files)} files with pattern '{pattern}'")
                break

        # If no patterns worked, try to use all files in directory as fallback
        if not panel_files and all_files:
            logger.warning(f"No patterns matched, using all {format_type} files as fallback: {all_files}")
            panel_files = all_files

        # Remove duplicates and sort
        panel_files = sorted(list(set(panel_files)))

        # Limit to max_panels
        if len(panel_files) > max_panels:
            logger.warning(f"Found {len(panel_files)} panel files, limiting to {max_panels}")
            panel_files = panel_files[:max_panels]

        if not panel_files:
            # Fallback: check if the original file exists (might be single file after all)
            if os.path.exists(temp_path):
                logger.debug(f"Using original file as single panel: {temp_path}")
                panel_files = [temp_path]
            else:
                # List all files in directory for debugging
                try:
                    all_files_debug = os.listdir(temp_chart_dir)
                    logger.error(f"No panel files found. Directory contents: {all_files_debug}")
                except Exception as e:
                    logger.error(f"Could not list directory for debugging: {e}")
                raise FileNotFoundError(f"No panel files found for combined chart in {temp_chart_dir}")

        logger.info(f"Found {len(panel_files)} panel files for combined chart")

        # Determine subplot layout
        num_panels = len(panel_files)
        if isinstance(panel_layout, tuple) and len(panel_layout) == 2:
            rows, cols = panel_layout
        elif panel_layout == 'horizontal':
            rows, cols = 1, num_panels
        elif panel_layout == 'vertical':
            rows, cols = num_panels, 1
        else:  # 'auto'
            # Calculate optimal grid layout
            import math
            cols = math.ceil(math.sqrt(num_panels))
            rows = math.ceil(num_panels / cols)

        # Create matplotlib figure with subplots
        fig, axes = plt.subplots(rows, cols, figsize=(4 * cols, 3 * rows))

        # Handle single subplot case
        if num_panels == 1:
            axes = [axes]
        elif rows == 1 or cols == 1:
            axes = axes.flatten() if hasattr(axes, 'flatten') else [axes]
        else:
            axes = axes.flatten()

        # Load and display each panel
        for i, panel_file in enumerate(panel_files):
            if i >= len(axes):
                break

            ax = axes[i]

            try:
                # Load panel image based on format
                if format_type == 'svg':
                    panel_fig = _svg_to_matplotlib(svg_file=panel_file, dpi=150, figsize=None, background='None')
                elif format_type == 'pdf':
                    panel_fig = _pdf_to_matplotlib(pdf_file=panel_file, dpi=150, figsize=None)
                else:  # PNG
                    panel_fig = _png_to_matplotlib(png_file=panel_file, figsize=None)

                # Extract image data from panel figure
                if panel_fig and len(panel_fig.axes) > 0:
                    panel_ax = panel_fig.axes[0]

                    # Copy the panel content to our subplot
                    for child in panel_ax.get_children():
                        if hasattr(child, 'get_array'):  # Image data
                            try:
                                ax.imshow(child.get_array(), aspect='auto')
                                ax.set_xticks([])
                                ax.set_yticks([])
                            except Exception as e:
                                logger.debug(f"Could not copy image data from panel {i}: {e}")

                    # Copy title if available
                    panel_title = panel_ax.get_title()
                    if panel_title:
                        ax.set_title(f"Panel {i + 1}: {panel_title}")

                    # Close the temporary panel figure
                    plt.close(panel_fig)
                else:
                    ax.text(0.5, 0.5, f'Panel {i + 1}\n(Load Error)',
                            ha='center', va='center', transform=ax.transAxes)
                    ax.set_xticks([])
                    ax.set_yticks([])

            except Exception as e:
                logger.warning(f"Failed to load panel {i + 1} from {panel_file}: {e}")
                ax.text(0.5, 0.5, f'Panel {i + 1}\n(Error)',
                        ha='center', va='center', transform=ax.transAxes)
                ax.set_xticks([])
                ax.set_yticks([])

        # Hide unused subplots
        for i in range(num_panels, len(axes)):
            axes[i].set_visible(False)

        # Add overall title
        try:
            chart_title = chart.getTitle()
            if chart_title:
                fig.suptitle(f"{chart_title}", fontsize=12)
        except Exception as e:
            logger.debug(f"Could not set chart title: {e}")

        plt.tight_layout()

        # Clean up all temporary files after figure is created
        try:
            import shutil
            shutil.rmtree(temp_chart_dir, ignore_errors=True)
            logger.debug(f"Cleaned up temp directory: {temp_chart_dir}")
        except Exception as e:
            logger.debug(f"Could not clean up temp directory: {e}")

        return fig

    except Exception:
        # Clean up on error
        try:
            import shutil
            shutil.rmtree(temp_chart_dir, ignore_errors=True)
        except Exception as cleanup_e:
            logger.debug(f"Could not clean up temp directory after error: {cleanup_e}")
        raise


def _create_matplotlib_figure_from_image(img_array, figsize=None, title=None, dpi=None):
    """
    Common matplotlib figure creation from image array.
    
    Parameters
    ----------
    img_array : array-like
        Image data as numpy array
    figsize : tuple, optional
        Figure size (width, height) in inches
    title : str, optional
        Figure title
    dpi : int, optional
        Figure DPI

    Returns
    -------
    matplotlib.figure.Figure
        Figure containing the image
    """
    import matplotlib.pyplot as plt

    # Ensure matplotlib is in interactive mode based on configuration
    from .config import get_option
    if get_option('pyplot.ion') and not plt.isinteractive():
        plt.ion()

    # Create figure with specified parameters
    fig_kwargs = {}
    if figsize:
        fig_kwargs['figsize'] = figsize
    if dpi:
        fig_kwargs['dpi'] = dpi

    fig, ax = plt.subplots(**fig_kwargs)

    # Display image
    ax.imshow(img_array)
    ax.axis('off')  # Hide axes for cleaner look

    if title:
        ax.set_title(title)

    return fig


def _png_to_matplotlib(png_file: str, figsize=None) -> Figure:
    """
    Convert PNG file to matplotlib figure.
    
    Parameters
    ----------
    png_file : str
        Path to PNG file
    figsize : tuple, optional
        Figure size (width, height)
        
    Returns
    -------
    matplotlib.figure.Figure
        The matplotlib figure containing the PNG image
    """
    import matplotlib.image as mpimg

    try:
        # Load PNG image
        img = mpimg.imread(png_file)

        # Estimate size if not provided
        if figsize is None:
            height, width = img.shape[:2]
            figsize = (width / 100, height / 100)  # Rough conversion to inches

        # Use common figure creation
        return _create_matplotlib_figure_from_image(img, figsize=figsize)

    except Exception as e:
        logger.error(f"Failed to convert PNG to matplotlib: {e}")
        raise


def _convert_snt_table(table: Any, **kwargs) -> SNTObject:
    """
    Convert SNT Table to a SNTObject containing a xarray Dataset.

    Parameters
    ----------
    table : SNT Table
        The table object to convert
    **kwargs
        Additional conversion options:
        - include_metadata: bool, whether to include table metadata (default: True)
        - column_names: list, custom column names (default: use table's column names)

    Returns
    -------
    dict
        Dictionary containing table information and xarray Dataset
    """

    # Create result SNTObject dictionary
    result: SNTObject = {
        'type': type(xarray.Dataset ),
        'data': None,
        'metadata': {},
        'error': None
    }

    try:
        # Check if pandas are available
        if not HAS_PANDAS:
            result['error'] = ImportError(
                "pandas is required for SNTTable conversion. Install with: pip install pandas")
            logger.error("Missing pandas for SNTTable conversion")
            return result # type: ignore

        # Get table dimensions
        try:
            row_count = table.getRowCount()
            col_count = table.getColumnCount()
            logger.info(f"Converting SNTTable with {row_count} rows and {col_count} columns")
        except Exception as e:
            result['error'] = e
            logger.error(f"Failed to get table dimensions: {e}")
            return result # type: ignore

        # Get column names
        column_names = kwargs.get('column_names', None)
        if column_names is None:
            try:
                column_names = []
                for col_idx in range(col_count):
                    col_name = table.getColumnHeader(col_idx)
                    if col_name is None or col_name == "":
                        col_name = f"Column_{col_idx}"
                    column_names.append(str(col_name))
            except Exception as e:
                # Fallback to generic column names
                column_names = [f"Column_{i}" for i in range(col_count)]
                logger.warning(f"Could not get column headers, using generic names: {e}")

        # Extract table data
        try:
            data_dict = {}
            for col_idx in range(col_count):
                col_name = column_names[col_idx]
                col_data = []

                # Extract data for this column
                for row_idx in range(row_count):
                    try:
                        cell_value = table.get(col_name, row_idx)
                        col_data.append(cell_value)

                    except Exception as cell_e:
                        logger.debug(f"Error getting cell value at ({row_idx}, {col_idx}): {cell_e}")
                        col_data.append(None)

                data_dict[col_name] = col_data

            # Convert to pandas DataFrame first (easier data type handling)
            df = pd.DataFrame(data_dict)

            # Convert to xarray Dataset
            import xarray as xr
            xr_dataset = xr.Dataset.from_dataframe(df)

            # Add row index as a coordinate
            xr_dataset = xr_dataset.assign_coords(index=range(row_count))

            result['data'] = xr_dataset

            # Get table metadata if available
            include_metadata = kwargs.get('include_metadata', True)
            if include_metadata:
                try:
                    result['metadata']['row_count'] = row_count
                    result['metadata']['column_count'] = col_count
                    result['metadata']['column_names'] = column_names
                    result['metadata']['title'] = table.getTitle()

                    # Add data types for each column
                    result['metadata']['dtypes'] = {col: str(df[col].dtype) for col in df.columns}

                except Exception as e:
                    logger.debug(f"Could not extract table metadata: {e}")

            logger.info(f"Successfully converted SNTTable to xarray Dataset with shape {xr_dataset.dims}")

        except Exception as e:
            result['error'] = e
            logger.error(f"Failed to extract table data: {e}")
            return result # type: ignore

        return result # type: ignore

    except Exception as e:
        logger.error(f"Failed to convert SNTTable: {e}")
        result['error'] = e
        return result # type: ignore


def _svg_to_matplotlib(svg_file, dpi=300, figsize=None, background='white'):
    """
    Convert an SVG file to a matplotlib Figure object using cairosvg.

    Args:
        svg_file: Path to the SVG file or file-like object
        dpi: Resolution for rendering (default: 300)
        figsize: Tuple (width, height). If None, auto-sizes based on SVG
        background: Background color (default: 'white', use None for transparent)

    Returns:
        matplotlib.figure.Figure: Figure object containing the rendered SVG

    Example:
        >>> # Standard usage
        >>> fig = _svg_to_matplotlib('diagram.svg')
        >>> # Custom size
        >>> fig = _svg_to_matplotlib('diagram.svg', dpi=600, figsize=(10, 8))
        >>> plt.show()
    """
    if not HAS_CAIROSVG:
        raise ImportError("cairosvg is required for SVG conversion. Install with: pip install cairosvg")

    png_data = cairosvg.svg2png(
        url=svg_file,
        dpi=dpi,
        background_color=background
    )

    # Load PNG data as image array
    img = mpimg.imread(BytesIO(png_data), format='PNG')

    # Calculate figure size based on image dimensions
    if figsize is None:
        h, w = img.shape[:2]
        # Convert pixels back to inches at the specified DPI
        figsize = (w / dpi, h / dpi)

    # Use common figure creation
    fig = _create_matplotlib_figure_from_image(img, figsize=figsize, dpi=dpi)

    # Apply SVG-specific formatting
    fig.tight_layout(pad=0)
    fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
    fig.axes[0].margins(0)

    return fig


def _pdf_to_matplotlib(pdf_file, page=0, dpi=300, figsize=None):
    """
    Convert a PDF file (or specific page) to a matplotlib Figure object using PyMuPDF (fitz).

    Args:
        pdf_file: Path to the PDF file or file-like object
        page: Page number to convert (0-indexed, default: 0 for first page)
        dpi: Resolution for rendering (default: 300 for print quality)
        figsize: Tuple (width, height) in inches. If None, auto-sizes based on PDF

    Returns:
        matplotlib.figure.Figure: Figure object containing the rendered PDF page

    Example:
        >>> # Convert first page
        >>> fig = _pdf_to_matplotlib('document.pdf')
        >>> # Convert specific page at high quality
        >>> fig = _pdf_to_matplotlib('document.pdf', page=2, dpi=600)
        >>> # Custom size
        >>> fig = _pdf_to_matplotlib('document.pdf', figsize=(10, 8))
        >>> plt.show()
    """
    if not HAS_FITZ:
        raise ImportError("PyMuPDF (fitz) is required for PDF conversion. Install with: pip install PyMuPDF")

    # Open PDF
    doc = fitz.open(pdf_file)

    # Check if page exists
    if page >= len(doc):
        doc.close()
        raise ValueError(f"Page {page} does not exist. PDF has {len(doc)} pages.")

    # Get the page
    pdf_page = doc[page]

    # Calculate zoom factor for desired DPI
    # PyMuPDF default is 72 DPI
    zoom = dpi / 72.0
    mat = fitz.Matrix(zoom, zoom)

    # Render page to pixmap (image)
    pix = pdf_page.get_pixmap(matrix=mat)

    # Convert pixmap to numpy array
    img = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width, pix.n)

    # Handle different color modes
    if pix.n == 4:  # RGBA
        pass
    elif pix.n == 3:  # RGB
        pass
    elif pix.n == 1:  # Grayscale
        img = np.stack([img] * 3, axis=-1).squeeze()

    doc.close()

    # Calculate figure size based on image dimensions
    if figsize is None:
        h, w = img.shape[:2]
        figsize = (w / dpi, h / dpi)

    # Use common figure creation
    fig = _create_matplotlib_figure_from_image(
        img,
        figsize=figsize,
        title=f"PDF Page {page + 1}",
        dpi=dpi
    )

    # Apply PDF-specific formatting
    fig.tight_layout(pad=0)
    fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
    fig.axes[0].margins(0)

    return fig


# Define the converters
SNT_CONVERTERS = [
    sj.Converter(
        predicate=_is_snt_table,
        converter=_convert_snt_table,
        priority=sj.Priority.EXTREMELY_HIGH,  # Higher priority than generic collection converters
        name="SNTTable_to_Xarray"
    ),
    sj.Converter(
        predicate=_is_snt_chart,
        converter=_convert_snt_chart,
        priority=sj.Priority.NORMAL,
        name="SNTChart_to_Matplotlib"
    ),
]


def register_snt_converters():
    """
    Register SNT converters with scyjava.
    
    Note: This must be called BEFORE the JVM starts. Converters are
    automatically registered during pysnt.initialize().
    """
    if sj.jvm_started():
        logger.warning(
            "Cannot register converters: JVM already started! "
            "Converters must be registered before JVM startup."
        )
        return False

    try:
        for converter in SNT_CONVERTERS:
            sj.add_py_converter(converter)
            logger.info(f"Registered converter: {converter.name}")

        logger.info(f"Successfully registered {len(SNT_CONVERTERS)} SNT converter(s)")
        return True

    except Exception as e:
        logger.error(f"Failed to register SNT converter(s): {e}")
        return False


def _get_display_handler(obj):
    """
    Unified object type detection system for display handlers.
    
    Parameters
    ----------
    obj : Any
        Object to analyze
        
    Returns
    -------
    tuple
        (type_name, handler_function) or (None, None) if unknown
    """
    # Check matplotlib Figure
    if isinstance(obj, Figure):
        return 'matplotlib_figure', _display_matplotlib_figure

    # Check xarray objects
    try:
        if (hasattr(obj, 'plot') and hasattr(obj, 'dims') and hasattr(obj, 'values') and
                (str(type(obj)).find('xarray') != -1 or
                 str(type(obj)).find('DataArray') != -1 or
                 str(type(obj)).find('Dataset') != -1)):
            return 'xarray', _display_xarray
    except (AttributeError, TypeError, RuntimeError):
        pass

    # Check SNTObject dictionary
    if (isinstance(obj, dict) and
            all(k in obj for k in SNTObject.__annotations__.keys())):
        return 'snt_object', _display_snt_object

    # Check ImagePlus objects
    if str(type(obj)).find('ImagePlus') != -1:
        return 'imageplus', _display_imageplus

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
    >>> 
    >>> # Direct usage with ImagePlus
    >>> skeleton = tree.getSkeleton2D()
    >>> snt_obj = pysnt.display(skeleton)  # Returns SNTObject with xarray data
    >>> 
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
        if _is_tree_object(obj):
            obj = obj.getSkeleton2D()
        elif _is_path_object(obj):
            from . import Tree
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

        # Display the data
        try:
            if hasattr(data, 'to_pandas'):
                print(data.to_pandas().head())
            else:
                print(data)
        except Exception as e:
            logger.warning(f"Could not display xarray data: {e}")
            print(f"xarray object: {type(data)}")
        return obj
    elif isinstance(data, numpy.ndarray):
        logger.info(f"Displaying numpy array (size: {data.size})")
        with np.printoptions(precision=3, suppress=True):
            print(data)
        return obj
    else:
        logger.warning(f"SNTObject data is not supported: {type(data)}")
        return None


def _display_snt_object(obj, **kwargs):
    """Handler function for SNTObject display (for dispatch table)."""
    return _handle_snt_object_display(obj, **kwargs)


def _display_imageplus(obj, **kwargs):
    """
    Handler function for ImagePlus display.

    If the image is a timelapse, only the first frame is considered; if 3D, a MIP is retrieved;
    if multichannel an RGB version is obtained. ROIs are also displayed if image has stored ROIs.

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
    logger.info("Detected ImagePlus object - attempting conversion to xarray...")
    try:
        from .util import ImpUtils
        from .core import ij
        logger.info("Converting ImagePlus to xarray using ImpUtils and ij.py.from_java()...")

        # Extract frame parameter (supports frame=, t=, time=, case-insensitive)
        kwargs_lower = {k.lower(): v for k, v in kwargs.items()}
        frame = None
        for key in ['frame', 't', 'time', 'timepoint']:
            if key in kwargs_lower:
                try:
                    frame = int(kwargs_lower[key])
                    break
                except (ValueError, TypeError):
                    pass
        frame = frame if frame is not None else 1
        converted = ij().py.from_java(ImpUtils.convertToSimple2D(obj, frame))
        _display_xarray(converted, **kwargs)
        return converted

    except Exception as ij_e:
        logger.info(f"ImagePlus conversion failed: {ij_e}")
        return None


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
    import scyjava as sj

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

    # Fallbacks - return info about the object
    logger.warning(f"Could not convert or display object of type: {type(obj)}")
    logger.info("Available options:")
    logger.info("1. Use pysnt.to_python(obj) to convert manually")
    logger.info("3. Use pysnt.enhance_java_object(obj) to enhance its display capabilities")
    logger.info("4. Check if object has a show() method: obj.show()")
    logger.info("5. Open an issue at https://github.com/morphonets/pysnt")

    return None


def _show_matplotlib_figure(fig=None, **kwargs) -> bool:
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
    import matplotlib.pyplot as plt
    import matplotlib

    # Get the figure to display
    if fig is None:
        fig = plt.gcf()  # Get current figure

    logger.debug(f"Showing matplotlib figure with unified display (backend: {matplotlib.get_backend()})")

    # Ensure matplotlib is in interactive mode based on configuration
    from .config import get_option
    if get_option('pyplot.ion') and not plt.isinteractive():
        plt.ion()

    try:
        # Make figure current and show
        current_fig = plt.figure(fig.number)  # Make this figure current
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
                # Method 3: Force display using canvas
                fig.canvas.show()
                logger.info("Successfully displayed figure using canvas.show()")
            except Exception as e3:
                logger.debug(f"canvas.show() failed: {e3}")
                # Method 4: Save and display info as fallback
                logger.warning(f"Could not display figure directly. Figure created with {len(fig.axes)} axes.")
                logger.info("Figure is available but display failed - you may need to call plt.show() manually")


def _display_xarray(xarr: Any, **kwargs) -> None:
    """
    Display an xarray DataArray or Dataset using matplotlib.
    
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
    import matplotlib.pyplot as plt
    
    # Ensure matplotlib is in interactive mode based on configuration
    from .config import get_option
    if get_option('pyplot.ion') and not plt.isinteractive():
        plt.ion()

    logger.debug(f"Displaying xarray object: {type(xarr)}")

    try:
        # Get display parameters
        cmap = kwargs.get('cmap', 'gray')  # Default to grayscale for images
        title = kwargs.get('title', None)

        # Handle xarray Dataset (from SNTTable) vs DataArray (from ImagePlus)
        if str(type(xarr)).find('Dataset') != -1:
            logger.debug("Detected xarray Dataset - displaying as table/data summary")
            _display_xarray_dataset(xarr, **kwargs)
            return

        # Method 1: Try xarray's built-in plot method for DataArray
        try:
            logger.debug("Trying xarray.plot() method...")

            # Handle different dimensionalities
            if hasattr(xarr, 'ndim'):
                if xarr.ndim == 2:
                    # 2D image - use imshow-style plot
                    # Ensure xarray doesn't add its own colorbar if we're going to add one later
                    plot_obj = xarr.plot(cmap=cmap, add_colorbar=True, **kwargs)
                elif xarr.ndim == 3:
                    # 3D image - plot middle slice
                    middle_slice = xarr.shape[0] // 2
                    plot_obj = xarr[middle_slice].plot(cmap=cmap, add_colorbar=True, **kwargs)
                    if not title:
                        title = f"Slice {middle_slice} of 3D image"
                else:
                    # Higher dimensions - flatten to 2D
                    plot_obj = xarr.plot(cmap=cmap, add_colorbar=True, **kwargs)
            else:
                # Fallback - just try to plot
                plot_obj = xarr.plot(cmap=cmap, add_colorbar=True, **kwargs)

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
    if not HAS_PANDASGUI:
        logger.warning("PandasGUI not available. Install with: pip install pandasgui")
        return False

    try:
        import threading
        import time
        import sys
        import os
        
        # Check if we should use safe mode
        from .config import get_option
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
                    from PyQt5.QtWidgets import QApplication
                    from PyQt5.QtCore import Qt
                    
                    # Set attributes before creating QApplication
                    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
                    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
                except ImportError:
                    pass  # PyQt5 not available, continue anyway

                # Show in PandasGUI with the specified title
                gui = pandasgui_show(df_copy, title=title)

                # Keep the GUI alive by running its event loop
                if hasattr(gui, 'app') and hasattr(gui.app, 'exec_'):
                    gui.app.exec_()

            except Exception as e:
                logger.error(f"PandasGUI error: {e}")
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
    from .config import get_option
    
    try:
        import pandas as pd

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
    import matplotlib.pyplot as plt
    import numpy as np
    
    # Ensure matplotlib is in interactive mode based on configuration
    from .config import get_option
    if get_option('pyplot.ion') and not plt.isinteractive():
        plt.ion()

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
            except Exception:
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
            except Exception:
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

                import pandas as pd
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
    import matplotlib.pyplot as plt
    import numpy as np
    
    # Ensure matplotlib is in interactive mode based on configuration
    from .config import get_option
    if get_option('pyplot.ion') and not plt.isinteractive():
        plt.ion()

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
    import matplotlib.pyplot as plt
    import numpy as np
    
    # Ensure matplotlib is in interactive mode based on configuration
    from .config import get_option
    if get_option('pyplot.ion') and not plt.isinteractive():
        plt.ion()

    try:
        # Get numeric variables
        numeric_vars = []
        for var in display_vars:
            try:
                data = dataset[var].values
                if np.issubdtype(data.dtype, np.number):
                    numeric_vars.append(var)
            except Exception:
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

        import pandas as pd
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
                text = ax.text(j, i, f'{corr_matrix.iloc[i, j]:.2f}',
                               ha="center", va="center",
                               color="black" if abs(corr_matrix.iloc[i, j]) < 0.5 else "white")

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


def _display_xarray_dataset(dataset: Any, **kwargs) -> Any:
    """
    Display an xarray Dataset (e.g., SNTTable conversion).
    
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
    from .config import get_option
    
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


# Registry for custom display handlers
_DISPLAY_HANDLERS = {}


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
        Display parameters
        
    Returns
    -------
    SNTObject or None
        SNTObject with display result or None on failure
    """
    import matplotlib.pyplot as plt
    
    # Ensure matplotlib is in interactive mode based on configuration
    from .config import get_option
    if get_option('pyplot.ion') and not plt.isinteractive():
        plt.ion()

    # Handle different dimensionalities
    original_shape = data.shape
    title = kwargs.get('title', None)

    if data.ndim == 3:
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

    # Create figure and display
    fig, ax = plt.subplots()
    ax.set_title(title)

    cmap = kwargs.get('cmap', 'gray')

    # Filter kwargs for matplotlib imshow - exclude internal and display-specific parameters
    internal_params = {'_internal', 'cmap', 'title', 'add_colorbar'}
    imshow_kwargs = {k: v for k, v in kwargs.items() if k not in internal_params}

    logger.debug(f"Using matplotlib imshow with filtered kwargs: {imshow_kwargs}")
    im = ax.imshow(img_data, cmap=cmap, **imshow_kwargs)

    # Add colorbar if requested
    if kwargs.get('add_colorbar', True):
        plt.colorbar(im, ax=ax)

    # Use unified display system
    if _show_matplotlib_figure(fig):
        logger.info(f"Successfully displayed {source_type} data as image")
        return {
            'type': Figure,
            'data': data,
            'metadata': {
                'source_type': source_type,
                'original_shape': original_shape,
                'displayed_shape': img_data.shape,
                'title': title
            },
            'error': None
        }
    else:
        logger.warning(f"Failed to display {source_type} figure")
        return None


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


def list_converters() -> List[Dict[str, Any]]:
    """
    List all registered SNT converters.
    
    Returns
    -------
    list
        List of dictionaries containing converter information
    """
    converter_info = []

    for converter in SNT_CONVERTERS:
        info = {
            'name': converter.name,
            'priority': converter.priority,
            'predicate': converter.predicate.__name__ if hasattr(converter.predicate, '__name__') else str(
                converter.predicate),
            'converter': converter.converter.__name__ if hasattr(converter.converter, '__name__') else str(
                converter.converter),
        }
        converter_info.append(info)

    return converter_info


def _should_enhance_object(obj) -> bool:
    """Check if object should be enhanced with fallback methods."""
    return _is_snt_chart_object(obj) or _is_gui_object(obj)


def _enhanced_show_method(original_obj):
    """
    Create an enhanced show() method that falls back to display() on failure.
    
    Parameters
    ----------
    original_obj : Any
        The original Java object
        
    Returns
    -------
    callable
        Enhanced show method with fallback logic
    """

    def enhanced_show(*args, **kwargs):
        """
        Enhanced show method with fallback to display().
        
        This method first tries the original Java show() method, and if that fails
        (e.g., due to HeadlessException), it falls back to display() which should
        handle SNT-specific conversions.
        """
        try:
            # Try to call the original Java show method
            # Get the original show method from the Java object
            original_show = getattr(original_obj.__class__, 'show', None)
            if original_show:
                return original_show(original_obj, *args, **kwargs)
            else:
                # Fallback if no original show method
                raise AttributeError("No original show method found")

        except Exception as e:
            logger.info(f"Original show() failed ({e}), falling back to auto-conversion")
            # Fallback to auto-conversion
            return _display_with_auto_conversion(original_obj, **kwargs)

    return enhanced_show


class EnhancedJavaObject:
    """
    Wrapper class that adds enhanced show() and setVisible() methods to Java objects.
    
    This wrapper delegates all attribute access to the wrapped Java object,
    but provides enhanced methods with fallback logic for GUI operations.
    """

    def __init__(self, java_obj):
        """Initialize with a Java object to wrap."""
        object.__setattr__(self, '_java_obj', java_obj)
        object.__setattr__(self, '_is_chart', _is_snt_chart_object(java_obj))
        object.__setattr__(self, '_is_gui', _is_gui_object(java_obj))
        object.__setattr__(self, '_enhanced', _should_enhance_object(java_obj))

    def __getattr__(self, name):
        """Delegate attribute access to the wrapped Java object."""
        is_chart = object.__getattribute__(self, '_is_chart')
        is_gui = object.__getattribute__(self, '_is_gui')

        if name == 'show' and is_chart:
            return self._enhanced_show
        elif name == 'setVisible' and is_gui:
            return self._enhanced_setVisible

        return getattr(object.__getattribute__(self, '_java_obj'), name)

    def __setattr__(self, name, value):
        """Delegate attribute setting to the wrapped Java object."""
        if name.startswith('_'):
            object.__setattr__(self, name, value)
        else:
            setattr(object.__getattribute__(self, '_java_obj'), name, value)

    def __dir__(self):
        """Return attributes from the wrapped Java object."""
        return dir(object.__getattribute__(self, '_java_obj'))

    def __repr__(self):
        """Return representation of the wrapped Java object."""
        java_obj = object.__getattribute__(self, '_java_obj')
        enhanced = object.__getattribute__(self, '_enhanced')
        if enhanced:
            return f"<Enhanced {repr(java_obj)}>"
        return repr(java_obj)

    def _enhanced_show(self, *args, **kwargs):
        """
        Enhanced show method with fallback to display().
        
        This method first tries the original Java show() method, and if that fails
        (e.g., due to HeadlessException), it falls back to display() which can 
        handle SNT-specific conversions.
        """
        java_obj = object.__getattribute__(self, '_java_obj')
        try:
            # Try to call the original Java show method
            original_show = getattr(java_obj, 'show')
            return original_show(*args, **kwargs)

        except Exception as e:
            logger.info(f"Original show() failed ({e}), falling back to auto-conversion")
            # Fallback: use auto-conversion display
            try:
                return _display_with_auto_conversion(java_obj, **kwargs)
            except Exception as conv_e:
                logger.error(f"Auto-conversion display failed: {conv_e}")
                return None

    def _enhanced_setVisible(self, visible=True, **kwargs):
        """
        Enhanced setVisible method with fallback to display().
        
        This method first tries the original Java setVisible() method, and if that fails
        (e.g., due to HeadlessException), it falls back to display() when visible=True.
        """
        java_obj = object.__getattribute__(self, '_java_obj')
        try:
            # Try to call the original Java setVisible method
            original_setVisible = getattr(java_obj, 'setVisible')
            return original_setVisible(visible)

        except Exception as e:
            if visible:
                logger.info(f"Original setVisible(true) failed ({e}), falling back to auto-conversion")
                # Only fallback to display when trying to make visible (not when hiding)
                try:
                    return _display_with_auto_conversion(java_obj, **kwargs)
                except Exception as conv_e:
                    logger.error(f"Auto-conversion display failed: {conv_e}")
                    return None
            else:
                # For setVisible(false), just log and return (nothing to display)
                logger.info(f"setVisible(false) failed ({e}), ignoring (object already hidden)")
                return None


def enhance_java_object(obj: Any) -> Any:
    """
    Enhance a Java object with fallback show() and setVisible() methods if applicable.
    
    This function checks if the object is an SNT chart or GUI object and if so, wraps it
    with an enhanced version that falls back to display() on GUI method failures.
    
    Parameters
    ----------
    obj : Any
        Java object to potentially enhance
        
    Returns
    -------
    Any
        Enhanced wrapper object if applicable, otherwise the original object
        
    Examples
    --------
    >>> # For charts
    >>> chart = stats.getHistogram('Branch length')
    >>> enhanced_chart = enhance_java_object(chart)
    >>> enhanced_chart.show()  # Will fallback to display() if GUI fails
    >>> 
    >>> # For GUI objects
    >>> ui = pysnt.PathManagerUI()
    >>> enhanced_ui = enhance_java_object(ui)
    >>> enhanced_ui.setVisible(True)  # Will fallback to display() if GUI fails
    """
    if _should_enhance_object(obj):
        try:
            enhanced_obj = EnhancedJavaObject(obj)
            enhancement_types = []
            if _is_snt_chart_object(obj):
                enhancement_types.append("show()")
            if _is_gui_object(obj):
                enhancement_types.append("setVisible()")

            logger.debug(f"Enhanced {type(obj).__name__} with fallback {', '.join(enhancement_types)} method(s)")
            return enhanced_obj
        except Exception as e:
            logger.warning(f"Failed to enhance object with fallback methods: {e}")

    return obj


def auto_enhance_java_objects(enabled: bool = True):
    """
    Enable or disable automatic enhancement of Java objects.
    
    When enabled, this function monkey-patches scyjava's jimport to automatically
    enhance returned Java objects with fallback show() methods.
    
    Parameters
    ----------
    enabled : bool, default True
        Whether to enable automatic enhancement
        
    Note
    ----
    This is experimental and may have side effects. Use with caution.
    """
    if not enabled:
        logger.info("Auto-enhancement of Java objects disabled")
        return

    try:
        # This would require more complex implementation to intercept
        # all Java object creation. For now, we'll rely on manual enhancement.
        logger.info("Auto-enhancement not yet implemented. Use enhance_java_object() manually.")
    except Exception as e:
        logger.error(f"Failed to enable auto-enhancement: {e}")
