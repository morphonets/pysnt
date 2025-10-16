"""
This module provides convenient access to
`SNT's viewer classes <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/viewer/package-summary.html>`__.
"""

import logging
import scyjava
from typing import Dict, Any, List

from ..common_module import setup_module_classes

logger = logging.getLogger(__name__)

# Curated classes - always available for direct import
CURATED_CLASSES = [
    "MultiViewer", "MultiViewer2D", "MultiViewer3D",
    "Viewer2D", "Viewer3D"
]

# Extended classes - available via get_class() after discovery
EXTENDED_CLASSES = [
    "Annotation3D",
    "Bvv",
    "ColorTableMapper",
    "GraphViewer"
]

# Placeholder classes for IDE support - will be replaced with Java classes

class Viewer2D:
    """
    SNT's Reconstruction Plotter.
    """
    pass

class Viewer3D:
    """
    SNT's Reconstruction Viewer.
    """
    pass

class MultiViewer:
    """
    SNT's Multipanel Viewers.
    """
    pass


# Setup common module functionality
_module_funcs = setup_module_classes(
    package_name="sc.fiji.snt.viewer",
    curated_classes=CURATED_CLASSES,
    extended_classes=EXTENDED_CLASSES,
    globals_dict=globals(),
    placeholder_classes={
        'Viewer2D': Viewer2D,
        'Viewer3D': Viewer3D,
        'MultiViewer': MultiViewer
    }
)

# Import functions into module namespace
get_available_classes = _module_funcs['get_available_classes']
get_class = _module_funcs['get_class']
list_classes = _module_funcs['list_classes']
get_curated_classes = _module_funcs['get_curated_classes']
get_extended_classes = _module_funcs['get_extended_classes']

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
    "Viewer2D",
    "Viewer3D",
    "MultiViewer",
]