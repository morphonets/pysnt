"""
Core initialization and setup for PySNT.

This module handles the initialization of the Java environment and
Fiji integration required for SNT functionality.
"""

import logging
import os
import platform
from pathlib import Path
from typing import Optional, List, Dict, Any

try:
    import scyjava
    import imagej
except ImportError as e:
    raise ImportError("Required dependencies not found.") from e

logger = logging.getLogger(__name__)


class _DropKnownPyImageJNoise(logging.Filter):
    """Drop one known-harmless PyImageJ warning, leaving everything else untouched.

    PyImageJ cannot parse PySNT's open-ended Java constraint ("21+"), logs
    "Failed to guess the Java version." and, as a result, would not add its own
    --add-opens option (PySNT adds it itself, see initialize())
    """
    _MESSAGES = ("Failed to guess the Java version.",)

    def filter(self, record):
        return record.getMessage() not in self._MESSAGES

# Global state
_ij = None
_jvm_started = False
_mode = None
_source = None  # 'maven' or 'fiji': where the running SNT came from


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
    
    # Add logging system properties based on current configuration
    from .config import get_option
    try:
        # Read current logging configuration
        level = get_option('java.logging.level').lower()
        suppress_slf4j = get_option('java.logging.suppress_slf4j_warnings')
        
        # Add system properties to control logging during JVM startup
        logging_properties = [
            # SLF4J configuration
            f"-Dorg.slf4j.simpleLogger.defaultLogLevel={level}",
            "-Dorg.slf4j.simpleLogger.showDateTime=false",
            "-Dorg.slf4j.simpleLogger.showThreadName=false",
            "-Dorg.slf4j.simpleLogger.showLogName=false",
            "-Dorg.slf4j.simpleLogger.showShortLogName=false",
            
            # Log4j configuration
            f"-Dlog4j.rootLogger={level.upper()},console",
            "-Dlog4j.logger.org.apache=ERROR",
            "-Dlog4j.logger.org.scijava=ERROR",
            "-Dlog4j.logger.net.imagej=ERROR",
            
            # Java util logging
            f"-Djava.util.logging.level={level.upper()}",
            "-Djava.util.logging.ConsoleHandler.level=ERROR",
            
            # ImageJ/SciJava specific
            "-Dscijava.log.level=error",
            "-Dimagej.log.level=error",
        ]
        
        # Add SLF4J warning suppression if requested
        if suppress_slf4j:
            slf4j_suppression_properties = [
                # Try to suppress SLF4J multiple bindings warnings
                "-Dorg.slf4j.simpleLogger.log.org.slf4j=ERROR",
                "-Dorg.slf4j.simpleLogger.log.ch.qos.logback=ERROR",
                # Redirect SLF4J output to null (aggressive suppression)
                "-Dorg.slf4j.simpleLogger.logFile=System.err",
            ]
            logging_properties.extend(slf4j_suppression_properties)
        
        for prop in logging_properties:
            scyjava.config.add_option(prop)
            logger.debug(f"Added logging property: {prop}")
        
        logger.debug("Added logging system properties based on configuration")
        
    except Exception as e:
        logger.debug(f"Failed to add logging properties: {e}")
    
    logger.info("JVM configuration complete")


