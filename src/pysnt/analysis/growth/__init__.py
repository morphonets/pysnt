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
    Curated SNT class from analysis/growth package with method signatures.
    
    Available for direct import after JVM initialization.
    Call pysnt.initialize() before using this class.
    
    See `analysis_growth_GrowthAnalyzer_javadoc`_.
    
    .. _analysis_growth_GrowthAnalyzer_javadoc: https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/analysis/growth/GrowthAnalyzer.html
    """
    
    def __new__(cls, *args, **kwargs):
        """Smart constructor that redirects to real Java class if available."""
        # Try to get the real Java class
        try:
            # Access the module functions that were set up
            import pysnt.analysis.growth
            if hasattr(pysnt.analysis.growth, '_module_funcs'):
                module_funcs = pysnt.analysis.growth._module_funcs
                if "_curated_classes" in module_funcs:
                    curated_classes = module_funcs["_curated_classes"]
                    if "GrowthAnalyzer" in curated_classes and curated_classes["GrowthAnalyzer"] is not None:
                        # We have the real Java class, use it instead
                        real_class = curated_classes["GrowthAnalyzer"]
                        return real_class(*args, **kwargs)
        except Exception:
            pass
        
        # No real class available, show error
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")
    
    def __getattr__(self, name: str):
        """Dynamic attribute access for Java methods."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

class GrowthAnalysisResults:
    """
    Curated SNT class from analysis/growth package with method signatures.
    
    Available for direct import after JVM initialization.
    Call pysnt.initialize() before using this class.
    
    See `analysis_growth_GrowthAnalysisResults_javadoc`_.
    
    .. _analysis_growth_GrowthAnalysisResults_javadoc: https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/analysis/growth/GrowthAnalysisResults.html
    """
    
    def __new__(cls, *args, **kwargs):
        """Smart constructor that redirects to real Java class if available."""
        # Try to get the real Java class
        try:
            # Access the module functions that were set up
            import pysnt.analysis.growth
            if hasattr(pysnt.analysis.growth, '_module_funcs'):
                module_funcs = pysnt.analysis.growth._module_funcs
                if "_curated_classes" in module_funcs:
                    curated_classes = module_funcs["_curated_classes"]
                    if "GrowthAnalysisResults" in curated_classes and curated_classes["GrowthAnalysisResults"] is not None:
                        # We have the real Java class, use it instead
                        real_class = curated_classes["GrowthAnalysisResults"]
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
    package_name="sc.fiji.snt.analysis.growth",
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