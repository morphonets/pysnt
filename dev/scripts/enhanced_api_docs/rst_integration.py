"""
RST integration system for embedding enhanced Javadoc into existing auto-generated RST files.

This module provides tools to modify existing auto-generated RST files to include
enhanced JavaDoc information while preserving the existing autodoc structure.
"""

import json
import re
from pathlib import Path
from typing import Dict, List, Optional, Any

from .config import config
from .logging_setup import get_logger

logger = get_logger('rst_integration')


class RSTIntegrator:
    """Integrates enhanced JavaDoc information into existing RST files."""
    
    def __init__(self):
        """Initialize the RST integrator."""
        self.logger = logger
        self.api_auto_dir = config.project_root / "docs" / "api_auto"
        self.enhanced_json_dir = config.get_path('output.docs_dir') / 'enhanced_json'
        
        # Load enhanced JSON data
        self.enhanced_data = self._load_enhanced_json_data()
    
    def _load_enhanced_json_data(self) -> Dict[str, Any]:
        """Load enhanced JSON data for all classes."""
        enhanced_data = {}
        
        if not self.enhanced_json_dir.exists():
            self.logger.warning(f"Enhanced JSON directory not found: {self.enhanced_json_dir}")
            return enhanced_data
        
        for json_file in self.enhanced_json_dir.glob("*_enhanced.json"):
            try:
                with open(json_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                
                class_name = data.get('class_name', json_file.stem.replace('_enhanced', ''))
                enhanced_data[class_name] = data
                
            except Exception as e:
                self.logger.warning(f"Failed to load {json_file}: {e}")
        
        self.logger.info(f"Loaded enhanced data for {len(enhanced_data)} classes")
        return enhanced_data
    
    def integrate_rst_file(self, rst_file: Path, dry_run: bool = False) -> Dict[str, Any]:
        """
        Integrate enhanced JavaDoc information into an RST file.
        
        Args:
            rst_file: Path to the RST file to enhance
            dry_run: If True, don't modify files, just return what would be changed
            
        Returns:
            Dictionary with integration results
        """
        self.logger.info(f"Integrating JavaDoc into {rst_file}")
        
        try:
            # Read the RST file
            with open(rst_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Find automodule and autoclass directives
            integrations = []
            modified_content = content
            
            # Look for autoclass directives
            autoclass_pattern = r'^\.\. autoclass:: ([^\s]+)$'
            matches = re.finditer(autoclass_pattern, content, re.MULTILINE)
            
            for match in matches:
                full_class_name = match.group(1)
                class_name = full_class_name.split('.')[-1]  # Get just the class name
                
                if class_name in self.enhanced_data:
                    integration = self._create_javadoc_integration(
                        class_name,
                        full_class_name,
                        match,
                        content,
                        self.enhanced_data[class_name]
                    )
                    
                    if integration:
                        integrations.append(integration)
                        # Apply the integration
                        modified_content = modified_content.replace(
                            integration['original_section'],
                            integration['enhanced_section']
                        )
            
            # Write the enhanced content if not dry run
            if not dry_run and integrations:
                with open(rst_file, 'w', encoding='utf-8') as f:
                    f.write(modified_content)
                
                self.logger.info(f"Integrated JavaDoc for {len(integrations)} classes in {rst_file}")
            
            return {
                'file': str(rst_file),
                'integrations': len(integrations),
                'enhanced_classes': [i['class_name'] for i in integrations],
                'dry_run': dry_run
            }
            
        except Exception as e:
            self.logger.error(f"Failed to integrate {rst_file}: {e}")
            return {
                'file': str(rst_file),
                'error': str(e),
                'integrations': 0
            }
    
    def _create_javadoc_integration(self, class_name: str, full_class_name: str,
                                  match: re.Match, content: str, 
                                  enhanced_data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Create JavaDoc integration for a class."""
        
        # Find the autoclass directive and its options
        start_pos = match.start()
        lines = content[:start_pos].count('\\n')
        content_lines = content.split('\\n')
        
        # Find the end of the autoclass directive (next blank line or next directive)
        directive_start = lines
        directive_end = directive_start + 1
        
        # Look for directive options (lines starting with spaces and :)
        for i in range(directive_start + 1, len(content_lines)):
            line = content_lines[i]
            if line.strip() == '':
                directive_end = i
                break
            elif line.startswith('   :') or line.startswith('      '):
                directive_end = i + 1
            else:
                directive_end = i
                break
        
        # Extract the original section
        original_section = '\\n'.join(content_lines[directive_start:directive_end])
        
        # Create enhanced section
        enhanced_section = self._create_enhanced_autoclass_section(
            original_section,
            class_name,
            full_class_name,
            enhanced_data
        )
        
        return {
            'class_name': class_name,
            'full_class_name': full_class_name,
            'original_section': original_section,
            'enhanced_section': enhanced_section
        }
    
    def _create_enhanced_autoclass_section(self, original_section: str, class_name: str,
                                         full_class_name: str, enhanced_data: Dict[str, Any]) -> str:
        """Create an enhanced autoclass section with JavaDoc information."""
        
        lines = original_section.split('\\n')
        enhanced_lines = []
        
        # Add the original autoclass directive
        enhanced_lines.extend(lines)
        
        # Add enhanced JavaDoc information
        javadoc_description = enhanced_data.get('javadoc_description', '')
        methods = enhanced_data.get('methods', [])
        
        if javadoc_description or methods:
            enhanced_lines.append('')
            enhanced_lines.append('**Enhanced JavaDoc Information**')
            enhanced_lines.append('')
        
        # Add JavaDoc description
        if javadoc_description:
            enhanced_lines.append('**Description:**')
            enhanced_lines.append('')
            # Wrap long descriptions
            desc_lines = self._wrap_text(javadoc_description, 80)
            enhanced_lines.extend(desc_lines)
            enhanced_lines.append('')
        
        # Add key methods summary
        if methods:
            key_methods = self._select_key_methods(methods)
            if key_methods:
                enhanced_lines.append('**Key Methods:**')
                enhanced_lines.append('')
                
                for method in key_methods:
                    signature = self._get_method_signature(method)
                    description = method.get('javadoc_description', '')
                    if description:
                        description = description.split('.')[0] + '.'
                    
                    enhanced_lines.append(f'* ``{signature}`` - {description}')
                
                enhanced_lines.append('')
        
        # Add usage examples if available
        examples = self._get_class_examples(methods)
        if examples:
            enhanced_lines.append('**Usage Examples:**')
            enhanced_lines.append('')
            enhanced_lines.append('.. code-block:: python')
            enhanced_lines.append('')
            
            for example in examples:
                enhanced_lines.append(f'   {example}')
            
            enhanced_lines.append('')
        
        # Add JavaDoc link
        package = enhanced_data.get('package', 'sc.fiji.snt')
        javadoc_url = f"https://javadoc.scijava.org/SNT/index.html?{package.replace('.', '/')}/{class_name}.html"
        enhanced_lines.append(f'**JavaDoc:** `{class_name} JavaDoc <{javadoc_url}>`_')
        enhanced_lines.append('')
        
        return '\\n'.join(enhanced_lines)
    
    def _select_key_methods(self, methods: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Select key methods to highlight."""
        # Group by category
        categorized = {}
        for method in methods:
            category = method.get('category', 'Other')
            if category not in categorized:
                categorized[category] = []
            categorized[category].append(method)
        
        # Select key methods from important categories
        key_methods = []
        priority_categories = ['Analysis', 'I/O Operations', 'Visualization', 'Getters']
        
        for category in priority_categories:
            if category in categorized:
                # Take methods with JavaDoc descriptions first
                cat_methods = [m for m in categorized[category] if m.get('javadoc_description')]
                key_methods.extend(cat_methods[:2])  # Top 2 from each category
        
        return key_methods[:6]  # Limit to 6 total
    
    def _get_class_examples(self, methods: List[Dict[str, Any]]) -> List[str]:
        """Get usage examples for the class."""
        examples = []
        
        # Look for methods with examples
        for method in methods:
            method_examples = method.get('examples', [])
            if method_examples:
                examples.extend(method_examples[:2])  # Limit examples per method
                if len(examples) >= 3:  # Limit total examples
                    break
        
        return examples[:3]
    
    def _get_method_signature(self, method: Dict[str, Any]) -> str:
        """Get a clean method signature."""
        overloads = method.get('overloads', [])
        if overloads:
            signature = overloads[0].get('signature', '')
            if ' -> ' in signature:
                # Extract just the method part (before the return type)
                # The method_part already includes the closing parenthesis
                return signature.split(' -> ')[0]
            return signature
        
        return f"{method.get('name', '')}()"
    
    def _wrap_text(self, text: str, width: int) -> List[str]:
        """Wrap text to specified width."""
        words = text.split()
        lines = []
        current_line = []
        current_length = 0
        
        for word in words:
            if current_length + len(word) + 1 <= width:
                current_line.append(word)
                current_length += len(word) + 1
            else:
                if current_line:
                    lines.append(' '.join(current_line))
                current_line = [word]
                current_length = len(word)
        
        if current_line:
            lines.append(' '.join(current_line))
        
        return lines
    
    def integrate_all_rst_files(self, dry_run: bool = False) -> Dict[str, Any]:
        """Integrate JavaDoc information into all RST files."""
        results = {
            'files_processed': 0,
            'files_enhanced': 0,
            'total_integrations': 0,
            'enhanced_files': [],
            'errors': []
        }
        
        if not self.api_auto_dir.exists():
            self.logger.warning(f"API auto directory not found: {self.api_auto_dir}")
            return results
        
        # Find all RST files
        rst_files = list(self.api_auto_dir.rglob("*.rst"))
        
        for rst_file in rst_files:
            results['files_processed'] += 1
            
            try:
                file_result = self.integrate_rst_file(rst_file, dry_run)
                
                if file_result.get('integrations', 0) > 0:
                    results['files_enhanced'] += 1
                    results['total_integrations'] += file_result['integrations']
                    results['enhanced_files'].append(file_result)
                
                if 'error' in file_result:
                    results['errors'].append(file_result)
                    
            except Exception as e:
                self.logger.error(f"Error processing {rst_file}: {e}")
                results['errors'].append({
                    'file': str(rst_file),
                    'error': str(e)
                })
        
        self.logger.info(f"Integrated JavaDoc into {results['files_enhanced']} files with {results['total_integrations']} total integrations")
        return results


def main():
    """Main entry point for RST integration."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Integrate JavaDoc information into RST files')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be changed without modifying files')
    parser.add_argument('--file', type=Path, help='Integrate a specific file')
    parser.add_argument('--verbose', '-v', action='store_true', help='Enable verbose logging')
    
    args = parser.parse_args()
    
    if args.verbose:
        import logging
        logging.getLogger('rst_integration').setLevel(logging.DEBUG)
    
    integrator = RSTIntegrator()
    
    if args.file:
        result = integrator.integrate_rst_file(args.file, args.dry_run)
        print(f"Integrated JavaDoc for {result.get('integrations', 0)} classes in {args.file}")
    else:
        results = integrator.integrate_all_rst_files(args.dry_run)
        print(f"Processed {results['files_processed']} files")
        print(f"Enhanced {results['files_enhanced']} files with {results['total_integrations']} total integrations")
        
        if results['errors']:
            print(f"Encountered {len(results['errors'])} errors")


if __name__ == "__main__":
    main()