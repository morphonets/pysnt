#!/usr/bin/env python3
"""
Verifies that type stubs are working correctly by checking that all module-level
functions are accessible. It does NOT execute the functions to avoid requiring
Java/Fiji setup.
"""

def test_type_stub_accessibility():
    """
    Test that all type stub declarations are accessible.
    
    This test verifies that all module-level functions are properly declared
    in the type stub files and can be imported without errors.
    """
    
    # Import pysnt - this should work even without Java/Fiji setup
    import pysnt
    
    # Test that all functions are accessible (but don't call them)
    # These should all be recognized by PyCharm with no warnings
    
    # Core functions
    assert hasattr(pysnt, 'initialize'), "initialize function not found"
    assert hasattr(pysnt, 'inspect'), "inspect function not found"
    assert hasattr(pysnt, 'get_methods'), "get_methods function not found"
    assert hasattr(pysnt, 'get_fields'), "get_fields function not found"
    assert hasattr(pysnt, 'find_members'), "find_members function not found"
    
    # Version functions
    assert hasattr(pysnt, 'version'), "version function not found"
    assert hasattr(pysnt, 'print_version'), "print_version function not found"
    assert hasattr(pysnt, 'show_version'), "show_version function not found"
    assert hasattr(pysnt, 'info'), "info function not found"
    
    # Setup utilities
    assert hasattr(pysnt, 'get_fiji_path'), "get_fiji_path function not found"
    assert hasattr(pysnt, 'set_fiji_path'), "set_fiji_path function not found"
    assert hasattr(pysnt, 'show_config_status'), "show_config_status function not found"
    assert hasattr(pysnt, 'auto_detect_and_configure'), "auto_detect_and_configure function not found"
    
    # Exception class
    assert hasattr(pysnt, 'FijiNotFoundError'), "FijiNotFoundError class not found"
    assert issubclass(pysnt.FijiNotFoundError, Exception), "FijiNotFoundError is not an Exception subclass"
    
    # Module functions
    assert hasattr(pysnt, 'get_class'), "get_class function not found"
    assert hasattr(pysnt, 'get_available_classes'), "get_available_classes function not found"
    assert hasattr(pysnt, 'list_classes'), "list_classes function not found"
    
    # Constants
    assert hasattr(pysnt, 'CURATED_ROOT_CLASSES'), "CURATED_ROOT_CLASSES constant not found"
    assert hasattr(pysnt, 'EXTENDED_ROOT_CLASSES'), "EXTENDED_ROOT_CLASSES constant not found"
    
    print("All type stub references are accessible!")


def test_type_hints():
    """
    Test that type hints work correctly.
    
    This test verifies that all functions have proper type annotations
    and can be assigned to typed variables without errors.
    """
    import pysnt
    from typing import Optional, Dict, List, Any

    # Core functions with type hints
    init_func: callable = pysnt.initialize  # (fiji_dir: Optional[str] = None, headless: bool = True, enable_ui: bool = False) -> Any
    inspect_func: callable = pysnt.inspect  # (class_or_object: Union[str, Any], keyword: str = "", ...) -> None
    get_methods_func: callable = pysnt.get_methods  # (class_or_object: Union[str, Any], ...) -> List[Dict[str, Any]]
    get_fields_func: callable = pysnt.get_fields  # (class_or_object: Union[str, Any], ...) -> List[Dict[str, Any]]
    find_members_func: callable = pysnt.find_members  # (class_or_object: Union[str, Any], ...) -> Dict[str, List[Dict[str, Any]]]
    
    # Version functions
    version_func: callable = pysnt.version  # (detailed: bool = False) -> str
    print_version_func: callable = pysnt.print_version  # (detailed: bool = False) -> None
    
    # Setup utilities
    get_fiji_path_func: callable = pysnt.get_fiji_path  # () -> Optional[str]
    set_fiji_path_func: callable = pysnt.set_fiji_path  # (path: str) -> bool
    
    print("Type hints are working correctly!")


def test_all_functions_in_all_list():
    """
    Test that all functions are properly exported in __all__.
    
    This test verifies that functions declared in type stubs are also
    properly exported in the module's __all__ list.
    """
    import pysnt
    
    # Get the __all__ list
    all_exports = getattr(pysnt, '__all__', [])
    
    # Core functions that should be in __all__
    expected_functions = [
        'initialize', 'inspect', 'get_methods', 'get_fields', 'find_members',
        'version', 'print_version', 'show_version', 'info',
        'get_fiji_path', 'set_fiji_path', 'show_config_status', 'auto_detect_and_configure',
        'get_class', 'get_available_classes', 'list_classes',
        'FijiNotFoundError'
    ]
    
    for func_name in expected_functions:
        assert func_name in all_exports, f"Function '{func_name}' not found in __all__"
        assert hasattr(pysnt, func_name), f"Function '{func_name}' not accessible as attribute"


if __name__ == "__main__":
    # Allow running as a script for manual testing
    print("🔍 Verifying PySNT Type Stubs")
    print("=" * 35)
    try:
        test_type_stub_accessibility()
        test_type_hints()
        test_all_functions_in_all_list()
        print("\nAll type stub tests passed!")
    except Exception as e:
        print(f"\nType stub test failed: {e}")
        print("\nThis likely means function not added to generate_stubs.py")
        exit(1)