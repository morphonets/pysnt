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
        
        # Handle summary mode specially
        if table_mode == 'summary':
            title = kwargs.get('title', 'DataFrame Summary')
            _summarize_dataframe(df, title)
            return df
        
        # Map table mode to display parameters
        if table_mode == 'pandasgui':
            kwargs['use_gui'] = True
        else:
            # For other modes (heatmap, heatmap_norm, etc.), use GUI if available
            kwargs['use_gui'] = _has_pandasgui()
        
        # Use the existing DataFrame display function
        success = _show_pandasgui_dataframe(df, title=kwargs.get('title', 'DataFrame'), **kwargs)
        
        if not success:
            # Fallback to console display
            config = _extract_display_config(**kwargs)
            max_rows = config.get('max_rows', get_option('display.max_rows'))
            max_cols = config.get('max_cols', get_option('display.max_columns'))
            precision = config.get('precision', get_option('display.precision'))
            
            # Ensure precision is a valid integer (pandas can't handle None or invalid values)
            if precision is None or not isinstance(precision, int) or precision < 0:
                precision = 6  # Default fallback
            
            # Handle None values in DataFrame that can cause formatting issues
            df_display = df.copy()
            df_display = df_display.fillna('None')
            
            with pandas.option_context('display.max_rows', max_rows,
                                     'display.max_columns', max_cols,
                                     'display.precision', precision,
                                     'display.width', None):
                print("pandas.DataFrame:")
                print(df_display)
                print(f"Shape: {df.shape}")
                if hasattr(df, 'describe'):
                    print("\nSummary statistics:")
                    try:
                        print(df.describe())
                    except Exception as e:
                        print(f"Summary statistics unavailable: {e}")
        
        return df
        
    except Exception as e:
        _handle_display_error(e, "pandas DataFrame display", "DataFrame")
        # Fallback to simple print
        print("pandas.DataFrame:")
        try:
            # Handle None values that can cause formatting issues
            df_display = df.copy()
            df_display = df_display.fillna('None')
            print(df_display)
        except Exception as e2:
            print(f"DataFrame display failed: {e2}")
            print(f"DataFrame shape: {df.shape}")
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

        # SKIP xarray.plot() to avoid double figure creation
        # The issue is that xarray.plot() creates a figure, and then _display_array_data also creates one
        # Let's use only the unified array display system
        logger.debug("Skipping xarray.plot() to avoid double figure creation, using unified array display")
        
        # Method: Convert to numpy and use matplotlib directly
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
        
        # Return the original ImagePlus object instead of the xarray to prevent double processing
        # The display has already been handled by _display_xarray()
        return obj

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
        - plot_type: 'auto', 'dataframe', 'heatmap', 'heatmap_norm', 'summary' (default: uses pysnt.get_option('display.table_mode'))
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
        elif plot_type == 'heatmap':
            # Keep as heatmap for special handling
            pass
        elif plot_type == 'heatmap_norm':
            # Keep as heatmap_norm for special handling
            pass
        
        # Auto-select plot type based on data
        if plot_type == 'auto':
            plot_type = 'summary'

        # Route to appropriate display function
        if plot_type == 'dataframe':
            return _display_dataset_as_dataframe(dataset, **kwargs)
        elif plot_type == 'heatmap':
            return _display_dataset_as_heatmap(dataset, **kwargs)
        elif plot_type == 'heatmap_norm':
            return _display_dataset_as_heatmap_normalized(dataset, **kwargs)
        elif plot_type == 'summary':
            return _display_dataset_as_summary(dataset, **kwargs)
        else:
            logger.warning(
                f"Unknown plot_type: {plot_type}. Available options: 'auto', 'dataframe', 'pandasgui', 'heatmap', 'heatmap_norm', 'summary'")
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
        
        # Ensure precision is a valid integer (pandas can't handle None or invalid values)
        if precision is None or not isinstance(precision, int) or precision < 0:
            precision = 6  # Default fallback
        
        # Handle None values in DataFrame that can cause formatting issues
        df_display = df.copy()
        
        # Replace None values with 'None' string for display to avoid pandas formatting errors
        df_display = df_display.fillna('None')

        with pandas.option_context('display.max_rows', max_rows,
                                 'display.max_columns', max_cols,
                                 'display.precision', precision,
                                 'display.width', None):
            print(f"xarray.Dataset as DataFrame: {title}")
            print(f"Shape: {df.shape}")
            print(df_display)
            
            if hasattr(df, 'describe'):
                print("\nSummary statistics:")
                # Use original df for describe() as it handles None values better
                try:
                    print(df.describe())
                except Exception as e:
                    print(f"Summary statistics unavailable: {e}")

        logger.info(f"Successfully displayed Dataset as DataFrame in console: '{title}'")
        return True

    except Exception as e:
        _handle_display_error(e, "Dataset to DataFrame display", "Dataset")
        return False


