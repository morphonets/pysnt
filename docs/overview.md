# <i class="fas fa-book-open"></i>&hairsp;PySNT Overview

```{important}
Make sure PySNT is properly
<a href="./install.html">installed</a> before running the examples in this page.
```

This overview describes how PySNT works under the hood by covering PySNT's architecture, configuration options, class system, and discovery tools.

```{seealso}
- [Quickstart](quickstart.md) - Step-by-step introduction and workflows
- [Limitations and Quirks](limitations.md) - Known limitations and workarounds
- [API Reference](api.md) - Complete function and class documentation
```

## Initializing

Once installed, `pysnt` is imported as any other module. However *it is only available once the gateway is initialized*:

```python
import pysnt
pysnt.initialize()  # initialize with default options
```

```{important}
**Important:** pysnt is only available *after* `pysnt.initialize()` is called.
```

### Cleanup and Disposal

When you're done with PySNT, you can properly clean up resources:

```python
pysnt.dispose()  # Clean shutdown of ImageJ and JVM
```

```{warning}
**Important:** After calling `pysnt.dispose()`, you cannot reinitialize PySNT in the same Python session. The JVM cannot be restarted once it has been shut down. You must restart your Python session to use PySNT again.
```

### Java Logging Control

You can use the PySNT configuration system to control Java-side logging verbosity:

```python
# Configure logging levels and frameworks
pysnt.set_option('java.logging.level', 'ERROR')        # Only show errors, change to 'INFO' for debugging
pysnt.set_option('java.logging.jpype.silence', True)   # Silence JPype
pysnt.set_option('java.logging.log4j.silence', True)   # Silence Log4j
pysnt.set_option('java.logging.slf4j.silence', True)   # Silence SLF4J
pysnt.set_option('java.logging.jul.silence', True)     # Silence java.util.logging

pysnt.initialize()
```

**Note on SLF4J Warnings**: You may still see some SLF4J warnings about multiple providers during initialization. These occur during SLF4J's initialization phase before logging configuration takes effect. To minimize them:

```python
pysnt.set_option('java.logging.level', 'ERROR')
# Enable aggressive SLF4J suppression
pysnt.set_option('java.logging.suppress_slf4j_warnings', True)
pysnt.initialize()
```

### Advanced Initialization Options

There are also some advanced initialization options:

