#!/usr/bin/env python3
"""
Prepares PySNT for deployment by generating stubs and API docs.

This script:
1. Run quality control validations
2. Generate type stub files (.pyi) from cached signatures
3. Generate API documentation
4. Build HTML documentation

Uses the clean cache-only stub generation approach.
Placeholder classes are created automatically at runtime via setup_module_classes().
"""

import argparse
import subprocess
import sys
from datetime import datetime
from pathlib import Path


def run_command(cmd, description, cwd=None):
    """Run a command and handle errors gracefully."""
    print(f"🔄 {description}...")

    try:
        result = subprocess.run(
            cmd,
            check=True,
            capture_output=True,
            text=True,
            cwd=cwd
        )

        if result.stdout.strip():
            print(result.stdout)

        print(f"✅ {description} completed")
        return True

    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed")
        if e.stdout:
            print("STDOUT:", e.stdout)
        if e.stderr:
            print("STDERR:", e.stderr)
        return False
    except Exception as e:
        print(f"❌ {description} failed: {e}")
        return False


def main():
    """Main deployment script."""
    parser = argparse.ArgumentParser(
        description="Deploy PySNT - generate stubs and documentation"
    )
    parser.add_argument(
        "--skip-stubs",
        action="store_true",
        help="Skip stub generation (faster, use existing stubs)"
    )
    parser.add_argument(
        "--skip-docs",
        action="store_true",
        help="Skip documentation generation"
    )
    parser.add_argument(
        "--skip-enhanced-docs",
        action="store_true",
        help="Skip enhanced API documentation (JavaDoc integration)"
    )
    parser.add_argument(
        "--force-enhanced-docs",
        action="store_true",
        help="Force regeneration of enhanced API documentation"
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Show detailed output"
    )

    args = parser.parse_args()

    # Get paths
    script_dir = Path(__file__).parent
    project_root = script_dir.parent.parent  # dev/scripts -> dev -> project_root
    docs_dir = project_root / "docs"

    print("🚀 PySNT Deployment Script")
    print("=" * 30)
    print(f"📁 Project root: {project_root}")

    success_count = 0
    total_tasks = 0

    # 0. Run quality control validation
    total_tasks += 1
    cmd = [sys.executable, str(script_dir / "pysnt_utils.py"), "--qc"]
    if args.verbose:
        cmd.append("--verbose")
    
    if run_command(cmd, "Running quality control validation"):
        success_count += 1
    else:
        print("⚠️ Quality control validation failed, but continuing...")

    # 1. Check cache status first
    if not args.skip_stubs:
        total_tasks += 1
        cmd = [sys.executable, str(script_dir / "generate_stubs.py"), "--check-cache"]
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            import re
            missing = [ln.strip() for ln in result.stdout.splitlines()
                       if re.search(r"Missing cache: [1-9]\d*/", ln)]  # the summary also prints "0/N"
            if missing:
                print("⚠️  Some cached signatures are missing: " + "; ".join(missing))
                print("💡 Consider running: python dev/scripts/extract_class_signatures.py --all-classes --prune")
                print("🔄 Proceeding with available caches...")
        except:
            pass  # Continue anyway
        
        success_count += 1  # Cache check always succeeds

    # 2. Generate stubs from cache
    if not args.skip_stubs:
        total_tasks += 1
        cmd = [sys.executable, str(script_dir / "generate_stubs.py"), "--overwrite"]
        if args.verbose:
            cmd.append("--verbose")

        if run_command(cmd, "Generating stub files from cache"):
            success_count += 1
        else:
            print("⚠️ Stub generation failed, but continuing...")

    # 3. Generate API documentation (unless skipped)
    if not args.skip_docs:
        total_tasks += 1
        cmd = [sys.executable, str(script_dir / "generate_api_docs.py")]

        if run_command(cmd, "Generating API documentation"):
            success_count += 1
        
        # 3a. Generate enhanced API documentation (unless skipped)
        if not args.skip_enhanced_docs:
            total_tasks += 1
            print("\n" + "=" * 50)
            print("Enhanced API Documentation (JavaDoc Integration)")
            print("=" * 50)
            
            try:
                # Import and run enhanced docs directly
                sys.path.insert(0, str(script_dir))
                from enhanced_api_docs.orchestrator import DocumentationOrchestrator
                from enhanced_api_docs.config import config as enhanced_config
                
                # Check if prerequisites are met
                if enhanced_config.validate():
                    orchestrator = DocumentationOrchestrator(
                        dry_run=False,
                        show_progress=True,
                        verbose=1 if args.verbose else 0
                    )
                    
                    generation_options = {
                        'force': args.force_enhanced_docs,
                        'incremental': not args.force_enhanced_docs,
                        'components': ['json', 'rst', 'index', 'sphinx'],
                        'classes': None,
                        'output_format': 'rst',
                        'validate_after': True,
                        'toctree_enabled': True,
                        'toctree_maxdepth': 3
                    }
                    
                    javadoc_jar = enhanced_config.get_path('javadoc.source_zip')
                    print(f"📚 JavaDoc source: {javadoc_jar.name} "
                          f"(modified {datetime.fromtimestamp(javadoc_jar.stat().st_mtime):%Y-%m-%d %H:%M}). "
                          "Copy a fresh SNT-*-javadoc.jar to dev/scripts (or set PYSNT_JAVADOC) if the API changed")
                    print("🚀 Generating enhanced API documentation...")
                    success, results = orchestrator.generate_documentation(generation_options)
                    
                    if success:
                        stats = results.get('statistics', {})
                        print(f"✅ Enhanced API docs: {stats.get('classes_processed', 0)} classes, "
                              f"{stats.get('methods_documented', 0)} methods")
                        success_count += 1
                    else:
                        print("⚠️ Enhanced API documentation had issues, but continuing...")
                else:
                    print("⚠️ Enhanced API docs prerequisites not met (missing JavaDoc/stubs)")
                    print("   Skipping enhanced documentation - this is optional")
                    success_count += 1  # Don't fail deployment for optional feature
                    
            except ImportError:
                print("⚠️ Enhanced API documentation system not available")
                print("   This is optional - deployment will continue")
                success_count += 1  # Don't fail deployment for optional feature
            except Exception as e:
                print(f"⚠️ Enhanced API documentation failed: {e}")
                if args.verbose:
                    import traceback
                    traceback.print_exc()
                print("   Continuing with standard documentation...")
                success_count += 1  # Don't fail deployment for optional feature

        # 4. Build HTML documentation
        total_tasks += 1
        if docs_dir.exists():
            cmd = ["make", "html"]
            if run_command(cmd, "Building HTML documentation", cwd=docs_dir):
                success_count += 1
        else:
            print("⚠️  Docs directory not found, skipping HTML build")

    # Summary
    print(f"\n📊 Deployment Summary")
    print("=" * 25)
    print(f"✅ Completed: {success_count}/{total_tasks} tasks")

    if success_count == total_tasks:
        print("🎉 Deployment completed successfully!")
        print("\n💡 Generated files:")
        if not args.skip_stubs:
            print("  • Type stub files (.pyi) from cached signatures")
            print("  • High-quality stubs for classes with cached data")
        if not args.skip_docs:
            print("  • Standard API documentation (.rst files)")
            if not args.skip_enhanced_docs:
                print("  • Enhanced API documentation with JavaDoc integration")
                print("    - Enhanced class docstrings")
                print("    - Detailed reference pages (*_doc.rst)")
                print("    - Alphabetical method index (method_index.html)")
                print("    - Class index (class_index.html)")
                print("    - Constants index (constants_index.html)")
            print("  • HTML documentation (docs/_build/html/)")
        
        print("\n💡 Note: Placeholder classes are generated automatically at runtime")
        print("  • No manual sync or placeholder generation needed")
        print("  • Cache-only stub generation for predictable results")
        print("  • Run extract_class_signatures.py to improve coverage")
        
        if not args.skip_docs and not args.skip_enhanced_docs:
            print("\n💡 Enhanced API Documentation:")
            print("  • View method index: docs/_build/html/method_index.html")
            print("  • View class index: docs/_build/html/class_index.html")
            print("  • View constants index: docs/_build/html/constants_index.html")
            print("  • Detailed class docs: docs/pysnt/*_doc.rst")
            print("  • To update JavaDoc: copy a fresh SNT-*-javadoc.jar (mvn javadoc:jar) to dev/scripts, "
                  "or set PYSNT_JAVADOC (see dev/scripts/README.md)")

        print(f"\nDone.")
        return 0
    else:
        failed_tasks = total_tasks - success_count
        print(f"⚠️  {failed_tasks} task(s) failed")
        print("Check the output above for details")
        return 1


if __name__ == "__main__":
    sys.exit(main())
