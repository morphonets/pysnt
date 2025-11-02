"""
Visual display functionality for PySNT.

This module handles all matplotlib-based visualizations including figures,
graphs, arrays, and plot creation.
"""

import logging
import time
from typing import Any, List

import numpy as np

# Import utilities from our modules
from .utils import (
    DEFAULT_CMAP,
    DEFAULT_NODE_COLOR,
    DEFAULT_NODE_SIZE,
    ERROR_MISSING_NETWORKX,
    _setup_matplotlib_interactive,
    _create_standard_figure,
)

logger = logging.getLogger(__name__)

# Try to import optional dependencies
try:
    import matplotlib.pyplot as plt
    from matplotlib.figure import Figure
    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False
    Figure = None
    plt = None

try:
    import networkx as nx
    HAS_NETWORKX = True
except ImportError:
    HAS_NETWORKX = False
    nx = None


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
                # Method 3: Force display using canvas manager
                if hasattr(fig.canvas, 'manager') and hasattr(fig.canvas.manager, 'show'):
                    fig.canvas.manager.show()
                    logger.info("Successfully displayed figure using canvas.manager.show()")
                else:
                    # Fallback: draw and flush events
                    fig.canvas.draw()
                    fig.canvas.flush_events()
                    logger.info("Drew figure and flushed events as fallback")
            except Exception as e3:
                logger.debug(f"canvas manager show failed: {e3}")
                # Method 4: Save and display info as fallback
                logger.warning(f"Could not display figure directly. Figure created with {len(fig.axes)} axes.")
                logger.info("Figure is available but display failed - you may need to call plt.show() manually")


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
    import matplotlib
    
    plt = _setup_matplotlib_interactive()

    # Get the figure to display
    if fig is None:
        fig = plt.gcf()  # Get current figure

    logger.debug(f"Showing matplotlib figure with unified display (backend: {matplotlib.get_backend()})")

    try:
        # Make figure current and show
        plt.figure(fig.number)  # Make this figure current
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


def _get_default_layout_for_graph_type(graph_type: str) -> str:
    """
    Get the default layout algorithm based on the original SNT graph type.
    
    Parameters
    ----------
    graph_type : str
        The original SNT graph type (e.g., 'DirectedWeightedGraph', 'SNTGraph')
        
    Returns
    -------
    str
        The recommended layout algorithm name
    """
    from ..config import get_option
    
    # Map graph types to configuration keys
    config_keys = {
        'DirectedWeightedGraph': 'graph.layout.directed_weighted',
        'SNTGraph': 'graph.layout.snt_graph',
        'AnnotationGraph': 'graph.layout.annotation_graph',
    }
    
    # Check for exact matches first
    if graph_type in config_keys:
        return get_option(config_keys[graph_type])
    
    # Check for partial matches (in case of full class names)
    for key, config_key in config_keys.items():
        if key in graph_type:
            return get_option(config_key)
    
    # Default fallback
    return get_option('graph.layout.default')


