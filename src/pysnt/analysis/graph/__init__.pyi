"""Comprehensive type stubs for Java classes."""

from typing import Any, List, Dict, Optional, Union, overload, Set, Callable

class AnnotationGraph:
    """
    SNT AnnotationGraph class (type stub).
    
    This class provides access to the Java AnnotationGraph functionality.
    At runtime, this is handled by the dynamic placeholder system in setup_module_classes().
    All methods and properties are dynamically resolved at runtime.
    """
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the AnnotationGraph."""
        ...
    
    def __getattr__(self, name: str) -> Any:
        """Dynamic attribute access for Java methods and fields."""
        ...
    
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """Make the class callable if it has a default method."""
        ...

class DirectedWeightedGraph:
    """
    SNT DirectedWeightedGraph class (type stub).
    
    This class provides access to the Java DirectedWeightedGraph functionality.
    At runtime, this is handled by the dynamic placeholder system in setup_module_classes().
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
    SNT DirectedWeightedSubgraph class (type stub).
    
    This class provides access to the Java DirectedWeightedSubgraph functionality.
    At runtime, this is handled by the dynamic placeholder system in setup_module_classes().
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

class SNTGraph:
    """
    SNT SNTGraph class (type stub).
    
    This class provides access to the Java SNTGraph functionality.
    At runtime, this is handled by the dynamic placeholder system in setup_module_classes().
    All methods and properties are dynamically resolved at runtime.
    """
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the SNTGraph."""
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
def list_classes() -> None: ...
def get_curated_classes() -> List[str]: ...
def get_extended_classes() -> List[str]: ...
def __getattr__(name: str) -> Any: ...
def __dir__() -> List[str]: ...

# Imported classes
class Any: ...
class Dict: ...
class List: ...

# Constants
CURATED_CLASSES: List[str]
EXTENDED_CLASSES: List[str]