"""
Type stubs for gui_utils.py

Auto-generated stub file.
"""

from typing import Any

logger: Any
def is_main_thread() -> bool: ...

def is_macos() -> bool: ...

def safe_gui_call(func: Callable, *args: Any, **kwargs: Any) -> Any: ...

def configure_gui_safety(enabled: bool) -> None: ...

def main_thread_wrapper(func: Callable) -> Callable: ...
