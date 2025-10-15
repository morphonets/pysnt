"""
Type stubs for pysnt main package.

This file provides comprehensive type hints for IDEs and static type checkers
for better autocompletion and type checking support.
"""

from typing import Any, List, Optional, Union, Literal
from types import ModuleType

# Type aliases for better type hints
JavaClass = Any  # Represents a Java class imported via scyjava
ImageJMode = Literal["headless", "gui", "interactive", "interactive:force"]

# Module metadata
__version__: str
__author__: str
__all__: List[str]

# Constants
CURATED_ROOT_CLASSES: List[str]

# Root SNT classes - always available for direct import
# These are Java classes from sc.fiji.snt package
SNTService: Optional[JavaClass]
SNTUtils: Optional[JavaClass]
Tree: Optional[JavaClass]
Path: Optional[JavaClass]

# Submodule classes (backward compatibility imports)
# These are imported from submodules for convenience
TreeStatistics: Optional[JavaClass]  # from pysnt.analysis
PointInImage: Optional[JavaClass]    # from pysnt.util
SWCPoint: Optional[JavaClass]        # from pysnt.util

# Core functions
def initialize_snt(
    fiji_path: Optional[str] = None,
    interactive: bool = True,
    ensure_java: bool = True,
    mode: ImageJMode = "headless"
) -> None:
    """
    Initialize the SNT environment with ImageJ/Fiji.
    
    Parameters
    ----------
    fiji_path : str, optional
        Path to Fiji installation. If None, will try to auto-detect.
    interactive : bool, default True
        Whether to prompt user for Fiji path if not found automatically.
        Set to False for non-interactive environments (CI, scripts, etc.).
    ensure_java : bool, default True
        Whether to check and ensure Java is available.
    mode : ImageJMode, default "headless"
        ImageJ initialization mode.
        
    Raises
    ------
    RuntimeError
        If initialization fails or Fiji is not found.
    """
    ...

# Version functions
def version(detailed: bool = False) -> str:
    """
    Get pySNT version information.
    
    Parameters
    ----------
    detailed : bool, default False
        If True, returns detailed version information including dependencies.
        
    Returns
    -------
    str
        Version information string.
    """
    ...

def print_version(detailed: bool = False) -> None:
    """
    Print pySNT version information.
    
    Parameters
    ----------
    detailed : bool, default False
        If True, prints detailed version information including dependencies.
    """
    ...

def show_version(detailed: bool = False) -> None:
    """Alias for print_version()."""
    ...

def info() -> None:
    """Show detailed pySNT information (alias for print_version(detailed=True))."""
    ...

# Class access functions - consistent with submodules
def get_available_classes() -> List[str]:
    """
    Get list of all available classes from the root SNT package.
    
    Returns
    -------
    List[str]
        List of available class names.
    """
    ...

def get_class(class_name: str) -> JavaClass:
    """
    Get a specific SNT class by name from the root package.
    
    Parameters
    ----------
    class_name : str
        Name of the class to retrieve from sc.fiji.snt package.
        
    Returns
    -------
    JavaClass
        The requested SNT class.
        
    Raises
    ------
    KeyError
        If the class is not available.
    RuntimeError
        If the JVM has not been started.
    """
    ...

def get_curated_classes() -> List[str]:
    """
    Get list of curated classes that are always available for direct import.
    
    Returns
    -------
    List[str]
        List of curated class names from the root SNT package.
    """
    ...

def get_extended_classes() -> List[str]:
    """
    Get list of extended classes available via get_class().
    
    Returns
    -------
    List[str]
        Empty list (root package discovers classes dynamically).
    """
    ...

def list_classes() -> None:
    """Print all available root SNT classes organized by tier."""
    ...

# Submodules - these are actual module objects
analysis: ModuleType
util: ModuleType
viewer: ModuleType
tracing: ModuleType

# Dynamic attribute access support
def __getattr__(name: str) -> Any:
    """
    Provide dynamic access to root SNT classes.
    
    This allows importing root classes that were discovered at runtime.
    """
    ...