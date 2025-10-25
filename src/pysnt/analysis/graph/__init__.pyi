"""Comprehensive type stubs for Java classes."""

from typing import Any, List, Dict, Optional, Union, overload, Set, Callable

class DirectedWeightedGraph:
    """
    SNT DirectedWeightedGraph class.
    
    This class provides access to the Java DirectedWeightedGraph functionality.
    All methods and properties are dynamically resolved at runtime.
    """
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the DirectedWeightedGraph."""
        ...
    
    def __getattr__(self, name: str) -> Any:
        """Dynamic attribute access for Java methods and fields."""
        ...
    
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """Make the class callable if it has a default method."""
        ...

class DirectedWeightedSubgraph:
    """
    SNT DirectedWeightedSubgraph class.
    
    This class provides access to the Java DirectedWeightedSubgraph functionality.
    All methods and properties are dynamically resolved at runtime.
    """
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the DirectedWeightedSubgraph."""
        ...
    
    def __getattr__(self, name: str) -> Any:
        """Dynamic attribute access for Java methods and fields."""
        ...
    
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """Make the class callable if it has a default method."""
        ...

class GraphColorMapper:
    """
    SNT GraphColorMapper class.
    
    This class provides access to the Java GraphColorMapper functionality.
    All methods and properties are dynamically resolved at runtime.
    """
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the GraphColorMapper."""
        ...
    
    def __getattr__(self, name: str) -> Any:
        """Dynamic attribute access for Java methods and fields."""
        ...
    
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """Make the class callable if it has a default method."""
        ...

class GraphUtils:
    """
    SNT GraphUtils class.
    
    This class provides access to the Java GraphUtils functionality.
    All methods and properties are dynamically resolved at runtime.
    """
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the GraphUtils."""
        ...
    
    def __getattr__(self, name: str) -> Any:
        """Dynamic attribute access for Java methods and fields."""
        ...
    
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """Make the class callable if it has a default method."""
        ...

def _java_setup() -> Any: ...
def _discover_extended_classes() -> Any: ...
def get_available_classes() -> List[str]: ...
def get_class(class_name: str) -> Any: ...
def list_classes() -> Any: ...
def get_curated_classes() -> List[str]: ...
def get_extended_classes() -> List[str]: ...
def __getattr__(name: str) -> Any: ...
def __dir__() -> List[str]: ...

# Other functions
def __dir__(*args: Any, **kwargs: Any) -> Any: ...
def __getattr__(*args: Any, **kwargs: Any) -> Any: ...
def _discover_extended_classes(*args: Any, **kwargs: Any) -> Any: ...
def _java_setup(*args: Any, **kwargs: Any) -> Any: ...
def get_available_classes() -> Any: ...
def get_class() -> Any: ...
def get_curated_classes() -> Any: ...
def get_extended_classes() -> Any: ...
def list_classes() -> List[str]: ...

# Imported classes
class Any: ...
class Dict: ...
class List: ...

# Constants
CURATED_CLASSES: List[str]
EXTENDED_CLASSES: List[str]