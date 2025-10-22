"""Comprehensive type stubs for Java classes."""

from typing import Any, List

class BiSearch:
    """
    SNT BiSearch class.
    
    This class provides access to the Java BiSearch functionality.
    All methods and properties are dynamically resolved at runtime.
    """
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the BiSearch."""
        ...
    
    def __getattr__(self, name: str) -> Any:
        """Dynamic attribute access for Java methods and fields."""
        ...
    
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """Make the class callable if it has a default method."""
        ...

class BiSearchNode:
    """
    SNT BiSearchNode class.
    
    This class provides access to the Java BiSearchNode functionality.
    All methods and properties are dynamically resolved at runtime.
    """
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the BiSearchNode."""
        ...
    
    def __getattr__(self, name: str) -> Any:
        """Dynamic attribute access for Java methods and fields."""
        ...
    
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """Make the class callable if it has a default method."""
        ...

class DefaultSearchNode:
    """
    SNT DefaultSearchNode class.
    
    This class provides access to the Java DefaultSearchNode functionality.
    All methods and properties are dynamically resolved at runtime.
    """
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the DefaultSearchNode."""
        ...
    
    def __getattr__(self, name: str) -> Any:
        """Dynamic attribute access for Java methods and fields."""
        ...
    
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """Make the class callable if it has a default method."""
        ...

class FillerThread:
    """
    SNT FillerThread class.
    
    This class provides access to the Java FillerThread functionality.
    All methods and properties are dynamically resolved at runtime.
    """
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the FillerThread."""
        ...
    
    def __getattr__(self, name: str) -> Any:
        """Dynamic attribute access for Java methods and fields."""
        ...
    
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """Make the class callable if it has a default method."""
        ...

class PathResult:
    """
    SNT PathResult class.
    
    This class provides access to the Java PathResult functionality.
    All methods and properties are dynamically resolved at runtime.
    """
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the PathResult."""
        ...
    
    def __getattr__(self, name: str) -> Any:
        """Dynamic attribute access for Java methods and fields."""
        ...
    
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """Make the class callable if it has a default method."""
        ...

class SearchNode:
    """
    SNT SearchNode class.
    
    This class provides access to the Java SearchNode functionality.
    All methods and properties are dynamically resolved at runtime.
    """
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the SearchNode."""
        ...
    
    def __getattr__(self, name: str) -> Any:
        """Dynamic attribute access for Java methods and fields."""
        ...
    
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """Make the class callable if it has a default method."""
        ...

class SearchThread:
    """
    SNT SearchThread class.
    
    This class provides access to the Java SearchThread functionality.
    All methods and properties are dynamically resolved at runtime.
    """
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the SearchThread."""
        ...
    
    def __getattr__(self, name: str) -> Any:
        """Dynamic attribute access for Java methods and fields."""
        ...
    
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """Make the class callable if it has a default method."""
        ...

class TracerThread:
    """
    SNT TracerThread class.
    
    This class provides access to the Java TracerThread functionality.
    All methods and properties are dynamically resolved at runtime.
    """
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the TracerThread."""
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