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
    "MultiViewer2D", "MultiViewer3D",
    "Viewer2D", "Viewer3D"
]

# Extended classes - available via get_class() after discovery
EXTENDED_CLASSES = [
    "Annotation3D",
    "Bvv",
    "ColorTableMapper",
    "GraphViewer"
]


class MultiViewer2D:
    """
    Curated SNT class from viewer package with method signatures.
    
    Available for direct import after JVM initialization.
    Call pysnt.initialize() before using this class.
    
    See `viewer_MultiViewer2D_javadoc`_.
    
    .. _viewer_MultiViewer2D_javadoc: https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/viewer/MultiViewer2D.html
    """
    
    def __new__(cls, *args, **kwargs):
        """Smart constructor that redirects to real Java class if available."""
        # Try to get the real Java class
        try:
            # Access the module functions that were set up
            import pysnt.viewer
            if hasattr(pysnt.viewer, '_module_funcs'):
                module_funcs = pysnt.viewer._module_funcs
                if "_curated_classes" in module_funcs:
                    curated_classes = module_funcs["_curated_classes"]
                    if "MultiViewer2D" in curated_classes and curated_classes["MultiViewer2D"] is not None:
                        # We have the real Java class, use it instead
                        real_class = curated_classes["MultiViewer2D"]
                        return real_class(*args, **kwargs)
        except Exception:
            pass
        
        # No real class available, show error
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")
    
    def __getattr__(self, name: str):
        """Dynamic attribute access for Java methods."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

class MultiViewer3D:
    """
    Curated SNT class from viewer package with method signatures.
    
    Available for direct import after JVM initialization.
    Call pysnt.initialize() before using this class.
    
    See `viewer_MultiViewer3D_javadoc`_.
    
    .. _viewer_MultiViewer3D_javadoc: https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/viewer/MultiViewer3D.html
    """
    
    def __new__(cls, *args, **kwargs):
        """Smart constructor that redirects to real Java class if available."""
        # Try to get the real Java class
        try:
            # Access the module functions that were set up
            import pysnt.viewer
            if hasattr(pysnt.viewer, '_module_funcs'):
                module_funcs = pysnt.viewer._module_funcs
                if "_curated_classes" in module_funcs:
                    curated_classes = module_funcs["_curated_classes"]
                    if "MultiViewer3D" in curated_classes and curated_classes["MultiViewer3D"] is not None:
                        # We have the real Java class, use it instead
                        real_class = curated_classes["MultiViewer3D"]
                        return real_class(*args, **kwargs)
        except Exception:
            pass
        
        # No real class available, show error
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")
    
    def __getattr__(self, name: str):
        """Dynamic attribute access for Java methods."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

class Viewer2D:
    """
    Curated SNT class from viewer package with method signatures.
    
    Available for direct import after JVM initialization.
    Call pysnt.initialize() before using this class.
    
    See `viewer_Viewer2D_javadoc`_.
    
    .. _viewer_Viewer2D_javadoc: https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/viewer/Viewer2D.html
    """
    
    def __new__(cls, *args, **kwargs):
        """Smart constructor that redirects to real Java class if available."""
        # Try to get the real Java class
        try:
            # Access the module functions that were set up
            import pysnt.viewer
            if hasattr(pysnt.viewer, '_module_funcs'):
                module_funcs = pysnt.viewer._module_funcs
                if "_curated_classes" in module_funcs:
                    curated_classes = module_funcs["_curated_classes"]
                    if "Viewer2D" in curated_classes and curated_classes["Viewer2D"] is not None:
                        # We have the real Java class, use it instead
                        real_class = curated_classes["Viewer2D"]
                        return real_class(*args, **kwargs)
        except Exception:
            pass
        
        # No real class available, show error
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")
    
    def __getattr__(self, name: str):
        """Dynamic attribute access for Java methods."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

class Viewer3D:
    """
    Curated SNT class from viewer package with method signatures.
    
    Available for direct import after JVM initialization.
    Call pysnt.initialize() before using this class.
    
    See `viewer_Viewer3D_javadoc`_.
    
    .. _viewer_Viewer3D_javadoc: https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/viewer/Viewer3D.html
    """
    
    def __new__(cls, *args, **kwargs):
        """Smart constructor that redirects to real Java class if available."""
        # Try to get the real Java class
        try:
            # Access the module functions that were set up
            import pysnt.viewer
            if hasattr(pysnt.viewer, '_module_funcs'):
                module_funcs = pysnt.viewer._module_funcs
                if "_curated_classes" in module_funcs:
                    curated_classes = module_funcs["_curated_classes"]
                    if "Viewer3D" in curated_classes and curated_classes["Viewer3D"] is not None:
                        # We have the real Java class, use it instead
                        real_class = curated_classes["Viewer3D"]
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
    package_name="sc.fiji.snt.viewer",
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
]