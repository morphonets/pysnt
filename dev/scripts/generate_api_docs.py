#!/usr/bin/env python3
"""
Generate API documentation for PySNT using sphinx-apidoc,
i.e., .rst files for all modules in the PySNT package.
"""

import subprocess
import sys
import re
from pathlib import Path


def generate_api_docs():
    """Generate API documentation using sphinx-apidoc."""

    # Paths - adjusted for scripts folder location
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    docs_dir = project_root / "docs"
    src_dir = project_root / "src"
    api_dir = docs_dir / "api_auto"

    # Create API directory
    api_dir.mkdir(exist_ok=True)

    # Run sphinx-apidoc
    cmd = [
        "sphinx-apidoc",
        "-f",  # Force overwrite
        "-e",  # Put each module on separate page
        "-T",  # Don't create table of contents file
        "-M",  # Put module documentation before submodule documentation
        "-o", str(api_dir),  # Output directory
        str(src_dir),  # Source directory
        str(src_dir / "pysnt" / "__pycache__"),  # Exclude patterns
    ]

    print(f"Running: {' '.join(cmd)}")

    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print(" API documentation generated successfully!")
        print(f"Output directory: {api_dir}")

        # List generated files
        generated_files = list(api_dir.glob("*.rst"))
        print(f"Generated {len(generated_files)} files:")
        for file in sorted(generated_files):
            print(f"  - {file.name}")

    except subprocess.CalledProcessError as e:
        print(f" Error generating API docs: {e}")
        print(f"stdout: {e.stdout}")
        print(f"stderr: {e.stderr}")
        return False

    except FileNotFoundError:
        print(" sphinx-apidoc not found. Install with: pip install sphinx")
        return False

    return True


def fix_javadoc_links():
    """Fix Javadoc link references to make them unique per class."""
    
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    src_dir = project_root / "src" / "pysnt"
    
    # Find all Python files
    python_files = list(src_dir.rglob("*.py"))
    
    fixed_files = 0
    total_replacements = 0
    
    for py_file in python_files:
        try:
            with open(py_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            modified = False
            i = 0
            used_refs = set()  # Track used references in this file
            
            while i < len(lines):
                line = lines[i]
                
                # Look for "See `Javadoc Documentation`_." lines
                if "See `Javadoc Documentation`_." in line:
                    # Look ahead for the corresponding link definition
                    j = i + 1
                    while j < len(lines) and j < i + 5:  # Look within next 5 lines
                        if lines[j].strip().startswith(".. _Javadoc Documentation:"):
                            # Extract class name from URL
                            url_match = re.search(r'sc/fiji/snt/(.+?)\.html', lines[j])
                            if url_match:
                                class_path = url_match.group(1)
                                # Convert path to safe identifier
                                class_id = class_path.replace('/', '_')
                                
                                # Make sure the reference is unique within this file
                                base_ref = f"{class_id}_javadoc"
                                unique_ref = base_ref
                                counter = 1
                                
                                while unique_ref in used_refs:
                                    unique_ref = f"{base_ref}_{counter}"
                                    counter += 1
                                
                                used_refs.add(unique_ref)
                                
                                # Update the reference line
                                lines[i] = line.replace(
                                    "See `Javadoc Documentation`_.",
                                    f"See `{unique_ref}`_."
                                )
                                
                                # Update the target line
                                lines[j] = lines[j].replace(
                                    ".. _Javadoc Documentation:",
                                    f".. _{unique_ref}:"
                                )
                                
                                modified = True
                                total_replacements += 1
                            break
                        j += 1
                
                i += 1
            
            if modified:
                with open(py_file, 'w', encoding='utf-8') as f:
                    f.writelines(lines)
                fixed_files += 1
                
        except Exception as e:
            print(f"⚠  Error processing {py_file}: {e}")
    
    print(f" Fixed Javadoc links in {fixed_files} files ({total_replacements} replacements)")


def create_api_index():
    """Create an index file for the auto-generated API docs."""

    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    docs_dir = project_root / "docs"
    api_dir = docs_dir / "api_auto"
    index_file = api_dir / "index.rst"

    content = """
Auto-Generated API Documentation
=================================

This section contains automatically generated API documentation for all pySNT modules.

.. toctree::
   :maxdepth: 2
   :glob:
   
   pysnt*

"""

    with open(index_file, 'w') as f:
        f.write(content)

    print(f"Created API index: {index_file}")


if __name__ == "__main__":
    print("Generating pySNT API Documentation")
    print("=" * 40)

    # First fix the Javadoc links to make them unique
    print("\nFixing Javadoc link references...")
    fix_javadoc_links()

    # Then generate the API docs
    print("\nGenerating API documentation...")
    if generate_api_docs():
        create_api_index()
    else:
        print("\nAPI documentation generation failed")
        sys.exit(1)
