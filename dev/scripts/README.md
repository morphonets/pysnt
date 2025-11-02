# PySNT Development Scripts

Development scripts for building, deploying, and maintaining PySNT.

## Overview

This directory contains scripts for:
- **Type Stub Generation**: Creating `.pyi` files for IDE autocompletion
- **Java Signature Extraction**: Caching detailed method signatures from Java classes
- **API Documentation**: Generating Sphinx documentation
- **Quality Control**: Validation and maintenance tools
- **Deployment**: Building and deploying PySNT

## Prerequisites

Access to a Fiji installation running SNT is required for most scripts:

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
```

## Core Scripts

### `extract_class_signatures.py`

**Purpose**:
Extract detailed method signatures from Java classes and cache them for stub generation.

**What it does**:
- Discovers all `CURATED_CLASSES` from all pysnt modules
- Uses Java reflection to extract complete method signatures
- Saves detailed signatures as JSON files in the `STUBS/` directory

**Usage**:
```bash
# Extract signatures for all curated classes (recommended)
python dev/scripts/extract_class_signatures.py --all-classes --verbose

# Extract specific classes
python dev/scripts/extract_class_signatures.py --class SNTService Tree Path

# Custom output directory
python dev/scripts/extract_class_signatures.py --all-classes --stubs-dir custom/path
```

**Output**:
Creates JSON files in `dev/scripts/STUBS/` with detailed method signatures:
- `Path.json`, `SNTService.json`, `Tree.json`, etc.
- Used by `generate_stubs.py` for type stubs

### `generate_stubs.py`

**Purpose**:
Generate type stub files (`.pyi`) exclusively from cached JSON signatures.

**Notes**:
- Cache-only approach - if signatures are missing, extraction is required first.
- Only regenerates stubs when needed based on:
  - Cache age (considers stale after 7 days) // TODO: In the future this would be replaced by a proper versioning system
  - File timestamps (cache vs stub file modification times)
  - Cache version compatibility
  - `--check-cache`: Shows cache status for all classes
  - `--force`: Forces regeneration regardless of cache status

**Usage**:
```bash
# Generate all stubs (recommended)
python dev/scripts/generate_stubs.py --verbose --overwrite

# Generate with existing files preserved
python dev/scripts/generate_stubs.py --verbose

# Check cache status (see which files need updates)
python dev/scripts/generate_stubs.py --check-cache

# Force regeneration of all stubs (ignore cache freshness)
python dev/scripts/generate_stubs.py --force --verbose

# Smart regeneration (only updates stale caches)
python dev/scripts/generate_stubs.py --verbose
```

### `deploy.py`

**Purpose**:
Complete build and deployment pipeline.

**What it does**:
- Generates stub files (`.pyi`) for Java classes
- Syncs Python classes with stub files
- Generates API documentation files (`.rst`)

**Usage**:
```bash
# Complete build with documentation
python dev/scripts/deploy.py

# Quick build without docs
python dev/scripts/deploy.py --skip-docs
```

### `pysnt_utils.py`

**Purpose**:
Quality control and maintenance utilities.

**Features**:
- Quality control validation (detects duplicate classes, naming issues)
- Cleaning up unused typing imports in `.pyi` files
- Module configuration analysis and reporting

**Usage**:
```bash
# Quality control validation
python dev/scripts/pysnt_utils.py --qc

# Fix import depths
python dev/scripts/pysnt_utils.py --fix-imports

# Clean unused typing imports
python dev/scripts/pysnt_utils.py --clean-pyi-imports

# Analyze module configurations
python dev/scripts/pysnt_utils.py --analyze --verbose

# Preview changes without modifying files
python dev/scripts/pysnt_utils.py --qc --dry-run
```

### `generate_api_docs.py`

**Purpose**:
Generate Sphinx API documentation files.

**Usage**:
```bash
python dev/scripts/generate_api_docs.py
```

## STUBS Directory

The `STUBS/` directory contains cached Java class signatures in JSON format

**Purpose**:
- No need to run Java reflection every time
- Detailed parameter names and types
- Can generate stubs without running Java

### Manual Editing of JSON Signatures

The cached JSON files can be manually edited to improve type information or handle complex cases that automated extraction doesn't handle perfectly.

#### JSON Structure

Each JSON file follows this structure:

```json
{
  "class_name": "Path",
  "package": "sc.fiji.snt",
  "extracted_at": "2025-11-02T07:56:02.398503",
  "extractor_version": "1.0.0",
  "methods": [
    {
      "name": "getLength",
      "overloads": [
        {
          "signature": "getLength() -> double",
          "params": [],
          "return_type": "float",
          "java_return_type": "double"
        }
      ],
      "documentation": "Java method: getLength"
    }
  ],
  "fields": [
    {
      "name": "SOME_CONSTANT",
      "type": "str",
      "java_type": "String"
    }
  ]
}
```

#### Common Manual Edits

**1. Improve Parameter Names**:
```json
// Before (generic names)
"params": [
  {"name": "arg0", "type": "Any", "java_type": "String"},
  {"name": "arg1", "type": "int", "java_type": "int"}
]

