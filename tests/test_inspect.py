#!/usr/bin/env python3
"""
Tests for the pysnt.inspect() function.
"""

import sys
from pathlib import Path
from unittest.mock import Mock, patch
from io import StringIO

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

def test_inspect_function_exists():
    """Test that the inspect function is available in pysnt."""
    import pysnt
    
    # Check that inspect function exists
    assert hasattr(pysnt, 'inspect')
    assert callable(pysnt.inspect)


def test_inspect_without_jvm():
    """Test inspect function behavior when JVM is not started."""
    import pysnt
    
    # This test just checks that the function can be called
    # The actual JVM check is tested in integration tests
    try:
        # This should either work or print an error message
        # We're just testing that it doesn't crash
        with patch('builtins.print'):
            pysnt.inspect('TreeStatistics')
    except Exception as e:
        # If there's an exception, it should be related to JVM or imports
        assert any(keyword in str(e).lower() for keyword in ['jvm', 'scyjava', 'import'])


def test_inspect_function_signature():
    """Test that inspect function has the expected signature."""
    import pysnt
    import inspect as py_inspect
    
    # Get function signature
    sig = py_inspect.signature(pysnt.inspect)
    
    # Check expected parameters exist
    expected_params = [
        'class_or_object', 'keyword', 'methods', 'fields', 
        'constructors', 'static_only', 'case_sensitive', 'max_results'
    ]
    
    actual_params = list(sig.parameters.keys())
    
    for param in expected_params:
        assert param in actual_params, f"Parameter '{param}' missing from inspect function"


def test_inspect_parameter_defaults():
    """Test that inspect function has correct default values."""
    import pysnt
    import inspect as py_inspect
    
    sig = py_inspect.signature(pysnt.inspect)
    
    # Check default values
    expected_defaults = {
        'keyword': '',
        'methods': True,
        'fields': True,
        'constructors': False,
        'static_only': False,
        'case_sensitive': False,
        'max_results': 50
    }
    
    for param_name, expected_default in expected_defaults.items():
        param = sig.parameters[param_name]
        assert param.default == expected_default, f"Parameter '{param_name}' has wrong default: {param.default} != {expected_default}"


def test_inspect_helper_functions():
    """Test the helper functions used by inspect."""
    from pysnt.java_utils import _matches_keyword
    
    # Test keyword matching
    assert _matches_keyword("getLength", "length", False) == True
    assert _matches_keyword("getLength", "Length", False) == True  # case insensitive
    assert _matches_keyword("getLength", "Length", True) == True   # case sensitive - "Length" is in "getLength"
    assert _matches_keyword("getLength", "length", True) == False  # case sensitive - "length" not in "getLength"
    assert _matches_keyword("getLength", "width", False) == False
    assert _matches_keyword("getLength", "", False) == True  # empty keyword matches all


def test_inspect_module_import():
    """Test that inspect can be imported from pysnt.java_utils."""
    from pysnt.java_utils import inspect
    
    assert callable(inspect)


def test_inspect_in_all():
    """Test that inspect is included in pysnt.__all__."""
    import pysnt
    
    assert 'inspect' in pysnt.__all__


if __name__ == "__main__":
    # Run basic tests
    test_inspect_function_exists()
    test_inspect_without_jvm()
    test_inspect_function_signature()
    test_inspect_parameter_defaults()
    test_inspect_helper_functions()
    test_inspect_module_import()
    test_inspect_in_all()
    
    print("✓ All inspect function tests passed!")