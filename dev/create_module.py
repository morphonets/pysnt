#!/usr/bin/env python3
"""
Quick setup script for creating new PySNT modules.

This script automates the process of creating a new PySNT module from the template.

Usage:
    python dev/create_module.py analysis.morphology
    python dev/create_module.py util.advanced
    python dev/create_module.py tracing.algorithms
"""

import argparse
import sys
from pathlib import Path


def create_module(module_path: str, curated_classes: list = None, extended_classes: list = None):
    """
    Create a new PySNT module from the template.
    
    Args:
        module_path: Module path like "analysis.morphology" or "util.advanced"
        curated_classes: List of curated class names
        extended_classes: List of extended class names
    """
    
    # Parse module path
    parts = module_path.split('.')
    if len(parts) < 2:
        print("❌ Module path must have at least 2 parts (e.g., 'analysis.morphology')")
        return False
    
    # Determine paths
    project_root = Path(__file__).parent.parent
    template_path = project_root / "dev" / "placeholder_template.py"
    
    # Create module directory
    module_dir = project_root / "src" / "pysnt"
    for part in parts:
        module_dir = module_dir / part
    
    module_file = module_dir / "__init__.py"
    
    # Check if module already exists
    if module_file.exists():
        print(f"❌ Module already exists: {module_file}")
        return False
    
    # Create directory
    module_dir.mkdir(parents=True, exist_ok=True)
    print(f"📁 Created directory: {module_dir}")
    
    # Read template
    if not template_path.exists():
        print(f"❌ Template not found: {template_path}")
        return False
    
    template_content = template_path.read_text()
    
    # Configure template
    java_package_path = "/".join(parts)  # For URLs and paths
    java_package_dotted = ".".join(parts)  # For Java package names
    python_module_path = ".".join(parts)
    module_name = parts[-1]
    
    # Replace placeholders - order matters!
    configured_content = template_content.replace(
        '"sc.fiji.snt.[PACKAGE_PATH]"', f'"sc.fiji.snt.{java_package_dotted}"'  # Java package names (with dots)
    ).replace(
        "[PACKAGE_PATH]", java_package_path  # URLs and paths (with slashes)
    ).replace(
        "[MODULE_NAME]", module_name
    ).replace(
        "[MODULE_PATH]", python_module_path
    ).replace(
        "pysnt.[MODULE_PATH]", f"pysnt.{python_module_path}"
    )
    
    # Update class lists if provided
    if curated_classes:
        curated_str = '[\n    "' + '",\n    "'.join(curated_classes) + '"\n]'
        # Find and replace the CURATED_CLASSES section
        import re
        pattern = r'CURATED_CLASSES = \[\s*# Add your most important classes here.*?\]'
        replacement = f'CURATED_CLASSES = {curated_str}'
        configured_content = re.sub(pattern, replacement, configured_content, flags=re.DOTALL)
    
    if extended_classes:
        extended_str = '[\n    "' + '",\n    "'.join(extended_classes) + '"\n]'
        # Find and replace the EXTENDED_CLASSES section
        import re
        pattern = r'EXTENDED_CLASSES = \[\s*# Add your extended classes here.*?\]'
        replacement = f'EXTENDED_CLASSES = {extended_str}'
        configured_content = re.sub(pattern, replacement, configured_content, flags=re.DOTALL)
    
    # Adjust import path based on depth
    if len(parts) == 2:
        # Direct submodule (e.g., analysis.morphology)
        import_path = "..common_module"
    elif len(parts) == 3:
        # Nested submodule (e.g., analysis.sholl.gui)
        import_path = "...common_module"
    else:
        # Deeper nesting
        import_path = "." + "." * len(parts) + "common_module"
    
    configured_content = configured_content.replace(
        "from ..common_module import setup_module_classes  # Adjust import depth based on module location",
        f"from {import_path} import setup_module_classes"
    )
    
    # Write configured template
    module_file.write_text(configured_content)
    print(f"📝 Created module: {module_file}")
    
    # Show next steps
    print(f"\n✅ Module '{module_path}' created successfully!")
    print("\n📋 Next steps:")
    print(f"1. Edit {module_file}")
    print("   - Update CURATED_CLASSES and EXTENDED_CLASSES")
    print("   - Remove the template checklist section")
    print(f"2. Test: python -c \"import src.pysnt.{python_module_path}; print('Success!')\"")
    print("3. Run quality control: python dev/scripts/pysnt_utils.py --qc")

    return True


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Create a new PySNT module from template",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python dev/create_module.py analysis.morphology
  python dev/create_module.py util.advanced
  python dev/create_module.py tracing.algorithms
  
  # With predefined classes
  python dev/create_module.py analysis.morphology \\
    --curated MorphologyAnalyzer ShapeMetrics \\
    --extended AdvancedMorphology DetailedMetrics
        """
    )
    
    parser.add_argument(
        "module_path",
        help="Module path (e.g., 'analysis.morphology', 'util.advanced')"
    )
    
    parser.add_argument(
        "--curated",
        nargs="*",
        help="Curated class names"
    )
    
    parser.add_argument(
        "--extended", 
        nargs="*",
        help="Extended class names"
    )
    
    args = parser.parse_args()
    
    # Validate module path
    if not args.module_path or "." not in args.module_path:
        print("❌ Invalid module path. Use format like 'analysis.morphology'")
        return 1
    
    # Create module
    success = create_module(
        args.module_path,
        curated_classes=args.curated,
        extended_classes=args.extended
    )
    
    return 0 if success else 1


if __name__ == "__main__":
    exit(main())