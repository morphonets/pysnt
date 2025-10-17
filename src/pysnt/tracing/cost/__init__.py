"""
This module provides convenient access to
`SNT's cost classes <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/tracing/cost/package-summary.html>`__.
"""

import logging
import scyjava
from typing import Dict, Any, List

from ...common_module import setup_module_classes

logger = logging.getLogger(__name__)

# Curated classes - always available for direct import
# These are the most commonly used classes that users will import directly
CURATED_CLASSES = ["Difference", "DifferenceSq", "OneMinusErf", "Reciprocal"]

# Extended classes - available via get_class() after discovery
# These are less commonly used classes that are loaded on-demand
EXTENDED_CLASSES = ["Cost"]

# Setup common module functionality
_module_funcs = setup_module_classes(
    package_name="sc.fiji.snt.tracing.cost",
    curated_classes=CURATED_CLASSES,
    extended_classes=EXTENDED_CLASSES,
    globals_dict=globals(),
    # Optional parameters (uncomment and modify if needed):
    # discovery_packages=["sc.fiji.snt", "sc.fiji.snt.util"],  # Search multiple packages
    # include_interfaces=True,  # Include Java interfaces (useful for tracing modules)
)

# Import functions into module namespace
get_available_classes = _module_funcs["get_available_classes"]
get_class = _module_funcs["get_class"]
list_classes = _module_funcs["list_classes"]
get_curated_classes = _module_funcs["get_curated_classes"]
get_extended_classes = _module_funcs["get_extended_classes"]

# Create module-level __getattr__ and __dir__
__getattr__ = _module_funcs["create_getattr"]("pysnt.tracing.cost")
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
