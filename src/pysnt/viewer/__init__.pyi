"""
Type stubs for __init__.py

Auto-generated stub file.
"""

from typing import Any

logger: Any
CURATED_CLASSES: Any
EXTENDED_CLASSES: Any
class Viewer2D:
    pass

class Viewer3D:
    pass

class MultiViewer:
    pass

def _java_setup() -> Any: ...

def _discover_extended_classes() -> Any: ...

def get_available_classes() -> List[str]: ...

def get_class(class_name: str) -> Any: ...

def list_classes() -> Any: ...

def get_curated_classes() -> List[str]: ...

def get_extended_classes() -> List[str]: ...

def __getattr__(name: str) -> Any: ...

def __dir__() -> List[str]: ...

__all__: Any