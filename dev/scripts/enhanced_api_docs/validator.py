"""
Validation system for the enhanced API documentation.
"""

import json
import re
from pathlib import Path
from typing import Dict, Any, List

from .config import config
from .logging_setup import get_logger


class DocumentationValidator:
    """Validator for enhanced API documentation system."""
    
    def __init__(self, check_links: bool = False, report_missing: bool = False):
        """Initialize the validator."""
        self.check_links = check_links
        self.report_missing = report_missing
        self.logger = get_logger('validator')
        
        self.validation_results = {
            'configuration': {'status': 'unknown', 'issues': [], 'recovery_suggestions': []},
            'dependencies': {'status': 'unknown', 'issues': [], 'recovery_suggestions': []},
            'documentation': {'status': 'unknown', 'issues': [], 'statistics': {}, 'recovery_suggestions': []},
            'completeness': {'status': 'unknown', 'issues': [], 'statistics': {}, 'recovery_suggestions': []},
            'cross_references': {'status': 'unknown', 'issues': [], 'statistics': {}, 'recovery_suggestions': []},
            'overall_status': 'unknown'
        }
    
    def validate_all(self) -> Dict[str, Any]:
        """Run comprehensive validation of the documentation system."""
        self.logger.info("Starting comprehensive validation...")
        
        # Validate configuration
        self._validate_configuration()
        
        # Validate dependencies
        self._validate_dependencies()
        
        # Validate generated documentation
        self._validate_documentation()
        
        # Validate documentation completeness
        self._validate_completeness()
        
        # Validate cross-references
        self._validate_cross_references()
        
        # Determine overall status
        self._determine_overall_status()
        
        return self.validation_results
    
    def _validate_configuration(self):
        """Validate system configuration."""
        self.logger.info("Validating configuration...")
        
        issues = []
        
        try:
            # Check if configuration is valid
            if not config.validate():
                issues.append("Configuration validation failed")
            
            # Check required paths
            required_paths = [
                ('javadoc.source_zip', 'JavaDoc ZIP file'),
                ('json_stubs.directory', 'JSON stubs directory'),
                ('output.docs_dir', 'Output documentation directory')
            ]
            
            for path_key, description in required_paths:
                try:
                    path = config.get_path(path_key)
                    if path_key == 'javadoc.source_zip':
                        if not path.exists():
                            issues.append(f"{description} not found: {path}")
                    elif path_key == 'json_stubs.directory':
                        if not path.exists():
                            issues.append(f"{description} not found: {path}")
                        else:
                            json_files = list(path.glob('*.json'))
                            if not json_files:
                                issues.append(f"No JSON files found in {description}: {path}")
                except Exception as e:
                    issues.append(f"Invalid {description} path: {e}")
            
            # Check configuration values
            categories = config.get('generation.categories', [])
            if not categories:
                issues.append("No method categories configured")
            
            # Generate recovery suggestions
            recovery_suggestions = self._generate_config_recovery_suggestions(issues)
            
            self.validation_results['configuration'] = {
                'status': 'passed' if not issues else 'failed',
                'issues': issues,
                'recovery_suggestions': recovery_suggestions
            }
            
        except Exception as e:
            issues.append(f"Configuration validation error: {e}")
            recovery_suggestions = self._generate_config_recovery_suggestions(issues)
            self.validation_results['configuration'] = {
                'status': 'failed',
                'issues': issues,
                'recovery_suggestions': recovery_suggestions
            }
    
    def _validate_dependencies(self):
        """Validate system dependencies."""
        self.logger.info("Validating dependencies...")
        
        issues = []
        
        try:
            # Check JavaDoc extraction
            from .javadoc_extractor import JavaDocExtractor
            extractor = JavaDocExtractor()
            info = extractor.get_extraction_info()
            
            if not info['zip_exists']:
                issues.append("JavaDoc ZIP file not found")
            
            if not info['extracted']:
                issues.append("JavaDoc not extracted")
            elif info.get('class_files_count', 0) == 0:
                issues.append("No JavaDoc class files found")
            
            # Check JSON stubs
            stubs_dir = config.get_path('json_stubs.directory')
            if stubs_dir.exists():
                json_files = list(stubs_dir.glob('*.json'))
                if not json_files:
                    issues.append("No JSON stub files found")
                else:
                    # Validate a few JSON files
                    for json_file in json_files[:3]:
                        try:
                            with open(json_file, 'r', encoding='utf-8') as f:
                                data = json.load(f)
                            
                            required_fields = ['class_name', 'package', 'methods']
                            for field in required_fields:
                                if field not in data:
                                    issues.append(f"JSON stub {json_file.name} missing field: {field}")
                                    break
                        except Exception as e:
                            issues.append(f"Invalid JSON stub {json_file.name}: {e}")
            
            # Generate recovery suggestions
            recovery_suggestions = self._generate_deps_recovery_suggestions(issues)
            
            self.validation_results['dependencies'] = {
                'status': 'passed' if not issues else 'failed',
                'issues': issues,
                'recovery_suggestions': recovery_suggestions
            }
            
        except Exception as e:
            issues.append(f"Dependencies validation error: {e}")
            recovery_suggestions = self._generate_deps_recovery_suggestions(issues)
            self.validation_results['dependencies'] = {
                'status': 'failed',
                'issues': issues,
                'recovery_suggestions': recovery_suggestions
            }
    
    def _validate_documentation(self):
        """Validate generated documentation."""
        self.logger.info("Validating generated documentation...")
        
        issues = []
        statistics = {
            'files_checked': 0,
            'broken_links': 0,
            'missing_references': 0,
            'rst_files': 0,
            'json_files': 0
        }
        
        try:
            output_dir = config.get_path('output.docs_dir')
            
            if not output_dir.exists():
                issues.append("Output documentation directory does not exist")
            else:
                # Check RST files
                rst_files = list(output_dir.rglob('*.rst'))
                statistics['rst_files'] = len(rst_files)
                
                for rst_file in rst_files:
                    statistics['files_checked'] += 1
                    
                    try:
                        content = rst_file.read_text(encoding='utf-8')
                        
                        # Check for basic RST syntax issues
                        if self._check_rst_syntax_issues(content):
                            issues.append(f"RST syntax issues in {rst_file.name}")
                        
                        # Check for broken references if requested
                        if self.check_links:
                            broken_refs = self._check_rst_references(content, rst_file)
                            statistics['broken_links'] += len(broken_refs)
                            for ref in broken_refs:
                                issues.append(f"Broken reference in {rst_file.name}: {ref}")
                        
                    except Exception as e:
                        issues.append(f"Error reading {rst_file.name}: {e}")
                
                # Check JSON files
                json_files = list(output_dir.rglob('*.json'))
                statistics['json_files'] = len(json_files)
                
                for json_file in json_files:
                    statistics['files_checked'] += 1
                    
                    try:
                        with open(json_file, 'r', encoding='utf-8') as f:
                            data = json.load(f)
                        
                        # Basic JSON structure validation
                        if not isinstance(data, dict):
                            issues.append(f"Invalid JSON structure in {json_file.name}")
                        
                    except Exception as e:
                        issues.append(f"Invalid JSON file {json_file.name}: {e}")
                
                # Check for missing files if requested
                if self.report_missing:
                    missing_files = self._check_missing_files()
                    statistics['missing_references'] = len(missing_files)
                    for missing_file in missing_files:
                        issues.append(f"Missing expected file: {missing_file}")
            
            # Generate recovery suggestions
            recovery_suggestions = self._generate_docs_recovery_suggestions(issues, statistics)
            
            self.validation_results['documentation'] = {
                'status': 'passed' if not issues else ('warnings' if statistics['files_checked'] > 0 else 'failed'),
                'issues': issues,
                'statistics': statistics,
                'recovery_suggestions': recovery_suggestions
            }
            
        except Exception as e:
            issues.append(f"Documentation validation error: {e}")
            recovery_suggestions = self._generate_docs_recovery_suggestions(issues, statistics)
            self.validation_results['documentation'] = {
                'status': 'failed',
                'issues': issues,
                'statistics': statistics,
                'recovery_suggestions': recovery_suggestions
            }
    
    def _check_rst_syntax_issues(self, content: str) -> bool:
        """Check for basic RST syntax issues."""
        # Check for common RST issues
        lines = content.split('\n')
        
        for i, line in enumerate(lines):
            # Check for title underlines that don't match title length
            if i > 0 and line and all(c in '=-~^"' for c in line):
                title_line = lines[i-1].strip()
                if title_line and len(line) != len(title_line):
                    return True
        
        return False
    
    def _check_rst_references(self, content: str, rst_file: Path) -> List[str]:
        """Check for broken RST references."""
        broken_refs = []
        
        # Find :doc: references
        doc_refs = re.findall(r':doc:`([^`]+)`', content)
        for ref in doc_refs:
            # Check if referenced file exists
            ref_path = rst_file.parent / f"{ref}.rst"
            if not ref_path.exists():
                # Try relative to output directory
                output_dir = config.get_path('output.docs_dir')
                ref_path = output_dir / f"{ref}.rst"
                if not ref_path.exists():
                    broken_refs.append(f":doc:`{ref}`")
        
        return broken_refs
    
    def _check_missing_files(self) -> List[str]:
        """Check for missing expected files."""
        missing_files = []
        
        output_dir = config.get_path('output.docs_dir')
        
        # Expected files
        expected_files = [
            'index.rst',
            'method_index.rst'
        ]
        
        for expected_file in expected_files:
            file_path = output_dir / expected_file
            if not file_path.exists():
                missing_files.append(expected_file)
        
        return missing_files
    
    def _validate_completeness(self):
        """Validate documentation completeness."""
        self.logger.info("Validating documentation completeness...")
        
        issues = []
        statistics = {
            'total_classes': 0,
            'documented_classes': 0,
            'total_methods': 0,
            'documented_methods': 0,
            'missing_descriptions': 0,
            'missing_examples': 0
        }
        
        try:
            # Check JSON stubs for completeness
            stubs_dir = config.get_path('json_stubs.directory')
            if stubs_dir.exists():
                json_files = list(stubs_dir.glob('*.json'))
                statistics['total_classes'] = len(json_files)
                
                for json_file in json_files:
                    try:
                        with open(json_file, 'r', encoding='utf-8') as f:
                            data = json.load(f)
                        
                        class_name = data.get('class_name', json_file.stem)
                        methods = data.get('methods', [])
                        statistics['total_methods'] += len(methods)
                        
                        # Check if class has documentation
                        if data.get('javadoc_description') or data.get('description'):
                            statistics['documented_classes'] += 1
                        else:
                            issues.append(f"Class {class_name} missing description")
                        
                        # Check method documentation
                        for method in methods:
                            method_name = method.get('name', 'unknown')
                            if method.get('documentation') or method.get('javadoc_description'):
                                statistics['documented_methods'] += 1
                            else:
                                statistics['missing_descriptions'] += 1
                                if self.report_missing:
                                    issues.append(f"Method {class_name}.{method_name} missing description")
                            
                            # Check for examples
                            if not method.get('examples', []):
                                statistics['missing_examples'] += 1
                        
                    except Exception as e:
                        issues.append(f"Error checking completeness of {json_file.name}: {e}")
            
            # Generate recovery suggestions
            recovery_suggestions = self._generate_completeness_recovery_suggestions(issues, statistics)
            
            self.validation_results['completeness'] = {
                'status': 'passed' if not issues else ('warnings' if statistics['documented_classes'] > 0 else 'failed'),
                'issues': issues,
                'statistics': statistics,
                'recovery_suggestions': recovery_suggestions
            }
            
        except Exception as e:
            issues.append(f"Completeness validation error: {e}")
            recovery_suggestions = self._generate_completeness_recovery_suggestions(issues, statistics)
            self.validation_results['completeness'] = {
                'status': 'failed',
                'issues': issues,
                'statistics': statistics,
                'recovery_suggestions': recovery_suggestions
            }
    
    def _validate_cross_references(self):
        """Validate cross-references and links."""
        self.logger.info("Validating cross-references...")
        
        issues = []
        statistics = {
            'total_references': 0,
            'broken_references': 0,
            'external_links': 0,
            'internal_links': 0
        }
        
        try:
            if self.check_links:
                output_dir = config.get_path('output.docs_dir')
                
                if output_dir.exists():
                    rst_files = list(output_dir.rglob('*.rst'))
                    
                    for rst_file in rst_files:
                        try:
                            content = rst_file.read_text(encoding='utf-8')
                            
                            # Check :doc: references
                            doc_refs = re.findall(r':doc:`([^`]+)`', content)
                            statistics['total_references'] += len(doc_refs)
                            statistics['internal_links'] += len(doc_refs)
                            
                            for ref in doc_refs:
                                if not self._check_doc_reference_exists(ref, rst_file):
                                    statistics['broken_references'] += 1
                                    issues.append(f"Broken :doc: reference in {rst_file.name}: {ref}")
                            
                            # Check external links
                            http_links = re.findall(r'https?://[^\s<>"]+', content)
                            statistics['external_links'] += len(http_links)
                            
                            # Check class references
                            class_refs = re.findall(r':class:`([^`]+)`', content)
                            statistics['total_references'] += len(class_refs)
                            
                            for ref in class_refs:
                                if not self._check_class_reference_exists(ref):
                                    statistics['broken_references'] += 1
                                    issues.append(f"Broken :class: reference in {rst_file.name}: {ref}")
                            
                        except Exception as e:
                            issues.append(f"Error checking references in {rst_file.name}: {e}")
            
            # Generate recovery suggestions
            recovery_suggestions = self._generate_cross_ref_recovery_suggestions(issues, statistics)
            
            self.validation_results['cross_references'] = {
                'status': 'passed' if not issues else 'warnings',
                'issues': issues,
                'statistics': statistics,
                'recovery_suggestions': recovery_suggestions
            }
            
        except Exception as e:
            issues.append(f"Cross-reference validation error: {e}")
            recovery_suggestions = self._generate_cross_ref_recovery_suggestions(issues, statistics)
            self.validation_results['cross_references'] = {
                'status': 'failed',
                'issues': issues,
                'statistics': statistics,
                'recovery_suggestions': recovery_suggestions
            }
    
    def _check_doc_reference_exists(self, ref: str, current_file: Path) -> bool:
        """Check if a :doc: reference exists."""
        output_dir = config.get_path('output.docs_dir')
        
        # Try relative to current file
        ref_path = current_file.parent / f"{ref}.rst"
        if ref_path.exists():
            return True
        
        # Try relative to output directory
        ref_path = output_dir / f"{ref}.rst"
        if ref_path.exists():
            return True
        
        # Try with .rst extension if not present
        if not ref.endswith('.rst'):
            ref_path = output_dir / f"{ref}.rst"
            if ref_path.exists():
                return True
        
        return False
    
    def _check_class_reference_exists(self, ref: str) -> bool:
        """Check if a :class: reference exists."""
        # Check if class exists in JSON stubs
        stubs_dir = config.get_path('json_stubs.directory')
        
        # Extract class name from reference (handle package.ClassName format)
        class_name = ref.split('.')[-1]
        class_file = stubs_dir / f"{class_name}.json"
        
        return class_file.exists()
    
    def _generate_config_recovery_suggestions(self, issues: List[str]) -> List[str]:
        """Generate recovery suggestions for configuration issues."""
        suggestions = []
        
        for issue in issues:
            if "JavaDoc ZIP file not found" in issue:
                suggestions.append("Download the JavaDoc ZIP file and place it in the configured location")
                suggestions.append("Update the configuration to point to the correct JavaDoc ZIP file path")
            elif "JSON stubs directory not found" in issue:
                suggestions.append("Run the JSON stub generation process first")
                suggestions.append("Check if the JSON stubs directory path is correct in configuration")
            elif "No JSON files found" in issue:
                suggestions.append("Generate JSON stub files using the reflection-based extractor")
                suggestions.append("Verify that the file pattern in configuration matches your JSON files")
            elif "No method categories configured" in issue:
                suggestions.append("Add method categories to the configuration file")
                suggestions.append("Use default categories: ['Getters', 'Setters', 'Analysis', 'I/O Operations', 'Visualization', 'Utilities']")
        
        # Remove duplicates
        return list(set(suggestions))
    
    def _generate_deps_recovery_suggestions(self, issues: List[str]) -> List[str]:
        """Generate recovery suggestions for dependency issues."""
        suggestions = []
        
        for issue in issues:
            if "JavaDoc not extracted" in issue:
                suggestions.append("Run: python -m enhanced_api_docs extract-javadoc")
                suggestions.append("Check if the JavaDoc ZIP file is valid and not corrupted")
            elif "No JavaDoc class files found" in issue:
                suggestions.append("Verify that the JavaDoc ZIP contains HTML class documentation")
                suggestions.append("Re-extract the JavaDoc with --force flag")
            elif "No JSON stub files found" in issue:
                suggestions.append("Generate JSON stubs using the existing reflection-based system")
                suggestions.append("Check if the JSON stubs directory path is correct")
            elif "missing field" in issue:
                suggestions.append("Regenerate JSON stub files with the latest extractor version")
                suggestions.append("Validate JSON stub file format against the expected schema")
        
        return list(set(suggestions))
    
    def _generate_completeness_recovery_suggestions(self, issues: List[str], statistics: Dict[str, int]) -> List[str]:
        """Generate recovery suggestions for completeness issues."""
        suggestions = []
        
        if statistics.get('missing_descriptions', 0) > 0:
            suggestions.append("Run JavaDoc parsing to extract method descriptions")
            suggestions.append("Manually add descriptions to methods missing documentation")
        
        if statistics.get('missing_examples', 0) > 0:
            suggestions.append("Add usage examples to method documentation")
            suggestions.append("Extract examples from existing tutorials and notebooks")
        
        if statistics.get('documented_classes', 0) < statistics.get('total_classes', 1):
            suggestions.append("Add class-level documentation from JavaDoc")
            suggestions.append("Write overview descriptions for undocumented classes")
        
        return suggestions
    
    def _generate_cross_ref_recovery_suggestions(self, issues: List[str], statistics: Dict[str, int]) -> List[str]:
        """Generate recovery suggestions for cross-reference issues."""
        suggestions = []
        
        if statistics.get('broken_references', 0) > 0:
            suggestions.append("Update broken references to point to existing documentation files")
            suggestions.append("Generate missing documentation files for referenced classes")
            suggestions.append("Remove references to non-existent classes or methods")
        
        if any("Broken :doc:" in issue for issue in issues):
            suggestions.append("Check that all referenced RST files exist in the documentation directory")
            suggestions.append("Use relative paths for :doc: references within the same documentation tree")
        
        if any("Broken :class:" in issue for issue in issues):
            suggestions.append("Ensure all referenced classes have corresponding JSON stub files")
            suggestions.append("Update class references to use the correct package and class names")
        
        return suggestions
    
    def _generate_docs_recovery_suggestions(self, issues: List[str], statistics: Dict[str, int]) -> List[str]:
        """Generate recovery suggestions for documentation issues."""
        suggestions = []
        
        for issue in issues:
            if "RST syntax issues" in issue:
                suggestions.append("Fix RST syntax errors in the affected files")
                suggestions.append("Use a RST linter to validate syntax before generation")
            elif "Error reading" in issue:
                suggestions.append("Check file permissions and encoding")
                suggestions.append("Regenerate the affected documentation files")
            elif "Invalid JSON" in issue:
                suggestions.append("Validate and fix JSON syntax in the affected files")
                suggestions.append("Regenerate JSON files from source data")
            elif "Missing expected file" in issue:
                suggestions.append("Run the complete documentation generation process")
                suggestions.append("Check if the file generation step completed successfully")
        
        if statistics.get('rst_files', 0) == 0:
            suggestions.append("Generate RST documentation files")
            suggestions.append("Run: python -m enhanced_api_docs generate --components rst")
        
        if statistics.get('json_files', 0) == 0:
            suggestions.append("Generate enhanced JSON files")
            suggestions.append("Run: python -m enhanced_api_docs generate --components json")
        
        return list(set(suggestions))
    
    def _determine_overall_status(self):
        """Determine overall validation status."""
        statuses = [
            self.validation_results['configuration']['status'],
            self.validation_results['dependencies']['status'],
            self.validation_results['documentation']['status'],
            self.validation_results['completeness']['status'],
            self.validation_results['cross_references']['status']
        ]
        
        if 'failed' in statuses:
            self.validation_results['overall_status'] = 'failed'
        elif 'warnings' in statuses:
            self.validation_results['overall_status'] = 'warnings'
        else:
            self.validation_results['overall_status'] = 'passed'
    
    def generate_validation_report(self, results: Dict[str, Any]) -> Dict[str, Any]:
        """Generate a comprehensive validation report."""
        total_issues = (
            len(results['configuration']['issues']) +
            len(results['dependencies']['issues']) +
            len(results['documentation']['issues']) +
            len(results['completeness']['issues']) +
            len(results['cross_references']['issues'])
        )
        
        total_suggestions = (
            len(results['configuration']['recovery_suggestions']) +
            len(results['dependencies']['recovery_suggestions']) +
            len(results['documentation']['recovery_suggestions']) +
            len(results['completeness']['recovery_suggestions']) +
            len(results['cross_references']['recovery_suggestions'])
        )
        
        return {
            'timestamp': self._get_timestamp(),
            'overall_status': results['overall_status'],
            'configuration': results['configuration'],
            'dependencies': results['dependencies'],
            'documentation': results['documentation'],
            'completeness': results['completeness'],
            'cross_references': results['cross_references'],
            'summary': {
                'total_issues': total_issues,
                'total_recovery_suggestions': total_suggestions,
                'files_validated': results['documentation']['statistics'].get('files_checked', 0),
                'classes_checked': results['completeness']['statistics'].get('total_classes', 0),
                'methods_checked': results['completeness']['statistics'].get('total_methods', 0),
                'references_checked': results['cross_references']['statistics'].get('total_references', 0),
                'validation_passed': results['overall_status'] in ['passed', 'warnings']
            },
            'recommendations': self._generate_overall_recommendations(results)
        }
    
    def save_report(self, report: Dict[str, Any], output_path: Path):
        """Save validation report to file."""
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(report, f, indent=2, ensure_ascii=False)
            self.logger.info(f"Validation report saved to: {output_path}")
        except Exception as e:
            self.logger.error(f"Failed to save validation report: {e}")
    
    def _generate_overall_recommendations(self, results: Dict[str, Any]) -> List[str]:
        """Generate overall recommendations based on validation results."""
        recommendations = []
        
        # Priority recommendations based on status
        if results['configuration']['status'] == 'failed':
            recommendations.append("CRITICAL: Fix configuration issues before proceeding")
            recommendations.extend(results['configuration']['recovery_suggestions'][:2])
        
        if results['dependencies']['status'] == 'failed':
            recommendations.append("CRITICAL: Resolve dependency issues")
            recommendations.extend(results['dependencies']['recovery_suggestions'][:2])
        
        # Improvement recommendations
        completeness_stats = results['completeness']['statistics']
        if completeness_stats.get('documented_methods', 0) < completeness_stats.get('total_methods', 1) * 0.8:
            recommendations.append("IMPROVEMENT: Increase method documentation coverage (currently below 80%)")
        
        if results['cross_references']['statistics'].get('broken_references', 0) > 0:
            recommendations.append("IMPROVEMENT: Fix broken cross-references for better navigation")
        
        # Success recommendations
        if results['overall_status'] == 'passed':
            recommendations.append("SUCCESS: All validations passed - documentation system is ready")
            recommendations.append("Consider running periodic validation to maintain quality")
        
        return recommendations[:5]  # Limit to top 5 recommendations
    
    def _get_timestamp(self) -> str:
        """Get current timestamp string."""
        import datetime
        return datetime.datetime.now().isoformat()


