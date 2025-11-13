"""
Command-line interface for the enhanced API documentation system.
"""

import argparse
import sys
import time
from pathlib import Path
from typing import Dict, Any, Optional

from .config import config
from .logging_setup import setup_logging, get_logger
from .javadoc_extractor import JavaDocExtractor
from .orchestrator import DocumentationOrchestrator
from .validator import DocumentationValidator, DocumentationCleaner
from .integration_manager import IntegrationManager, IntegrationStrategy


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description='Enhanced API Documentation Generator for PySNT',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Full documentation generation
  python -m enhanced_api_docs generate --verbose
  
  # Incremental update (only changed files)
  python -m enhanced_api_docs generate --incremental
  
  # Generate specific components
  python -m enhanced_api_docs generate --components javadoc,json,rst
  
  # Validate and report issues
  python -m enhanced_api_docs validate --report-missing
  
  # System information and status
  python -m enhanced_api_docs info --detailed
        """
    )
    
    parser.add_argument(
        '--verbose', '-v',
        action='count',
        default=0,
        help='Increase verbosity (use -v, -vv, or -vvv)'
    )
    
    parser.add_argument(
        '--config',
        type=Path,
        help='Path to custom configuration file'
    )
    
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be done without making changes'
    )
    
    parser.add_argument(
        '--progress',
        action='store_true',
        default=True,
        help='Show progress bars and detailed status (default: enabled)'
    )
    
    parser.add_argument(
        '--no-progress',
        dest='progress',
        action='store_false',
        help='Disable progress bars and detailed status'
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Generate documentation command (main orchestration)
    generate_parser = subparsers.add_parser(
        'generate',
        help='Generate enhanced API documentation (main command)'
    )
    generate_parser.add_argument(
        '--force',
        action='store_true',
        help='Force regeneration of all documentation'
    )
    generate_parser.add_argument(
        '--incremental',
        action='store_true',
        help='Only process changed files (faster updates)'
    )
    generate_parser.add_argument(
        '--components',
        type=str,
        help='Comma-separated list of components to generate: javadoc,json,rst,index,sphinx'
    )
    generate_parser.add_argument(
        '--classes',
        type=str,
        help='Comma-separated list of specific classes to process'
    )
    generate_parser.add_argument(
        '--output-format',
        choices=['rst', 'markdown', 'both'],
        default='rst',
        help='Output format for generated documentation'
    )
    generate_parser.add_argument(
        '--validate-after',
        action='store_true',
        default=True,
        help='Validate generated documentation after creation (default: enabled)'
    )
    generate_parser.add_argument(
        '--no-validate',
        dest='validate_after',
        action='store_false',
        help='Skip validation after generation'
    )
    generate_parser.add_argument(
        '--no-toctree',
        action='store_true',
        help='Disable automatic toctree injection in enhanced class documentation'
    )
    generate_parser.add_argument(
        '--toctree-maxdepth',
        type=int,
        default=3,
        help='Maximum depth for toctree (default: 3)'
    )
    
    # Validate documentation command
    validate_parser = subparsers.add_parser(
        'validate',
        help='Validate configuration, dependencies, and generated documentation'
    )
    validate_parser.add_argument(
        '--report-missing',
        action='store_true',
        help='Report missing JavaDoc or JSON stub data'
    )
    validate_parser.add_argument(
        '--check-links',
        action='store_true',
        help='Check for broken cross-references and links'
    )
    validate_parser.add_argument(
        '--output-report',
        type=Path,
        help='Save validation report to file'
    )
    
    # Info command
    info_parser = subparsers.add_parser(
        'info',
        help='Show system information and status'
    )
    info_parser.add_argument(
        '--detailed',
        action='store_true',
        help='Show detailed system information'
    )
    info_parser.add_argument(
        '--stats',
        action='store_true',
        help='Show documentation statistics'
    )
    
    # Extract JavaDoc command
    extract_parser = subparsers.add_parser(
        'extract-javadoc',
        help='Extract JavaDoc ZIP file'
    )
    extract_parser.add_argument(
        '--force',
        action='store_true',
        help='Force re-extraction even if already extracted'
    )
    
    # Sphinx integration command
    sphinx_parser = subparsers.add_parser(
        'integrate-sphinx',
        help='Integrate enhanced documentation with existing Sphinx setup'
    )
    sphinx_parser.add_argument(
        '--validate-only',
        action='store_true',
        help='Only validate integration without making changes'
    )
    
    # Integration command
    integrate_parser = subparsers.add_parser(
        'integrate',
        help='Integrate enhanced JavaDoc into existing API documentation'
    )
    integrate_parser.add_argument(
        '--strategy',
        choices=['docstring', 'rst_injection', 'sphinx_extension', 'hybrid'],
        default='hybrid',
        help='Integration strategy to use (default: hybrid)'
    )
    integrate_parser.add_argument(
        '--recommendations',
        action='store_true',
        help='Show integration recommendations without performing integration'
    )
    integrate_parser.add_argument(
        '--key-classes',
        type=str,
        help='Comma-separated list of key classes to prioritize for docstring enhancement'
    )
    
    # Clean command
    clean_parser = subparsers.add_parser(
        'clean',
        help='Clean generated files and caches'
    )
    clean_parser.add_argument(
        '--cache-only',
        action='store_true',
        help='Only clean cache files, keep generated documentation'
    )
    clean_parser.add_argument(
        '--generated-only',
        action='store_true',
        help='Only clean generated documentation, keep cache'
    )
    
    args = parser.parse_args()
    
    # Set up logging based on verbosity level
    if args.verbose == 0:
        log_level = 'INFO'
    elif args.verbose == 1:
        log_level = 'DEBUG'
    else:  # args.verbose >= 2
        log_level = 'DEBUG'
    
    logger = setup_logging(level=log_level)
    
    # Load custom config if provided
    if args.config:
        if args.config.exists():
            config.load_config(args.config)
            logger.info(f"Loaded custom configuration: {args.config}")
        else:
            logger.error(f"Configuration file not found: {args.config}")
            return 1
    
    # Show dry-run notice
    if getattr(args, 'dry_run', False):
        logger.info("DRY RUN MODE: No files will be modified")
    
    # Execute command
    try:
        if args.command == 'generate':
            return generate_command(args)
        elif args.command == 'validate':
            return validate_command(args)
        elif args.command == 'info':
            return info_command(args)
        elif args.command == 'extract-javadoc':
            return extract_javadoc_command(args)
        elif args.command == 'integrate-sphinx':
            return integrate_sphinx_command(args)
        elif args.command == 'integrate':
            return integrate_command(args)
        elif args.command == 'clean':
            return clean_command(args)
        else:
            parser.print_help()
            return 1
    except KeyboardInterrupt:
        logger.info("Operation cancelled by user")
        return 130  # Standard exit code for SIGINT
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        if args.verbose >= 2:
            import traceback
            traceback.print_exc()
        return 1


def extract_javadoc_command(args) -> int:
    """Extract JavaDoc ZIP file."""
    logger = get_logger('cli')
    
    try:
        extractor = JavaDocExtractor()
        
        logger.info("Starting JavaDoc extraction...")
        success = extractor.extract_javadoc(force=args.force)
        
        if success:
            # Show extraction info
            info = extractor.get_extraction_info()
            logger.info(f"JavaDoc extracted successfully:")
            logger.info(f"  - Extract directory: {info['extract_dir']}")
            logger.info(f"  - Class files found: {info.get('class_files_count', 'Unknown')}")
            
            if 'sample_classes' in info:
                logger.info("  - Sample classes:")
                for class_name in info['sample_classes']:
                    logger.info(f"    - {class_name}")
            
            return 0
        else:
            logger.error("JavaDoc extraction failed")
            return 1
            
    except Exception as e:
        logger.error(f"Error during JavaDoc extraction: {e}")
        return 1


def validate_command(args) -> int:
    """Validate configuration, dependencies, and generated documentation."""
    logger = get_logger('cli.validate')
    
    try:
        # Initialize validator
        validator = DocumentationValidator(
            check_links=getattr(args, 'check_links', False),
            report_missing=getattr(args, 'report_missing', False)
        )
        
        logger.info("Starting validation...")
        
        # Run validation
        validation_results = validator.validate_all()
        
        # Generate report
        report = validator.generate_validation_report(validation_results)
        
        # Output report
        if getattr(args, 'output_report', None):
            validator.save_report(report, args.output_report)
            logger.info(f"Validation report saved to: {args.output_report}")
        else:
            _print_validation_report(logger, report)
        
        # Return appropriate exit code
        if validation_results['overall_status'] == 'passed':
            logger.info("✓ All validation checks passed")
            return 0
        elif validation_results['overall_status'] == 'warnings':
            logger.warning("⚠ Validation completed with warnings")
            return 0
        else:
            logger.error("✗ Validation failed")
            return 1
            
    except Exception as e:
        logger.error(f"Validation failed: {e}")
        return 1


def info_command(args) -> int:
    """Show system information."""
    logger = get_logger('cli')
    
    logger.info("Enhanced API Documentation System Information")
    logger.info("=" * 50)
    
    # Configuration info
    logger.info("Configuration:")
    logger.info(f"  - JavaDoc ZIP: {config.get_path('javadoc.source_zip')}")
    logger.info(f"  - Extract directory: {config.get_path('javadoc.extract_dir')}")
    logger.info(f"  - JSON stubs directory: {config.get_path('json_stubs.directory')}")
    logger.info(f"  - Output directory: {config.get_path('output.docs_dir')}")
    
    # System status
    extractor = JavaDocExtractor()
    info = extractor.get_extraction_info()
    
    logger.info("\nSystem Status:")
    logger.info(f"  - JavaDoc ZIP exists: {info['zip_exists']}")
    logger.info(f"  - JavaDoc extracted: {info['extracted']}")
    
    if info['extracted']:
        logger.info(f"  - Class files found: {info.get('class_files_count', 'Unknown')}")
        if 'sample_classes' in info:
            logger.info("  - Sample classes:")
            for class_name in info['sample_classes'][:5]:
                logger.info(f"    - {class_name}")
            if len(info['sample_classes']) > 5:
                logger.info(f"    ... and {len(info['sample_classes']) - 5} more")
    
    # JSON stubs info
    stubs_dir = config.get_path('json_stubs.directory')
    json_files = list(stubs_dir.glob(config.get('json_stubs.file_pattern', '*.json')))
    logger.info(f"  - JSON stub files: {len(json_files)}")
    
    if json_files:
        logger.info("  - Sample JSON stubs:")
        for json_file in json_files[:5]:
            logger.info(f"    - {json_file.name}")
        if len(json_files) > 5:
            logger.info(f"    ... and {len(json_files) - 5} more")
    
    return 0


def generate_command(args) -> int:
    """Generate enhanced API documentation (main orchestration command)."""
    logger = get_logger('cli.generate')
    
    start_time = time.time()
    
    try:
        # Initialize orchestrator
        orchestrator = DocumentationOrchestrator(
            dry_run=getattr(args, 'dry_run', False),
            show_progress=getattr(args, 'progress', True),
            verbose=getattr(args, 'verbose', 0)
        )
        
        # Parse generation options
        components = _parse_components(getattr(args, 'components', None))
        classes = _parse_classes(getattr(args, 'classes', None))
        
        generation_options = {
            'force': getattr(args, 'force', False),
            'incremental': getattr(args, 'incremental', False),
            'components': components,
            'classes': classes,
            'output_format': getattr(args, 'output_format', 'rst'),
            'validate_after': getattr(args, 'validate_after', True),
            'toctree_enabled': not getattr(args, 'no_toctree', False),
            'toctree_maxdepth': getattr(args, 'toctree_maxdepth', 3)
        }
        
        logger.info("Starting enhanced API documentation generation")
        logger.info(f"Options: {generation_options}")
        
        # Run generation
        success, results = orchestrator.generate_documentation(generation_options)
        
        # Report results
        elapsed_time = time.time() - start_time
        _report_generation_results(logger, success, results, elapsed_time)
        
        return 0 if success else 1
        
    except Exception as e:
        logger.error(f"Documentation generation failed: {e}")
        if getattr(args, 'verbose', 0) >= 2:
            import traceback
            traceback.print_exc()
        return 1


def integrate_sphinx_command(args) -> int:
    """Integrate enhanced documentation with existing Sphinx setup."""
    logger = get_logger('cli')
    
    try:
        from .sphinx_integration import SphinxIntegrator
        
        integrator = SphinxIntegrator()
        
        if args.validate_only:
            logger.info("Validating Sphinx integration...")
            is_compatible, issues = integrator.validate_sphinx_compatibility()
            
            if is_compatible:
                logger.info("✓ Sphinx integration validation passed")
                
                # Show integration status
                status = integrator.get_integration_status()
                logger.info("Integration Status:")
                logger.info(f"  - Sphinx compatible: {status['sphinx_compatible']}")
                logger.info(f"  - Directory structure: {status['directory_structure_ok']}")
                logger.info(f"  - Main API updated: {status['main_api_updated']}")
                logger.info(f"  - Main index updated: {status['main_index_updated']}")
                logger.info(f"  - Cross-references valid: {status['cross_references_valid']}")
                
                return 0
            else:
                logger.error("✗ Sphinx integration validation failed:")
                for issue in issues:
                    logger.error(f"  - {issue}")
                return 1
        else:
            logger.info("Integrating enhanced documentation with Sphinx...")
            success = integrator.ensure_sphinx_integration()
            
            if success:
                logger.info("✓ Sphinx integration completed successfully")
                
                # Show final status
                status = integrator.get_integration_status()
                logger.info("Final Integration Status:")
                logger.info(f"  - Sphinx compatible: {status['sphinx_compatible']}")
                logger.info(f"  - Directory structure: {status['directory_structure_ok']}")
                logger.info(f"  - Main API updated: {status['main_api_updated']}")
                logger.info(f"  - Main index updated: {status['main_index_updated']}")
                logger.info(f"  - Cross-references valid: {status['cross_references_valid']}")
                
                if status['issues']:
                    logger.warning("Issues found:")
                    for issue in status['issues']:
                        logger.warning(f"  - {issue}")
                
                return 0
            else:
                logger.error("✗ Sphinx integration failed")
                return 1
                
    except Exception as e:
        logger.error(f"Error during Sphinx integration: {e}")
        return 1


def integrate_command(args) -> int:
    """Integrate enhanced JavaDoc into existing API documentation."""
    logger = get_logger('cli.integrate')
    
    try:
        manager = IntegrationManager()
        
        if getattr(args, 'recommendations', False):
            # Show recommendations
            recommendations = manager.get_integration_recommendations()
            
            logger.info("=" * 60)
            logger.info("JAVADOC INTEGRATION RECOMMENDATIONS")
            logger.info("=" * 60)
            
            rec_strategy = recommendations.get('recommended_strategy')
            if rec_strategy:
                logger.info(f"📋 Recommended Strategy: {rec_strategy.value.upper()}")
            else:
                logger.warning("❌ No strategy recommended - check prerequisites")
            
            reasons = recommendations.get('reasons', [])
            if reasons:
                logger.info("\\n✅ Reasons:")
                for reason in reasons:
                    logger.info(f"  - {reason}")
            
            considerations = recommendations.get('considerations', [])
            if considerations:
                logger.info("\\n⚠️  Considerations:")
                for consideration in considerations:
                    logger.info(f"  - {consideration}")
            
            next_steps = recommendations.get('next_steps', [])
            if next_steps:
                logger.info("\\n🚀 Next Steps:")
                for step in next_steps:
                    logger.info(f"  - {step}")
            
            return 0
        
        # Parse options
        strategy = IntegrationStrategy(getattr(args, 'strategy', 'hybrid'))
        dry_run = getattr(args, 'dry_run', False)
        
        options = {}
        if getattr(args, 'key_classes', None):
            options['key_classes'] = [c.strip() for c in args.key_classes.split(',')]
        
        if dry_run:
            logger.info("DRY RUN MODE: No files will be modified")
        
        logger.info(f"Starting JavaDoc integration using {strategy.value} strategy")
        
        # Run integration
        results = manager.integrate_enhanced_javadoc(strategy, dry_run, options)
        
        # Report results
        _report_integration_results(logger, results)
        
        return 0 if results.get('overall_success', False) else 1
        
    except Exception as e:
        logger.error(f"Integration failed: {e}")
        if getattr(args, 'verbose', 0) >= 2:
            import traceback
            traceback.print_exc()
        return 1


def _report_integration_results(logger, results: Dict[str, Any]):
    """Report integration results to user."""
    logger.info("=" * 60)
    logger.info("JAVADOC INTEGRATION SUMMARY")
    logger.info("=" * 60)
    
    summary = results.get('summary', {})
    strategy = summary.get('strategy', 'Unknown')
    success = summary.get('success', False)
    
    if success:
        logger.info(f"✅ JavaDoc integration completed successfully ({strategy})")
    else:
        logger.error(f"❌ JavaDoc integration failed ({strategy})")
    
    # Strategy-specific results
    if strategy == 'Docstring Enhancement':
        logger.info(f"📝 Files processed: {summary.get('files_processed', 0)}")
        logger.info(f"📝 Files enhanced: {summary.get('files_enhanced', 0)}")
        logger.info(f"📝 Total enhancements: {summary.get('total_enhancements', 0)}")
    
    elif strategy == 'RST Injection':
        logger.info(f"📄 RST files processed: {summary.get('files_processed', 0)}")
        logger.info(f"📄 RST files enhanced: {summary.get('files_enhanced', 0)}")
        logger.info(f"📄 Total integrations: {summary.get('total_integrations', 0)}")
    
    elif strategy == 'Sphinx Extension':
        logger.info(f"🔧 Extension configured: {summary.get('extension_configured', False)}")
        logger.info(f"🔧 conf.py updated: {summary.get('conf_py_updated', False)}")
    
    elif strategy == 'Hybrid Integration':
        logger.info(f"📝 Docstring enhancements: {summary.get('docstring_enhancements', 0)}")
        logger.info(f"🔧 Sphinx extension: {summary.get('sphinx_extension_configured', False)}")
        logger.info(f"📄 Enhanced pages: {summary.get('enhanced_pages_created', 0)}")
        logger.info(f"📁 Total files modified: {summary.get('total_files_modified', 0)}")
    
    # Error reporting
    errors = summary.get('errors', 0)
    if errors > 0:
        logger.warning(f"⚠️  Encountered {errors} errors during integration")
    
    # Next steps
    if success:
        logger.info("\\n🚀 Next Steps:")
        logger.info("  - Rebuild documentation: make html-integrated")
        logger.info("  - Review enhanced docstrings in key classes")
        logger.info("  - Test Sphinx extension functionality")
        if strategy == 'Hybrid Integration':
            logger.info("  - Check enhanced reference pages in api_enhanced_ref/")


def clean_command(args) -> int:
    """Clean generated files and caches."""
    logger = get_logger('cli.clean')
    
    try:
        cleaner = DocumentationCleaner()
        
        if getattr(args, 'cache_only', False):
            logger.info("Cleaning cache files only...")
            success = cleaner.clean_cache()
        elif getattr(args, 'generated_only', False):
            logger.info("Cleaning generated documentation only...")
            success = cleaner.clean_generated()
        else:
            logger.info("Cleaning all generated files and caches...")
            success = cleaner.clean_all()
        
        if success:
            logger.info("✓ Cleanup completed successfully")
            return 0
        else:
            logger.error("✗ Cleanup failed")
            return 1
            
    except Exception as e:
        logger.error(f"Cleanup failed: {e}")
        return 1


def _parse_components(components_str: Optional[str]) -> Optional[list]:
    """Parse comma-separated components string."""
    if not components_str:
        return None
    
    valid_components = {'javadoc', 'json', 'rst', 'index', 'sphinx'}
    components = [c.strip().lower() for c in components_str.split(',')]
    
    invalid = set(components) - valid_components
    if invalid:
        raise ValueError(f"Invalid components: {invalid}. Valid: {valid_components}")
    
    return components


def _parse_classes(classes_str: Optional[str]) -> Optional[list]:
    """Parse comma-separated classes string."""
    if not classes_str:
        return None
    
    return [c.strip() for c in classes_str.split(',')]


def _report_generation_results(logger, success: bool, results: Dict[str, Any], elapsed_time: float):
    """Report generation results to user."""
    logger.info("=" * 60)
    logger.info("DOCUMENTATION GENERATION SUMMARY")
    logger.info("=" * 60)
    
    if success:
        logger.info("✓ Documentation generation completed successfully")
    else:
        logger.error("✗ Documentation generation failed")
    
    logger.info(f"⏱️  Total time: {elapsed_time:.2f} seconds")
    
    # Report statistics
    stats = results.get('statistics', {})
    if stats:
        logger.info("\n📊 Statistics:")
        logger.info(f"  - Classes processed: {stats.get('classes_processed', 0)}")
        logger.info(f"  - Methods documented: {stats.get('methods_documented', 0)}")
        logger.info(f"  - Files generated: {stats.get('files_generated', 0)}")
        logger.info(f"  - Errors encountered: {stats.get('errors', 0)}")
        logger.info(f"  - Warnings: {stats.get('warnings', 0)}")
    
    # Report generated files
    generated_files = results.get('generated_files', {})
    if generated_files:
        logger.info("\n📁 Generated Files:")
        for file_type, files in generated_files.items():
            if isinstance(files, list):
                logger.info(f"  - {file_type}: {len(files)} files")
            else:
                logger.info(f"  - {file_type}: {files}")
    
    # Report issues
    issues = results.get('issues', [])
    if issues:
        logger.warning(f"\n⚠️  Issues ({len(issues)}):")
        for issue in issues[:10]:  # Show first 10 issues
            logger.warning(f"  - {issue}")
        if len(issues) > 10:
            logger.warning(f"  ... and {len(issues) - 10} more issues")


def _print_validation_report(logger, report: Dict[str, Any]):
    """Print validation report to console."""
    logger.info("=" * 60)
    logger.info("VALIDATION REPORT")
    logger.info("=" * 60)
    
    # Overall status
    status = report.get('overall_status', 'unknown')
    if status == 'passed':
        logger.info("✓ Overall Status: PASSED")
    elif status == 'warnings':
        logger.warning("⚠ Overall Status: WARNINGS")
    else:
        logger.error("✗ Overall Status: FAILED")
    
    # Summary statistics
    summary = report.get('summary', {})
    logger.info(f"\n📊 Summary:")
    logger.info(f"  - Total issues: {summary.get('total_issues', 0)}")
    logger.info(f"  - Files validated: {summary.get('files_validated', 0)}")
    logger.info(f"  - Classes checked: {summary.get('classes_checked', 0)}")
    logger.info(f"  - Methods checked: {summary.get('methods_checked', 0)}")
    logger.info(f"  - References checked: {summary.get('references_checked', 0)}")
    
    # Configuration validation
    config_status = report.get('configuration', {})
    _print_validation_section(logger, "🔧 Configuration", config_status)
    
    # Dependencies validation
    deps_status = report.get('dependencies', {})
    _print_validation_section(logger, "📦 Dependencies", deps_status)
    
    # Documentation validation
    docs_status = report.get('documentation', {})
    _print_validation_section(logger, "📚 Documentation Files", docs_status)
    
    # Completeness validation
    completeness_status = report.get('completeness', {})
    _print_validation_section(logger, "📝 Documentation Completeness", completeness_status)
    
    # Cross-references validation
    cross_ref_status = report.get('cross_references', {})
    _print_validation_section(logger, "🔗 Cross-References", cross_ref_status)
    
    # Overall recommendations
    recommendations = report.get('recommendations', [])
    if recommendations:
        logger.info(f"\n💡 Recommendations:")
        for rec in recommendations:
            if rec.startswith('CRITICAL:'):
                logger.error(f"  - {rec}")
            elif rec.startswith('IMPROVEMENT:'):
                logger.warning(f"  - {rec}")
            else:
                logger.info(f"  - {rec}")


def _print_validation_section(logger, title: str, section_data: Dict[str, Any]):
    """Print a validation section with issues and recovery suggestions."""
    status = section_data.get('status', 'unknown')
    status_icon = "✓" if status == 'passed' else ("⚠" if status == 'warnings' else "✗")
    
    logger.info(f"\n{title}: {status_icon} {status.upper()}")
    
    # Print statistics if available
    stats = section_data.get('statistics', {})
    if stats:
        logger.info("  Statistics:")
        for key, value in stats.items():
            if isinstance(value, int):
                logger.info(f"    - {key.replace('_', ' ').title()}: {value}")
    
    # Print issues
    issues = section_data.get('issues', [])
    if issues:
        logger.warning(f"  Issues ({len(issues)}):")
        for issue in issues[:5]:  # Show first 5 issues
            logger.warning(f"    - {issue}")
        if len(issues) > 5:
            logger.warning(f"    ... and {len(issues) - 5} more issues")
    
    # Print recovery suggestions
    suggestions = section_data.get('recovery_suggestions', [])
    if suggestions:
        logger.info(f"  Recovery Suggestions:")
        for suggestion in suggestions[:3]:  # Show first 3 suggestions
            logger.info(f"    - {suggestion}")
        if len(suggestions) > 3:
            logger.info(f"    ... and {len(suggestions) - 3} more suggestions")


if __name__ == '__main__':
    sys.exit(main())