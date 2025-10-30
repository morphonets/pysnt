"""Comprehensive type stubs for Java classes."""

from typing import Any, List, Dict, Optional, Union, overload, Set, Callable

class Dijkstra:
    """
    SNT Dijkstra class with complete method signatures.
    Generated using Java reflection.
    """

    def __init__(self) -> None:
        """Initialize Dijkstra."""
        ...

    # Methods
    def estimateCostToGoal(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> float: ...

    def __getattr__(self, name: str) -> Any:
        """Dynamic attribute access for additional methods."""
        ...

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """Make the class callable."""
        ...

class Euclidean:
    """
    SNT Euclidean class with complete method signatures.
    Generated using Java reflection.
    """

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: Any) -> None: ...
    @overload
    def __init__(self, arg0: Any) -> None: ...

    # Methods
    def estimateCostToGoal(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> float: ...

    def __getattr__(self, name: str) -> Any:
        """Dynamic attribute access for additional methods."""
        ...

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """Make the class callable."""
        ...

class Heuristic:
    """
    SNT Heuristic class with complete method signatures.
    Generated using Java reflection.
    """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize Heuristic."""
        ...

    # Methods
    def estimateCostToGoal(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> float: ...

    def __getattr__(self, name: str) -> Any:
        """Dynamic attribute access for additional methods."""
        ...

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """Make the class callable."""
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