"""
SNT object converters for PySNT.

This module provides custom converters that transform SNT Java objects into 
Python equivalents (matplotlib figures, xarray datasets, etc.) and handles
their display and visualization.

The converters module is organized into the following submodules:
- core: Base utilities, constants, and factory functions
- extractors: Graph vertex and edge attribute extraction (SNTGraph)
- graph_converters: SNTGraph to NetworkX conversion
- chart_converters: SNTChart to matplotlib conversion
- structured_data_converters: SNTTable/Path/ImagePlus to xarray conversion and metadata extraction
- display: Display and visualization functions
- enhancement: Java object enhancement functionality
"""

import logging
from typing import Any, Dict, List

# Import main public API functions
from .display import display, register_display_handler
from .enhancement import enhance_java_object, auto_enhance_java_objects

# Import structured data converter functions for backward compatibility
from .structured_data_converters import (
    _is_snt_table,
    _convert_snt_table,
    _convert_path_to_xarray,
    _extract_imageplus_metadata
)

# Import graph converter functions for backward compatibility
from .graph_converters import (
    _is_snt_graph,
    _convert_snt_graph,
    _is_directed_weighted_graph,
    _convert_directed_weighted_graph,
    _diagnose_graph_structure,
    _get_default_layout_for_graph_type,
    _graph_to_matplotlib,
    HAS_NETWORKX
)

# Import core types
from .core import SNTObject

logger = logging.getLogger(__name__)

# Try to import scyjava for converter registration
try:
    import scyjava as sj # noqa
    HAS_SCYJAVA = True
except ImportError:
    HAS_SCYJAVA = False
    sj = None

# Define the converters list
SNT_CONVERTERS = []

def _initialize_converters():
    """Initialize the SNT_CONVERTERS list with converter definitions."""
    global SNT_CONVERTERS
    
    if not HAS_SCYJAVA:
        logger.warning("scyjava not available - converter registration disabled")
        return
    
    # Import converter functions
    from .structured_data_converters import _is_snt_table, _convert_snt_table
    from .chart_converters import _is_snt_chart, _convert_snt_chart
    from .graph_converters import _is_snt_graph, _convert_snt_graph
    
    # Define converters
    SNT_CONVERTERS = [
        sj.Converter(
            predicate=_is_snt_table,
            converter=_convert_snt_table,
            name="SNTTable"
        ),
        sj.Converter(
            predicate=_is_snt_chart,
            converter=_convert_snt_chart,
            name="SNTChart"
        ),
        sj.Converter(
            predicate=_is_snt_graph,
            converter=_convert_snt_graph,
            name="SNTGraph"
        )
    ]

def register_snt_converters():
    """
    Register SNT converters with scyjava.
    
    This function registers custom converters that transform SNT Java objects
    into Python equivalents. The converters handle:
    - SNT tables -> xarray datasets
    - SNT charts -> matplotlib figures
    - SNT graphs -> NetworkX graphs
    
    Returns
    -------
    bool
        True if registration succeeded, False otherwise
    """
    if not HAS_SCYJAVA:
        logger.error("scyjava is required for converter registration. Install with: pip install scyjava")
        return False
    
    if not SNT_CONVERTERS:
        _initialize_converters()
    
    try:
        for converter in SNT_CONVERTERS:
            sj.add_py_converter(converter)
            logger.info(f"Registered converter: {converter.name}")
        
        logger.info(f"Successfully registered {len(SNT_CONVERTERS)} SNT converter(s)")
        return True
    
    except Exception as e:
        logger.error(f"Failed to register SNT converters: {e}")
        return False

def list_converters() -> List[Dict[str, Any]]:
    """
    List all registered SNT converters.
    
    Returns
    -------
    List[Dict[str, Any]]
        List of converter information dictionaries containing:
        - name: converter name
        - predicate: predicate function name
        - converter: converter function name
    """
    if not SNT_CONVERTERS:
        _initialize_converters()
    
    converter_info = []
    
    for converter in SNT_CONVERTERS:
        info = {
            'name': converter.name,
            'predicate': converter.predicate.__name__ if hasattr(converter.predicate, '__name__') else str(converter.predicate),
            'converter': converter.converter.__name__ if hasattr(converter.converter, '__name__') else str(converter.converter)
        }
        converter_info.append(info)
    
    return converter_info

# Initialize converters on module import
_initialize_converters()

__version__ = "1.0.0"
__all__ = [
    # Main public API functions
    "display",
    "register_snt_converters",
    "list_converters",
    
    # Enhancement functions
    "enhance_java_object",
    "auto_enhance_java_objects",
    
    # Display registration
    "register_display_handler",
    
    # Converter registration
    "SNT_CONVERTERS",
    
    # Core types
    "SNTObject",
    
    # Structured data converter functions (backward compatibility)
    "_is_snt_table",
    "_convert_snt_table", 
    "_convert_path_to_xarray",
    "_extract_imageplus_metadata",
    
    # Graph converter functions (backward compatibility)
    "_is_snt_graph",
    "_convert_snt_graph",
    "_is_directed_weighted_graph", 
    "_convert_directed_weighted_graph",
    "_diagnose_graph_structure",
    "_get_default_layout_for_graph_type",
    "_graph_to_matplotlib",
    
    # Constants
    "HAS_NETWORKX"
]