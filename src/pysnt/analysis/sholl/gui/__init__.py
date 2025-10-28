"""
This module provides convenient access to
`SNT's Sholl GUI classes <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/analysis/sholl/gui/package-summary.html>`__.
"""

import logging
import scyjava
from typing import Dict, Any, List

logger = logging.getLogger(__name__)

# Curated classes - always available for direct import
CURATED_CLASSES = [
    "ShollOverlay", "ShollPlot", "ShollTable"
]

# Extended classes - available via get_class() after discovery
EXTENDED_CLASSES = []

# Global registries
_curated_classes: Dict[str, Any] = {}
_extended_classes: Dict[str, Any] = {}
_discovery_completed: bool = False

# Make curated classes None initially (will be set by _java_setup)
# These explicit declarations ensure IDE autocompletion works

def _java_setup():
    """
    Lazy initialization function for Java-dependent Sholl GUI classes.
    
    This loads curated classes immediately and prepares extended classes
    for on-demand loading.
    
    Do not call this directly; use scyjava.start_jvm() instead.
    This function is automatically called when the JVM starts.
    """
    global _curated_classes, ShollPlot, ShollTable, ShollOverlay, ShollWidget
    
    try:
        package_name = "sc.fiji.snt.analysis.sholl.gui"
        
        # Import curated classes immediately
        for class_name in CURATED_CLASSES:
            try:
                full_class_name = f"{package_name}.{class_name}"
                java_class = scyjava.jimport(full_class_name)
                _curated_classes[class_name] = java_class
                
                # Make available at module level for direct import
                globals()[class_name] = java_class
                
                logger.debug(f"Loaded curated class: {class_name}")
                
            except Exception as e:
                logger.warning(f"Failed to load curated class {class_name}: {e}")
                # Set to None so users get clear error messages
                globals()[class_name] = None
        
        # Replace placeholder classes with actual Java classes
        if "ShollOverlay" in _curated_classes:
            globals()["ShollOverlay"] = _curated_classes["ShollOverlay"]
        if "ShollPlot" in _curated_classes:
            globals()["ShollPlot"] = _curated_classes["ShollPlot"]
        if "ShollTable" in _curated_classes:
            globals()["ShollTable"] = _curated_classes["ShollTable"]
        logger.info(f"Successfully loaded {len(_curated_classes)} curated Sholl GUI classes")
        
    except Exception as e:
        logger.error(f"Failed to load curated Sholl GUI classes: {e}")
        raise ImportError(f"Could not load curated Sholl GUI classes: {e}") from e

def _discover_extended_classes():
    """
    Discover and load extended classes on-demand.
    
    This is called the first time get_class() is used for a non-curated class.
    """
    global _extended_classes, _discovery_completed
    
    if _discovery_completed:
        return
    
    try:
        from ....java_utils import discover_java_classes
        
        package_name = "sc.fiji.snt.analysis.sholl.gui"
        
        # Discover all available classes
        all_classes = CURATED_CLASSES + EXTENDED_CLASSES
        discovered_classes = discover_java_classes(
            package_name,
            known_classes=all_classes,
            include_abstract=False,
            include_interfaces=False
        )
        
        # Load extended classes (excluding already loaded curated ones)
        for class_name in discovered_classes:
            if class_name not in _curated_classes:
                try:
                    full_class_name = f"{package_name}.{class_name}"
                    java_class = scyjava.jimport(full_class_name)
                    _extended_classes[class_name] = java_class
                    logger.debug(f"Discovered extended class: {class_name}")
                    
                except Exception as e:
                    logger.warning(f"Failed to load extended class {class_name}: {e}")
        
        _discovery_completed = True
        logger.info(f"Discovered {len(_extended_classes)} extended Sholl GUI classes")
        
    except Exception as e:
        logger.error(f"Failed to discover extended classes: {e}")
        _discovery_completed = True  # Prevent repeated attempts

# Register the setup function to run when JVM starts
scyjava.when_jvm_starts(_java_setup)