// After (meaningful names)
"params": [
  {"name": "file_path", "type": "str", "java_type": "String"},
  {"name": "max_depth", "type": "int", "java_type": "int"}
]
```

**2. Refine Return Types**:
```json
// Before (generic)
"return_type": "Any",
"java_return_type": "Object"

// After (specific)
"return_type": "List[str]",
"java_return_type": "List<String>"
```

**3. Add Method Documentation**:
```json
"documentation": "Get the total length of this path in calibrated units."
```

**4. Handle Generic Types**:
```json
// Before
"return_type": "Any"

// After (for collections)
"return_type": "List[Path]"  // for List<Path>
"return_type": "Dict[str, Any]"  // for Map<String, Object>
"return_type": "Optional[Tree]"  // for nullable Tree
```

**5. Fix Complex Method Signatures**:
```json
{
  "name": "findPath",
  "overloads": [
    {
      "signature": "findPath(PointInImage, PointInImage, boolean) -> Path",
      "params": [
        {"name": "start_point", "type": "Any", "java_type": "PointInImage"},
        {"name": "end_point", "type": "Any", "java_type": "PointInImage"},
        {"name": "use_heuristic", "type": "bool", "java_type": "boolean"}
      ],
      "return_type": "Optional[Path]",
      "java_return_type": "Path"
    }
  ],
  "documentation": "Find a path between two points using A* algorithm."
}
```

#### Best Practices for Manual Editing

**Type Mapping Guidelines**:
- `String` → `str`
- `boolean` → `bool`
- `int`, `long`, `short`, `byte` → `int`
- `float`, `double` → `float`
- `List<T>` → `List[T]` (or `List[Any]` if T is complex)
- `Map<K,V>` → `Dict[K, V]`
- `Set<T>` → `Set[T]`
- Nullable types → `Optional[T]`
- Arrays → `List[T]`

**Parameter Naming**:
- Use descriptive names: `file_path` not `arg0`
- Follow Python conventions: `snake_case`
- Be consistent within the same class
- Use common patterns: `x, y, z` for coordinates, `width, height` for dimensions, etc.

**Documentation**:
- Keep it concise but informative
- Mention units for measurements: "in calibrated units", "in pixels"
- Note important constraints or side effects

#### Workflow for Manual Editing

1. **Extract base signatures**:
   ```bash
   python dev/scripts/extract_class_signatures.py --class ClassName --verbose
   ```

2. **Edit the JSON file**:
   ```bash
   # Edit dev/scripts/STUBS/ClassName.json
   # Improve parameter names, types, documentation
   ```

3. **Validate the JSON**:
   ```bash
   python -m json.tool dev/scripts/STUBS/ClassName.json > /dev/null
   echo "JSON is valid"
   ```

4. **Generate stubs**:
   ```bash
   python dev/scripts/generate_stubs.py --force --verbose
   ```

5. **Test in IDE**:
   - Check autocompletion works
   - Verify parameter hints are helpful
   - Ensure return types are accurate

#### Example: Improving TreeStatistics.json

```json
{
  "name": "getHistogram",
  "overloads": [
    {
      "signature": "getHistogram(String) -> SNTChart",
      "params": [
        {
          "name": "measurement_type",
          "type": "str",
          "java_type": "String"
        }
      ],
      "return_type": "Any",  // SNTChart type
      "java_return_type": "SNTChart"
    }
  ],
  "documentation": "Generate histogram for the specified measurement type (e.g., 'Branch length', 'Path length')."
}
```

#### Troubleshooting Manual Edits

**Invalid JSON**:
```bash
# Check JSON syntax
python -m json.tool dev/scripts/STUBS/ClassName.json
```

**Stub generation fails**:
```bash
# Check for typos in field names
python dev/scripts/generate_stubs.py --verbose --force
```

**Troubleshooting: IDE doesn't recognize changes**:
- Restart IDE
- Clear IDE caches if available
- Verify the `.pyi` file was actually updated

## Workflow Examples

### Complete Development Workflow

```bash
# 1. Extract signatures for all classes (run once or when classes change)
python dev/scripts/extract_class_signatures.py --all-classes --verbose

# 2. Generate type stubs using cached signatures
python dev/scripts/generate_stubs.py --verbose --overwrite

# 3. Run quality control
python dev/scripts/pysnt_utils.py --qc

# 4. Complete build with documentation
python dev/scripts/deploy.py
```

### Quick Stub Update

```bash
# Smart regeneration (only updates what's needed)
python dev/scripts/generate_stubs.py --verbose

# Check what needs updating first
python dev/scripts/generate_stubs.py --check-cache

