"""
Type stubs for visual_display.py

Auto-generated stub file.
"""

from typing import Any, Dict, List, Optional, Union, Callable

logger: Any
def _display_matplotlib_figure(fig: Figure, **kwargs: Any) -> None: ...

def _show_matplotlib_figure(fig: Any, **kwargs: Any) -> bool: ...

def _get_default_layout_for_graph_type(graph_type: str) -> str: ...

def _graph_to_matplotlib(graph: Any, **kwargs: Any) -> Figure: ...

def _display_array_data(data: Any, source_type: Any, **kwargs: Any) -> Any: ...

def _create_dataset_summary_plot(dataset: Any, display_vars: List[str], title: str, figsize: tuple) -> bool: ...

def _create_dataset_distribution_plot(dataset: Any, display_vars: List[str], title: str, figsize: tuple) -> bool: ...

def _create_dataset_correlation_plot(dataset: Any, display_vars: List[str], title: str, figsize: tuple) -> bool: ...

__version__: Any
__refactoring_phase__: Any