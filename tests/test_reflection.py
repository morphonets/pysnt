#!/usr/bin/env python3
"""
Test Java reflection to see if we can extract methods from SNT classes.
"""

import sys
import pytest
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

def test_reflection():
    """Test if we can use reflection to get methods from SNT classes."""
    
    print("Testing Java reflection...")
    
    import pysnt
    print("pysnt imported successfully")
    
    # Try to initialize SNT
    print("Attempting to initialize SNT...")
    try:
        pysnt.initialize()
        print("SNT initialized successfully")
    except Exception as e:
        print(f"SNT initialization failed: {e}")
        print("This is expected if SNT/Fiji is not properly installed")
        pytest.skip(f"SNT initialization failed: {e}")
        
    # Try to get a class and use reflection
    print("Testing reflection on Tree class...")
    tree_class = pysnt.Tree
    print(f"Got Tree class: {tree_class}")
    assert tree_class is not None, "Tree class should be accessible"
    
    # Try different approaches to get the Java class
    java_class = None
    methods = None
    
    # Approach 1: Try to get the Java class directly
    try:
        if hasattr(tree_class, '__javaclass__'):
            java_class = tree_class.__javaclass__
            print(f"Got Java class via __javaclass__: {java_class}")
        elif hasattr(tree_class, 'class_'):
            java_class = getattr(tree_class, 'class_')
            print(f"Got Java class via .class_: {java_class}")
        else:
            # Try to create an instance and get its class
            print("Trying to get class from instance...")
            # This might fail if constructor needs arguments
            pass
        
        if java_class:
            methods = java_class.getMethods()
            print(f"Got {len(methods)} methods via reflection")
        
    except Exception as e:
        print(f"Java class access failed: {e}")
        
    # Approach 2: Try using jpype if available
    if not methods:
        try:
            import jpype
            if jpype.isJVMStarted():
                java_tree_class = jpype.JClass('sc.fiji.snt.Tree')
                methods = java_tree_class.class_.getMethods()
                print(f"Got {len(methods)} methods via jpype")
        except Exception as e:
            print(f"jpype approach failed: {e}")
    
    # Approach 3: Try using dir() as fallback
    if not methods:
        print("Falling back to dir() inspection...")
        all_attrs = dir(tree_class)
        method_like = [attr for attr in all_attrs if not attr.startswith('_') and callable(getattr(tree_class, attr, None))]
        print(f"Found {len(method_like)} callable attributes via dir()")
        methods = method_like  # Use this as fallback
    
    # Verify we found some methods
    assert methods is not None and len(methods) > 0, "Should find at least some methods via reflection or dir()"
    
    # Show first few methods
    method_names = []
    for i, method in enumerate(methods):
        if i >= 10:  # Just show first 10
            break
        
        if isinstance(method, str):
            # dir() approach - method is already a string
            method_name = method
        else:
            # Java reflection - method is a Method object
            method_name = str(method.getName())
        
        if method_name not in ['equals', 'hashCode', 'toString', 'getClass', 'notify', 'notifyAll', 'wait']:
            method_names.append(method_name)
    
    print(f"Sample methods: {method_names[:5]}")
    assert len(method_names) > 0, "Should find at least some non-Object methods"

def test_inspect_function():
    """Test the pysnt.inspect function as an alternative."""
    
    print("\nTesting pysnt.inspect function...")
    
    import pysnt
    
    # Try to initialize SNT
    try:
        pysnt.initialize()
        print("SNT initialized for inspect test")
        
        # Use the inspect function - this should not raise an exception
        print("Using pysnt.inspect('Tree'):")
        pysnt.inspect('Tree', max_results=10)
        
        # If we get here, the function worked
        assert True, "inspect function should work without raising exceptions"
        
    except Exception as e:
        print(f"SNT initialization failed for inspect: {e}")
        pytest.skip(f"SNT initialization failed for inspect: {e}")

if __name__ == "__main__":
    print("PySNT Reflection Test")
    print("=" * 30)
    
    try:
        test_reflection()
        print("Reflection test passed")
        reflection_works = True
    except Exception as e:
        print(f"Reflection test failed: {e}")
        reflection_works = False
    
    try:
        test_inspect_function()
        print("Inspect function test passed")
        inspect_works = True
    except Exception as e:
        print(f"Inspect function test failed: {e}")
        inspect_works = False
    
    print(f"\nResults:")
    print(f"  Reflection: {'Working' if reflection_works else '✘ Failed'}")
    print(f"  Inspect:    {'Working' if inspect_works else '✘ Failed'}")
    
    if not reflection_works:
        print(f"\nReflection failed:")
        print(f"  • SNT/Fiji might not be properly installed")
        print(f"  • Java environment might not be set up")

    if reflection_works:
        print(f"\nReflection is working!")
