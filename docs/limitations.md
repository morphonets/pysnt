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


### Maven and Other Java Tooling

SNT is a Java application, so PySNT relies on a few Java tools that have Python counterparts. You rarely run them
yourself: `pysnt.initialize()` uses them behind the scenes.

| Java                                  | Python counterpart  | What it is                                                                 |
|---------------------------------------|---------------------|----------------------------------------------------------------------------|
| JDK                                   | Python interpreter  | Runs SNT (Java 21+ is needed)                                              |
| JAR                                   | wheel               | A bundle of compiled code: how SNT and its dependencies are distributed    |
| Maven                                 | pip                 | Downloads a package together with everything it depends on                 |
| maven.scijava.org, Maven Central      | PyPI                | The repositories where those packages are hosted                           |
| `pom.xml`                             | `pyproject.toml`    | Declares a project's dependencies                                          |
| `mvn install`                         | `pip install .`     | Builds and installs a local copy of a project                              |

In practice: the first call to `pysnt.initialize()` downloads SNT and its dependencies from a Maven repository (the
"Maven source") and caches them, much like `pip install` fetches from PyPI. The alternative is to use a local Fiji
installation, see [Attaching to SNT](install.md#attaching-to-snt).

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

### Verbose Console Output

Debug messages and warnings may appear when working with Java objects:
```console
log4j:WARN No appenders could be found for logger (org.bushe.swing.event.EventService).
log4j:WARN Please initialize the log4j system properly.
```

**Workaround:**

These messages can be safely ignored and don't affect functionality. To suppress them, you can configure logging
at the _start_ of your script, i.e., before calling `pysnt.initialize()`:
```python
import pysnt
pysnt.set_option('java.logging.level', 'OFF') #OFF, ERROR, WARN, INFO, DEBUG, TRACE
pysnt.initialize()
```

As the library matures, these messages are expected to be reduced or eliminated.


## Limitations

PySNT has some limitations that may not be addressed in future releases. However, workarounds are available for most cases.


### Interactive Viewers

SNT provides several interactive 3D visualization tools: [Reconstruction Viewer](https://imagej.net/plugins/snt/reconstruction-viewer) (`Viewer3D`, also opened by `tree.show3D()`), [SciView](https://imagej.net/plugins/snt/modeling), and [Big Volume Viewer](https://imagej.net/plugins/snt/manual#big-volume-viewer). While these viewers can be launched from Python, their usage remains experimental with several limitations:

- PySNT starts in headless mode by default, in which SNT native windows cannot open: viewers fail with `IllegalArgumentException: Offscreen canvas cannot be displayed`. Initialize with `pysnt.initialize(mode='interactive')` to use them
- On macOS, Java viewers (e.g., Reconstruction Viewer, Big Volume Viewer) must also be launched on the event dispatch thread (see [GUI Threading Issues](#gui-threading-issues))
- For some viewers, the ImageJ GUI may need to linger in the background, even if it is not needed nor used

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

PySNT can open GUI windows (SNT's own viewers and tables, napari, etc.). On macOS, GUI toolkits require window creation on the AppKit main thread, which the Python kernel owns. This has two consequences: Java GUI calls may hang, and only one GUI event loop can be active per kernel.

#### Java GUIs on macOS (e.g., Big Volume Viewer)

Java windows can only be created on macOS if PySNT is initialized in interactive mode, which enables IPython's `osx` event loop (`%gui osx`). That loop is serviced only while the kernel is idle, so the call that opens the window must not block the kernel. In particular, never wait for the Java event dispatch thread (EDT) from the kernel thread: it deadlocks (the cell appears to run forever). Instead, use `pysnt.run_on_edt()`, which _queues_ the GUI code on the EDT without waiting for it (on Linux and Windows it simply calls the function):

```python
import pysnt
pysnt.initialize(mode='interactive')

def show_viewer():
    bvv = pysnt.Bvv()  # any Java GUI code
    bvv.add(tree)
    bvv.show(image)

pysnt.run_on_edt(show_viewer)
```

Notes:

- Wrap every Java GUI call (creating, showing or updating a window) in `run_on_edt()`. The queued code runs once the cell finishes.
- Do not rely on return values from queued code in the same cell. Assign results to global variables if you need them afterwards.
- `run_on_edt()` raises an error on macOS if PySNT was not initialized in interactive mode.
- `mode='interactive:force'` does not work around this: it is not supported by PyImageJ.

#### Qt-based viewers (napari) and Java GUIs

IPython/ipykernel allows a single GUI event loop per kernel. Interactive mode uses `osx`, napari uses `qt`, so on macOS they cannot be used in the same kernel (attempting to do so raises `RuntimeError: Cannot activate multiple GUI eventloops`). Choose one:

- **Java GUIs** (Big Volume Viewer, etc.): initialize with `mode='interactive'` and skip napari
- **napari**: initialize with `mode='headless'` (the default) and skip Java GUIs

The [crossover detection tutorial](./notebooks/08_crossover_detection.ipynb) implements this with a single switch (`BVV_ON_MACOS`) that selects the mode at initialization. Restart the kernel after changing it.

#### GUI safe mode

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
pysnt.set_option('display.table_mode', 'summary')  # Text-based summary
pysnt.set_option('display.table_mode', 'heatmap')  # Heatmap visualization
pysnt.set_option('display.table_mode', 'heatmap_norm')  # Normalized heatmap visualization
pysnt.display(some_table)
```

If you need to inspect your environment:

```python
import pysnt

print(f"Main thread: {pysnt.is_main_thread()}")
print(f"macOS: {pysnt.is_macos()}")
print(f"GUI safe mode: {pysnt.get_option('display.gui_safe_mode')}")
```


### napari and Qt Bindings

Recent napari versions require Qt6. If another package in your environment installs PyQt5, napari may fail to start with `ImportError: napari requires Qt >= 6...`, because Qt5 is picked up.

**Workaround**:

Install a Qt6 binding (`python -m pip install "napari[pyqt6]"`) and select it before importing napari or anything else that imports Qt:

```python
import os
os.environ['QT_API'] = 'pyqt6'
os.environ['FORCE_QT_API'] = '1'
import napari
```

Do not mix Qt5 and Qt6 in the same Python session. Restart the kernel if Qt has already been imported.

If the kernel crashes instead with `Could not find the Qt platform plugin "cocoa"` (macOS), the environment likely contains conda's Qt5 packages (e.g., installed by Spyder), which add a `bin/qt.conf` file that redirects Qt6 to Qt5 paths. Use an environment without Spyder (or Qt5 conda packages), or rename `<env>/bin/qt.conf`. Spyder is not recommended for running the tutorials.

### Disposal

`pysnt.dispose()` can be used to properly dispose of resources:

```python
# Clean shutdown when done
pysnt.dispose()
```

However, after calling `pysnt.dispose()`, you cannot reinitialize PySNT in the same Python session.
You will need to restart Python to use PySNT again.

**Workaround**:
Ensure `pysnt.dispose()` is called after PySNT is no longer needed.
