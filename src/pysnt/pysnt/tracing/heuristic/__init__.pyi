"""Comprehensive type stubs for Java classes."""

from typing import Any, List, Dict, Optional, Union, overload, Set, Callable

class Dijkstra:
    """
    SNT Dijkstra class (type stub).
    
    This class provides access to the Java Dijkstra functionality.
    At runtime, this is handled by the dynamic placeholder system in setup_module_classes().
    All methods and properties are dynamically resolved at runtime.
    """
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the Dijkstra."""
        ...
    
    def __getattr__(self, name: str) -> Any:
        """Dynamic attribute access for Java methods and fields."""
        ...
    
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """Make the class callable if it has a default method."""
        ...

class Euclidean:
    """
    SNT Euclidean class (type stub).
    
    This class provides access to the Java Euclidean functionality.
    At runtime, this is handled by the dynamic placeholder system in setup_module_classes().
    All methods and properties are dynamically resolved at runtime.
    """
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the Euclidean."""
        ...
    
    def __getattr__(self, name: str) -> Any:
        """Dynamic attribute access for Java methods and fields."""
        ...
    
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """Make the class callable if it has a default method."""
        ...

class Heuristic:
    """
    SNT Heuristic class (type stub).
    
    This class provides access to the Java Heuristic functionality.
    At runtime, this is handled by the dynamic placeholder system in setup_module_classes().
    All methods and properties are dynamically resolved at runtime.
    """
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the Heuristic."""
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