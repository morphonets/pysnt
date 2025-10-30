"""Comprehensive type stubs for Java classes."""

from typing import Any, List, Dict, Optional, Union, overload, Set, Callable

class BiSearch:
    """
    SNT BiSearch class (type stub).
    
    This class provides access to the Java BiSearch functionality.
    At runtime, this is handled by the dynamic placeholder system in setup_module_classes().
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
    SNT BiSearchNode class (type stub).
    
    This class provides access to the Java BiSearchNode functionality.
    At runtime, this is handled by the dynamic placeholder system in setup_module_classes().
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
    SNT DefaultSearchNode class (type stub).
    
    This class provides access to the Java DefaultSearchNode functionality.
    At runtime, this is handled by the dynamic placeholder system in setup_module_classes().
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
    SNT FillerThread class (type stub).
    
    This class provides access to the Java FillerThread functionality.
    At runtime, this is handled by the dynamic placeholder system in setup_module_classes().
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
    SNT PathResult class (type stub).
    
    This class provides access to the Java PathResult functionality.
    At runtime, this is handled by the dynamic placeholder system in setup_module_classes().
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
    SNT SearchNode class (type stub).
    
    This class provides access to the Java SearchNode functionality.
    At runtime, this is handled by the dynamic placeholder system in setup_module_classes().
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
    SNT SearchThread class (type stub).
    
    This class provides access to the Java SearchThread functionality.
    At runtime, this is handled by the dynamic placeholder system in setup_module_classes().
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
    SNT TracerThread class (type stub).
    
    This class provides access to the Java TracerThread functionality.
    At runtime, this is handled by the dynamic placeholder system in setup_module_classes().
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

# Core functions (fallback)
def initialize(fiji_path: Optional[str] = None, interactive: bool = True, ensure_java: bool = True, mode: str = "headless") -> None: ...

# Exception classes
class FijiNotFoundError(Exception): ...
class OptionError(Exception): ...