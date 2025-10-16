"""
PySNT: Python interface for SNT

This package provides convenient Python access to SNT's Java classes, including
`core classes <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/package-summary.html>`__.
"""

__version__ = "0.0.1"
__author__ = "SNT contributors"

import logging
import scyjava
from typing import Dict, Any, List

logger = logging.getLogger(__name__)

# Import main initialization
from .core import initialize, FijiNotFoundError

# Import Java utilities
from .java_utils import inspect

# Import setup utilities for Fiji configuration
from .setup_utils import (
    set_fiji_path, get_fiji_path, clear_fiji_path, reset_fiji_path,
    get_config_info, show_config_status, auto_detect_and_configure,
    is_fiji_valid, get_fiji_status
)

# Curated classes from root sc.fiji.snt package - always available for direct import
CURATED_ROOT_CLASSES = [
    "Fill",
    "Path", "PathAndFillManager", "PathFitter", "PathManagerUI",
    "SNT", "SNTService", "SNTUI", "SNTUtils",
    "TracerCanvas", "Tree", "TreeProperties"
]

# Global registries for root classes
_root_classes: Dict[str, Any] = {}

# Make root classes None initially (will be set by _java_setup)

class SNTService:
    """
    SNT's Scijava Service
    
    NB: Only available after calling pysnt.initialize().
    """
    pass

class SNTUtils:
    """
    """
    @staticmethod
    def getVersion():
        """Placeholder method. Call pysnt.initialize() first."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

    @staticmethod
    def isDebugMode():
        """Placeholder method. Call pysnt.initialize() first."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

    @staticmethod
    def setDebugMode(arg0):
        """Placeholder method. Call pysnt.initialize() first."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

    def __getattr__(self, name: str):
        """Dynamic attribute access for additional Java methods."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

class Tree:
    """
    """
    def size(self):
        """Placeholder method. Call pysnt.initialize() first."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

    def isEmpty(self):
        """Placeholder method. Call pysnt.initialize() first."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

    def getNodes(self):
        """Placeholder method. Call pysnt.initialize() first."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

    def getPaths(self):
        """Placeholder method. Call pysnt.initialize() first."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

    def getBoundingBox(self):
        """Placeholder method. Call pysnt.initialize() first."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

    def getRoot(self):
        """Placeholder method. Call pysnt.initialize() first."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

    def getTips(self):
        """Placeholder method. Call pysnt.initialize() first."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

    def getBranchPoints(self):
        """Placeholder method. Call pysnt.initialize() first."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

    def getCableLength(self):
        """Placeholder method. Call pysnt.initialize() first."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

    def getSWCTypes(self):
        """Placeholder method. Call pysnt.initialize() first."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

    def getLabel(self):
        """Placeholder method. Call pysnt.initialize() first."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

    def setLabel(self, arg0):
        """Placeholder method. Call pysnt.initialize() first."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

    def getColor(self):
        """Placeholder method. Call pysnt.initialize() first."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

    def setColor(self, arg0):
        """Placeholder method. Call pysnt.initialize() first."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

    def translate(self, arg0, arg1, arg2):
        """Placeholder method. Call pysnt.initialize() first."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

    def scale(self, arg0):
        """Placeholder method. Call pysnt.initialize() first."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

    def rotate(self, arg0, arg1):
        """Placeholder method. Call pysnt.initialize() first."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

    def save(self, arg0):
        """Placeholder method. Call pysnt.initialize() first."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

    def saveAsSWC(self, arg0):
        """Placeholder method. Call pysnt.initialize() first."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

    def __getattr__(self, name: str):
        """Dynamic attribute access for additional Java methods."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

class Path:
    """
    """
    def size(self):
        """Placeholder method. Call pysnt.initialize() first."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

    def getNodes(self):
        """Placeholder method. Call pysnt.initialize() first."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

    def getLength(self):
        """Placeholder method. Call pysnt.initialize() first."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

    def getStartRadius(self):
        """Placeholder method. Call pysnt.initialize() first."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

    def getEndRadius(self):
        """Placeholder method. Call pysnt.initialize() first."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

    def getSWCType(self):
        """Placeholder method. Call pysnt.initialize() first."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

    def setSWCType(self, arg0):
        """Placeholder method. Call pysnt.initialize() first."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

    def getChannel(self):
        """Placeholder method. Call pysnt.initialize() first."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

    def setChannel(self, arg0):
        """Placeholder method. Call pysnt.initialize() first."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

    def __getattr__(self, name: str):
        """Dynamic attribute access for additional Java methods."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

