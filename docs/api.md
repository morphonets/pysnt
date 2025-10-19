# <i class="fa-solid fa-code"></i>&hairsp;API

```{toctree}
:maxdepth: 1
:caption: Complete API Reference

api_auto/pysnt
```

```{toctree}
:maxdepth: 2
:caption: Analysis

api_auto/pysnt.analysis
api_auto/pysnt.viewer
```

```{toctree}
:maxdepth: 2
:caption: Tracing

api_auto/pysnt.tracing
```

```{toctree}
:maxdepth: 0
:caption: Core Functionality

api_auto/pysnt
api_auto/pysnt.util
```

```{toctree}
:maxdepth: 2
:caption: Internal & Setup
api_auto/pysnt.core
api_auto/pysnt.java_utils
api_auto/pysnt.setup_utils
```

## Quick Reference

### API Organization
PySNT modules map directly into SNT's [Java API](https://javadoc.scijava.org/SNT/index.html), so that e.g., SNT's [sc.fiji.snt.analysis](https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/analysis/package-summary.html) package,
has a direct Python mirror in {func}`pysnt.analysis`

| Module                            | Description                                                     | SNT API Match                                                                                                             |
|-----------------------------------|-----------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| {doc}`api_auto/pysnt`             | main package interface with root classes and core functionality | [<i class="fa-brands fa-java"></i>](https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/package-summary.html)          |
| {doc}`api_auto/pysnt.analysis`    | neuronal morphology analysis tools and statistics               | [<i class="fa-brands fa-java"></i>](https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/analysis/package-summary.html) |
| {doc}`api_auto/pysnt.tracing`     | tracing tools                                                   | [<i class="fa-brands fa-java"></i>](https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/tracing/package-summary.html)  |
| {doc}`api_auto/pysnt.util`        | Utility classes and helper functions                            | [<i class="fa-brands fa-java"></i>](https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/util/package-summary.html)     |
| {doc}`api_auto/pysnt.viewer`      | 2D and 3D visualization utilities                               | [<i class="fa-brands fa-java"></i>](https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/viewer/package-summary.html)   |
|                                   |                                                                 |
| {doc}`api_auto/pysnt.core`        | handles initialization and setup functions                      |                                                                                                                           |
|                                   |                                                                 |
| {doc}`api_auto/pysnt.java_utils`  | Java environment management utilities                           |                                                                                                                           |
| {doc}`api_auto/pysnt.setup_utils` | Setup and configuration helpers                                 |                                                                                                                           |

### Initialization

```python
import pysnt
pysnt.initialize()  # Required first step
```

### Import Strategies
Three ways to import SNT classes:

| Method              | Coverage                      | Use Case                | Autocompletion | Comments                                                   |
|---------------------|-------------------------------|-------------------------|----------------|------------------------------------------------------------|
| Direct Import       | Restricted to curated classes | Common tasks            | Detailed       | Fast, convenient                                           |
| `get_class()`       | Discoverable classes          | Advanced/uncommon tasks | Basic          | Slower on first access, then cached                        |
| `scyjava.jimport()` | _Any_ Java class              | Expert usage            | N/A            | Fast. May require a priori knowledge of SNT's architecture |

```python
# Method 1: Direct import (curated classes - recommended)
# Covers most common tasks
import pysnt
pysnt.initialize()
from pysnt import Tree
from pysnt.analysis import TreeStatistics
tree = Tree()
stats = TreeStatistics()

# Method 2: Discoverable classes via get_class()
# Covers advanced functionality beyond the preset list of direct imports
import pysnt
CircModels = pysnt.analysis.get_class("CircularModels")
# Get all methods from CircularModels
methods = pysnt.get_methods(CircModels)
# Find all members containing 'length'
results = pysnt.find_members(CircModels, 'length')
# Get only static fields (constants)
constants = pysnt.get_fields(CircModels, static_only=True)

# Method 3: Direct Java access (expert users)
import scyjava
CustomClass = scyjava.jimport("sc.fiji.snt.CustomClass")
```

### Discover Classes

```python
import pysnt.analysis as analysis
import pysnt.util as util

# Discover what's available
print("Analysis classes:")
analysis.list_classes()
print("\nUtility classes:")
util.list_classes()

# Get class lists programmatically
analysis_classes = analysis.get_available_classes()
util_classes = util.get_available_classes()

# Get curated classes (always available for direct import)
curated = analysis.get_curated_classes()
print(f"Curated: {curated}")

# Get extended classes (available via get_class)
extended = analysis.get_extended_classes()
print(f"Extended: {extended}")
```

### Error Handling

```python
try:
    # Try curated class first
    from pysnt.analysis import TreeStatistics
except ImportError:
    print("TreeStatistics not available - check PySNT installation")

try:
    # Try extended class
    import pysnt.analysis as analysis
    NodeStats = analysis.get_class("NodeStatistics")
except KeyError:
    print("NodeStatistics not found - may not be available in this SNT version")

try:
    # Try direct Java access
    import scyjava
    CustomClass = scyjava.jimport("sc.fiji.snt.custom.MyClass")
except Exception as e:
    print(f"Direct Java access failed: {e}")
```