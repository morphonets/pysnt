"""
Java object enhancement functionality.

This module provides enhanced methods for Java objects, including:
- Enhancement predicate functions for object type detection
- Enhancement classes that add methods to Java objects
- Enhancement functions for automatic object enhancement
- Object type predicates for different SNT object types

Dependencies: core.py
"""

from typing import Any

from .chart_converters import _is_snt_chart
from .core import logger


def _should_enhance_object(obj) -> bool:
    """Check if object should be enhanced with fallback methods."""
    return _is_snt_chart(obj) or _is_gui_object(obj)


def _is_gui_object(obj) -> bool:
    """Check if object is a Java GUI object (typically a Swing/AWT class) that should
    have enhanced setVisible() method."""
    try:
        # Check if it's a Java object with setVisible() method
        return (
                hasattr(obj, 'setVisible') and
                (hasattr(obj, 'getFrame') or hasattr(obj, 'show') or
                 hasattr(obj, 'pack') or hasattr(obj, 'setTitle') or
                 str(type(obj)).find('UI') != -1 or str(type(obj)).find('Frame') != -1 or
                 str(type(obj)).find('Dialog') != -1 or str(type(obj)).find('Window') != -1)
        )
    except (AttributeError, TypeError, RuntimeError):
        return False


class EnhancedJavaObject:
    """
    Wrapper class that adds enhanced show() and setVisible() methods to Java objects.
    
    This wrapper delegates all attribute access to the wrapped Java object,
    but provides enhanced methods with fallback logic for GUI operations.
    """

    def __init__(self, java_obj):
        """Initialize with a Java object to wrap."""
        object.__setattr__(self, '_java_obj', java_obj)
        object.__setattr__(self, '_is_chart', _is_snt_chart(java_obj))
        object.__setattr__(self, '_is_gui', _is_gui_object(java_obj))
        object.__setattr__(self, '_enhanced', _should_enhance_object(java_obj))

    def __getattr__(self, name):
        """Delegate attribute access to the wrapped Java object."""
        is_chart = object.__getattribute__(self, '_is_chart')
        is_gui = object.__getattribute__(self, '_is_gui')

        if name == 'show' and is_chart:
            return self._enhanced_show
        elif name == 'setVisible' and is_gui:
            return self._enhanced_setVisible

        return getattr(object.__getattribute__(self, '_java_obj'), name)

    def __setattr__(self, name, value):
        """Delegate attribute setting to the wrapped Java object."""
        if name.startswith('_'):
            object.__setattr__(self, name, value)
        else:
            setattr(object.__getattribute__(self, '_java_obj'), name, value)

    def __dir__(self):
        """Return attributes from the wrapped Java object."""
        return dir(object.__getattribute__(self, '_java_obj'))

    def __repr__(self):
        """Return representation of the wrapped Java object."""
        java_obj = object.__getattribute__(self, '_java_obj')
        enhanced = object.__getattribute__(self, '_enhanced')
        if enhanced:
            return f"<Enhanced {repr(java_obj)}>"
        return repr(java_obj)

    def _enhanced_show(self, *args, **kwargs):
        """
        Enhanced show method with fallback to display().
        
        This method first tries the original Java show() method, and if that fails
        (e.g., due to HeadlessException), it falls back to display() which can 
        handle SNT-specific conversions.
        """
        java_obj = object.__getattribute__(self, '_java_obj')
        try:
            # Try to call the original Java show method
            original_show = getattr(java_obj, 'show')
            return original_show(*args, **kwargs)

        except Exception as e:
            logger.info(f"Original show() failed ({e}), falling back to auto-conversion")
            # Fallback: use auto-conversion display
            try:
                # Import here to avoid circular imports
                from .display import _display_with_auto_conversion
                return _display_with_auto_conversion(java_obj, **kwargs)
            except Exception as conv_e:
                logger.error(f"Auto-conversion display failed: {conv_e}")
                return None

    def _enhanced_setVisible(self, visible=True, **kwargs):
        """
        Enhanced setVisible method with fallback to display().
        
        This method first tries the original Java setVisible() method, and if that fails
        (e.g., due to HeadlessException), it falls back to display() when visible=True.
        """
        java_obj = object.__getattribute__(self, '_java_obj')
        try:
            # Try to call the original Java setVisible method
            original_setVisible = getattr(java_obj, 'setVisible')
            return original_setVisible(visible)

        except Exception as e:
            if visible:
                logger.info(f"Original setVisible(true) failed ({e}), falling back to auto-conversion")
                # Only fallback to display when trying to make visible (not when hiding)
                try:
                    # Import here to avoid circular imports
                    from .display import _display_with_auto_conversion
                    return _display_with_auto_conversion(java_obj, **kwargs)
                except Exception as conv_e:
                    logger.error(f"Auto-conversion display failed: {conv_e}")
                    return None
            else:
                # For setVisible(false), just log and return (nothing to display)
                logger.info(f"setVisible(false) failed ({e}), ignoring (object already hidden)")
                return None


