# <i class="fa-solid fa-code"></i>&hairsp;API

```{toctree}
:maxdepth: 3
:caption: API Modules

api_auto/pysnt
api_auto/pysnt.core
api_auto/pysnt.analysis
api_auto/pysnt.util
api_auto/pysnt.viewer
api_auto/pysnt.tracing
api_auto/pysnt.java_utils
api_auto/pysnt.setup_utils
```

## Imports

There are three ways to import SNT classes:

| Method              | Coverage                      | Use Case       | Comments         |
|---------------------|-------------------------------|----------------|------------------|
| Direct Import       | Restricted to curated classes | Common tasks   | Fast, convenient |
| `get_class()`       | Discoverable classes          | Advanced tasks | Slower on first access, then cached |
| `scyjava.jimport()` | _Any_ Java class              | Expert usage   | Fast. May require a priori knowlege of SNT's architecture |

```python
import pysnt
pysnt.initialize_snt()  # Required first step

# Method 1: Direct import (curated classes - recommended)
# Covers most common tasks
from pysnt import SNTService, SNTUtils, Tree, Path  # Root sc.fiji.snt classes
from pysnt.analysis import TreeStatistics, MultiTreeStatistics, ConvexHull
from pysnt.util import PointInImage, SWCPoint

# Method 2: Discoverable classes
# Covers advanced functionality beyond the preset list of direct imports 
import pysnt.analysis as analysis
NodeStats = analysis.get_class("NodeStatistics")
ShollAnalyzer = analysis.get_class("ShollAnalyzer")

# Method 3: Discoverable classes
# Method 3: Direct Java access (expert users)
import scyjava
CustomClass = scyjava.jimport("sc.fiji.snt.CustomClass")

```

## Discovering Classes

PySNT modules map directly into SNT's [Java API](https://javadoc.scijava.org/SNT/index.html), so that e.g., the Java package [sc.fiji.snt.analysis](https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/analysis/package-summary.html), has a direct Python mirror in {func}`pysnt.analysis`

```python
import pysnt.analysis as analysis
import pysnt.util as util

# Show all available classes
analysis.list_classes()
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


## Quick Reference

| Module | Description | SNT API Match |
|-------|--------------|---------------|
| {doc}`api_auto/pysnt` | main package interface with root classes and core functionality | [<i class="fa-brands fa-java"></i>](https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/package-summary.html) |
| {doc}`api_auto/pysnt.analysis` | neuronal morphology analysis tools and statistics | [<i class="fa-brands fa-java"></i>](https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/analysis/package-summary.html) |
| {doc}`api_auto/pysnt.tracing` | tracing tools | [<i class="fa-brands fa-java"></i>](https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/tracing/package-summary.html) |
| {doc}`api_auto/pysnt.util` | Utility classes and helper functions | [<i class="fa-brands fa-java"></i>](https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/util/package-summary.html) |
| {doc}`api_auto/pysnt.viewer` | 2D and 3D visualization utilities | [<i class="fa-brands fa-java"></i>](https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/viewer/package-summary.html) |
| | |
| {doc}`api_auto/pysnt.core` | handles initialization and setup functions | |
| | |
| {doc}`api_auto/pysnt.java_utils` | Java environment management utilities | |
| {doc}`api_auto/pysnt.setup_utils` | Setup and configuration helpers | |

### Core Functions
- {func}`pysnt.initialize_snt` - Initialize the SNT environment
- {func}`pysnt.version` - Get version information  
- {func}`pysnt.info` - Show detailed system information

### Exploration
```python
# Discover what's available
import pysnt.analysis as analysis
import pysnt.util as util

print("Analysis classes:")
analysis.list_classes()

print("\nUtility classes:")
util.list_classes()
```

## Error Handling

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