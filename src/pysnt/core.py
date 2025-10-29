"""
Core initialization and setup for PySNT.

This module handles the initialization of the Java environment and
Fiji integration required for SNT functionality.
"""

import logging
import os
from pathlib import Path
from typing import Optional, List, Dict, Any

try:
    import scyjava
    import imagej
except ImportError as e:
    raise ImportError("Required dependencies not found.") from e

logger = logging.getLogger(__name__)

# Global state
_ij = None
_jvm_started = False


class FijiNotFoundError(RuntimeError):
    """
    Exception raised when Fiji installation cannot be found or configured.
    """
    pass


def _configure_jvm(max_heap: Optional[str] = None, min_heap: Optional[str] = None, jvm_args: Optional[List[str]] = None) -> None:
    """
    Configure JVM parameters before startup.
    
    Parameters
    ----------
    max_heap : str, optional
        Maximum heap size (e.g., "8g", "4096m")
    min_heap : str, optional
        Initial heap size (e.g., "2g", "1024m")
    jvm_args : List[str], optional
        Additional JVM arguments
    """
    if max_heap is None and min_heap is None and (jvm_args is None or len(jvm_args) == 0):
        return  # Nothing to configure
    
    logger.info("Configuring JVM parameters...")
    
    # Configure heap sizes
    if max_heap is not None:
        max_heap_arg = f"-Xmx{max_heap}"
        scyjava.config.add_option(max_heap_arg)
        logger.info(f"Set maximum heap size: {max_heap_arg}")
    
    if min_heap is not None:
        min_heap_arg = f"-Xms{min_heap}"
        scyjava.config.add_option(min_heap_arg)
        logger.info(f"Set initial heap size: {min_heap_arg}")
    
    # Configure additional JVM arguments
    if jvm_args is not None:
        for arg in jvm_args:
            scyjava.config.add_option(arg)
            logger.info(f"Added JVM argument: {arg}")
    
    logger.info("JVM configuration complete")


