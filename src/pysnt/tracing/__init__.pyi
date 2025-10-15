"""
Type stubs for pysnt.tracing module.

This file provides type hints for the tracing module,
covering automated and manual neurite tracing classes.
"""

from typing import Any, List, Optional

# Type alias for Java classes
JavaClass = Any

# Constants
CURATED_CLASSES: List[str]
EXTENDED_CLASSES: List[str]

# Curated classes - always available for direct import
SearchThread: Optional[JavaClass]
TracerThread: Optional[JavaClass]

# Class discovery and access functions
def get_available_classes() -> List[str]:
    """
    Get list of all available tracing classes.
    
    Returns
    -------
    List[str]
        List of available class names.
    """
    ...

def get_class(class_name: str) -> JavaClass:
    """
    Get a specific tracing class by name.
    
    Parameters
    ----------
    class_name : str
        Name of the class to retrieve.
        
    Returns
    -------
    JavaClass
        The requested SNT tracing class.
        
    Raises
    ------
    KeyError
        If the class is not available.
    RuntimeError
        If the JVM has not been started.
    """
    ...

def list_classes() -> None:
    """Print all available tracing classes organized by tier."""
    ...

def get_curated_classes() -> List[str]:
    """
    Get list of curated classes that are always available for direct import.
    
    Returns
    -------
    List[str]
        List of curated class names.
    """
    ...

def get_extended_classes() -> List[str]:
    """
    Get list of extended classes available via get_class().
    
    This will trigger discovery if not already done.
    
    Returns
    -------
    List[str]
        List of extended class names.
    """
    ...

# Dynamic attribute access support
def __getattr__(name: str) -> JavaClass:
    """
    Provide dynamic access to tracing classes.
    
    This allows importing classes that were discovered at runtime.
    """
    ...

def __dir__() -> List[str]:
    """Return list of available attributes for IDE autocompletion."""
    ...

# Module attributes
__all__: List[str]