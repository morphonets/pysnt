# <i class="fas fa-exclamation-triangle"></i>&hairsp;Quirks and Limitations

```{seealso}
- [Overview](overview.md) - Architecture and configuration details
- [Quickstart](quickstart.md) - Introduction to PySNT
- [API Reference](api.md) - Complete function and class documentation
```

## Quirks

There are a couple of quirks/annoyances to be aware of:

### Java vs Python Conventions

Accessing Java classes and methods may feel awkward due to differences in naming conventions between Java and Python:

| Element           | Java               | Python                      |
|-------------------|--------------------|-----------------------------|
| Methods/Functions | `camelCase`        | `snake_case`                |
| Variables         | `camelCase`        | `snake_case`                |
| Classes           | `PascalCase`       | `PascalCase` ✓ (same)       |
| Constants         | `UPPER_SNAKE_CASE` | `UPPER_SNAKE_CASE` ✓ (same) |

**Workaround**:

PySNT intentionally preserves Java naming conventions to maintain consistency with SNT's documentation and make examples translatable between languages. Use your IDE's autocomplete to discover available methods. For frequently used operations, consider creating your own Pythonic wrapper functions if preferred.


### _self_ in Method Signatures

Python type stubs follow Python conventions and show `self` arguments for type checking and IDE autocompletion.
However, the underlying Java methods don't use explicit `self`. This can be confusing at first.

**What you'll see in your IDE**:
```python
from pysnt import Tree
tree = Tree("/path/to/file")
label = tree.getLabel()  # IDE shows: getLabel(self) -> str
```

**Why this happens**:

When you call `tree.getLabel()`, you're calling a Java method through a Python wrapper.
The Python-Java bridge (scyjava/JPype) automatically creates a Python method signature `getLabel(self)` where `self`
refers to the Java object. Python automatically passes the `tree` instance as `self` behind the scenes.
The IDE showing `self` is technically correct for Python's type system, but you should treat these methods
like any other Python instance method—just call them on the object.

**Workaround**:

Simply **ignore the `self` parameter** in autocompletion. Call methods normally without passing `self` explicitly:
```python
tree = Tree("/path/to/file")
label = tree.getLabel()           # ✓ Correct - call normally
# label = tree.getLabel(tree)     # ✗ Wrong - don't pass self!
```



## Limitations

PySNT has some limitations that may not be addressed in future releases. However, workarounds are available for most cases.


### Interactive Viewers

SNT provides several interactive 3D visualization tools: [Reconstruction Viewer](https://imagej.net/plugins/snt/reconstruction-viewer), [SciView](https://imagej.net/plugins/snt/modeling), and [Big Volume Viewer](https://imagej.net/plugins/snt/manual#big-volume-viewer). While these viewers can be launched from Python, their usage remains experimental with several limitations:

- GPU acceleration may not work reliably
- Viewers don't seem to run in non-blocking mode on macOS (see [GUI Threading Issues](#gui-threading-issues))
- The ImageJ GUI must linger in the background, even if it is not needed

**Workaround**:

For programmatic visualization, you can extract static snapshots from 3D scenes without launching interactive viewers. See [Tutorials](./notebooks/index.md) for examples.



### Exception Handling

When calling Java methods through PySNT, exception handling may require a different approach than pure Python code. Java exceptions are wrapped by the Python-Java bridge, which loses some type granularity in the process.

While Python best practices favor catching specific exceptions, working with SNT-wrapped methods may require catching generic `Exception`. This is a pragmatic compromise when the exact exception types from Java code are unpredictable.

**Workaround**:

Handle known Python exceptions first, then catch generic exceptions from SNT/Java:
```python
try:
    tree = pysnt.Tree("path/to/file.swc")
except (FileNotFoundError, PermissionError, IsADirectoryError) as e:
    # Handle Python file system exceptions specifically
    print(f"File access error: {e}")
except Exception as e:
    # Handle Java exceptions generically
    print(f"Error loading tree: {e}")

    # Optional: inspect the exception for more details
    error_msg = str(e).lower()
    if "no paths extracted" in error_msg or "invalid file" in error_msg:
        print("The SWC file appears to be malformed or empty")
    elif "illegalargumentexception" in error_msg:
        print("Invalid argument passed to Java method")
```

It is also possible to extract the Java-side stack trace from a Java exception using scyjava:
```python
try:
    tree = pysnt.Tree("path/to/file.swc")
except Exception as e:
    from scyjava import jstacktrace
    print(jstacktrace(e))
```

### GUI Threading Issues

PySNT includes GUI components like PandasGUI for interactive data exploration. However, GUI applications can encounter threading issues, particularly on macOS where Qt applications must be created on the main thread.

**Workaround**:

PySNT automatically enables GUI safe mode on macOS, which falls back to console display when GUI operations would be unsafe:

```python
import pysnt

# Check if GUI safe mode is enabled (default: True on macOS)
print(pysnt.get_option('display.gui_safe_mode'))

# Enable GUI safe mode explicitly
pysnt.set_option('display.gui_safe_mode', True)
pysnt.display(some_pandas_table)  # Falls back to console if unsafe
```

Instead of GUI-enabled modes, you can always use console-safe display modes:

```python
import pysnt

# Safe display modes
pysnt.set_option('display.table_mode', 'basic')  # Console table display
pysnt.set_option('display.table_mode', 'summary')  # Summary statistics
pysnt.set_option('display.table_mode', 'distribution')  # Distribution plots
pysnt.display(some_table)
```

If you need to inspect your environment:

```python
import pysnt

print(f"Main thread: {pysnt.is_main_thread()}")
print(f"macOS: {pysnt.is_macos()}")
print(f"GUI safe mode: {pysnt.get_option('display.gui_safe_mode')}")
```