def get_available_classes() -> List[str]:
    """
    Get list of all available Sholl GUI classes.
    
    This includes both curated classes (always loaded) and extended classes
    (loaded on-demand). Extended classes are discovered if not already loaded.
    
    Returns
    -------
    List[str]
        List of available class names.
    """
    if not scyjava.jvm_started():
        return CURATED_CLASSES.copy()
    
    # Ensure extended classes are discovered
    _discover_extended_classes()
    
    all_available = list(_curated_classes.keys()) + list(_extended_classes.keys())
    return sorted(all_available)

def get_class(class_name: str) -> Any:
    """
    Get a specific Sholl GUI class by name.

    This method provides access to both curated and extended classes.
    Extended classes are discovered and loaded on first access.
    
    Parameters
    ----------
    class_name : str
        Name of the class to retrieve.
        
    Returns
    -------
    Java class
        The requested SNT Sholl GUI class.
        
    Raises
    ------
    KeyError
        If the class is not available.
    RuntimeError
        If the JVM has not been started.
    """
    if not scyjava.jvm_started():
        raise RuntimeError(
            "JVM not started. Call pysnt.initialize() first."
        )
    
    # Check curated classes first (fast path)
    if class_name in _curated_classes:
        return _curated_classes[class_name]
    
    # Check extended classes
    if class_name in _extended_classes:
        return _extended_classes[class_name]
    
    # Try to discover extended classes if not done yet
    if not _discovery_completed:
        _discover_extended_classes()
        
        # Check again after discovery
        if class_name in _extended_classes:
            return _extended_classes[class_name]
    
    # Class not found - provide helpful error
    available_curated = list(_curated_classes.keys())
    available_extended = list(_extended_classes.keys())
    all_available = available_curated + available_extended
    
    if all_available:
        available_str = ", ".join(sorted(all_available))
        raise KeyError(f"Class '{class_name}' not found. Available: {available_str}")
    else:
        raise KeyError(f"Class '{class_name}' not found. No classes loaded.")

def list_classes():
    """
    Print all available Sholl GUI classes organized by tier.
    """
    if not scyjava.jvm_started():
        print("JVM not started. Only curated classes listed.")
        print("\nCurated Classes (always available):")
        print("=" * 40)
        for class_name in CURATED_CLASSES:
            print(f"  • {class_name}")
        return
    
    print("Available SNT Sholl GUI Classes:")
    print("=" * 40)
    
    # Show curated classes
    print("\n📌 Curated Classes (direct import):")
    for class_name in sorted(_curated_classes.keys()):
        status = "✅" if _curated_classes[class_name] is not None else "❌"
        print(f"  {status} {class_name}")
    
    # Discover and show extended classes
    _discover_extended_classes()
    if _extended_classes:
        print(f"\n🔍 Extended Classes (via get_class()):")
        for class_name in sorted(_extended_classes.keys()):
            print(f"  • {class_name}")
    
    total = len(_curated_classes) + len(_extended_classes)
    print(f"\nTotal: {total} classes")

def get_curated_classes() -> List[str]:
    """
    Get list of curated classes that are always available for direct import.
    
    Returns
    -------
    List[str]
        List of curated class names.
    """
    return CURATED_CLASSES.copy()

def get_extended_classes() -> List[str]:
    """
    Get list of extended classes available via get_class().
    
    This will trigger discovery if not already done.
    
    Returns
    -------
    List[str]
        List of extended class names.
    """
    if scyjava.jvm_started():
        _discover_extended_classes()
        return list(_extended_classes.keys())
    else:
        return EXTENDED_CLASSES.copy()

# Dynamic __getattr__ to provide access to extended classes
def __getattr__(name: str) -> Any:
    """
    Provide dynamic access to Sholl GUI classes.
    
    This allows importing extended classes that were discovered at runtime,
    but prioritizes curated classes for performance.
    """
    # Check if it's a curated class that failed to load
    if name in CURATED_CLASSES:
        if name in _curated_classes:
            return _curated_classes[name]
        else:
            raise AttributeError(f"Curated class '{name}' failed to load. Check SNT installation.")
    
    # Try to get extended class
    try:
        return get_class(name)
    except (KeyError, RuntimeError):
        # Provide helpful error message
        available_curated = ", ".join(CURATED_CLASSES)
        raise AttributeError(
            f"Class '{name}' not found. "
            f"Curated classes: {available_curated}. "
            f"Use get_class('{name}') for extended classes or list_classes() to see all."
        )

