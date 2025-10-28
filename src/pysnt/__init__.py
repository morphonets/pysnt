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
from .core import initialize, FijiNotFoundError, ij

# Import PyImageJ integration functions
from .core import to_python, from_java, show

# Import converter utilities
from .converters import (
    register_snt_converters, register_display_handler, list_converters, display, enhance_java_object
)

# Import Java utilities
from .java_utils import inspect, get_methods, get_fields, find_members

# Import setup utilities for Fiji configuration
from .setup_utils import (
    set_fiji_path,
    get_fiji_path,
    clear_fiji_path,
    reset_fiji_path,
    get_config_info,
    show_config_status,
    auto_detect_and_configure,
    is_fiji_valid,
    get_fiji_status,
)

# Import common module functionality
from .common_module import setup_module_classes

# Import configuration system
from .config import (
    get_option, set_option, reset_option, describe_option, list_options,
    option_context, options, OptionError
)

# Import GUI utilities
from .gui_utils import (
    configure_gui_safety, safe_gui_call, is_main_thread, is_macos
)

# Curated classes from root sc.fiji.snt package - always available for direct import
CURATED_ROOT_CLASSES = [
    "Fill",
    "FillConverter",
    "InteractiveTracerCanvas",
    "Path",
    "PathAndFillManager",
    "PathChangeListener",
    "PathDownsampler",
    "PathFitter",
    "PathManagerUI",
    "SciViewSNT",
    "SNT",
    "SNTService",
    "SNTUI",
    "SNTUtils",
    "TracerCanvas",
    "Tree",
    "TreeProperties",
]

# Extended classes - available via get_class() (root package discovers dynamically)
EXTENDED_ROOT_CLASSES = [
    "BookmarkManager",
    "ClarifyingKeyListener",
    "DelineationsManager",
    "FillerProgressCallback",
    "FillManagerUI",
    "FittingProgress",
    "HessianGenerationCallback",
    "MultiTaskProgress",
    "NearPoint",
    "NormalPlaneCanvas",
    "NotesUI",
    "PathAndFillListener",
    "PathChangeEvent",
    "PathChangeListener",
    "PathNodeCanvas",
    "PathTransformer",
    "QueueJumpingKeyListener",
    "SearchProgressCallback",
    "SNTPrefs",
]


# Placeholder classes for IDE support - will be replaced with Java classes
class Fill:
    """
    Curated SNT class from root package with method signatures.
    
    Available for direct import after JVM initialization.
    Call pysnt.initialize() before using this class.
    
    See `Javadoc Documentation`_.
    
    .. _Javadoc Documentation: https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/Fill.html
    """
    
    def __getattr__(self, name: str):
        """Dynamic attribute access for Java methods."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")
    
    def __init__(self, *args, **kwargs):
        """Placeholder constructor."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

class FillConverter:
    """
    Curated SNT class from root package with method signatures.
    
    Available for direct import after JVM initialization.
    Call pysnt.initialize() before using this class.
    
    See `Javadoc Documentation`_.
    
    .. _Javadoc Documentation: https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/FillConverter.html
    """
    
    def __getattr__(self, name: str):
        """Dynamic attribute access for Java methods."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")
    
    def __init__(self, *args, **kwargs):
        """Placeholder constructor."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

class InteractiveTracerCanvas:
    """
    Curated SNT class from root package with method signatures.
    
    Available for direct import after JVM initialization.
    Call pysnt.initialize() before using this class.
    
    See `Javadoc Documentation`_.
    
    .. _Javadoc Documentation: https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/InteractiveTracerCanvas.html
    """
    
    def __getattr__(self, name: str):
        """Dynamic attribute access for Java methods."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")
    
    def __init__(self, *args, **kwargs):
        """Placeholder constructor."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

class Path:
    """
    Curated SNT class from root package with method signatures.
    
    Available for direct import after JVM initialization.
    Call pysnt.initialize() before using this class.
    
    See `Javadoc Documentation`_.
    
    .. _Javadoc Documentation: https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/Path.html
    """
    
    def __getattr__(self, name: str):
        """Dynamic attribute access for Java methods."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")
    
    def __init__(self, *args, **kwargs):
        """Placeholder constructor."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

class PathAndFillManager:
    """
    Curated SNT class from root package with method signatures.
    
    Available for direct import after JVM initialization.
    Call pysnt.initialize() before using this class.
    
    See `Javadoc Documentation`_.
    
    .. _Javadoc Documentation: https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/PathAndFillManager.html
    """
    
    def __getattr__(self, name: str):
        """Dynamic attribute access for Java methods."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")
    
    def __init__(self, *args, **kwargs):
        """Placeholder constructor."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

