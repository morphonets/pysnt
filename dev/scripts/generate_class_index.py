#!/usr/bin/env python3
"""
Generate class_index.rst from class documentation files.

This script reads all *_doc.rst files in docs/pysnt/ and extracts class information,
then generates an alphabetical index with links to the class doc.
"""

import re
from pathlib import Path
from typing import List, Dict, Tuple


def load_class_info() -> List[Dict[str, str]]:
    """
    Load all class information from documentation files.
    
    Returns:
        List of dicts with class_name, filename, package, description
    """
    docs_dir = Path('docs/pysnt')
    all_classes = []
    
    for doc_file in docs_dir.glob('*_doc.rst'):
        try:
            with open(doc_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract class name from title like ``ClassName`` Class Documentation
            class_match = re.search(r'``(\w+)`` Class Documentation', content)
            if not class_match:
                continue
            
            class_name = class_match.group(1)
            filename = doc_file.stem.replace('_doc', '')
            
            # Extract package from **Package:** ``package.name``
            package_match = re.search(r'\*\*Package:\*\* ``([^`]+)``', content)
            package = package_match.group(1) if package_match else 'sc.fiji.snt'
            
            # Extract description (text after package line)
            desc_match = re.search(r'\*\*Package:\*\* ``[^`]+``\n\n(.+?)(?:\n\n|\nRelated|\nFields|\nMethods)', content, re.DOTALL)
            if desc_match:
                description = desc_match.group(1).strip()
                # Clean up - take first sentence
                description = description.split('.')[0] + '.' if '.' in description else description
                description = description.replace('\n', ' ').strip()
            else:
                description = ''
            
            all_classes.append({
                'name': class_name,
                'filename': filename,
                'package': package,
                'description': description
            })
        
        except Exception as e:
            print(f"Warning: Failed to process {doc_file}: {e}")
            continue
    
    return all_classes


def generate_class_index(classes: List[Dict[str, str]]) -> str:
    """
    Generate the class_index.rst content.
    
    Args:
        classes: List of class info dicts
    
    Returns:
        RST content as string
    """
    # Sort alphabetically by class name
    classes.sort(key=lambda x: x['name'].lower())
    
    content = f"""
Class Index
===========

This page provides an index of all classes available in the SNT API.

Total classes: **{len(classes)}**

"""
    
    # Group by first letter
    current_letter = None
    for cls in classes:
        first_letter = cls['name'][0].upper()
        
        if first_letter != current_letter:
            current_letter = first_letter
            content += f"\n{current_letter}\n"
            content += "-" * len(current_letter) + "\n\n"
        
        # Create link to class documentation
        class_link = f"../pysnt/{cls['filename']}_doc.html"
        
        # Format: * ClassName (package) - description
        content += f"* `{cls['name']} <{class_link}>`_ (``{cls['package']}``) - {cls['description']}\n"
    
    # Add see also section
    content += """

See Also
--------

* :doc:`Method Index </api_auto/method_index>`
* :doc:`Constants Index </api_auto/constants_index>`
* :doc:`API Documentation </api_auto/index>`
"""
    
    return content


def main():
    """Main entry point."""
    print("Generating class_index.rst...")
    
    # Load all class information
    classes = load_class_info()
    
    if not classes:
        print("Warning: No class documentation files found.")
        print("Expected files in: docs/pysnt/*_doc.rst")
        return 1
    
    print(f"Found {len(classes)} classes")
    
    # Generate the index
    content = generate_class_index(classes)
    
    # Write to file
    output_file = Path('docs/api_auto/class_index.rst')
    output_file.write_text(content, encoding='utf-8')
    
    print(f"✅ Generated {output_file}")
    print(f"   Total classes: {len(classes)}")
    
    # Show top packages by class count
    package_counts = {}
    for cls in classes:
        package = cls['package']
        package_counts[package] = package_counts.get(package, 0) + 1
    
    print("\nTop 5 packages by class count:")
    for package, count in sorted(package_counts.items(), key=lambda x: -x[1])[:5]:
        print(f"  {package}: {count} classes")
    
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
