"""Comprehensive type stubs for Java classes."""

from typing import Any, List, Dict, Optional, Union, overload, Set, Callable

class ShollAnalyzer:
    """
    SNT ShollAnalyzer class.
    
    This class provides access to the Java ShollAnalyzer functionality.
    All methods and properties are dynamically resolved at runtime.
    """
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the ShollAnalyzer."""
        ...
    
    def __getattr__(self, name: str) -> Any:
        """Dynamic attribute access for Java methods and fields."""
        ...
    
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """Make the class callable if it has a default method."""
        ...

class ShollChart:
    """
    SNT ShollChart class.
    
    This class provides access to the Java ShollChart functionality.
    All methods and properties are dynamically resolved at runtime.
    """
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the ShollChart."""
        ...
    
    def __getattr__(self, name: str) -> Any:
        """Dynamic attribute access for Java methods and fields."""
        ...
    
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """Make the class callable if it has a default method."""
        ...

class ShollProfile:
    """
    SNT ShollProfile class.
    
    This class provides access to the Java ShollProfile functionality.
    All methods and properties are dynamically resolved at runtime.
    """
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the ShollProfile."""
        ...
    
    def __getattr__(self, name: str) -> Any:
        """Dynamic attribute access for Java methods and fields."""
        ...
    
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """Make the class callable if it has a default method."""
        ...

class ShollUtils:
    """
    SNT ShollUtils class with complete method signatures.
    Generated using Java reflection.
    """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize ShollUtils."""
        ...

    # Fields
    URL: str

    # Methods
    @staticmethod
    def constantLUT(arg0: Any) -> Any: ...
    @staticmethod
    def csvSample() -> Any: ...
    @staticmethod
    def d2s(arg0: float) -> str: ...
    @staticmethod
    def demoProfile() -> Any: ...
    @staticmethod
    def extractHemiShellFlag(arg0: str) -> str: ...
    @staticmethod
    def getRadii(arg0: float, arg1: float, arg2: float) -> List[Any]: ...
    @staticmethod
    def sampleImage() -> Any: ...

    def __getattr__(self, name: str) -> Any:
        """Dynamic attribute access for additional methods."""
        ...

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """Make the class callable."""
        ...

# Module functions
def get_available_classes() -> List[str]: ...
def get_class(class_name: str) -> Any: ...
def list_classes() -> None: ...
def get_curated_classes() -> List[str]: ...
def get_extended_classes() -> List[str]: ...

CURATED_CLASSES: List[str]
EXTENDED_CLASSES: List[str]