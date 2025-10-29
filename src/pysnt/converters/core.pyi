"""
Type stubs for core.py

Auto-generated stub file.
"""

from typing import Any, Optional, Type, Dict, List

logger: Any
HAS_CAIROSVG: bool
cairosvg: Any
HAS_FITZ: bool
fitz: Any
HAS_PANDAS: bool
pd: Any
HAS_PANDASGUI: bool
pandasgui_show: Any
HAS_NETWORKX: bool
nx: Any
DEFAULT_CMAP: Any
DEFAULT_NODE_SIZE: Any
DEFAULT_NODE_COLOR: Any
DEFAULT_DPI: Any
DEFAULT_FIGSIZE: Any
DEFAULT_SCALE: Any
DEFAULT_MAX_PANELS: Any
DEFAULT_PANEL_LAYOUT: Any
FRAME_PARAM_NAMES: Any
ERROR_MISSING_NETWORKX: Any
ERROR_MISSING_PANDAS: Any
ERROR_MISSING_CAIROSVG: Any
ERROR_MISSING_FITZ: Any
INTERNAL_PARAMS: Any
class SNTObject:
    pass

def _create_snt_object(data_type: Type, data: Any, metadata: Optional[Dict[str, Any]], error: Optional[Exception]) -> SNTObject: ...

def _create_converter_result(data: Any, source_type: str, **metadata_kwargs: Any) -> 'SNTObject': ...

def _create_error_result(data_type: Type, error: Exception, source_type: str) -> 'SNTObject': ...

def _extract_frame_parameter(kwargs: Dict[str, Any]) -> int: ...

def _filter_matplotlib_kwargs(kwargs: Dict[str, Any], additional_exclude: Optional[List[str]]) -> Dict[str, Any]: ...

def _create_standard_error_message(operation: str, error: Exception, obj_type: str) -> str: ...

def _setup_matplotlib_interactive() -> Any: ...

def _matplotlib_context(figsize: Any, dpi: Any, **kwargs: Any) -> Any: ...

def _create_standard_figure(data: Any, title: Any, figsize: Any, dpi: Any, cmap: Any, add_colorbar: Any, is_rgb: Any, **kwargs: Any) -> Any: ...

def _temp_file(format_type: Any, temp_dir: Any, cleanup: Any) -> Any: ...

def _temp_directory(temp_dir: Any, cleanup: Any) -> Any: ...

def _get_java_class_name(obj: Any) -> str: ...

class JavaTypeDetector:
    def has_class_name(obj: Any, *names: Any) -> bool: ...
    def has_methods(obj: Any, *method_names: Any) -> bool: ...
    def matches_pattern(obj: Any, class_patterns: List[str], required_methods: List[str]) -> bool: ...

def _extract_color_attributes(color_obj: Any, prefix: str) -> Dict[str, Any]: ...
