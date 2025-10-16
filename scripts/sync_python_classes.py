#!/usr/bin/env python3
"""
Sync Python classes with their stub files.

Adds placeholder methods to Python classes to match their stub files,
ensuring IDEs can provide proper autocompletion.
"""

import ast
from pathlib import Path
from typing import Dict, List


def extract_methods_from_stub(stub_file: Path, class_name: str) -> List[Dict]:
    """Extract method definitions from a stub file for a specific class."""

    if not stub_file.exists():
        return []

    try:
        with open(stub_file, 'r') as f:
            content = f.read()

        tree = ast.parse(content)
        methods = []

        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and node.name == class_name:
                for item in node.body:
                    if isinstance(item, ast.FunctionDef) and item.name not in ['__init__', '__getattr__', '__call__']:
                        # Extract method signature
                        args = []
                        for arg in item.args.args:
                            if arg.arg != 'self':  # Skip self parameter
                                args.append(arg.arg)

                        # Get return annotation
                        return_type = 'Any'
                        if item.returns:
                            return_type = ast.unparse(item.returns)

                        methods.append({
                            'name': item.name,
                            'args': args,
                            'return_type': return_type,
                            'is_static': any(isinstance(d, ast.Name) and d.id == 'staticmethod'
                                             for d in item.decorator_list)
                        })

        return methods

    except Exception as e:
        print(f"Error parsing stub file {stub_file}: {e}")
        return []


def generate_placeholder_method(method: Dict) -> str:
    """Generate a placeholder method implementation."""

    args_str = ', '.join(method['args'])
    if args_str:
        args_str = ', ' + args_str

    if method['is_static']:
        return f'''    @staticmethod
    def {method['name']}({', '.join(method['args'])}):
        """Placeholder method. Call pysnt.initialize() first."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")'''
    else:
        return f'''    def {method['name']}(self{args_str}):
        """Placeholder method. Call pysnt.initialize() first."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")'''


def update_python_class(py_file: Path, class_name: str, methods: List[Dict]) -> bool:
    """Update a Python class to include placeholder methods."""

    if not methods:
        return False

    try:
        with open(py_file, 'r') as f:
            content = f.read()

        # Find the class definition
        lines = content.split('\n')
        class_start = None
        class_end = None
        indent_level = None

        for i, line in enumerate(lines):
            if line.strip().startswith(f'class {class_name}:'):
                class_start = i
                # Find the indentation level of the class content
                for j in range(i + 1, len(lines)):
                    if lines[j].strip() and not lines[j].startswith(' '):
                        class_end = j
                        break
                    elif lines[j].strip() and indent_level is None:
                        indent_level = len(lines[j]) - len(lines[j].lstrip())

                if class_end is None:
                    class_end = len(lines)
                break

        if class_start is None:
            print(f"Class {class_name} not found in {py_file}")
            return False

        # Check if class only has 'pass' and docstrings
        class_content = lines[class_start + 1:class_end]
        method_lines = []
        in_docstring = False

        for line in class_content:
            stripped = line.strip()
            if not stripped or stripped.startswith('#'):
                continue
            elif stripped == 'pass':
                continue
            elif '"""' in stripped:
                in_docstring = not in_docstring
                continue
            elif in_docstring:
                continue
            else:
                # This is actual code
                method_lines.append(line)

        if method_lines:
            print(f"Class {class_name} already has methods: {[l.strip() for l in method_lines[:3]]}, skipping")
            return False

        # Generate new class content
        new_lines = lines[:class_start + 1]  # Include class definition

        # Add docstring if it exists
        docstring_added = False
        for line in class_content:
            if line.strip().startswith('"""') or (docstring_added and '"""' in line):
                new_lines.append(line)
                if line.strip().endswith('"""') and line.strip() != '"""':
                    docstring_added = True
                    break
                elif '"""' in line and docstring_added:
                    docstring_added = True
                    break
                else:
                    docstring_added = True

        # Add placeholder methods
        for method in methods:
            method_code = generate_placeholder_method(method)
            new_lines.extend(method_code.split('\n'))
            new_lines.append('')  # Empty line between methods

        # Add __getattr__ for dynamic access
        new_lines.extend([
            '    def __getattr__(self, name: str):',
            '        """Dynamic attribute access for additional Java methods."""',
            '        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")',
            ''
        ])

        # Add the rest of the file
        new_lines.extend(lines[class_end:])

        # Write back to file
        with open(py_file, 'w') as f:
            f.write('\n'.join(new_lines))

        print(f"✅ Updated {class_name} in {py_file} with {len(methods)} methods")
        return True

    except Exception as e:
        print(f"Error updating {py_file}: {e}")
        return False


def main():
    """Main function to sync Python classes with stub files."""

    print("🔄 Syncing Python classes with stub files...")

    project_root = Path(__file__).parent.parent

    # Classes to sync
    classes_to_sync = [
        {
            'py_file': project_root / 'src/pysnt/__init__.py',
            'stub_file': project_root / 'src/pysnt/__init__.pyi',
            'classes': ['Tree', 'Path', 'SNTUtils']
        },
        {
            'py_file': project_root / 'src/pysnt/analysis/__init__.py',
            'stub_file': project_root / 'src/pysnt/analysis/__init__.pyi',
            'classes': ['TreeStatistics']
        }
    ]

    total_updated = 0

    for config in classes_to_sync:
        py_file = config['py_file']
        stub_file = config['stub_file']

        print(f"\n📝 Processing {py_file.name}...")

        for class_name in config['classes']:
            methods = extract_methods_from_stub(stub_file, class_name)
            if methods:
                print(f"  Found {len(methods)} methods for {class_name} in stub file")
                if update_python_class(py_file, class_name, methods):
                    total_updated += 1
            else:
                print(f"  No methods found for {class_name} in stub file")

    print(f"\n🎉 Updated {total_updated} classes")
    print("💡 Python classes now match their stub files for better IDE support")


if __name__ == "__main__":
    main()
