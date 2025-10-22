"""Comprehensive type stubs for Java classes."""

from typing import Any, List

class MultiViewer2D:
    """
    SNT MultiViewer2D class.
    
    This class provides access to the Java MultiViewer2D functionality.
    All methods and properties are dynamically resolved at runtime.
    """
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the MultiViewer2D."""
        ...
    
    def __getattr__(self, name: str) -> Any:
        """Dynamic attribute access for Java methods and fields."""
        ...
    
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """Make the class callable if it has a default method."""
        ...

class MultiViewer3D:
    """
    SNT MultiViewer3D class.
    
    This class provides access to the Java MultiViewer3D functionality.
    All methods and properties are dynamically resolved at runtime.
    """
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the MultiViewer3D."""
        ...
    
    def __getattr__(self, name: str) -> Any:
        """Dynamic attribute access for Java methods and fields."""
        ...
    
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """Make the class callable if it has a default method."""
        ...

class Viewer2D:
    """
    SNT Viewer2D class.
    
    This class provides access to the Java Viewer2D functionality.
    All methods and properties are dynamically resolved at runtime.
    """
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the Viewer2D."""
        ...
    
    def __getattr__(self, name: str) -> Any:
        """Dynamic attribute access for Java methods and fields."""
        ...
    
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """Make the class callable if it has a default method."""
        ...

class Viewer3D:
    """
    SNT Viewer3D class.
    
    This class provides access to the Java Viewer3D functionality.
    All methods and properties are dynamically resolved at runtime.
    """
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the Viewer3D."""
        ...
    
    def __getattr__(self, name: str) -> Any:
        """Dynamic attribute access for Java methods and fields."""
        ...
    
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """Make the class callable if it has a default method."""
        ...

# Module functions
def get_available_classes() -> List[str]: ...
def get_class(class_name: str) -> Any: ...
def list_classes() -> None: ...
def get_curated_classes() -> List[str]: ...
def get_extended_classes() -> List[str]: ...

CURATED_CLASSES: List[str]
EXTENDED_CLASSES: List[str]