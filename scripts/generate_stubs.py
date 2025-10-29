#!/usr/bin/env python3
"""
stub generator for PySNT.

Combines several stub generation approaches:
1. Java reflection (most complete) - extracts actual method signatures
2. Basic stubs (fallback) - generic __getattr__ approach
2. Python AST stubs - for Python code
"""

import argparse
import ast
import logging
import subprocess
import sys
from pathlib import Path
from typing import Dict, List

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))


class ComprehensiveStubGenerator:
    """Unified stub generator with multiple fallback strategies."""

    def __init__(self, source_dir: Path, verbose: bool = False):
        self.source_dir = Path(source_dir)
        self.verbose = verbose
        self._classes_with_converters = None  # Cache for converter detection
        self.java_type_map = {
            'void': 'None',
            'boolean': 'bool',
            'byte': 'int', 'short': 'int', 'int': 'int', 'long': 'int',
            'float': 'float', 'double': 'float',
            'char': 'str', 'String': 'str',
            'Object': 'Any',
            'List': 'List[Any]', 'ArrayList': 'List[Any]', 'Collection': 'List[Any]',
            'Map': 'Dict[str, Any]', 'HashMap': 'Dict[str, Any]',
            'Set': 'Set[Any]', 'HashSet': 'Set[Any]'
        }

        # Configuration for Java classes
        self.java_classes_config = {
            'pysnt': {
                'classes': ['Fill', 'Path', 'PathAndFillManager', 'PathFitter', 'PathManagerUI',
                            'SNT', 'SNTService', 'SNTUI', 'SNTUtils', 'TracerCanvas', 'Tree', 'TreeProperties'],
                'package': 'sc.fiji.snt'
            },
            'pysnt.analysis': {
                'classes': ['ConvexHull2D', 'ConvexHull3D', 'TreeStatistics',
                            'MultiTreeStatistics', 'SNTChart', 'SNTTable'],
                'package': 'sc.fiji.snt.analysis'
            },
            'pysnt.analysis.graph': {
                'classes': ['DirectedWeightedGraph', 'DirectedWeightedSubgraph',
                            'GraphColorMapper', 'GraphUtils'],
                'package': 'sc.fiji.snt.analysis.graph'
            },
            'pysnt.analysis.growth': {
                'classes': ['GrowthAnalyzer', 'GrowthChart', 'GrowthStatistics', 'GrowthUtils'],
                'package': 'sc.fiji.snt.analysis.growth'
            },
            'pysnt.analysis.sholl': {
                'classes': ['ShollAnalyzer', 'ShollChart', 'ShollProfile', 'ShollUtils'],
                'package': 'sc.fiji.snt.analysis.sholl'
            },
            'pysnt.analysis.sholl.gui': {
                'classes': ['ShollPlot', 'ShollTable', 'ShollOverlay', 'ShollWidget'],
                'package': 'sc.fiji.snt.analysis.sholl.gui'
            },
            'pysnt.analysis.sholl.math': {
                'classes': ['LinearProfileStats', 'NormalizedProfileStats',
                            'ProfileStats', 'ShollStats'],
                'package': 'sc.fiji.snt.analysis.sholl.math'
            },
            'pysnt.analysis.sholl.parsers': {
                'classes': ['ImageParser', 'TreeParser', 'ImageParser2D', 'ImageParser3D'],
                'package': 'sc.fiji.snt.analysis.sholl.parsers'
            }
        }

    def java_type_to_python(self, java_type: str) -> str:
        """Convert Java type to Python type hint."""
        if not java_type:
            return 'Any'

        # Handle arrays
        if java_type.endswith('[]'):
            base_type = java_type[:-2]
            return f'List[{self.java_type_to_python(base_type)}]'

        return self.java_type_map.get(java_type, 'Any')

    def get_classes_with_converters(self) -> Dict[str, str]:
        """
        Get classes that have SNT converters.
        
        Returns a mapping of class names to their converter types.
        """
        # Use cached result if available
        if self._classes_with_converters is not None:
            return self._classes_with_converters
            
        classes_with_converters = {}
        
        try:
            # Import the converter system
            from pysnt.converters import SNT_CONVERTERS
            
            # Map converter names to class names
            for converter in SNT_CONVERTERS:
                converter_name = converter.name
                
                # Parse converter names to extract class names
                if '_to_' in converter_name:
                    type_part = converter_name.split('_to_')[0]
                    # Handle SNTChart_to_Matplotlib -> SNTChart
                    if type_part == 'SNTChart':
                        classes_with_converters['SNTChart'] = 'chart'
                    # Handle SNTTable_to_xarray -> SNTTable
                    elif type_part == 'SNTTable':
                        classes_with_converters['SNTTable'] = 'table'
                    # Generic handling for future converters
                    elif type_part.startswith('SNT'):
                        classes_with_converters[type_part] = type_part.lower().replace('snt', '')
                
                # Handle other naming patterns for future converters
                elif 'Chart' in converter_name and 'SNT' in converter_name:
                    classes_with_converters['SNTChart'] = 'chart'
                elif 'Table' in converter_name and 'SNT' in converter_name:
                    classes_with_converters['SNTTable'] = 'table'
            
            if self.verbose and classes_with_converters:
                print(f"    📋 Found {len(classes_with_converters)} classes with converters: {list(classes_with_converters.keys())}")
                
        except ImportError as e:
            if self.verbose:
                print(f"    ⚠️  Could not import converter system: {e}")
        except Exception as e:
            if self.verbose:
                print(f"    ⚠️  Error detecting converters: {e}")
        
        # Cache the result
        self._classes_with_converters = classes_with_converters
        return classes_with_converters

    def extract_all_methods_via_reflection(self, classes_by_module: Dict[str, List[str]]) -> Dict[str, Dict]:
        """Extract methods from all Java classes using reflection in a single subprocess call."""

        if self.verbose:
            print(f"    🔬 Attempting Java reflection for all classes...")

        # Use the external reflection script
        classes_dict_str = repr(classes_by_module)
        reflection_script_path = Path(__file__).parent / "java_reflection_extractor.py"
        
        if not reflection_script_path.exists():
            if self.verbose:
                print(f"      ❌ Reflection script not found: {reflection_script_path}")
            return {}

        try:
            result = subprocess.run(
                [sys.executable, str(reflection_script_path), str(self.source_dir), classes_dict_str],
                capture_output=True,
                text=True,
                timeout=120  # Longer timeout for all classes
            )

            # Check for FijiNotFoundError - this should be fatal
            if "INIT_ERROR: Fiji/SNT not configured properly:" in result.stdout:
                print("\n❌ FATAL ERROR: Fiji/SNT environment not properly configured!")
                print("The reflection script detected that Fiji/SNT is not set up correctly.")
                print("\nTo fix this, run one of:")
                print("  python -m pysnt.setup_utils --auto-detect")
                print("  python -m pysnt.setup_utils --set /path/to/Fiji.app")
                print("\nStub generation cannot continue without proper Fiji/SNT setup.")
                sys.exit(1)

            if result.returncode != 0 or "REFLECTION_ERROR" in result.stdout:
                if self.verbose:
                    print(f"      ❌ Reflection failed: {result.stderr}")
                return {}

            return self._parse_all_reflection_output(result.stdout)

        except Exception as e:
            if self.verbose:
                print(f"      ❌ Reflection error: {e}")
            return {}

    def _parse_all_reflection_output(self, output: str) -> Dict[str, Dict]:
        """Parse reflection output for all classes."""
        all_data = {}
        current_class = None
        current_data = None

        for line in output.strip().split('\n'):
            if line.startswith('=== CLASS '):
                class_key = line.replace('=== CLASS ', '').replace(' ===', '')
                current_class = class_key
                current_data = {'methods': [], 'constructors': [], 'fields': []}
                all_data[current_class] = current_data
            elif line.startswith('=== END CLASS ==='):
                current_class = None
                current_data = None
            elif current_data is not None:
                if line.startswith('METHOD|'):
                    parts = line.split('|')
                    if len(parts) >= 5:
                        current_data['methods'].append({
                            'name': parts[1],
                            'params': eval(parts[2]),
                            'return_type': parts[3],
                            'is_static': parts[4] == 'True'
                        })
                elif line.startswith('CONSTRUCTOR|'):
                    parts = line.split('|')
                    if len(parts) >= 2:
                        current_data['constructors'].append({'params': eval(parts[1])})
                elif line.startswith('FIELD|'):
                    parts = line.split('|')
                    if len(parts) >= 5:
                        current_data['fields'].append({
                            'name': parts[1],
                            'type': parts[2],
                            'is_static': parts[3] == 'True',
                            'is_final': parts[4] == 'True'
                        })

        return all_data

    @staticmethod
    def _parse_reflection_output(output: str) -> Dict:
        """Parse reflection output into structured data."""
        data = {'methods': [], 'constructors': [], 'fields': []}

        for line in output.strip().split('\n'):
            if line.startswith('METHOD|'):
                parts = line.split('|')
                if len(parts) >= 5:
                    data['methods'].append({
                        'name': parts[1],
                        'params': eval(parts[2]),
                        'return_type': parts[3],
                        'is_static': parts[4] == 'True'
                    })
            elif line.startswith('CONSTRUCTOR|'):
                parts = line.split('|')
                if len(parts) >= 2:
                    data['constructors'].append({'params': eval(parts[1])})
            elif line.startswith('FIELD|'):
                parts = line.split('|')
                if len(parts) >= 5:
                    data['fields'].append({
                        'name': parts[1],
                        'type': parts[2],
                        'is_static': parts[3] == 'True',
                        'is_final': parts[4] == 'True'
                    })

        return data

    def generate_java_class_stub(self, class_name: str, module_name: str, reflection_data: Dict = None) -> str:
        """Generate stub for a Java class using the best available method."""

        if self.verbose:
            print(f"  📝 Generating stub for {class_name}...")

        # Strategy 1: Use provided reflection data (most complete)
        if reflection_data and (reflection_data.get('methods') or reflection_data.get('constructors')):
            if self.verbose:
                method_count = len(reflection_data.get('methods', []))
                field_count = len(reflection_data.get('fields', []))
                print(f"    ✅ Using reflection: {method_count} methods, {field_count} fields")
            return self._generate_reflection_stub(class_name, reflection_data)

        # Strategy 2: Basic fallback stub
        if self.verbose:
            print(f"    ✅ Using basic stub")
        return self._generate_basic_stub(class_name)

    def _generate_reflection_stub(self, class_name: str, data: Dict) -> str:
        """Generate stub using reflection data."""
        lines = [
            f'class {class_name}:',
            f'    """',
            f'    SNT {class_name} class with complete method signatures.',
            f'    Generated using Java reflection.',
            f'    """',
            ''
        ]

        # Constructors
        constructors = data.get('constructors', [])
        if constructors:
            if len(constructors) == 1 and not constructors[0]['params']:
                lines.extend([
                    '    def __init__(self) -> None:',
                    f'        """Initialize {class_name}."""',
                    '        ...',
                    ''
                ])
            else:
                lines.append('    @overload')
                lines.append('    def __init__(self) -> None: ...')
                for constructor in constructors:
                    if constructor['params']:
                        lines.append('    @overload')
                        params = [f'arg{i}: {self.java_type_to_python(p)}'
                                  for i, p in enumerate(constructor['params'])]
                        params_str = ', '.join(params)
                        lines.append(f'    def __init__(self, {params_str}) -> None: ...')
                lines.append('')
        else:
            lines.extend([
                '    def __init__(self, *args: Any, **kwargs: Any) -> None:',
                f'        """Initialize {class_name}."""',
                '        ...',
                ''
            ])

        # Fields
        fields = data.get('fields', [])
        if fields:
            lines.append('    # Fields')
            for field in fields:
                python_type = self.java_type_to_python(field['type'])
                lines.append(f"    {field['name']}: {python_type}")
            lines.append('')

        # Methods
        methods = data.get('methods', [])
        if methods:
            lines.append('    # Methods')
            method_groups = {}
            for method in methods:
                name = method['name']
                if name not in method_groups:
                    method_groups[name] = []
                method_groups[name].append(method)

            # Check if this class has converters for special show() method handling
            classes_with_converters = self.get_classes_with_converters()
            has_converter = class_name in classes_with_converters

            for method_name, method_list in sorted(method_groups.items()):
                # Special handling for show() method if class has converter
                if method_name == 'show' and has_converter:
                    self._generate_display_show_method(lines, method_list)
                elif len(method_list) == 1:
                    method = method_list[0]
                    params = [f'arg{i}: {self.java_type_to_python(p)}'
                              for i, p in enumerate(method['params'])]
                    return_type = self.java_type_to_python(method['return_type'])

                    if method['is_static']:
                        lines.append('    @staticmethod')
                        params_str = ', '.join(params)
                        lines.append(f"    def {method_name}({params_str}) -> {return_type}: ...")
                    else:
                        params_str = ', '.join(params)
                        if params_str:
                            params_str = ', ' + params_str
                        lines.append(f"    def {method_name}(self{params_str}) -> {return_type}: ...")
                else:
                    for method in method_list:
                        lines.append('    @overload')
                        params = [f'arg{i}: {self.java_type_to_python(p)}'
                                  for i, p in enumerate(method['params'])]
                        return_type = self.java_type_to_python(method['return_type'])

                        if method['is_static']:
                            lines.append('    @staticmethod')
                            params_str = ', '.join(params)
                            lines.append(f"    def {method_name}({params_str}) -> {return_type}: ...")
                        else:
                            params_str = ', '.join(params)
                            if params_str:
                                params_str = ', ' + params_str
                            lines.append(f"    def {method_name}(self{params_str}) -> {return_type}: ...")
            lines.append('')
            
            # Add enhanced show() method if class has converter but no existing show() method
            if has_converter and 'show' not in method_groups:
                lines.extend([
                    '    # Enhanced show() method with converter support',
                    '    def show(self, **kwargs: Any) -> Any:',
                    '        """',
                    '        Display this object using enhanced conversion.',
                    '        ',
                    '        This method uses display() which can handle SNT-specific conversions.',
                    '        """',
                    '        from pysnt.converters import display',
                    '        return display(self, **kwargs)',
                    ''
                ])

        # Note: Enhanced show() method patching is handled during method generation
        # to avoid duplicate method definitions

        # Dynamic access fallback
        lines.extend([
            '    def __getattr__(self, name: str) -> Any:',
            '        """Dynamic attribute access for additional methods."""',
            '        ...',
            '',
            '    def __call__(self, *args: Any, **kwargs: Any) -> Any:',
            '        """Make the class callable."""',
            '        ...'
        ])

        return '\n'.join(lines)

    def _generate_display_show_method(self, lines: List[str], method_list: List[Dict]) -> None:
        """
        Generate show() method that preserves original signatures but adds display fallback.
        
        This method generates the original Java show() method signatures with enhanced
        fallback logic, avoiding duplicate method definitions.
        """
        if len(method_list) == 1:
            # Single show() method
            method = method_list[0]
            params = [f'arg{i}: {self.java_type_to_python(p)}'
                      for i, p in enumerate(method['params'])]
            return_type = self.java_type_to_python(method['return_type'])
            
            if method['is_static']:
                # Static show method - just generate normally (no enhancement needed)
                lines.append('    @staticmethod')
                params_str = ', '.join(params)
                lines.append(f"    def show({params_str}) -> {return_type}: ...")
            else:
                # Instance show method - add enhanced version
                params_str = ', '.join(params)
                if params_str:
                    params_str = ', ' + params_str
                
                lines.extend([
                    f'    def show(self{params_str}) -> {return_type}:',
                    '        """',
                    '        Display this object using enhanced conversion.',
                    '        ',
                    '        This method first tries the original Java show() method, and if that fails,',
                    '        it falls back to display() which can handle SNT-specific conversions.',
                    '        """',
                    '        try:',
                    '            # Try to call the original Java show method via __getattr__',
                    '            original_show = object.__getattribute__(self, "__getattr__")("show")',
                    f'            return original_show({", ".join(f"arg{i}" for i in range(len(params)))})',
                    '        except (AttributeError, TypeError, Exception):',
                    '            # Fallback to display',
                    '            from pysnt.converters import display',
                    '            return display(self)',
                ])
        else:
            # Multiple show() method overloads - preserve all signatures with enhancement
            lines.append('    # Enhanced show() method with multiple overloads')
            
            for i, method in enumerate(method_list):
                params = [f'arg{i}: {self.java_type_to_python(p)}'
                          for i, p in enumerate(method['params'])]
                return_type = self.java_type_to_python(method['return_type'])
                
                if method['is_static']:
                    lines.append('    @overload')
                    lines.append('    @staticmethod')
                    params_str = ', '.join(params)
                    lines.append(f"    def show({params_str}) -> {return_type}: ...")
                else:
                    lines.append('    @overload')
                    params_str = ', '.join(params)
                    if params_str:
                        params_str = ', ' + params_str
                    lines.append(f"    def show(self{params_str}) -> {return_type}: ...")
            
            # Add the implementation with fallback logic
            lines.extend([
                '    def show(self, *args: Any, **kwargs: Any) -> Any:',
                '        """',
                '        Display this object using enhanced conversion.',
                '        ',
                '        This method first tries the original Java show() method, and if that fails,',
                '        it falls back to display() which can handle SNT-specific conversions.',
                '        """',
                '        try:',
                '            # Try to call the original Java show method via __getattr__',
                '            original_show = object.__getattribute__(self, "__getattr__")("show")',
                '            return original_show(*args, **kwargs)',
                '        except (AttributeError, TypeError, Exception):',
                '            # Fallback to display',
                '            from pysnt.converters import display',
                '            return display(self, **kwargs)',
            ])

    def _generate_basic_stub(self, class_name: str) -> str:
        """Generate basic fallback stub."""
        
        # Check if this class has a converter
        classes_with_converters = self.get_classes_with_converters()
        display_show_method = ""
        
        if class_name in classes_with_converters:
            display_show_method = f'''
    
    def show(self, **kwargs: Any) -> Any:
        """
        Display this object using enhanced conversion.
        
        This method first tries the original Java show() method, and if that fails,
        it falls back to display() which can handle SNT-specific conversions.
        """
        try:
            # Try to call the original Java show method via __getattr__
            original_show = object.__getattribute__(self, "__getattr__")("show")
            return original_show(**kwargs)
        except (AttributeError, TypeError, Exception):
            # Fallback to display
            from pysnt.converters import display
            return display(self, **kwargs)'''
        
        return f'''class {class_name}:
    """
    SNT {class_name} class.
    
    This class provides access to the Java {class_name} functionality.
    All methods and properties are dynamically resolved at runtime.
    """
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the {class_name}."""
        ...{display_show_method}
    
    def __getattr__(self, name: str) -> Any:
        """Dynamic attribute access for Java methods and fields."""
        ...
    
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """Make the class callable if it has a default method."""
        ...'''

    def generate_python_stub(self, py_file: Path, stub_file: Path) -> bool:
        """Generate stub for Python file using AST."""
        try:
            with open(py_file, 'r', encoding='utf-8') as f:
                source_code = f.read()

            tree = ast.parse(source_code)
            stub_content = self._generate_python_stub_content(tree, py_file)

            with open(stub_file, 'w', encoding='utf-8') as f:
                f.write(stub_content)

            return True
        except Exception as e:
            logger.error(f"Failed to generate Python stub for {py_file}: {e}")
            return False

    def extract_module_functions_from_python(self, module_name: str) -> List[str]:
        """
        Extract function signatures from actual Python module files.
        
        Parameters
        ----------
        module_name : str
            Module name (e.g., 'pysnt', 'pysnt.analysis')
            
        Returns
        -------
        List[str]
            List of function signature strings for the stub file
        """
        module_functions = []
        
        try:
            # Convert module name to file path
            module_path = self.source_dir / module_name.replace('.', '/')
            init_file = module_path / "__init__.py"
            
            if not init_file.exists():
                if self.verbose:
                    print(f"    ⚠️  No __init__.py found for {module_name}")
                return []
            
            # Parse the Python file
            with open(init_file, 'r', encoding='utf-8') as f:
                source_code = f.read()
            
            tree = ast.parse(source_code)
            
            # Extract imports to understand what functions are available
            imported_functions = set()
            imported_classes = set()
            imported_exceptions = set()
            
            for node in tree.body:
                if isinstance(node, ast.ImportFrom):
                    if node.names:
                        for alias in node.names:
                            name = alias.name
                            # Categorize imports based on naming patterns
                            if name.endswith('Error') or name.endswith('Exception'):
                                imported_exceptions.add(name)
                            elif name[0].isupper():  # Likely a class
                                imported_classes.add(name)
                            else:  # Likely a function
                                imported_functions.add(name)
                
                elif isinstance(node, ast.FunctionDef):
                    # Direct function definitions in the module
                    func_sig = self._extract_function_signature(node)
                    imported_functions.add(node.name)
                    module_functions.append(func_sig)
                
                elif isinstance(node, ast.Assign):
                    # Handle assignments like get_class = _module_funcs["get_class"]
                    for target in node.targets:
                        if isinstance(target, ast.Name):
                            name = target.id
                            # Check if it's a function assignment from _module_funcs
                            if (isinstance(node.value, ast.Subscript) and 
                                isinstance(node.value.value, ast.Name) and 
                                node.value.value.id == '_module_funcs'):
                                # This is likely a function
                                imported_functions.add(name)
            
            # Group functions by category for better organization
            config_functions = []
            gui_functions = []
            setup_functions = []
            core_functions = []
            converter_functions = []
            other_functions = []
            
            for func_name in sorted(imported_functions):
                func_sig = self._create_function_signature_from_name(func_name)
                
                if any(keyword in func_name for keyword in ['option', 'config']):
                    config_functions.append(func_sig)
                elif any(keyword in func_name for keyword in ['gui', 'safety', 'thread', 'macos']):
                    gui_functions.append(func_sig)
                elif any(keyword in func_name for keyword in ['fiji', 'path', 'detect', 'configure']):
                    setup_functions.append(func_sig)
                elif any(keyword in func_name for keyword in ['initialize', 'version', 'info', 'show', 'display']):
                    core_functions.append(func_sig)
                elif any(keyword in func_name for keyword in ['convert', 'register', 'enhance']):
                    converter_functions.append(func_sig)
                else:
                    other_functions.append(func_sig)
            
            # Build organized function list
            if core_functions:
                module_functions.extend(['', '# Core functions'] + core_functions)
            if converter_functions:
                module_functions.extend(['', '# Converter utilities'] + converter_functions)
            if config_functions:
                module_functions.extend(['', '# Configuration system'] + config_functions)
            if gui_functions:
                module_functions.extend(['', '# GUI utilities'] + gui_functions)
            if setup_functions:
                module_functions.extend(['', '# Setup utilities'] + setup_functions)
            if other_functions:
                module_functions.extend(['', '# Other functions'] + other_functions)
            
            # Add classes
            if imported_classes:
                class_stubs = []
                for class_name in sorted(imported_classes):
                    if class_name.endswith('Error') or class_name.endswith('Exception'):
                        continue  # Handle exceptions separately
                    class_stubs.append(f'class {class_name}: ...')
                
                if class_stubs:
                    module_functions.extend(['', '# Imported classes'] + class_stubs)
            
            # Add exceptions
            if imported_exceptions:
                exception_stubs = []
                for exc_name in sorted(imported_exceptions):
                    exception_stubs.append(f'class {exc_name}(Exception): ...')
                
                if exception_stubs:
                    module_functions.extend(['', '# Exception classes'] + exception_stubs)
            
            # Add constants (look for ALL_CAPS variables)
            constants = []
            for node in tree.body:
                if isinstance(node, ast.Assign):
                    for target in node.targets:
                        if isinstance(target, ast.Name) and target.id.isupper():
                            constants.append(f'{target.id}: List[str]')
            
            if constants:
                module_functions.extend(['', '# Constants'] + constants)
            
            if self.verbose:
                print(f"    📋 Extracted {len(imported_functions)} functions, {len(imported_classes)} classes, {len(imported_exceptions)} exceptions from {module_name}")
            
        except Exception as e:
            if self.verbose:
                print(f"    ⚠️  Failed to extract functions from {module_name}: {e}")
        
        return module_functions
    
    def _extract_function_signature(self, node: ast.FunctionDef) -> str:
        """Extract function signature from AST node."""
        args = self._process_arguments(node.args)
        return_annotation = " -> Any"
        if node.returns:
            try:
                return_annotation = f" -> {ast.unparse(node.returns)}"
            except:
                return_annotation = " -> Any"
        
        return f"def {node.name}({args}){return_annotation}: ..."
    
    def _create_function_signature_from_name(self, func_name: str) -> str:
        """
        Create a function signature from just the function name.
        
        This uses heuristics to guess the likely signature based on the function name.
        """
        # Common patterns for different function types
        # Handle specific cases first
        if func_name == 'get_class':
            return f"def {func_name}(class_name: str) -> Any: ..."
        elif func_name == 'register_display_handler':
            return f"def {func_name}(handler: Callable) -> None: ..."
        elif func_name == 'enhance_java_object':
            return f"def {func_name}(obj: Any) -> Any: ..."
        
        elif func_name.startswith('get_'):
            if 'option' in func_name:
                return f"def {func_name}(key: str) -> Any: ..."
            else:
                return f"def {func_name}() -> Any: ..."
        
        elif func_name.startswith('set_'):
            if 'option' in func_name:
                return f"def {func_name}(key: str, value: Any) -> None: ..."
            elif 'path' in func_name:
                return f"def {func_name}(path: str) -> bool: ..."
            else:
                return f"def {func_name}(value: Any) -> None: ..."
        
        elif func_name.startswith('is_'):
            return f"def {func_name}() -> bool: ..."
        
        elif func_name.startswith('list_'):
            return f"def {func_name}() -> List[str]: ..."
        
        elif func_name.startswith('describe_'):
            return f"def {func_name}(key: Optional[str] = None) -> None: ..."
        
        elif func_name.startswith('reset_'):
            return f"def {func_name}(key: str) -> None: ..."
        
        elif func_name.startswith('configure_'):
            return f"def {func_name}(enabled: bool = True) -> None: ..."
        
        elif 'context' in func_name:
            return f"def {func_name}(**kwargs: Any) -> Any: ..."
        
        elif func_name in ['initialize']:
            return f"def {func_name}(fiji_path: Optional[str] = None, interactive: bool = True, ensure_java: bool = True, mode: str = \"headless\") -> None: ..."
        
        elif func_name in ['show', 'display']:
            return f"def {func_name}(obj: Any, **kwargs: Any) -> Any: ..."
        
        elif func_name in ['to_python', 'from_java']:
            return f"def {func_name}(obj: Any, **kwargs: Any) -> Any: ..."
        
        elif func_name.startswith('safe_'):
            return f"def {func_name}(func: Callable, *args: Any, fallback_func: Optional[Callable] = None, **kwargs: Any) -> Any: ..."
        
        else:
            # Generic fallback
            return f"def {func_name}(*args: Any, **kwargs: Any) -> Any: ..."

    def _generate_python_stub_content(self, tree: ast.AST, py_file: Path) -> str:
        """Generate Python stub content from AST."""
        # First pass: collect all imports and analyze what we need
        original_imports = self._extract_imports_from_ast(tree)
        
        # Generate stub content first to analyze what types are used
        stub_body_lines = []
        
        # Process top-level nodes
        for node in tree.body:
            if isinstance(node, ast.FunctionDef):
                stub_body_lines.extend(self._process_function(node))
                stub_body_lines.append('')
            elif isinstance(node, ast.ClassDef):
                stub_body_lines.extend(self._process_class(node))
                stub_body_lines.append('')
            elif isinstance(node, ast.Assign):
                stub_body_lines.extend(self._process_assignment(node))

        # Analyze stub content to determine needed imports
        stub_content = '\n'.join(stub_body_lines)
        needed_imports = self._analyze_needed_imports(stub_content, original_imports, py_file)
        
        # Build final stub with proper imports
        lines = [
            '"""',
            f'Type stubs for {py_file.name}',
            '',
            'Auto-generated stub file.',
            '"""',
            ''
        ]
        
        # Add imports
        lines.extend(needed_imports)
        lines.append('')
        
        # Add stub content
        lines.extend(stub_body_lines)

        return '\n'.join(lines)

    def _process_function(self, node: ast.FunctionDef) -> List[str]:
        """Process function definition."""
        args = self._process_arguments(node.args)
        return_annotation = " -> Any"
        if node.returns:
            return_annotation = f" -> {ast.unparse(node.returns)}"

        return [f"def {node.name}({args}){return_annotation}: ..."]

    def _process_class(self, node: ast.ClassDef) -> List[str]:
        """Process class definition."""
        lines = [f"class {node.name}:"]

        class_body = []
        for item in node.body:
            if isinstance(item, ast.FunctionDef):
                item_lines = self._process_function(item)
                class_body.extend([f"    {line}" for line in item_lines])

        if not class_body:
            class_body = ["    pass"]

        lines.extend(class_body)
        return lines

    @staticmethod
    def _process_assignment(node: ast.Assign) -> List[str]:
        """Process variable assignment."""
        lines = []
        for target in node.targets:
            if isinstance(target, ast.Name):
                lines.append(f"{target.id}: Any")
        return lines

    @staticmethod
    def _process_arguments(args: ast.arguments) -> str:
        """Process function arguments."""
        arg_strs = []

        for arg in args.args:
            arg_str = arg.arg
            if arg.annotation:
                arg_str += f": {ast.unparse(arg.annotation)}"
            else:
                arg_str += ": Any"
            arg_strs.append(arg_str)

        if args.vararg:
            vararg_str = f"*{args.vararg.arg}: Any"
            arg_strs.append(vararg_str)

        if args.kwarg:
            kwarg_str = f"**{args.kwarg.arg}: Any"
            arg_strs.append(kwarg_str)

        return ", ".join(arg_strs)

    def _extract_imports_from_ast(self, tree: ast.AST) -> Dict[str, List[str]]:
        """Extract imports from the original Python file."""
        imports = {
            'typing': [],
            'relative': [],
            'external': []
        }
        
        for node in tree.body:
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imports['external'].append(alias.name)
            elif isinstance(node, ast.ImportFrom):
                module = node.module or ''
                if module == 'typing':
                    imports['typing'].extend([alias.name for alias in node.names])
                elif module.startswith('.'):
                    # Relative import
                    import_items = [alias.name for alias in node.names]
                    imports['relative'].append((module, import_items))
                else:
                    imports['external'].append(module)
        
        return imports

    def _analyze_needed_imports(self, stub_content: str, original_imports: Dict, py_file: Path) -> List[str]:
        """Analyze stub content to determine what imports are needed."""
        import_lines = []
        
        # Always include basic typing imports
        typing_imports = {'Any'}
        
        # Check for specific types used in the stub
        if 'List[' in stub_content:
            typing_imports.add('List')
        if 'Dict[' in stub_content:
            typing_imports.add('Dict')
        if 'Optional[' in stub_content:
            typing_imports.add('Optional')
        if 'Union[' in stub_content:
            typing_imports.add('Union')
        if 'Callable[' in stub_content:
            typing_imports.add('Callable')
        if 'Tuple[' in stub_content:
            typing_imports.add('Tuple')
        if 'Set[' in stub_content:
            typing_imports.add('Set')
        if ': Type' in stub_content or '-> Type' in stub_content:
            typing_imports.add('Type')
        
        # Add typing import
        if typing_imports:
            import_lines.append(f"from typing import {', '.join(sorted(typing_imports))}")
        
        # Check for specific types that need special imports
        module_name = py_file.stem
        
        # Handle SNTObject import for converter modules
        if 'SNTObject' in stub_content and 'converters' in str(py_file):
            if module_name != 'core':  # Don't import from self
                import_lines.append("from .core import SNTObject")
        
        # Handle matplotlib Figure import
        if 'Figure' in stub_content:
            import_lines.append("from matplotlib.figure import Figure")
        
        # Handle other specific imports based on original file
        for module, items in original_imports.get('relative', []):
            # Only include relative imports that are actually used in the stub
            used_items = [item for item in items if item in stub_content]
            if used_items:
                import_lines.append(f"from {module} import {', '.join(used_items)}")
        
        return import_lines

    def generate_all_stubs(self, overwrite: bool = False) -> Dict[str, int]:
        """Generate all stub files."""
        results = {
            'java_stubs': 0,
            'python_stubs': 0,
            'errors': 0
        }

        print("🚀 Stub Generation")
        print("=" * 40)

        # Generate Java class stubs
        print("\n☕ Generating Java class stubs...")

        # First, try batch reflection for all classes
        classes_by_module = {module: config['classes'] for module, config in self.java_classes_config.items()}
        try:
            all_reflection_data = self.extract_all_methods_via_reflection(classes_by_module)
        except SystemExit:
            # Re-raise SystemExit (from FijiNotFoundError) to abort execution
            raise
        except Exception as e:
            if self.verbose:
                print(f"    ⚠️  Reflection failed, continuing with basic stubs: {e}")
            all_reflection_data = {}

        for module_name, config in self.java_classes_config.items():
            print(f"\n📦 Processing {module_name}...")

            stub_lines = [
                '"""Comprehensive type stubs for Java classes."""',
                '',
                'from typing import Any, List, Dict, Optional, Union, overload, Set, Callable',
                '',
            ]

            for class_name in config['classes']:
                try:
                    # Get reflection data for this class
                    class_key = f"{module_name}.{class_name}"
                    reflection_data = all_reflection_data.get(class_key, {})

                    class_stub = self.generate_java_class_stub(class_name, module_name, reflection_data)
                    stub_lines.append(class_stub)
                    stub_lines.append('')
                    results['java_stubs'] += 1
                except Exception as e:
                    logger.error(f"Error generating stub for {class_name}: {e}")
                    results['errors'] += 1

            # Add module functions
            module_functions = [
                '# Module functions',
                'def get_available_classes() -> List[str]: ...',
                'def get_class(class_name: str) -> Any: ...',
                'def list_classes() -> None: ...',
                'def get_curated_classes() -> List[str]: ...',
                'def get_extended_classes() -> List[str]: ...',
                '',
                'CURATED_CLASSES: List[str]',
                'EXTENDED_CLASSES: List[str]'
            ]
            
            # Use dynamic function extraction for Python modules
            if self.verbose:
                print(f"    🔍 Extracting functions dynamically from {module_name}...")
            
            module_functions = self.extract_module_functions_from_python(module_name)
            
            # If dynamic extraction fails or returns empty, use minimal fallback
            if not module_functions:
                if self.verbose:
                    print(f"    ⚠️  Dynamic extraction failed, using minimal fallback for {module_name}")
                module_functions = [
                    '# Core functions (fallback)',
                    'def initialize(fiji_path: Optional[str] = None, interactive: bool = True, ensure_java: bool = True, mode: str = "headless") -> None: ...',
                    '',
                    '# Exception classes',
                    'class FijiNotFoundError(Exception): ...',
                    'class OptionError(Exception): ...',
                ]
            
            stub_lines.extend(module_functions)

            # Write stub file
            module_path = self.source_dir / module_name.replace('.', '/')
            stub_file = module_path / "__init__.pyi"

            if stub_file.exists() and not overwrite:
                if self.verbose:
                    print(f"    ⏭️  Skipping existing: {stub_file}")
                continue

            stub_file.parent.mkdir(parents=True, exist_ok=True)
            with open(stub_file, 'w') as f:
                f.write('\n'.join(stub_lines))

            print(f"    ✅ Generated: {stub_file}")

        # Generate Python stubs
        print(f"\n🐍 Generating Python stubs...")
        python_files = list(self.source_dir.rglob("*.py"))
        exclude_patterns = ['test_*', '__pycache__', '.*']

        for py_file in python_files:
            if any(py_file.match(pattern) for pattern in exclude_patterns):
                continue

            stub_file = py_file.with_suffix('.pyi')

            # Skip if Java stub exists (preserve Java stubs)
            if stub_file.exists():
                with open(stub_file, 'r') as f:
                    content = f.read()
                    if any(indicator in content for indicator in [
                        'Java class', 'Dynamic attribute access', 'SNT.*class'
                    ]):
                        if self.verbose:
                            print(f"    ⏭️  Preserving Java stub: {stub_file}")
                        continue

            if stub_file.exists() and not overwrite:
                continue

            if self.generate_python_stub(py_file, stub_file):
                results['python_stubs'] += 1
                if self.verbose:
                    print(f"    ✅ Generated Python stub: {stub_file}")
            else:
                results['errors'] += 1

        return results


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Comprehensive stub generator for PySNT"
    )
    parser.add_argument(
        "source_dir",
        nargs="?",
        default="src",
        help="Source directory (default: src)"
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing stub files"
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Verbose output"
    )

    args = parser.parse_args()

    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    source_dir = project_root / args.source_dir

    if not source_dir.exists():
        print(f"❌ Source directory does not exist: {source_dir}")
        return 1

    generator = ComprehensiveStubGenerator(source_dir, True)  # args.verbose)
    results = generator.generate_all_stubs(True)  # args.overwrite)

    print(f"\n📊 Generation Summary")
    print("=" * 25)
    print(f"✅ Java class stubs: {results['java_stubs']}")
    print(f"✅ Python stubs: {results['python_stubs']}")
    if results['errors']:
        print(f"❌ Errors: {results['errors']}")

    total_success = results['java_stubs'] + results['python_stubs']
    print(f"\n🎉 Generated {total_success} stub files successfully!")
    print("💡 You may need to restart your IDE to see autocompletion")

    return 0 if results['errors'] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
