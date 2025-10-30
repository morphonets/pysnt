"""Comprehensive type stubs for Java classes."""

from typing import Any, List, Dict, Optional, Union, overload, Set, Callable

class TestClass:
    """
    SNT TestClass class (type stub).
    
    This class provides access to the Java TestClass functionality.
    At runtime, this is handled by the dynamic placeholder system in setup_module_classes().
    All methods and properties are dynamically resolved at runtime.
    """
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the TestClass."""
        ...
    
    def __getattr__(self, name: str) -> Any:
        """Dynamic attribute access for Java methods and fields."""
        ...
    
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """Make the class callable if it has a default method."""
        ...

class ExampleAnalyzer:
    """
    SNT ExampleAnalyzer class (type stub).
    
    This class provides access to the Java ExampleAnalyzer functionality.
    At runtime, this is handled by the dynamic placeholder system in setup_module_classes().
    All methods and properties are dynamically resolved at runtime.
    """
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the ExampleAnalyzer."""
        ...
    
    def __getattr__(self, name: str) -> Any:
        """Dynamic attribute access for Java methods and fields."""
        ...
    
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """Make the class callable if it has a default method."""
        ...


# Other functions
def get_available_classes() -> Any: ...
def get_class(class_name: str) -> Any: ...
def get_curated_classes() -> Any: ...
def get_extended_classes() -> Any: ...
def list_classes() -> None: ...
def setup_module_classes(*args: Any, **kwargs: Any) -> Any: ...

# Imported classes
class Any: ...
class Dict: ...
class List: ...

# Constants
CURATED_CLASSES: List[str]
EXTENDED_CLASSES: List[str]