def _enhanced_show_method(original_obj):
    """
    Create an enhanced show() method that falls back to display() on failure.
    
    Parameters
    ----------
    original_obj : Any
        The original Java object
        
    Returns
    -------
    callable
        Enhanced show method with fallback logic
    """

    def enhanced_show(*args, **kwargs):
        """
        Enhanced show method with fallback to display().
        
        This method first tries the original Java show() method, and if that fails
        (e.g., due to HeadlessException), it falls back to display() which should
        handle SNT-specific conversions.
        """
        try:
            # Try to call the original Java show method
            # Get the original show method from the Java object
            original_show = getattr(original_obj.__class__, 'show', None)
            if original_show:
                return original_show(original_obj, *args, **kwargs)
            else:
                # Fallback if no original show method
                raise AttributeError("No original show method found")

        except Exception as e:
            logger.info(f"Original show() failed ({e}), falling back to auto-conversion")
            # Fallback to auto-conversion
            from .display import _display_with_auto_conversion
            return _display_with_auto_conversion(original_obj, **kwargs)

    return enhanced_show


def enhance_java_object(obj: Any) -> Any:
    """
    Enhance a Java object with fallback show() and setVisible() methods if applicable.
    
    This function checks if the object is an SNT chart or GUI object and if so, wraps it
    with an enhanced version that falls back to display() on GUI method failures.
    
    Parameters
    ----------
    obj : Any
        Java object to potentially enhance
        
    Returns
    -------
    Any
        Enhanced wrapper object if applicable, otherwise the original object
        
    Examples
    --------
    >>> # For charts
    >>> chart = stats.getHistogram('Branch length')
    >>> enhanced_chart = enhance_java_object(chart)
    >>> enhanced_chart.show()  # Will fallback to display() if GUI fails

    >>> # For GUI objects
    >>> ui = pysnt.PathManagerUI()
    >>> enhanced_ui = enhance_java_object(ui)
    >>> enhanced_ui.setVisible(True)  # Will fallback to display() if GUI fails
    """
    if _should_enhance_object(obj):
        try:
            enhanced_obj = EnhancedJavaObject(obj)
            enhancement_types = []
            if _is_snt_chart(obj):
                enhancement_types.append("show()")
            if _is_gui_object(obj):
                enhancement_types.append("setVisible()")

            logger.debug(f"Enhanced {type(obj).__name__} with fallback {', '.join(enhancement_types)} method(s)")
            return enhanced_obj
        except Exception as e:
            logger.warning(f"Failed to enhance object with fallback methods: {e}")

    return obj


def auto_enhance_java_objects(enabled: bool = True):
    """
    Enable or disable automatic enhancement of Java objects.
    
    When enabled, this function monkey-patches scyjava's jimport to automatically
    enhance returned Java objects with fallback show() methods.
    
    Parameters
    ----------
    enabled : bool, default True
        Whether to enable automatic enhancement
        
    Note
    ----
    This is experimental and may have side effects. Use with caution.
    """
    if not enabled:
        logger.info("Auto-enhancement of Java objects disabled")
        return

    try:
        # This would require more complex implementation to intercept
        # all Java object creation. For now, we'll rely on manual enhancement.
        logger.info("Auto-enhancement not yet implemented. Use enhance_java_object() manually.")
    except Exception as e:
        logger.error(f"Failed to enable auto-enhancement: {e}")


def _is_snt_tree(obj) -> bool:
    """Check if object is an SNT Tree."""
    try:
        return hasattr(obj, 'getRoot') and hasattr(obj, 'getNodes') and hasattr(obj, 'setRadii')
    except (AttributeError, TypeError, RuntimeError):
        return False


def _is_snt_path(obj) -> bool:
    """Check if object is an SNT Path."""
    try:
        return hasattr(obj, 'findJunctions') and hasattr(obj, 'getCanvasOffset') and hasattr(obj, 'getFitted')
    except (AttributeError, TypeError, RuntimeError):
        return False


def _is_xarray_object(obj) -> bool:
    """Check if object is an xarray DataArray or Dataset."""
    # Import here to avoid circular imports
    from .display import _get_display_handler
    obj_type, _ = _get_display_handler(obj)
    return obj_type == 'xarray'