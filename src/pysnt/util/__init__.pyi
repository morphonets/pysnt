"""Comprehensive type stubs for Java classes."""

from typing import Any, List

class BoundingBox:
    """
    SNT BoundingBox class.
    
    This class provides access to the Java BoundingBox functionality.
    All methods and properties are dynamically resolved at runtime.
    """
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the BoundingBox."""
        ...
    
    def __getattr__(self, name: str) -> Any:
        """Dynamic attribute access for Java methods and fields."""
        ...
    
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """Make the class callable if it has a default method."""
        ...

class ColorMaps:
    """
    SNT ColorMaps class.
    
    This class provides access to the Java ColorMaps functionality.
    All methods and properties are dynamically resolved at runtime.
    """
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the ColorMaps."""
        ...
    
    def __getattr__(self, name: str) -> Any:
        """Dynamic attribute access for Java methods and fields."""
        ...
    
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """Make the class callable if it has a default method."""
        ...

class CrossoverFinder:
    """
    SNT CrossoverFinder class.
    
    This class provides access to the Java CrossoverFinder functionality.
    All methods and properties are dynamically resolved at runtime.
    """
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the CrossoverFinder."""
        ...
    
    def __getattr__(self, name: str) -> Any:
        """Dynamic attribute access for Java methods and fields."""
        ...
    
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """Make the class callable if it has a default method."""
        ...

class ImgUtils:
    """
    SNT ImgUtils class.
    
    This class provides access to the Java ImgUtils functionality.
    All methods and properties are dynamically resolved at runtime.
    """
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the ImgUtils."""
        ...
    
    def __getattr__(self, name: str) -> Any:
        """Dynamic attribute access for Java methods and fields."""
        ...
    
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """Make the class callable if it has a default method."""
        ...

class ImpUtils:
    """
    SNT ImpUtils class.
    
    This class provides access to the Java ImpUtils functionality.
    All methods and properties are dynamically resolved at runtime.
    """
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the ImpUtils."""
        ...
    
    def __getattr__(self, name: str) -> Any:
        """Dynamic attribute access for Java methods and fields."""
        ...
    
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """Make the class callable if it has a default method."""
        ...

class PointInImage:
    """
    SNT PointInImage class.
    
    This class provides access to the Java PointInImage functionality.
    All methods and properties are dynamically resolved at runtime.
    """
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the PointInImage."""
        ...
    
    def __getattr__(self, name: str) -> Any:
        """Dynamic attribute access for Java methods and fields."""
        ...
    
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """Make the class callable if it has a default method."""
        ...

class SNTColor:
    """
    SNT SNTColor class.
    
    This class provides access to the Java SNTColor functionality.
    All methods and properties are dynamically resolved at runtime.
    """
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the SNTColor."""
        ...
    
    def __getattr__(self, name: str) -> Any:
        """Dynamic attribute access for Java methods and fields."""
        ...
    
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """Make the class callable if it has a default method."""
        ...

class SNTPoint:
    """
    SNT SNTPoint class.
    
    This class provides access to the Java SNTPoint functionality.
    All methods and properties are dynamically resolved at runtime.
    """
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the SNTPoint."""
        ...
    
    def __getattr__(self, name: str) -> Any:
        """Dynamic attribute access for Java methods and fields."""
        ...
    
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """Make the class callable if it has a default method."""
        ...

class SWCPoint:
    """
    SNT SWCPoint class.
    
    This class provides access to the Java SWCPoint functionality.
    All methods and properties are dynamically resolved at runtime.
    """
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the SWCPoint."""
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