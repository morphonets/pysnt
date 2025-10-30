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

## Dynamic Placeholder System

Placeholder classes are generated automatically: `common_module.py` _should_ create placeholder classes for all modules
using `setup_module_classes()`. This means:

- No manual placeholder generation needed
- At runtime import declarations can be placed _before_ `pysnt.initialize()`. e.g.,
  `from pysnt.analysis import TreeStatistics` works before `TreeStatistics()` is called.

How it works:
1. Classes to `CURATED_CLASSES` or `EXTENDED_CLASSES` in module `__init__.py` as usual
2. Each module calls `setup_module_classes()` in its `__init__.py`
3. Dynamic placeholders are created in bulk for all curated classes. No need to run placeholder generation scripts
4. When `pysnt.initialize()` is called, placeholders redirect to the actual Java classes
5. Type stubs (`.pyi`) are still generated separately for IDE support

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

### `pysnt_utils.py`

**Scope:**
  - Quality control validation (detects duplicate classes, naming issues, etc.)
  - Import depth fixing for `common_module` imports
  - Cleaning up unused typing imports in `.pyi` files
  - Module configuration analysis and reporting

**Available Options:**
  - `--qc`: Run quality control validation
  - `--fix-imports`: Fix import depths for common_module imports
  - `--clean-pyi-imports`: Clean up unused typing imports in .pyi files
  - `--analyze`: Analyze module configurations and show statistics
  - `--dry-run`: Preview changes without modifying files
  - `--verbose`: Enable detailed logging

```bash
# Quality control validation
python scripts/pysnt_utils.py --qc

# Fix import depths
python scripts/pysnt_utils.py --fix-imports

# Clean unused typing imports
python scripts/pysnt_utils.py --clean-pyi-imports

# Analyze module configurations
python scripts/pysnt_utils.py --analyze --verbose
```

### `generate_stubs.py`

**Scope:**
  - Generates type stub files (`.pyi`) for IDE autocompletion and type checking
  - **Independent of runtime placeholders** (which are now handled automatically)
  - Dynamically discovers classes from `CURATED_CLASSES` in all modules
  - Strategy:
    - **Java Reflection**: Extracts actual method signatures from SNT Java classes
    - **Fallback Stubs**: Uses basic stubs with `__getattr__` when reflection fails
    - **Python AST**: Analyzes Python code for function signatures
  - **Type Hints**: Provides proper Python type annotations for Java methods
  - **Overloaded Methods**: Handles Java method overloading with `@overload` decorators

**Options:**
  - `--overwrite`: Overwrite existing stub files
  - `--verbose`: Verbose output

```bash
python scripts/generate_stubs.py [--verbose] [--overwrite]
```
This generates `.pyi` files for IDEs, not runtime placeholder classes.
Runtime placeholders are handled automatically by `setup_module_classes()`.


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
# Quality control validation
python scripts/pysnt_utils.py --qc
# Fix import depths
python scripts/pysnt_utils.py --fix-imports
# Analyze module configurations
python scripts/pysnt_utils.py --analyze
# Quick build without docs
python scripts/deploy.py --skip-docs
# Complete build with documentation
python scripts/deploy.py
# Generate stubs only
python scripts/generate_stubs.py --verbose
# Generate docs only
python scripts/generate_api_docs.py
```

## Development Tools

See the [`dev/`](../dev/) directory for development tools and templates:

- **`dev/placeholder_template.py`**: Template for creating new PySNT module `__init__.py` files
- **`dev/create_module.py`**: Script to quickly create new modules from template
- **`dev/README.md`**:  Guide for adding new SNT packages

### Quick Module Creation

```bash
# Create a new module (uses dynamic placeholder system)
python dev/create_module.py analysis.morphology

# Create with predefined classes (automatically creates dynamic placeholders)
python dev/create_module.py analysis.morphology \
  --curated MorphologyAnalyzer ShapeMetrics \
  --extended AdvancedMorphology DetailedMetrics
```