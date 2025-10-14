"""
Tracing utilities for automated and manual neurite tracing.

This module provides convenient access to SNT's tracing classes
for automated pathfinding and manual tracing operations.

All public classes from sc.fiji.snt.tracing are automatically imported
and made available for direct import.
"""

import logging
import scyjava
from typing import Dict, Any, List

logger = logging.getLogger(__name__)

# Global registry for dynamically imported classes
_java_classes: Dict[str, Any] = {}
_all_classes: List[str] = []


def _java_setup():
    """
    Lazy initialization function for Java-dependent tracing classes.
    
    Do not call this directly; use scyjava.start_jvm() instead.
    This function is automatically called when the JVM starts.
    """
    global _java_classes, _all_classes
    
    try:
        # Import the utility function from core
        from ..core import setup_dynamic_imports
        
        # Known tracing classes (used as fallback if scanning fails)
        known_classes = [
            "PathFitter",
            "TracerThread",
            "SearchThread",
            "FillerThread",
            "SimpleNeuriteTracer",
            "PathAndFillManager",
            "SearchInterface",
            "TracingUtils",
            "PathFitterSimple",
            "BiDirSearchThread",
        ]
        
        # Use the utility function to set up dynamic imports
        _java_classes = setup_dynamic_imports(
            globals(),
            "sc.fiji.snt.tracing",
            known_classes,
            include_abstract=False,
            include_interfaces=True  # Include interfaces for tracing
        )
        
        _all_classes = list(_java_classes.keys())
        logger.info(f"Successfully imported {len(_java_classes)} SNT tracing classes")
        
    except Exception as e:
        logger.error(f"Failed to import SNT tracing classes: {e}")
        raise ImportError(f"Could not import SNT tracing classes: {e}") from e


# Register the setup function to run when JVM starts
scyjava.when_jvm_starts(_java_setup)


def get_available_classes() -> List[str]:
    """
    Get list of all available tracing classes.
    
    Returns
    -------
    List[str]
        List of available class names.
    """
    return _all_classes.copy()


def get_class(class_name: str) -> Any:
    """
    Get a specific tracing class by name.
    
    Parameters
    ----------
    class_name : str
        Name of the class to retrieve.
        
    Returns
    -------
    Java class
        The requested SNT tracing class.
        
    Raises
    ------
    KeyError
        If the class is not available.
    RuntimeError
        If the JVM has not been started.
    """
    if not _java_classes:
        raise RuntimeError(
            "Tracing classes not available. Ensure JVM is started and SNT is initialized."
        )
    
    if class_name not in _java_classes:
        available = ", ".join(_java_classes.keys())
        raise KeyError(f"Class '{class_name}' not found. Available: {available}")
    
    return _java_classes[class_name]


def list_classes():
    """
    Print all available tracing classes with their descriptions.
    """
    if not _java_classes:
        print("No classes available. Initialize SNT first.")
        return
        
    print("Available SNT Tracing Classes:")
    print("=" * 40)
    for class_name in sorted(_java_classes.keys()):
        print(f"  • {class_name}")


# Dynamic __getattr__ to provide access to classes
def __getattr__(name: str) -> Any:
    """
    Provide dynamic access to tracing classes.
    
    This allows importing classes that were discovered at runtime:
    from pysnt.tracing import SomeDiscoveredClass
    """
    if name in _java_classes:
        return _java_classes[name]
    
    # If class not found, provide helpful error
    if _java_classes:
        available = ", ".join(_java_classes.keys())
        raise AttributeError(f"Class '{name}' not found in tracing module. Available: {available}")
    else:
        raise AttributeError(f"Tracing classes not loaded. Initialize SNT first.")


# Dynamic __all__ that gets populated after Java setup
def __dir__() -> List[str]:
    """Return list of available attributes including dynamically loaded classes."""
    base_attrs = [
        "get_available_classes", 
        "get_class", 
        "list_classes"
    ]
    return base_attrs + _all_classes


# Initial __all__ (will be updated after Java classes are loaded)
__all__ = [
    "get_available_classes",
    "get_class", 
    "list_classes",
]