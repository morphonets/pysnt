"""
Main orchestration system for the enhanced API documentation generation.
"""

import time
from pathlib import Path
from typing import Dict, Any, List, Optional, Tuple
import json

from .config import config
from .logging_setup import get_logger
from .javadoc_extractor import JavaDocExtractor
from .json_stub_reader import JSONStubReader
from .json_enhancer import JSONStubEnhancer
from .javadoc_parser import JavaDocHTMLParser
from .rst_generator import SphinxRSTGenerator
from .comprehensive_method_index import ComprehensiveMethodIndexSystem
from .structured_integration import StructuredIntegrationManager


class DocumentationOrchestrator:
    """Main orchestrator for enhanced API documentation generation."""
    
    def __init__(self, dry_run: bool = False, show_progress: bool = True, verbose: int = 0):
        """Initialize the orchestrator."""
        self.dry_run = dry_run
        self.show_progress = show_progress
        self.verbose = verbose
        self.logger = get_logger('orchestrator')
        
        # Initialize components
        self.javadoc_extractor = JavaDocExtractor()
        self.json_reader = JSONStubReader()
        self.json_enhancer = JSONStubEnhancer()
        self.rst_generator = SphinxRSTGenerator()
        self.method_index_system = ComprehensiveMethodIndexSystem()
        self.structured_integration = StructuredIntegrationManager()
        
        # Track generation state
        self.generation_stats = {
            'classes_processed': 0,
            'methods_documented': 0,
            'files_generated': 0,
            'errors': 0,
            'warnings': 0,
            'start_time': None,
            'end_time': None
        }
        
        self.generated_files = {
            'class_pages': [],
            'index_files': [],
            'enhanced_json': [],
            'sphinx_integration': []
        }
        
        self.issues = []
    
    def generate_documentation(self, options: Dict[str, Any]) -> Tuple[bool, Dict[str, Any]]:
        """
        Generate enhanced API documentation with specified options.
        
        Args:
            options: Generation options including:
                - force: Force regeneration of all files
                - incremental: Only process changed files
                - components: List of components to generate
                - classes: List of specific classes to process
                - output_format: Output format ('rst', 'markdown', 'both')
                - validate_after: Whether to validate after generation
        
        Returns:
            Tuple of (success, results_dict)
        """
        self.generation_stats['start_time'] = time.time()
        
        try:
            self.logger.info("Starting documentation generation orchestration")
            
            # Step 1: Validate prerequisites
            if not self._validate_prerequisites():
                return False, self._get_results()
            
            # Step 2: Extract JavaDoc if needed
            if not self._ensure_javadoc_extracted(options.get('force', False)):
                return False, self._get_results()
            
            # Step 3: Load and validate JSON stubs
            json_stubs = self._load_json_stubs(options.get('classes'))
            if not json_stubs:
                return False, self._get_results()
            
            # Step 4: Parse JavaDoc documentation
            javadoc_data = self._parse_javadoc_documentation(options.get('classes'))
            
            # Step 5: Enhance JSON stubs with JavaDoc data
            enhanced_stubs = self._enhance_json_stubs(json_stubs, javadoc_data, options)
            
            # Step 6: Generate documentation components
            components = options.get('components')
            if components is None:
                components = ['javadoc', 'json', 'rst', 'index', 'sphinx']
            self.logger.info(f"Components to generate: {components}")
            
            if 'json' in components:
                self.logger.info("Starting JSON file generation...")
                self._generate_enhanced_json_files(enhanced_stubs, options)
                self.logger.info("✓ JSON file generation completed")
            
            if 'rst' in components:
                self.logger.info("Starting RST documentation generation...")
                self._generate_rst_documentation(enhanced_stubs, options)
                self.logger.info("✓ RST documentation generation completed")
            
            if 'index' in components:
                self.logger.info("Starting method index generation...")
                self._generate_method_index(enhanced_stubs, options)
                self.logger.info("✓ Method index generation completed")
            
            if 'sphinx' in components:
                self.logger.info("Starting Sphinx integration...")
                self._integrate_with_sphinx(options)
                self.logger.info("✓ Sphinx integration completed")
            
            # Step 7: Validate generated documentation
            if options.get('validate_after', True):
                self._validate_generated_documentation()
            
            self.generation_stats['end_time'] = time.time()
            
            success = self.generation_stats['errors'] == 0
            self.logger.info(f"Documentation generation {'completed' if success else 'failed'}")
            
            return success, self._get_results()
            
        except Exception as e:
            self.logger.error(f"Documentation generation failed: {e}")
            self.generation_stats['errors'] += 1
            self.issues.append(f"Generation failed: {e}")
            return False, self._get_results()
    
    def _validate_prerequisites(self) -> bool:
        """Validate that all prerequisites are met."""
        self.logger.info("Validating prerequisites...")
        
        # Check configuration
        if not config.validate():
            self.issues.append("Configuration validation failed")
            self.generation_stats['errors'] += 1
            return False
        
        # Ensure directories exist
        try:
            config.ensure_directories()
        except Exception as e:
            self.issues.append(f"Failed to create directories: {e}")
            self.generation_stats['errors'] += 1
            return False
        
        # Check for JSON stub files
        stubs_dir = config.get_path('json_stubs.directory')
        json_files = list(stubs_dir.glob(config.get('json_stubs.file_pattern', '*.json')))
        
        if not json_files:
            self.issues.append(f"No JSON stub files found in {stubs_dir}")
            self.generation_stats['warnings'] += 1
        
        self.logger.info("✓ Prerequisites validated")
        return True
    
    def _ensure_javadoc_extracted(self, force: bool = False) -> bool:
        """Ensure JavaDoc is extracted and available."""
        self.logger.info("Checking JavaDoc extraction...")
        
        try:
            info = self.javadoc_extractor.get_extraction_info()
            
            if not info['extracted'] or force:
                self.logger.info("Extracting JavaDoc...")
                if not self.dry_run:
                    success = self.javadoc_extractor.extract_javadoc(force=force)
                    if not success:
                        self.issues.append("JavaDoc extraction failed")
                        self.generation_stats['errors'] += 1
                        return False
                else:
                    self.logger.info("DRY RUN: Would extract JavaDoc")
            
            self.logger.info("✓ JavaDoc available")
            return True
            
        except Exception as e:
            self.issues.append(f"JavaDoc extraction error: {e}")
            self.generation_stats['errors'] += 1
            return False
    
    def _load_json_stubs(self, specific_classes: Optional[List[str]] = None) -> Dict[str, Any]:
        """Load JSON stub files."""
        self.logger.info("Loading JSON stub files...")
        
        try:
            stubs_dir = config.get_path('json_stubs.directory')
            json_files = list(stubs_dir.glob(config.get('json_stubs.file_pattern', '*.json')))
            
            if specific_classes:
                # Filter to specific classes
                class_files = {}
                for class_name in specific_classes:
                    class_file = stubs_dir / f"{class_name}.json"
                    if class_file.exists():
                        class_files[class_name] = class_file
                    else:
                        self.issues.append(f"JSON stub not found for class: {class_name}")
                        self.generation_stats['warnings'] += 1
                json_files = list(class_files.values())
            
            json_stubs = {}
            for json_file in json_files:
                try:
                    stub_data = self.json_reader.load_json_stub(json_file)
                    if stub_data:
                        class_name = stub_data.class_name
                        json_stubs[class_name] = stub_data
                        self.generation_stats['classes_processed'] += 1
                    else:
                        self.issues.append(f"Failed to load {json_file}: Invalid or missing data")
                        self.generation_stats['errors'] += 1
                except Exception as e:
                    self.issues.append(f"Failed to load {json_file}: {e}")
                    self.generation_stats['errors'] += 1
            
            self.logger.info(f"✓ Loaded {len(json_stubs)} JSON stub files")
            return json_stubs
            
        except Exception as e:
            self.issues.append(f"Failed to load JSON stubs: {e}")
            self.generation_stats['errors'] += 1
            return {}
    
    def _parse_javadoc_documentation(self, specific_classes: Optional[List[str]] = None) -> Dict[str, Any]:
        """Parse JavaDoc documentation."""
        self.logger.info("Parsing JavaDoc documentation...")
        
        try:
            javadoc_root = config.get_path('javadoc.extract_dir')
            
            if not javadoc_root.exists():
                self.issues.append("JavaDoc directory not found")
                self.generation_stats['warnings'] += 1
                return {}
            
            parser = JavaDocHTMLParser(javadoc_root)
            
            # Parse JavaDoc for the specified classes or all available classes
            if specific_classes:
                self.logger.info(f"Parsing JavaDoc for {len(specific_classes)} specific classes...")
                parsed_classes = parser.parse_all_classes(specific_classes)
            else:
                self.logger.info("Parsing JavaDoc for all available classes...")
                parsed_classes = parser.parse_all_classes()
            
            # Keep ClassDocumentation objects for the JSON enhancer
            self.logger.info(f"✓ Successfully parsed JavaDoc for {len(parsed_classes)} classes")
            return parsed_classes
            
        except Exception as e:
            self.logger.error(f"JavaDoc parsing error: {e}")
            self.issues.append(f"JavaDoc parsing error: {e}")
            self.generation_stats['errors'] += 1
            return {}
    

    
    def _enhance_json_stubs(self, json_stubs: Dict[str, Any], javadoc_data: Dict[str, Any], 
                           options: Dict[str, Any]) -> Dict[str, Any]:
        """Enhance JSON stubs with JavaDoc data."""
        self.logger.info("Enhancing JSON stubs with JavaDoc data...")
        
        try:
            enhanced_stubs = {}
            
            for class_name, stub_data in json_stubs.items():
                try:
                    # Get JavaDoc data for this class if available
                    class_javadoc = javadoc_data.get(class_name, None)
                    
                    # Enhance the stub
                    enhanced_stub = self.json_enhancer.enhance_json_stub(stub_data, class_javadoc)
                    enhanced_stubs[class_name] = enhanced_stub
                    
                    # Count methods
                    methods = enhanced_stub.methods if hasattr(enhanced_stub, 'methods') else []
                    self.generation_stats['methods_documented'] += len(methods)
                    
                except Exception as e:
                    self.issues.append(f"Failed to enhance {class_name}: {e}")
                    self.generation_stats['errors'] += 1
            
            self.logger.info(f"✓ Enhanced {len(enhanced_stubs)} JSON stubs")
            return enhanced_stubs
            
        except Exception as e:
            self.issues.append(f"JSON enhancement error: {e}")
            self.generation_stats['errors'] += 1
            return {}
    
    def _generate_enhanced_json_files(self, enhanced_stubs: Dict[str, Any], options: Dict[str, Any]):
        """Generate enhanced JSON files."""
        self.logger.info("Generating enhanced JSON files...")
        
        try:
            output_dir = config.get_path('output.docs_dir')
            json_dir = output_dir / 'enhanced_json'
            
            if not self.dry_run:
                json_dir.mkdir(parents=True, exist_ok=True)
            
            for class_name, enhanced_stub in enhanced_stubs.items():
                json_file = json_dir / f"{class_name}_enhanced.json"
                
                if not self.dry_run:
                    # Convert enhanced stub to dictionary for JSON serialization
                    enhanced_stub_dict = self._convert_enhanced_stub_to_dict(enhanced_stub)
                    with open(json_file, 'w', encoding='utf-8') as f:
                        json.dump(enhanced_stub_dict, f, indent=2, ensure_ascii=False)
                
                self.generated_files['enhanced_json'].append(str(json_file))
                self.generation_stats['files_generated'] += 1
            
            self.logger.info(f"✓ Generated {len(enhanced_stubs)} enhanced JSON files")
            
        except Exception as e:
            self.issues.append(f"Enhanced JSON generation error: {e}")
            self.generation_stats['errors'] += 1
    
    def _generate_rst_documentation(self, enhanced_stubs: Dict[str, Any], options: Dict[str, Any]):
        """Generate RST documentation files using structured integration system."""
        self.logger.info("Generating RST documentation...")
        
        try:
            # Apply toctree options to config if provided
            if 'toctree_enabled' in options:
                config.config['sphinx']['inject_toctree'] = options['toctree_enabled']
            if 'toctree_maxdepth' in options:
                config.config['sphinx']['toctree_maxdepth'] = options['toctree_maxdepth']
            
            # Use the structured integration system for proper RST generation
            success = self.structured_integration.create_structured_integration()
            
            if success:
                self.logger.info("✓ Generated RST documentation using structured integration system")
                # Note: The structured integration system handles its own file tracking
                # We'll approximate the file count based on enhanced stubs
                self.generation_stats['files_generated'] += len(enhanced_stubs) * 2  # Estimate: docstring + detailed doc per class
            else:
                self.generation_stats['errors'] += 1
                self.issues.append("Structured integration failed")
                self.logger.error("Structured integration failed")
            
        except Exception as e:
            self.issues.append(f"RST generation error: {e}")
            self.generation_stats['errors'] += 1
    
    def _generate_method_index(self, enhanced_stubs: Dict[str, Any], options: Dict[str, Any]):
        """Generate comprehensive method index."""
        self.logger.info("Generating method index...")
        
        try:
            # Use the existing method index system
            results = self.method_index_system.generate_complete_index_system(enhanced_stubs)
            
            # Track generated files
            generated_files = results.get('generated_files', {})
            for file_type, files in generated_files.items():
                if isinstance(files, dict):
                    self.generated_files['index_files'].extend(files.values())
                    self.generation_stats['files_generated'] += len(files)
                elif isinstance(files, list):
                    self.generated_files['index_files'].extend(files)
                    self.generation_stats['files_generated'] += len(files)
                else:
                    self.generated_files['index_files'].append(str(files))
                    self.generation_stats['files_generated'] += 1
            
            self.logger.info("✓ Generated method index system")
            
        except Exception as e:
            self.issues.append(f"Method index generation error: {e}")
            self.generation_stats['errors'] += 1
    
    def _integrate_with_sphinx(self, options: Dict[str, Any]):
        """Integrate with existing Sphinx documentation."""
        self.logger.info("Integrating with Sphinx...")
        
        try:
            # Basic Sphinx integration - create index file
            output_dir = config.get_path('output.docs_dir')
            index_file = output_dir / 'index.rst'
            
            if not self.dry_run:
                index_content = self._generate_main_index_content()
                with open(index_file, 'w', encoding='utf-8') as f:
                    f.write(index_content)
            
            self.generated_files['sphinx_integration'].append(str(index_file))
            self.generation_stats['files_generated'] += 1
            
            self.logger.info("✓ Sphinx integration completed")
            
        except Exception as e:
            self.issues.append(f"Sphinx integration error: {e}")
            self.generation_stats['errors'] += 1
    
    def _validate_generated_documentation(self):
        """Validate generated documentation."""
        self.logger.info("Validating generated documentation...")
        
        try:
            # Basic validation - check that files exist
            all_files = (
                self.generated_files['class_pages'] +
                self.generated_files['index_files'] +
                self.generated_files['enhanced_json'] +
                self.generated_files['sphinx_integration']
            )
            
            missing_files = []
            for file_path in all_files:
                if not Path(file_path).exists():
                    missing_files.append(file_path)
            
            if missing_files:
                self.issues.append(f"Missing generated files: {len(missing_files)}")
                self.generation_stats['warnings'] += len(missing_files)
            
            self.logger.info("✓ Documentation validation completed")
            
        except Exception as e:
            self.issues.append(f"Validation error: {e}")
            self.generation_stats['errors'] += 1
    
    def _generate_class_rst_content(self, class_name: str, enhanced_stub: Any) -> str:
        """Generate basic RST content for a class."""
        # Handle both dictionary and EnhancedJSONStubData objects
        if hasattr(enhanced_stub, 'package'):
            package = enhanced_stub.package
            methods = enhanced_stub.methods
            javadoc_desc = enhanced_stub.javadoc_description
        else:
            package = enhanced_stub.get('package', 'unknown')
            methods = enhanced_stub.get('methods', [])
            javadoc_desc = enhanced_stub.get('javadoc_description', 'Class documentation not available.')
        
        content = f"""
{class_name}
{'=' * len(class_name)}

**Package:** ``{package}``

Overview
--------

{javadoc_desc}

Methods
-------

"""
        
        for method in methods[:5]:  # Show first 5 methods
            method_name = method.get('name', 'unknown')
            signature = method.get('signature', '')
            content += f"""
{method_name}
{'^' * len(method_name)}

**Signature:** ``{signature}``

{method.get('documentation', 'Method documentation not available.')}

"""
        
        if len(methods) > 5:
            content += f"\n... and {len(methods) - 5} more methods.\n"
        
        return content
    
    def _generate_main_index_content(self) -> str:
        """Generate main index RST content."""
        return """
API Documentation
=================

This section contains enhanced API documentation that combines reflection-based 
method signatures with JavaDoc descriptions.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

"""
    
    def _get_results(self) -> Dict[str, Any]:
        """Get generation results dictionary."""
        return {
            'statistics': self.generation_stats.copy(),
            'generated_files': self.generated_files.copy(),
            'issues': self.issues.copy()
        }
    
    def _convert_enhanced_stub_to_dict(self, enhanced_stub) -> Dict[str, Any]:
        """Convert EnhancedJSONStubData object to dictionary for JSON serialization."""
        from dataclasses import asdict
        
        try:
            # Use dataclasses.asdict for automatic conversion
            return asdict(enhanced_stub)
        except Exception:
            # Fallback to manual conversion if asdict fails
            return {
                'class_name': getattr(enhanced_stub, 'class_name', ''),
                'package': getattr(enhanced_stub, 'package', ''),
                'extracted_at': getattr(enhanced_stub, 'extracted_at', ''),
                'extractor_version': getattr(enhanced_stub, 'extractor_version', ''),
                'enhancement_timestamp': getattr(enhanced_stub, 'enhancement_timestamp', ''),
                'enhancement_version': getattr(enhanced_stub, 'enhancement_version', ''),
                'javadoc_description': getattr(enhanced_stub, 'javadoc_description', ''),
                'methods': [self._convert_method_to_dict(method) for method in getattr(enhanced_stub, 'methods', [])],
                'fields': getattr(enhanced_stub, 'fields', []),
                'constructors': getattr(enhanced_stub, 'constructors', []),
                'inheritance': getattr(enhanced_stub, 'inheritance', {}),
                'nested_classes': getattr(enhanced_stub, 'nested_classes', []),
                'deprecated': getattr(enhanced_stub, 'deprecated', False),
                'since_version': getattr(enhanced_stub, 'since_version', None),
                'see_also': getattr(enhanced_stub, 'see_also', []),
                'enhancement_metadata': getattr(enhanced_stub, 'enhancement_metadata', {})
            }
    
    def _convert_method_to_dict(self, method) -> Dict[str, Any]:
        """Convert enhanced method to dictionary."""
        try:
            from dataclasses import asdict
            return asdict(method)
        except Exception:
            # Fallback to manual conversion
            return {
                'name': getattr(method, 'name', ''),
                'overloads': getattr(method, 'overloads', []),
                'documentation': getattr(method, 'documentation', ''),
                'javadoc_description': getattr(method, 'javadoc_description', ''),
                'category': getattr(method, 'category', ''),
                'deprecated': getattr(method, 'deprecated', False),
                'since_version': getattr(method, 'since_version', None),
                'see_also': getattr(method, 'see_also', []),
                'examples': getattr(method, 'examples', [])
            }