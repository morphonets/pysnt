"""
This module provides convenient access to
`SNT's io classes <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/io/package-summary.html>`__.
"""

import logging
import scyjava
from typing import Dict, Any, List

from ..common_module import setup_module_classes  # Adjust import path as needed

logger = logging.getLogger(__name__)

# Curated classes - always available for direct import
# These are the most commonly used classes that users will import directly
CURATED_CLASSES = [
    "FlyCircuitLoader",
    "InsectBrainLoader",
    "MouseLightLoader",
    "MouseLightQuerier",
    "NeuroMorphoLoader",
    "RemoteSWCLoader",
    "WekaModelLoader",
]

# Extended classes - available via get_class() after discovery
# These are less commonly used classes that are loaded on-demand
EXTENDED_CLASSES = [
    "NDFImporter",
    "RemoteSWCLoader",
    "SWCExportException",
    "TracesFileFormatException",
]

# =============================================================================
# MODULE SETUP - USUALLY NO CHANGES NEEDED
# =============================================================================

# Setup common module functionality
_module_funcs = setup_module_classes(
    package_name="sc.fiji.snt.io",
    curated_classes=CURATED_CLASSES,
    extended_classes=EXTENDED_CLASSES,
    globals_dict=globals(),
    include_interfaces=True,
)

# Import functions into module namespace
get_available_classes = _module_funcs["get_available_classes"]
get_class = _module_funcs["get_class"]
list_classes = _module_funcs["list_classes"]
get_curated_classes = _module_funcs["get_curated_classes"]
get_extended_classes = _module_funcs["get_extended_classes"]

# Create module-level __getattr__ and __dir__
__getattr__ = _module_funcs["create_getattr"]("pysnt.io")
__dir__ = _module_funcs["create_dir"]()


# Static __all__ with curated classes always available
# This ensures IDEs know these symbols are available for import
__all__ = [
    # Functions (standard for all modules)
    "get_available_classes",
    "get_class",
    "list_classes",
    "get_curated_classes",
    "get_extended_classes",
    # Constants (standard for all modules)
    "CURATED_CLASSES",
    "EXTENDED_CLASSES",
    # Curated classes (will be populated by placeholder generation)
] + CURATED_CLASSES
