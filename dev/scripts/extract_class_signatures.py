#!/usr/bin/env python3
"""
Class Signature Extractor for PySNT

This script extracts complete method and field signatures from Java classes
using reflection and stores them in structured text files for later stub generation.

Usage:
    python scripts/extract_class_signatures.py --all-classes
    python scripts/extract_class_signatures.py --class SNTService
    python scripts/extract_class_signatures.py --class SNTService Tree Path
"""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional, Union

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

class JavaSignatureExtractor:
    """Extracts Java class signatures using reflection."""
    
    def __init__(self, stubs_dir: Path, verbose: bool = False):
        self.stubs_dir = Path(stubs_dir)
        self.verbose = verbose
        self.stubs_dir.mkdir(parents=True, exist_ok=True)
        
        # Java type to Python type mapping
        self.type_mapping = {
            # Primitive types
            'void': 'None',
            'boolean': 'bool',
            'byte': 'int', 'short': 'int', 'int': 'int', 'long': 'int',
            'float': 'float', 'double': 'float',
            'char': 'str', 'String': 'str',
            
            # Generic Java types
            'Object': 'Any',
            'Class': 'type',
            'Number': 'Union[int, float]',
            
            # Collections
            'List': 'List[Any]', 'ArrayList': 'List[Any]', 'LinkedList': 'List[Any]',
            'Collection': 'List[Any]', 'Iterable': 'List[Any]',
            'Map': 'Dict[str, Any]', 'HashMap': 'Dict[str, Any]', 'TreeMap': 'Dict[str, Any]',
            'Set': 'Set[Any]', 'HashSet': 'Set[Any]', 'TreeSet': 'Set[Any]',
            'Queue': 'List[Any]', 'Deque': 'List[Any]',
            
            # Common Java types
            'File': 'str',  # File paths as strings in Python
            'URL': 'str',   # URLs as strings
            'URI': 'str',   # URIs as strings
            'BigInteger': 'int',
            'BigDecimal': 'float',
            'Date': 'Any',  # Could be datetime, but Any is safer
            'Calendar': 'Any',
            
            # ImageJ types
            'ImagePlus': 'Any',
            'ImageProcessor': 'Any',
            'ImageStack': 'Any',
            'Roi': 'Any',
            'Calibration': 'Any',
            'ResultsTable': 'Any',
            
            # SNT specific types (use actual class names for better IDE support)
            'Tree': 'Tree',
            'Path': 'Path', 
            'SNTService': 'SNTService',
            'SNTUtils': 'SNTUtils',
            'SNTTable': 'SNTTable',
            'SNTChart': 'SNTChart',
            'TreeStatistics': 'TreeStatistics',
            'MultiTreeStatistics': 'MultiTreeStatistics',
            'DirectedWeightedGraph': 'DirectedWeightedGraph',
            'AnnotationGraph': 'AnnotationGraph',
            'ConvexHull2D': 'ConvexHull2D',
            'ConvexHull3D': 'ConvexHull3D',
            'PointInImage': 'PointInImage',
            'SNTPoint': 'SNTPoint',
            'SWCPoint': 'SWCPoint',
            'BoundingBox': 'BoundingBox',
            
            # Viewer types
            'Viewer2D': 'Viewer2D',
            'Viewer3D': 'Viewer3D',
            'MultiViewer2D': 'MultiViewer2D',
            'MultiViewer3D': 'MultiViewer3D',
            
            # Tracing types
            'SearchNode': 'SearchNode',
            'BiSearchNode': 'BiSearchNode',
            'FillerThread': 'FillerThread',
            'TracerThread': 'TracerThread',
            
            # Analysis types
            'Profile': 'Profile',
            'ProfileEntry': 'ProfileEntry',
            'ShollStats': 'ShollStats',
            'GrowthAnalyzer': 'GrowthAnalyzer',
        }
    
    def map_java_type(self, java_type: str) -> str:
        """Map Java type to Python type hint."""
        # Handle array types
        if java_type.endswith('[]'):
            base_type = java_type[:-2]
            mapped_base = self.type_mapping.get(base_type, 'Any')
            return f'List[{mapped_base}]'
        
        # Handle generic types (basic)
        if '<' in java_type:
            base_type = java_type.split('<')[0]
            return self.type_mapping.get(base_type, 'Any')
        
        return self.type_mapping.get(java_type, 'Any')
    
    def find_class_in_modules(self, class_name: str) -> Optional[tuple]:
        """Find a class in pysnt modules and return (class_obj, module_name, package_name)."""
        import pysnt
        
        # Try main pysnt module first
        if hasattr(pysnt, class_name):
            return (getattr(pysnt, class_name), 'pysnt', 'sc.fiji.snt')
        
        # Try submodules - need to import them explicitly
        submodules = [
            ('analysis', 'sc.fiji.snt.analysis'),
            ('annotation', 'sc.fiji.snt.annotation'),
            ('viewer', 'sc.fiji.snt.viewer'),
            ('io', 'sc.fiji.snt.io'),
            ('tracing', 'sc.fiji.snt.tracing'),
            ('util', 'sc.fiji.snt.util')
        ]
        
        for module_name, java_package in submodules:
            try:
                # Import the submodule explicitly
                import importlib
                full_module_name = f'pysnt.{module_name}'
                module = importlib.import_module(full_module_name)
                
                if hasattr(module, class_name):
                    return (getattr(module, class_name), full_module_name, java_package)
            except (AttributeError, ImportError) as e:
                continue
        
        return None

    def extract_class_info(self, class_name: str) -> Optional[Dict[str, Any]]:
        """Extract complete information for a Java class."""
        try:
            import pysnt
            
            # Initialize PySNT if not already done
            try:
                from pysnt.core import is_initialized
                if not is_initialized():
                    if self.verbose:
                        print(f"Initializing PySNT...")
                    pysnt.initialize()
            except Exception as e:
                if self.verbose:
                    print(f"Could not check initialization status: {e}")
                # Try to initialize anyway
                try:
                    pysnt.initialize()
                except Exception as init_e:
                    if self.verbose:
                        print(f"Initialization failed: {init_e}")
                    # Continue anyway, might work
            
            # Find the class in the appropriate module
            class_info = self.find_class_in_modules(class_name)
            if not class_info:
                print(f"❌ Could not find class {class_name} in any pysnt module")
                return None
            
            java_class, module_name, java_package = class_info
            
            if self.verbose:
                print(f"🔍 Extracting signatures for {class_name} from {module_name}...")
            
            # Check if this is a dynamic placeholder class and get the real Java class
            # Do this BEFORE trying to instantiate to avoid getting wrappers
            is_dynamic_placeholder = (
                type(java_class).__name__ == 'DynamicPlaceholderMeta' or
                (hasattr(java_class, '__mro__') and any('DynamicPlaceholder' in str(base) for base in java_class.__mro__))
            )
            
            if is_dynamic_placeholder:
                if self.verbose:
                    print(f"📋 Detected dynamic placeholder, using get_class() to get real Java class")
                try:
                    # Get the module and use its get_class function
                    if module_name == 'pysnt':
                        real_java_class = pysnt.get_class(class_name)
                    else:
                        # For submodules like pysnt.annotation
                        import importlib
                        module = importlib.import_module(module_name)
                        real_java_class = module.get_class(class_name)
                    
                    if self.verbose:
                        print(f"📋 Got real Java class: {type(real_java_class)}")
                    java_class = real_java_class
                    
                    # For classes that return wrappers when instantiated (like Viewer3D),
                    # we should use the class directly for inspection
                    # Set java_instance to the class itself
                    java_instance = java_class
                    
                    if self.verbose:
                        print(f"📋 Using Java class directly for inspection: {type(java_instance)}")
                    
                except Exception as e:
                    if self.verbose:
                        print(f"⚠️  Could not get real Java class via get_class(): {e}")
                    # Continue with the placeholder, might still work
                    java_instance = None
            else:
                java_instance = None
            
            # Create an instance to get the actual Java object for inspection
            # (unless already set above for dynamic placeholders)
            if java_instance is None:
                try:
                    if class_name == 'SNTService':
                        # SNTService can be instantiated directly
                        java_instance = java_class()
                    elif class_name in ['Tree', 'Path']:
                        # These might need special handling or demo instances
                        if class_name == 'Tree':
                            # Try to get a demo tree
                            service = pysnt.SNTService()
                            java_instance = service.demoTree()
                        else:
                            # For Path, try to create an empty one or get from tree
                            service = pysnt.SNTService()
                            tree = service.demoTree()
                            paths = tree.list() if hasattr(tree, 'list') else []
                            if paths:
                                java_instance = paths[0]
                            else:
                                # Fallback to class inspection
                                java_instance = java_class
                    elif class_name in ['SNTChart', 'SNTTable']:
                        # These need data to be instantiated, try to get from TreeStatistics
                        try:
                            service = pysnt.SNTService()
                            tree = service.demoTree()
                            stats = pysnt.analysis.TreeStatistics(tree)
                            if class_name == 'SNTChart':
                                java_instance = stats.getHistogram("Branch length")
                            else:  # SNTTable
                                java_instance = stats.getSummaryTable()
                        except Exception as chart_e:
                            if self.verbose:
                                print(f"⚠️  Could not create {class_name} from stats: {chart_e}")
                            java_instance = java_class
                    else:
                        # Try direct instantiation
                        try:
                            java_instance = java_class()
                        except Exception as inst_e:
                            if self.verbose:
                                print(f"⚠️  Could not instantiate {class_name}: {inst_e}")
                            # For utility classes with static methods, try to get the actual Java class
                            try:
                                import scyjava as sj
                                full_class_name = f'{java_package}.{class_name}'
                                java_instance = sj.jimport(full_class_name)
                                if self.verbose:
                                    print(f"📋 Got Java class directly: {java_instance}")
                            except Exception as java_e:
                                if self.verbose:
                                    print(f"⚠️  Could not get Java class directly: {java_e}")
                                java_instance = java_class
                    
                        if self.verbose:
                            print(f"📋 Created instance: {type(java_instance)}")
                        
                except Exception as e:
                    if self.verbose:
                        print(f"⚠️  Could not create instance, using class: {e}")
                    java_instance = java_class
            
            # Use pysnt.inspect to get method information
            # Capture the printed output since inspect() returns None
            import io
            from contextlib import redirect_stdout
            
            captured_output = io.StringIO()
            with redirect_stdout(captured_output):
                pysnt.inspect(java_instance, methods=True, fields=True, constructors=True)
            
            methods_info = captured_output.getvalue().split('\n')
            
            if not methods_info or len(methods_info) < 5:
                print(f"❌ Failed to inspect {class_name} - no reflection data available")
                return None
            
            # Parse the inspection results
            class_info_dict = {
                'class_name': class_name,
                'package': java_package,
                'extracted_at': datetime.now().isoformat(),
                'extractor_version': '1.0.0',
                'methods': [],
                'fields': [],
                'constructors': []
            }
            
            # Process methods and constructors from inspection output
            current_method = None
            method_groups = {}  # Group overloaded methods
            constructor_list = []  # Store constructors
            in_constructors_section = False
            
            for line in methods_info:
                line = line.strip()
                if not line or line.startswith('='):
                    continue
                
                # Track sections
                if 'Constructors' in line:
                    in_constructors_section = True
                    continue
                elif 'Methods' in line or 'Fields' in line:
                    in_constructors_section = False
                    continue
                
                # Parse constructor lines (format: "  1. ClassName(params)")
                if in_constructors_section and line and line[0].isdigit():
                    # Extract constructor signature
                    if '(' in line and ')' in line:
                        # Find the constructor signature part
                        constructor_part = line[line.find('.')+1:].strip()  # Remove "1. " prefix
                        if '(' in constructor_part:
                            # Extract parameters from constructor
                            params_start = constructor_part.find('(')
                            params_end = constructor_part.rfind(')')
                            params_str = constructor_part[params_start+1:params_end]
                            
                            # Parse parameters
                            params = []
                            if params_str.strip():
                                # Handle special case where params end with semicolon
                                params_str = params_str.rstrip(';')
                                param_parts = params_str.split(',')
                                for i, param in enumerate(param_parts):
                                    param = param.strip()
                                    if param:
                                        param_name = f"arg{i}"
                                        param_type = self.map_java_type(param)
                                        params.append({
                                            'name': param_name,
                                            'type': param_type,
                                            'java_type': param
                                        })
                            
                            constructor_list.append({
                                'signature': f"{class_name}({', '.join([p['java_type'] for p in params])})",
                                'params': params,
                                'return_type': 'None',
                                'java_return_type': 'void'
                            })
                    continue
                
                if line.startswith('•'):
                    # Method signature line
                    method_sig = line[1:].strip()  # Remove bullet point
                    
                    # Parse method signature: "methodName(params) -> returnType"
                    if ' -> ' in method_sig:
                        method_part, return_type = method_sig.split(' -> ', 1)
                        
                        # Extract method name and parameters
                        if '(' in method_part:
                            method_name = method_part.split('(')[0]
                            params_str = method_part[method_part.find('(')+1:method_part.rfind(')')]
                            
                            # Parse parameters
                            params = []
                            if params_str.strip():
                                param_parts = params_str.split(',')
                                for i, param in enumerate(param_parts):
                                    param = param.strip()
                                    if param:
                                        # For now, use generic parameter names
                                        param_name = f"arg{i}" if param != "boolean" else f"arg{i}"
                                        param_type = self.map_java_type(param)
                                        params.append({
                                            'name': param_name,
                                            'type': param_type,
                                            'java_type': param
                                        })
                            
                            # Group overloaded methods
                            if method_name not in method_groups:
                                method_groups[method_name] = []
                            
                            method_groups[method_name].append({
                                'signature': method_sig,
                                'params': params,
                                'return_type': self.map_java_type(return_type),
                                'java_return_type': return_type
                            })
            
            # Convert method groups to final format
            for method_name, overloads in method_groups.items():
                class_info_dict['methods'].append({
                    'name': method_name,
                    'overloads': overloads,
                    'documentation': f"Java method: {method_name}"
                })
            
            # Add constructors to class info
            if constructor_list:
                class_info_dict['constructors'] = [{
                    'name': '__init__',
                    'overloads': constructor_list,
                    'documentation': f"Java constructors for {class_name}"
                }]
            
            if self.verbose:
                print(f"✅ Extracted {len(class_info_dict['methods'])} methods and {len(constructor_list)} constructors for {class_name}")
            
            return class_info_dict
            
        except Exception as e:
            print(f"❌ Failed to extract {class_name}: {e}")
            if self.verbose:
                import traceback
                traceback.print_exc()
            return None
    
    def save_class_info(self, class_info: Dict[str, Any]) -> bool:
        """Save class information to a structured file."""
        try:
            class_name = class_info['class_name']
            output_file = self.stubs_dir / f"{class_name}.json"
            
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(class_info, f, indent=2, ensure_ascii=False)
            
            if self.verbose:
                print(f"💾 Saved signatures to {output_file}")
            
            return True
            
        except Exception as e:
            print(f"❌ Failed to save {class_info['class_name']}: {e}")
            return False
    
    def extract_and_save(self, class_name: str) -> bool:
        """Extract and save signatures for a single class."""
        class_info = self.extract_class_info(class_name)
        if class_info:
            return self.save_class_info(class_info)
        return False
    
    def get_curated_classes(self) -> List[str]:
        """Get list of curated classes from all pysnt modules by parsing __init__.py files."""
        all_classes = []
        
        try:
            # Get the source directory
            src_dir = Path(__file__).parent.parent / "src" / "pysnt"
            
            if self.verbose:
                print(f"🔍 Scanning {src_dir} for CURATED_CLASSES...")
            
            # Find all __init__.py files in the pysnt package
            init_files = list(src_dir.rglob("__init__.py"))
            
            for init_file in init_files:
                # Skip __pycache__ and other non-source directories
                if "__pycache__" in str(init_file):
                    continue
                
                try:
                    with open(init_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Parse the file to extract CURATED_CLASSES
                    import ast
                    tree = ast.parse(content)
                    
                    for node in ast.walk(tree):
                        if isinstance(node, ast.Assign):
                            for target in node.targets:
                                if isinstance(target, ast.Name):
                                    if target.id in ["CURATED_CLASSES", "CURATED_ROOT_CLASSES"] and isinstance(node.value, ast.List):
                                        # Extract string values from the list
                                        classes = []
                                        for item in node.value.elts:
                                            if isinstance(item, ast.Constant) and isinstance(item.value, str):
                                                classes.append(item.value)
                                            elif isinstance(item, ast.Str):  # Python < 3.8 compatibility
                                                classes.append(item.s)
                                        
                                        all_classes.extend(classes)
                                        
                                        if self.verbose:
                                            relative_path = init_file.relative_to(src_dir)
                                            print(f"    📋 Found {len(classes)} classes in {relative_path}: {classes}")
                
                except Exception as e:
                    if self.verbose:
                        print(f"    ⚠️  Failed to parse {init_file}: {e}")
                    continue
            
            # Remove duplicates and sort
            all_classes = sorted(list(set(all_classes)))
            
            if self.verbose:
                print(f"📋 Total unique curated classes found: {len(all_classes)}")
                print(f"    Classes: {all_classes}")
            
            return all_classes
                
        except Exception as e:
            print(f"❌ Failed to scan for curated classes: {e}")
            if self.verbose:
                import traceback
                traceback.print_exc()
            
            # Fallback to known core classes
            fallback_classes = ['SNTService', 'Tree', 'Path', 'SNTUtils']
            if self.verbose:
                print(f"🔄 Using fallback classes: {fallback_classes}")
            return fallback_classes


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Extract Java class signatures for PySNT stub generation"
    )
    parser.add_argument(
        "--class", 
        dest="classes",
        nargs="*",
        help="Specific class names to extract (e.g., SNTService Tree)"
    )
    parser.add_argument(
        "--all-classes",
        action="store_true",
        help="Extract all curated classes"
    )
    parser.add_argument(
        "--stubs-dir",
        default="dev/scripts/STUBS",
        help="Directory to store signature files (default: dev/scripts/STUBS)"
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Verbose output"
    )
    
    args = parser.parse_args()
    
    if not args.classes and not args.all_classes:
        parser.error("Must specify either --class <names> or --all-classes")
    
    # Create extractor
    extractor = JavaSignatureExtractor(args.stubs_dir, args.verbose)
    
    # Determine classes to extract
    if args.all_classes:
        classes_to_extract = extractor.get_curated_classes()
    else:
        classes_to_extract = args.classes
    
    print(f"🚀 Extracting signatures for {len(classes_to_extract)} classes...")
    
    # Extract each class
    success_count = 0
    for class_name in classes_to_extract:
        print(f"\n📦 Processing {class_name}...")
        if extractor.extract_and_save(class_name):
            success_count += 1
        else:
            print(f"❌ Failed to process {class_name}")
    
    print(f"\n📊 Extraction Summary:")
    print(f"✅ Successfully extracted: {success_count}/{len(classes_to_extract)} classes")
    print(f"💾 Signatures saved to: {extractor.stubs_dir}")
    
    if success_count > 0:
        print(f"\n💡 Next steps:")
        print(f"1. Review generated files in {extractor.stubs_dir}")
        print(f"2. Edit files manually if needed to improve signatures")
        print(f"3. Run stub generator to create .pyi files from cached data")
    
    return 0 if success_count == len(classes_to_extract) else 1


if __name__ == "__main__":
    sys.exit(main())