# Enhanced __dir__ for IDE autocompletion
def __dir__() -> List[str]:
    """
    Return list of available attributes for IDE autocompletion.
    
    This ensures that IDEs can discover both functions and curated classes
    for autocompletion, even before the JVM is started.
    """
    base_attrs = [
        # Functions
        "get_available_classes", 
        "get_class", 
        "list_classes",
        "get_curated_classes",
        "get_extended_classes",
        # Constants
        "CURATED_CLASSES",
        "EXTENDED_CLASSES",
    ]
    
    # Always include curated classes for IDE autocompletion
    curated_attrs = [
        "ShollPlot",
        "ShollTable", 
        "ShollOverlay",
    ]
    
    # If JVM is started and extended classes are discovered, include them too
    extended_attrs = []
    if scyjava.jvm_started() and _discovery_completed:
        extended_attrs = list(_extended_classes.keys())
    
    return sorted(base_attrs + curated_attrs + extended_attrs)

# Static __all__ with curated classes always available
# This ensures IDEs know these symbols are available for import
__all__ = [
    # Functions
    "get_available_classes",
    "get_class", 
    "list_classes",
    "get_curated_classes",
    "get_extended_classes",
    # Constants
    "CURATED_CLASSES",
    "EXTENDED_CLASSES",
    # Curated classes (always available for direct import)
    "ShollPlot",
    "ShollTable", 
    "ShollOverlay",
]

# Placeholder classes for IDE support - will be replaced with Java classes
class ShollOverlay:
    """
    Curated SNT class from analysis/sholl/gui package with complete method signatures.
    
    Available for direct import after JVM initialization.
    Call pysnt.initialize() before using this class.
    
    See `analysis_sholl_gui_ShollOverlay_javadoc`_.
    
    .. _analysis_sholl_gui_ShollOverlay_javadoc: https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/analysis/sholl/gui/ShollOverlay.html
    """
    
    def __new__(cls, *args, **kwargs):
        """Smart constructor that redirects to real Java class if available."""
        # Try to get the real Java class
        try:
            # Access the module functions that were set up
            import pysnt.analysis.sholl.gui
            if hasattr(pysnt.analysis.sholl.gui, '_module_funcs'):
                module_funcs = pysnt.analysis.sholl.gui._module_funcs
                if "_curated_classes" in module_funcs:
                    curated_classes = module_funcs["_curated_classes"]
                    if "ShollOverlay" in curated_classes and curated_classes["ShollOverlay"] is not None:
                        # We have the real Java class, use it instead
                        real_class = curated_classes["ShollOverlay"]
                        return real_class(*args, **kwargs)
        except Exception:
            pass
        
        # No real class available, show error
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")
    
    def __getattr__(self, name: str):
        """Dynamic attribute access for Java methods."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

class ShollPlot:
    """
    Curated SNT class from analysis/sholl/gui package with complete method signatures.
    
    Available for direct import after JVM initialization.
    Call pysnt.initialize() before using this class.
    
    See `analysis_sholl_gui_ShollPlot_javadoc`_.
    
    .. _analysis_sholl_gui_ShollPlot_javadoc: https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/analysis/sholl/gui/ShollPlot.html
    """
    
    def __new__(cls, *args, **kwargs):
        """Smart constructor that redirects to real Java class if available."""
        # Try to get the real Java class
        try:
            # Access the module functions that were set up
            import pysnt.analysis.sholl.gui
            if hasattr(pysnt.analysis.sholl.gui, '_module_funcs'):
                module_funcs = pysnt.analysis.sholl.gui._module_funcs
                if "_curated_classes" in module_funcs:
                    curated_classes = module_funcs["_curated_classes"]
                    if "ShollPlot" in curated_classes and curated_classes["ShollPlot"] is not None:
                        # We have the real Java class, use it instead
                        real_class = curated_classes["ShollPlot"]
                        return real_class(*args, **kwargs)
        except Exception:
            pass
        
        # No real class available, show error
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")
    
    def __getattr__(self, name: str):
        """Dynamic attribute access for Java methods."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

