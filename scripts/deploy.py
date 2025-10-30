#!/usr/bin/env python3
"""
Prepares PySNT for deployment by generating stubs and API docs.

This script:
1. Generate type stub files (.pyi) for IDE support
2. Generate API documentation
3. Run some quality control validations

Placeholder classes are created automatically at runtime via setup_module_classes().
No manual sync or placeholder generation is required.
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
        "--skip-java",
        action="store_true",
        help="Skip Java stub generation (faster, no JVM required)"
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
    project_root = script_dir.parent
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

    # 1. Generate stubs (Python + Java with some fallback strategies)
    if not args.skip_java:
        total_tasks += 1
        cmd = [sys.executable, str(script_dir / "generate_stubs.py"), "--overwrite"]
        if args.verbose:
            cmd.append("--verbose")

        if run_command(cmd, "Generating stub files (Java + Python)"):
            success_count += 1
        else:
            print("⚠️ stub generation failed, but continuing...")

    else:
        # Python-only mode
        total_tasks += 1
        cmd = [sys.executable, str(script_dir / "generate_stubs.py"), "--overwrite"]
        if args.verbose:
            cmd.append("--verbose")

        if run_command(cmd, "Generating Python stub files"):
            success_count += 1

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
        print("  • Type stub files (.pyi) with complete method signatures")
        if not args.skip_java:
            print("  • Java class stubs using reflection (most complete available)")
        if not args.skip_docs:
            print("  • API documentation (.rst files)")
            print("  • HTML documentation (docs/_build/html/)")
        
        print("\n💡 Note: Placeholder classes are generated automatically at runtime")
        print("  • No manual sync or placeholder generation needed")
        print("  • Import timing issues resolved with dynamic placeholders")
        print("  • Simplified deployment process")

        print(f"\nDone.")
        return 0
    else:
        failed_tasks = total_tasks - success_count
        print(f"⚠️  {failed_tasks} task(s) failed")
        print("Check the output above for details")
        return 1


if __name__ == "__main__":
    sys.exit(main())