def initialize(fiji_path: Optional[str] = None, interactive: bool = True, ensure_java: bool = True, mode: str = "headless", 
               max_heap: Optional[str] = None, min_heap: Optional[str] = None, jvm_args: Optional[List[str]] = None) -> None:
    """
    Initialize the SNT environment with ImageJ/Fiji.
    
    Parameters
    ----------
    fiji_path : str, optional
        Path to Fiji installation. If None, will try to auto-detect.
        Can also be a mode string for convenience (e.g., "gui", "interactive").
    interactive : bool, default True
        Whether to prompt user for Fiji path if not found automatically.
        Set to False for non-interactive environments (CI, scripts, etc.).
    ensure_java : bool, default True
        Whether to check and ensure Java is available. If True, will attempt
        to install OpenJDK if Java is not found or version is too old.
    mode : str, default "headless"
        pyimagej initialization mode. Either "headless", "gui", "interactive",
        or "interactive:force"
    max_heap : str, optional
        Maximum JVM heap size (e.g., "8g", "4096m", "2G"). 
        Convenient alternative to manually configuring JVM args.
    min_heap : str, optional
        Initial JVM heap size (e.g., "2g", "1024m", "1G").
        Convenient alternative to manually configuring JVM args.
    jvm_args : List[str], optional
        Additional JVM arguments to pass (e.g., ["-XX:+UseG1GC", "-Xss2m"]).
        For advanced users who need full control over JVM configuration.
        
    Examples
    --------
    >>> # Standard usage
    >>> pysnt.initialize("/path/to/Fiji.app", mode="gui")
    >>> 
    >>> # Convenience syntax - just specify mode
    >>> pysnt.initialize("gui")
    >>> pysnt.initialize("interactive")
    >>> 
    >>> # Memory configuration
    >>> pysnt.initialize(max_heap="8g")  # 8GB heap
    >>> pysnt.initialize(max_heap="16g", min_heap="4g")  # 16GB max, 4GB initial
    >>> 
    >>> # Advanced JVM configuration
    >>> pysnt.initialize(jvm_args=["-Xmx8g", "-XX:+UseG1GC"])
    >>> 
    >>> # Full control
    >>> pysnt.initialize(None, True, True, "gui", max_heap="8g")
        
    Raises
    ------
    FijiNotFoundError
        If Fiji installation cannot be found or configured.
    RuntimeError
        If initialization fails for other reasons (Java issues, etc.).
        
    Notes
    -----
    JVM memory configuration (max_heap, min_heap, jvm_args) must be specified
    on the first call to initialize(). Subsequent calls will ignore these
    parameters since the JVM cannot be reconfigured once started.
    """
    # Handle convenience syntax: initialize("gui") -> initialize(mode="gui")
    valid_modes = {"headless", "gui", "interactive", "interactive:force"}
    if fiji_path in valid_modes:
        # Shift parameters: fiji_path is actually the mode
        mode = fiji_path
        fiji_path = None
    global _ij, _jvm_started
    
    if _jvm_started:
        logger.info("SNT already initialized")
        return
        
    try:
        # Check and ensure Java is available
        if ensure_java:
            from .java_utils import ensure_java_available
            if not ensure_java_available(auto_install=interactive):
                logger.warning("Java requirements not met, but continuing initialization")
        
        # Auto-detect Fiji if not provided
        if fiji_path is None:
            fiji_path = _find_fiji(interactive=interactive)
            
        if fiji_path:
            if not Path(fiji_path).exists():
                raise FileNotFoundError(f"Fiji not found at: {fiji_path}")
            elif not _validate_fiji_path(fiji_path):
                logger.warning(f"Path may not be a valid Fiji installation: {fiji_path}")
        else:
            # Create an error message with helpful instructions
            from . import setup_utils
            
            error_msg = [
                "❌ Fiji installation not found!",
                "",
                "PySNT requires Fiji to function. Here's how to fix this:",
                "",
                "🔧 Quick Solutions:",
            ]
            
            # Check if we're in interactive mode
            if interactive:
                error_msg.extend([
                    "  1. Run the interactive setup:",
                    "     python -m pysnt.setup_utils",
                    "",
                    "  2. Auto-detect Fiji installation:",
                    "     python -m pysnt.setup_utils --auto-detect",
                ])
            else:
                error_msg.extend([
                    "  1. Auto-detect Fiji installation:",
                    "     python -m pysnt.setup_utils --auto-detect",
                    "",
                    "  2. Set Fiji path manually:",
                    "     python -m pysnt.setup_utils --set /path/to/Fiji.app",
                ])
            
            error_msg.extend([
                "",
                "📋 Alternative Methods:",
                "  • Set environment variable: export FIJI_PATH='/path/to/Fiji.app'",
                "  • Pass path directly: pysnt.initialize(fiji_path='/path/to/Fiji.app')",
                "  • Use pysnt.set_fiji_path('/path/to/Fiji.app')",
                "",
            ])
            
            # Add platform-specific common locations
            try:
                common_paths = setup_utils.find_fiji_installations()
                if common_paths:
                    error_msg.extend([
                        "🔍 We checked these common locations:",
                        *[f"  ✗ {path}" for path in common_paths[:5]],  # Show first 5
                    ])
                    if len(common_paths) > 5:
                        error_msg.append(f"  ... and {len(common_paths) - 5} more locations")
                else:
                    error_msg.extend([
                        "🔍 No Fiji installations found in common locations for your platform.",
                    ])
            except Exception:
                # Don't let setup_utils errors break the main error message
                pass
            
            error_msg.extend([
                "",
                "💡 Need help? Check configuration status:",
                "   python -m pysnt.setup_utils --status",
                "",
                "For more information, see: https://github.com/morphonets/pysnt"
            ])
            
            raise FijiNotFoundError("\n".join(error_msg))
            
        # Configure JVM BEFORE it starts
        if not scyjava.jvm_started():
            _configure_jvm(max_heap, min_heap, jvm_args)
        
        # Register SNT converters BEFORE JVM starts
        if not scyjava.jvm_started():
            logger.info("Registering SNT converters before JVM startup...")
            try:
                from .converters import register_snt_converters
                register_snt_converters()
                logger.info("SNT converters registered successfully")
            except Exception as e:
                logger.warning(f"Failed to register SNT converters: {e}")
        
        # Initialize PyImageJ from local Fiji
        logger.info(f"Initializing ImageJ with Fiji at: {fiji_path}")
        _ij = imagej.init(fiji_path, mode=mode)
        
        # Start JVM if not already started
        if not scyjava.jvm_started():
            if "headless" == mode:
                scyjava.config.enable_headless_mode() # System.setProperty("java.awt.headless", "true");
            scyjava.start_jvm()
            
        _jvm_started = True
        logger.info("SNT initialization complete")
        
    except FijiNotFoundError:
        # Re-raise FijiNotFoundError as-is (it already has helpful messages)
        raise
    except Exception as e:
        logger.error(f"Failed to initialize SNT: {e}")
        raise RuntimeError(f"SNT initialization failed: {e}") from e


