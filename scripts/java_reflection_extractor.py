#!/usr/bin/env python3
"""
Java reflection script for extracting method signatures from SNT classes.

This script uses Java reflection to extract complete method signatures,
constructors, and fields from Java classes in the SNT library.
"""

import sys
import os

def main():
    """Main reflection extraction logic."""
    # Get source directory and classes dict from command line args
    if len(sys.argv) < 3:
        print("Usage: python java_reflection_extractor.py <source_dir> <classes_dict_repr>")
        sys.exit(1)
    
    source_dir = sys.argv[1]
    classes_dict_str = sys.argv[2]
    
    sys.path.insert(0, source_dir)

    try:
        import pysnt
        
        # Try to initialize SNT
        try:
            print("INIT_INFO: Initializing SNT (non-interactive mode)")
            pysnt.initialize(interactive=False)
            print("INIT_SUCCESS: SNT initialized successfully")
        except pysnt.FijiNotFoundError as e:
            print(f"INIT_ERROR: Fiji/SNT not configured properly:")
            print(str(e))
            print("\nTo fix this, run one of:")
            print("  python -m pysnt.setup_utils --auto-detect")
            print("  python -m pysnt.setup_utils --set /path/to/Fiji.app")
            sys.exit(1)  # Fatal error - environment not configured
        except Exception as e:
            print(f"INIT_ERROR: SNT initialization failed: {e}")
            # For other initialization errors, continue gracefully
            print("REFLECTION_ERROR: SNT initialization failed, continuing with basic stubs")
            sys.exit(0)
        
        classes_to_process = eval(classes_dict_str)
        
        for module_name, class_names in classes_to_process.items():
            for class_name in class_names:
                try:
                    print(f"=== CLASS {module_name}.{class_name} ===")
                    
                    # Get the class
                    if module_name and module_name != "pysnt":
                        module = __import__(module_name, fromlist=[class_name])
                        python_class = getattr(module, class_name)
                    else:
                        python_class = getattr(pysnt, class_name)
                    
                    # Get the underlying Java class for reflection
                    java_class = None
                    
                    # Try different approaches to get the Java class
                    if hasattr(python_class, '__javaclass__'):
                        java_class = python_class.__javaclass__
                    elif hasattr(python_class, 'class_'):
                        java_class = getattr(python_class, 'class_')
                    elif hasattr(python_class, '_java_object'):
                        # py4j approach
                        java_class = python_class._java_object.getClass()
                    else:
                        # Try jpype approach
                        try:
                            import jpype
                            if jpype.isJVMStarted():
                                # Construct the full Java class name
                                full_class_name = f"sc.fiji.snt.{class_name}"
                                if module_name and module_name != "pysnt":
                                    # Map module names to Java packages
                                    package_map = {
                                        "pysnt.analysis": "sc.fiji.snt.analysis",
                                        "pysnt.analysis.sholl": "sc.fiji.snt.analysis.sholl",
                                        "pysnt.analysis.graph": "sc.fiji.snt.analysis.graph",
                                        "pysnt.analysis.growth": "sc.fiji.snt.analysis.growth",
                                        "pysnt.analysis.sholl.gui": "sc.fiji.snt.analysis.sholl.gui",
                                        "pysnt.analysis.sholl.math": "sc.fiji.snt.analysis.sholl.math",
                                        "pysnt.analysis.sholl.parsers": "sc.fiji.snt.analysis.sholl.parsers"
                                    }
                                    java_package = package_map.get(module_name, "sc.fiji.snt")
                                    full_class_name = f"{java_package}.{class_name}"
                                
                                java_class_obj = jpype.JClass(full_class_name)
                                java_class = java_class_obj.class_
                        except Exception:
                            pass
                    
                    if not java_class:
                        print("REFLECTION_ERROR: Could not access Java class")
                        continue
                    
                    # Use reflection
                    methods = java_class.getMethods()
                    constructors = java_class.getConstructors()
                    fields = java_class.getFields()
                    
                    print("=== METHODS ===")
                    for method in methods:
                        method_name = str(method.getName())
                        if method_name in ['equals', 'hashCode', 'toString', 'getClass', 'notify', 'notifyAll', 'wait']:
                            continue
                        
                        param_types = [str(p.getSimpleName()) for p in method.getParameterTypes()]
                        return_type = str(method.getReturnType().getSimpleName())
                        modifiers = method.getModifiers()
                        is_static = bool(modifiers & 0x0008)
                        
                        print(f"METHOD|{method_name}|{param_types}|{return_type}|{is_static}")
                    
                    print("=== CONSTRUCTORS ===")
                    for constructor in constructors:
                        param_types = [str(p.getSimpleName()) for p in constructor.getParameterTypes()]
                        print(f"CONSTRUCTOR|{param_types}")
                    
                    print("=== FIELDS ===")
                    for field in fields:
                        field_name = str(field.getName())
                        field_type = str(field.getType().getSimpleName())
                        modifiers = field.getModifiers()
                        is_static = bool(modifiers & 0x0008)
                        is_final = bool(modifiers & 0x0010)
                        
                        print(f"FIELD|{field_name}|{field_type}|{is_static}|{is_final}")
                    
                    print("=== END CLASS ===")
                    
                except Exception as e:
                    print(f"CLASS_ERROR|{module_name}.{class_name}|{e}")

    except Exception as e:
        print(f"REFLECTION_ERROR: {e}")


if __name__ == "__main__":
    main()