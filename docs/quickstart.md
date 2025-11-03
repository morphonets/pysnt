# <i class="fas fa-rocket"></i>&hairsp;Quickstart

Get up and running with PySNT quickly! This guide covers essential workflows and practical examples to start analyzing neuronal morphology right after [installation](install.md).

```{seealso}
- [PySNT Overview](overview.md) - Core concepts and detailed usage patterns
- [Limitations and Quirks](limitations.md) - Known limitations and workarounds
- [API Reference](api.md) - Complete function and class documentation
```

## Quick Verification

First, let's make sure everything is working:

```python
import pysnt
pysnt.initialize()

# Quick system check
pysnt.show_version()
pysnt.info()
```

If this works without errors, you're ready to go! If not, see [troubleshooting](install.md#troubleshooting).

## Core Concepts

- **Initialization**: PySNT needs to be initialized as early as possible using `pysnt.initialize()`
- **Data types**: PySNT automatically converts Java objects to Python-friendly formats when possible
- **Display data**: Use `pysnt.display(object)` to display data in friendly formats
- **Key Classes/Objects**:
  - **SNTService**: SNTService is SNT's service that provides convenience access to common operations like accessing the current instance of the program, or accessing demo datasets
  - **Tree**: A neuronal reconstruction. It is organized as a list of traced Paths. A Tree can be _any_ traced structure. A formal graph representation can be obtained using `tree.getGraph(bool)` where 'bool' indicates whether the  graph should be simplified
  - **BrainAnnotation**: Neuropil labels of a reference atlas defining brain regions. These are generic to any atlas (and species), but currently the Allen Brain Atlas is the most supported
  - **TreeStatistics**: Measures various properties of a tree, such as total length, number of branches, etc. There are variants of this class that measure MultipleTrees, or Groups of Trees. All of them provide immediate access to histograms, plots, etc.
  - **Analyzers**: Provide specialized analysis like Strahler, Sholl, Persistene Homology, etc. There are _many_. See [tutorials](notebooks/index.md) for details
  - **Viewers**: Provide 2D/3D visualizations for trees and brain annotations, designed for quantitative analysis

## Essential Workflows

### 1. Working with Demo Data

Start with built-in demo datasets to explore the basics:

```python
import pysnt
from pysnt import SNTService

pysnt.initialize()

# Get and display demo data
snt_service = SNTService()
tree = snt_service.demoTree('pyramidal')  # or 'OP1' (DIADEM dataset), or 'DG' (Dentate gyrus granule cell), or 'fractal' for an L-system toy neuron
print(f"Demo tree loaded: {tree}")
pysnt.display(tree)
```

### 2. Basic Analysis

```python
from pysnt.analysis import TreeStatistics

# Analyze the tree
stats = TreeStatistics(tree)

# Get basic measurements
cable_length = stats.getCableLength()
n_branches = len(stats.getBranchPoints())
n_tips = len(stats.getTips())

print(f"Cable length: {cable_length:.2f}")
print(f"# Branch points: {n_branches}")
print(f"# Tips: {n_tips}")
```

### 3. Detailed Analysis

```python
from pysnt.analysis import TreeStatistics

# Analyze the tree
stats = TreeStatistics(tree)

# Get specialized metric
all_metrics = stats.getMetrics('all') # Either 'safe', 'common', 'quick', or 'all'
pysnt.display(all_metrics) # formated printing of list
metric = stats.getMetric("Complexity index: DCI") #TreeStatistics.COMPLEXITY_INDEX_DCI
print(f"DCI: {metric}")
```

### 3. Visualization and Export

```python
# Display tree
pysnt.display(tree)

# Display charts
chart = stats.getHistogram("internode distance")
pysnt.display(chart)

# Display all measuremts in one go
all_metrics = stats.getMetrics()
stats.measure('some row description', all_metrics, True) # bool: Split measurements by compartment (axon/dendrites!?)
pysnt.set_option("display.table_mode", "pandasgui")
pysnt.display(stats.getTable()) # displays Dataframe in a pandasgui window
```

## File I/O Essentials

### Loading Your Own Data

```python
# Load a single reconstruction file (common formats: SWC, TRACES (SNT's native format), JSON (MouseLight), or NDF (NeuronJ))
from pysnt import Tree
tree = Tree("/path/to/your/reconstruction.swc") # single neuron

# Load multiple reconstruction files
trees = Tree.listFromDir("/path/to/directory/with/reconstruction.swc")
trees = Tree.listFromDir("/path/to/directory/with/reconstruction.swc", "filename-pattern")
```

