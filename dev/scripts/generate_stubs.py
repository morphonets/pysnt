#!/usr/bin/env python3
"""
Clean Type Stub Generator for PySNT

Generates .pyi files exclusively from cached JSON signatures.
No fallback strategies - if cache is missing, extraction is required first.

Usage:
    python dev/scripts/generate_stubs.py --verbose
    python dev/scripts/generate_stubs.py --check-cache
    python dev/scripts/generate_stubs.py --force --overwrite
"""

import argparse
import ast
import json
import logging
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))


class CleanStubGenerator:
    """Clean stub generator using only cached JSON signatures."""

    def __init__(self, source_dir: Path, verbose: bool = False):
        self.source_dir = Path(source_dir)
        self.verbose = verbose
        self.stubs_cache_dir = Path("dev/scripts/STUBS")
        
        # Java type to Python type mapping (mainly for fallback cases)
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

        # Discover Java classes from modules
        self.java_classes_config = {}
        self._populate_java_classes_config()

    def _populate_java_classes_config(self):
        """Discover Java classes from all pysnt modules."""
        try:
            init_files = list(self.source_dir.rglob("__init__.py"))
            
            for init_file in init_files:
                if "__pycache__" in str(init_file):
                    continue
                
                # Get module name from path
                relative_path = init_file.relative_to(self.source_dir)
                module_parts = relative_path.parts[:-1]  # Remove __init__.py
                
                if not module_parts:
                    module_name = "pysnt"
                    java_package = "sc.fiji.snt"
                else:
                    filtered_parts = [part for part in module_parts if part != 'pysnt']
                    if filtered_parts:
                        module_name = "pysnt." + ".".join(filtered_parts)
                        java_package = "sc.fiji.snt." + ".".join(filtered_parts)
                    else:
                        module_name = "pysnt"
                        java_package = "sc.fiji.snt"
                
                # Parse CURATED_CLASSES from the file
                try:
                    with open(init_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    tree = ast.parse(content)
                    curated_classes = []
                    
                    for node in ast.walk(tree):
                        if isinstance(node, ast.Assign):
                            for target in node.targets:
                                if isinstance(target, ast.Name):
                                    if target.id in ["CURATED_CLASSES", "CURATED_ROOT_CLASSES"] and isinstance(node.value, ast.List):
                                        for item in node.value.elts:
                                            if isinstance(item, ast.Constant) and isinstance(item.value, str):
                                                curated_classes.append(item.value)
                                            elif isinstance(item, ast.Str):  # Python < 3.8
                                                curated_classes.append(item.s)
                    
                    if curated_classes:
                        self.java_classes_config[module_name] = {
                            'classes': curated_classes,
                            'package': java_package
                        }
                        if self.verbose:
                            print(f"    📋 Found {len(curated_classes)} classes in {module_name}")
                
                except Exception as e:
                    if self.verbose:
                        print(f"    ⚠️  Failed to parse {init_file}: {e}")
        
        except Exception as e:
            logger.error(f"Failed to populate Java classes config: {e}")
            sys.exit(1)

    def load_cached_signatures(self, class_name: str) -> Optional[Dict[str, Any]]:
        """Load cached method signatures for a class."""
        cache_file = self.stubs_cache_dir / f"{class_name}.json"
        
        if not cache_file.exists():
            return None
        
        try:
            with open(cache_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"Failed to load cached signatures for {class_name}: {e}")
            return None

    def check_cache_freshness(self, class_name: str, module_name: str) -> Dict[str, Any]:
        """Check if cached signatures are up-to-date for a class."""
        cache_file = self.stubs_cache_dir / f"{class_name}.json"
        stub_file = self.source_dir / module_name.replace('.', '/') / "__init__.pyi"
        
        result = {
            'has_cache': cache_file.exists(),
            'has_stub': stub_file.exists(),
            'cache_newer': False,
            'needs_update': True,
            'cache_age_days': None,
            'stub_age_days': None,
            'cache_version': None,
            'reason': 'No cache file'
        }
        
        if not cache_file.exists():
            return result
        
        try:
            # Load cache metadata
            with open(cache_file, 'r', encoding='utf-8') as f:
                cache_data = json.load(f)
            
            cache_time_str = cache_data.get('extracted_at')
            cache_version = cache_data.get('extractor_version', 'unknown')
            result['cache_version'] = cache_version
            
            if not cache_time_str:
                result['reason'] = 'No timestamp in cache'
                return result
            
            # Cache validity is tied to the SNT version, not to its age
            cache_time = datetime.fromisoformat(cache_time_str.replace('Z', '+00:00'))
            result['cache_age_days'] = (datetime.now() - cache_time).days
            if stub_file.exists():
                stub_mtime = datetime.fromtimestamp(stub_file.stat().st_mtime)
                result['stub_age_days'] = (datetime.now() - stub_mtime).days
                result['cache_newer'] = cache_time > stub_mtime

            snt_version = cache_data.get('snt_version')
            if not snt_version or not str(cache_version).startswith('2.'):
                result['reason'] = 'Cache predates version stamping: re-run extract_class_signatures.py'
            elif result['cache_newer'] or not stub_file.exists():
                result['reason'] = f'Cache (SNT {snt_version}) is newer than the stub'
            else:
                result['needs_update'] = False
                result['reason'] = f'Stub is current with cache (SNT {snt_version})'

            return result

        except Exception as e:
            result['reason'] = f'Error reading cache: {e}'
            return result

    def should_regenerate_stub(self, class_name: str, module_name: str, force: bool = False) -> tuple[bool, str]:
        """Determine if a stub should be regenerated."""
        if force:
            return True, "Forced regeneration"
        
        cache_status = self.check_cache_freshness(class_name, module_name)
        
        if not cache_status['has_cache']:
            return True, "No cached signatures available"
        
        if cache_status['needs_update']:
            return True, cache_status['reason']
        
        return False, cache_status['reason']

    _PY_KEYWORDS = {
        "False", "None", "True", "and", "as", "assert", "async", "await", "break", "class",
        "continue", "def", "del", "elif", "else", "except", "finally", "for", "from",
        "global", "if", "import", "in", "is", "lambda", "nonlocal", "not", "or", "pass",
        "raise", "return", "try", "while", "with", "yield", "self",
    }

    def _stub_params(self, params):
        """Render Java parameters: positional-only (JPype calls are positional), varargs as *name"""
        out = []
        used = set()
        for i, param in enumerate(params):
            name = param.get('name') or f'arg{i}'
            if name in self._PY_KEYWORDS or not name.isidentifier():
                name = f'{name}_' if name.isidentifier() else f'arg{i}'
            while name in used:
                name += '_'
            used.add(name)
            ptype = param.get('type', 'Any')
            if param.get('varargs'):
                inner = ptype[5:-1] if ptype.startswith('List[') and ptype.endswith(']') else 'Any'
                out.append(f'*{name}: {inner}')
            else:
                out.append(f'{name}: {ptype}')
        # Positional-only marker (cannot follow *args)
        if out and not any(p.startswith('*') for p in out):
            out.append('/')
        return out

    @staticmethod
    def _deprecation_decorator(overload):
        if not overload.get('deprecated'):
            return None
        msg = "Deprecated; scheduled for removal" if overload.get('for_removal') else "Deprecated"
        return f'@deprecated("{msg}")'

    def _emit_overloads(self, lines, name, overloads, is_constructor=False):
        """Append stub lines for one method name (all its overloads)"""
        statics = {bool(o.get('is_static')) for o in overloads}
        # Python cannot mix static and instance overloads under one name: fall back to instance
        static = (statics == {True}) and not is_constructor
        multi = len(overloads) > 1
        for ov in overloads:
            if multi:
                lines.append('    @overload')
            dec = self._deprecation_decorator(ov)
            if dec:
                lines.append(f'    {dec}')
            if static:
                lines.append('    @staticmethod')
            params = self._stub_params(ov.get('params', []))
            first = [] if static else ['self']
            ret = 'None' if is_constructor else ov.get('return_type', 'Any')
            lines.append(f"    def {name}({', '.join(first + params)}) -> {ret}: ...")

    def generate_class_stub_from_cache(self, class_name: str, signatures: Dict[str, Any]) -> str:
        """Generate a class stub from cached signatures."""
        package = signatures.get('package', 'sc.fiji.snt')
        snt_version = signatures.get('snt_version', 'unknown')
        py_name = class_name.replace('.', '_')

        lines = [f'class {py_name}:']
        doc = f'{package}.{class_name}  (SNT {snt_version})'
        if signatures.get('deprecated'):
            doc += '  [deprecated]'
        lines.append(f'    """{doc}"""')

        # Constants / static fields
        for field in signatures.get('static_fields', []):
            lines.append(f"    {field['name']}: ClassVar[{field.get('type', 'Any')}]")
        for field in signatures.get('fields', []):
            lines.append(f"    {field['name']}: {field.get('type', 'Any')}")

        # Constructors
        ctors = signatures.get('constructors', [])
        if ctors and ctors[0].get('overloads'):
            self._emit_overloads(lines, '__init__', ctors[0]['overloads'], is_constructor=True)
        else:
            lines.append('    def __init__(self, *args: Any, **kwargs: Any) -> None: ...')

        # Methods
        for method_info in signatures.get('methods', []):
            name = self._clean_method_name(method_info['name'])
            overloads = method_info.get('overloads', [])
            if overloads:
                self._emit_overloads(lines, name, overloads)

        lines.append('    def __getattr__(self, name: str) -> Any: ...')
        lines.append('')
        return '\n'.join(lines)

    def _clean_method_name(self, method_name: str) -> str:
        """Clean method name by removing Java modifiers and invalid Python syntax."""
        # Remove Java modifiers that can appear in method names
        java_modifiers = ['static', 'final', 'synchronized', 'native', 'abstract', 'public', 'private', 'protected']
        
        # Split the method name and remove any Java modifiers
        parts = method_name.split()
        cleaned_parts = [part for part in parts if part not in java_modifiers]
        
        # Join back and take the last part (the actual method name)
        if cleaned_parts:
            return cleaned_parts[-1]
        else:
            # Fallback if all parts were modifiers
            return method_name.replace(' ', '_')

    def generate_basic_stub(self, class_name: str) -> str:
        """Generate basic stub when no cache is available."""
        return f'''class {class_name}:
    """
    {class_name} - No cached signatures available.
    
    Run: python dev/scripts/extract_class_signatures.py --all-classes
    """
    
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def __getattr__(self, name: str) -> Any: ...
    def __call__(self, *args: Any, **kwargs: Any) -> Any: ...'''

    def extract_module_functions_from_python(self, module_name: str) -> List[str]:
        """Extract function signatures from Python module files."""
        module_functions = []
        
        try:
            module_path = self.source_dir / module_name.replace('.', '/')
            init_file = module_path / "__init__.py"
            
            if not init_file.exists():
                return []
            
            with open(init_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            tree = ast.parse(content)
            
            # Extract imports and functions
            imported_functions = set()
            imported_classes = set()
            imported_exceptions = set()
            imported_constants = set()
            
            for node in tree.body:
                if isinstance(node, ast.ImportFrom):
                    if node.names:
                        for alias in node.names:
                            name = alias.name
                            if name.endswith('Error') or name.endswith('Exception'):
                                imported_exceptions.add(name)
                            elif name[0].isupper() and '_' in name:
                                # Constants like DEFAULT_CMAP, ERROR_MISSING_NETWORKX
                                imported_constants.add(name)
                            elif name[0].isupper():
                                imported_classes.add(name)
                            else:
                                imported_functions.add(name)
                
                elif isinstance(node, ast.FunctionDef):
                    func_sig = self._extract_function_signature(node)
                    module_functions.append(func_sig)
            
            # Special handling for display.utils module
            if module_name == 'pysnt.display.utils':
                module_functions.extend(self._get_display_utils_special_stubs())
            
            # Add organized function stubs
            if imported_constants:
                module_functions.extend(['', '# Constants imported from converters.core'])
                for const_name in sorted(imported_constants):
                    const_type = self._get_constant_type(const_name)
                    module_functions.append(f'{const_name}: {const_type}')
            
            if imported_functions:
                module_functions.extend(['', '# Imported functions'])
                for func_name in sorted(imported_functions):
                    func_sig = self._create_function_signature_from_name(func_name)
                    module_functions.append(func_sig)
            
            if imported_classes:
                module_functions.extend(['', '# Imported classes'])
                for class_name in sorted(imported_classes):
                    if not class_name.endswith('Error') and not class_name.endswith('Exception'):
                        module_functions.append(f'class {class_name}: ...')
            
            if imported_exceptions:
                module_functions.extend(['', '# Exception classes'])
                for exc_name in sorted(imported_exceptions):
                    module_functions.append(f'class {exc_name}(Exception): ...')
            
            if self.verbose:
                print(f"    📋 Extracted {len(imported_functions)} functions, {len(imported_classes)} classes, {len(imported_constants)} constants from {module_name}")
            
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
        """Create a function signature from function name using heuristics."""
        if func_name == 'initialize':
            return f"def {func_name}(fiji_path: Optional[str] = None, interactive: bool = True, ensure_java: bool = True, mode: str = \"headless\", max_heap: Optional[str] = None, min_heap: Optional[str] = None, jvm_args: Optional[List[str]] = None) -> None: ..."
        elif func_name == 'dispose':
            return f"def {func_name}() -> None: ..."
        elif func_name in ['show', 'display']:
            return f"def {func_name}(obj: Any, **kwargs: Any) -> Any: ..."
        elif func_name == 'register_display_handler':
            return f"def {func_name}(obj_type: str, handler_func: Callable) -> None: ..."
        elif func_name == 'enhance_java_object':
            return f"def {func_name}(obj: Any) -> Any: ..."
        elif func_name == 'register_snt_converters':
            return f"def {func_name}() -> bool: ..."
        elif func_name == 'list_converters':
            return f"def {func_name}() -> List[str]: ..."
        elif func_name == 'to_python':
            return f"def {func_name}(obj: Any) -> Any: ..."
        elif func_name == 'from_java':
            return f"def {func_name}(obj: Any) -> Any: ..."
        elif func_name == 'ij':
            return f"def {func_name}() -> Any: ..."
        elif func_name.startswith('get_'):
            return f"def {func_name}() -> Any: ..."
        elif func_name.startswith('set_'):
            return f"def {func_name}(value: Any) -> None: ..."
        elif func_name.startswith('is_'):
            return f"def {func_name}() -> bool: ..."
        elif func_name == '_setup_matplotlib_interactive':
            return f"def {func_name}() -> Any: ..."  # Returns matplotlib.pyplot module
        elif func_name == '_create_standard_figure':
            return f"def {func_name}(data: Any = None, title: Optional[str] = None, figsize: Optional[tuple[float, float]] = None, dpi: Optional[int] = None, cmap: Optional[str] = None, add_colorbar: bool = True, is_rgb: bool = False, **kwargs: Any) -> tuple[Any, Any, Any]: ..."
        elif func_name == '_extract_color_attributes':
            return f"def {func_name}(color_obj: Any, prefix: str = 'color') -> Dict[str, Any]: ..."
        else:
            return f"def {func_name}(*args: Any, **kwargs: Any) -> Any: ..."

    def _get_constant_type(self, const_name: str) -> str:
        """Get the type for a constant based on its name."""
        if const_name in ['DEFAULT_CMAP', 'DEFAULT_NODE_COLOR', 'ERROR_MISSING_NETWORKX']:
            return 'str'
        elif const_name == 'DEFAULT_NODE_SIZE':
            return 'int'
        else:
            return 'Any'

    def _get_display_utils_special_stubs(self) -> List[str]:
        """Get special stub definitions for display.utils module."""
        return [
            '',
            'def _hide_axis_decorations(ax: Any, hide_axis_completely: bool = False) -> None: ...',
            'def _setup_clean_axis(ax: Any, title: Optional[str] = None, show_title: bool = True, hide_axis_completely: bool = False) -> None: ...',
            'def _apply_standard_layout(fig: Any, show_overall_title: bool = False, show_panel_titles: bool = False, overall_title: Optional[str] = None) -> None: ...',
            'def _create_subplot_grid(num_panels: int, panel_layout: Union[str, tuple[int, int]] = "auto", figsize: Optional[tuple[float, float]] = None, source_figures: Optional[List[Any]] = None) -> tuple[Any, List[Any], tuple[int, int]]: ...',
        ]

    def _generate_display_utils_stub_content(self, tree: ast.AST) -> List[str]:
        """Generate special stub content for display.utils module."""
        lines = []
        
        # Extract imports and constants
        imported_constants = set()
        imported_functions = set()
        
        for node in tree.body:
            if isinstance(node, ast.ImportFrom):
                if node.names:
                    for alias in node.names:
                        name = alias.name
                        if name[0].isupper() and '_' in name:
                            # Constants like DEFAULT_CMAP
                            imported_constants.add(name)
                        elif name.startswith('_'):
                            # Functions like _setup_matplotlib_interactive
                            imported_functions.add(name)
            elif isinstance(node, ast.FunctionDef):
                func_sig = self._extract_function_signature(node)
                lines.append(func_sig)
            elif isinstance(node, ast.Assign):
                lines.extend(self._process_assignment(node))
        
        # Add constants
        if imported_constants:
            lines.extend(['', '# Constants imported from converters.core'])
            for const_name in sorted(imported_constants):
                const_type = self._get_constant_type(const_name)
                lines.append(f'{const_name}: {const_type}')
        
        # Add imported functions with proper signatures
        if imported_functions:
            lines.extend(['', '# Functions imported from converters.core'])
            for func_name in sorted(imported_functions):
                func_sig = self._create_function_signature_from_name(func_name)
                lines.append(func_sig)
        
        # Add our special utility functions
        lines.extend(self._get_display_utils_special_stubs())
        
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
            'from typing import Any, Dict, List, Optional, Union, Callable, Tuple',
            '',
        ]
        
        # Special handling for display.utils module
        if 'display' in str(py_file) and py_file.name == 'utils.py':
            lines.extend(self._generate_display_utils_stub_content(tree))
        else:
            # Standard processing for other modules
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

    def generate_all_stubs(self, overwrite: bool = False, force: bool = False) -> Dict[str, int]:
        """Generate all stub files using cached signatures."""
        results = {
            'java_stubs': 0,
            'python_stubs': 0,
            'errors': 0,
            'missing_cache': 0
        }

        print("🚀 Clean Stub Generation (Cache-Only)")
        print("=" * 45)

        # Generate Java class stubs
        print("\n☕ Generating Java class stubs from cache...")

        for module_name, config in self.java_classes_config.items():
            print(f"\n📦 Processing {module_name}...")

            # Check cache status for all classes in this module
            classes_needing_update = []
            classes_up_to_date = []
            classes_missing_cache = []
            
            for class_name in config['classes']:
                cache_file = self.stubs_cache_dir / f"{class_name}.json"
                if not cache_file.exists():
                    classes_missing_cache.append(class_name)
                    continue
                    
                should_regen, reason = self.should_regenerate_stub(class_name, module_name, force)
                if should_regen:
                    classes_needing_update.append((class_name, reason))
                else:
                    classes_up_to_date.append((class_name, reason))
            
            # Report missing caches
            if classes_missing_cache:
                results['missing_cache'] += len(classes_missing_cache)
                print(f"    ❌ Missing cache for {len(classes_missing_cache)} classes:")
                for class_name in classes_missing_cache[:3]:
                    print(f"      ❌ {class_name}")
                if len(classes_missing_cache) > 3:
                    print(f"      ... and {len(classes_missing_cache) - 3} more")
                print(f"    💡 Run: python dev/scripts/extract_class_signatures.py --all-classes")
            
            # Check if we should skip this module
            module_path = self.source_dir / module_name.replace('.', '/')
            stub_file = module_path / "__init__.pyi"
            
            if not classes_needing_update and stub_file.exists() and not overwrite and not classes_missing_cache:
                if self.verbose:
                    print(f"    ⏭️  Skipping {module_name}: All {len(classes_up_to_date)} classes have fresh cache")
                continue
            
            # Report status
            if self.verbose and classes_up_to_date:
                print(f"    ✅ {len(classes_up_to_date)} classes have fresh cache")
            
            if self.verbose and classes_needing_update:
                print(f"    🔄 {len(classes_needing_update)} classes need updates")

            # Generate stub content
            stub_lines = [
                '"""Comprehensive type stubs for Java classes."""',
                '',
                'from typing import Any, List, Dict, Optional, Union, overload, Set, Callable, Tuple, ClassVar',
                'from typing_extensions import deprecated',
                '',
            ]

            for class_name in config['classes']:
                try:
                    signatures = self.load_cached_signatures(class_name)
                    
                    if signatures:
                        class_stub = self.generate_class_stub_from_cache(class_name, signatures)
                        if self.verbose:
                            method_count = len(signatures.get('methods', []))
                            print(f"    📋 {class_name}: {method_count} methods from cache")
                    else:
                        class_stub = self.generate_basic_stub(class_name)
                        if self.verbose:
                            print(f"    ⚠️  {class_name}: Using basic stub (no cache)")
                    
                    stub_lines.append(class_stub)
                    stub_lines.append('')
                    results['java_stubs'] += 1
                    
                except Exception as e:
                    logger.error(f"Error generating stub for {class_name}: {e}")
                    results['errors'] += 1

            # Add Python functions
            if self.verbose:
                print(f"    🔍 Extracting Python functions from {module_name}...")
            
            module_functions = self.extract_module_functions_from_python(module_name)
            stub_lines.extend(module_functions)

            # Write stub file
            if stub_file.exists() and not overwrite:
                if self.verbose:
                    print(f"    ⏭️  Skipping existing: {stub_file}")
                continue

            stub_file.parent.mkdir(parents=True, exist_ok=True)
            with open(stub_file, 'w', encoding='utf-8') as f:
                f.write('\n'.join(stub_lines))

            print(f"    ✅ Generated: {stub_file}")

        # Pure-Python modules are intentionally not stubbed (inline annotations suffice)

        return results


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Clean stub generator for PySNT (cache-only)"
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
    parser.add_argument(
        "--force",
        action="store_true",
        help="Force regeneration even if cached signatures are up-to-date"
    )
    parser.add_argument(
        "--check-cache",
        action="store_true",
        help="Check cache status and show which files would be regenerated"
    )

    args = parser.parse_args()

    script_dir = Path(__file__).parent
    project_root = script_dir.parent.parent  # dev/scripts -> dev -> project_root
    source_dir = project_root / args.source_dir

    if not source_dir.exists():
        print(f"❌ Source directory does not exist: {source_dir}")
        return 1

    generator = CleanStubGenerator(source_dir, args.verbose)
    
    # Handle cache checking mode
    if args.check_cache:
        print("🔍 Checking cache status...")
        print("=" * 40)
        
        total_classes = 0
        fresh_classes = 0
        missing_classes = 0
        
        for module_name, config in generator.java_classes_config.items():
            print(f"\n📦 {module_name}:")
            for class_name in config['classes']:
                total_classes += 1
                cache_file = generator.stubs_cache_dir / f"{class_name}.json"
                
                if not cache_file.exists():
                    missing_classes += 1
                    print(f"  ❌ {class_name}: NO CACHE - Run extraction first")
                    continue
                
                cache_status = generator.check_cache_freshness(class_name, module_name)
                
                if cache_status['needs_update']:
                    status_icon = "🔄"
                    status_text = "NEEDS UPDATE"
                else:
                    status_icon = "✅"
                    status_text = "UP-TO-DATE"
                    fresh_classes += 1
                
                age_info = ""
                if cache_status['cache_age_days'] is not None:
                    age_info = f" ({cache_status['cache_age_days']}d old)"
                
                print(f"  {status_icon} {class_name}: {status_text} - {cache_status['reason']}{age_info}")
        
        print(f"\n📊 Cache Summary:")
        print(f"✅ Fresh: {fresh_classes}/{total_classes} classes")
        print(f"🔄 Need update: {total_classes - fresh_classes - missing_classes}/{total_classes} classes")
        print(f"❌ Missing cache: {missing_classes}/{total_classes} classes")
        
        if missing_classes > 0:
            print(f"\n💡 Extract missing signatures:")
            print(f"   python dev/scripts/extract_class_signatures.py --all-classes --verbose")
        elif fresh_classes == total_classes:
            print("💡 All caches are fresh! Use --force to regenerate anyway.")
        
        return 0
    
    results = generator.generate_all_stubs(args.overwrite, args.force)

    print(f"\n📊 Generation Summary")
    print("=" * 25)
    print(f"✅ Java class stubs: {results['java_stubs']}")
    print(f"✅ Python stubs: {results['python_stubs']}")
    if results['missing_cache']:
        print(f"❌ Missing cache: {results['missing_cache']}")
    if results['errors']:
        print(f"❌ Errors: {results['errors']}")

    total_success = results['java_stubs'] + results['python_stubs']
    print(f"\n🎉 Generated {total_success} stub files successfully!")
    
    if results['missing_cache'] > 0:
        print(f"💡 Extract missing signatures: python dev/scripts/extract_class_signatures.py --all-classes")
    
    if not args.force:
        print("💡 Use --check-cache to see cache status")
        print("💡 Use --force to regenerate all stubs regardless of cache")
    
    print("💡 You may need to restart your IDE to see autocompletion")

    return 0 if results['errors'] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())