class ShollTable:
    """
    Curated SNT class from analysis/sholl/gui package with complete method signatures.
    
    Available for direct import after JVM initialization.
    Call pysnt.initialize() before using this class.
    
    See `analysis_sholl_gui_ShollTable_javadoc`_.
    
    .. _analysis_sholl_gui_ShollTable_javadoc: https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/analysis/sholl/gui/ShollTable.html
    """
    
    def __new__(cls, *args, **kwargs):
        """Smart constructor that redirects to real Java class if available."""
        # Try to get the real Java class
        try:
            # Access the module functions that were set up
            import pysnt.analysis.sholl.gui
            if hasattr(pysnt.analysis.sholl.gui, '_module_funcs'):
                module_funcs = pysnt.analysis.sholl.gui._module_funcs
                if "_curated_classes" in module_funcs:
                    curated_classes = module_funcs["_curated_classes"]
                    if "ShollTable" in curated_classes and curated_classes["ShollTable"] is not None:
                        # We have the real Java class, use it instead
                        real_class = curated_classes["ShollTable"]
                        return real_class(*args, **kwargs)
        except Exception:
            pass
        
        # No real class available, show error
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")
    
    def __getattr__(self, name: str):
        """Dynamic attribute access for Java methods."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

# Placeholder classes for IDE support - will be replaced with Java classes
("SNT not initialized. Call pysnt.initialize() first.")

("SNT not initialized. Call pysnt.initialize() first.")

("SNT not initialized. Call pysnt.initialize() first.")

# Placeholder classes for IDE support - will be replaced with Java classes
("SNT not initialized. Call pysnt.initialize() first.")

("SNT not initialized. Call pysnt.initialize() first.")

("SNT not initialized. Call pysnt.initialize() first.")

# Placeholder classes for IDE support - will be replaced with Java classes
("SNT not initialized. Call pysnt.initialize() first.")

("SNT not initialized. Call pysnt.initialize() first.")

("SNT not initialized. Call pysnt.initialize() first.")

# Placeholder classes for IDE support - will be replaced with Java classes
("SNT not initialized. Call pysnt.initialize() first.")

("SNT not initialized. Call pysnt.initialize() first.")

("SNT not initialized. Call pysnt.initialize() first.")

# Placeholder classes for IDE support - will be replaced with Java classes
("SNT not initialized. Call pysnt.initialize() first.")

("SNT not initialized. Call pysnt.initialize() first.")

("SNT not initialized. Call pysnt.initialize() first.")

# Placeholder classes for IDE support - will be replaced with Java classes
("SNT not initialized. Call pysnt.initialize() first.")

("SNT not initialized. Call pysnt.initialize() first.")

("SNT not initialized. Call pysnt.initialize() first.")

# Placeholder classes for IDE support - will be replaced with Java classes
("SNT not initialized. Call pysnt.initialize() first.")

("SNT not initialized. Call pysnt.initialize() first.")

("SNT not initialized. Call pysnt.initialize() first.")

# Placeholder classes for IDE support - will be replaced with Java classes
("SNT not initialized. Call pysnt.initialize() first.")

("SNT not initialized. Call pysnt.initialize() first.")

("SNT not initialized. Call pysnt.initialize() first.")

# Placeholder classes for IDE support - will be replaced with Java classes
("SNT not initialized. Call pysnt.initialize() first.")

("SNT not initialized. Call pysnt.initialize() first.")

("SNT not initialized. Call pysnt.initialize() first.")

# Placeholder classes for IDE support - will be replaced with Java classes
("SNT not initialized. Call pysnt.initialize() first.")

("SNT not initialized. Call pysnt.initialize() first.")

("SNT not initialized. Call pysnt.initialize() first.")

# Placeholder classes for IDE support - will be replaced with Java classes
("SNT not initialized. Call pysnt.initialize() first.")

("SNT not initialized. Call pysnt.initialize() first.")

("SNT not initialized. Call pysnt.initialize() first.")

# Placeholder classes for IDE support - will be replaced with Java classes
("SNT not initialized. Call pysnt.initialize() first.")

("SNT not initialized. Call pysnt.initialize() first.")

("SNT not initialized. Call pysnt.initialize() first.")

# Placeholder classes for IDE support - will be replaced with Java classes
("SNT not initialized. Call pysnt.initialize() first.")

("SNT not initialized. Call pysnt.initialize() first.")

("SNT not initialized. Call pysnt.initialize() first.")

# Placeholder classes for IDE support - will be replaced with Java classes
("SNT not initialized. Call pysnt.initialize() first.")

("SNT not initialized. Call pysnt.initialize() first.")

("SNT not initialized. Call pysnt.initialize() first.")

# Placeholder classes for IDE support - will be replaced with Java classes
("SNT not initialized. Call pysnt.initialize() first.")

("SNT not initialized. Call pysnt.initialize() first.")

("SNT not initialized. Call pysnt.initialize() first.")

# Placeholder classes for IDE support - will be replaced with Java classes
("SNT not initialized. Call pysnt.initialize() first.")

("SNT not initialized. Call pysnt.initialize() first.")

("SNT not initialized. Call pysnt.initialize() first.")

# Placeholder classes for IDE support - will be replaced with Java classes
("SNT not initialized. Call pysnt.initialize() first.")

("SNT not initialized. Call pysnt.initialize() first.")

("SNT not initialized. Call pysnt.initialize() first.")

# Placeholder classes for IDE support - will be replaced with Java classes
("SNT not initialized. Call pysnt.initialize() first.")

("SNT not initialized. Call pysnt.initialize() first.")

("SNT not initialized. Call pysnt.initialize() first.")

# Placeholder classes for IDE support - will be replaced with Java classes
("SNT not initialized. Call pysnt.initialize() first.")

("SNT not initialized. Call pysnt.initialize() first.")

("SNT not initialized. Call pysnt.initialize() first.")

# Placeholder classes for IDE support - will be replaced with Java classes
("SNT not initialized. Call pysnt.initialize() first.")

("SNT not initialized. Call pysnt.initialize() first.")

("SNT not initialized. Call pysnt.initialize() first.")

# Placeholder classes for IDE support - will be replaced with Java classes
("SNT not initialized. Call pysnt.initialize() first.")

("SNT not initialized. Call pysnt.initialize() first.")

("SNT not initialized. Call pysnt.initialize() first.")

# Placeholder classes for IDE support - will be replaced with Java classes
("SNT not initialized. Call pysnt.initialize() first.")

("SNT not initialized. Call pysnt.initialize() first.")

("SNT not initialized. Call pysnt.initialize() first.")

# Placeholder classes for IDE support - will be replaced with Java classes
("SNT not initialized. Call pysnt.initialize() first.")

("SNT not initialized. Call pysnt.initialize() first.")

("SNT not initialized. Call pysnt.initialize() first.")

# Placeholder classes for IDE support - will be replaced with Java classes
("SNT not initialized. Call pysnt.initialize() first.")

("SNT not initialized. Call pysnt.initialize() first.")

("SNT not initialized. Call pysnt.initialize() first.")

# Placeholder classes for IDE support - will be replaced with Java classes
("SNT not initialized. Call pysnt.initialize() first.")

("SNT not initialized. Call pysnt.initialize() first.")

("SNT not initialized. Call pysnt.initialize() first.")

# Placeholder classes for IDE support - will be replaced with Java classes
("SNT not initialized. Call pysnt.initialize() first.")

("SNT not initialized. Call pysnt.initialize() first.")

("SNT not initialized. Call pysnt.initialize() first.")

# Placeholder classes for IDE support - will be replaced with Java classes
("SNT not initialized. Call pysnt.initialize() first.")

("SNT not initialized. Call pysnt.initialize() first.")

("SNT not initialized. Call pysnt.initialize() first.")

# Placeholder classes for IDE support - will be replaced with Java classes
("SNT not initialized. Call pysnt.initialize() first.")

("SNT not initialized. Call pysnt.initialize() first.")

("SNT not initialized. Call pysnt.initialize() first.")

# Placeholder classes for IDE support - will be replaced with Java classes
("SNT not initialized. Call pysnt.initialize() first.")

("SNT not initialized. Call pysnt.initialize() first.")

("SNT not initialized. Call pysnt.initialize() first.")

