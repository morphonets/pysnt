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
    "SWCExportException",
    "TracesFileFormatException",
]

# =============================================================================
# MODULE SETUP - USUALLY NO CHANGES NEEDED
# =============================================================================


# Placeholder classes for IDE support - will be replaced with Java classes
class FlyCircuitLoader:
    """
    Curated SNT class from io package with method signatures.
    
    Available for direct import after JVM initialization.
    Call pysnt.initialize() before using this class.
    
    See `io_FlyCircuitLoader_javadoc`_.
    
    .. _io_FlyCircuitLoader_javadoc: https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/io/FlyCircuitLoader.html
    """
    
    def __new__(cls, *args, **kwargs):
        """Smart constructor that redirects to real Java class if available."""
        # Try to get the real Java class
        try:
            # Access the module functions that were set up
            import pysnt.io
            if hasattr(pysnt.io, '_module_funcs'):
                module_funcs = pysnt.io._module_funcs
                if "_curated_classes" in module_funcs:
                    curated_classes = module_funcs["_curated_classes"]
                    if "FlyCircuitLoader" in curated_classes and curated_classes["FlyCircuitLoader"] is not None:
                        # We have the real Java class, use it instead
                        real_class = curated_classes["FlyCircuitLoader"]
                        return real_class(*args, **kwargs)
        except Exception:
            pass
        
        # No real class available, show error
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")
    
    def __getattr__(self, name: str):
        """Dynamic attribute access for Java methods."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

class InsectBrainLoader:
    """
    Curated SNT class from io package with method signatures.
    
    Available for direct import after JVM initialization.
    Call pysnt.initialize() before using this class.
    
    See `io_InsectBrainLoader_javadoc`_.
    
    .. _io_InsectBrainLoader_javadoc: https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/io/InsectBrainLoader.html
    """
    
    def __new__(cls, *args, **kwargs):
        """Smart constructor that redirects to real Java class if available."""
        # Try to get the real Java class
        try:
            # Access the module functions that were set up
            import pysnt.io
            if hasattr(pysnt.io, '_module_funcs'):
                module_funcs = pysnt.io._module_funcs
                if "_curated_classes" in module_funcs:
                    curated_classes = module_funcs["_curated_classes"]
                    if "InsectBrainLoader" in curated_classes and curated_classes["InsectBrainLoader"] is not None:
                        # We have the real Java class, use it instead
                        real_class = curated_classes["InsectBrainLoader"]
                        return real_class(*args, **kwargs)
        except Exception:
            pass
        
        # No real class available, show error
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")
    
    def __getattr__(self, name: str):
        """Dynamic attribute access for Java methods."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

class MouseLightLoader:
    """
    Curated SNT class from io package with method signatures.
    
    Available for direct import after JVM initialization.
    Call pysnt.initialize() before using this class.
    
    See `io_MouseLightLoader_javadoc`_.
    
    .. _io_MouseLightLoader_javadoc: https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/io/MouseLightLoader.html
    """
    
    def __new__(cls, *args, **kwargs):
        """Smart constructor that redirects to real Java class if available."""
        # Try to get the real Java class
        try:
            # Access the module functions that were set up
            import pysnt.io
            if hasattr(pysnt.io, '_module_funcs'):
                module_funcs = pysnt.io._module_funcs
                if "_curated_classes" in module_funcs:
                    curated_classes = module_funcs["_curated_classes"]
                    if "MouseLightLoader" in curated_classes and curated_classes["MouseLightLoader"] is not None:
                        # We have the real Java class, use it instead
                        real_class = curated_classes["MouseLightLoader"]
                        return real_class(*args, **kwargs)
        except Exception:
            pass
        
        # No real class available, show error
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")
    
    def __getattr__(self, name: str):
        """Dynamic attribute access for Java methods."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

class MouseLightQuerier:
    """
    Curated SNT class from io package with method signatures.
    
    Available for direct import after JVM initialization.
    Call pysnt.initialize() before using this class.
    
    See `io_MouseLightQuerier_javadoc`_.
    
    .. _io_MouseLightQuerier_javadoc: https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/io/MouseLightQuerier.html
    """
    
    def __new__(cls, *args, **kwargs):
        """Smart constructor that redirects to real Java class if available."""
        # Try to get the real Java class
        try:
            # Access the module functions that were set up
            import pysnt.io
            if hasattr(pysnt.io, '_module_funcs'):
                module_funcs = pysnt.io._module_funcs
                if "_curated_classes" in module_funcs:
                    curated_classes = module_funcs["_curated_classes"]
                    if "MouseLightQuerier" in curated_classes and curated_classes["MouseLightQuerier"] is not None:
                        # We have the real Java class, use it instead
                        real_class = curated_classes["MouseLightQuerier"]
                        return real_class(*args, **kwargs)
        except Exception:
            pass
        
        # No real class available, show error
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")
    
    def __getattr__(self, name: str):
        """Dynamic attribute access for Java methods."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

