"""
PySNT: Python interface for SNT

This package provides convenient Python access to SNT's Java classes through scyjava et al.
"""

__version__ = "0.0.1"
__author__ = "SNT contributors"

import logging
import scyjava
from typing import Dict, Any, List, Optional

logger = logging.getLogger(__name__)

# Import main initialization
from .core import initialize_snt

# Curated classes from root sc.fiji.snt package - always available for direct import
CURATED_ROOT_CLASSES = [
    "SNTService",
    "SNTUtils", 
    "Tree",
    "Path",
]

# Global registries for root classes
_root_classes: Dict[str, Any] = {}

# Make root classes None initially (will be set by _java_setup)
SNTService: Optional[Any] = None
SNTUtils: Optional[Any] = None
Tree: Optional[Any] = None
Path: Optional[Any] = None

# Also import from submodules for backward compatibility
from .analysis import TreeStatistics
from .util import PointInImage, SWCPoint

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
                
                # Make available at module level for direct import
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


def get_root_class(class_name: str) -> Any:
    """
    Get a specific root SNT class by name.
    
    Parameters
    ----------
    class_name : str
        Name of the class to retrieve from sc.fiji.snt package.
        
    Returns
    -------
    Java class
        The requested SNT root class.
        
    Raises
    ------
    KeyError
        If the class is not available.
    RuntimeError
        If the JVM has not been started.
        
    Examples
    --------
    >>> # Get a curated root class
    >>> SNTService = get_root_class("SNTService")
    >>> SNTUtils = get_root_class("SNTUtils")
    """
    if not scyjava.jvm_started():
        raise RuntimeError(
            "JVM not started. Call pysnt.initialize_snt() first."
        )
    
    # Check curated root classes
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
        raise KeyError(f"Root class '{class_name}' not found. Available: {available_str}")
    else:
        raise KeyError(f"Root class '{class_name}' not found. No classes loaded.")


def get_curated_root_classes() -> List[str]:
    """
    Get list of curated root classes that are always available for direct import.
    
    Returns
    -------
    List[str]
        List of curated root class names.
    """
    return CURATED_ROOT_CLASSES.copy()


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
        return get_root_class(name)
    except (KeyError, RuntimeError):
        # Provide helpful error message
        available_curated = ", ".join(CURATED_ROOT_CLASSES)
        raise AttributeError(
            f"Class '{name}' not found. "
            f"Curated root classes: {available_curated}. "
            f"Use get_root_class('{name}') for other root classes."
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
    # Displays comprehensive version information
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
    
    lines = []
    
    # Header
    lines.append("PySNT Version Information")
    lines.append("=" * 35)
    
    # pysnt version
    lines.append(f"PySNT version: {__version__}")
    lines.append(f"Author: {__author__}")
    
    # Python environment
    lines.append(f"\nPython Environment:")
    lines.append(f"Python version: {sys.version.split()[0]}")
    lines.append(f"Python executable: {sys.executable}")
    lines.append(f"Platform: {platform.platform()}")
    lines.append(f"Architecture: {platform.machine()}")
    
    # Core dependencies
    lines.append(f"\n📦 Core Dependencies:")
    
    dependencies = [
        ("scyjava", "SciJava Python bridge"),
        ("imagej", "PyImageJ"),
        ("numpy", "NumPy"),
        ("jdk", "Java JDK installer"),
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
        from .core import is_initialized, get_imagej
        
        if is_initialized():
            lines.append(f"  ✅ PySNT initialized: Yes")
            
            try:
                ij = get_imagej()
                ij_version = ij.getVersion() if ij else "Unknown"
                lines.append(f"  📊 ImageJ version: {ij_version}")
                
                # Try to get SNT version
                try:
                    import scyjava
                    if scyjava.jvm_started():
                        SNTUtils = scyjava.jimport('sc.fiji.snt.SNTUtils')
                        snt_version = SNTUtils.VERSION
                        lines.append(f"  🧠 SNT version: {snt_version}")
                    else:
                        lines.append(f"  🧠 SNT version: JVM not started")
                except Exception as e:
                    lines.append(f"  🧠 SNT version: Could not determine ({e})")
                    
            except Exception as e:
                lines.append(f"  ⚠️  ImageJ access failed: {e}")
        else:
            lines.append(f"  ❌ PySNT initialized: No (call pysnt.initialize_snt())")
            
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
    # Displays comprehensive version information
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
    "initialize_snt",
    "version",
    "print_version", 
    "show_version",
    "info",
    "get_root_class",
    "get_curated_root_classes",
    # Constants
    "CURATED_ROOT_CLASSES",
    # Root SNT classes (sc.fiji.snt.*)
    "SNTService",
    "SNTUtils",
    "Tree", 
    "Path",
    # Submodule classes (for backward compatibility)
    "TreeStatistics",
    "PointInImage",
    "SWCPoint",
    # Submodules
    "analysis",
    "util", 
    "viewer",
    "tracing",
]