def initialize(fiji_path: Optional[str] = None, interactive: bool = True, ensure_java: bool = True, mode: str = "headless", 
               max_heap: Optional[str] = None, min_heap: Optional[str] = None, jvm_args: Optional[List[str]] = None,
               snt_version: Optional[str] = None, extras: Optional[List[str]] = None,
               source: Optional[str] = None) -> None:
    """
    Initialize the SNT environment (ImageJ2 + SNT), from Maven or from Fiji.

    By default SNT is resolved from Maven (``org.morphonets:SNT``), so no Fiji
    installation is required. A local Fiji is used instead when one is
    requested. Source precedence (``source=None``):

    1. ``fiji_path`` argument
    2. ``FIJI_PATH`` environment variable
    3. Fiji path saved with ``pysnt.set_fiji_path()``
    4. Maven (default)

    Parameters
    ----------
    fiji_path : str, optional
        Path to a Fiji installation. Can also be a mode string for
        convenience (e.g., "gui", "interactive").
    interactive : bool, default True
        Whether Java may be installed interactively if missing. Fiji is never
        prompted for: if none is configured, Maven is used.
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
    snt_version : str, optional
        SNT version to resolve from Maven (Maven source only). Defaults to the
        SNT_VERSION environment variable, then to the version PySNT targets.
    extras : List[str], optional
        Additional Maven endpoints (Maven source only). None adds PySNT's
        defaults (BigVolumeViewer, needed by Bvv); [] adds nothing.
    source : {"maven", "fiji"}, optional
        Force the source instead of following the precedence above.
        "maven" (aliases "remote", "online") downloads SNT, no Fiji needed.
        "fiji" (alias "local") uses a local Fiji.app: if none is configured,
        common install locations are scanned and, when ``interactive`` is
        True, you are prompted for the path (the result is saved).

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
    global _ij, _jvm_started, _mode, _source
    
    if _jvm_started:
        requested = None
        if fiji_path:
            requested = "fiji"
        elif source:
            requested = _SOURCE_ALIASES.get(str(source).lower())
        if requested and requested != _source:
            logger.warning(
                f"SNT is already running from {_source}: the JVM cannot be restarted, so "
                f"source='{requested}' was ignored. Restart the kernel/console to switch.")
        else:
            logger.info("SNT already initialized")
        return
        
    try:
        # Check and ensure Java is available
        if ensure_java:
            from .java_utils import ensure_java_available
            if not ensure_java_available(auto_install=interactive):
                logger.warning("Java requirements not met, but continuing initialization")

        # Make JAVA_HOME explicit. Without it, JPype's macOS discovery returns bytes and
        # scyjava.start_jvm() crashes ("a bytes-like object is required, not 'str'")
        # https://github.com/scijava/scyjava/issues/95
        if not os.environ.get("JAVA_HOME"):
            from .java_utils import resolve_java_home
            java_home = resolve_java_home()
            if java_home:
                os.environ["JAVA_HOME"] = java_home
                logger.info(f"JAVA_HOME not set: using {java_home}")

        # Tell scyjava to prefer an existing system JDK meeting SNT's actual
        # requirement, instead of silently downloading/using its own cached
        # JDK. scyjava's own defaults (fetch="always", version="11") ignore
        # JAVA_HOME entirely and always fetch a Java 11 via cjdk, regardless
        # of what Java is already installed and correctly configured.
        from .java_utils import REQUIRED_JAVA_VERSION
        scyjava.config.set_java_constraints(
            fetch="auto", version=f"{REQUIRED_JAVA_VERSION}+"
        )

        # Java 17+ blocks the bytecode patching that ImageJ1 needs unless java.lang is opened.
        # pyimagej adds this option itself, but only if it can parse the requested Java version,
        # which fails for a constraint such as "21+" ("Failed to guess the Java version.")
        # and then surfaces as "Invalid service: net.imagej.legacy.LegacyService"
        # JPype loads a native library: Java 24+ warns about it unless native access is enabled
        _jvm_opts = ["--add-opens=java.base/java.lang=ALL-UNNAMED",
                     "--enable-native-access=ALL-UNNAMED"]
        # On macOS, ImageJ1 (IJ1Helper) reflectively accesses com.apple.eawt (dock icon, menu
        # bar, etc.) when the legacy GUI is initialized ("gui"/"interactive" modes). Java 17+
        # does not export that package to unnamed modules by default, which otherwise fails with
        # "IllegalAccessException: ... module java.desktop does not export com.apple.eawt"
        # (the same option is added by the Fiji launcher)
        if platform.system() == "Darwin":
            _jvm_opts.append("--add-opens=java.desktop/com.apple.eawt=ALL-UNNAMED")
        for _opt in _jvm_opts:
            if _opt not in scyjava.config.get_options():
                scyjava.config.add_option(_opt)

        # Decide where SNT comes from: a Fiji install, or Maven
        fiji_path = _select_source(fiji_path, source, interactive)
        _source = "fiji" if fiji_path else "maven"
        if fiji_path:
            if not Path(fiji_path).expanduser().exists():
                raise FijiNotFoundError(f"Fiji not found at: {fiji_path}")
            fiji_path = _resolve_fiji_path(fiji_path)
            if not _validate_fiji_path(fiji_path):
                logger.warning(f"Fiji at {fiji_path} may be incomplete (e.g., no SNT jar found)")
            ij_source = fiji_path
        else:
            from ._endpoints import build_endpoints
            ij_source = build_endpoints(snt_version, extras)
            logger.info(f"No Fiji configured: resolving SNT from Maven: {ij_source}")

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
        
        # Initialize PyImageJ (Fiji install or Maven endpoints)
        logger.info(f"Initializing ImageJ from: {ij_source}")
        _noise = _DropKnownPyImageJNoise()
        _ij_logger = logging.getLogger("imagej")
        _ij_logger.addFilter(_noise)
        try:
            _ij = imagej.init(ij_source, mode=mode)
        finally:
            _ij_logger.removeFilter(_noise)
        
        # Store the mode for later retrieval
        _mode = mode
        
        # Start JVM if not already started
        if not scyjava.jvm_started():
            if "headless" == mode:
                scyjava.config.enable_headless_mode() # System.setProperty("java.awt.headless", "true");
            scyjava.start_jvm()
            
        # Configure Java logging after JVM starts
        try:
            from .java_utils import configure_java_logging
            if configure_java_logging():
                logger.debug("Configured Java logging")
            else:
                logger.debug("Some Java logging configuration failed, but continuing")
        except Exception as e:
            logger.debug(f"Failed to configure Java logging: {e}")
            # Don't fail initialization for logging configuration issues
            
        _jvm_started = True
        logger.info("SNT initialization complete")
        # An explicit Maven version pin is deliberate: no mismatch warning for it
        _check_snt_version(requested=not fiji_path and bool(snt_version or os.environ.get("SNT_VERSION")))
        if _source == "maven":
            _check_jogamp_version()
        
    except FijiNotFoundError:
        # Re-raise FijiNotFoundError as-is (it already has helpful messages)
        raise
    except Exception as e:
        logger.error(f"Failed to initialize SNT: {e}")
        raise RuntimeError(f"SNT initialization failed: {e}") from e


_SOURCE_ALIASES = {
    "maven": "maven", "remote": "maven", "online": "maven",
    "fiji": "fiji", "local": "fiji",
}


def _major_minor(version: str) -> Optional[tuple]:
    """(major, minor) from e.g. '5.0.24-SNAPSHOT-abc123', or None"""
    import re
    m = re.match(r"\s*(\d+)\.(\d+)", str(version or ""))
    return (int(m.group(1)), int(m.group(2))) if m else None


def snt_version() -> Optional[str]:
    """
    Version of the SNT library loaded in the JVM (e.g. '5.0.24'), or None if
    PySNT has not been initialized.
    """
    # Never start a JVM as a side effect of asking for a version
    if not _jvm_started or not scyjava.jvm_started():
        return None
    try:
        return str(scyjava.jimport("sc.fiji.snt.SNTUtils").VERSION)
    except Exception:
        return None


def _check_snt_version(requested: bool) -> None:
    """
    Warn (never fail) when the loaded SNT differs in major.minor from the version
    PySNT's stubs and docs describe. Silent if the user pinned a version explicitly.
    """
    if requested:
        return
    from ._endpoints import DEFAULT_SNT_VERSION
    loaded = snt_version()
    if loaded is None:
        return
    if _major_minor(loaded) != _major_minor(DEFAULT_SNT_VERSION):
        logger.warning(
            f"Loaded SNT {loaded}, but this PySNT targets SNT {DEFAULT_SNT_VERSION}: "
            "some classes or methods may be missing or behave differently. "
            "Use source='maven' (default without a configured Fiji) or update Fiji."
        )


def _check_jogamp_version() -> None:
    """
    Warn (never fail) when the jogl-all jar resolved by Maven differs from
    JOGAMP_VERSION, i.e., the natives PySNT requests would not match it
    """
    import re
    from ._endpoints import JOGAMP_VERSION, jogamp_natives_endpoints
    if not jogamp_natives_endpoints():
        return  # no natives published for this platform
    try:
        classpath = str(scyjava.jimport("java.lang.System").getProperty("java.class.path"))
    except Exception:
        return
    found = {m.group(1) for m in re.finditer(r"jogl-all-(\d+(?:\.\d+)+)\.jar", classpath)}
    if found and found != {JOGAMP_VERSION}:
        logger.warning(
            f"Resolved jogl-all {', '.join(sorted(found))}, but PySNT requests JogAmp natives "
            f"{JOGAMP_VERSION}: 3D viewers may fail to load. Update JOGAMP_VERSION in pysnt/_endpoints.py")


def _is_imagej_root(path: Path) -> bool:
    """True if path looks like an ImageJ2/Fiji application directory (has a jars folder)."""
    return (path / "jars").is_dir()


def _resolve_fiji_path(fiji_path: str) -> str:
    """
    Return the ImageJ/Fiji root for a user-supplied path, tolerating near misses.

    Accepts the path itself, a child named Fiji.app/Fiji (user pointed to the folder
    that contains the install), or the parent (user pointed one level too deep).
    Anything else raises FijiNotFoundError with the locations that were checked,
    rather than letting pyimagej fail later with a generic JVM error.
    """
    path = Path(fiji_path).expanduser()
    if _is_imagej_root(path):
        return str(path)
    candidates = [path / "Fiji.app", path / "Fiji", path.parent]
    for candidate in candidates:
        if _is_imagej_root(candidate):
            logger.info(f"'{path}' is not an ImageJ/Fiji root; using '{candidate}' instead")
            return str(candidate)
    raise FijiNotFoundError(
        f"'{path}' does not look like a Fiji/ImageJ2 installation (no 'jars' folder).\n"
        "Checked: " + ", ".join(str(c) for c in [path] + candidates) + "\n"
        "Point fiji_path to the Fiji.app folder, or omit it to download SNT from Maven."
    )


def _select_source(fiji_path: Optional[str], source: Optional[str], interactive: bool = False) -> Optional[str]:
    """
    Return the Fiji path to use, or None to resolve SNT from Maven.

    Precedence: explicit fiji_path > FIJI_PATH > saved config > Maven.
    source="maven" (aliases: "remote", "online") forces Maven.
    source="fiji" (alias: "local") requires a local Fiji: when none is
    configured, common install locations are scanned and, if interactive,
    the user is prompted.
    """
    if source is not None:
        canonical = _SOURCE_ALIASES.get(str(source).lower())
        if canonical is None:
            raise ValueError(
                f"source must be 'maven' (or 'remote'/'online') or 'fiji' (or 'local'), not {source!r}")
        source = canonical
    if source == "maven":
        return None
    if fiji_path:
        return str(fiji_path)
    found = _find_configured_fiji()
    if found is None and source == "fiji":
        found = _find_fiji(interactive=interactive)
        if found is None:
            raise FijiNotFoundError(
                "source='fiji' requested but no Fiji was found. Pass fiji_path, set "
                "FIJI_PATH, or run: pysnt setup --auto-detect")
    return found


def _find_configured_fiji() -> Optional[str]:
    """Fiji from FIJI_PATH or the saved config; no scanning, no prompting."""
    from . import setup_utils

    fiji_env = os.environ.get("FIJI_PATH")
    if fiji_env and Path(fiji_env).exists():
        logger.info(f"Using Fiji from FIJI_PATH: {fiji_env}")
        return fiji_env
    fiji_config = setup_utils.load_config().get("fiji_path")
    if fiji_config and Path(fiji_config).exists():
        logger.info(f"Using Fiji from saved config: {fiji_config}")
        return fiji_config
    elif fiji_config:
        logger.warning(f"Saved Fiji path no longer exists, removing it from config: {fiji_config}")
        config = setup_utils.load_config()
        config.pop("fiji_path", None)
        setup_utils.save_config(config)
    return None


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

    # 1-2. FIJI_PATH environment variable, then saved config (single implementation)
    configured = _find_configured_fiji()
    if configured:
        return configured

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


def get_mode() -> Optional[str]:
    """
    Get the initialization mode used.
    
    Returns the mode that was specified when initialize() was called.
    This indicates how the ImageJ/Fiji environment was started.
    
    Returns
    -------
    str or None
        The mode used during initialization:
        - "headless": No GUI, for batch processing and scripts
        - "gui": Full GUI mode with ImageJ windows
        - "interactive": Interactive mode with some GUI elements
        - "interactive:force": Force interactive mode
        - None: If SNT has not been initialized yet
        
    Examples
    --------
    >>> import pysnt
    >>> pysnt.initialize("headless")
    >>> pysnt.get_mode()
    'headless'
    >>> 
    >>> # Check mode before performing GUI operations
    >>> if pysnt.get_mode() in ["gui", "interactive"]:
    ...     pysnt.show(image)
    ... else:
    ...     print("GUI not available in headless mode")
    """
    return _mode


def dispose() -> None:
    """
    Dispose of PySNT resources and shut down the JVM.
    
    This function properly cleans up all resources created by initialize(),
    including the ImageJ instance and the Java Virtual Machine. After calling
    dispose(), you will need to call initialize() again to use PySNT functionality.
    
    The cleanup process includes:
    1. Disposing of the ImageJ instance (if available)
    2. Shutting down the JVM via scyjava
    3. Resetting internal state variables
    
    Notes
    -----
    - After calling dispose(), the JVM cannot be restarted in the same Python session
    - This is a limitation of the JVM architecture - once shut down, it cannot be restarted
    - If you need to reinitialize PySNT, you must restart your Python session
    - This function is safe to call multiple times or when PySNT is not initialized
    
    Examples
    --------
    >>> import pysnt
    >>> pysnt.initialize()
    >>> # ... do work with PySNT ...
    >>> pysnt.dispose()  # Clean shutdown
    >>> 
    >>> # To use PySNT again, restart Python session and call initialize()
    
    Warnings
    --------
    After calling dispose(), you cannot reinitialize PySNT in the same Python session.
    The JVM cannot be restarted once it has been shut down.
    """
    global _ij, _jvm_started, _mode
    
    logger.info("Disposing PySNT resources...")
    
    try:
        # 1. Dispose of ImageJ instance if available
        if _ij is not None:
            try:
                logger.debug("Disposing ImageJ instance...")
                _ij.dispose()
                logger.debug("ImageJ instance disposed successfully")
            except Exception as e:
                logger.warning(f"Error disposing ImageJ instance: {e}")
            finally:
                _ij = None
        
        # 2. Shut down the JVM if it was started
        if _jvm_started and scyjava.jvm_started():
            try:
                logger.debug("Shutting down JVM...")
                scyjava.shutdown_jvm()
                logger.debug("JVM shutdown successfully")
            except Exception as e:
                logger.warning(f"Error shutting down JVM: {e}")
        
        # 3. Reset state variables
        _jvm_started = False
        _mode = None
        
        logger.info("PySNT disposal complete")
        
    except Exception as e:
        logger.error(f"Error during PySNT disposal: {e}")
        # Still reset state even if there were errors
        _ij = None
        _jvm_started = False
        _mode = None
        raise RuntimeError(f"PySNT disposal failed: {e}") from e




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


def extract_figure(display_result):
    """
    Extract matplotlib figure from display result.
    
    This convenience function extracts the underlying data (typically a matplotlib figure)
    from an SNTObject dictionary returned by pysnt.display(). If the input is already
    a matplotlib figure or other object, it returns it unchanged.
    
    Parameters
    ----------
    display_result : Any
        Result from pysnt.display() - can be:
        - SNTObject dictionary (data will be extracted)
        - matplotlib.Figure (returned as-is)
        - Any other object (returned as-is)
        
    Returns
    -------
    Any
        The extracted data (typically matplotlib.Figure) or the original object
        
    Examples
    --------
    >>> import pysnt
    >>> pysnt.initialize()
    >>> 
    >>> # Extract figure from display result
    >>> result = pysnt.display(tree)
    >>> fig = pysnt.extract_figure(result)  # matplotlib.Figure
    >>> 
    >>> # Works with lists for multi-panel display
    >>> fig1 = pysnt.extract_figure(pysnt.display(img))
    >>> fig2 = pysnt.extract_figure(pysnt.display(tree))
    >>> pysnt.display([fig1, fig2], panel_layout=(1,2))
    >>> 
    >>> # Also works with objects that aren't SNTObject dicts
    >>> fig = plt.figure()
    >>> same_fig = pysnt.extract_figure(fig)  # Returns fig unchanged
    """
    if isinstance(display_result, dict) and 'data' in display_result:
        return display_result['data']
    return display_result






