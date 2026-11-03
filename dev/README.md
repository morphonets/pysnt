# PySNT Development Tools

Development tools and templates for PySNT.

## Overview
- Curated vs Extended classes: In theory, all SNT classes would be treated the same. In practice, we split them in two
  groups:
  - Curated classes: Most commonly used. These are 1st class citizens with functional autocompletion (type stubs)
  - Extended classes: Less common, or 'problematic' classes (e.g., objects that cannot be constructed in headless env.).
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
- Only public classes and interfaces should be curated. Nested classes follow their outer class (access them with
  `get_class("Outer.Inner")`)
- Which SNT packages/classes are listed, skipped, curated or extended is decided by `dev/scripts/class_policy.toml`
- See [dev/scripts/README.md](scripts/README.md) for the details of every script


## Keeping PySNT in Sync with SNT

PySNT's `major.minor` version matches the SNT release it targets (PySNT 5.1.x targets SNT 5.1.x). The patch number is
independent. The current targets live in two places that must be updated together:

| What                                   | Where                                  |
|----------------------------------------|----------------------------------------|
| PySNT version                          | `__version__` in `src/pysnt/__init__.py` (`pyproject.toml` reads it) |
| SNT version resolved from Maven        | `DEFAULT_SNT_VERSION` in `src/pysnt/_endpoints.py` |

Users can override the SNT version with `pysnt.initialize(snt_version="x.y.z")` or the `SNT_VERSION` environment
variable, or use a local Fiji (`fiji_path`, `FIJI_PATH`). PySNT only warns when the loaded SNT differs in
major.minor; `pysnt.snt_version()` reports the one in use.

### After changing SNT's API (or targeting a new SNT version)

Prerequisites: JDK 21, and, if working on an unreleased SNT, `mvn clean install -DskipTests` in the SNT repository
followed by `rm -rf ~/.jgo ~/.cache/jgo` (jgo caches resolved snapshots, so the old jar would be served otherwise).
Add `--snt-version X.Y.Z` to the scripts below (or set `SNT_VERSION`) to target a specific release.

```bash
python dev/scripts/snt_inventory.py                 # 1. List SNT's public API; reports new/removed/deprecated classes
python dev/scripts/sync_module_lists.py             # 2. Dry run: what would change in the CURATED/EXTENDED lists?
python dev/scripts/sync_module_lists.py --apply     #    ...apply it (edit class_policy.toml first to change decisions)
python dev/scripts/extract_class_signatures.py --all-classes --prune -v   # 3. Reflect curated classes -> STUBS/*.json
python dev/scripts/generate_stubs.py --overwrite -v                       # 4. STUBS -> .pyi (stamped with SNT version)
python dev/scripts/deploy.py --force-enhanced-docs  # 5. API docs (needs SNT's javadoc jar in dev/scripts/, see below)
python -m pytest tests -q                           # 6. Check
```
Notes:
- New SNT packages need a new module first (see below); `sync_module_lists.py` reports them but does not create them.
- Each cached signature records the SNT version it came from. `generate_stubs.py --check-cache` shows which are stale.
- Javadoc jar: `cd SNT && mvn javadoc:jar`, then copy `target/SNT-<version>-javadoc.jar` to `dev/scripts/`.
- Deprecated SNT members are emitted as `@deprecated` in the stubs so IDEs flag them.

### Cutting a PySNT release
1. Publish (or pick) the SNT release being targeted and set `DEFAULT_SNT_VERSION` to it (no `-SNAPSHOT`: CI and
   users resolve it from Maven, snapshots would skip the JVM tests)
2. Run the sync workflow above, then `python -m pytest tests`
3. Set `__version__` in `src/pysnt/__init__.py` (`major.minor` = SNT's; bump the patch for PySNT-only fixes)
4. Make sure CI is green (tests, lowest declared dependencies, docs)


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
- Remove template sections and the template checklist
- Let `sync_module_lists.py` fill the class lists from SNT's API (see above) instead of typing them
- Generate type stubs:
  ```bash
  python dev/scripts/extract_class_signatures.py --all-classes --verbose  # Extract signatures
  python dev/scripts/generate_stubs.py --verbose --overwrite              # Generate stubs
  ```
- Test the module:
  ```bash
  python -c "import pysnt.analysis.morphology; print('Module works!')"
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
  import pysnt.new.module as mod
  print(f'Curated: {mod.get_curated_classes()}')
  print(f'Extended: {mod.get_extended_classes()}')
  print(f'Total: {len(mod.get_available_classes())} classes')
  "
  ```

  ```bash
  # Generate type stubs and test
  python dev/scripts/generate_stubs.py --verbose
  python -c "
  import pysnt.new.module as mod
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

## Constructor Exception Handling Guide

The `handle_constructor_exceptions()` function in `src/pysnt/common_module.py` provides a centralized way to handle Java constructor issues that arise from the Python-Java bridge.

### Common Issues

1. Varargs Constructor Selection
**Problem**: Python calls `Constructor(args, String...)` with empty varargs instead of `Constructor(args)`
**Example**: `MultiTreeStatistics(Collection)` vs `MultiTreeStatistics(Collection, String...)`

2. Overloaded Constructor Ambiguity
**Problem**: Python can't distinguish between similar constructor signatures
**Example**: Multiple constructors with different parameter types

3. Parameter Type Conversion
**Problem**: Python types don't map correctly to expected Java types
**Example**: Python list vs Java Collection vs Java Array

### Adding New Exception Handlers

To add a new constructor exception handler, modify the `handle_constructor_exceptions()` function:

```python
def handle_constructor_exceptions(java_class, class_name, *args, **kwargs):
    # Existing MultiTreeStatistics case
    if class_name == 'MultiTreeStatistics' and len(args) == 1 and len(kwargs) == 0:
        return java_class(args[0], "all")

    # NEW CASE: Add another case here
    if class_name == 'TheProblematicClass' and the_condition:
        # return fix here
        return java_class(modified_args)

    # No special handling needed
    return None
```

## Tutorial notebooks: environment cell
Every notebook in `docs/notebooks/` ends with a code cell (tagged `hide-input`) that prints the run date and the
PySNT, SNT, Python and Java versions of the session that produced the stored outputs. Docs are built without
executing notebooks (`nb_execution_mode = "off"`), so this is the notebook's "last tested" certificate. Before a
release: use a fresh environment (see the install docs), restart the kernel, run all cells, save, and commit. The
cell source lives in the existing notebooks: copy it from `01_single_cell_analysis.ipynb` when adding a new one.