# Force complete regeneration
python dev/scripts/generate_stubs.py --force --verbose --overwrite
```

### Adding New Classes

```bash
# 1. Add class names to CURATED_CLASSES in appropriate __init__.py
# 2. Extract signatures for the new classes
python dev/scripts/extract_class_signatures.py --all-classes --verbose

# 3. Regenerate stubs
python dev/scripts/generate_stubs.py --verbose --overwrite
```

### Troubleshooting

```bash
# Check Fiji configuration
python -m pysnt.setup_utils --status

# Validate module configurations
python dev/scripts/pysnt_utils.py --analyze --verbose

# Test specific class extraction
python dev/scripts/extract_class_signatures.py --class ClassName --verbose
```

## Dynamic Placeholder System

PySNT uses an automatic placeholder system that works independently of these scripts:

- Created automatically by `setup_module_classes()` in each module
- Placeholder classes are created dynamically at runtime

How it works:
1. Add classes to `CURATED_CLASSES` or `EXTENDED_CLASSES` in module `__init__.py`
2. Each module calls `setup_module_classes()` in its `__init__.py`
3. Dynamic placeholders are created automatically for all curated classes
4. When `pysnt.initialize()` is called, placeholders redirect to actual Java classes
5. Type stubs (`.pyi`) are generated separately (see above)

## Configuration Management

```bash
# Fiji configuration management
python -m pysnt.setup_utils --status
python -m pysnt.setup_utils --auto-detect
python -m pysnt.setup_utils --set /Applications/Fiji.app
python -m pysnt.setup_utils --clear
python -m pysnt.setup_utils --reset
python -m pysnt.setup_utils --check
```

## Development Tools

See the parent [`dev/`](../) directory for additional development tools:

- **`dev/placeholder_template.py`**: Template for creating new PySNT module `__init__.py` files
- **`dev/create_module.py`**: Script to quickly create new modules from template
- **`dev/README.md`**: Guide for adding new SNT packages

### Quick Module Creation

```bash
# Create a new module (uses dynamic placeholder system)
python dev/create_module.py analysis.morphology

# Create with predefined classes (automatically creates dynamic placeholders)
python dev/create_module.py analysis.morphology \
  --curated MorphologyAnalyzer ShapeMetrics \
  --extended AdvancedMorphology DetailedMetrics
```

## File Organization

```
dev/scripts/
├── README.md                      # This file
├── STUBS/                         # Cached Java signatures (one per class)
│   ├── Path.json
│   ├── SNTService.json
│   └── etc...
├── extract_class_signatures.py   # Extract Java signatures
├── generate_stubs.py             # Generate .pyi files
├── deploy.py                     # Complete build pipeline
├── pysnt_utils.py                # Quality control utilities
├── generate_api_docs.py          # Sphinx documentation
└── java_reflection_extractor.py  # Java reflection helper
```

## Quick Reference

### Essential Commands

```bash
# Check cache status for all classes
python dev/scripts/generate_stubs.py --check-cache

# Extract signatures for all classes
python dev/scripts/extract_class_signatures.py --all-classes --verbose

# Generate stubs (cache-only, fast)
python dev/scripts/generate_stubs.py --verbose

# Force complete regeneration
python dev/scripts/generate_stubs.py --force --overwrite --verbose

# Complete build pipeline
python dev/scripts/deploy.py --verbose
```

### Manual JSON Editing Checklist

- [ ] Extract base signatures first: `extract_class_signatures.py --class ClassName`
- [ ] Edit `dev/scripts/STUBS/ClassName.json`
- [ ] Improve parameter names (use `snake_case`, be descriptive)
- [ ] Refine return types (use `Optional[T]` for nullable, `List[T]` for collections)
- [ ] Add meaningful documentation
- [ ] Validate JSON: `python -m json.tool dev/scripts/STUBS/ClassName.json`
- [ ] Regenerate stubs: `generate_stubs.py --force --verbose`
- [ ] Test in IDE (restart if needed)

### Common Type Mappings

| Java Type | Python Type | Notes |
|-----------|-------------|-------|
| `String` | `str` | |
| `boolean` | `bool` | |
| `int`, `long` | `int` | |
| `float`, `double` | `float` | |
| `List<T>` | `List[T]` | Use `List[Any]` if T is complex |
| `Map<K,V>` | `Dict[K, V]` | |
| `Set<T>` | `Set[T]` | |
| `T[]` | `List[T]` | Arrays become lists |
| `@Nullable T` | `Optional[T]` | Nullable types |
| `Object` | `Any` | Generic object |
| `Tree` | `Tree` | SNT-specific types use class names |
| `Path` | `Path` | Better IDE support |
| `SNTService` | `SNTService` | Specific type hints |
| `ImagePlus` | `Any` | ImageJ types (complex) |

### File Locations

- **Cached signatures**: `dev/scripts/STUBS/*.json`
- **Generated stubs**: `src/pysnt/**/__init__.pyi`
- **Module definitions**: `src/pysnt/**/__init__.py` (CURATED_CLASSES)
- **Scripts**: `dev/scripts/*.py`
