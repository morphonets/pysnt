# <i class="fa-solid fa-code"></i>&hairsp;API

```{seealso}
- [Quickstart](quickstart.md) - Step-by-step introduction and workflows
- [PySNT Overview](overview.md) - Core concepts and detailed usage patterns
- [Quirks and Limitations](limitations.md) - Known limitations and workarounds
```

```{toctree}
:maxdepth: 3
:caption: Complete API Reference
:hidden:

api_auto/index
api_auto/pysnt
api_auto/pysnt.analysis
api_auto/pysnt.analysis.graph
api_auto/pysnt.analysis.growth
api_auto/pysnt.analysis.sholl
api_auto/pysnt.analysis.sholl.gui
api_auto/pysnt.analysis.sholl.math
api_auto/pysnt.analysis.sholl.parsers
api_auto/pysnt.annotation
api_auto/pysnt.converters
api_auto/pysnt.converters.chart_converters
api_auto/pysnt.converters.core
api_auto/pysnt.converters.enhancement
api_auto/pysnt.converters.extractors
api_auto/pysnt.converters.graph_converters
api_auto/pysnt.converters.structured_data_converters
api_auto/pysnt.core
api_auto/pysnt.display
api_auto/pysnt.display.core
api_auto/pysnt.display.data_display
api_auto/pysnt.display.utils
api_auto/pysnt.display.visual_display
api_auto/pysnt.gui
api_auto/pysnt.gui.cmds
api_auto/pysnt.io
api_auto/pysnt.tracing
api_auto/pysnt.tracing.artist
api_auto/pysnt.tracing.cost
api_auto/pysnt.tracing.heuristic
api_auto/pysnt.tracing.image
api_auto/pysnt.util
api_auto/pysnt.viewer
api_auto/pysnt.common_module
api_auto/pysnt.config
api_auto/pysnt.gui_utils
api_auto/pysnt.java_utils
api_auto/pysnt.setup_utils
api_auto/method_index
api_auto/class_index
api_auto/constants_index
```

```{toctree}
:maxdepth: 2
:caption: Enhanced Class Documentation
:hidden:

pysnt/index
```

#### Documentation Types

PySNT provides two API documentation approaches:

- **{doc}`api_auto/index`** - Python API reference with type hints and signatures
- **{doc}`api_auto/method_index`** - Alphabetical index of all SNT methods
- **{doc}`api_auto/class_index`** - Alphabetical index of all SNT classes
- **{doc}`api_auto/constants_index`** - Index of public static fields (constants)

### API Organization
PySNT modules map directly into SNT's [Java API](https://javadoc.scijava.org/SNT/index.html), so that e.g.,
{func}`pysnt.analysis` mirrors SNT's [sc.fiji.snt.analysis](https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/analysis/package-summary.html) package.

| SNT Module                            | Description                                                     | SNT API Match                                                                                                                    |
|---------------------------------------|-----------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| {doc}`api_auto/pysnt`                 | main package interface with root classes and core functionality | [<i class="fa-brands fa-java"></i>](https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/package-summary.html)                 |
| {doc}`api_auto/pysnt.analysis`        | neuronal morphology analysis tools and statistics               | [<i class="fa-brands fa-java"></i>](https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/analysis/package-summary.html)        |
| {doc}`api_auto/pysnt.analysis.graph`  | handling neuronal reconstructions as graphs                     | [<i class="fa-brands fa-java"></i>](https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/analysis/graph/package-summary.html)  |
| {doc}`api_auto/pysnt.analysis.growth` | growth analysis of neurites across time                         | [<i class="fa-brands fa-java"></i>](https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/analysis/growth/package-summary.html) |
| {doc}`api_auto/pysnt.analysis.sholl`  | Sholl analysis                                                  | [<i class="fa-brands fa-java"></i>](https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/analysis/sholl/package-summary.html)  |
| {doc}`api_auto/pysnt.annotation`      | handling of neuropil annotations and atlases metadata           | [<i class="fa-brands fa-java"></i>](https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/annotation/package-summary.html)      |
| {doc}`api_auto/pysnt.io`              | import of neuronal reconstructions from multiple sources        | [<i class="fa-brands fa-java"></i>](https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/io/package-summary.html)              |
| {doc}`api_auto/pysnt.tracing`         | tracing tools                                                   | [<i class="fa-brands fa-java"></i>](https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/tracing/package-summary.html)         |
| {doc}`api_auto/pysnt.util`            | Utility classes and helper functions                            | [<i class="fa-brands fa-java"></i>](https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/util/package-summary.html)            |
| {doc}`api_auto/pysnt.viewer`          | 2D and 3D visualization utilities                               | [<i class="fa-brands fa-java"></i>](https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/viewer/package-summary.html)          |

| PySNT Module                      | Description                                                               | 
|-----------------------------------|---------------------------------------------------------------------------|
| {doc}`api_auto/pysnt.config`      | Configuration system for PySNT                                            | 
| {doc}`api_auto/pysnt.converters`  | Converters that transform SNT Java objects into Python equivalents        |
| {doc}`api_auto/pysnt.core`        | Handles initialization and setup functions                                |
|                                   |                                                                           |
| {doc}`api_auto/pysnt.gui_utils`   | GUI utilities for PySNT to handle threading and platform-specific issues. |
| {doc}`api_auto/pysnt.java_utils`  | Java environment management utilities                                     |
| {doc}`api_auto/pysnt.setup_utils` | Setup and configuration helpers                                           |


## Quick Reference

### Essential Imports
```python
import pysnt
from pysnt import SNTService, Tree
from pysnt.analysis import TreeStatistics
```

### Essential Functions
```python
pysnt.initialize()          # Start PySNT
pysnt.display(obj)          # Smart display any object
pysnt.list_classes()        # Explore available classes
pysnt.get_methods(cls)      # Explore class methods
pysnt.find_members(cls, kw) # Search for functionality
```

### Memory Configuration
```python
pysnt.initialize(max_heap="8g")     # 8GB heap
pysnt.initialize(max_heap="16g", min_heap="4g")  # 16GB max, 4GB initial
```

### Configuration
```python
pysnt.set_option('display.table_mode', 'pandasgui')
pysnt.set_option('display.chart_format', 'svg')
```


### Initialization

```python
import pysnt
pysnt.initialize()
pysnt.initialize('/path/to/Fiji.app', max_heap='8g')
```


```{important}
**Important:** pysnt is only available *after* `pysnt.initialize()` is called.
```


### Import Strategies
Three ways to import SNT classes:

| Method              | Coverage                      | Use Case                | Autocompletion | Comments                                             |
|---------------------|-------------------------------|-------------------------|----------------|------------------------------------------------------|
| Direct Import       | Restricted to curated classes | Common tasks            | Detailed       | Fast, convenient                                     |
| `get_class()`       | Discoverable classes          | Advanced/uncommon tasks | Basic          | Slower on first access, then cached                  |
| `scyjava.jimport()` | _Any_ Java class              | Expert usage            | N/A            | May require a priori knowledge of SNT's architecture |

### Discovery of Classes

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


### Discovery of Functions

```python
import pysnt
from pysnt.analysis import TreeStatistics
# Get all methods from TreeStatistics
methods = pysnt.get_methods(TreeStatistics)
# Find all members containing 'length'
results = pysnt.find_members(TreeStatistics, 'length')
# Get only static fields (constants)
constants = pysnt.get_fields(TreeStatistics, static_only=True)
```
