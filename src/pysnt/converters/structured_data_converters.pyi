"""
Type stubs for structured_data_converters.py

Auto-generated stub file.
"""

from typing import Any

from pysnt.converters.core import SNTObject


def _is_snt_table(obj: Any) -> bool: ...

def _convert_snt_table(table: Any, **kwargs: Any) -> SNTObject: ...

def _convert_path_to_xarray(path: Any) -> Any: ...

def _extract_imageplus_metadata(imageplus: Any, **kwargs: Any) -> dict: ...