### Batch Processing Setup

```python
import os
import pandas as pd
from pathlib import Path # do not confuse with pysnt.Path (!)
import pysnt
from pysnt import Tree
from pysnt.analysis import TreeStatistics

# Initialize PySNT
pysnt.initialize()

# Process multiple files
data_dir = Path("/path/to/a/directory/of/SWC/files")
swc_files = list(data_dir.glob("*.swc"))
results = []

for swc_file in swc_files:

    tree = Tree(str(swc_file))
    stats = TreeStatistics(tree)

    # Define measurements: We can retrieve safe metrics that can be computed
    # from invalid graphs, commonly used metrics, 'quick' (used by SNT's
    # 'quick measure' command), or all metrics supported by TreeStatistics
    # (NB: Specialized analyzers will retrieve their own metrics)
    metrics = stats.getMetrics('common') # Either 'safe', 'common', 'quick', or 'all'

    # Initialize result for this file
    result = {'filename': swc_file.name}

    # Iterate over metrics
    for metric in metrics:
        measurement = stats.getMetric(metric)
        # Clean column name and append to results
        column_name = str(metric).translate(str.maketrans(' /', '__', '()')) # delete parentheses, and replace space and slash with _
        result[column_name] = measurement

    results.append(result)

# Convert to DataFrame for analysis
df = pd.DataFrame(results)

# Instruct pysnt to display DataFrame in PandasGUI
pysnt.set_option('display.table_mode', 'pandasgui')
pysnt.display(df)
```

## Memory Management

For large datasets, configure memory appropriately at startup:

```python
# For large datasets (recommended)
pysnt.initialize(max_heap="8g")

# For very large datasets
pysnt.initialize(max_heap="16g", min_heap="4g")
```

## Discovery and Exploration

### Finding Available Classes

```python
# List all available classes
pysnt.list_classes()

# Explore specific modules
pysnt.analysis.list_classes()
pysnt.viewer.list_classes()
```

### Exploring Class Capabilities

```python
from pysnt.analysis import TreeStatistics

# See all available methods
methods = pysnt.get_methods(TreeStatistics)
pysnt.display(methods)

# Find specific functionality
hits = pysnt.find_members(TreeStatistics, "length")
pysnt.display(hits)

# Get help on specific methods
help(TreeStatistics.getCableLength)
```

## Configuration Best Practices

Set up your preferred defaults early:

```python
import pysnt

# Configure for your workflow
pysnt.set_option('display.table_mode', 'pandasgui')  # Interactive tables
pysnt.set_option('plotting.figure_size', (10, 10))   # Larger plots

# Initialize with memory for your data size
pysnt.initialize(max_heap="8g")
```


## Error Handling

Common issues and solutions:

```python
# Memory errors
try:
    pysnt.initialize()
except RuntimeError as e:
    if "memory" in str(e).lower():
        print("Try: pysnt.initialize(max_heap='8g')")
    raise

# File loading errors
try:
    tree = pysnt.Tree("path/to/file.swc")
except (FileNotFoundError, PermissionError) as e:
    print(f"File access error: {e}")
except Exception as e:  # Will catch Java/SNT exceptions
    print(f"Unexpected error: {e}")

# Analysis errors
try:
    stats = TreeStatistics(tree)
    length = stats.getCableLength()
except Exception as e:
    print(f"Analysis failed: {e}")
    # Check if tree is valid, has required data, etc.
```


## Cleanup

When you're finished with your analysis session, properly dispose of resources:

```python
# Clean shutdown when done
pysnt.dispose()
```

```{warning}
After calling `pysnt.dispose()`, you cannot reinitialize PySNT in the same Python session. Restart Python to use PySNT again.
```

## Next Steps

Now that you understand the basics:

1. **Configure your environment**: Adjust [configurations](overview.md#setting-options) for your needs
2. **Explore tutorials**: Check out [notebooks](notebooks/index.md) for specific analysis workflows
3. **Read the API**: Browse the [API reference](api.md) for detailed documentation
4. **Join the community**: Ask questions on the [ImageJ Forum](https://forum.image.sc/tag/snt)
