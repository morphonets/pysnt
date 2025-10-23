"""
Configuration system for PySNT

This module provides a global configuration system that allows to set
and get various options that control PySNT behavior

Examples
--------
>>> import pysnt
>>> pysnt.set_option('display.chart_format', 'svg')
>>> pysnt.get_option('display.chart_format')
'svg'
>>> pysnt.describe_option('display.chart_format')
display.chart_format: str
    Default export format for SNTChart
    [default: png] [currently: svg]
"""

import warnings
from typing import Any, Dict, List, Optional, Union
from collections.abc import Callable


class OptionError(AttributeError, KeyError):
    """Exception for option errors."""
    pass


class _Option:
    """Internal class to represent a configuration option."""
    
    def __init__(self, key: str, default_value: Any, doc: str, validator: Optional[Callable] = None):
        self.key = key
        self.default_value = default_value
        self.doc = doc
        self.validator = validator
        self._value = default_value
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, val):
        if self.validator:
            val = self.validator(val)
        self._value = val


def _chart_format_validator(value: str) -> str:
    """Validate chart format option."""
    valid_formats = {'svg', 'png', 'pdf'}
    if value not in valid_formats:
        raise ValueError(f"Invalid chart format '{value}'. Must be one of {valid_formats}")
    return value


def _table_display_validator(value: str) -> str:
    """Validate table display option."""
    valid_displays = {'pandasgui', 'distribution', 'summary', 'basic'}
    if value not in valid_displays:
        raise ValueError(f"Invalid table display '{value}'. Must be one of {valid_displays}")
    return value


def _positive_int_validator(value: int) -> int:
    """Validate positive integer."""
    if not isinstance(value, int) or value <= 0:
        raise ValueError(f"Value must be a positive integer, got {value}")
    return value


# Global configuration registry
_global_config: Dict[str, _Option] = {}


def _register_option(key: str, default_value: Any, doc: str, validator: Optional[Callable] = None):
    """Register a configuration option."""
    _global_config[key] = _Option(key, default_value, doc, validator)


# Register default options
_register_option(
    'display.chart_format', 
    'png',
    'Default export format for SNTChart (svg, png, or pdf)',
    _chart_format_validator
)

_register_option(
    'display.table_mode',
    'summary',
    'Default display mode for SNTTables (pandasgui, distribution, summary, or basic)',
    _table_display_validator
)

_register_option(
    'display.max_columns',
    20,
    'Maximum number of columns to display in table outputs',
    _positive_int_validator
)

_register_option(
    'display.max_rows',
    100,
    'Maximum number of rows to display in table outputs', 
    _positive_int_validator
)

_register_option(
    'display.precision',
    6,
    'Number of decimal places to display for floating point numbers',
    lambda x: max(0, int(x))
)

_register_option(
    'plotting.figure_size',
    (8, 8),
    'Default figure size for plots as (width, height) in inches',
    lambda x: tuple(float(v) for v in x) if len(x) == 2 else (8.0, 8.0)
)

_register_option(
    'display.gui_safe_mode',
    True,
    'Use safe GUI mode to avoid threading issues on macOS',
    lambda x: bool(x)
)

_register_option(
    'pyplot.ion',
    True,
    'Enable matplotlib interactive mode (plt.ion()) for better plot display',
    lambda x: bool(x)
)


def get_option(key: str) -> Any:
    """
    Get the value of a configuration option.
    
    Parameters
    ----------
    key : str
        The option key in dot notation (e.g., 'display.chart_format')
        
    Returns
    -------
    Any
        The current value of the option
        
    Raises
    ------
    OptionError
        If the option key is not found
        
    Examples
    --------
    >>> import pysnt
    >>> pysnt.get_option('display.chart_format')
    'png'
    """
    if key not in _global_config:
        raise OptionError(f"No such option: '{key}'. Use list_options() to see available options.")
    
    return _global_config[key].value


def set_option(key: str, value: Any) -> None:
    """
    Set the value of a configuration option.
    
    Parameters
    ----------
    key : str
        The option key in dot notation (e.g., 'display.chart_format')
    value : Any
        The new value for the option
        
    Raises
    ------
    OptionError
        If the option key is not found
    ValueError
        If the value is invalid for the option
        
    Examples
    --------
    >>> import pysnt
    >>> pysnt.set_option('display.chart_format', 'svg')
    >>> pysnt.set_option('display.max_rows', 50)
    """
    if key not in _global_config:
        raise OptionError(f"No such option: '{key}'. Use list_options() to see available options.")
    
    _global_config[key].value = value