# Import submodules for easy access
from . import analysis
from . import util
from . import viewer
from . import tracing


def _java_setup():
    """
    Lazy initialization function for root SNT classes.
    
    This loads curated classes from sc.fiji.snt package immediately.
    
    Do not call this directly; use scyjava.start_jvm() instead.
    This function is automatically called when the JVM starts.
    """
    global _root_classes, SNTService, SNTUtils, Tree, Path
    
    try:
        package_name = "sc.fiji.snt"
        
        # Import curated root classes immediately
        for class_name in CURATED_ROOT_CLASSES:
            try:
                full_class_name = f"{package_name}.{class_name}"
                java_class = scyjava.jimport(full_class_name)
                _root_classes[class_name] = java_class
                
                # Replace placeholder class with actual Java class
                globals()[class_name] = java_class
                
                logger.debug(f"Loaded root class: {class_name}")
                
            except Exception as e:
                logger.warning(f"Failed to load root class {class_name}: {e}")
                # Set to None so users get clear error messages
                globals()[class_name] = None
        
        # Update module-level variables for IDE support
        SNTService = _root_classes.get("SNTService")
        SNTUtils = _root_classes.get("SNTUtils")
        Tree = _root_classes.get("Tree")
        Path = _root_classes.get("Path")
        
        logger.info(f"Successfully loaded {len(_root_classes)} root SNT classes")
        
    except Exception as e:
        logger.error(f"Failed to load root SNT classes: {e}")
        raise ImportError(f"Could not load root SNT classes: {e}") from e


# Register the setup function to run when JVM starts
scyjava.when_jvm_starts(_java_setup)


def get_class(class_name: str) -> Any:
    """
    Get a specific SNT class by name from the root package.
    
    This method provides access to classes from the sc.fiji.snt package.
    For classes from subpackages, use the respective module's get_class() method.
    
    Parameters
    ----------
    class_name : str
        Name of the class to retrieve from sc.fiji.snt package.
        
    Returns
    -------
    Java class
        The requested SNT class.
        
    Raises
    ------
    KeyError
        If the class is not available.
    RuntimeError
        If the JVM has not been started.
        
    Examples
    --------
    >>> # Get curated root classes
    >>> SNTService = get_class("SNTService")
    >>> Tree = get_class("Tree")
    >>> 
    >>> # Get other root package classes
    >>> PathFitter = get_class("PathFitter")
    """
    if not scyjava.jvm_started():
        raise RuntimeError(
            "JVM not started. Call pysnt.initialize() first."
        )
    
    # Check curated root classes first (fast path)
    if class_name in _root_classes:
        return _root_classes[class_name]
    
    # Try to import directly if not in curated list
    try:
        full_class_name = f"sc.fiji.snt.{class_name}"
        java_class = scyjava.jimport(full_class_name)
        return java_class
    except Exception:
        pass
    
    # Class not found - provide helpful error
    available = list(_root_classes.keys())
    if available:
        available_str = ", ".join(sorted(available))
        raise KeyError(f"Class '{class_name}' not found. Available: {available_str}")
    else:
        raise KeyError(f"Class '{class_name}' not found. No classes loaded.")


def get_available_classes() -> List[str]:
    """
    Get list of all available classes from the root SNT package.
    
    This includes curated classes that are always loaded. Unlike submodules,
    the root package doesn't have extended classes since all root classes
    are discovered dynamically via direct import.
    
    Returns
    -------
    List[str]
        List of available class names.
    """
    if not scyjava.jvm_started():
        return CURATED_ROOT_CLASSES.copy()
    
    return sorted(_root_classes.keys())


def get_curated_classes() -> List[str]:
    """
    Get list of curated classes that are always available for direct import.
    
    Returns
    -------
    List[str]
        List of curated class names from the root SNT package.
    """
    return CURATED_ROOT_CLASSES.copy()


def get_extended_classes() -> List[str]:
    """
    Get list of extended classes available via get_class().
    
    Note: The root package doesn't pre-define extended classes like submodules do.
    Any class from sc.fiji.snt package can be accessed via get_class() even if
    not in the curated list.
    
    Returns
    -------
    List[str]
        Empty list (root package discovers classes dynamically).
    """
    return []


