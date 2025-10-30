"""Comprehensive type stubs for Java classes."""

from typing import Any, List, Dict, Optional, Union, overload, Set, Callable

class Difference:
    """
    SNT Difference class with complete method signatures.
    Generated using Java reflection.
    """

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: float, arg1: float) -> None: ...

    # Methods
    def costMovingTo(self, arg0: float) -> float: ...
    def minStepCost(self) -> float: ...

    def __getattr__(self, name: str) -> Any:
        """Dynamic attribute access for additional methods."""
        ...

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """Make the class callable."""
        ...

class DifferenceSq:
    """
    SNT DifferenceSq class with complete method signatures.
    Generated using Java reflection.
    """

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: float, arg1: float) -> None: ...

    # Fields
    MIN_COST_PER_UNIT_DISTANCE: float

    # Methods
    def costMovingTo(self, arg0: float) -> float: ...
    def minStepCost(self) -> float: ...

    def __getattr__(self, name: str) -> Any:
        """Dynamic attribute access for additional methods."""
        ...

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """Make the class callable."""
        ...

class OneMinusErf:
    """
    SNT OneMinusErf class with complete method signatures.
    Generated using Java reflection.
    """

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float) -> None: ...

    # Methods
    def costMovingTo(self, arg0: float) -> float: ...
    def getZFudge(self) -> float: ...
    def minStepCost(self) -> float: ...
    def setZFudge(self, arg0: float) -> None: ...

    def __getattr__(self, name: str) -> Any:
        """Dynamic attribute access for additional methods."""
        ...

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """Make the class callable."""
        ...

class Reciprocal:
    """
    SNT Reciprocal class with complete method signatures.
    Generated using Java reflection.
    """

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: float, arg1: float) -> None: ...

    # Fields
    RECIPROCAL_FUDGE: float
    CONST_8: float
    MIN_COST_PER_UNIT_DISTANCE: float

    # Methods
    def costMovingTo(self, arg0: float) -> float: ...
    def minStepCost(self) -> float: ...

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