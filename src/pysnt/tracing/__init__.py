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
    "BiSearch",
    "BiSearchNode",
    "DefaultSearchNode",
    "FillerThread",
    "PathResult",
    "SearchNode",
    "SearchThread",
    "TracerThread",
]

# Extended classes - available via get_class() after discovery
EXTENDED_CLASSES = [
    "AbstractSearch",
    "ManualTracerThread",
    "SearchInterface",
    "TubularGeodesicsTracer",
]


# Placeholder classes for IDE support - will be replaced with Java classes
class BiSearch:
    """
    Curated SNT class from tracing package with method signatures.
    
    Available for direct import after JVM initialization.
    Call pysnt.initialize() before using this class.
    
    See `tracing_BiSearch_javadoc`_.
    
    .. _tracing_BiSearch_javadoc: https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/tracing/BiSearch.html
    """
    
    def __new__(cls, *args, **kwargs):
        """Smart constructor that redirects to real Java class if available."""
        # Try to get the real Java class
        try:
            # Access the module functions that were set up
            import pysnt.tracing
            if hasattr(pysnt.tracing, '_module_funcs'):
                module_funcs = pysnt.tracing._module_funcs
                if "_curated_classes" in module_funcs:
                    curated_classes = module_funcs["_curated_classes"]
                    if "BiSearch" in curated_classes and curated_classes["BiSearch"] is not None:
                        # We have the real Java class, use it instead
                        real_class = curated_classes["BiSearch"]
                        return real_class(*args, **kwargs)
        except Exception:
            pass
        
        # No real class available, show error
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")
    
    def __getattr__(self, name: str):
        """Dynamic attribute access for Java methods."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

class BiSearchNode:
    """
    Curated SNT class from tracing package with method signatures.
    
    Available for direct import after JVM initialization.
    Call pysnt.initialize() before using this class.
    
    See `tracing_BiSearchNode_javadoc`_.
    
    .. _tracing_BiSearchNode_javadoc: https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/tracing/BiSearchNode.html
    """
    
    def __new__(cls, *args, **kwargs):
        """Smart constructor that redirects to real Java class if available."""
        # Try to get the real Java class
        try:
            # Access the module functions that were set up
            import pysnt.tracing
            if hasattr(pysnt.tracing, '_module_funcs'):
                module_funcs = pysnt.tracing._module_funcs
                if "_curated_classes" in module_funcs:
                    curated_classes = module_funcs["_curated_classes"]
                    if "BiSearchNode" in curated_classes and curated_classes["BiSearchNode"] is not None:
                        # We have the real Java class, use it instead
                        real_class = curated_classes["BiSearchNode"]
                        return real_class(*args, **kwargs)
        except Exception:
            pass
        
        # No real class available, show error
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")
    
    def __getattr__(self, name: str):
        """Dynamic attribute access for Java methods."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

class DefaultSearchNode:
    """
    Curated SNT class from tracing package with method signatures.
    
    Available for direct import after JVM initialization.
    Call pysnt.initialize() before using this class.
    
    See `tracing_DefaultSearchNode_javadoc`_.
    
    .. _tracing_DefaultSearchNode_javadoc: https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/tracing/DefaultSearchNode.html
    """
    
    def __new__(cls, *args, **kwargs):
        """Smart constructor that redirects to real Java class if available."""
        # Try to get the real Java class
        try:
            # Access the module functions that were set up
            import pysnt.tracing
            if hasattr(pysnt.tracing, '_module_funcs'):
                module_funcs = pysnt.tracing._module_funcs
                if "_curated_classes" in module_funcs:
                    curated_classes = module_funcs["_curated_classes"]
                    if "DefaultSearchNode" in curated_classes and curated_classes["DefaultSearchNode"] is not None:
                        # We have the real Java class, use it instead
                        real_class = curated_classes["DefaultSearchNode"]
                        return real_class(*args, **kwargs)
        except Exception:
            pass
        
        # No real class available, show error
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")
    
    def __getattr__(self, name: str):
        """Dynamic attribute access for Java methods."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

class FillerThread:
    """
    Curated SNT class from tracing package with method signatures.
    
    Available for direct import after JVM initialization.
    Call pysnt.initialize() before using this class.
    
    See `tracing_FillerThread_javadoc`_.
    
    .. _tracing_FillerThread_javadoc: https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/tracing/FillerThread.html
    """
    
    def __new__(cls, *args, **kwargs):
        """Smart constructor that redirects to real Java class if available."""
        # Try to get the real Java class
        try:
            # Access the module functions that were set up
            import pysnt.tracing
            if hasattr(pysnt.tracing, '_module_funcs'):
                module_funcs = pysnt.tracing._module_funcs
                if "_curated_classes" in module_funcs:
                    curated_classes = module_funcs["_curated_classes"]
                    if "FillerThread" in curated_classes and curated_classes["FillerThread"] is not None:
                        # We have the real Java class, use it instead
                        real_class = curated_classes["FillerThread"]
                        return real_class(*args, **kwargs)
        except Exception:
            pass
        
        # No real class available, show error
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")
    
    def __getattr__(self, name: str):
        """Dynamic attribute access for Java methods."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

