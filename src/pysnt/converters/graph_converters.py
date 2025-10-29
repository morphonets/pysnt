"""
SNT graph to NetworkX conversion functionality.

This module converts SNT graph objects to NetworkX graphs, including:
- Graph predicate functions for type detection
- Graph converter functions for different graph types
- Graph utility functions for structure analysis
- Graph-specific constants and helpers

Dependencies: core.py, extractors.py
"""

import logging
from typing import Any

try:
    import networkx as nx  # noqa

    HAS_NETWORKX = True
except ImportError:
    HAS_NETWORKX = False
    nx = None

try:
    import matplotlib.pyplot as plt
    from matplotlib.figure import Figure

    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False
    plt = None
    Figure = None

from .core import (
    _create_converter_result,
    _create_error_result,
    JavaTypeDetector,
    ERROR_MISSING_NETWORKX,
    SNTObject,
)
from .extractors import (
    _VERTEX_EXTRACTORS,
    _EDGE_EXTRACTORS,
    _detect_vertex_type,
    _detect_edge_type,
)

logger = logging.getLogger(__name__)

# Graph layout defaults
DEFAULT_GRAPH_LAYOUTS = {
    "SWCPoint": "spring",
    "BrainAnnotation": "circular",
    "Unknown": "spring",
}


def _is_snt_graph(obj: Any) -> bool:
    """Check if object is any SNTGraph."""
    try:
        return JavaTypeDetector.matches_pattern(
            obj,
            class_patterns=["SNTGraph", "Graph"],
            required_methods=["vertexSet", "edgeSet", "getEdgeSource", "getEdgeTarget"],
        )
    except (AttributeError, TypeError, RuntimeError) as e:
        logger.debug(f"SNTGraph predicate: FAILED for {type(obj)} - {e}")
        return False


def _is_directed_weighted_graph(obj: Any) -> bool:
    """Check if object is a DirectedWeightedGraph."""
    try:
        return JavaTypeDetector.matches_pattern(
            obj,
            class_patterns=["DirectedWeightedGraph"],
            required_methods=["vertexSet", "edgeSet", "getEdgeSource", "getEdgeTarget"],
        )
    except (AttributeError, TypeError, RuntimeError) as e:
        logger.debug(f"DirectedWeightedGraph predicate: FAILED for {type(obj)} - {e}")
        return False


def _diagnose_graph_structure(nx_graph, graph_type: str = "Unknown") -> None:
    """
    Diagnose and log information about graph structure for debugging.

    Parameters
    ----------
    nx_graph : networkx.Graph
        The NetworkX graph to diagnose
    graph_type : str
        Type of the graph for context
    """
    if not HAS_NETWORKX:
        return

    logger.info(f"Graph structure diagnosis for {graph_type}:")
    logger.info(f"  Nodes: {nx_graph.number_of_nodes()}")
    logger.info(f"  Edges: {nx_graph.number_of_edges()}")
    logger.info(f"  Directed: {nx_graph.is_directed()}")

    # Check for self-loops
    self_loops = list(nx.selfloop_edges(nx_graph))
    logger.info(f"  Self-loops: {len(self_loops)}")
    if self_loops:
        logger.warning(
            f"  Self-loop edges: {self_loops[:5]}{'...' if len(self_loops) > 5 else ''}"
        )

    # Check for multiple edges between same nodes
    if hasattr(nx_graph, "is_multigraph") and not nx_graph.is_multigraph():
        # For simple graphs, check for potential issues
        edge_list = list(nx_graph.edges())
        unique_edges = set(edge_list)
        if len(edge_list) != len(unique_edges):
            logger.warning(
                f"  Duplicate edges detected: {len(edge_list) - len(unique_edges)} duplicates"
            )

    # Check connectivity
    if nx_graph.number_of_nodes() > 0:
        if nx_graph.is_directed():
            is_connected = nx.is_weakly_connected(nx_graph)
            logger.info(f"  Weakly connected: {is_connected}")
        else:
            is_connected = nx.is_connected(nx_graph)
            logger.info(f"  Connected: {is_connected}")


