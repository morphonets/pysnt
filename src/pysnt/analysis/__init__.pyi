"""
Type stubs for pysnt.analysis module.

This file provides comprehensive type hints for the analysis module,
ensuring excellent IDE support for both curated and extended classes.
"""

from typing import Any, List, Optional, Union

# Type alias for Java classes
JavaClass = Any

# Constants
CURATED_CLASSES: List[str]
EXTENDED_CLASSES: List[str]

# Curated classes - always available for direct import
# These are the most commonly used analysis classes from sc.fiji.snt.analysis
TreeStatistics: Optional[JavaClass]
MultiTreeStatistics: Optional[JavaClass]
ConvexHull: Optional[JavaClass]

# Class discovery and access functions
def get_available_classes() -> List[str]:
    """
    Get list of all available analysis classes.
    
    This includes both curated classes (always loaded) and extended classes
    (loaded on-demand). Extended classes are discovered if not already loaded.
    
    Returns
    -------
    List[str]
        List of available class names.
    """
    ...

def get_class(class_name: str) -> JavaClass:
    """
    Get a specific analysis class by name.
    
    This method provides access to both curated and extended classes.
    Extended classes are discovered and loaded on first access.
    
    Parameters
    ----------
    class_name : str
        Name of the class to retrieve.
        
    Returns
    -------
    JavaClass
        The requested SNT analysis class.
        
    Raises
    ------
    KeyError
        If the class is not available.
    RuntimeError
        If the JVM has not been started.
    """
    ...

def list_classes() -> None:
    """Print all available analysis classes organized by tier."""
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
    Provide dynamic access to analysis classes.
    
    This allows importing classes that were discovered at runtime.
    """
    ...

def __dir__() -> List[str]:
    """Return list of available attributes for IDE autocompletion."""
    ...

# Module attributes
__all__: List[str]