"""
Data display functionality for PySNT.

This module handles display of structured data including xarray datasets,
pandas DataFrames, and other tabular data structures.
"""

import logging
from typing import Any

import numpy as np

# Import utilities from our modules
from .utils import (
    _extract_display_config,
    _handle_display_error,
    _has_pandasgui,
    _get_pandasgui_show,
    DEFAULT_CMAP,
    _setup_matplotlib_interactive,
)

logger = logging.getLogger(__name__)

# Try to import optional dependencies
try:
    import xarray
    HAS_XARRAY = True
except ImportError:
    HAS_XARRAY = False
    xarray = None

try:
    import pandas
    HAS_PANDAS = True
except ImportError:
    HAS_PANDAS = False
    pandas = None

try:
    import matplotlib.pyplot as plt
    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False
    plt = None


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
            config = _extract_display_config(**kwargs)
            max_rows = config.get('max_rows', get_option('display.max_rows'))
            max_cols = config.get('max_cols', get_option('display.max_columns'))
            precision = config.get('precision', get_option('display.precision'))
            
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
        _handle_display_error(e, "pandas DataFrame display", "DataFrame")
        # Fallback to simple print
        print("pandas.DataFrame:")
        print(df)
        return df


def _show_pandasgui_dataframe(df, title="Dataset", **kwargs) -> bool:
    """
    Display a pandas DataFrame using PandasGUI with thread handling.
    
    This function provides a safe way to display DataFrames using PandasGUI
    with proper thread management and fallback handling.
    
    Parameters
    ----------
    df : pandas.DataFrame
        The DataFrame to display
    title : str, default "Dataset"
        Title for the PandasGUI window
    **kwargs
        Additional arguments:
        - use_gui: bool, whether to use PandasGUI (default: True if available)
        - gui_safe_mode: bool, whether to use safe mode for GUI (from config)
        
    Returns
    -------
    bool
        True if PandasGUI display succeeded, False otherwise
    """
    # Check if GUI display is requested and available
    use_gui = kwargs.get('use_gui', True)
    if not use_gui or not _has_pandasgui():
        return False
    
    try:
        # Check if we should use safe mode
        from ..config import get_option
        gui_safe_mode = get_option('display.gui_safe_mode')
        
        # Check if we're on macOS
        import platform
        is_macos = platform.system() == 'Darwin'
        
        if gui_safe_mode and is_macos:
            logger.info("GUI safe mode enabled on macOS - using console display")
            return False
        
        # Import PandasGUI
        pandasgui_show = _get_pandasgui_show()
        
        if pandasgui_show is None:
            logger.debug("PandasGUI not available")
            return False
        
        logger.info(f"Displaying DataFrame in PandasGUI: '{title}' (shape: {df.shape})")
        
        # Use threading to avoid blocking
        import threading
        import time
        
        def show_gui():
            try:
                pandasgui_show(df, title=title)
            except Exception as e:
                logger.debug(f"PandasGUI display failed in thread: {e}")
        
        # Start GUI in separate thread
        gui_thread = threading.Thread(target=show_gui, daemon=True)
        gui_thread.start()
        
        # Give GUI time to start
        time.sleep(0.5)
        
        logger.info("PandasGUI window should be opening...")
        return True
        
    except Exception as e:
        logger.debug(f"PandasGUI display failed: {e}")
        return False


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
            from .visual_display import _show_matplotlib_figure
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
                from .visual_display import _display_array_data
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
        _handle_display_error(e, "xarray display", str(type(xarr)))


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
        from ..converters.structured_data_converters import _extract_imageplus_metadata
        
        # Extract metadata first (before conversion to avoid recursion)
        metadata = _extract_imageplus_metadata(obj, **kwargs)
        
        # Convert ImagePlus to xarray using existing utilities
        # This bypasses the scyjava converter system to avoid recursion
        logger.debug("Converting ImagePlus to xarray using ImpUtils...")
        frame = int(metadata.get('frame', 1))
        
        try:
            converted_imp = ImpUtils.convertToSimple2D(obj, frame)
        except (TypeError, AttributeError) as e:
            logger.warning(f"ImpUtils.convertToSimple2D failed: {e}")
            logger.info("Falling back to direct ij().py.from_java() conversion...")
            # Fallback: try direct conversion without ImpUtils
            converted_imp = obj
        
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
        _handle_display_error(e, "ImagePlus display", "ImagePlus")
        return None


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
        config = _extract_display_config(**kwargs)
        plot_type = config.get('table_mode', get_option('display.table_mode')).lower()
        max_vars = kwargs.get('max_vars', 10)
        figsize = config.get('figsize', get_option('plotting.figure_size'))
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
        elif plot_type in ['summary', 'distribution', 'correlation']:
            # Import plotting functions from visual_display
            from .visual_display import _create_dataset_summary_plot, _create_dataset_distribution_plot, _create_dataset_correlation_plot
            if plot_type == 'summary':
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
        _handle_display_error(e, "xarray Dataset display", "Dataset")
        return False


def _display_dataset_as_dataframe(dataset: Any, **kwargs) -> bool:
    """
    Display xarray Dataset as a pandas DataFrame.
    
    This function converts an xarray Dataset to a pandas DataFrame and displays it
    using the configured display method (console or PandasGUI).
    
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
        True if display succeeded, False otherwise
    """
    try:
        logger.debug("Converting xarray Dataset to pandas DataFrame for display")

        # Get display parameters with config defaults
        config = _extract_display_config(**kwargs)
        use_gui = config.get('use_gui', False)
        title = kwargs.get('title', 'SNT Dataset')

        # Convert dataset to DataFrame
        df = dataset.to_dataframe()

        if use_gui:
            # Use PandasGUI
            success = _show_pandasgui_dataframe(df, title=title, **kwargs)
            if success:
                logger.info(f"Successfully displayed Dataset as DataFrame in PandasGUI: '{title}'")
                return True
            else:
                logger.info("PandasGUI display failed, falling back to console")

        # Console display
        max_rows = config.get('max_rows')
        max_cols = config.get('max_cols')
        precision = config.get('precision')

        with pandas.option_context('display.max_rows', max_rows,
                                 'display.max_columns', max_cols,
                                 'display.precision', precision,
                                 'display.width', None):
            print(f"xarray.Dataset as DataFrame: {title}")
            print(f"Shape: {df.shape}")
            print(df)
            
            if hasattr(df, 'describe'):
                print("\nSummary statistics:")
                print(df.describe())

        logger.info(f"Successfully displayed Dataset as DataFrame in console: '{title}'")
        return True

    except Exception as e:
        _handle_display_error(e, "Dataset to DataFrame display", "Dataset")
        return False