def _display_dataset_as_heatmap(dataset: Any, **kwargs) -> bool:
    """
    Display xarray Dataset as a heatmap visualization.
    
    This function converts the dataset to a pandas DataFrame, converts all values
    to numeric (replacing None and empty strings with NaN), and creates a heatmap
    visualization using matplotlib.
    
    Parameters
    ----------
    dataset : xarray.Dataset
        The dataset to display as a heatmap
    **kwargs
        Additional arguments for display:
        - title : str, optional
          Title for the heatmap (default: "Dataset Comparison Heatmap")
        - xlabel : str, optional
          X-axis label (default: "Metrics")
        - ylabel : str, optional
          Y-axis label (default: "Datasets")
        - cmap : str, optional
          Colormap for the heatmap (default: "viridis")
        - figsize : tuple, optional
          Figure size (default: uses pysnt.get_option('plotting.figure_size'))
        
    Returns
    -------
    bool
        True if successful, False otherwise
    """
    from ..config import get_option
    
    logger.debug(f"Displaying xarray Dataset as heatmap: {dataset}")

    try:
        # Import required libraries
        import pandas as pd
        import matplotlib.pyplot as plt
        
        # Convert dataset to DataFrame
        df = dataset.to_dataframe()
        
        if df.empty:
            logger.warning("Dataset is empty, cannot create heatmap")
            return False
        
        logger.info(f"Converting Dataset to heatmap: {df.shape[0]} rows × {df.shape[1]} columns")
        
        # Convert to numeric, replacing None and empty strings with NaN
        df_numeric = df.apply(pd.to_numeric, errors='coerce')
        
        # Get display parameters
        config = _extract_display_config(**kwargs)
        figsize = config.get('figsize', get_option('plotting.figure_size'))
        title = kwargs.get('title', 'Dataset Comparison Heatmap')
        xlabel = kwargs.get('xlabel', 'Metrics')
        ylabel = kwargs.get('ylabel', 'Datasets')
        cmap = kwargs.get('cmap', 'viridis')
        
        # Setup matplotlib for interactive display
        _setup_matplotlib_interactive()
        
        # Create heatmap
        fig, ax = plt.subplots(figsize=figsize)
        im = ax.imshow(df_numeric.values, aspect='auto', cmap=cmap)
        
        # NaN values will appear as a different color (white by default)
        im.cmap.set_bad(color='lightgray')  # Set color for NaN values
        
        # Set ticks and labels
        ax.set_xticks(np.arange(len(df_numeric.columns)))
        ax.set_yticks(np.arange(len(df_numeric.index)))
        ax.set_xticklabels(df_numeric.columns, rotation=90, ha='right', fontsize=8)
        ax.set_yticklabels(df_numeric.index)
        
        # Add colorbar
        cbar = plt.colorbar(im, ax=ax, label='Value')
        
        # Labels
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.set_title(title)
        
        plt.tight_layout()
        plt.show()
        
        logger.info(f"Successfully displayed Dataset as heatmap: '{title}'")
        return True

    except Exception as e:
        _handle_display_error(e, "Dataset heatmap display", "Dataset")
        return False


