"""
Type stubs for graph_converters.py

Auto-generated stub file.
"""

from typing import Any
from matplotlib.figure import Figure

from pysnt.converters.core import SNTObject

HAS_NETWORKX: bool
HAS_MATPLOTLIB: bool
DEFAULT_GRAPH_LAYOUTS: dict

def _is_snt_graph(obj: Any) -> bool: ...

def _is_directed_weighted_graph(obj: Any) -> bool: ...

def _diagnose_graph_structure(nx_graph: Any, graph_type: str = "Unknown") -> None: ...

def _convert_snt_graph(graph: Any, **kwargs: Any) -> SNTObject: ...

def _convert_directed_weighted_graph(graph: Any, **kwargs: Any) -> SNTObject: ...

def _get_default_layout_for_graph_type(graph_type: str) -> str: ...

def _graph_to_matplotlib(graph: Any, **kwargs: Any) -> Figure: ...
