#!/usr/bin/env python3
"""
Test Java reflection to see if we can extract methods from SNT classes.
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

def test_reflection():
    """Test if we can use reflection to get methods from SNT classes."""
    
    print("🔬 Testing Java reflection...")
    
    try:
        import pysnt
        print("✓ pysnt imported successfully")
        
        # Try to initialize SNT
        print("🚀 Attempting to initialize SNT...")
        try:
            pysnt.initialize()
            print("✓ SNT initialized successfully")
        except Exception as e:
            print(f"✘ SNT initialization failed: {e}")
            print("This is expected if SNT/Fiji is not properly installed")
            return False
        
        # Try to get a class and use reflection
        print("🔍 Testing reflection on Tree class...")
        try:
            tree_class = pysnt.Tree
            print(f"✓ Got Tree class: {tree_class}")
            
            # Try different approaches to get the Java class
            java_class = None
            methods = None
            
            # Approach 1: Try to get the Java class directly
            try:
                if hasattr(tree_class, '__javaclass__'):
                    java_class = tree_class.__javaclass__
                    print(f"✓ Got Java class via __javaclass__: {java_class}")
                elif hasattr(tree_class, 'class_'):
                    java_class = getattr(tree_class, 'class_')
                    print(f"✓ Got Java class via .class_: {java_class}")
                else:
                    # Try to create an instance and get its class
                    print("🔄 Trying to get class from instance...")
                    # This might fail if constructor needs arguments
                    pass
                
                if java_class:
                    methods = java_class.getMethods()
                    print(f"✓ Got {len(methods)} methods via reflection")
                
            except Exception as e:
                print(f"✘ Java class access failed: {e}")
                
            # Approach 2: Try using jpype if available
            if not methods:
                try:
                    import jpype
                    if jpype.isJVMStarted():
                        java_tree_class = jpype.JClass('sc.fiji.snt.Tree')
                        methods = java_tree_class.class_.getMethods()
                        print(f"✓ Got {len(methods)} methods via jpype")
                except Exception as e:
                    print(f"✘ jpype approach failed: {e}")
            
            # Approach 3: Try using dir() as fallback
            if not methods:
                print("🔄 Falling back to dir() inspection...")
                all_attrs = dir(tree_class)
                method_like = [attr for attr in all_attrs if not attr.startswith('_') and callable(getattr(tree_class, attr, None))]
                print(f"✓ Found {len(method_like)} callable attributes via dir()")
                methods = method_like  # Use this as fallback
            
            # Show first few methods
            if methods:
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
                
                print(f"📋 Sample methods: {method_names[:5]}")
                return True
            else:
                print("✘ No methods found")
                return False
            
        except Exception as e:
            print(f"✘ Reflection failed: {e}")
            return False
            
    except ImportError as e:
        print(f"✘ Import failed: {e}")
        return False
    except Exception as e:
        print(f"✘ Unexpected error: {e}")
        return False

def test_inspect_function():
    """Test the pysnt.inspect function as an alternative."""
    
    print("\n🔍 Testing pysnt.inspect function...")
    
    try:
        import pysnt
        
        # Try to initialize SNT
        try:
            pysnt.initialize()
            print("✓ SNT initialized for inspect test")
            
            # Use the inspect function
            print("📋 Using pysnt.inspect('Tree'):")
            pysnt.inspect('Tree', max_results=10)
            return True
            
        except Exception as e:
            print(f"✘ SNT initialization failed for inspect: {e}")
            return False
            
    except Exception as e:
        print(f"✘ Inspect test failed: {e}")
        return False

if __name__ == "__main__":
    print("PySNT Reflection Test")
    print("=" * 30)
    
    reflection_works = test_reflection()
    inspect_works = test_inspect_function()
    
    print(f"\n📊 Results:")
    print(f"  Reflection: {'✓ Working' if reflection_works else '✘ Failed'}")
    print(f"  Inspect:    {'✓ Working' if inspect_works else '✘ Failed'}")
    
    if not reflection_works:
        print(f"\n💡 Reflection failed:")
        print(f"  • SNT/Fiji might not be properly installed!?")
        print(f"  • Java environment might not be set up!?")

    if reflection_works:
        print(f"\n🎉 Reflection is working!")
