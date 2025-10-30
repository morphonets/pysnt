"""Comprehensive type stubs for Java classes."""

from typing import Any, List, Dict, Optional, Union, overload, Set, Callable

class ConvexHull2D:
    """
    SNT ConvexHull2D class (type stub).
    
    This class provides access to the Java ConvexHull2D functionality.
    At runtime, this is handled by the dynamic placeholder system in setup_module_classes().
    All methods and properties are dynamically resolved at runtime.
    """
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the ConvexHull2D."""
        ...
    
    def __getattr__(self, name: str) -> Any:
        """Dynamic attribute access for Java methods and fields."""
        ...
    
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """Make the class callable if it has a default method."""
        ...

class ConvexHull3D:
    """
    SNT ConvexHull3D class (type stub).
    
    This class provides access to the Java ConvexHull3D functionality.
    At runtime, this is handled by the dynamic placeholder system in setup_module_classes().
    All methods and properties are dynamically resolved at runtime.
    """
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the ConvexHull3D."""
        ...
    
    def __getattr__(self, name: str) -> Any:
        """Dynamic attribute access for Java methods and fields."""
        ...
    
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """Make the class callable if it has a default method."""
        ...

class TreeStatistics:
    """
    SNT TreeStatistics class (type stub).
    
    This class provides access to the Java TreeStatistics functionality.
    At runtime, this is handled by the dynamic placeholder system in setup_module_classes().
    All methods and properties are dynamically resolved at runtime.
    """
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the TreeStatistics."""
        ...
    
    def __getattr__(self, name: str) -> Any:
        """Dynamic attribute access for Java methods and fields."""
        ...
    
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """Make the class callable if it has a default method."""
        ...

class MultiTreeStatistics:
    """
    SNT MultiTreeStatistics class (type stub).
    
    This class provides access to the Java MultiTreeStatistics functionality.
    At runtime, this is handled by the dynamic placeholder system in setup_module_classes().
    All methods and properties are dynamically resolved at runtime.
    """
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the MultiTreeStatistics."""
        ...
    
    def __getattr__(self, name: str) -> Any:
        """Dynamic attribute access for Java methods and fields."""
        ...
    
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """Make the class callable if it has a default method."""
        ...

class SNTChart:
    """
    SNT SNTChart class (type stub).
    
    This class provides access to the Java SNTChart functionality.
    At runtime, this is handled by the dynamic placeholder system in setup_module_classes().
    All methods and properties are dynamically resolved at runtime.
    """
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the SNTChart."""
        ...
    
    def show(self, **kwargs: Any) -> Any:
        """
        Display this object using enhanced conversion.
        
        This method first tries the original Java show() method, and if that fails,
        it falls back to display() which can handle SNT-specific conversions.
        """
        try:
            # Try to call the original Java show method via __getattr__
            original_show = object.__getattribute__(self, "__getattr__")("show")
            return original_show(**kwargs)
        except (AttributeError, TypeError, Exception):
            # Fallback to display
            from pysnt.converters import display
            return display(self, **kwargs)
    
    def __getattr__(self, name: str) -> Any:
        """Dynamic attribute access for Java methods and fields."""
        ...
    
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """Make the class callable if it has a default method."""
        ...

class SNTTable:
    """
    SNT SNTTable class (type stub).
    
    This class provides access to the Java SNTTable functionality.
    At runtime, this is handled by the dynamic placeholder system in setup_module_classes().
    All methods and properties are dynamically resolved at runtime.
    """
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the SNTTable."""
        ...
    
    def show(self, **kwargs: Any) -> Any:
        """
        Display this object using enhanced conversion.
        
        This method first tries the original Java show() method, and if that fails,
        it falls back to display() which can handle SNT-specific conversions.
        """
        try:
            # Try to call the original Java show method via __getattr__
            original_show = object.__getattribute__(self, "__getattr__")("show")
            return original_show(**kwargs)
        except (AttributeError, TypeError, Exception):
            # Fallback to display
            from pysnt.converters import display
            return display(self, **kwargs)
    
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