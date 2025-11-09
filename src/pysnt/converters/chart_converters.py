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
    # Use temporary directory approach instead of NamedTemporaryFile
    # This avoids issues with Java SNTChart save methods and file handles
    with _temp_directory(temp_dir) as temp_chart_dir:
        temp_path = os.path.join(temp_chart_dir, f"chart.{format_type}")
        
        # Initialize chart dimensions if needed
        try:
            if chart.getWidth() == 0 or chart.getHeight() == 0:
                chart.setSize(400, 400)
                chart.validate()
                chart.doLayout()
        except Exception as e:
            logger.debug(f"Could not initialize chart dimensions: {e}")
        
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
            fig = _svg_to_matplotlib(svg_file=temp_path, figsize=None, background='None')
        elif format_type == 'pdf':
            fig = _pdf_to_matplotlib(pdf_file=temp_path, figsize=None)
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

        # Create subplot grid using new utilities with aspect ratio preservation
        num_panels = len(panel_files)
        
        # Load panel figures first to analyze aspect ratios
        panel_figures = []
        for panel_file in panel_files:
            try:
                if format_type == 'svg':
                    panel_fig = _svg_to_matplotlib(svg_file=panel_file, figsize=None, background='None')
                elif format_type == 'pdf':
                    panel_fig = _pdf_to_matplotlib(pdf_file=panel_file, figsize=None)
                else:  # PNG
                    panel_fig = _png_to_matplotlib(png_file=panel_file, figsize=None)
                panel_figures.append(panel_fig)
            except Exception as e:
                logger.debug(f"Could not load panel figure for aspect analysis: {e}")
                panel_figures.append(None)
        
        # Use new grid creation utility with aspect ratio preservation
        from ..display.utils import _create_subplot_grid
        fig, axes, (rows, cols) = _create_subplot_grid(num_panels, panel_layout, 
                                                      figsize=None, source_figures=panel_figures)

        # Load and display each panel with improved formatting
        for i, (panel_file, panel_fig) in enumerate(zip(panel_files, panel_figures)):
            if i >= len(axes):
                break

            ax = axes[i]

            try:
                # Use pre-loaded panel figure or load if needed
                if panel_fig is None:
                    if format_type == 'svg':
                        panel_fig = _svg_to_matplotlib(svg_file=panel_file, figsize=None, background='None')
                    elif format_type == 'pdf':
                        panel_fig = _pdf_to_matplotlib(pdf_file=panel_file, figsize=None)
                    else:  # PNG
                        panel_fig = _png_to_matplotlib(png_file=panel_file, figsize=None)

                # Extract image data from panel figure
                if panel_fig and len(panel_fig.axes) > 0:
                    panel_ax = panel_fig.axes[0]
                    
                    # Detect if this is a polar plot or aspect-sensitive content
                    is_polar = any(hasattr(ax_check, 'name') and ax_check.name == 'polar' 
                                 for ax_check in panel_fig.axes)

                    # Copy the panel content to our subplot with aspect preservation
                    for child in panel_ax.get_children():
                        if hasattr(child, 'get_array'):  # Image data
                            try:
                                array = child.get_array()
                                
                                # Use new aspect ratio logic
                                from ..display.visual_display import _should_preserve_aspect
                                aspect = 'equal' if is_polar or _should_preserve_aspect(array) else 'auto'
                                ax.imshow(array, aspect=aspect)
                            except Exception as e:
                                logger.debug(f"Could not copy image data from panel {i}: {e}")

                    # Set equal aspect ratio for polar plots
                    if is_polar:
                        ax.set_aspect('equal', adjustable='box')

                    # Use clean axis formatting (no titles by default for consistency)
                    from ..display.utils import _setup_clean_axis
                    _setup_clean_axis(ax, title=None, show_title=False, hide_axis_completely=True)

                    # Close the temporary panel figure
                    plt.close(panel_fig)
                else:
                    ax.text(0.5, 0.5, f'Panel {i + 1}\n(Load Error)',
                            ha='center', va='center', transform=ax.transAxes)
                    # Use clean axis formatting for error placeholder
                    from ..display.utils import _setup_clean_axis
                    _setup_clean_axis(ax, title=None, show_title=False, hide_axis_completely=True)

            except Exception as e:
                logger.warning(f"Failed to load panel {i + 1} from {panel_file}: {e}")
                ax.text(0.5, 0.5, f'Panel {i + 1}\n(Error)',
                        ha='center', va='center', transform=ax.transAxes)
                # Use clean axis formatting for error placeholder
                from ..display.utils import _setup_clean_axis
                _setup_clean_axis(ax, title=None, show_title=False, hide_axis_completely=True)

        # Hide unused subplots
        for i in range(num_panels, len(axes)):
            axes[i].set_visible(False)

        # Apply standardized layout (no overall title by default for consistency)
        from ..display.utils import _apply_standard_layout
        _apply_standard_layout(fig, show_overall_title=False, show_panel_titles=False)

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


