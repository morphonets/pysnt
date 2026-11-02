# <i class="fas fa-download"></i>&hairsp;Install

This section covers everything you need to get PySNT up and running.

```{toctree}
:maxdepth: 2
:hidden:
quickstart
overview
limitations
api
```

## Installation Requirements

PySNT needs Python 3.11+ and Java 21+ (a JDK). SNT itself is downloaded automatically the first time you call
`pysnt.initialize()` (see [Attaching to SNT](#attaching-to-snt)), so no Fiji installation is required. Any
Python environment manager works; we document pip and pixi.

```{tip}
No Java? Leave `ensure_java=True` (the default) in `pysnt.initialize()`: if no suitable JDK is found, PySNT offers to download one.
```

## Setting Up

Install into a *fresh, dedicated* environment: PySNT pulls in a large Java/Python stack and mixing it with other projects invites version conflicts.

```{tip}
Starting afresh and with no preference for a package manager? We recommend **pixi**: it is fast, installs Python, a JDK, and native libraries (such as cairo) in a single step, and keeps each project's environment isolated and reproducible. [Install pixi](https://pixi.sh), then follow the *pixi* tab below.
```

::::{tab-set}

:::{tab-item} pixi
[pixi](https://pixi.sh) installs Python, a JDK and Maven from conda-forge and records the environment in a lock file.

```bash
pixi init pysnt-project && cd pysnt-project
pixi add python=3.12 openjdk=21 maven pip cairo
pixi run pip install "pysnt[all] @ git+https://github.com/morphonets/pysnt"
pixi shell
```

Already use conda or mamba? Create an environment with the same `python`, `openjdk=21`, `maven` and `cairo` packages from
conda-forge, then `pip install "pysnt[all] @ git+https://github.com/morphonets/pysnt"` inside it.
:::

:::{tab-item} pip
Use a dedicated virtual environment (Python 3.11+):

```bash
python -m venv pysnt-env
source pysnt-env/bin/activate      # Windows: pysnt-env\Scripts\activate
pip install "pysnt[all] @ git+https://github.com/morphonets/pysnt"
```

`pysnt[all]` includes all optional features. For the core install, drop the extras: `pip install "pysnt @ git+https://github.com/morphonets/pysnt"`. Or pick extras
individually: `display`, `gui`, `java`, `zarr`, `info`. [uv](https://docs.astral.sh/uv/) users can run the same
commands with `uv venv` and `uv pip install`.

```{note}
The optional `display` extra (SVG chart conversion) needs the native *cairo* library, which pip cannot install: use `brew install cairo` (macOS) or `apt install libcairo2` (Linux). Without it PySNT still works, but SVG-based chart conversion is unavailable.
```
:::

::::

```{note}
PySNT is installed directly from GitHub. Add `@ <tag or branch>` after the repository URL (e.g., `.../pysnt@dev`) to install a specific version.
```

Then check that PySNT is installed:

```bash
python -c "import pysnt; print(f'Using PySNT version: {pysnt.version()}')"
```

To contribute to PySNT (editable install from a clone), see
[Install Instructions for Developers](https://github.com/morphonets/pysnt?tab=readme-ov-file#getting-started-for-developers).
The `environment*.yml` files in the repository are meant for that use.

### Choosing an interpreter (IDEs and notebooks)

Whatever you use, the one thing to get right is that it runs the Python of the environment above (and that
`JAVA_HOME`, if set, points to a JDK 21+).

- **Jupyter**: `pip install ipykernel` in the environment, then `python -m ipykernel install --user --name=pysnt`
  and select the `pysnt` kernel.
- **VS Code**: install the Python and Jupyter extensions, press `Ctrl/Cmd+Shift+P`, run *Python: Select
  Interpreter* and pick the environment (for notebooks, use the kernel picker at the top right).
- **PyCharm**: *Settings > Project > Python Interpreter > Add Interpreter > Existing*, and select the
  environment's `python`.
- **Spyder**: install `spyder-kernels` in the environment, then in *Preferences > Python interpreter* choose
  *Use the following interpreter* and select the environment's `python`.

```{note}
The JVM can only be started once per Python process. If you change `initialize()` settings (heap size, source,
version), restart the kernel/console. In Spyder and Jupyter this means restarting the kernel.
```

### Attaching to SNT

`pysnt.initialize()` needs SNT in the JVM. By default it is **downloaded from [Maven](https://maven.scijava.org/)** the first time
and cached for later runs, so no Fiji installation is required:

```python
import pysnt
pysnt.initialize()
```

The first start may take several minutes while dependencies are resolved. Java 21 is required
(`JAVA_HOME` must point to it, or let PySNT set it up with `ensure_java=True`).

To use a local Fiji instead (e.g., to access your plugins or update sites), provide its path. PySNT picks
the first source that applies:

1. `pysnt.initialize(fiji_path="/path/to/Fiji.app")`
2. The `FIJI_PATH` environment variable
3. A path saved with `pysnt.set_fiji_path("/path/to/Fiji.app")` (persists across sessions)
4. Maven (default)

Related options of `initialize()`:

| Argument | Effect |
|---|---|
| `source="maven"` (alias `"remote"`) | Ignore any configured Fiji and use Maven |
| `source="fiji"` (alias `"local"`) | Require a local Fiji: if none is configured, common install locations are searched and, when `interactive=True`, you are asked for the path |
| `snt_version="5.0.24"` | Maven only: SNT version to download (also settable with the `SNT_VERSION` environment variable) |
| `extras=[...]` | Maven only: additional Maven endpoints; `[]` skips the defaults (BigVolumeViewer) |

PySNT warns if the loaded SNT differs in major.minor from the version it was written for (e.g., an outdated
Fiji): classes or methods may then be missing. `pysnt.snt_version()` returns the version in use.

```{note}
For a Fiji install, subscribe to the [NeuroAnatomy update site](https://imagej.net/SNT#install) and run the
Updater so that SNT is current.
```

```{tip}
Developing against a local snapshot of SNT (`mvn install`)? Clear the cached environment so that the new
jar is used: `rm -rf ~/.jgo ~/.cache/jgo`
```

### Configuring a local Fiji

```console
pysnt setup               # interactive setup
pysnt setup --auto-detect # search common locations and save the first valid one
pysnt setup --status      # show the current configuration
```

## Verify Installation

To check version and system info:

```python
import pysnt
pysnt.initialize()  # Initialize first

print(f"PySNT version: {pysnt.version()}")
print("System info:")
pysnt.info()
```

This will output detailed system information:

```console
PySNT version: 0.0.1
System info:
PySNT Version Information
===================================
PySNT version: 0.0.1
Author: SNT contributors

Python Environment:
Python version: 3.13.9
Python executable: /Users/user/mamba/envs/pysnt-dev/bin/python
Platform: macOS-26.0.1-arm64-arm-64bit-Mach-O
Architecture: arm64

📦 Core Dependencies:
  ✅ scyjava      1.12.1       (SciJava Python bridge)
  ✅ imagej       1.7.0        (PyImageJ)
  ✅ numpy        2.3.3        (NumPy)
  ✅ jdk          unknown      (install-jdk library (OpenJDK installer))

☕ Java Environment:
  ✅ Java version: 21 (OpenJDK)
  📍 Java executable: /Users/user/mamba/envs/pysnt-dev/lib/jvm/bin/java
  🏠 JAVA_HOME: /Users/user/mamba/envs/pysnt-dev/lib/jvm

🔬 SNT/Fiji Environment:
  ✅ PySNT initialized: Yes
  ℹ️ ImageJ version: 2.17.0/1.54p
  ℹ️ SNT version: 4.9.9-SNAPSHOT-04cbcaef56cfd037a0bd9a2d9a73050b86049d3b

📁 Installation:
  📍 PySNT location: /Users/user/code/pysnt/src/pysnt

💻 System Information:
  OS: Darwin 25.0.0
  CPU: arm
  Memory: 48 GB total, 21 GB available
```

### Test SNT Functionality

Now you can test that SNT access is fully functional:

```python
import pysnt
from pysnt import SNTService, Tree
pysnt.initialize()
snt_service = SNTService()  # Start SNT's SciJava service
print("✓ SNTService created successfully")

# Retrieve and display a demo neuron
tree = snt_service.demoTree('fractal')  # retrieve a toy neuron
print(f"✓ Demo tree loaded: {type(tree)}")

tree.show() # Display the reconstruction
```

Because SNT is running headless, the reconstruction is displayed as ascii art in the console.
We can also display it in a matplotlib figure:

```python
pysnt.display(tree)
```

## Next Steps

See [PySNT Overview](./overview.md) to learn the basics of PySNT.

## Troubleshooting

### Java Issues

PySNT includes Java management capabilities:

```python
# Check Java installation status
from pysnt.java_utils import print_java_status
print_java_status()
```

This will show detailed Java information:

```console
☕ Java Installation Status
==============================
✅ Java available: openjdk version "21.0.8" 2025-07-15 LTS
📍 Executable: /Users/user/mamba/envs/pysnt-dev/lib/jvm/bin/java
🏠 JAVA_HOME: /Users/user/mamba/envs/pysnt-dev/lib/jvm
🏢 Vendor: OpenJDK
✅ Version check: 21 >= 21 (recommended)
```

### Manual Java Setup

```python
# Ensure Java 21 or newer is available
from pysnt.java_utils import ensure_java_available
ensure_java_available(required_version=21)
```

```python
# Interactive Java setup wizard (experimental)
from pysnt.java_utils import setup_java_environment
setup_java_environment()
```

### Common Issues

1. **"Fiji not found" error** (only when a Fiji is requested explicitly): check the path passed to `fiji_path`,
   or set the `FIJI_PATH` environment variable. Omit both to use Maven instead.
2. **Java version issues**: Ensure Java 21+ is installed and accessible
3. **Memory issues**: Use memory configuration:
   ```python
   import pysnt
   pysnt.initialize(max_heap="8g")  # 8GB heap
   ```
4. **Import errors**: Make sure your shell or IDE uses the environment PySNT was installed into (see [Choosing an interpreter](#choosing-an-interpreter-ides-and-notebooks))

### Getting Help

```python
# Show version and system information
pysnt.show_version()
pysnt.info()

# Check configuration
pysnt.show_config_status()

# List available classes to verify SNT is working
pysnt.list_classes()
```

```{tip}
Do [reach out](https://forum.image.sc/tag/snt) if you run into issues!
```

## Next Steps

Once PySNT is installed and working:

1. **[Quickstart](quickstart.md)** - Learn essential workflows and concepts
2. **[PySNT Overview](overview.md)** - Dive deeper into core functionality and patterns
3. **[API Reference](api.md)** - Documentation of all functions and classes

[snt]: https://imagej.net/SNT
[api]: https://morphonets.github.io/SNT
[pyimagej]: https://github.com/imagej/pyimagej
[pyimagejdocs]: https://pyimagej.readthedocs.io/en/latest/