| Code | Comments |
| ---- | -------- |
|`pysnt.initialize('/path/to/Fiji.app')` | Loads SNT from the specified Fiji installation |
| `pysnt.initialize('interactive')` | See [pyimagej initialization mode](https://py.imagej.net/en/latest/Initialization.html#how-to-initialize-pyimagej) |
| `pysnt.initialize(max_heap="8g")` | Configure JVM memory (8GB heap) |
| `pysnt.initialize(max_heap="16g", min_heap="4g")` | Advanced memory configuration (16GB max, 4GB initial) |
| `pysnt.initialize('/path/to/Fiji.app', interactive=True, ensure_java=True, mode='headless')` | See [API](api_auto/pysnt.core.rst) |

## Setting Options

PySNT provides a pandas-style configuration system that allows you to customize various preferences and settings. Here are some of the most common options:

| Setting                            | Type  | Description                                                                       | Default  |
|------------------------------------|-------|-----------------------------------------------------------------------------------|----------|
| display.chart_format               | str   | Default export format for SNTChart (svg, png, or pdf)                             | png      |
| display.gui_safe_mode              | bool  | Use safe GUI mode to avoid threading issues on macOS                              | True     |
| display.max_columns                | int   | Maximum number of columns to display in table outputs                             | 20       |
| display.max_rows                   | int   | Maximum number of rows to display in table outputs                                | 100      |
| display.precision                  | int   | Number of decimal places to display for floating point numbers                    | 6        |
| display.table_mode                 | str   | Default display mode for SNTTables (pandasgui, heatmap, heatmap_norm, or summary) | summary  |
| plotting.figure_size               | tuple | Default figure size for plots as (width, height) in inches                        | (8, 8)   |
| pyplot.ion                         | bool  | Enable matplotlib interactive mode (plt.ion()) for better plot display            | True     |
| graph.processing.warn_self_loops   | bool  | Warn when self-loops are detected in neural morphology graphs                     | True     |
| graph.layout.AnnotationGraph       | str   | Default layout algorithm for AnnotationGraph (brain regions)                      | circular |
| graph.layout.DirectedWeightedGraph | str   | Default layout algorithm for DirectedWeightedGraph (neural morphology)            | spring   |

E.g., to have tables displayed in an interactive window, one can use:

```python
pysnt.set_option('display.table_mode', 'pandasgui')
```

To list available options or know more about them, you can use:

```python
# List all available options
options = pysnt.list_options()
print(f"Available options: {len(options)}")

# Get detailed descriptions
pysnt.describe_option()  # Describe all options
pysnt.describe_option('display.chart_format')  # Describe specific option
```


## Managing Fiji Installations

PySNT provides utilities to manage your Fiji configuration:

```python
# Check current configuration status
pysnt.show_config_status()

# Set Fiji path (with SNT installed) programmatically
pysnt.set_fiji_path('/path/to/your/Fiji.app')

# Get current Fiji path
fiji_path = pysnt.get_fiji_path()
print(f"Current Fiji path: {fiji_path}")

# Auto-detect Fiji installations
from pysnt.setup_utils import find_fiji_installations
installations = find_fiji_installations()
print(f"Found {len(installations)} Fiji installations")
```

## Handling SNT Classes

PySNT handles two types of classes:

1. **Curated Classes**: Always available for direct import. These work as any other Python class (IDE autocompletion, etc.)

2. **Extended Classes**: Discovered dynamically and loaded lazily. The expectation is that extended classes are not needed frequently: these are either not relevant to Python scripting, too experimental, or both.

You can explore available classes, like so:

```python
pysnt.list_classes()  # Lists all class names
pysnt.get_curated_classes()  # Returns curated classes (always available for direct import)
pysnt.get_extended_classes()  # Returns extended classes (discovered dynamically/loaded lazily)
pysnt.get_available_classes()  # Returns all classes (both curated and extended)
```

and of course, you can apply this to any other submodule:

```python
pysnt.analysis.list_classes()  # Lists all class names in the analysis module
pysnt.analysis.get_extended_classes()  # get extended classes in the analysis module
pysnt.viewer.list_classes()  # Lists all class names in the viewer module
pysnt.viewer.get_extended_classes()  # get extended classes in the viewer module
```

### Import and Instantiation

Curated classes are imported and instantiated as usual. E.g., to initialize SNTService<sup>1</sup>:

```python
import pysnt
pysnt.initialize()

from pysnt import SNTService
snt_service = SNTService()  # Instantiate SNTService
```
<sup>1</sup> SNTService is SNT's SciJava service that provides convenience access to SNT, and common operations (like accessing the current instance of the program, or accessing demo datasets).

Extended classes are imported after a reference has been obtained:
```python
PCAnalyzer = pysnt.analysis.get_class('PCAnalyzer')  # Obtain reference to extended class PCAnalyzer
pc_analyzer = PCAnalyzer()  # Instantiate the extended class PCAnalyzer
tree = (...)  # code to access a reconstruction
principal_axes = pc_analyzer.getPrincipalAxes(tree)  # Use the instance as usual
```

### Inner Classes

Inner classes can be accessed using the dot notation. First, you can discover inner classes using `find_members`:

```python
CircModels = pysnt.analysis.get_class("CircularModels")
hits = pysnt.find_members(CircModels, "VonMisesFit")  # Discovers VonMisesFit inner class
print(f"Found inner class: {hits['inner_classes'][0]['signature']}")
```

Then access the inner class directly using the enhanced `get_class` function:

```python
VonMisesFit = pysnt.analysis.get_class("CircularModels.VonMisesFit")
```

You can also list all inner classes in a class:

```python
inner_classes = pysnt.get_inner_classes(CircModels)
for cls in inner_classes:
    print(f"Inner class: {cls['name']} - {cls['signature']}")
```

Note that if you are familiar with SNT's Java API (or e.g., are simply converting a Groovy script into Python), you can always use scyjava directly to import _any_ class directly:

```python
from scyjava import jimport
VonMisesFit = jimport('sc.fiji.snt.analysis.CircularModels.VonMisesFit')
```


## Discover SNT Functionality

In addition to obtaining the class lists [described above](#handling-snt-classes), you can use inspection functions to explore SNT's API:

```python
import pysnt
pysnt.initialize()

from pysnt.analysis import TreeStatistics
import pprint

# Get all methods in the TreeStatistics class
methods = pysnt.get_methods(TreeStatistics)
print(f"TreeStatistics has {len(methods)} methods")

# Find all members (methods, fields, and inner classes) containing 'length'
hits = pysnt.find_members(TreeStatistics, "length")
print(f"Length-related: {len(hits['methods'])} methods, {len(hits['fields'])} fields")

# Get only static fields (constants)
constants = pysnt.get_fields(TreeStatistics, static_only=True)
print(f"TreeStatistics has {len(constants)} static fields")
```

This approach works the same for extended classes:
```python
CircModels = pysnt.analysis.get_class("CircularModels")

# Get all methods from CircularModels
methods = pysnt.get_methods(CircModels)
print(f"CircularModels has {len(methods)} methods")

# Find all members containing 'kappa'
results = pysnt.find_members(CircModels, 'kappa')
print(f"Kappa-related: {len(results['methods'])} methods, {len(results['inner_classes'])} inner classes")

# Discover inner classes
inner_classes = pysnt.get_inner_classes(CircModels)
print(f"CircularModels has {len(inner_classes)} inner classes:")
for cls in inner_classes:
    print(f"  - {cls['signature']}")
```

### Enhanced Discovery Features

The `find_members` function  supports searching across methods, fields, and inner classes:

```python
# Find everything related to "Fit" in CircularModels
results = pysnt.find_members(CircModels, "Fit")
print(f"Found {len(results['methods'])} methods:")
for method in results['methods']:
    print(f"  - {method['signature']}")

print(f"Found {len(results['inner_classes'])} inner classes:")
for cls in results['inner_classes']:
    print(f"  - {cls['signature']}")
```

You can also control what to search for:

```python
# Search only methods
methods_only = pysnt.find_members(CircModels, "get",
                                  include_fields=False,
                                  include_inner_classes=False)

# Search only static members
static_only = pysnt.find_members(CircModels, "fit", static_only=True)

# Case-sensitive search
case_sensitive = pysnt.find_members(CircModels, "Fit", case_sensitive=True)
```

## Working with SNT Data

### Converting Objects

Common data types require no convertion at all. However, some operations return specialized SNT Java objects, that may require conversion to Python. When that happens, one can use the `to_python()` function:

```python
# Only needed for specialized objects
java_result = (...)  # some specialized SNT operation result
python_result = pysnt.to_python(java_result)
```

Under the hood, `pysnt.to_python(java_result)` will use all of Java -> Python converters available in ScyJava in addition to the ones provided by PySNT.

### Displaying Objects

PySNT provides a convenient `display()` function that handles _any_ object you throw at it: It automatically chooses the "best" visualization based on the object type - DataFrames for tabulardata, Figures for charts, formatted lists for collections, etc.

```python
import pysnt
from pysnt import Tree
from pysnt.analysis import TreeStatistics, SNTChart

# Display discovery results
tree = Tree("path/to/swc/file.swc")
stats = TreeStatistics(tree)
pysnt.display(tree) # Shows the reconstruction
methods = pysnt.get_methods(stats)
pysnt.display(methods)  # Shows formatted method list

# Display search results
results = pysnt.find_members(stats, "length")
pysnt.display(results)  # Prints nicely formatted search results

# Display inner classes
CircModels = pysnt.analysis.get_class("CircularModels")
inner_classes = pysnt.get_inner_classes(CircModels)
pysnt.display(inner_classes)  # Prints formatted class information

# Display charts and plots (when you have data)
chart = stats.getHistogram("internode-distance")
pysnt.display(chart)  # Shows the chart
chart = stats.getPolarHistogram("internode-angle")
pysnt.display(chart)  # Shows the chart

metrics = stats.getMetrics("common")
stats.measure("Common measurements", metrics, True)
table = stats.getTable()
pysnt.display(table)  # Shows tabular data

# etc.
```

```{tip}
In addition, PYSNT can also patch the show() method of SNT objects, so that they can displayed in Python:
An example is the `Tree` class:

When running from Java its `show()` method displays the tree in either
[Reconstructing Plotter](https://imagej.net/plugins/snt/manual#reconstruction-plotter) or [Reconstruction Viewer](https://imagej.net/plugins/snt/reconstruction-viewer) (depending if the reconstruction is 2D or 3D).
In PySNT, calling `tree.show()` from a headless environment will print the tree as ASCII art to the console, while `pysnt.display(tree)` will display it as a matplotlib figure.
```

### Advanced Operations

```python
# Access PyImageJ's instance for advanced operations
ij = pysnt.ij()
print(f"ImageJ version: {ij.getVersion()}")

# Access ImageJ Ops and its tubeness filter
[op for op in ij.op().ops() if "tube" in op]

# Convert specialized objects when needed
specialized_result = (...)  # some specialized SNT operation
python_equivalent = pysnt.to_python(specialized_result)
```

## Best Practices

1. **Always initialize first**: Call `pysnt.initialize()` as early as possible, before using any pysnt functionality
2. **Use curated classes when possible**: They provide better IDE support and autocompletion
3. **Explore before coding**: Use `list_classes()`, `find_members()`, and `get_methods()` to discover available functionality
5. **Use `pysnt.display()` for output**: It automatically handles any object type
6. **Conversion is usually automatic**: Most results are already Python objects; only use `pysnt.to_python()` for specialized Java objects

## Troubleshooting

If you encounter issues:

```python
# Check version information
pysnt.show_version()

# Check configuration status
pysnt.show_config_status()

# List available classes if a class is not found
pysnt.analysis.list_classes()  # for analysis classes
pysnt.viewer.list_classes()    # for viewer classes
```
