"""
Core initialization and setup for PySNT.

This module handles the initialization of the Java environment and
Fiji integration required for SNT functionality.
"""

import logging
import os
import zipfile
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


def initialize_snt(fiji_path: Optional[str] = None, interactive: bool = True, ensure_java: bool = True, mode: str = "headless") -> None:
    """
    Initialize the SNT environment with ImageJ/Fiji.
    
    Parameters
    ----------
    fiji_path : str, optional
        Path to Fiji installation. If None, will try to auto-detect.
    mode : str, default "headless"
        pyimagej initialization mode. Either "headless", "gui", "interactive",
        or "interactive:force"
    interactive : bool, default True
        Whether to prompt user for Fiji path if not found automatically.
        Set to False for non-interactive environments (CI, scripts, etc.).
    ensure_java : bool, default True
        Whether to check and ensure Java is available. If True, will attempt
        to install OpenJDK 21 if Java is not found or version is too old.
        
    Raises
    ------
    RuntimeError
        If initialization fails or Fiji is not found.
    """
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
            raise RuntimeError(
                "Fiji installation not found. Please:\n"
                "  1. Set the FIJI_PATH environment variable, or\n"
                "  2. Pass the fiji_path parameter to initialize_snt()"
            )
            
        # Initialize PyImageJ from local Fiji
        logger.info(f"Initializing ImageJ with Fiji at: {fiji_path}")
        _ij = imagej.init(fiji_path, mode=mode)
        
        # Start JVM if not already started
        if not scyjava.jvm_started():
            scyjava.start_jvm()
            
        _jvm_started = True
        logger.info("SNT initialization complete")
        
    except Exception as e:
        logger.error(f"Failed to initialize SNT: {e}")
        raise RuntimeError(f"SNT initialization failed: {e}") from e


def _find_fiji(interactive: bool = True) -> Optional[str]:
    """
    Attempt to auto-detect Fiji installation with interactive fallback.
    
    Parameters
    ----------
    interactive : bool, default True
        Whether to prompt user for Fiji path if not found automatically.
        
    Returns
    -------
    str or None
        Path to Fiji if found, None otherwise.
    """
    logger = logging.getLogger(__name__)

    # Check environment variable first
    fiji_env = os.environ.get("FIJI_PATH")
    if fiji_env and Path(fiji_env).exists():
        logger.info(f"Found Fiji via FIJI_PATH environment variable: {fiji_env}")
        return fiji_env
        
    # Check common paths
    common_paths = [
        "/Applications/Fiji.app",  # macOS
        "C:/Fiji.app",
        "/opt/Fiji.app",
        os.path.expanduser("~/Fiji.app"),  # User home
        os.path.expanduser("~/Applications/Fiji.app"),  # macOS user
        os.path.expanduser("~/Desktop/Fiji.app"),  # Desktop
        os.path.expanduser("~/Downloads/Fiji.app"),  # Downloads
    ]
    for path in common_paths:
        if Path(path).exists():
            logger.info(f"Found Fiji at common location: {path}")
            return path
    
    # If not found and interactive mode is enabled, ask user
    if interactive:
        return _prompt_for_fiji_path()
    else:
        logger.warning("Fiji not found in common locations. Please specify fiji_path or set FIJI_PATH environment variable.")
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
    print("  2. Pass fiji_path parameter to initialize_snt()")
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
            
            # Optionally save to environment for future use
            save_env = input("❓Save this path to FIJI_PATH environment variable for future use? (y/N): ").strip().lower()
            if save_env in ['y', 'yes']:
                try:
                    # Note: This only sets for current session
                    os.environ['FIJI_PATH'] = fiji_path
                    print("✅ FIJI_PATH set for current session.")
                    print("👉 To make permanent, add this to your shell profile:")
                    print(f"   export FIJI_PATH='{fiji_path}'")
                except Exception as e:
                    print(f"⚠️  Could not set environment variable: {e}")
            
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
    print("  - pysnt.initialize_snt(fiji_path='/path/to/Fiji.app')")
    print("  - Set FIJI_PATH environment variable")
    
    return None