def _convert_snt_graph(graph: Any, **kwargs) -> SNTObject:
    """
    Generic converter for SNTGraph objects to NetworkX graphs.

    This converter uses a plugin system with vertex and edge extractors
    to handle different SNTGraph subtypes (DirectedWeightedGraph, AnnotationGraph, etc.).

    Parameters
    ----------
    graph : SNTGraph
        Any SNTGraph object (DirectedWeightedGraph, AnnotationGraph, etc.)
    **kwargs
        Additional conversion options:
        - include_metadata: bool, whether to include graph metadata (default: True)
        - node_attributes: list, node attributes to extract (default: auto-detected)
        - edge_attributes: list, edge attributes to extract (default: auto-detected)
        - vertex_extractor: VertexExtractor, custom vertex extractor
        - edge_extractor: EdgeExtractor, custom edge extractor
        - layout: str, layout algorithm for positioning (default: auto-detected)
        - remove_self_loops: bool, whether to remove self-loops (default: True)

    Returns
    -------
    SNTObject
        Dictionary containing:
        - type: networkx.DiGraph
        - data: NetworkX DiGraph with extracted attributes
        - metadata: Graph metadata including source type, vertex/edge types, etc.
        - error: None if successful, Exception if failed
    """
    if not HAS_NETWORKX:
        error = ImportError(ERROR_MISSING_NETWORKX)
        return _create_error_result(nx.DiGraph if nx else type(None), error, "SNTGraph")

    try:
        # Extract options
        include_metadata = kwargs.get("include_metadata", True)
        node_attributes = kwargs.get("node_attributes", None)
        edge_attributes = kwargs.get("edge_attributes", None)
        remove_self_loops = kwargs.get("remove_self_loops", True)

        # Detect vertex and edge types
        vertex_type = _detect_vertex_type(graph)
        edge_type = _detect_edge_type(graph)

        # Get extractors
        vertex_extractor = kwargs.get("vertex_extractor") or _VERTEX_EXTRACTORS.get(
            vertex_type
        )
        edge_extractor = kwargs.get("edge_extractor") or _EDGE_EXTRACTORS.get(edge_type)

        # Use default attributes if not specified
        if node_attributes is None and vertex_extractor:
            node_attributes = vertex_extractor.get_default_attributes()
        if edge_attributes is None and edge_extractor:
            edge_attributes = edge_extractor.get_default_attributes()

        # Create NetworkX graph (assume directed for SNT graphs)
        nx_graph = nx.DiGraph()

        # Add vertices with attributes
        vertices = graph.vertexSet()
        for vertex in vertices:
            # Extract vertex attributes
            vertex_attrs = {}
            if vertex_extractor and node_attributes:
                vertex_attrs = vertex_extractor.extract_attributes(
                    vertex, node_attributes
                )

            # Use vertex object as node ID (NetworkX handles hashable objects)
            nx_graph.add_node(vertex, **vertex_attrs)

        # Add edges with attributes
        edges = graph.edgeSet()
        for edge in edges:
            source = graph.getEdgeSource(edge)
            target = graph.getEdgeTarget(edge)

            # Skip self-loops if requested
            if remove_self_loops and source == target:
                logger.debug(f"Skipping self-loop edge: {source} -> {target}")
                continue

            # Extract edge attributes
            edge_attrs = {}
            if edge_extractor and edge_attributes:
                edge_attrs = edge_extractor.extract_attributes(edge, edge_attributes)

            nx_graph.add_edge(source, target, **edge_attrs)

        # Prepare metadata
        metadata = {
            "vertex_type": vertex_type,
            "edge_type": edge_type,
            "vertex_count": len(vertices),
            "edge_count": len(edges),
            "is_directed": True,
            "layout": kwargs.get(
                "layout", _get_default_layout_for_graph_type(vertex_type)
            ),
        }

        if include_metadata:
            # Add graph structure diagnosis
            _diagnose_graph_structure(nx_graph, f"{vertex_type} Graph")

        return _create_converter_result(nx_graph, source_type="SNTGraph", **metadata)

    except Exception as e:
        logger.error(f"Failed to convert SNTGraph: {e}")
        return _create_error_result(nx.DiGraph, e, "SNTGraph")


def _convert_directed_weighted_graph(graph: Any, **kwargs) -> "SNTObject":
    """
    Convert DirectedWeightedGraph to NetworkX DiGraph.

    This is a specialized converter for DirectedWeightedGraph objects.
    It delegates to the generic _convert_snt_graph function.

    Parameters
    ----------
    graph : DirectedWeightedGraph
        The DirectedWeightedGraph to convert
    **kwargs
        Additional conversion options (passed to _convert_snt_graph)

    Returns
    -------
    SNTObject
        Dictionary containing NetworkX DiGraph and metadata
    """
    # Use the generic converter
    return _convert_snt_graph(graph, **kwargs)


def _get_default_layout_for_graph_type(graph_type: str) -> str:
    """
    Get default layout algorithm for a graph type.

    Parameters
    ----------
    graph_type : str
        The type of graph vertices

    Returns
    -------
    str
        Layout algorithm name
    """
    return DEFAULT_GRAPH_LAYOUTS.get(graph_type, "spring")


def _graph_to_matplotlib(graph, **kwargs) -> Figure:
    """
    Convert a NetworkX graph to a matplotlib figure for display.

    Parameters
    ----------
    graph : networkx.Graph
        The NetworkX graph to visualize
    **kwargs
        Visualization options:
        - layout: str, layout algorithm (default: 'spring')
        - node_size: int, size of nodes (default: 300)
        - node_color: str, color of nodes (default: 'lightblue')
        - figsize: tuple, figure size (default: (8, 6))
        - title: str, figure title

    Returns
    -------
    matplotlib.figure.Figure
        Figure containing the graph visualization
    """
    if not HAS_NETWORKX:
        raise ImportError(ERROR_MISSING_NETWORKX)

    if not HAS_MATPLOTLIB:
        raise ImportError("matplotlib is required for graph visualization")

    # Extract options
    layout_name = kwargs.get("layout", "spring")
    node_size = kwargs.get("node_size", 300)
    node_color = kwargs.get("node_color", "lightblue")
    figsize = kwargs.get("figsize", (8, 6))
    title = kwargs.get("title", "Graph Visualization")

    # Create figure
    fig, ax = plt.subplots(figsize=figsize)

    try:
        # Calculate layout
        if layout_name == "spring":
            pos = nx.spring_layout(graph)
        elif layout_name == "circular":
            pos = nx.circular_layout(graph)
        elif layout_name == "random":
            pos = nx.random_layout(graph)
        else:
            # Default to spring layout
            pos = nx.spring_layout(graph)

        # Draw the graph
        nx.draw(
            graph,
            pos,
            ax=ax,
            node_size=node_size,
            node_color=node_color,
            with_labels=True,
            font_size=8,
            font_weight="bold",
            arrows=True if graph.is_directed() else False,
        )

        ax.set_title(title)

    except Exception as e:
        logger.error(f"Failed to create graph visualization: {e}")
        ax.text(
            0.5,
            0.5,
            f"Graph visualization failed:\n{e}",
            ha="center",
            va="center",
            transform=ax.transAxes,
        )

    return fig
