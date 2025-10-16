# Scripts for Building & Deploying PySNT

## Setup

Access to a Fiji install running SNT is required:

```python
import pysnt.setup_utils as setup

# Configuration management
setup.show_config_status()
setup.set_fiji_path("/Applications/Fiji.app")
setup.auto_detect_and_configure()

# Quick validation for scripts
if not setup.is_fiji_valid():
    print("Fiji not configured!")
    exit(1)

# Detailed status
status = setup.get_fiji_status()
if not status['valid']:
    print(f"Issues: {status['issues']}")

# Reset configuration
setup.reset_fiji_path()  # Clears config + env var
setup.clear_fiji_path(reset_env=True)  # Same as above
```

## Scripts

### `deploy.py`

**Scope:**
  - Generates stub files (`.pyi`) for Java classes: Type definitions for IDE support
  - Syncs Python classes with stub files with placeholder methods
  - Generates API files (`.rst`): Sphinx documentation files

**Options:**
  - `--skip-docs`: Skip API documentation generation

```bash
python scripts/deploy.py [--skip-docs]
```


### `generate_stubs.py`

**Scope:**
  - Generates TypeScript-style stub files (`.pyi`) for Java classes using real Java reflection when possible:
  - Strategy:
    - Java Reflection: Extracts method signatures from SNT Java classes first
    - Fallbacks: Uses basic stubs with `__getattr__` when reflection is unavailable/fails
  - Type Hints: Provides proper Python type annotations for Java methods
  - Overloaded Methods: Handles Java method overloading with `@overload` decorators

**Options:**
  - `--overwrite`: Overwrite existing stub files
  - `--Verbose`: Verbose output

```bash
python scripts/generate_stubs.py [--verbose] [--overwrite]
```


### `sync_python_classes.py`

**Scope:**
  - Synchronizes Python wrapper classes with their stub files to ensure IDE autocompletion works properly:
    1. Scans all `.pyi` stub files for method definitions
    2. Checks corresponding Python classes for missing methods
    3. Adds placeholder methods with proper signatures
    4. Maintains runtime error handling for uninitialized SNT

```bash
python scripts/sync_python_classes.py
```


### `generate_api_docs.py`

**Scope:**
  - Uses `sphinx-apidoc` to auto-generate `.rst` API documentation files

```bash
python scripts/generate_api_docs.py
```

### Examples
```bash
# Fiji configuration management
python -m pysnt.setup_utils --status
python -m pysnt.setup_utils --auto-detect
python -m pysnt.setup_utils --set /Applications/Fiji.app
python -m pysnt.setup_utils --clear
python -m pysnt.setup_utils --reset
python -m pysnt.setup_utils --check
# Quick build without docs
python scripts/deploy.py --skip-docs
# Complete build with documentation
python scripts/deploy.py
# Generate stubs only
python scripts/generate_stubs.py --verbose
# Sync classes only
python scripts/sync_python_classes.py
# Generate docs only
python scripts/generate_api_docs.py
```
