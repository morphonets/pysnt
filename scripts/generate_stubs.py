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

            for method_name, method_list in sorted(method_groups.items()):
                if len(method_list) == 1:
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

    @staticmethod
    def _generate_basic_stub(class_name: str) -> str:
        """Generate basic fallback stub."""
        return f'''class {class_name}:
    """
    SNT {class_name} class.
    
    This class provides access to the Java {class_name} functionality.
    All methods and properties are dynamically resolved at runtime.
    """
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the {class_name}."""
        ...
    
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

    def _generate_python_stub_content(self, tree: ast.AST, py_file: Path) -> str:
        """Generate Python stub content from AST."""
        lines = [
            '"""',
            f'Type stubs for {py_file.name}',
            '',
            'Auto-generated stub file.',
            '"""',
            '',
            'from typing import Any',
            ''
        ]

        # Process top-level nodes
        for node in tree.body:
            if isinstance(node, ast.FunctionDef):
                lines.extend(self._process_function(node))
                lines.append('')
            elif isinstance(node, ast.ClassDef):
                lines.extend(self._process_class(node))
                lines.append('')
            elif isinstance(node, ast.Assign):
                lines.extend(self._process_assignment(node))

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
                'from typing import Any, List, Dict, Optional, Union, overload, Set',
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
            
            # Add custom functions for main pysnt module
            if module_name == 'pysnt':
                module_functions = [
                    '# Module functions',
                    'def initialize(fiji_dir: Optional[str] = None, headless: bool = True, enable_ui: bool = False) -> Any: ...',
                    'def inspect(class_or_object: Union[str, Any], keyword: str = "", methods: bool = True, fields: bool = True, constructors: bool = False, static_only: bool = False, case_sensitive: bool = False, max_results: int = 50) -> None: ...',
                    'def get_methods(class_or_object: Union[str, Any], static_only: bool = False, include_inherited: bool = True) -> List[Dict[str, Any]]: ...',
                    'def get_fields(class_or_object: Union[str, Any], static_only: bool = False) -> List[Dict[str, Any]]: ...',
                    'def find_members(class_or_object: Union[str, Any], keyword: str, include_methods: bool = True, include_fields: bool = True, static_only: bool = False, case_sensitive: bool = False) -> Dict[str, List[Dict[str, Any]]]: ...',
                    'def version(detailed: bool = False) -> str: ...',
                    'def print_version(detailed: bool = False) -> None: ...',
                    'def show_version(detailed: bool = False) -> None: ...',
                    'def info() -> None: ...',
                    'def get_available_classes() -> List[str]: ...',
                    'def get_class(class_name: str) -> Any: ...',
                    'def list_classes() -> None: ...',
                    'def get_curated_classes() -> List[str]: ...',
                    'def get_extended_classes() -> List[str]: ...',
                    '',
                    '# Setup utilities',
                    'def set_fiji_path(path: str) -> bool: ...',
                    'def get_fiji_path() -> Optional[str]: ...',
                    'def clear_fiji_path() -> None: ...',
                    'def reset_fiji_path() -> None: ...',
                    'def get_config_info() -> Dict[str, Any]: ...',
                    'def show_config_status() -> None: ...',
                    'def auto_detect_and_configure() -> bool: ...',
                    'def is_fiji_valid(path: str) -> bool: ...',
                    'def get_fiji_status() -> Dict[str, Any]: ...',
                    '',
                    '# Exception classes',
                    'class FijiNotFoundError(Exception): ...',
                    '',
                    '# Constants',
                    'CURATED_ROOT_CLASSES: List[str]',
                    'EXTENDED_ROOT_CLASSES: List[str]',
                    'CURATED_CLASSES: List[str]',
                    'EXTENDED_CLASSES: List[str]'
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
