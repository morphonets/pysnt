"""
This module provides convenient access to
`SNT's growth analysis classes <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/analysis/growth/package-summary.html>`__.
"""

import logging
import scyjava
from typing import Dict, Any, List

from ...common_module import setup_module_classes

logger = logging.getLogger(__name__)

# Curated classes - always available for direct import
CURATED_CLASSES = [
    "GrowthAnalyzer", "GrowthAnalysisResults"
]

# Extended classes - available via get_class() after discovery
EXTENDED_CLASSES = [
    "NeuriteGrowthData"
]

# Placeholder classes for IDE support - will be replaced with Java classes

class GrowthAnalyzer:
    """
    Core analyzer for time-lapse growth analysis of neuronal paths
    """
    pass


class GrowthAnalysisResults:
    """
    Container class for growth analysis results from GrowthAnalyzer
    """
    pass


# Setup common module functionality
_module_funcs = setup_module_classes(
    package_name="sc.fiji.snt.analysis.growth",
    curated_classes=CURATED_CLASSES,
    extended_classes=EXTENDED_CLASSES,
    globals_dict=globals(),
    placeholder_classes={
        'GrowthAnalyzer': GrowthAnalyzer,
        'GrowthAnalysisResults': GrowthAnalysisResults
    }
)

# Import functions into module namespace
get_available_classes = _module_funcs['get_available_classes']
get_class = _module_funcs['get_class']
list_classes = _module_funcs['list_classes']
get_curated_classes = _module_funcs['get_curated_classes']
get_extended_classes = _module_funcs['get_extended_classes']

# Create module-level __getattr__ and __dir__
__getattr__ = _module_funcs['create_getattr']('pysnt.analysis.growth')
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
    "GrowthAnalyzer",
    "GrowthAnalysisResults",
]