#!/usr/bin/env python3
"""
Generate constants_index.rst from JSON stub files.

This script reads all JSON stub files and extracts static fields (constants),
then generates an alphabetical index with links to the class documentation.
"""

import json
from pathlib import Path
from typing import List, Tuple


def load_static_fields() -> List[Tuple[str, str, str, str]]:
    """
    Load all static fields from JSON stub files.
    
    Returns:
        List of tuples: (constant_name, class_name, java_type, documentation)
    """
    stubs_dir = Path('dev/scripts/STUBS')
    all_constants = []
    
    for json_file in stubs_dir.glob('*.json'):
        try:
            with open(json_file, 'r') as f:
                data = json.load(f)
            
            class_name = data.get('class_name', json_file.stem)
            static_fields = data.get('static_fields', [])
            
            for field in static_fields:
                constant_name = field.get('name', '')
                java_type = field.get('java_type', 'Object')
                documentation = field.get('documentation', '')
                
                all_constants.append((constant_name, class_name, java_type, documentation))
        
        except Exception as e:
            print(f"Warning: Failed to process {json_file}: {e}")
            continue
    
    return all_constants


def generate_constants_index(constants: List[Tuple[str, str, str, str]]) -> str:
    """
    Generate the constants_index.rst content.
    
    Args:
        constants: List of (constant_name, class_name, java_type, documentation)
    
    Returns:
        RST content as string
    """
    # Sort alphabetically by constant name
    constants.sort(key=lambda x: x[0].lower())
    
    content = f"""Constants Index
========================

This page provides an index of all public static fields (constants) available in the SNT API.

Total constants: **{len(constants)}** across **{len(set(c[1] for c in constants))}** classes.

"""
    
    # Group by first letter
    current_letter = None
    for constant_name, class_name, java_type, documentation in constants:
        first_letter = constant_name[0].upper()
        
        if first_letter != current_letter:
            current_letter = first_letter
            content += f"\n{current_letter}\n"
            content += "-" * len(current_letter) + "\n\n"
        
        # Create link to class documentation
        class_name_lower = class_name.lower()
        class_link = f"../pysnt/{class_name_lower}_doc.html"
        
        # Format: * ClassName.CONSTANT_NAME (type) - description
        content += f"* `{class_name}.{constant_name} <{class_link}>`_ (``{java_type}``) - {documentation}\n"
    
    # Add see also section
    content += """

See Also
--------

* :doc:`Method Index </api_auto/method_index>`
* :doc:`Class Index </api_auto/class_index>`
* :doc:`API Documentation </api_auto/index>`
"""
    
    return content


def main():
    """Main entry point."""
    print("Generating constants_index.rst...")
    
    # Load all static fields
    constants = load_static_fields()
    
    if not constants:
        print("Warning: No static fields found in JSON stubs.")
        print("Run: python dev/scripts/extract_class_signatures.py --all-classes")
        return 1
    
    print(f"Found {len(constants)} constants across {len(set(c[1] for c in constants))} classes")
    
    # Generate the index
    content = generate_constants_index(constants)
    
    # Write to file
    output_file = Path('docs/api_auto/constants_index.rst')
    output_file.write_text(content, encoding='utf-8')
    
    print(f"✅ Generated {output_file}")
    print(f"   Total constants: {len(constants)}")
    print(f"   Classes with constants: {len(set(c[1] for c in constants))}")
    
    # Show top classes by constant count
    class_counts = {}
    for _, class_name, _, _ in constants:
        class_counts[class_name] = class_counts.get(class_name, 0) + 1
    
    print("\nTop 5 classes by constant count:")
    for class_name, count in sorted(class_counts.items(), key=lambda x: -x[1])[:5]:
        print(f"  {class_name}: {count} constants")
    
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
