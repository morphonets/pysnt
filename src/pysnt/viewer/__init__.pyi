"""
Type stubs for pysnt.viewer module.

This file provides type hints for the viewer module,
covering 2D and 3D visualization classes.
"""

from typing import Any, List

# Type alias for Java classes
JavaClass = Any

# Class discovery and access functions
def get_available_classes() -> List[str]:
    """
    Get list of all available viewer classes.
    
    Returns
    -------
    List[str]
        List of available class names.
    """
    ...

def get_class(class_name: str) -> JavaClass:
    """
    Get a specific viewer class by name.
    
    Parameters
    ----------
    class_name : str
        Name of the class to retrieve.
        
    Returns
    -------
    JavaClass
        The requested SNT viewer class.
        
    Raises
    ------
    KeyError
        If the class is not available.
    RuntimeError
        If the JVM has not been started.
    """
    ...

def list_classes() -> None:
    """Print all available viewer classes with their descriptions."""
    ...

# Dynamic attribute access support
def __getattr__(name: str) -> JavaClass:
    """
    Provide dynamic access to viewer classes.
    
    This allows importing classes that were discovered at runtime.
    """
    ...

def __dir__() -> List[str]:
    """Return list of available attributes for IDE autocompletion."""
    ...

# Module attributes
__all__: List[str]