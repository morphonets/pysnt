"""
Type stubs for data_display.py

Auto-generated stub file.
"""

from typing import Any, Dict, List, Optional, Union, Callable, Tuple

logger: Any
def _display_pandas_dataframe(df: Any, **kwargs: Any) -> Any: ...

def _show_pandasgui_dataframe(df: Any, title: Any, **kwargs: Any) -> bool: ...

def _display_xarray(xarr: Any, **kwargs: Any) -> None: ...

def _display_imageplus(obj: Any, **kwargs: Any) -> Any: ...

def _display_xarray_dataset(dataset: Any, **kwargs: Any) -> Any: ...

def _display_dataset_as_dataframe(dataset: Any, **kwargs: Any) -> bool: ...