def _display_dataset_as_heatmap_normalized(dataset: Any, **kwargs) -> bool:
    """
    Display xarray Dataset as a normalized heatmap visualization.
    
    This function converts the dataset to a pandas DataFrame, converts all values
    to numeric (replacing None and empty strings with NaN), normalizes each column
    to 0-1 range, and creates a heatmap visualization using matplotlib.
    
    Parameters
    ----------
    dataset : xarray.Dataset
        The dataset to display as a normalized heatmap
    **kwargs
        Additional arguments for display:
        - title : str, optional
          Title for the heatmap (default: "Normalized Dataset Comparison Heatmap")
        - xlabel : str, optional
          X-axis label (default: "Metrics")
        - ylabel : str, optional
          Y-axis label (default: "Datasets")
        - cmap : str, optional
          Colormap for the heatmap (default: "viridis")
        - figsize : tuple, optional
          Figure size (default: uses pysnt.get_option('plotting.figure_size'))
        
    Returns
    -------
    bool
        True if successful, False otherwise
    """
    from ..config import get_option
    
    logger.debug(f"Displaying xarray Dataset as normalized heatmap: {dataset}")

    try:
        # Import required libraries
        import pandas as pd
        import matplotlib.pyplot as plt
        
        # Convert dataset to DataFrame
        df = dataset.to_dataframe()
        
        if df.empty:
            logger.warning("Dataset is empty, cannot create normalized heatmap")
            return False
        
        logger.info(f"Converting Dataset to normalized heatmap: {df.shape[0]} rows × {df.shape[1]} columns")
        
        # Convert to numeric, replacing None and empty strings with NaN
        df_numeric = df.apply(pd.to_numeric, errors='coerce')
        
        # Normalize each column to 0-1 range
        # Handle columns that are all NaN or have no variation
        df_normalized = df_numeric.copy()
        for col in df_numeric.columns:
            col_data = df_numeric[col]
            # Skip normalization if column is all NaN or has no variation
            if col_data.isna().all():
                logger.warning(f"Column '{col}' is all NaN, skipping normalization")
                continue
            
            col_min = col_data.min()
            col_max = col_data.max()
            
            if pd.isna(col_min) or pd.isna(col_max):
                logger.warning(f"Column '{col}' has NaN min/max values, skipping normalization")
                continue
                
            if col_min == col_max:
                # No variation in column - set to 0.5 (middle of 0-1 range)
                logger.warning(f"Column '{col}' has no variation (min=max={col_min}), setting to 0.5")
                df_normalized[col] = 0.5
            else:
                # Standard min-max normalization
                df_normalized[col] = (col_data - col_min) / (col_max - col_min)
        
        # Get display parameters
        config = _extract_display_config(**kwargs)
        figsize = config.get('figsize', get_option('plotting.figure_size'))
        title = kwargs.get('title', 'Normalized Dataset Comparison Heatmap')
        xlabel = kwargs.get('xlabel', 'Metrics')
        ylabel = kwargs.get('ylabel', 'Datasets')
        cmap = kwargs.get('cmap', 'viridis')
        
        # Setup matplotlib for interactive display
        _setup_matplotlib_interactive()
        
        # Create heatmap
        fig, ax = plt.subplots(figsize=figsize)
        im = ax.imshow(df_normalized.values, aspect='auto', cmap=cmap, vmin=0, vmax=1)
        
        # NaN values will appear as a different color (white by default)
        im.cmap.set_bad(color='lightgray')  # Set color for NaN values
        
        # Set ticks and labels
        ax.set_xticks(np.arange(len(df_normalized.columns)))
        ax.set_yticks(np.arange(len(df_normalized.index)))
        ax.set_xticklabels(df_normalized.columns, rotation=90, ha='right', fontsize=8)
        ax.set_yticklabels(df_normalized.index)
        
        # Add colorbar with normalized range
        cbar = plt.colorbar(im, ax=ax, label='Normalized Value (0-1)')
        
        # Labels
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.set_title(title)
        
        plt.tight_layout()
        plt.show()
        
        logger.info(f"Successfully displayed Dataset as normalized heatmap: '{title}'")
        return True

    except Exception as e:
        _handle_display_error(e, "Dataset normalized heatmap display", "Dataset")
        return False


