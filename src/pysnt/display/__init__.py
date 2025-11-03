"""
PySNT Display Module

Provides unified display functionality for SNT objects, matplotlib figures,
xarray datasets, pandas DataFrames, and other data structures.

This module is organized into submodules:
- core: Main display orchestration and SNT object handling
- visual_display: Matplotlib figures, graphs, and visualizations
- data_display: xarray datasets, pandas DataFrames, and structured data
- utils: Shared utilities and helper functions

The main display function is available directly:
    from pysnt.display import display
"""

# Import main functions from core module
from .core import display

# Import utilities from  utils module
from .utils import (
    _is_snt_object,
    _is_snt_tree,
    _is_snt_path,
    _is_xarray_object,
    _has_pandasgui,
    _extract_display_config,
    _handle_display_error,
    _validate_display_kwargs,
    _hide_axis_decorations,
    _setup_clean_axis,
    _apply_standard_layout,
    _create_subplot_grid,
)
from .utils import register_display_handler

# Main public API
__all__ = [
    "display",
    "register_display_handler",
]
