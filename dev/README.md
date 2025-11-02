# PySNT Development Tools

Development tools and templates for PySNT.

## Overview
- Curate vs Extended classes: In theory, all SNT classes would be treated the same. In practice, we split them in two 
  groups: 
  - Curate classes: Most commonly used. These are 1st class citizens with functional autocompletion
  - Extended classes: These are either 'problematic' classes (e.g., objects that cannot be constructed in headless env.).
    These won't have much of auto-completion. Users need to use java_utils to explore extended classes:
    ```python
    import pysnt
    pysnt.initialize()
    # Get all methods from TreeStatistics
    methods = pysnt.get_methods('TreeStatistics')
    # Find all members containing 'length'
    results = pysnt.find_members('TreeStatistics', 'length')
    # Get static fields (constants)
    constants = pysnt.get_fields('TreeStatistics', static_only=True)
    ```
- Package names: Follow Java package structure (`sc.fiji.snt.analysis.morphology`)
- Module paths: Follow Python import structure (`pysnt.analysis.morphology`)
- Class names: Use exact Java class names. Reflection converters use underscore notation (OuterClass_InnerClass)
- Module docstring: Include link to Javadoc package summary
- `placeholder_template.py`: Is the template for creating new PySNT module `__init__.py` files with consistent structure
- See the `dev/scripts/` directory for build and deployment scripts
- Use `dev/scripts/extract_class_signatures.py` and `dev/scripts/generate_stubs.py` for type stub generation


## To Add a New SNT Package

### Option 1 (Recommended): Using `create_module.py`

Basic examples:
```bash
# Create a basic morphology analysis module
python dev/create_module.py analysis.morphology
# Create nested modules
python dev/create_module.py analysis.morphology.advanced
```
What this creates:
- __init__.py files that now need to be manually edited

Examples with Class Lists:
```bash
python dev/create_module.py analysis.morphology \
  --curated Class1Name Class2Name Class3Name \
  --extended Class4Name Class5Name Class6Name 
```
What this creates:
- Module: `src/pysnt/analysis/morphology/__init__.py` (Java package: sc.fiji.snt.analysis.morphology)
- Curated classes (always available): Class1Name, Class2Name, Class3Name
- Extended classes (on-demand): Class4Name, Class5Name, Class6Name

Examples with Inner Classes:
```bash
python dev/create_module.py analysis.morphology \
  --curated Class1Name_Config  \
  --extended Class2Name_Config
```
What this creates:
- Module: `src/pysnt/analysis/morphology/__init__.py` (Java package: sc.fiji.snt.analysis.morphology)
- Curated classes (always available): Class1Name$Config
- Extended classes (on-demand): Class2Name$Config

After creating any module:
- Edit the generated file
- Update docstrings
- Remove template sections:
- Delete the template checklist
- Generate type stubs:
  ```bash
  python dev/scripts/extract_class_signatures.py --all-classes --verbose  # Extract signatures
  python dev/scripts/generate_stubs.py --verbose --overwrite              # Generate stubs
  ```
- Test the module:
  ```bash
  python -c "import src.pysnt.analysis.morphology; print('Module works!')"
  ```

### Option 2 (Manually)

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

4. Generate Type Stubs
  ```bash
  python dev/scripts/extract_class_signatures.py --all-classes --verbose
  python dev/scripts/generate_stubs.py --verbose --overwrite
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
  # Generate type stubs and test
  python dev/scripts/generate_stubs.py --verbose
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
    package_name="sc.fiji.snt.new.package",
    curated_classes=CURATED_CLASSES,
    extended_classes=EXTENDED_CLASSES,
    globals_dict=globals(),
)
```

### Advanced Configuration
```python
# Advanced setup with additional options
_module_funcs = setup_module_classes(
    package_name="sc.fiji.snt.new.package",
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

__getattr__ = _module_funcs['create_getattr']('pysnt.new.module', submodules=['submodule1', 'submodule2'])
```