class NeuroMorphoLoader:
    """
    Curated SNT class from io package with method signatures.
    
    Available for direct import after JVM initialization.
    Call pysnt.initialize() before using this class.
    
    See `io_NeuroMorphoLoader_javadoc`_.
    
    .. _io_NeuroMorphoLoader_javadoc: https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/io/NeuroMorphoLoader.html
    """
    
    def __new__(cls, *args, **kwargs):
        """Smart constructor that redirects to real Java class if available."""
        # Try to get the real Java class
        try:
            # Access the module functions that were set up
            import pysnt.io
            if hasattr(pysnt.io, '_module_funcs'):
                module_funcs = pysnt.io._module_funcs
                if "_curated_classes" in module_funcs:
                    curated_classes = module_funcs["_curated_classes"]
                    if "NeuroMorphoLoader" in curated_classes and curated_classes["NeuroMorphoLoader"] is not None:
                        # We have the real Java class, use it instead
                        real_class = curated_classes["NeuroMorphoLoader"]
                        return real_class(*args, **kwargs)
        except Exception:
            pass
        
        # No real class available, show error
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")
    
    def __getattr__(self, name: str):
        """Dynamic attribute access for Java methods."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

class RemoteSWCLoader:
    """
    Curated SNT class from io package with method signatures.
    
    Available for direct import after JVM initialization.
    Call pysnt.initialize() before using this class.
    
    See `io_RemoteSWCLoader_javadoc`_.
    
    .. _io_RemoteSWCLoader_javadoc: https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/io/RemoteSWCLoader.html
    """
    
    def __new__(cls, *args, **kwargs):
        """Smart constructor that redirects to real Java class if available."""
        # Try to get the real Java class
        try:
            # Access the module functions that were set up
            import pysnt.io
            if hasattr(pysnt.io, '_module_funcs'):
                module_funcs = pysnt.io._module_funcs
                if "_curated_classes" in module_funcs:
                    curated_classes = module_funcs["_curated_classes"]
                    if "RemoteSWCLoader" in curated_classes and curated_classes["RemoteSWCLoader"] is not None:
                        # We have the real Java class, use it instead
                        real_class = curated_classes["RemoteSWCLoader"]
                        return real_class(*args, **kwargs)
        except Exception:
            pass
        
        # No real class available, show error
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")
    
    def __getattr__(self, name: str):
        """Dynamic attribute access for Java methods."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

class WekaModelLoader:
    """
    Curated SNT class from io package with method signatures.
    
    Available for direct import after JVM initialization.
    Call pysnt.initialize() before using this class.
    
    See `io_WekaModelLoader_javadoc`_.
    
    .. _io_WekaModelLoader_javadoc: https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/io/WekaModelLoader.html
    """
    
    def __new__(cls, *args, **kwargs):
        """Smart constructor that redirects to real Java class if available."""
        # Try to get the real Java class
        try:
            # Access the module functions that were set up
            import pysnt.io
            if hasattr(pysnt.io, '_module_funcs'):
                module_funcs = pysnt.io._module_funcs
                if "_curated_classes" in module_funcs:
                    curated_classes = module_funcs["_curated_classes"]
                    if "WekaModelLoader" in curated_classes and curated_classes["WekaModelLoader"] is not None:
                        # We have the real Java class, use it instead
                        real_class = curated_classes["WekaModelLoader"]
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