class PathChangeListener:
    """
    Curated SNT class from root package with method signatures.
    
    Available for direct import after JVM initialization.
    Call pysnt.initialize() before using this class.
    
    See `Javadoc Documentation`_.
    
    .. _Javadoc Documentation: https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/PathChangeListener.html
    """
    
    def __getattr__(self, name: str):
        """Dynamic attribute access for Java methods."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")
    
    def __init__(self, *args, **kwargs):
        """Placeholder constructor."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

class PathDownsampler:
    """
    Curated SNT class from root package with method signatures.
    
    Available for direct import after JVM initialization.
    Call pysnt.initialize() before using this class.
    
    See `Javadoc Documentation`_.
    
    .. _Javadoc Documentation: https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/PathDownsampler.html
    """
    
    def __getattr__(self, name: str):
        """Dynamic attribute access for Java methods."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")
    
    def __init__(self, *args, **kwargs):
        """Placeholder constructor."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

class PathFitter:
    """
    Curated SNT class from root package with method signatures.
    
    Available for direct import after JVM initialization.
    Call pysnt.initialize() before using this class.
    
    See `Javadoc Documentation`_.
    
    .. _Javadoc Documentation: https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/PathFitter.html
    """
    
    def __getattr__(self, name: str):
        """Dynamic attribute access for Java methods."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")
    
    def __init__(self, *args, **kwargs):
        """Placeholder constructor."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

class PathManagerUI:
    """
    Curated SNT class from root package with method signatures.
    
    Available for direct import after JVM initialization.
    Call pysnt.initialize() before using this class.
    
    See `Javadoc Documentation`_.
    
    .. _Javadoc Documentation: https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/PathManagerUI.html
    """
    
    def __getattr__(self, name: str):
        """Dynamic attribute access for Java methods."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")
    
    def __init__(self, *args, **kwargs):
        """Placeholder constructor."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

class SciViewSNT:
    """
    Curated SNT class from root package with method signatures.
    
    Available for direct import after JVM initialization.
    Call pysnt.initialize() before using this class.
    
    See `Javadoc Documentation`_.
    
    .. _Javadoc Documentation: https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/SciViewSNT.html
    """
    
    def __getattr__(self, name: str):
        """Dynamic attribute access for Java methods."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")
    
    def __init__(self, *args, **kwargs):
        """Placeholder constructor."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

class SNT:
    """
    Curated SNT class from root package with method signatures.
    
    Available for direct import after JVM initialization.
    Call pysnt.initialize() before using this class.
    
    See `Javadoc Documentation`_.
    
    .. _Javadoc Documentation: https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/SNT.html
    """
    
    def __getattr__(self, name: str):
        """Dynamic attribute access for Java methods."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")
    
    def __init__(self, *args, **kwargs):
        """Placeholder constructor."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

class SNTService:
    """
    Curated SNT class from root package with method signatures.
    
    Available for direct import after JVM initialization.
    Call pysnt.initialize() before using this class.
    
    See `Javadoc Documentation`_.
    
    .. _Javadoc Documentation: https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/SNTService.html
    """
    
    def __getattr__(self, name: str):
        """Dynamic attribute access for Java methods."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")
    
    def __init__(self, *args, **kwargs):
        """Placeholder constructor."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

class SNTUI:
    """
    Curated SNT class from root package with method signatures.
    
    Available for direct import after JVM initialization.
    Call pysnt.initialize() before using this class.
    
    See `Javadoc Documentation`_.
    
    .. _Javadoc Documentation: https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/SNTUI.html
    """
    
    def __getattr__(self, name: str):
        """Dynamic attribute access for Java methods."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")
    
    def __init__(self, *args, **kwargs):
        """Placeholder constructor."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

class SNTUtils:
    """
    Curated SNT class from root package with method signatures.
    
    Available for direct import after JVM initialization.
    Call pysnt.initialize() before using this class.
    
    See `Javadoc Documentation`_.
    
    .. _Javadoc Documentation: https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/SNTUtils.html
    """
    
    def __getattr__(self, name: str):
        """Dynamic attribute access for Java methods."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")
    
    def __init__(self, *args, **kwargs):
        """Placeholder constructor."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

