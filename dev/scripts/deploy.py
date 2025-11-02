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
            if "Missing cache:" in result.stdout and "45/88" in result.stdout:
                print("⚠️  Many cached signatures are missing!")
                print("💡 Consider running: python dev/scripts/extract_class_signatures.py --all-classes")
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
            print("  • API documentation (.rst files)")
            print("  • HTML documentation (docs/_build/html/)")
        
        print("\n💡 Note: Placeholder classes are generated automatically at runtime")
        print("  • No manual sync or placeholder generation needed")
        print("  • Cache-only stub generation for predictable results")
        print("  • Run extract_class_signatures.py to improve coverage")

        print(f"\nDone.")
        return 0
    else:
        failed_tasks = total_tasks - success_count
        print(f"⚠️  {failed_tasks} task(s) failed")
        print("Check the output above for details")
        return 1


if __name__ == "__main__":
    sys.exit(main())