class PathResult:
    """
    Curated SNT class from tracing package with method signatures.
    
    Available for direct import after JVM initialization.
    Call pysnt.initialize() before using this class.
    
    See `tracing_PathResult_javadoc`_.
    
    .. _tracing_PathResult_javadoc: https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/tracing/PathResult.html
    """
    
    def __new__(cls, *args, **kwargs):
        """Smart constructor that redirects to real Java class if available."""
        # Try to get the real Java class
        try:
            # Access the module functions that were set up
            import pysnt.tracing
            if hasattr(pysnt.tracing, '_module_funcs'):
                module_funcs = pysnt.tracing._module_funcs
                if "_curated_classes" in module_funcs:
                    curated_classes = module_funcs["_curated_classes"]
                    if "PathResult" in curated_classes and curated_classes["PathResult"] is not None:
                        # We have the real Java class, use it instead
                        real_class = curated_classes["PathResult"]
                        return real_class(*args, **kwargs)
        except Exception:
            pass
        
        # No real class available, show error
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")
    
    def __getattr__(self, name: str):
        """Dynamic attribute access for Java methods."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

class SearchNode:
    """
    Curated SNT class from tracing package with method signatures.
    
    Available for direct import after JVM initialization.
    Call pysnt.initialize() before using this class.
    
    See `tracing_SearchNode_javadoc`_.
    
    .. _tracing_SearchNode_javadoc: https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/tracing/SearchNode.html
    """
    
    def __new__(cls, *args, **kwargs):
        """Smart constructor that redirects to real Java class if available."""
        # Try to get the real Java class
        try:
            # Access the module functions that were set up
            import pysnt.tracing
            if hasattr(pysnt.tracing, '_module_funcs'):
                module_funcs = pysnt.tracing._module_funcs
                if "_curated_classes" in module_funcs:
                    curated_classes = module_funcs["_curated_classes"]
                    if "SearchNode" in curated_classes and curated_classes["SearchNode"] is not None:
                        # We have the real Java class, use it instead
                        real_class = curated_classes["SearchNode"]
                        return real_class(*args, **kwargs)
        except Exception:
            pass
        
        # No real class available, show error
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")
    
    def __getattr__(self, name: str):
        """Dynamic attribute access for Java methods."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

class SearchThread:
    """
    Curated SNT class from tracing package with method signatures.
    
    Available for direct import after JVM initialization.
    Call pysnt.initialize() before using this class.
    
    See `tracing_SearchThread_javadoc`_.
    
    .. _tracing_SearchThread_javadoc: https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/tracing/SearchThread.html
    """
    
    def __new__(cls, *args, **kwargs):
        """Smart constructor that redirects to real Java class if available."""
        # Try to get the real Java class
        try:
            # Access the module functions that were set up
            import pysnt.tracing
            if hasattr(pysnt.tracing, '_module_funcs'):
                module_funcs = pysnt.tracing._module_funcs
                if "_curated_classes" in module_funcs:
                    curated_classes = module_funcs["_curated_classes"]
                    if "SearchThread" in curated_classes and curated_classes["SearchThread"] is not None:
                        # We have the real Java class, use it instead
                        real_class = curated_classes["SearchThread"]
                        return real_class(*args, **kwargs)
        except Exception:
            pass
        
        # No real class available, show error
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")
    
    def __getattr__(self, name: str):
        """Dynamic attribute access for Java methods."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

class TracerThread:
    """
    Curated SNT class from tracing package with method signatures.
    
    Available for direct import after JVM initialization.
    Call pysnt.initialize() before using this class.
    
    See `tracing_TracerThread_javadoc`_.
    
    .. _tracing_TracerThread_javadoc: https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/tracing/TracerThread.html
    """
    
    def __new__(cls, *args, **kwargs):
        """Smart constructor that redirects to real Java class if available."""
        # Try to get the real Java class
        try:
            # Access the module functions that were set up
            import pysnt.tracing
            if hasattr(pysnt.tracing, '_module_funcs'):
                module_funcs = pysnt.tracing._module_funcs
                if "_curated_classes" in module_funcs:
                    curated_classes = module_funcs["_curated_classes"]
                    if "TracerThread" in curated_classes and curated_classes["TracerThread"] is not None:
                        # We have the real Java class, use it instead
                        real_class = curated_classes["TracerThread"]
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
    package_name="sc.fiji.snt.tracing",
    curated_classes=CURATED_CLASSES,
    extended_classes=EXTENDED_CLASSES,
    globals_dict=globals(),
    include_interfaces=True  # Include interfaces for tracing
)

# Import functions into module namespace
get_available_classes = _module_funcs["get_available_classes"]
get_class = _module_funcs["get_class"]
list_classes = _module_funcs["list_classes"]
get_curated_classes = _module_funcs["get_curated_classes"]
get_extended_classes = _module_funcs["get_extended_classes"]

# Create module-level __getattr__ and __dir__
__getattr__ = _module_funcs["create_getattr"]("pysnt.tracing", submodules=["artist", "cost", "heuristic", "image"])
__dir__ = _module_funcs["create_dir"]()


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
    # Submodules
    "artist",
    "cost", 
    "heuristic",
    "image",
]

# Submodule imports
from . import artist, cost, heuristic, image