def _graph_to_matplotlib(graph, **kwargs) -> Figure:
    """
    Convert a NetworkX graph to a matplotlib figure for display.
    
    Parameters
    ----------
    graph : networkx.Graph
        The NetworkX graph to visualize
    **kwargs
        Additional visualization options:
        - layout: str or dict, layout algorithm or position dict (default: auto-detected by graph type)
        - graph_type: str, original SNT graph type for smart defaults (optional)
        - node_color: str or list, node colors (default: 'lightblue')
        - node_size: int or list, node sizes (default: 500)
        - edge_color: str or list, edge colors (default: 'gray')
        - edge_width: float or list, edge widths (default: 2)
        - with_labels: bool, whether to show node labels (default: True)
        - figsize: tuple, figure size (default: (10, 8))
        - title: str, plot title (default: 'NetworkX Graph')
        - seed: int, random seed for layout (default: 42)
        - use_node_positions: bool, use node spatial coordinates if available (default: True)
        
    Returns
    -------
    matplotlib.figure.Figure
        Figure containing the graph visualization
    """
    if not HAS_NETWORKX:
        raise ImportError(ERROR_MISSING_NETWORKX)
    
    plt = _setup_matplotlib_interactive()
    
    # Get visualization parameters with sensible defaults
    graph_type = kwargs.get('graph_type', 'Unknown')
    default_layout = _get_default_layout_for_graph_type(graph_type)
    layout = kwargs.get('layout', default_layout)
    node_color = kwargs.get('node_color', DEFAULT_NODE_COLOR)
    node_size = kwargs.get('node_size', DEFAULT_NODE_SIZE)
    edge_color = kwargs.get('edge_color', 'gray')
    edge_width = kwargs.get('edge_width', 2)
    with_labels = kwargs.get('with_labels', graph_type != 'DirectedWeightedGraph')
    figsize = kwargs.get('figsize', (10, 8))
    title = kwargs.get('title', graph_type)
    seed = kwargs.get('seed', 42)
    use_node_positions = kwargs.get('use_node_positions', True)
    
    # Create figure
    fig, ax = plt.subplots(figsize=figsize)
    
    try:
        # Determine node positions
        if isinstance(layout, dict):
            # Use provided position dictionary
            pos = layout
        elif layout == 'spatial' or (use_node_positions and layout == 'spring'):
            # Try to use spatial coordinates from SWCPoint nodes
            pos = {}
            has_spatial_coords = False
            
            for node in graph.nodes():
                try:
                    # Try to get coordinates from SWCPoint attributes
                    if 'x' in graph.nodes[node] and 'y' in graph.nodes[node]:
                        # Use node attributes if available
                        x = float(graph.nodes[node]['x'])
                        y = float(graph.nodes[node]['y'])
                        pos[node] = (x, y)
                        has_spatial_coords = True
                except Exception as e:
                    logger.debug(f"Could not extract spatial coordinates from node {node}: {e}")
            
            # Fall back to spring layout if no spatial coordinates found
            if not has_spatial_coords or len(pos) != graph.number_of_nodes():
                logger.debug("No spatial coordinates found, using spring layout")
                pos = nx.spring_layout(graph, seed=seed)
        else:
            # Use specified layout algorithm
            if layout == 'spring':
                pos = nx.spring_layout(graph, seed=seed)
            elif layout == 'circular':
                pos = nx.circular_layout(graph)
            elif layout == 'random':
                pos = nx.random_layout(graph, seed=seed)
            elif layout == 'shell':
                pos = nx.shell_layout(graph)
            elif layout == 'kamada_kawai':
                pos = nx.kamada_kawai_layout(graph)
            elif layout == 'planar':
                try:
                    pos = nx.planar_layout(graph)
                except nx.NetworkXException:
                    logger.warning("Graph is not planar, falling back to spring layout")
                    pos = nx.spring_layout(graph, seed=seed)
            else:
                logger.warning(f"Unknown layout '{layout}', using spring layout")
                pos = nx.spring_layout(graph, seed=seed)
        
        # Handle node colors based on attributes
        if node_color == 'by_type' and graph.number_of_nodes() > 0:
            # Color nodes by SWC type if available
            node_colors = []
            # see Path#getSWCcolor()
            type_colors = {1: 'blue', 2: 'red', 3: 'green', 4: 'cyan', 5: 'yellow', 6: 'orange', 7: 'pink', 8: 'goldenrod'}
            
            for node in graph.nodes():
                try:
                    if hasattr(node, 'getType'):
                        node_type = int(node.getType())
                    elif 'type' in graph.nodes[node]:
                        node_type = int(graph.nodes[node]['type'])
                    else:
                        node_type = 1  # Default
                    
                    node_colors.append(type_colors.get(node_type, 'lightblue'))
                except (AttributeError, TypeError, RuntimeError):
                    node_colors.append('lightblue')
            
            node_color = node_colors
        elif node_color == 'by_annotation' and graph.number_of_nodes() > 0:
            # Color nodes by BrainAnnotation color if available
            node_colors = []
            
            for node in graph.nodes():
                try:
                    # Try to get color from BrainAnnotation
                    if 'color_hex' in graph.nodes[node]:
                        node_colors.append(graph.nodes[node]['color_hex'])
                    elif 'color_rgb' in graph.nodes[node]:
                        rgb = graph.nodes[node]['color_rgb']
                        hex_color = f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"
                        node_colors.append(hex_color)
                    elif hasattr(node, 'color'):
                        color = node.color()
                        from .utils import _extract_color_attributes
                        color_attrs = _extract_color_attributes(color, "color")
                        if 'color_hex' in color_attrs:
                            node_colors.append(color_attrs['color_hex'])
                        else:
                            node_colors.append('lightblue')
                    else:
                        node_colors.append('lightblue')
                except (AttributeError, TypeError, RuntimeError):
                    node_colors.append('lightblue')
            
            node_color = node_colors
        
        # Handle node sizes based on radius if available
        if node_size == 'by_radius' and graph.number_of_nodes() > 0:
            node_sizes = []
            base_size = 300
            
            for node in graph.nodes():
                try:
                    if hasattr(node, 'getRadius'):
                        radius = float(node.getRadius())
                    elif 'radius' in graph.nodes[node]:
                        radius = float(graph.nodes[node]['radius'])
                    else:
                        radius = 1.0  # Default
                    
                    # Scale radius to reasonable node size
                    node_sizes.append(base_size * max(0.5, radius))
                except (AttributeError, TypeError, RuntimeError):
                    node_sizes.append(base_size)
            
            node_size = node_sizes
        
        # Handle edge widths based on weight if available
        if edge_width == 'by_weight' and graph.number_of_edges() > 0:
            edge_widths = []
            
            for edge in graph.edges():
                try:
                    weight = graph.edges[edge].get('weight', 1.0)
                    # Scale weight to reasonable line width
                    edge_widths.append(max(0.5, min(5.0, float(weight))))
                except (AttributeError, TypeError, RuntimeError):
                    edge_widths.append(2.0)
            
            edge_width = edge_widths
        
        # Draw the graph
        nx.draw(graph, pos,
                node_color=node_color,
                node_size=node_size,
                edge_color=edge_color,
                width=edge_width,
                with_labels=with_labels,
                ax=ax,
                arrows=True,           # Ensure arrows are drawn for directed graphs
                arrowsize=10,          # Smaller arrows to reduce visual clutter
                arrowstyle='->'        # Simple arrow style
                )
        
        # Add title and labels
        ax.set_title(title, fontsize=14, fontweight='normal')
        
        # Add graph statistics as text
        stats_text = f"Nodes: {graph.number_of_nodes()}, Edges: {graph.number_of_edges()}"
        if hasattr(graph, 'is_directed') and graph.is_directed():
            stats_text += " (Directed)"
        
        ax.text(0.02, 0.98, stats_text, transform=ax.transAxes, 
                verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
        
        # Add colorbar for edge weights if they vary
        if isinstance(edge_width, list) and len(set(edge_width)) > 1:
            # Create a simple legend for edge weights
            legend_text = "Edge width ∝ weight"
            ax.text(0.02, 0.02, legend_text, transform=ax.transAxes,
                    verticalalignment='bottom', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
        
        plt.tight_layout()
        
        logger.info(f"Successfully created NetworkX graph visualization with {graph.number_of_nodes()} nodes and {graph.number_of_edges()} edges")
        return fig
        
    except Exception as e:
        logger.error(f"Failed to create graph visualization: {e}")
        # Create a simple error figure
        ax.text(0.5, 0.5, f'Graph visualization failed:\n{str(e)}', 
                ha='center', va='center', transform=ax.transAxes,
                bbox=dict(boxstyle='round', facecolor='red', alpha=0.3))
        ax.set_title(title)
        return fig


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
        Display parameters including:
        - metadata: dict, optional metadata from SNTObject conversion
        - title: str, optional title override
        - is_rgb: bool, optional RGB flag override
        - add_colorbar: bool, whether to add colorbar (default: True for grayscale)
        
    Returns
    -------
    SNTObject or None
        SNTObject with display result or None on failure
    """
    # Handle different dimensionalities
    original_shape = data.shape
    title = kwargs.get('title', None)
    
    # Check for metadata-based RGB detection (most reliable)
    metadata = kwargs.get('metadata', {})
    is_rgb = metadata.get('is_rgb', False)
    
    # Use metadata title if available and no title override provided
    if not title and 'image_title' in metadata:
        title = metadata['image_title']
    
    # If no metadata available, fall back to manual override or shape detection
    if not is_rgb and 'is_rgb' in kwargs:
        is_rgb = kwargs['is_rgb']
    elif not is_rgb and data.ndim == 3 and data.shape[2] in [3, 4]:
        # Fallback: shape-based detection (less reliable)
        is_rgb = True
        logger.warning(f"Using fallback RGB detection based on shape {data.shape}. "
                      f"Consider using metadata-based detection for reliability.")

    if data.ndim == 3:
        if is_rgb:
            # RGB/RGBA data - display as-is
            img_data = data
            logger.debug(f"Displaying RGB/RGBA data: shape={img_data.shape}")
            if not title:
                title = f"RGB {source_type}"
        else:
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

    # Use the new standardized figure creation
    cmap = kwargs.get('cmap', DEFAULT_CMAP)
    add_colorbar = kwargs.get('add_colorbar', True)
    
    fig, ax, im = _create_standard_figure(
        data=img_data,
        title=title,
        cmap=cmap,
        add_colorbar=add_colorbar,
        is_rgb=is_rgb,
        **kwargs
    )

    # Use unified display system
    if _show_matplotlib_figure(fig):
        logger.info(f"Successfully displayed {source_type} data as {'RGB' if is_rgb else 'grayscale'} image: '{title}'")
        return {
            'type': Figure,
            'data': data,
            'metadata': {
                'source_type': source_type,
                'original_shape': original_shape,
                'displayed_shape': img_data.shape,
                'title': title,
                'is_rgb': is_rgb,
                **metadata  # Include original metadata
            },
            'error': None
        }
    else:
        logger.warning(f"Failed to display {source_type} figure")
        return None


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
    plt = _setup_matplotlib_interactive()

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
                # Check for missing values
                if hasattr(np, 'isnan'):
                    missing = np.sum(np.isnan(data)) if np.issubdtype(data.dtype, np.floating) else 0
                else:
                    missing = 0
                var_info.append(f"{var}\n({data.dtype})")
                missing_counts.append(missing)
            except (AttributeError, TypeError, RuntimeError):
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
            except (AttributeError, TypeError, RuntimeError):
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
    plt = _setup_matplotlib_interactive()

    try:
        n_vars = len(display_vars)
        n_cols = min(3, n_vars)
        n_rows = (n_vars + n_cols - 1) // n_cols

        fig, axes = plt.subplots(n_rows, n_cols, figsize=figsize)
        fig.suptitle(title, fontsize=14)

        # Ensure axes is always a list
        if n_vars == 1:
            axes = [axes]
        elif n_rows == 1:
            axes = axes if isinstance(axes, (list, np.ndarray)) else [axes]
        else:
            axes = axes.flatten()

        for i, var in enumerate(display_vars):
            ax = axes[i]
            try:
                data = dataset[var].values
                
                # Flatten multi-dimensional data
                if data.ndim > 1:
                    data = data.flatten()
                
                if np.issubdtype(data.dtype, np.number):
                    # Numeric data - histogram
                    ax.hist(data[~np.isnan(data)], bins=30, alpha=0.7, edgecolor='black')
                    ax.set_title(f'{var} Distribution')
                    ax.set_xlabel(var)
                    ax.set_ylabel('Frequency')
                else:
                    # Non-numeric data - value counts
                    unique, counts = np.unique(data, return_counts=True)
                    ax.bar(range(len(unique)), counts)
                    ax.set_title(f'{var} Value Counts')
                    ax.set_xlabel(var)
                    ax.set_ylabel('Count')
                    if len(unique) <= 10:
                        ax.set_xticks(range(len(unique)))
                        ax.set_xticklabels(unique, rotation=45)
                
                ax.grid(True, alpha=0.3)
                
            except Exception as e:
                logger.debug(f"Could not plot distribution for {var}: {e}")
                ax.text(0.5, 0.5, f'Could not plot\n{var}', 
                       ha='center', va='center', transform=ax.transAxes)

        # Hide unused subplots
        for i in range(n_vars, len(axes)):
            axes[i].set_visible(False)

        plt.tight_layout()

        # Use unified display system
        if _show_matplotlib_figure(fig):
            logger.info("Successfully displayed dataset distribution plots")
            return True
        else:
            logger.warning("Failed to display dataset distribution plots")
            return False

    except Exception as e:
        logger.error(f"Failed to create distribution plots: {e}")
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
    plt = _setup_matplotlib_interactive()

    try:
        # Filter to numeric variables only
        numeric_vars = []
        corr_data = {}
        
        for var in display_vars:
            try:
                data = dataset[var].values
                if np.issubdtype(data.dtype, np.number):
                    # Flatten multi-dimensional arrays
                    if data.ndim > 1:
                        data = data.flatten()
                    corr_data[var] = data
                    numeric_vars.append(var)
            except Exception as e:
                logger.debug(f"Could not process variable {var}: {e}")

        if len(numeric_vars) < 2:
            logger.warning("Need at least 2 numeric variables for correlation plot")
            return False

        # Create correlation matrix
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
                             ha="center", va="center", color="black" if abs(corr_matrix.iloc[i, j]) < 0.5 else "white")

        ax.set_title(title)
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


__version__ = "0.1.0-refactoring"
__refactoring_phase__ = "Phase 4: Visual Functions Nearly Complete"