def list_classes():
    """
    Print all available root SNT classes organized by tier.
    """
    if not scyjava.jvm_started():
        print("JVM not started. Only curated classes listed.")
        print("\nCurated Classes (always available):")
        print("=" * 40)
        for class_name in CURATED_ROOT_CLASSES:
            print(f"  • {class_name}")
        return
    
    print("Available SNT Root Classes:")
    print("=" * 40)
    
    # Show curated classes
    print("\n📌 Curated Classes (direct import):")
    for class_name in sorted(_root_classes.keys()):
        status = "✅" if _root_classes[class_name] is not None else "❌"
        print(f"  {status} {class_name}")
    
    print(f"\n💡 Extended Classes:")
    print("  Any class from sc.fiji.snt package can be accessed via get_class()")
    print("  even if not in the curated list above.")
    
    total = len(_root_classes)
    print(f"\nTotal curated: {total} classes")


# Dynamic __getattr__ to provide access to root classes
def __getattr__(name: str) -> Any:
    """
    Provide dynamic access to root SNT classes.
    
    This allows importing root classes that were discovered at runtime,
    but prioritizes curated classes for performance.
    """
    # Check if it's a curated root class that failed to load
    if name in CURATED_ROOT_CLASSES:
        if name in _root_classes:
            return _root_classes[name]
        else:
            raise AttributeError(f"Curated root class '{name}' failed to load. Check SNT installation.")
    
    # Try to get root class directly
    try:
        return get_class(name)
    except (KeyError, RuntimeError):
        # Provide helpful error message
        available_curated = ", ".join(CURATED_ROOT_CLASSES)
        raise AttributeError(
            f"Class '{name}' not found. "
            f"Curated classes: {available_curated}. "
            f"Use get_class('{name}') for other root classes."
        )

def version(detailed: bool = False) -> str:
    """
    Get PySNT version information.
    
    Parameters
    ----------
    detailed : bool, default False
        If True, returns detailed version information including dependencies.
        If False, returns just the pysnt version string.
        
    Returns
    -------
    str
        Version information string
        
    Examples
    --------
    >>> import pysnt
    >>> pysnt.version()
    '0.1.0'
    >>> 
    >>> pysnt.version(detailed=True)
    # Displays detailed version information
    """
    if not detailed:
        return __version__
    
    return _get_detailed_version_info()


