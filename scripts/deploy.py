#!/usr/bin/env python3
"""
Prepares PySNT for deployment by generating stubs and API docs.
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

    # 1. Generate stubs (Python + Java with some fallback strategies)
    if not args.skip_java:
        total_tasks += 1
        cmd = [sys.executable, str(script_dir / "generate_stubs.py"), "--overwrite"]
        if args.verbose:
            cmd.append("--verbose")

        if run_command(cmd, "Generating stub files (Java + Python)"):
            # Also sync Python classes with stub files for better IDE support
            sync_cmd = [sys.executable, str(script_dir / "sync_python_classes.py")]
            if run_command(sync_cmd, "Syncing Python classes with stub files"):
                success_count += 1
            else:
                print("⚠️  Python class sync failed, but stubs are still generated")
                success_count += 1  # Still count as success since stubs are generated
        else:
            print("⚠️ stub generation failed, but continuing...")

    else:
        # Python-only mode
        total_tasks += 1
        cmd = [sys.executable, str(script_dir / "generate_stubs.py"), "--overwrite"]
        if args.verbose:
            cmd.append("--verbose")

        if run_command(cmd, "Generating Python stub files"):
            # Also sync Python classes with stub files for better IDE support
            sync_cmd = [sys.executable, str(script_dir / "sync_python_classes.py")]
            if run_command(sync_cmd, "Syncing Python classes with stub files"):
                success_count += 1
            else:
                print("⚠️  Python class sync failed, but stubs are still generated")
                success_count += 1  # Still count as success since stubs are generated

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
        print("  • stub files (.pyi) with complete method signatures")
        if not args.skip_java:
            print("  • Java class stubs using reflection (most complete available)")
        if not args.skip_docs:
            print("  • API documentation (.rst files)")
            print("  • HTML documentation (docs/_build/html/)")

        print(f"\nDone.")
        return 0
    else:
        failed_tasks = total_tasks - success_count
        print(f"⚠️  {failed_tasks} task(s) failed")
        print("Check the output above for details")
        return 1


if __name__ == "__main__":
    sys.exit(main())