def _find_fiji(interactive: bool = True) -> Optional[str]:
    """
    Multi-level Fiji path discovery strategy with persistent configuration.
    
    Uses the setup_utils module for configuration management.
    
    Discovery priority order:
    1. Environment variable (FIJI_PATH) - highest priority
    2. Config file - stored in platform-specific location
    3. Common installation locations - platform-specific defaults
    4. Interactive prompt - ask user on first run
    
    Parameters
    ----------
    interactive : bool, default True
        Whether to prompt user for Fiji path if not found automatically.
        
    Returns
    -------
    str or None
        Path to Fiji if found, None otherwise.
    """
    from . import setup_utils
    
    # 1. Check environment variable first (highest priority)
    fiji_env = os.environ.get("FIJI_PATH")
    if fiji_env and Path(fiji_env).exists():
        logger.info(f"Found Fiji via FIJI_PATH environment variable: {fiji_env}")
        return fiji_env
    
    # 2. Check config file
    config = setup_utils.load_config()
    fiji_config = config.get("fiji_path")
    if fiji_config and Path(fiji_config).exists():
        logger.info(f"Found Fiji via config file: {fiji_config}")
        return fiji_config
    elif fiji_config:
        logger.warning(f"Config file contains invalid Fiji path: {fiji_config}")
        # Remove invalid path from config
        config.pop("fiji_path", None)
        setup_utils.save_config(config)
        
    # 3. Check common installation locations
    common_paths = setup_utils.find_fiji_installations()
    for path in common_paths:
        if Path(path).exists():
            logger.info(f"Found Fiji at common location: {path}")
            # Save to config for future use
            if setup_utils.set_fiji_path(path):
                logger.info(f"Saved Fiji path to config: {path}")
            return path
    
    # 4. Interactive prompt if enabled
    if interactive:
        fiji_path = _prompt_for_fiji_path()
        if fiji_path:
            # Save to config for future use
            if setup_utils.set_fiji_path(fiji_path, validate=False):
                logger.info(f"Saved user-provided Fiji path to config: {fiji_path}")
        return fiji_path
    else:
        # In non-interactive mode, return None and let the caller handle the error
        logger.debug("Fiji not found in any location (non-interactive mode)")
        return None


