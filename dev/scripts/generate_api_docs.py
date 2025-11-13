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
    project_root = script_dir.parent.parent  # Go up two levels: scripts -> dev -> project_root
    docs_dir = project_root / "docs"
    src_dir = project_root / "src"
    api_dir = docs_dir / "api_auto"

    # Create API directory (with parents if needed)
    api_dir.mkdir(parents=True, exist_ok=True)

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
    project_root = script_dir.parent.parent  # Go up two levels: scripts -> dev -> project_root
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
    """Create method_index, class_index, and constants_index files."""

    script_dir = Path(__file__).parent
    project_root = script_dir.parent.parent  # Go up two levels: scripts -> dev -> project_root
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
   :hidden:
   pysnt*

"""

    with open(index_file, 'w') as f:
        f.write(content)

    print(f"Created API index: {index_file}")


def generate_class_and_constants_indexes():
    """Generate class and constants indexes after enhanced docs are created."""
    script_dir = Path(__file__).parent
    
    # Generate class index from documentation files
    print("\nGenerating class index...")
    try:
        generate_class_script = script_dir / "generate_class_index.py"
        if generate_class_script.exists():
            result = subprocess.run(
                [sys.executable, str(generate_class_script)],
                capture_output=True,
                text=True,
                check=True
            )
            print(result.stdout)
        else:
            print(f"⚠️  Class index generator not found: {generate_class_script}")
    except subprocess.CalledProcessError as e:
        print(f"⚠️  Failed to generate class index: {e}")
        if e.stdout:
            print(e.stdout)
        if e.stderr:
            print(e.stderr)
    except Exception as e:
        print(f"⚠️  Error generating class index: {e}")
    
    # Generate constants index from JSON stubs
    print("\nGenerating constants index...")
    try:
        generate_constants_script = script_dir / "generate_constants_index.py"
        if generate_constants_script.exists():
            result = subprocess.run(
                [sys.executable, str(generate_constants_script)],
                capture_output=True,
                text=True,
                check=True
            )
            print(result.stdout)
        else:
            print(f"⚠️  Constants index generator not found: {generate_constants_script}")
    except subprocess.CalledProcessError as e:
        print(f"⚠️  Failed to generate constants index: {e}")
        if e.stdout:
            print(e.stdout)
        if e.stderr:
            print(e.stderr)
    except Exception as e:
        print(f"⚠️  Error generating constants index: {e}")


def generate_enhanced_api_docs():
    """Generate enhanced API documentation if available."""
    try:
        # Try to import enhanced API documentation system
        from enhanced_api_docs.orchestrator import DocumentationOrchestrator
        from enhanced_api_docs.config import config
        
        print("\n" + "=" * 60)
        print("ENHANCED API DOCUMENTATION GENERATION")
        print("=" * 60)
        
        # Validate prerequisites
        if not config.validate():
            print("⚠ Enhanced API docs prerequisites not met")
            print("  Missing JavaDoc ZIP or JSON stubs")
            print("  This is optional - standard docs will still be generated")
            return False
        
        # Initialize orchestrator
        orchestrator = DocumentationOrchestrator(
            dry_run=False,
            show_progress=True,
            verbose=0
        )
        
        # Configure generation options
        generation_options = {
            'force': False,  # Use incremental updates for speed
            'incremental': True,
            'components': ['json', 'rst', 'index', 'sphinx'],
            'classes': None,  # Process all classes
            'output_format': 'rst',
            'validate_after': True,
            'toctree_enabled': True,
            'toctree_maxdepth': 3
        }
        
        print("\n🚀 Starting enhanced API documentation generation...")
        print("   Components: JSON enhancement, RST generation, Method index, Sphinx integration")
        
        # Run generation
        success, results = orchestrator.generate_documentation(generation_options)
        
        # Report results
        stats = results.get('statistics', {})
        
        print("\n" + "=" * 60)
        print("ENHANCED API DOCUMENTATION SUMMARY")
        print("=" * 60)
        
        if success:
            print("✓ Enhanced API documentation generated successfully")
            print(f"\n📊 Statistics:")
            print(f"  • Classes processed: {stats.get('classes_processed', 0)}")
            print(f"  • Methods documented: {stats.get('methods_documented', 0)}")
            print(f"  • Files generated: {stats.get('files_generated', 0)}")
            
            if stats.get('errors', 0) > 0:
                print(f"  ⚠ Errors: {stats.get('errors', 0)}")
            if stats.get('warnings', 0) > 0:
                print(f"  ⚠ Warnings: {stats.get('warnings', 0)}")
            
            elapsed = stats.get('end_time', 0) - stats.get('start_time', 0)
            if elapsed > 0:
                print(f"  ⏱ Time: {elapsed:.2f}s")
            
            print("\n📁 Generated:")
            print("  • Enhanced class docstrings in src/pysnt/__init__.py")
            print("  • Detailed documentation files in docs/pysnt/*_doc.rst")
            print("  • Alphabetical method index at docs/_build/html/method_index.html")
            print("  • Class index at docs/_build/html/class_index.html")
            print("  • Constants index at docs/_build/html/constants_index.html")
            
            return True
        else:
            print("✗ Enhanced API documentation generation failed")
            issues = results.get('issues', [])
            if issues:
                print(f"\n⚠ Issues encountered ({len(issues)}):")
                for issue in issues[:5]:
                    print(f"  • {issue}")
                if len(issues) > 5:
                    print(f"  ... and {len(issues) - 5} more issues")
            return False
            
    except ImportError as e:
        print("\n⚠ Enhanced API documentation system not available")
        print(f"  Import error: {e}")
        print("  This is optional - standard docs will still be generated")
        return False
    except Exception as e:
        print(f"\n⚠ Enhanced API documentation generation failed: {e}")
        import traceback
        print("\nTraceback:")
        traceback.print_exc()
        return False


if __name__ == "__main__":
    print("Generating pySNT API Documentation")
    print("=" * 40)

    # First fix the Javadoc links to make them unique
    print("\nFixing Javadoc link references...")
    fix_javadoc_links()

    # Then generate the standard API docs
    print("\nGenerating standard API documentation...")
    standard_success = False
    if generate_api_docs():
        create_api_index()
        standard_success = True
    else:
        print("\nStandard API documentation generation failed")

    # Try to generate enhanced API documentation
    enhanced_success = generate_enhanced_api_docs()
    
    # Generate class and constants indexes after enhanced docs
    if enhanced_success:
        generate_class_and_constants_indexes()
    
    # Report final status
    print("\n" + "=" * 40)
    print("API DOCUMENTATION GENERATION SUMMARY")
    print("=" * 40)
    
    if standard_success:
        print("✓ Standard API documentation: SUCCESS")
    else:
        print("✗ Standard API documentation: FAILED")
    
    if enhanced_success:
        print("✓ Enhanced API documentation: SUCCESS")
    else:
        print("⚠ Enhanced API documentation: UNAVAILABLE/FAILED")
    
    # Exit with error only if standard docs failed
    if not standard_success:
        print("\nCritical: Standard API documentation generation failed")
        sys.exit(1)
    else:
        print("\nAPI documentation generation completed")
        if not enhanced_success:
            print("Note: Enhanced features not available - this is optional")
        sys.exit(0)
