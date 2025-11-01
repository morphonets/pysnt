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
    assert hasattr(pysnt, "inspect")
    assert callable(pysnt.inspect)


def test_inspect_without_jvm():
    """Test inspect function behavior when JVM is not started."""
    import pysnt

    # This test just checks that the function can be called
    # The actual JVM check is tested in integration tests
    try:
        # This should either work or print an error message
        # We're just testing that it doesn't crash
        with patch("builtins.print"):
            pysnt.inspect("TreeStatistics")
    except Exception as e:
        # If there's an exception, it should be related to JVM or imports
        assert any(
            keyword in str(e).lower() for keyword in ["jvm", "scyjava", "import"]
        )


def test_inspect_function_signature():
    """Test that inspect function has the expected signature."""
    import pysnt
    import inspect as py_inspect

    # Get function signature
    sig = py_inspect.signature(pysnt.inspect)

    # Check expected parameters exist
    expected_params = [
        "class_or_object",
        "keyword",
        "methods",
        "fields",
        "constructors",
        "static_only",
        "case_sensitive",
        "max_results",
    ]

    actual_params = list(sig.parameters.keys())

    for param in expected_params:
        assert (
            param in actual_params
        ), f"Parameter '{param}' missing from inspect function"


def test_inspect_parameter_defaults():
    """Test that inspect function has correct default values."""
    import pysnt
    import inspect as py_inspect

    sig = py_inspect.signature(pysnt.inspect)

    # Check default values
    expected_defaults = {
        "keyword": "",
        "methods": True,
        "fields": True,
        "constructors": False,
        "static_only": False,
        "case_sensitive": False,
        "max_results": 50,
    }

    for param_name, expected_default in expected_defaults.items():
        param = sig.parameters[param_name]
        assert (
            param.default == expected_default
        ), f"Parameter '{param_name}' has wrong default: {param.default} != {expected_default}"


def test_inspect_helper_functions():
    """Test the helper functions used by inspect."""
    from pysnt.java_utils import _matches_keyword

    # Test keyword matching
    assert _matches_keyword("getLength", "length", False) == True
    assert _matches_keyword("getLength", "Length", False) == True  # case insensitive
    assert (
        _matches_keyword("getLength", "Length", True) == True
    )  # case sensitive - "Length" is in "getLength"
    assert (
        _matches_keyword("getLength", "length", True) == False
    )  # case sensitive - "length" not in "getLength"
    assert _matches_keyword("getLength", "width", False) == False
    assert _matches_keyword("getLength", "", False) == True  # empty keyword matches all


def test_inspect_module_import():
    """Test that inspect can be imported from pysnt.java_utils."""
    from pysnt.java_utils import inspect

    assert callable(inspect)


def test_inspect_in_all():
    """Test that inspect is included in pysnt.__all__."""
    import pysnt

    assert "inspect" in pysnt.__all__