class DocumentationCleaner:
    """Cleaner for generated documentation files and caches."""
    
    def __init__(self):
        """Initialize the cleaner."""
        self.logger = get_logger('cleaner')
    
    def clean_all(self) -> bool:
        """Clean all generated files and caches."""
        self.logger.info("Cleaning all generated files and caches...")
        
        try:
            cache_success = self.clean_cache()
            generated_success = self.clean_generated()
            
            return cache_success and generated_success
            
        except Exception as e:
            self.logger.error(f"Failed to clean all files: {e}")
            return False
    
    def clean_cache(self) -> bool:
        """Clean cache files only."""
        self.logger.info("Cleaning cache files...")
        
        try:
            cache_dir = config.get_path('caching.cache_dir')
            
            if cache_dir.exists():
                import shutil
                shutil.rmtree(cache_dir)
                self.logger.info(f"Removed cache directory: {cache_dir}")
            
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to clean cache: {e}")
            return False
    
    def clean_generated(self) -> bool:
        """Clean generated documentation files only."""
        self.logger.info("Cleaning generated documentation files...")
        
        try:
            output_dir = config.get_path('output.docs_dir')
            
            if output_dir.exists():
                # Remove specific generated files/directories
                generated_items = [
                    'classes',
                    'enhanced_json',
                    'index.rst',
                    'method_index.rst',
                    'method_search_data.json',
                    'method_examples_data.json'
                ]
                
                for item in generated_items:
                    item_path = output_dir / item
                    if item_path.exists():
                        if item_path.is_dir():
                            import shutil
                            shutil.rmtree(item_path)
                            self.logger.info(f"Removed directory: {item_path}")
                        else:
                            item_path.unlink()
                            self.logger.info(f"Removed file: {item_path}")
            
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to clean generated files: {e}")
            return False