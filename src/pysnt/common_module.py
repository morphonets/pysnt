"""
Common functionality for PySNT submodules.

This module provides shared functionality for all PySNT submodules to eliminate
code duplication in __init__.py files.
"""

import logging
import scyjava
from typing import Dict, Any, List, Optional, Callable

logger = logging.getLogger(__name__)


def _normalize_class_name_for_python(class_name: str) -> str:
    """
    Convert Java inner class names to Python-friendly names.

    Java inner classes use $ internally (e.g., OuterClass$InnerClass)
    but are accessed with . in Java code (OuterClass.InnerClass).

    For Python, we'll use underscore notation to avoid conflicts with
    attribute access: OuterClass_InnerClass

    Args:
        class_name: Java class name (may contain $)

    Returns:
        Python-friendly class name
    """
    return class_name.replace("$", "_")


def _get_java_class_name(class_name: str) -> str:
    """
    Convert Python class name back to Java internal name for import.

    Args:
        class_name: Python class name (may contain _)

    Returns:
        Java internal class name (with $ for inner classes)
    """
    # For now, assume that any _ in the name might represent an inner class
    # FIXME: This is a heuristic: likely needs more sophistication
    return class_name.replace("_", "$")


def setup_module_classes(
    package_name: str,
    curated_classes: List[str],
    extended_classes: List[str],
    globals_dict: Dict[str, Any],
    discovery_packages: Optional[List[str]] = None,
    include_interfaces: bool = False,
) -> Dict[str, Any]:
    """
    Setup function that handles all common module initialization.

    This function creates all the standard functionality that PySNT modules need:
    - Class registries for curated and extended classes
    - Java setup function that loads curated classes
    - Discovery function for extended classes
    - get_class(), list_classes(), and other standard functions
    - Dynamic __getattr__ and __dir__ functions

    Parameters
    ----------
    package_name : str
        Java package name (e.g., "sc.fiji.snt.analysis")
    curated_classes : List[str]
        Classes that are always loaded and available for direct import
    extended_classes : List[str]
        Classes that are loaded on-demand via get_class()
    globals_dict : Dict[str, Any]
        The module's globals() dict to update with Java classes
    discovery_packages : List[str], optional
        Additional packages to search for classes (defaults to [package_name])
    include_interfaces : bool, default False
        Whether to include Java interfaces in discovery

    Returns
    -------
    Dict[str, Any]
        Dictionary containing all the module functions and data
    """

    # Module state
    _curated_classes: Dict[str, Any] = {}
    _extended_classes: Dict[str, Any] = {}
    _discovery_completed: bool = False

    # Default discovery packages
    if discovery_packages is None:
        discovery_packages = [package_name]

    def _java_setup():
        """
        Lazy initialization function for Java-dependent classes.

        This loads curated classes immediately and prepares extended classes
        for on-demand loading.
        """
        nonlocal _curated_classes

        try:
            # Import curated classes immediately
            for class_name in curated_classes:
                java_class = None
                python_name = _normalize_class_name_for_python(class_name)
                java_name = _get_java_class_name(class_name)

                # Try all discovery packages for curated classes
                for pkg in discovery_packages:
                    try:
                        full_class_name = f"{pkg}.{java_name}"
                        java_class = scyjava.jimport(full_class_name)
                        logger.debug(
                            f"Loaded curated class {python_name} (Java: {java_name}) from {pkg}"
                        )
                        break
                    except Exception:
                        continue

                if java_class is not None:
                    _curated_classes[python_name] = java_class
                    # Replace placeholder class with actual Java class using Python name
                    globals_dict[python_name] = java_class
                else:
                    logger.warning(
                        f"Failed to load curated class {python_name} (Java: {java_name})"
                    )
                    # Set to None so users get clear error messages
                    globals_dict[python_name] = None

            logger.info(
                f"Successfully loaded {len(_curated_classes)} curated classes for {package_name}"
            )

        except Exception as e:
            logger.error(f"Failed to load curated classes for {package_name}: {e}")
            raise ImportError(
                f"Could not load curated classes for {package_name}: {e}"
            ) from e

    def _discover_extended_classes():
        """
        Discover and load extended classes on-demand.

        This is called the first time get_class() is used for a non-curated class.
        """
        nonlocal _extended_classes, _discovery_completed

        if _discovery_completed:
            return

        try:
            from .java_utils import discover_java_classes

            # Discover classes from all packages
            all_classes = curated_classes + extended_classes

            for pkg in discovery_packages:
                discovered_classes = discover_java_classes(
                    pkg,
                    known_classes=all_classes,
                    include_abstract=False,
                    include_interfaces=include_interfaces,
                )

                # Load extended classes (excluding already loaded curated ones)
                for java_class_name in discovered_classes:
                    python_name = _normalize_class_name_for_python(java_class_name)
                    if python_name not in _curated_classes:
                        try:
                            full_class_name = f"{pkg}.{java_class_name}"
                            java_class = scyjava.jimport(full_class_name)
                            _extended_classes[python_name] = java_class
                            logger.debug(
                                f"Discovered extended class: {python_name} (Java: {java_class_name}) from {pkg}"
                            )

                        except Exception as e:
                            logger.warning(
                                f"Failed to load extended class {python_name} (Java: {java_class_name}) from {pkg}: {e}"
                            )

            _discovery_completed = True
            logger.info(
                f"Discovered {len(_extended_classes)} extended classes for {package_name}"
            )

        except Exception as e:
            logger.error(f"Failed to discover extended classes for {package_name}: {e}")
            _discovery_completed = True  # Prevent repeated attempts

    def get_available_classes() -> List[str]:
        """
        Get list of all available classes.

        This includes both curated classes (always loaded) and extended classes
        (loaded on-demand). Extended classes are discovered if not already loaded.

        Returns
        -------
        List[str]
            List of available class names.
        """
        if not scyjava.jvm_started():
            return curated_classes.copy()

        # Ensure extended classes are discovered
        _discover_extended_classes()

        all_available = list(_curated_classes.keys()) + list(_extended_classes.keys())
        return sorted(all_available)

    def get_class(class_name: str) -> Any:
        """
        Get a specific class by name.

        This method provides access to both curated and extended classes.
        Extended classes are discovered and loaded on first access.

        Parameters
        ----------
        class_name : str
            Name of the class to retrieve.

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
        """
        if not scyjava.jvm_started():
            raise RuntimeError("JVM not started. Call pysnt.initialize() first.")

        # Normalize the class name for lookup (handle both Python and Java naming)
        python_name = _normalize_class_name_for_python(class_name)

        # Check curated classes first (fast path)
        if python_name in _curated_classes:
            return _curated_classes[python_name]

        # Check extended classes
        if python_name in _extended_classes:
            return _extended_classes[python_name]

        # Try to discover extended classes if not done yet
        if not _discovery_completed:
            _discover_extended_classes()

            # Check again after discovery
            if python_name in _extended_classes:
                return _extended_classes[python_name]

        # For root package, try direct import if not in registries
        if package_name == "sc.fiji.snt":
            try:
                # Try with Java naming (convert Python name back to Java)
                java_name = _get_java_class_name(class_name)
                full_class_name = f"{package_name}.{java_name}"
                java_class = scyjava.jimport(full_class_name)
                return java_class
            except Exception:
                pass

        # Class not found - provide helpful error
        available_curated = list(_curated_classes.keys())
        available_extended = list(_extended_classes.keys())
        all_available = available_curated + available_extended

        if all_available:
            available_str = ", ".join(sorted(all_available))
            raise KeyError(
                f"Class '{class_name}' not found. Available: {available_str}"
            )
        else:
            raise KeyError(f"Class '{class_name}' not found. No classes loaded.")

    def list_classes():
        """
        Print all available classes organized by tier.
        """
        module_name = package_name.split(".")[-1].title()

        if not scyjava.jvm_started():
            print("JVM not started. Only curated classes listed.")
            print(f"\nCurated Classes (always available):")
            print("=" * 40)
            for class_name in curated_classes:
                print(f"  • {class_name}")
            return

        print(f"Available SNT {module_name} Classes:")
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

        # Special handling for root package
        if package_name == "sc.fiji.snt":
            print(f"\n💡 Extended Classes:")
            print(
                "  Any class from sc.fiji.snt package can be accessed via get_class()"
            )
            print("  even if not in the curated list above.")

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
        return curated_classes.copy()

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
            return extended_classes.copy()

    def create_getattr(
        module_name: str, submodules: List[str] = None
    ) -> Callable[[str], Any]:
        """
        Create a __getattr__ function for the module.

        Parameters
        ----------
        module_name : str
            Name of the module for error messages
        submodules : List[str], optional
            List of submodule names that should not be intercepted

        Returns
        -------
        Callable
            __getattr__ function for the module
        """
        if submodules is None:
            submodules = []

        def __getattr__(name: str) -> Any:
            """
            Provide dynamic access to classes.

            This allows importing extended classes that were discovered at runtime,
            but prioritizes curated classes for performance.
            """
            # Don't intercept submodule access
            if name in submodules:
                raise AttributeError(f"'{module_name}' has no attribute '{name}'")

            # Check if it's a curated class that failed to load
            if name in curated_classes:
                if name in _curated_classes:
                    return _curated_classes[name]
                else:
                    raise AttributeError(
                        f"Curated class '{name}' failed to load. Check SNT installation."
                    )

            # Try to get extended class
            try:
                return get_class(name)
            except (KeyError, RuntimeError):
                # Provide helpful error message
                available_curated = ", ".join(curated_classes)
                raise AttributeError(
                    f"Class '{name}' not found in {module_name}. "
                    f"Curated classes: {available_curated}. "
                    f"Use get_class('{name}') for extended classes or list_classes() to see all."
                )

        return __getattr__

    def create_dir() -> Callable[[], List[str]]:
        """
        Create a __dir__ function for the module.

        Returns
        -------
        Callable
            __dir__ function for the module
        """

        def __dir__() -> List[str]:
            """
            Return list of available attributes for IDE autocompletion.

            This ensures that IDEs can discover both functions, curated classes,
            and extended classes for autocompletion, even before the JVM is started.
            Extended classes are included to improve IDE experience, though they
            will only work after JVM initialization.
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
            curated_attrs = curated_classes.copy()

            # Always include extended classes for IDE autocompletion
            # This improves IDE experience by showing all available class names
            # even before JVM starts, though the classes won't work until initialized
            extended_attrs = extended_classes.copy()

            # If JVM is started and additional classes were discovered, include them too
            if scyjava.jvm_started() and _discovery_completed:
                # Add any dynamically discovered classes not in the predefined list
                discovered_extended = list(_extended_classes.keys())
                for class_name in discovered_extended:
                    if class_name not in extended_attrs:
                        extended_attrs.append(class_name)

            return sorted(base_attrs + curated_attrs + extended_attrs)

        return __dir__

    # Register the setup function to run when JVM starts
    scyjava.when_jvm_starts(_java_setup)

    # Return all the module functions and data
    return {
        # Functions
        "get_available_classes": get_available_classes,
        "get_class": get_class,
        "list_classes": list_classes,
        "get_curated_classes": get_curated_classes,
        "get_extended_classes": get_extended_classes,
        "create_getattr": create_getattr,
        "create_dir": create_dir,
        # Constants
        "CURATED_CLASSES": curated_classes,
        "EXTENDED_CLASSES": extended_classes,
        # Internal state (for debugging/testing)
        "_curated_classes": _curated_classes,
        "_extended_classes": _extended_classes,
        "_discovery_completed": lambda: _discovery_completed,
        # Setup functions
        "_java_setup": _java_setup,
        "_discover_extended_classes": _discover_extended_classes,
    }
