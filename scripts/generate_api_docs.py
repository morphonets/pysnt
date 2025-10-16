#!/usr/bin/env python3
"""
Generate API documentation for PySNT using sphinx-apidoc,
i.e., .rst files for all modules in the PySNT package.
"""

import subprocess
import sys
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
        print("✅ API documentation generated successfully!")
        print(f"Output directory: {api_dir}")

        # List generated files
        generated_files = list(api_dir.glob("*.rst"))
        print(f"Generated {len(generated_files)} files:")
        for file in sorted(generated_files):
            print(f"  - {file.name}")

    except subprocess.CalledProcessError as e:
        print(f"❌ Error generating API docs: {e}")
        print(f"stdout: {e.stdout}")
        print(f"stderr: {e.stderr}")
        return False

    except FileNotFoundError:
        print("❌ sphinx-apidoc not found. Install with: pip install sphinx")
        return False

    return True


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

    print(f"✅ Created API index: {index_file}")


if __name__ == "__main__":
    print("🔧 Generating pySNT API Documentation")
    print("=" * 40)

    if generate_api_docs():
        create_api_index()
    else:
        print("\n❌ API documentation generation failed")
        sys.exit(1)
