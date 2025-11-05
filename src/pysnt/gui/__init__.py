"""
This module provides convenient access to
`SNT's GUI classes <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/gui/package-summary.html>`__.

The GUI module contains classes for SNT's graphical user interface components,
including commands, dialogs, and utility classes for GUI operations.
"""

import logging
import scyjava
from typing import Dict, Any, List

from ..common_module import setup_module_classes

logger = logging.getLogger(__name__)

# =============================================================================
# CLASS LISTS
# =============================================================================

# Curated classes - always available for direct import
# These are the most commonly used GUI classes that users will import directly
CURATED_CLASSES = [
    "FigCreatorCmd",  # Command for creating figures
]

# Extended classes - available via get_class() after discovery
# These are less commonly used GUI classes that are loaded on-demand
EXTENDED_CLASSES = [
    # Add additional GUI classes here as they are discovered
    # Examples: "PathManagerDialog", "SettingsPanel", etc.
]

# =============================================================================
# MODULE SETUP
# =============================================================================

# Setup common module functionality
_module_funcs = setup_module_classes(
    package_name="sc.fiji.snt.gui",
    curated_classes=CURATED_CLASSES,
    extended_classes=EXTENDED_CLASSES,
    globals_dict=globals(),
    # Search additional packages for GUI classes
    discovery_packages=["sc.fiji.snt.gui", "sc.fiji.snt.gui.cmds"],
)

# Import functions into module namespace
get_available_classes = _module_funcs['get_available_classes']
get_class = _module_funcs['get_class']
list_classes = _module_funcs['list_classes']
get_curated_classes = _module_funcs['get_curated_classes']
get_extended_classes = _module_funcs['get_extended_classes']

# Create module-level __getattr__ and __dir__
__getattr__ = _module_funcs['create_getattr']('pysnt.gui')
__dir__ = _module_funcs['create_dir']()

# =============================================================================
# SUBMODULE IMPORTS
# =============================================================================

# Import cmds submodule
from . import cmds

# Update __getattr__ to handle submodules
__getattr__ = _module_funcs['create_getattr']('pysnt.gui', submodules=['cmds'])

# =============================================================================
# MODULE EXPORTS
# =============================================================================

# Static __all__ with curated classes always available
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
    # Submodules
    "cmds",
    # Curated classes
] + CURATED_CLASSES