def _prompt_for_fiji_path() -> Optional[str]:
    """
    Interactively prompt user for Fiji installation path.
    
    Returns
    -------
    str or None
        Valid Fiji path provided by user, or None if cancelled.
    """
    logger = logging.getLogger(__name__)
    
    print("\nFiji Installation Not Found")
    print("=" * 40)
    print("PySNT requires Fiji to be installed:")
    print()
    print("Common installation locations checked:")
    print("  - /Applications/Fiji.app")
    print("  - C:/Fiji.app")
    print("  - ~/Fiji.app")
    print("  - ~/Applications/Fiji.app")
    print("  - ~/Desktop/Fiji.app")
    print("  - ~/Downloads/Fiji.app")
    print()
    print("If Fiji is installed in a different location, please provide the path.")
    print("If Fiji is not installed, you can:")
    print("  1. Set FIJI_PATH environment variable")
    print("  2. Pass fiji_path parameter to initialize()")
    print()
    
    max_attempts = 3
    for attempt in range(max_attempts):
        try:
            if attempt > 0:
                print(f"\nAttempt {attempt + 1}/{max_attempts}")
            
            # Prompt for path
            fiji_path = input("📍Enter Fiji installation path (or 'skip' to continue without): ").strip()
            
            # Handle special inputs
            if fiji_path.lower() in ['skip', 'cancel', 'quit', 'exit', '']:
                print("Skipping Fiji path setup. You can set it later with fiji_path parameter.")
                return None
            
            # Expand user path
            fiji_path = os.path.expanduser(fiji_path)
            
            # Validate path
            if not os.path.exists(fiji_path):
                print(f"❌ Path does not exist: {fiji_path}")
                continue
            
            # Check if it looks like a Fiji installation
            fiji_path_obj = Path(fiji_path)
            
            # Look for Fiji indicators
            fiji_indicators = [
                "fiji",   # executable
                "config", # jaunch config directory
                "lib",    # lib directory
                "jars",   # Jars directory
                "plugins",# plugins directory
            ]
            
            is_fiji = False
            for indicator in fiji_indicators:
                if (fiji_path_obj / indicator).exists():
                    is_fiji = True
                    break
            
            if not is_fiji:
                print(f"⚠️  Warning: {fiji_path} doesn't appear to be a Fiji installation.")
                confirm = input("Use this path anyway? (y/N): ").strip().lower()
                if confirm not in ['y', 'yes']:
                    continue
            
            # Path looks good
            print(f"✅ Using Fiji installation: {fiji_path}")
            logger.info(f"User provided Fiji path: {fiji_path}")
            
            return fiji_path
            
        except KeyboardInterrupt:
            print("\n\nCancelled by user.")
            return None
        except EOFError:
            print("\n\nInput cancelled.")
            return None
        except Exception as e:
            print(f"❌ Error processing input: {e}")
            continue
    
    print(f"\n❌ Maximum attempts ({max_attempts}) reached. Continuing without Fiji path.")
    print("You can specify the path later using:")
    print("  - pysnt.initialize(fiji_path='/path/to/Fiji.app')")
    print("  - Set FIJI_PATH environment variable")
    
    return None


def _validate_fiji_path(fiji_path: str) -> bool:
    """
    Validate that a path points to a valid Fiji installation serving SNT.

    Parameters
    ----------
    fiji_path : str
        Path to validate
        
    Returns
    -------
    bool
        True if path appears to be a valid Fiji installation with SNT
    """
    if not fiji_path or not os.path.exists(fiji_path):
        return False
    
    from . import setup_utils
    status = setup_utils.check_fiji_installation(fiji_path)
    return status["is_fiji"]


def ij():
    """
    Get the ImageJ instance.
    
    This provides access to the ImageJ instance used by PySNT.
    Consistent with PyImageJ's naming convention.
    
    Returns
    -------
    ImageJ instance
        The initialized ImageJ instance.
        
    Raises
    ------
    RuntimeError
        If SNT has not been initialized.
    """
    if _ij is None:
        raise RuntimeError("SNT not initialized. Call initialize() first.")
    return _ij


def is_initialized() -> bool:
    """
    Check if SNT has been initialized.
    
    Returns
    -------
    bool
        True if initialized, False otherwise.
    """
    return _jvm_started and _ij is not None




