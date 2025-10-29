"""
Chart conversion functionality for PySNT.

This module handles conversion of SNTChart objects to matplotlib figures,
including:
- Chart predicate functions for type detection
- Chart converter functions for single and combined (multipanel) charts
- Format conversion utilities (SVG, PDF, PNG to matplotlib)
- Chart-specific helper functions and utilities

Dependencies: core.py
"""

import logging
import os
from typing import Any, Optional

from matplotlib.figure import Figure

from .core import (
    _create_converter_result,
    _create_error_result,
    _create_standard_error_message,
    _temp_file,
    _temp_directory,
    _setup_matplotlib_interactive,
    DEFAULT_SCALE,
    DEFAULT_MAX_PANELS,
    DEFAULT_PANEL_LAYOUT,
    SNTObject
)

logger = logging.getLogger(__name__)


def _is_snt_chart(obj: Any) -> bool:
    """Check if object is an SNTChart."""
    try:
        # Check for SNTChart methods
        return hasattr(obj, 'show') and hasattr(obj, 'save') and (hasattr(obj, 'getChart') or hasattr(obj, 'getFrame'))
    except (AttributeError, TypeError, RuntimeError):  # java errors can cause RuntimeError, etc.
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
    from ..config import get_option

    try:
        # Get conversion options with config defaults
        format_type = kwargs.get('format', get_option('display.chart_format')).lower()
        temp_dir = kwargs.get('temp_dir', None)
        scale = kwargs.get('scale', DEFAULT_SCALE)
        max_panels = kwargs.get('max_panels', DEFAULT_MAX_PANELS)
        panel_layout = kwargs.get('panel_layout', DEFAULT_PANEL_LAYOUT)

        # Check if this is a combined chart
        is_combined = chart.isCombined()
        logger.debug(f"Chart isCombined: {is_combined}")

        if is_combined:
            # Handle combined chart with multiple panels
            logger.info(f"Processing combined chart")
            figure_data = _convert_combined_snt_chart(chart, format_type, temp_dir, scale, max_panels, panel_layout)
        else:
            # Handle single chart or forced single processing
            figure_data = _convert_single_snt_chart(chart, format_type, temp_dir, scale)

        if figure_data is None:
            raise ValueError("Chart conversion produced no data")

        # Prepare metadata
        metadata = {
            'format': format_type,
            'scale': scale,
            'is_combined': is_combined
        }
        
        # Get additional chart metadata if available
        try:
            metadata['title'] = chart.getTitle()
            if hasattr(chart, 'containsValidData'):
                metadata['containsValidData'] = chart.containsValidData()
            if hasattr(chart, 'isLegendVisible'):
                metadata['isLegendVisible'] = chart.isLegendVisible()
        except Exception as e:
            logger.debug(f"Could not extract chart metadata: {e}")

        logger.info(f"Successfully converted SNTChart ({'combined' if is_combined else 'single'}) to matplotlib figure")
        return _create_converter_result(figure_data, 'SNTChart', **metadata)

    except Exception as e:
        logger.error(_create_standard_error_message("convert SNTChart", e, "SNTChart"))
        return _create_error_result(Figure, e, 'SNTChart')


def _convert_single_snt_chart(chart: Any, format_type: str, temp_dir: Optional[str], scale: float) -> Figure:
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
    with _temp_file(format_type, temp_dir) as temp_path:
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


def _convert_combined_snt_chart(chart: Any, format_type: str, temp_dir: Optional[str], scale: float, max_panels: int,
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
    import glob
    import math
    
    plt = _setup_matplotlib_interactive()

    with _temp_directory(temp_dir) as temp_chart_dir:
        base_name = "combined_chart"
        temp_path = os.path.join(temp_chart_dir, f"{base_name}.{format_type}")
        logger.debug(f"Using temp directory: {temp_chart_dir}")
        logger.debug(f"Base temp path: {temp_path}")

        panel_files = []
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

        return fig


# Format conversion utilities

try:
    import cairosvg # noqa
    HAS_CAIROSVG = True
except ImportError:
    HAS_CAIROSVG = False
    cairosvg = None

try:
    import fitz # noqa
    HAS_FITZ = True
except ImportError:
    HAS_FITZ = False
    fitz = None

import matplotlib.image as mpimg
import numpy as np
from io import BytesIO


def _create_figure_with_image(img_array, figsize=None, title=None, dpi=None, tight_layout=True):
    """
    Unified figure creation with consistent formatting.
    
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
    tight_layout : bool, default True
        Whether to apply tight layout formatting

    Returns
    -------
    matplotlib.figure.Figure
        Figure containing the image
    """
    plt = _setup_matplotlib_interactive()

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

    if tight_layout:
        fig.tight_layout(pad=0)
        fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
        ax.margins(0)

    return fig


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
        >>> fig1 = _svg_to_matplotlib('diagram.svg')
        >>> # Custom size
        >>> fig2 = _svg_to_matplotlib('diagram.svg', dpi=600, figsize=(10, 8))
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

    # Use unified figure creation with SVG-specific tight layout
    return _create_figure_with_image(img, figsize=figsize, dpi=dpi, tight_layout=True)


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
        >>> fig1 = _pdf_to_matplotlib('document.pdf')
        >>> # Convert specific page at high quality
        >>> fig2 = _pdf_to_matplotlib('document.pdf', page=2, dpi=600)
        >>> # Custom size
        >>> fig3 = _pdf_to_matplotlib('document.pdf', figsize=(10, 8))
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

    # Use unified figure creation with PDF-specific tight layout
    return _create_figure_with_image(
        img,
        figsize=figsize,
        title=f"PDF Page {page + 1}",
        dpi=dpi,
        tight_layout=True
    )


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
    try:
        # Load PNG image
        img = mpimg.imread(png_file)

        # Estimate size if not provided
        if figsize is None:
            height, width = img.shape[:2]
            figsize = (width / 100, height / 100)  # Rough conversion to inches

        # Use unified figure creation
        return _create_figure_with_image(img, figsize=figsize, tight_layout=False)

    except Exception as e:
        logger.error(f"Failed to convert PNG to matplotlib: {e}")
        raise