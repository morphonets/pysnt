"""Comprehensive type stubs for Java classes."""

from typing import Any, List, Dict, Optional, Union, overload, Set, Callable

class ShollOverlay:
    """
    SNT ShollOverlay class (type stub).
    
    This class provides access to the Java ShollOverlay functionality.
    At runtime, this is handled by the dynamic placeholder system in setup_module_classes().
    All methods and properties are dynamically resolved at runtime.
    """
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the ShollOverlay."""
        ...
    
    def __getattr__(self, name: str) -> Any:
        """Dynamic attribute access for Java methods and fields."""
        ...
    
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """Make the class callable if it has a default method."""
        ...

class ShollPlot:
    """
    SNT ShollPlot class (type stub).
    
    This class provides access to the Java ShollPlot functionality.
    At runtime, this is handled by the dynamic placeholder system in setup_module_classes().
    All methods and properties are dynamically resolved at runtime.
    """
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the ShollPlot."""
        ...
    
    def __getattr__(self, name: str) -> Any:
        """Dynamic attribute access for Java methods and fields."""
        ...
    
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """Make the class callable if it has a default method."""
        ...

class ShollTable:
    """
    SNT ShollTable class (type stub).
    
    This class provides access to the Java ShollTable functionality.
    At runtime, this is handled by the dynamic placeholder system in setup_module_classes().
    All methods and properties are dynamically resolved at runtime.
    """
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the ShollTable."""
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