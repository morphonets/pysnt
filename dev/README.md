# PySNT Development Tools

Development tools and templates for PySNT.

## Contents

### `placeholder_template.py`
Template for creating new PySNT module `__init__.py` files with consistent structure.
See the `deploy.py` script for how these templates become populated with wrapper classes via Java reflection.

## To Add New SNT Package

1. Create Module Structure
  ```bash
  # Example: Adding morphology analysis module
  mkdir -p src/pysnt/analysis/morphology
  ```

2. Copy Template
  ```bash
  cp dev/placeholder_template.py src/pysnt/analysis/morphology/__init__.py
  ```

3. Configure Module
  Edit the new `__init__.py` file:

  ```python
    # 1. Update module docstring
    
    # 2. Fill-in the lists of public classes in the package
    CURATED_CLASSES = [
        "MorphologyAnalyzer",  # Most important classes
        "ShapeMetrics",
        "BranchAnalyzer"
    ]
    
    EXTENDED_CLASSES = [
        "AdvancedMorphology",  # Less common classes
        "DetailedMetrics",
        "InternalUtils"
    ]
    
    # Set package name
    _module_funcs = setup_module_classes(
        package_name="sc.fiji.snt.analysis.morphology",  # ← Edit this
        curated_classes=CURATED_CLASSES,
        extended_classes=EXTENDED_CLASSES,
        globals_dict=globals(),
    )
    
    # Set module path
    __getattr__ = _module_funcs['create_getattr']('pysnt.analysis.morphology')  # ← Edit this
  ```

4. Generate Placeholders
  ```bash
  python scripts/generate_placeholders.py
  ```

5. Test
  ```bash
  python -c "
  import src.pysnt.new.module as mod
  print(f'Curated: {mod.get_curated_classes()}')
  print(f'Extended: {mod.get_extended_classes()}')
  print(f'Total: {len(mod.get_available_classes())} classes')
  "
  ```

  ```bash
  # Run placeholder generation and test
  python scripts/generate_placeholders.py
  python -c "
  import src.pysnt.new.module as mod
  print('All tests passed!')
  print(f'Module ready with {len(mod.get_available_classes())} classes')
  "
  ```

6. Update Parent Module (as needed)
If adding a submodule, update the parent's `__init__.py`:

```python
# In parent src/pysnt/analysis/__init__.py
from . import morphology

# Update __getattr__ to handle submodules
__getattr__ = _module_funcs['create_getattr']('pysnt.analysis', submodules=['morphology'])   # ← Edit this
```

## Configuration Options

### Basic Configuration
```python
# Minimal setup for simple modules
_module_funcs = setup_module_classes(
    package_name="sc.fiji.snt.your.package",
    curated_classes=CURATED_CLASSES,
    extended_classes=EXTENDED_CLASSES,
    globals_dict=globals(),
)
```

### Advanced Configuration
```python
# Advanced setup with additional options
_module_funcs = setup_module_classes(
    package_name="sc.fiji.snt.your.package",
    curated_classes=CURATED_CLASSES,
    extended_classes=EXTENDED_CLASSES,
    globals_dict=globals(),
    discovery_packages=["sc.fiji.snt", "sc.fiji.snt.util"],  # Search multiple packages
    include_interfaces=True,  # Include Java interfaces
)
```

### Submodule Support
```python
# For modules with submodules
from . import submodule1, submodule2

__getattr__ = _module_funcs['create_getattr']('pysnt.your.module', submodules=['submodule1', 'submodule2'])
```

## Best Practices

### Class Organization
- Curated classes: Most commonly used classes
- Extended classes: All other classes in the package

### Naming Conventions
- Package names: Follow Java package structure (`sc.fiji.snt.analysis.morphology`)
- Module paths: Follow Python import structure (`pysnt.analysis.morphology`)
- Class names: Use exact Java class names

### Documentation
- Module docstring: Include link to Javadoc package summary
- Class lists: Add comments explaining what each class does
- Examples: If possible, orovide usage examples in docstrings
