"""
This module provides convenient access to
`SNT's util classes <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/util/package-summary.html>`__.
"""

import logging
import scyjava
from typing import Dict, Any, List

from ..common_module import setup_module_classes

logger = logging.getLogger(__name__)

# Curated classes - always available for direct import
CURATED_CLASSES = [
    "BoundingBox",
    "ColorMaps",
    "CrossoverFinder",
    "ImgUtils",
    "ImpUtils",
    "PointInImage",
    "SNTColor",
    "SNTPoint",
    "SWCPoint",
]

# Extended classes - available via get_class() after discovery
EXTENDED_CLASSES = [
    "CircleCursor3D",
    "DiskCursor3D",
    "LinAlgUtils",
    "Logger",
    "LSystemsTree",
    "PathCursor",
    "PointInCanvas" "ShollPoint",
    "SigmaUtils",
]


# Placeholder classes for IDE support - will be replaced with Java classes
class BoundingBox:
    """
    Curated SNT class from util package with method signatures.
    
    Available for direct import after JVM initialization.
    Call pysnt.initialize() before using this class.
    
    See `Javadoc Documentation`_.
    
    .. _Javadoc Documentation: https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/util/BoundingBox.html
    """
    
    def __getattr__(self, name: str):
        """Dynamic attribute access for Java methods."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")
    
    def __init__(self, *args, **kwargs):
        """Placeholder constructor."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

class ColorMaps:
    """
    Curated SNT class from util package with method signatures.
    
    Available for direct import after JVM initialization.
    Call pysnt.initialize() before using this class.
    
    See `Javadoc Documentation`_.
    
    .. _Javadoc Documentation: https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/util/ColorMaps.html
    """
    
    def __getattr__(self, name: str):
        """Dynamic attribute access for Java methods."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")
    
    def __init__(self, *args, **kwargs):
        """Placeholder constructor."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

class ImpUtils:
    """
    Curated SNT class from util package with method signatures.
    
    Available for direct import after JVM initialization.
    Call pysnt.initialize() before using this class.
    
    See `Javadoc Documentation`_.
    
    .. _Javadoc Documentation: https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/util/ImpUtils.html
    """
    
    def __getattr__(self, name: str):
        """Dynamic attribute access for Java methods."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")
    
    def __init__(self, *args, **kwargs):
        """Placeholder constructor."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

class PointInImage:
    """
    Curated SNT class from util package with method signatures.
    
    Available for direct import after JVM initialization.
    Call pysnt.initialize() before using this class.
    
    See `Javadoc Documentation`_.
    
    .. _Javadoc Documentation: https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/util/PointInImage.html
    """
    
    def __getattr__(self, name: str):
        """Dynamic attribute access for Java methods."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")
    
    def __init__(self, *args, **kwargs):
        """Placeholder constructor."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

class SNTColor:
    """
    Curated SNT class from util package with method signatures.
    
    Available for direct import after JVM initialization.
    Call pysnt.initialize() before using this class.
    
    See `Javadoc Documentation`_.
    
    .. _Javadoc Documentation: https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/util/SNTColor.html
    """
    
    def __getattr__(self, name: str):
        """Dynamic attribute access for Java methods."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")
    
    def __init__(self, *args, **kwargs):
        """Placeholder constructor."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

class SNTPoint:
    """
    Curated SNT class from util package with method signatures.
    
    Available for direct import after JVM initialization.
    Call pysnt.initialize() before using this class.
    
    See `Javadoc Documentation`_.
    
    .. _Javadoc Documentation: https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/util/SNTPoint.html
    """
    
    def __getattr__(self, name: str):
        """Dynamic attribute access for Java methods."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")
    
    def __init__(self, *args, **kwargs):
        """Placeholder constructor."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

class SWCPoint:
    """
    Curated SNT class from util package with method signatures.
    
    Available for direct import after JVM initialization.
    Call pysnt.initialize() before using this class.
    
    See `Javadoc Documentation`_.
    
    .. _Javadoc Documentation: https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/util/SWCPoint.html
    """
    
    def __getattr__(self, name: str):
        """Dynamic attribute access for Java methods."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")
    
    def __init__(self, *args, **kwargs):
        """Placeholder constructor."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")


# Setup common module functionality
_module_funcs = setup_module_classes(
    package_name="sc.fiji.snt.util",
    curated_classes=CURATED_CLASSES,
    extended_classes=EXTENDED_CLASSES,
    globals_dict=globals(),
    discovery_packages=["sc.fiji.snt", "sc.fiji.snt.util"],  # Search both packages
)

# Import functions into module namespace
get_available_classes = _module_funcs["get_available_classes"]
get_class = _module_funcs["get_class"]
list_classes = _module_funcs["list_classes"]
get_curated_classes = _module_funcs["get_curated_classes"]
get_extended_classes = _module_funcs["get_extended_classes"]

# Create module-level __getattr__ and __dir__
__getattr__ = _module_funcs["create_getattr"]("pysnt.util")
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
    "PointInImage",
    "SWCPoint",
]
