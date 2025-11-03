"""
Type stubs for common_module.py

Auto-generated stub file.
"""

from typing import Any, Dict, List, Optional, Union, Callable, Tuple

logger: Any
def create_dynamic_placeholder_class(java_class_name: str, javadoc_name: str) -> Any: ...

def _normalize_class_name_for_python(class_name: str) -> str: ...

def _get_java_class_name(class_name: str) -> str: ...

def setup_module_classes(package_name: str, curated_classes: List[str], extended_classes: List[str], globals_dict: Dict[str, Any], discovery_packages: Optional[List[str]], include_interfaces: bool) -> Dict[str, Any]: ...