def _svg_to_matplotlib(svg_file, dpi=None, figsize=None, background='white'):
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
    from ..config import get_option
    
    if not HAS_CAIROSVG:
        raise ImportError("cairosvg is required for SVG conversion. Install with: pip install cairosvg")

    # Use config default if DPI not specified
    if dpi is None:
        dpi = get_option('display.chart_dpi')

    try:
        # Try to read and validate SVG file first
        with open(svg_file, 'rb') as f:
            svg_content = f.read()
        
        # Check if file is actually SVG (should start with <?xml, <!DOCTYPE, or <svg)
        svg_start = svg_content[:100].decode('utf-8', errors='ignore').strip()
        if not (svg_start.startswith('<?xml') or svg_start.startswith('<svg') or svg_start.startswith('<!DOCTYPE')):
            logger.warning(f"SVG file doesn't start with expected XML/SVG header. First 100 chars: {svg_start}")
            raise ValueError(f"Invalid SVG file format. File starts with: {svg_start[:50]}")
        
        # Decode SVG content for text processing
        svg_text = svg_content.decode('utf-8', errors='ignore')
        
        # Fix rendering issues with cairosvg
        # Replace 'shape-rendering:crispEdges' which cairosvg doesn't support
        # This fixes thin line rendering issues
        svg_text = svg_text.replace('shape-rendering:crispEdges', 'shape-rendering:auto')
        logger.debug("Replaced 'shape-rendering:crispEdges' with 'shape-rendering:auto' for cairosvg compatibility")
        
        # Convert back to bytes
        svg_content = svg_text.encode('utf-8')
        
        # Try to convert using the file content directly
        png_data = cairosvg.svg2png(
            bytestring=svg_content,
            dpi=dpi,
            background_color=background
        )
    except Exception as e:
        logger.error(f"Failed to convert SVG with cairosvg: {e}")
        # Log first few lines of SVG for debugging
        try:
            with open(svg_file, 'r', encoding='utf-8', errors='ignore') as f:
                first_lines = ''.join(f.readlines()[:5])
                logger.debug(f"First lines of SVG file:\n{first_lines}")
        except:
            pass
        raise

    # Load PNG data as image array
    img = mpimg.imread(BytesIO(png_data), format='PNG')

    # Calculate figure size based on image dimensions
    if figsize is None:
        h, w = img.shape[:2]
        # Convert pixels back to inches at the specified DPI
        figsize = (w / dpi, h / dpi)

    # Use unified figure creation with SVG-specific tight layout
    return _create_figure_with_image(img, figsize=figsize, dpi=dpi, tight_layout=True)


def _pdf_to_matplotlib(pdf_file, page=0, dpi=None, figsize=None):
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
    from ..config import get_option
    
    if not HAS_FITZ:
        raise ImportError("PyMuPDF (fitz) is required for PDF conversion. Install with: pip install PyMuPDF")

    # Use config default if DPI not specified
    if dpi is None:
        dpi = get_option('display.chart_dpi')

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
    # Try different rendering flags for better text handling
    pix = pdf_page.get_pixmap(
        matrix=mat,
        alpha=False,  # No alpha channel unless needed
        annots=False,  # Include annotations
        clip=None
    )

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
        title=None,  # Don't add automatic title
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