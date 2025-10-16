"""
This module provides convenient access to
`SNT's analysis classes <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/analysis/package-summary.html>`__.
"""

import logging
import scyjava
from typing import Dict, Any, List

from ..common_module import setup_module_classes

logger = logging.getLogger(__name__)

# Curated classes - always available for direct import
CURATED_CLASSES = [
    "ConvexHull2D", "ConvexHull3D",
    "TreeStatistics", "MultiTreeStatistics",
    "SNTChart", "SNTTable"
]

# Extended classes - available via get_class() after discovery
EXTENDED_CLASSES = [
    "AbstractConvexHull", "AnalysisUtils", "AnnotationMapper",
    "CircularModels","ColorMapper", "ConvexHullAnalyzer",
    "GroupedTreeStatistics",
    "MultiTreeColorMapper",
    "NodeColorMapper", "NodeProfiler", "NodeStatistics",
    "PathProfiler", "PathStatistics", "PathStraightener", "PCAnalyzer", "PersistenceAnalyzer", "ProfileProcessor",
    "RoiConverter", "RootAngleAnalyzer",
    "ShollAnalyzer", "SkeletonConverter", "StrahlerAnalyzer",
    "TreeColorMapper"
]

# Placeholder classes for IDE support - will be replaced with Java classes

class TreeStatistics:
    """
    """
    def getCableLength(self):
        """Placeholder method. Call pysnt.initialize() first."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

    def getSummaryStats(self):
        """Placeholder method. Call pysnt.initialize() first."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

    def getHistogram(self, arg0):
        """Placeholder method. Call pysnt.initialize() first."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

    def getBranchPoints(self):
        """Placeholder method. Call pysnt.initialize() first."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

    def getTips(self):
        """Placeholder method. Call pysnt.initialize() first."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

    def getNodes(self):
        """Placeholder method. Call pysnt.initialize() first."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

    def getDepth(self):
        """Placeholder method. Call pysnt.initialize() first."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

    def getWidth(self):
        """Placeholder method. Call pysnt.initialize() first."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

    def getHeight(self):
        """Placeholder method. Call pysnt.initialize() first."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

    def __getattr__(self, name: str):
        """Dynamic attribute access for additional Java methods."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

class MultiTreeStatistics:
    """
    This class is a TreeStatistics variant providing comparison
    capabilities for collections of neuronal trees.
    """
    pass

class ConvexHull2D:
    """
    This class computes and analyzes the convex hull of a 2D Tree
    """
    pass

class ConvexHull3D:
    """
    This class computes and analyzes the convex hull of a 3D Tree
    """
    pass

class SNTChart:
    """
    Class for creating analysis charts and plots.
    """
    pass

class SNTTable:
    """
    Class for table creation, manipulation, and display of tabular data.
    """
    pass


# Setup common module functionality
_module_funcs = setup_module_classes(
    package_name="sc.fiji.snt.analysis",
    curated_classes=CURATED_CLASSES,
    extended_classes=EXTENDED_CLASSES,
    globals_dict=globals(),
    placeholder_classes={
        'TreeStatistics': TreeStatistics,
        'MultiTreeStatistics': MultiTreeStatistics,
        'ConvexHull2D': ConvexHull2D,
        'ConvexHull3D': ConvexHull3D,
        'SNTChart': SNTChart,
        'SNTTable': SNTTable
    }
)

# Import functions into module namespace
get_available_classes = _module_funcs['get_available_classes']
get_class = _module_funcs['get_class']
list_classes = _module_funcs['list_classes']
get_curated_classes = _module_funcs['get_curated_classes']
get_extended_classes = _module_funcs['get_extended_classes']

# Import submodules for easy access
from . import growth

# Create module-level __getattr__ and __dir__
__getattr__ = _module_funcs['create_getattr']('pysnt.analysis', submodules=['growth'])
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
    "TreeStatistics",
    "MultiTreeStatistics", 
    "ConvexHull2D",
    "ConvexHull3D",
    "SNTChart",
    "SNTTable",
]