def test_inspect_detailed_java_reflection():
    """
    Detailed test of the refactored inspect functionality using real Java classes.
    
    1. Tests actual Java classes (String, ArrayList, HashMap)
    2. Tests keyword filtering with various patterns
    3. Tests static vs instance member filtering
    4. Tests scyjava-based reflection functions
    5. Tests edge cases and error handling
    """
    try:
        import scyjava
        from pysnt.java_utils import (
            inspect, 
            get_methods, 
            get_fields, 
            is_instance_of, 
            reflect_java_object,
            find_members
        )
        from io import StringIO
        import sys
        
        # Skip test if JVM is not available
        if not scyjava.jvm_started():
            try:
                scyjava.start_jvm()
            except:
                print("  Skipping comprehensive test - JVM not available")
                return
        
        # Test 1: Basic Java class reflection with String
        print(" Testing comprehensive Java reflection...")
        
        String = scyjava.jimport('java.lang.String')
        ArrayList = scyjava.jimport('java.util.ArrayList')
        HashMap = scyjava.jimport('java.util.HashMap')
        
        # Test 2: Compare jreflect vs traditional methods
        print(" Comparing reflection methods...")
        
        # Get methods using our refactored function
        string_methods = get_methods(String)
        assert len(string_methods) > 50, f"Expected >50 methods, got {len(string_methods)}"
        
        # Verify method structure
        for method in string_methods[:5]:  # Check first 5 methods
            assert 'name' in method, "Method should have 'name' field"
            assert 'params' in method, "Method should have 'params' field"
            assert 'return_type' in method, "Method should have 'return_type' field"
            assert 'is_static' in method, "Method should have 'is_static' field"
            assert 'signature' in method, "Method should have 'signature' field"
            assert isinstance(method['params'], list), "params should be a list"
            assert isinstance(method['is_static'], bool), "is_static should be boolean"
        
        # Test 3: Keyword filtering with various patterns
        print(" Testing keyword filtering...")
        
        # Test case-insensitive filtering
        length_methods = find_members(String, "length", include_fields=False, include_inner_classes=False)
        assert len(length_methods['methods']) > 0, "Should find methods containing 'length'"
        
        # Verify all found methods contain the keyword
        for method in length_methods['methods']:
            method_name = str(method['name'])
            assert 'length' in method_name.lower(), f"Method {method_name} should contain 'length'"
        
        # Test case-sensitive filtering
        Length_methods = find_members(String, "Length", include_fields=False, include_inner_classes=False, case_sensitive=True)
        # Should find fewer or equal methods than case-insensitive
        assert len(Length_methods['methods']) <= len(length_methods['methods'])
        
        # Test 4: Static vs instance member filtering
        print(" Testing static filtering...")
        
        # Get all methods vs static-only methods
        all_string_methods = get_methods(String, static_only=False)
        static_string_methods = get_methods(String, static_only=True)
        
        assert len(static_string_methods) < len(all_string_methods), "Should have fewer static methods than total methods"
        
        # Verify all static methods are actually static
        for method in static_string_methods:
            assert method['is_static'] == True, f"Method {str(method['name'])} should be static"
        
        # Test 5: Field inspection
        print(" Testing field inspection...")
        
        string_fields = get_fields(String)
        # String should have at least CASE_INSENSITIVE_ORDER field
        assert len(string_fields) >= 1, "String should have at least 1 public field"
        
        # Test with a class that has more fields (HashMap)
        hashmap_fields = get_fields(HashMap)
        for field in hashmap_fields:
            assert 'name' in field, "Field should have 'name'"
            assert 'type' in field, "Field should have 'type'"
            assert 'is_static' in field, "Field should have 'is_static'"
            assert 'is_final' in field, "Field should have 'is_final'"
        
        # Test 6: Instance type checking
        print(" Testing instance checking...")
        
        # Create instances
        string_instance = String("test")
        arraylist_instance = ArrayList()
        
        # Test is_instance_of function
        assert is_instance_of(string_instance, "java.lang.String") == True
        assert is_instance_of(string_instance, "java.lang.Object") == True
        assert is_instance_of(string_instance, "java.util.List") == False
        
        assert is_instance_of(arraylist_instance, "java.util.ArrayList") == True
        assert is_instance_of(arraylist_instance, "java.util.List") == True
        assert is_instance_of(arraylist_instance, "java.lang.String") == False
        
        # Test 7: Direct jreflect wrapper
        print(" Testing direct jreflect wrapper...")
        
        methods_info = reflect_java_object(String, "methods")
        fields_info = reflect_java_object(String, "fields")
        constructors_info = reflect_java_object(String, "constructors")
        all_info = reflect_java_object(String, "all")
        
        assert len(methods_info) > 50, "Should find many methods"
        assert len(fields_info) >= 1, "Should find at least one field"
        assert len(constructors_info) > 5, "Should find multiple constructors"
        assert len(all_info) > len(methods_info), "All info should include more than just methods"
        
        # Test 8: Inspect function output capture
        print(" Testing inspect output...")
        
        # Capture output from inspect function
        old_stdout = sys.stdout
        sys.stdout = captured_output = StringIO()
        
        try:
            # Test inspect with various parameters
            inspect(String, keyword="char", methods=True, fields=False, max_results=5)
            output = captured_output.getvalue()
            
            # Verify output contains expected elements
            assert "Inspecting:" in output, "Output should contain inspection header"
            assert "Methods" in output, "Output should show methods section"
            assert "char" in output.lower(), "Output should contain filtered methods with 'char'"
            
        finally:
            sys.stdout = old_stdout
        
        # Test 9: Error handling and edge cases
        print("  Testing error handling...")
        
        # Test with non-existent class
        empty_methods = get_methods("NonExistentClass")
        assert len(empty_methods) == 0, "Non-existent class should return empty list"
        
        # Test with empty keyword (should return all members)
        all_members = find_members(String, "", include_inner_classes=False)
        assert len(all_members['methods']) > 50, "Empty keyword should return all methods"
        
        # Test 10: Performance and consistency check
        print(" Testing performance and consistency...")
        
        # Get the same data multiple ways and verify consistency
        methods1 = get_methods(String)
        methods2 = reflect_java_object(String, "methods")
        
        # Should have same number of methods (allowing for slight differences in filtering)
        assert abs(len(methods1) - len(methods2)) <= 10, f"Method counts should be similar: {len(methods1)} vs {len(methods2)}"
        
        # Verify some common methods exist in both
        method1_names = {str(m['name']) for m in methods1}
        method2_names = {str(m.get('name', '')) for m in methods2}
        
        common_methods = ['charAt', 'length', 'substring', 'toString']
        for method_name in common_methods:
            assert method_name in method1_names, f"Method {method_name} should be in get_methods result"
            assert method_name in method2_names, f"Method {method_name} should be in jreflect result"
        
        print(" All comprehensive tests passed!")
        
    except ImportError:
        print("  Skipping comprehensive test - scyjava not available")
    except Exception as e:
        print(f" Comprehensive test failed: {e}")
        raise


if __name__ == "__main__":
    # Run basic tests
    test_inspect_function_exists()
    test_inspect_without_jvm()
    test_inspect_function_signature()
    test_inspect_parameter_defaults()
    test_inspect_helper_functions()
    test_inspect_module_import()
    test_inspect_in_all()
    test_inspect_detailed_java_reflection()

    print("✓ All inspect function tests passed!")