def reset_option(key: str) -> None:
    """
    Reset an option to its default value.
    
    Parameters
    ----------
    key : str
        The option key to reset
        
    Examples
    --------
    >>> import pysnt
    >>> pysnt.reset_option('display.chart_format')
    """
    if key not in _global_config:
        raise OptionError(f"No such option: '{key}'")
    
    option = _global_config[key]
    option.value = option.default_value


def describe_option(key: Optional[str] = None) -> None:
    """
    Print description of one or all options.
    
    Parameters
    ----------
    key : str, optional
        The option key to describe. If None, describes all options.
        
    Examples
    --------
    >>> import pysnt
    >>> pysnt.describe_option('display.chart_format')
    display.chart_format: str
        Default export format for SNTChart (svg, png, or pdf)
        [default: png] [currently: png]
    """
    if key is not None:
        if key not in _global_config:
            raise OptionError(f"No such option: '{key}'")
        _describe_single_option(key)
    else:
        print("Available options:\n")
        for opt_key in sorted(_global_config.keys()):
            _describe_single_option(opt_key)
            print()


def _describe_single_option(key: str) -> None:
    """Print description of a single option."""
    option = _global_config[key]
    value_type = type(option.value).__name__
    
    print(f"{key}: {value_type}")
    print(f"    {option.doc}")
    print(f"    [default: {option.default_value}] [currently: {option.value}]")


def list_options() -> List[str]:
    """
    Get a list of all available option keys.
    
    Returns
    -------
    List[str]
        Sorted list of all option keys
        
    Examples
    --------
    >>> import pysnt
    >>> pysnt.list_options()
    ['display.chart_format', 'display.max_columns', 'display.max_rows', ...]
    """
    return sorted(_global_config.keys())


def option_context(**kwargs):
    """
    Context manager for temporarily setting options.
    
    Parameters
    ----------
    **kwargs
        Option key-value pairs to set temporarily
        
    Examples
    --------
    >>> import pysnt
    >>> with pysnt.option_context(display_chart_format='svg'):
    ...     # chart_format is temporarily 'svg'
    ...     chart = create_chart() # function to create a new graph
    ...     chart.save()  # saves as SVG
    # chart_format is back to original value
    """
    return _OptionContext(**kwargs)


class _OptionContext:
    """Context manager for temporarily changing options."""
    
    def __init__(self, **kwargs):
        self.options = kwargs
        self.old_values = {}
    
    def __enter__(self):
        # Save current values and set new ones
        for key, value in self.options.items():
            # Convert underscore notation to dot notation for convenience
            # Handle display_chart_format -> display.chart_format
            if '_' in key and '.' not in key:
                # Split on first underscore to get category.option format
                parts = key.split('_', 1)
                if len(parts) == 2:
                    key = f"{parts[0]}.{parts[1]}"
            
            if key in _global_config:
                self.old_values[key] = get_option(key)
                set_option(key, value)
            else:
                raise OptionError(f"No such option: '{key}'")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        # Restore old values
        for key, old_value in self.old_values.items():
            set_option(key, old_value)



# For backwards compatibility and pandas-style access
class _Config:
    """Config object for attribute access."""
    
    def __getattr__(self, name):
        # Convert attribute access to option key
        if '.' in name:
            key = name
        else:
            # Try to find matching option
            matches = [k for k in _global_config.keys() if k.endswith('.' + name)]
            if len(matches) == 1:
                key = matches[0]
            elif len(matches) > 1:
                raise OptionError(f"Ambiguous option '{name}'. Could be: {matches}")
            else:
                raise OptionError(f"No such option: '{name}'")
        
        return get_option(key)
    
    def __setattr__(self, name, value):
        # Convert attribute access to option key
        if '.' in name:
            key = name
        else:
            # Try to find matching option
            matches = [k for k in _global_config.keys() if k.endswith('.' + name)]
            if len(matches) == 1:
                key = matches[0]
            elif len(matches) > 1:
                raise OptionError(f"Ambiguous option '{name}'. Could be: {matches}")
            else:
                raise OptionError(f"No such option: '{name}'")
        
        set_option(key, value)


# Create global config object for pandas-style access
options = _Config()