def _display_dataset_as_summary(dataset: Any, **kwargs) -> bool:
    """
    Display xarray Dataset as a text-based summary.
    
    This function converts the dataset to a pandas DataFrame and provides
    a comprehensive text summary including shape, memory usage, data types,
    missing values, and data quality issues.
    
    Parameters
    ----------
    dataset : xarray.Dataset
        The dataset to summarize
    **kwargs
        Additional arguments for display:
        - title : str, optional
          Title for the summary (default: "Dataset Summary")
        
    Returns
    -------
    bool
        True if successful, False otherwise
    """
    logger.debug(f"Displaying xarray Dataset as summary: {dataset}")

    try:
        # Convert dataset to DataFrame
        df = dataset.to_dataframe()
        
        if df.empty:
            print("Dataset is empty - no data to summarize")
            return True
        
        # Get title
        title = kwargs.get('title', 'Dataset Summary')
        
        # Call the summary function
        _summarize_dataframe(df, title)
        
        logger.info(f"Successfully displayed Dataset summary: '{title}'")
        return True

    except Exception as e:
        _handle_display_error(e, "Dataset summary display", "Dataset")
        return False


def _summarize_dataframe(df, name="DataFrame"):
    """
    Pretty-print summary of DataFrame characteristics.
    
    Parameters
    ----------
    df : pandas.DataFrame
        The DataFrame to summarize
    name : str
        Name/title for the summary
    """
    import pandas as pd
    import numpy as np
    
    print(f"\n{'='*60}")
    print(f"  {name}")
    print(f"{'='*60}")

    # Basic info
    print(f"Shape: {df.shape[0]:,} rows × {df.shape[1]} columns")
    print(f"Memory: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
    print(f"Duplicate rows: {df.duplicated().sum():,}")

    # Missing values (simple version)
    missing = df.isnull().sum().sum()
    if missing > 0:
        print(f"Missing values: {missing:,} ({missing/df.size*100:.1f}%)")
    else:
        print("Missing values: None ✓")

    # Column types
    print(f"{'─'*60}")
    print("Column Types:")
    dtype_counts = df.dtypes.value_counts()
    for dtype, count in dtype_counts.items():
        print(f"  {dtype}: {count} columns")

    # Numeric columns summary
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    if len(numeric_cols) > 0:
        print(f"{'─'*60}")
        print(f"Numeric Columns ({len(numeric_cols)}):")
        for col in numeric_cols[:5]:  # Show first 5
            col_min = df[col].min()
            col_max = df[col].max()
            print(f"  {col}: [{col_min:.2f}, {col_max:.2f}]")
        if len(numeric_cols) > 5:
            print(f"  ... and {len(numeric_cols) - 5} more")

    # Categorical/object columns
    cat_cols = df.select_dtypes(include=['object', 'category']).columns
    if len(cat_cols) > 0:
        print(f"{'─'*60}")
        print(f"Categorical Columns ({len(cat_cols)}):")
        for col in cat_cols[:5]:  # Show first 5
            n_unique = df[col].nunique()
            print(f"  {col}: {n_unique} unique values")
        if len(cat_cols) > 5:
            print(f"  ... and {len(cat_cols) - 5} more")

    # Data quality issues
    issues = []
    all_nan_cols = df.columns[df.isnull().all()].tolist()
    if all_nan_cols:
        issues.append(f"Columns with all NaN: {', '.join(all_nan_cols)}")
    
    constant_cols = [col for col in df.columns if df[col].nunique() == 1]
    if constant_cols:
        issues.append(f"Constant columns: {', '.join(constant_cols)}")

    if issues:
        print(f"{'─'*60}")
        print("⚠ Data Quality Issues:")
        for issue in issues:
            print(f"  • {issue}")

    print(f"{'='*60}\n")