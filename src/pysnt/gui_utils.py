"""
GUI utilities for PySNT to handle threading and platform-specific issues.
"""

import logging
import sys
import threading
from typing import Any, Callable, Optional

logger = logging.getLogger(__name__)


def is_main_thread() -> bool:
    """Check if we're running in the main thread."""
    return threading.current_thread() is threading.main_thread()


def is_macos() -> bool:
    """Check if we're running on macOS."""
    return sys.platform == 'darwin'


def safe_gui_call(func: Callable, *args, fallback_func: Optional[Callable] = None, **kwargs) -> Any:
    """
    Safely call a GUI function with proper thread handling.
    
    This function helps avoid the common macOS threading issue where Qt/GUI
    applications must be created on the main thread.
    
    Parameters
    ----------
    func : callable
        The GUI function to call
    *args
        Arguments to pass to the function
    fallback_func : callable, optional
        Fallback function to call if GUI function fails
    **kwargs
        Keyword arguments to pass to the function
        
    Returns
    -------
    Any
        Result of the function call, or None if failed
        
    Examples
    --------
    >>> def show_gui():
    ...     # Some GUI code that might fail on macOS
    ...     return some_gui.show(df)
    >>> 
    >>> def fallback():
    ...     print("GUI failed, showing in console")
    ...     print(df)
    >>> 
    >>> safe_gui_call(show_gui, fallback_func=fallback)
    """
    from .config import get_option
    
    try:
        gui_safe_mode = get_option('display.gui_safe_mode')
        
        if gui_safe_mode and is_macos() and not is_main_thread():
            logger.warning("GUI safe mode: Skipping GUI call due to threading restrictions on macOS")
            if fallback_func:
                return fallback_func(*args, **kwargs)
            else:
                logger.info("No fallback function provided")
                return None
        
        # Try the GUI function
        return func(*args, **kwargs)
        
    except Exception as e:
        logger.error(f"GUI function failed: {e}")
        if fallback_func:
            logger.info("Calling fallback function")
            try:
                return fallback_func(*args, **kwargs)
            except Exception as fallback_e:
                logger.error(f"Fallback function also failed: {fallback_e}")
        return None


def configure_gui_safety(enabled: bool = True) -> None:
    """
    Configure GUI safety mode.
    
    When enabled, GUI operations that might cause threading issues on macOS
    will fall back to console-based alternatives.
    
    Parameters
    ----------
    enabled : bool, default True
        Whether to enable GUI safety mode
        
    Examples
    --------
    >>> # Disable GUI safety to try GUI operations anyway
    >>> pysnt.configure_gui_safety(False)
    >>> 
    >>> # Re-enable for safety
    >>> pysnt.configure_gui_safety(True)
    """
    from .config import set_option
    
    set_option('display.gui_safe_mode', enabled)
    
    if enabled:
        logger.info("GUI safety mode enabled - will use console fallbacks on macOS threading issues")
    else:
        logger.warning("GUI safety mode disabled - GUI operations may cause crashes on macOS")