def _validate_fiji_path(fiji_path: str) -> bool:
    """
    Validate that a path points to a valid Fiji installation.
    
    Parameters
    ----------
    fiji_path : str
        Path to validate
        
    Returns
    -------
    bool
        True if path appears to be a valid Fiji installation
    """
    if not fiji_path or not os.path.exists(fiji_path):
        return False
    
    fiji_path_obj = Path(fiji_path)
    
    # Check for key Fiji/ImageJ components
    required_indicators = [
        "/config/environment.yml",
        "/jars",
    ]
    
    for indicator_group in required_indicators:
        found = False
        for indicator in indicator_group:
            if (fiji_path_obj / indicator).exists():
                found = True
                break
        if not found:
            return False
    
    return True


def get_imagej():
    """
    Get the ImageJ instance.
    
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
        raise RuntimeError("SNT not initialized. Call initialize_snt() first.")
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


def discover_java_classes(
    package_name: str, 
    known_classes: Optional[List[str]] = None,
    include_abstract: bool = False,
    include_interfaces: bool = False
) -> List[str]:
    """
    Discover all public classes in a Java package.
    
    This utility function can be used to dynamically discover classes
    from any Java package, with filtering for visibility and type.
    
    Parameters
    ----------
    package_name : str
        Full Java package name (e.g., 'sc.fiji.snt.analysis')
    known_classes : List[str], optional
        List of known class names to test. If None, attempts package scanning.
    include_abstract : bool, default False
        Whether to include abstract classes
    include_interfaces : bool, default False
        Whether to include interfaces
        
    Returns
    -------
    List[str]
        List of discovered public class names
        
    Examples
    --------
    >>> # Discover analysis classes
    >>> classes = discover_java_classes('sc.fiji.snt.analysis')
    >>> 
    >>> # Discover with known class list
    >>> known = ['TreeStatistics', 'ConvexHull']
    >>> classes = discover_java_classes('sc.fiji.snt.analysis', known)
    """
    logger = logging.getLogger(__name__)
    
    if not scyjava.jvm_started():
        logger.warning("JVM not started. Cannot discover classes.")
        return []
    
    try:
        # Import Java reflection classes
        Class = scyjava.jimport("java.lang.Class")
        Modifier = scyjava.jimport("java.lang.reflect.Modifier")
        
        classes = []
        
        # Method 1: Advanced package scanning from JAR files
        if known_classes is None:
            try:
                classes = _scan_package_from_jars(package_name, logger)
            except Exception as e:
                logger.debug(f"JAR scanning failed: {e}")
        
        # Method 2: Use provided known classes or fallback list
        if not classes and known_classes:
            test_classes = known_classes
        elif not classes:
            # Generate some common class name patterns to test
            test_classes = _generate_common_class_names(package_name)
        else:
            test_classes = []
        
        # Test each class for existence and visibility
        for class_name in test_classes:
            try:
                full_class_name = f"{package_name}.{class_name}"
                java_class = Class.forName(full_class_name)
                
                # Check class modifiers
                modifiers = java_class.getModifiers()
                
                # Filter based on visibility and type
                if not Modifier.isPublic(modifiers):
                    logger.debug(f"Skipping non-public class: {class_name}")
                    continue
                    
                if Modifier.isAbstract(modifiers) and not include_abstract:
                    logger.debug(f"Skipping abstract class: {class_name}")
                    continue
                    
                if Modifier.isInterface(modifiers) and not include_interfaces:
                    logger.debug(f"Skipping interface: {class_name}")
                    continue
                
                # Skip inner classes (contain $)
                if '$' in class_name:
                    logger.debug(f"Skipping inner class: {class_name}")
                    continue
                
                classes.append(class_name)
                logger.debug(f"Found public class: {class_name}")
                
            except Exception as e:
                logger.debug(f"Class not found or not accessible: {class_name} - {e}")
                continue
        
        # Remove duplicates and sort
        classes = sorted(list(set(classes)))
        logger.info(f"Discovered {len(classes)} public classes in {package_name}")
        return classes
        
    except Exception as e:
        logger.error(f"Failed to discover classes in {package_name}: {e}")
        return []


def _scan_package_from_jars(package_name: str, logger) -> List[str]:
    """
    Scan JAR files in classpath for classes in the specified package.
    
    Parameters
    ----------
    package_name : str
        Java package name (e.g., 'sc.fiji.snt.analysis')
    logger : Logger
        Logger instance for debug messages
        
    Returns
    -------
    List[str]
        List of class names found in JAR files
    """
    classes = []
    package_path = package_name.replace('.', '/')
    
    # Get classpath
    classpath = os.environ.get('CLASSPATH', '')
    
    # Look for relevant JAR files
    potential_jars = []
    if classpath:
        for path in classpath.split(os.pathsep):
            if any(keyword in path.lower() for keyword in ['snt']): # snt jar only for now
                potential_jars.append(path)
    
    # Scan JAR files
    for jar_path in potential_jars:
        if os.path.exists(jar_path) and jar_path.endswith('.jar'):
            try:
                with zipfile.ZipFile(jar_path, 'r') as jar:
                    for entry in jar.namelist():
                        if (entry.startswith(f'{package_path}/') and 
                            entry.endswith('.class')):
                            
                            # Extract class name
                            relative_path = entry[len(f'{package_path}/'):]
                            if '/' not in relative_path:  # Top-level class only
                                class_name = relative_path[:-6]  # Remove .class
                                if not class_name.startswith('$'):  # Skip inner classes
                                    classes.append(class_name)
                                    logger.debug(f"Found class in JAR: {class_name}")
                                    
            except Exception as e:
                logger.debug(f"Could not scan JAR {jar_path}: {e}")
    
    return classes


def _generate_common_class_names(package_name: str) -> List[str]:
    """
    Generate common class name patterns based on package name.
    
    This is a fallback when no known classes are provided and
    JAR scanning fails.
    
    Parameters
    ----------
    package_name : str
        Java package name
        
    Returns
    -------
    List[str]
        List of potential class names to test
    """
    # Extract package suffix for pattern generation
    parts = package_name.split('.')
    suffix = parts[-1] if parts else ""
    
    common_patterns = []
    
    if 'analysis' in suffix.lower():
        common_patterns = [
            "AbstractConvexHull", "AnalysisUtils", "AnnotationMapper", "CircularModels",
            "ColorMapper", "ConvexHull2D", "ConvexHull3D", "ConvexHullAnalyzer",
            "GroupedTreeStatistics", "MultiTreeColorMapper", "MultiTreeStatistics",
            "NodeColorMapper", "NodeProfiler", "NodeStatistics", "PathProfiler",
            "PathStatistics", "PathStraightener", "PCAnalyzer", "PersistenceAnalyzer",
            "ProfileProcessor", "RoiConverter", "RootAngleAnalyzer", "ShollAnalyzer",
            "SkeletonConverter", "SNTChart", "SNTTable", "StrahlerAnalyzer",
            "TreeColorMapper", "TreeStatistics"
        ]
    elif 'util' in suffix.lower():
        common_patterns = [
            "BoundingBox", "CircleCursor3D", "ColorMaps", "CrossoverFinder",
            "DiskCursor3D", "ImgUtils", "ImpUtils", "LinAlgUtils", "PathCursor",
            "PointInCanvas", "PointInImage", "SNTColor", "SNTPoint", "SWCPoint"
        ]
    elif 'viewer' in suffix.lower():
        common_patterns = [
            "Annotation3D", "Bvv", "ColorTableMapper", "GraphViewer", "MultiViewer2D",
            "MultiViewer3D", "MultiViewer", "Viewer2D", "Viewer3D"
        ]
    elif 'tracing' in suffix.lower():
        common_patterns = [
            "AbstractSearch", "BiSearch", "BiSearchNode", "DefaultSearchNode",
            "FillerThread", "ManualTracerThread", "SearchNode", "SearchThread",
            "TracerThread" 
        ]
    else:
        # Generic patterns for unknown packages
        common_patterns = [
            "Fill", "FillConverter", "NearPoint", "Path", "PathAndFillManager",
            "PathChangeEvent", "PathDownsampler", "PathFitter", "PathManagerUI",
            "SciViewSNT", "SearchProgressCallback", "SNT", "SNTService", "SNTUI",
            "SNTUtils", "TracerCanvas", "Tree", "TreeProperties"
        ]
    
    return common_patterns


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