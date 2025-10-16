"""
This module provides convenient access to
`SNT's tracing classes <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/tracing/package-summary.html>`__.
"""

import logging
import scyjava
from typing import Dict, Any, List

from ..common_module import setup_module_classes

logger = logging.getLogger(__name__)

# Curated classes - always available for direct import
CURATED_CLASSES = [
    "SearchThread",
    "TracerThread"
]

# Extended classes - available via get_class() after discovery
EXTENDED_CLASSES = [
    "AbstractSearch",
    "BiSearch", "BiSearchNode",
    "DefaultSearchNode",
    "FillerThread",
    "ManualTracerThread",
    "SearchNode"
]

# Placeholder classes for IDE support - will be replaced with Java classes

class SearchThread:
    """
    SNT's SearchThread class for pathfinding algorithms.
    """
    pass

class TracerThread:
    """
    SNT's TracerThread class for pathfinding algorithms.
    """
    pass


# Setup common module functionality
_module_funcs = setup_module_classes(
    package_name="sc.fiji.snt.tracing",
    curated_classes=CURATED_CLASSES,
    extended_classes=EXTENDED_CLASSES,
    globals_dict=globals(),
    placeholder_classes={
        'SearchThread': SearchThread,
        'TracerThread': TracerThread
    },
    include_interfaces=True  # Include interfaces for tracing
)

# Import functions into module namespace
get_available_classes = _module_funcs['get_available_classes']
get_class = _module_funcs['get_class']
list_classes = _module_funcs['list_classes']
get_curated_classes = _module_funcs['get_curated_classes']
get_extended_classes = _module_funcs['get_extended_classes']

# Create module-level __getattr__ and __dir__
__getattr__ = _module_funcs['create_getattr']('pysnt.tracing')
__dir__ = _module_funcs['create_dir']()


# Static __all__ with curated classes always available
# This ensures IDEs know these symbols are available for import
__all__ = [
    # Functions
    "get_available_classes",
    "get_class", 
    "list_classes",
    "get_curated_classes",
    "get_extended_classes",
    # Constants
    "CURATED_CLASSES",
    "EXTENDED_CLASSES",
    # Curated classes (always available for direct import)
    "SearchThread",
    "TracerThread",
]