def setup_dynamic_imports(
    module_globals: Dict[str, Any],
    package_name: str,
    known_classes: Optional[List[str]] = None,
    include_abstract: bool = False,
    include_interfaces: bool = False
) -> Dict[str, Any]:
    """
    Set up dynamic imports for a module using discovered Java classes.
    
    This is a convenience function that discovers classes and sets up
    the module's global namespace and __all__ list.
    
    Parameters
    ----------
    module_globals : Dict[str, Any]
        The module's globals() dictionary
    package_name : str
        Java package name to discover classes from
    known_classes : List[str], optional
        Known class names to test
    include_abstract : bool, default False
        Whether to include abstract classes
    include_interfaces : bool, default False
        Whether to include interfaces
        
    Returns
    -------
    Dict[str, Any]
        Dictionary mapping class names to Java classes
        
    Examples
    --------
    >>> # In a module's _java_setup function:
    >>> java_classes = setup_dynamic_imports(
    ...     globals(), 
    ...     'sc.fiji.snt.analysis',
    ...     ['TreeStatistics', 'ConvexHull']
    ... )
    """
    logger = logging.getLogger(__name__)
    
    try:
        # Import the moved function
        from .java_utils import discover_java_classes
        
        # Discover classes
        class_names = discover_java_classes(
            package_name, 
            known_classes, 
            include_abstract, 
            include_interfaces
        )
        
        # Import each class
        java_classes = {}
        for class_name in class_names:
            try:
                full_class_name = f"{package_name}.{class_name}"
                java_class = scyjava.jimport(full_class_name)
                java_classes[class_name] = java_class
                
                # Make class available at module level
                module_globals[class_name] = java_class
                
                logger.debug(f"Imported {class_name}")
                
            except Exception as e:
                logger.warning(f"Failed to import {class_name}: {e}")
                continue
        
        # Update module's __all__
        base_all = module_globals.get('__all__', [])
        if isinstance(base_all, list):
            module_globals['__all__'] = base_all + list(java_classes.keys())
        
        logger.info(f"Set up {len(java_classes)} dynamic imports for {package_name}")
        return java_classes
        
    except Exception as e:
        logger.error(f"Failed to set up dynamic imports for {package_name}: {e}")
        return {}

# PyImageJ Integration and Convenience Methods
def to_python(obj, **kwargs):
    """
    Convert supported Java data into Python equivalents.

    This function extends scyjava's to_python() to support SNT-specific objects
    like Tree, Path, and SNTChart.

    Parameters
    ----------
    obj : Any
        The Java object to convert to Python
    **kwargs
        Additional arguments passed to the converter
        
    Returns
    -------
    Any
        The converted Python object
        
    Examples
    --------
    >>> import pysnt
    >>> pysnt.initialize("headless")
    >>> service = pysnt.SNTService()
    >>> tree = service.demoTree('fractal')
    >>> skeleton = tree.getSkeleton2D()
    >>> 
    >>> # Convert Java objects to Python
    >>> py_tree = pysnt.to_python(tree)
    >>> py_skeleton = pysnt.to_python(skeleton)
    """
    try:
        import scyjava as sj
        
        # Use scyjava's conversion system with our registered converters
        return sj.to_python(obj)
        
    except ImportError:
        logger.error("scyjava not available")
        raise RuntimeError("scyjava not available. Ensure scyjava is installed.")
    except Exception as e:
        logger.error(f"Conversion failed: {e}")
        raise


def from_java(obj, **kwargs):
    """
    Alias for to_python() for backward compatibility.
    
    This provides backward compatibility for existing code that uses from_java().
    New code should use to_python() for consistency with scyjava.
    """
    return to_python(obj, **kwargs)


def show(obj, **kwargs):
    """
    Enhanced show that handles SNT objects and converted data.
    
    This function extends PyImageJ's show() to support displaying SNT objects
    and data converted by our custom converters.
    
    Parameters
    ----------
    obj : Any
        The object to display (can be SNT objects, numpy arrays, etc.)
    **kwargs
        Additional display arguments (e.g., cmap='gray', title='My Image')
        
    Examples
    --------
    >>> import pysnt
    >>> pysnt.initialize("interactive")  # or "gui"
    >>> service = pysnt.SNTService()
    >>> tree = service.demoTree('fractal')
    >>> skeleton = tree.getSkeleton2D()
    >>> 
    >>> # Convert and display
    >>> py_skeleton = pysnt.to_python(skeleton)
    >>> pysnt.show(py_skeleton, cmap='gray', title='Fractal Skeleton')
    >>> 
    >>> # Or convert and display in one step
    >>> pysnt.show(pysnt.to_python(tree))
    """
    try:
        from .converters import display
        return display(obj, **kwargs)
    except ImportError:
        logger.error("PyImageJ integration module not available")
        raise RuntimeError("PyImageJ integration not available. Ensure PyImageJ is installed.")






