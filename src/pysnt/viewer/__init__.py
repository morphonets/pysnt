"""
This module provides convenient access to
`SNT's viewer classes <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/viewer/package-summary.html>`__.
"""

import logging
import scyjava
from typing import Dict, Any, List, Callable

from ..common_module import setup_module_classes

logger = logging.getLogger(__name__)

# Curated classes - always available for direct import
CURATED_CLASSES = [
    "MultiViewer2D", "MultiViewer3D",
    "Viewer2D", "Viewer3D"
]

# Extended classes - available via get_class() after discovery
EXTENDED_CLASSES = [
    "Annotation3D",
    "Bvv",
    "ColorTableMapper",
    "GraphViewer"
]


# Dynamic placeholder classes will be created automatically by setup_module_classes()

# Setup common module functionality
_module_funcs = setup_module_classes(
    package_name="sc.fiji.snt.viewer",
    curated_classes=CURATED_CLASSES,
    extended_classes=EXTENDED_CLASSES,
    globals_dict=globals()
)

# Import functions into module namespace
get_available_classes = _module_funcs['get_available_classes']  # type: Callable[[], List[str]]
get_class = _module_funcs['get_class']  # type: Callable[[str], Any]
list_classes = _module_funcs['list_classes']  # type: Callable[[], None]
get_curated_classes = _module_funcs['get_curated_classes']  # type: Callable[[], List[str]]
get_extended_classes = _module_funcs['get_extended_classes']  # type: Callable[[], List[str]]

# Create module-level __getattr__ and __dir__
__getattr__ = _module_funcs['create_getattr']('pysnt.viewer')
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
    "MultiViewer2D",
    "MultiViewer3D", 
    "Viewer2D",
    "Viewer3D",
]