def _get_detailed_version_info() -> str:
    """
    Get detailed version information including dependencies.
    
    Returns
    -------
    str
        Detailed version information
    """
    import sys
    import platform
    from pathlib import Path
    
    lines = [
        "PySNT Version Information", "=" * 35,
        f"PySNT version: {__version__}",
        f"Author: {__author__}",
        f"\nPython Environment:",
        f"Python version: {sys.version.split()[0]}",
        f"Python executable: {sys.executable}",
        f"Platform: {platform.platform()}",
        f"Architecture: {platform.machine()}",
        f"\n📦 Core Dependencies:"
    ]
    
    # Header

    # pysnt version

    # Python environment

    # Core dependencies

    dependencies = [
        ("scyjava", "SciJava Python bridge"),
        ("imagej", "PyImageJ"),
        ("numpy", "NumPy"),
        ("jdk", "install-jdk library (OpenJDK installer)"),
    ]
    
    for dep_name, description in dependencies:
        try:
            if dep_name == "imagej":
                import imagej
                version = getattr(imagej, '__version__', 'unknown')
            elif dep_name == "jdk":
                import jdk
                version = getattr(jdk, '__version__', 'unknown')
            else:
                module = __import__(dep_name)
                version = getattr(module, '__version__', 'unknown')
            
            lines.append(f"  ✅ {dep_name:<12} {version:<12} ({description})")
            
        except ImportError:
            lines.append(f"  ❌ {dep_name:<12} {'not found':<12} ({description})")
        except Exception as e:
            lines.append(f"  ⚠️  {dep_name:<12} {'error':<12} ({description}) - {e}")
    
    # Java information
    lines.append(f"\n☕ Java Environment:")
    
    try:
        from .java_utils import check_java_installation
        java_info = check_java_installation()
        
        if java_info['available']:
            lines.append(f"  ✅ Java version: {java_info['version']} ({java_info['vendor'] or 'Unknown vendor'})")
            lines.append(f"  📍 Java executable: {java_info['executable']}")
            if java_info['java_home']:
                lines.append(f"  🏠 JAVA_HOME: {java_info['java_home']}")
            else:
                lines.append(f"  🏠 JAVA_HOME: Not set")
        else:
            lines.append(f"  ❌ Java not found")
            
    except Exception as e:
        lines.append(f"  ⚠️  Java check failed: {e}")
    
    # SNT/Fiji information
    lines.append(f"\n🔬 SNT/Fiji Environment:")
    
    try:
        from .core import is_initialized, get_ij
        
        if is_initialized():
            lines.append(f"  ✅ PySNT initialized: Yes")
            
            try:
                ij = get_ij()
                ij_version = ij.getVersion() if ij else "Unknown"
                lines.append(f"  ℹ️ ImageJ version: {ij_version}")
                
                # Try to get SNT version
                try:
                    import scyjava
                    if scyjava.jvm_started():
                        SNTUtils = scyjava.jimport('sc.fiji.snt.SNTUtils')
                        snt_version = SNTUtils.VERSION
                        lines.append(f"  ℹ️ SNT version: {snt_version}")
                    else:
                        lines.append(f"  ℹ️ SNT version: JVM not started")
                except Exception as e:
                    lines.append(f"  ℹ️ SNT version: Could not determine ({e})")
                    
            except Exception as e:
                lines.append(f"  ⚠️  ImageJ access failed: {e}")
        else:
            lines.append(f"  ❌ PySNT initialized: No (call pysnt.initialize())")
            
    except Exception as e:
        lines.append(f"  ⚠️  Initialization check failed: {e}")
    
    # Installation path
    lines.append(f"\n📁 Installation:")
    try:
        pysnt_path = Path(__file__).parent
        lines.append(f"  📍 PySNT location: {pysnt_path}")
    except:
        lines.append(f"  📍 PySNT location: Unknown")
    
    # System information
    lines.append(f"\n💻 System Information:")
    lines.append(f"  OS: {platform.system()} {platform.release()}")
    lines.append(f"  CPU: {platform.processor() or 'Unknown'}")
    
    try:
        import psutil
        memory = psutil.virtual_memory()
        lines.append(f"  Memory: {memory.total // (1024**3)} GB total, {memory.available // (1024**3)} GB available")
    except ImportError:
        lines.append(f"  Memory: Unknown (install psutil for memory info)")
    except:
        lines.append(f"  Memory: Could not determine")
    
    return "\n".join(lines)


def print_version(detailed: bool = False):
    """
    Print PySNT version information.
    
    Parameters
    ----------
    detailed : bool, default False
        If True, prints detailed version information including dependencies.
        If False, prints just the PySNT version.
        
    Examples
    --------
    >>> import pysnt
    >>> pysnt.print_version()
    pysnt version: 0.1.0
    >>> 
    >>> pysnt.print_version(detailed=True)
    # Displays detailed version information
    """
    if detailed:
        print(_get_detailed_version_info())
    else:
        print(f"PySNT version: {__version__}")


# Convenience aliases
def show_version(detailed: bool = False):
    """Alias for print_version()."""
    print_version(detailed=detailed)


def info():
    """Show detailed PySNT information (alias for print_version(detailed=True))."""
    print_version(detailed=True)


__all__ = [
    # Functions
    "initialize",
    "inspect",
    # Exceptions
    "FijiNotFoundError",
    "version",
    "print_version", 
    "show_version",
    "info",
    "get_available_classes",
    "get_class",
    "get_curated_classes",
    "get_extended_classes",
    "list_classes",
    # Setup utilities
    "set_fiji_path",
    "get_fiji_path", 
    "clear_fiji_path",
    "reset_fiji_path",
    "get_config_info",
    "show_config_status",
    "auto_detect_and_configure",
    "is_fiji_valid",
    "get_fiji_status",
    # Constants
    "CURATED_ROOT_CLASSES",
    # Root SNT classes (sc.fiji.snt.*)
    "SNTService",
    "SNTUtils",
    "Tree", 
    "Path",
    # Submodules
    "analysis",
    "util", 
    "viewer",
    "tracing",
]