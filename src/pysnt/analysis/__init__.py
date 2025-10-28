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
class ConvexHull2D:
    """
    Curated SNT class from analysis package with method signatures.
    
    Available for direct import after JVM initialization.
    Call pysnt.initialize() before using this class.
    
    See `analysis_ConvexHull2D_javadoc`_.
    
    .. _analysis_ConvexHull2D_javadoc: https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/analysis/ConvexHull2D.html
    """
    
    def __new__(cls, *args, **kwargs):
        """Smart constructor that redirects to real Java class if available."""
        # Try to get the real Java class
        try:
            # Access the module functions that were set up
            import pysnt.analysis
            if hasattr(pysnt.analysis, '_module_funcs'):
                module_funcs = pysnt.analysis._module_funcs
                if "_curated_classes" in module_funcs:
                    curated_classes = module_funcs["_curated_classes"]
                    if "ConvexHull2D" in curated_classes and curated_classes["ConvexHull2D"] is not None:
                        # We have the real Java class, use it instead
                        real_class = curated_classes["ConvexHull2D"]
                        return real_class(*args, **kwargs)
        except Exception:
            pass
        
        # No real class available, show error
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")
    
    def __getattr__(self, name: str):
        """Dynamic attribute access for Java methods."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

class ConvexHull3D:
    """
    Curated SNT class from analysis package with method signatures.
    
    Available for direct import after JVM initialization.
    Call pysnt.initialize() before using this class.
    
    See `analysis_ConvexHull3D_javadoc`_.
    
    .. _analysis_ConvexHull3D_javadoc: https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/analysis/ConvexHull3D.html
    """
    
    def __new__(cls, *args, **kwargs):
        """Smart constructor that redirects to real Java class if available."""
        # Try to get the real Java class
        try:
            # Access the module functions that were set up
            import pysnt.analysis
            if hasattr(pysnt.analysis, '_module_funcs'):
                module_funcs = pysnt.analysis._module_funcs
                if "_curated_classes" in module_funcs:
                    curated_classes = module_funcs["_curated_classes"]
                    if "ConvexHull3D" in curated_classes and curated_classes["ConvexHull3D"] is not None:
                        # We have the real Java class, use it instead
                        real_class = curated_classes["ConvexHull3D"]
                        return real_class(*args, **kwargs)
        except Exception:
            pass
        
        # No real class available, show error
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")
    
    def __getattr__(self, name: str):
        """Dynamic attribute access for Java methods."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

class TreeStatistics:
    """
    Curated SNT class from analysis package with method signatures.
    
    Available for direct import after JVM initialization.
    Call pysnt.initialize() before using this class.
    
    See `analysis_TreeStatistics_javadoc`_.
    
    .. _analysis_TreeStatistics_javadoc: https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/analysis/TreeStatistics.html
    """
    
    def __new__(cls, *args, **kwargs):
        """Smart constructor that redirects to real Java class if available."""
        # Try to get the real Java class
        try:
            # Access the module functions that were set up
            import pysnt.analysis
            if hasattr(pysnt.analysis, '_module_funcs'):
                module_funcs = pysnt.analysis._module_funcs
                if "_curated_classes" in module_funcs:
                    curated_classes = module_funcs["_curated_classes"]
                    if "TreeStatistics" in curated_classes and curated_classes["TreeStatistics"] is not None:
                        # We have the real Java class, use it instead
                        real_class = curated_classes["TreeStatistics"]
                        return real_class(*args, **kwargs)
        except Exception:
            pass
        
        # No real class available, show error
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")
    
    def __getattr__(self, name: str):
        """Dynamic attribute access for Java methods."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

class MultiTreeStatistics:
    """
    Curated SNT class from analysis package with method signatures.
    
    Available for direct import after JVM initialization.
    Call pysnt.initialize() before using this class.
    
    See `analysis_MultiTreeStatistics_javadoc`_.
    
    .. _analysis_MultiTreeStatistics_javadoc: https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/analysis/MultiTreeStatistics.html
    """
    
    def __new__(cls, *args, **kwargs):
        """Smart constructor that redirects to real Java class if available."""
        # Try to get the real Java class
        try:
            # Access the module functions that were set up
            import pysnt.analysis
            if hasattr(pysnt.analysis, '_module_funcs'):
                module_funcs = pysnt.analysis._module_funcs
                if "_curated_classes" in module_funcs:
                    curated_classes = module_funcs["_curated_classes"]
                    if "MultiTreeStatistics" in curated_classes and curated_classes["MultiTreeStatistics"] is not None:
                        # We have the real Java class, use it instead
                        real_class = curated_classes["MultiTreeStatistics"]
                        return real_class(*args, **kwargs)
        except Exception:
            pass
        
        # No real class available, show error
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")
    
    def __getattr__(self, name: str):
        """Dynamic attribute access for Java methods."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

class SNTChart:
    """
    Curated SNT class from analysis package with method signatures.
    
    Available for direct import after JVM initialization.
    Call pysnt.initialize() before using this class.
    
    See `analysis_SNTChart_javadoc`_.
    
    .. _analysis_SNTChart_javadoc: https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/analysis/SNTChart.html
    """
    
    def __new__(cls, *args, **kwargs):
        """Smart constructor that redirects to real Java class if available."""
        # Try to get the real Java class
        try:
            # Access the module functions that were set up
            import pysnt.analysis
            if hasattr(pysnt.analysis, '_module_funcs'):
                module_funcs = pysnt.analysis._module_funcs
                if "_curated_classes" in module_funcs:
                    curated_classes = module_funcs["_curated_classes"]
                    if "SNTChart" in curated_classes and curated_classes["SNTChart"] is not None:
                        # We have the real Java class, use it instead
                        real_class = curated_classes["SNTChart"]
                        return real_class(*args, **kwargs)
        except Exception:
            pass
        
        # No real class available, show error
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")
    
    def __getattr__(self, name: str):
        """Dynamic attribute access for Java methods."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

class SNTTable:
    """
    Curated SNT class from analysis package with method signatures.
    
    Available for direct import after JVM initialization.
    Call pysnt.initialize() before using this class.
    
    See `analysis_SNTTable_javadoc`_.
    
    .. _analysis_SNTTable_javadoc: https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/analysis/SNTTable.html
    """
    
    def __new__(cls, *args, **kwargs):
        """Smart constructor that redirects to real Java class if available."""
        # Try to get the real Java class
        try:
            # Access the module functions that were set up
            import pysnt.analysis
            if hasattr(pysnt.analysis, '_module_funcs'):
                module_funcs = pysnt.analysis._module_funcs
                if "_curated_classes" in module_funcs:
                    curated_classes = module_funcs["_curated_classes"]
                    if "SNTTable" in curated_classes and curated_classes["SNTTable"] is not None:
                        # We have the real Java class, use it instead
                        real_class = curated_classes["SNTTable"]
                        return real_class(*args, **kwargs)
        except Exception:
            pass
        
        # No real class available, show error
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")
    
    def __getattr__(self, name: str):
        """Dynamic attribute access for Java methods."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

# Setup common module functionality
_module_funcs = setup_module_classes(
    package_name="sc.fiji.snt.analysis",
    curated_classes=CURATED_CLASSES,
    extended_classes=EXTENDED_CLASSES,
    globals_dict=globals()
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