class TracerCanvas:
    """
    Curated SNT class from root package with method signatures.
    
    Available for direct import after JVM initialization.
    Call pysnt.initialize() before using this class.
    
    See `Javadoc Documentation`_.
    
    .. _Javadoc Documentation: https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/TracerCanvas.html
    """
    
    def __getattr__(self, name: str):
        """Dynamic attribute access for Java methods."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")
    
    def __init__(self, *args, **kwargs):
        """Placeholder constructor."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

class Tree:
    """
    Curated SNT class from root package with method signatures.
    
    Available for direct import after JVM initialization.
    Call pysnt.initialize() before using this class.
    
    See `Javadoc Documentation`_.
    
    .. _Javadoc Documentation: https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/Tree.html
    """
    
    def __getattr__(self, name: str):
        """Dynamic attribute access for Java methods."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")
    
    def __init__(self, *args, **kwargs):
        """Placeholder constructor."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

class TreeProperties:
    """
    Curated SNT class from root package with method signatures.
    
    Available for direct import after JVM initialization.
    Call pysnt.initialize() before using this class.
    
    See `Javadoc Documentation`_.
    
    .. _Javadoc Documentation: https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/TreeProperties.html
    """
    
    def __getattr__(self, name: str):
        """Dynamic attribute access for Java methods."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")
    
    def __init__(self, *args, **kwargs):
        """Placeholder constructor."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

# Import submodules for easy access
from . import analysis
from . import util
from . import viewer
from . import tracing

# Setup common module functionality
_module_funcs = setup_module_classes(
    package_name="sc.fiji.snt",
    curated_classes=CURATED_ROOT_CLASSES,
    extended_classes=EXTENDED_ROOT_CLASSES,
    globals_dict=globals(),
)

# Import functions into module namespace
get_class = _module_funcs["get_class"]
get_available_classes = _module_funcs["get_available_classes"]
get_curated_classes = _module_funcs["get_curated_classes"]
get_extended_classes = _module_funcs["get_extended_classes"]
list_classes = _module_funcs["list_classes"]

# Create module-level __getattr__ and __dir__
__getattr__ = _module_funcs["create_getattr"]("pysnt")
__dir__ = _module_funcs["create_dir"]()

# Register the setup function to run when JVM starts
# This ensures that placeholder classes are replaced with actual Java classes
scyjava.when_jvm_starts(_module_funcs["_java_setup"])


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
        "PySNT Version Information",
        "=" * 35,
        f"PySNT version: {__version__}",
        f"Author: {__author__}",
        f"\nPython Environment:",
        f"Python version: {sys.version.split()[0]}",
        f"Python executable: {sys.executable}",
        f"Platform: {platform.platform()}",
        f"Architecture: {platform.machine()}",
        f"\n📦 Core Dependencies:",
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

                version = getattr(imagej, "__version__", "unknown")
            elif dep_name == "jdk":
                import jdk

                version = getattr(jdk, "__version__", "unknown")
            else:
                module = __import__(dep_name)
                version = getattr(module, "__version__", "unknown")

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

        if java_info["available"]:
            lines.append(
                f"  ✅ Java version: {java_info['version']} ({java_info['vendor'] or 'Unknown vendor'})"
            )
            lines.append(f"  📍 Java executable: {java_info['executable']}")
            if java_info["java_home"]:
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
        from .core import is_initialized, ij

        if is_initialized():
            lines.append(f"  ✅ PySNT initialized: Yes")

            try:
                ij_instance = ij()
                ij_version = ij_instance.getVersion() if ij_instance else "Unknown"
                lines.append(f"  ℹ️ ImageJ version: {ij_version}")

                # Try to get SNT version
                try:
                    import scyjava

                    if scyjava.jvm_started():
                        SNTUtils = scyjava.jimport("sc.fiji.snt.SNTUtils")
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
        lines.append(
            f"  Memory: {memory.total // (1024**3)} GB total, {memory.available // (1024**3)} GB available"
        )
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
    "ij",
    "inspect",
    "get_methods",
    "get_fields",
    "find_members",
    # PyImageJ integration
    "to_python",
    "from_java",  # backward compatibility alias
    "show", 
    # Converter utilities
    "register_snt_converters",
    "register_display_handler",
    "list_converters",
    "display",
    "enhance_java_object",
    # Configuration system
    "get_option",
    "set_option", 
    "reset_option",
    "describe_option",
    "list_options",
    "option_context",
    "options",
    # GUI utilities
    "configure_gui_safety",
    "safe_gui_call",
    "is_main_thread",
    "is_macos",
    # Exceptions
    "FijiNotFoundError",
    "OptionError",
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
    "EXTENDED_ROOT_CLASSES",
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
