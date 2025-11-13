"""
Integration manager for embedding JavaDoc into existing API documentation.

This module coordinates different integration strategies and provides a unified
interface for embedding Javadoc information into existing documentation.
"""

from enum import Enum
from typing import Dict, List, Optional, Any

from .config import config
from .docstring_enhancer import DocstringEnhancer
from .logging_setup import get_logger
from .rst_integration import RSTIntegrator

logger = get_logger('integration_manager')


class IntegrationStrategy(Enum):
    """Available integration strategies."""
    DOCSTRING = "docstring"  # Modify Python docstrings directly
    RST_INJECTION = "rst_injection"  # Inject into existing RST files
    SPHINX_EXTENSION = "sphinx_extension"  # Use Sphinx extension
    HYBRID = "hybrid"  # Combination of strategies


class IntegrationManager:
    """Manages the integration of enhanced JavaDoc into existing documentation."""
    
    def __init__(self):
        """Initialize the integration manager."""
        self.logger = logger
        self.docstring_enhancer = DocstringEnhancer()
        self.rst_integrator = RSTIntegrator()
        
        # Integration results
        self.results = {
            'strategy': None,
            'docstring_results': {},
            'rst_results': {},
            'sphinx_results': {},
            'overall_success': False,
            'summary': {}
        }
    
    def integrate_enhanced_javadoc(self, 
                                 strategy: IntegrationStrategy = IntegrationStrategy.HYBRID,
                                 dry_run: bool = False,
                                 options: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Integrate enhanced JavaDoc using the specified strategy.
        
        Args:
            strategy: Integration strategy to use
            dry_run: If True, show what would be done without making changes
            options: Additional options for integration
            
        Returns:
            Dictionary with integration results
        """
        self.logger.info(f"Starting JavaDoc integration using {strategy.value} strategy")
        
        options = options or {}
        self.results['strategy'] = strategy.value
        
        try:
            if strategy == IntegrationStrategy.DOCSTRING:
                return self._integrate_docstring_only(dry_run, options)
            
            elif strategy == IntegrationStrategy.RST_INJECTION:
                return self._integrate_rst_only(dry_run, options)
            
            elif strategy == IntegrationStrategy.SPHINX_EXTENSION:
                return self._integrate_sphinx_extension(dry_run, options)
            
            elif strategy == IntegrationStrategy.HYBRID:
                return self._integrate_hybrid(dry_run, options)
            
            else:
                raise ValueError(f"Unknown integration strategy: {strategy}")
                
        except Exception as e:
            self.logger.error(f"Integration failed: {e}")
            self.results['error'] = str(e)
            self.results['overall_success'] = False
            return self.results
    
    def _integrate_docstring_only(self, dry_run: bool, options: Dict[str, Any]) -> Dict[str, Any]:
        """Integrate using docstring enhancement only."""
        self.logger.info("Integrating using docstring enhancement strategy")
        
        # Enhance Python docstrings
        docstring_results = self.docstring_enhancer.enhance_all_python_files(dry_run)
        self.results['docstring_results'] = docstring_results
        
        # Determine success
        success = docstring_results.get('files_enhanced', 0) > 0
        self.results['overall_success'] = success
        
        # Create summary
        self.results['summary'] = {
            'strategy': 'Docstring Enhancement',
            'files_processed': docstring_results.get('files_processed', 0),
            'files_enhanced': docstring_results.get('files_enhanced', 0),
            'total_enhancements': docstring_results.get('total_enhancements', 0),
            'errors': len(docstring_results.get('errors', [])),
            'success': success
        }
        
        return self.results
    
    def _integrate_rst_only(self, dry_run: bool, options: Dict[str, Any]) -> Dict[str, Any]:
        """Integrate using RST injection only."""
        self.logger.info("Integrating using RST injection strategy")
        
        # Integrate into RST files
        rst_results = self.rst_integrator.integrate_all_rst_files(dry_run)
        self.results['rst_results'] = rst_results
        
        # Determine success
        success = rst_results.get('files_enhanced', 0) > 0
        self.results['overall_success'] = success
        
        # Create summary
        self.results['summary'] = {
            'strategy': 'RST Injection',
            'files_processed': rst_results.get('files_processed', 0),
            'files_enhanced': rst_results.get('files_enhanced', 0),
            'total_integrations': rst_results.get('total_integrations', 0),
            'errors': len(rst_results.get('errors', [])),
            'success': success
        }
        
        return self.results
    
    def _integrate_sphinx_extension(self, dry_run: bool, options: Dict[str, Any]) -> Dict[str, Any]:
        """Integrate using Sphinx extension."""
        self.logger.info("Integrating using Sphinx extension strategy")
        
        # Setup Sphinx extension
        sphinx_results = self._setup_sphinx_extension(dry_run)
        self.results['sphinx_results'] = sphinx_results
        
        # Determine success
        success = sphinx_results.get('extension_configured', False)
        self.results['overall_success'] = success
        
        # Create summary
        self.results['summary'] = {
            'strategy': 'Sphinx Extension',
            'extension_configured': sphinx_results.get('extension_configured', False),
            'conf_py_updated': sphinx_results.get('conf_py_updated', False),
            'success': success
        }
        
        return self.results
    
    def _integrate_hybrid(self, dry_run: bool, options: Dict[str, Any]) -> Dict[str, Any]:
        """Integrate using hybrid strategy (combination of approaches)."""
        self.logger.info("Integrating using hybrid strategy")
        
        # Strategy 1: Enhance key Python docstrings (for most important classes)
        key_classes = options.get('key_classes', ['Path', 'Tree', 'SNT', 'PathAndFillManager'])
        docstring_results = self._enhance_key_docstrings(key_classes, dry_run)
        self.results['docstring_results'] = docstring_results
        
        # Strategy 2: Setup Sphinx extension for automatic enhancement
        sphinx_results = self._setup_sphinx_extension(dry_run)
        self.results['sphinx_results'] = sphinx_results
        
        # Strategy 3: Create enhanced API reference pages
        enhanced_pages_results = self._create_enhanced_reference_pages(dry_run)
        self.results['enhanced_pages_results'] = enhanced_pages_results
        
        # Determine overall success
        docstring_success = docstring_results.get('files_enhanced', 0) > 0
        sphinx_success = sphinx_results.get('extension_configured', False)
        pages_success = enhanced_pages_results.get('pages_created', 0) > 0
        
        overall_success = docstring_success or sphinx_success or pages_success
        self.results['overall_success'] = overall_success
        
        # Create comprehensive summary
        self.results['summary'] = {
            'strategy': 'Hybrid Integration',
            'docstring_enhancements': docstring_results.get('total_enhancements', 0),
            'sphinx_extension_configured': sphinx_success,
            'enhanced_pages_created': enhanced_pages_results.get('pages_created', 0),
            'total_files_modified': (
                docstring_results.get('files_enhanced', 0) + 
                enhanced_pages_results.get('pages_created', 0)
            ),
            'errors': (
                len(docstring_results.get('errors', [])) + 
                len(sphinx_results.get('errors', [])) +
                len(enhanced_pages_results.get('errors', []))
            ),
            'success': overall_success
        }
        
        return self.results
    
    def _enhance_key_docstrings(self, key_classes: List[str], dry_run: bool) -> Dict[str, Any]:
        """Enhance docstrings for key classes only."""
        self.logger.info(f"Enhancing docstrings for key classes: {key_classes}")
        
        # Find Python files containing key classes
        src_dir = config.project_root / "src"
        results = {
            'files_processed': 0,
            'files_enhanced': 0,
            'total_enhancements': 0,
            'enhanced_files': [],
            'errors': []
        }
        
        for python_file in src_dir.rglob("*.py"):
            if '__pycache__' in str(python_file):
                continue
            
            # Check if file contains any key classes
            try:
                with open(python_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                contains_key_class = any(f"class {cls}" in content for cls in key_classes)
                
                if contains_key_class:
                    results['files_processed'] += 1
                    file_result = self.docstring_enhancer.enhance_python_file(python_file, dry_run)
                    
                    if file_result.get('enhancements', 0) > 0:
                        results['files_enhanced'] += 1
                        results['total_enhancements'] += file_result['enhancements']
                        results['enhanced_files'].append(file_result)
                    
                    if 'error' in file_result:
                        results['errors'].append(file_result)
                        
            except Exception as e:
                self.logger.warning(f"Error checking {python_file}: {e}")
        
        return results
    
    def _setup_sphinx_extension(self, dry_run: bool) -> Dict[str, Any]:
        """Setup the Sphinx extension for automatic JavaDoc integration."""
        results = {
            'extension_configured': False,
            'conf_py_updated': False,
            'errors': []
        }
        
        try:
            # Update conf.py to include the extension
            docs_dir = config.project_root / "docs"
            conf_py = docs_dir / "conf.py"
            
            if not conf_py.exists():
                results['errors'].append("conf.py not found")
                return results
            
            # Read conf.py
            with open(conf_py, 'r', encoding='utf-8') as f:
                conf_content = f.read()
            
            # Check if extension is already configured
            extension_import = "sys.path.insert(0, os.path.abspath('../dev/scripts'))"
            extension_name = "'enhanced_api_docs.sphinx_javadoc_extension'"
            
            needs_path_update = extension_import not in conf_content
            needs_extension_update = extension_name not in conf_content
            
            if needs_path_update or needs_extension_update:
                if not dry_run:
                    # Add path if needed
                    if needs_path_update:
                        # Find where sys is imported or add it
                        if "import sys" in conf_content:
                            conf_content = conf_content.replace(
                                "import sys",
                                f"import sys\\n{extension_import}"
                            )
                        else:
                            conf_content = f"import sys\\n{extension_import}\\n\\n{conf_content}"
                    
                    # Add extension if needed
                    if needs_extension_update:
                        # Find extensions list and add our extension
                        extensions_pattern = r"extensions = \[(.*?)\]"
                        import re
                        match = re.search(extensions_pattern, conf_content, re.DOTALL)
                        
                        if match:
                            extensions_content = match.group(1)
                            if extension_name not in extensions_content:
                                new_extensions = extensions_content.rstrip() + f",\\n    {extension_name}"
                                conf_content = conf_content.replace(
                                    f"extensions = [{extensions_content}]",
                                    f"extensions = [{new_extensions}]"
                                )
                    
                    # Write updated conf.py
                    with open(conf_py, 'w', encoding='utf-8') as f:
                        f.write(conf_content)
                
                results['conf_py_updated'] = True
            
            results['extension_configured'] = True
            
        except Exception as e:
            self.logger.error(f"Failed to setup Sphinx extension: {e}")
            results['errors'].append(str(e))
        
        return results
    
    def _create_enhanced_reference_pages(self, dry_run: bool) -> Dict[str, Any]:
        """Create enhanced API reference pages that link to existing autodoc."""
        results = {
            'pages_created': 0,
            'errors': []
        }
        
        try:
            docs_dir = config.project_root / "docs"
            enhanced_ref_dir = docs_dir / "api_enhanced_ref"
            
            if not dry_run:
                enhanced_ref_dir.mkdir(exist_ok=True)
            
            # Create enhanced reference pages for key classes
            enhanced_data = self.docstring_enhancer.enhanced_data
            
            for class_name, class_data in enhanced_data.items():
                if not dry_run:
                    ref_page = self._create_enhanced_reference_page(class_name, class_data)
                    ref_file = enhanced_ref_dir / f"{class_name.lower()}_enhanced.rst"
                    
                    with open(ref_file, 'w', encoding='utf-8') as f:
                        f.write(ref_page)
                
                results['pages_created'] += 1
            
            # Create index page
            if not dry_run and results['pages_created'] > 0:
                index_page = self._create_enhanced_reference_index(enhanced_data.keys())
                index_file = enhanced_ref_dir / "index.rst"
                
                with open(index_file, 'w', encoding='utf-8') as f:
                    f.write(index_page)
        
        except Exception as e:
            self.logger.error(f"Failed to create enhanced reference pages: {e}")
            results['errors'].append(str(e))
        
        return results
    
    def _create_enhanced_reference_page(self, class_name: str, class_data: Dict[str, Any]) -> str:
        """Create an enhanced reference page for a class."""
        package = class_data.get('package', 'sc.fiji.snt')
        javadoc_desc = class_data.get('javadoc_description', '')
        methods = class_data.get('methods', [])
        
        content = f"""
{class_name} Enhanced Reference
{'=' * (len(class_name) + 19)}

This page provides enhanced documentation for the ``{class_name}`` class with JavaDoc integration.

JavaDoc Description
-------------------

{javadoc_desc if javadoc_desc else 'No JavaDoc description available.'}

Auto-Generated Documentation
----------------------------

For complete method signatures and Python-specific documentation:

.. autoclass:: pysnt.{package.split('.')[-1] if '.' in package else package}.{class_name}
   :members:
   :show-inheritance:

Enhanced Method Information
---------------------------

"""
        
        # Add method categories
        categorized_methods = {}
        for method in methods:
            category = method.get('category', 'Other')
            if category not in categorized_methods:
                categorized_methods[category] = []
            categorized_methods[category].append(method)
        
        for category, cat_methods in categorized_methods.items():
            if not cat_methods:
                continue
                
            content += f"""
{category} Methods
{'^' * (len(category) + 8)}

"""
            
            for method in cat_methods[:5]:  # Limit methods per category
                method_name = method.get('name', '')
                javadoc_desc = method.get('javadoc_description', '')
                
                if javadoc_desc:
                    content += f"**{method_name}**\n   {javadoc_desc}\n\n"
        
        # Add JavaDoc link
        javadoc_url = f"https://javadoc.scijava.org/SNT/index.html?{package.replace('.', '/')}/{class_name}.html"
        content += f"""
JavaDoc Reference
-----------------

For complete JavaDoc documentation: `{class_name} JavaDoc <{javadoc_url}>`_
"""
        
        return content
    
    def _create_enhanced_reference_index(self, class_names: List[str]) -> str:
        """Create index page for enhanced references."""
        content = """
Enhanced API Reference
======================

This section provides enhanced API documentation that combines Python autodoc 
with JavaDoc information for better understanding of SNT classes.

.. toctree::
   :maxdepth: 1
   :caption: Enhanced Class References:

"""
        
        for class_name in sorted(class_names):
            content += f"   {class_name.lower()}_enhanced\n"
        
        content += """

About Enhanced References
-------------------------

These pages combine:

* **Python autodoc**: Complete method signatures and Python-specific documentation
* **JavaDoc descriptions**: Rich descriptions from the original Java documentation  
* **Method categorization**: Methods organized by functionality
* **Usage examples**: Code examples where available

For the standard auto-generated API documentation, see :doc:`../api_auto/index`.
"""
        
        return content
    
    def get_integration_recommendations(self) -> Dict[str, Any]:
        """Get recommendations for the best integration strategy."""
        recommendations = {
            'recommended_strategy': IntegrationStrategy.HYBRID,
            'reasons': [],
            'considerations': [],
            'next_steps': []
        }
        
        # Analyze current state
        has_enhanced_data = len(self.docstring_enhancer.enhanced_data) > 0
        has_autodoc_files = (config.project_root / "docs" / "api_auto").exists()
        
        if not has_enhanced_data:
            recommendations['recommended_strategy'] = None
            recommendations['reasons'].append("No enhanced JavaDoc data available - run generation first")
            return recommendations
        
        # Hybrid strategy is usually best
        recommendations['reasons'].extend([
            "Hybrid approach provides multiple access points to enhanced information",
            "Preserves existing autodoc structure while adding JavaDoc richness",
            "Sphinx extension provides automatic integration for future updates",
            "Enhanced reference pages offer focused JavaDoc-centric views"
        ])
        
        recommendations['considerations'].extend([
            "Docstring modifications will change source files",
            "Sphinx extension requires conf.py updates",
            "Enhanced reference pages create additional documentation to maintain"
        ])
        
        recommendations['next_steps'].extend([
            "Run integration with hybrid strategy",
            "Review enhanced docstrings in key classes",
            "Test Sphinx extension functionality",
            "Update main documentation index to reference enhanced pages"
        ])
        
        return recommendations


def main():
    """Main entry point for integration management."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Manage JavaDoc integration into existing API documentation')
    parser.add_argument('--strategy', 
                       choices=['docstring', 'rst_injection', 'sphinx_extension', 'hybrid'],
                       default='hybrid',
                       help='Integration strategy to use')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be done without making changes')
    parser.add_argument('--recommendations', action='store_true', help='Show integration recommendations')
    parser.add_argument('--verbose', '-v', action='store_true', help='Enable verbose logging')
    
    args = parser.parse_args()
    
    if args.verbose:
        import logging
        logging.getLogger('integration_manager').setLevel(logging.DEBUG)
    
    manager = IntegrationManager()
    
    if args.recommendations:
        recommendations = manager.get_integration_recommendations()
        print("Integration Recommendations:")
        print(f"Recommended Strategy: {recommendations['recommended_strategy']}")
        print("\\nReasons:")
        for reason in recommendations['reasons']:
            print(f"  - {reason}")
        print("\\nConsiderations:")
        for consideration in recommendations['considerations']:
            print(f"  - {consideration}")
        print("\\nNext Steps:")
        for step in recommendations['next_steps']:
            print(f"  - {step}")
    else:
        strategy = IntegrationStrategy(args.strategy)
        results = manager.integrate_enhanced_javadoc(strategy, args.dry_run)
        
        summary = results.get('summary', {})
        print(f"Integration Results ({summary.get('strategy', 'Unknown')}):")
        print(f"Success: {summary.get('success', False)}")
        
        for key, value in summary.items():
            if key not in ['strategy', 'success']:
                print(f"{key.replace('_', ' ').title()}: {value}")


if __name__ == "__main__":
    main()