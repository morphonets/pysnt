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


The stack of dependencies used by PySNT is rather complex and includes Python 3.11+, Java 21+, [SNTv5](https://github.com/morphonets/SNT/releases), [imglyb](https://github.com/imglib/imglyb), [jgo](https://github.com/scijava/jgo), [numpy](https://github.com/numpy/numpy), [pyimagej][pyimagejdocs], [scyjava](https://github.com/scijava/scyjava), among others. Because of this complexity we recommend using a package manager. We endorse Mamba
since Conda can be painfully slow with complex environments. If you do not have Mamba installed you can do
so by [Installing Miniforge3](https://github.com/conda-forge/miniforge#miniforge3).

```{important}
In the future, PySNT will automatically download SNT if it is not found. For now, you'll need to download it manually
(see installation instructions below).
```

Here we only summarize the _easiest_ way to install pysnt. For other (advanced) install options (via pip, condacolab,
dynamic install, etc.) you should be able to adapt the advanced install documentation of [pyimagej][pyimagejdocs]. If
you want to debug or improve PySNT have a look at
[Install Instructions for Developers](https://github.com/morphonets/pysnt?tab=readme-ov-file#getting-started-for-developers).

## Setting Up

1. Assuming you have `mamba` installed, activate conda-forge:

   ```bash
   mamba config prepend channels conda-forge
   conda config --set channel_priority strict
   ```

2. [Clone](https://github.com/morphonets/pysnt.git) or [download](https://github.com/morphonets/pysnt/archive/refs/heads/main.zip) pysnt

   ```bash
   cd /path/to/hosting/directory
   git clone https://github.com/morphonets/pysnt.git
   ```

3. Create a new `pysnt` environment using the provided `environment.yml` file. This will install all the needed dependencies:

   ```bash
   cd ./pysnt  # cd to pysnt root directory
   mamba env create -f environment.yml
   ```

   **Environment Options**: Other environment files are also provided for more granular installations:

   | File                | Scope/Comments                                        |
   |---------------------|-------------------------------------------------------|
   | environment.yml     | Full install with interactive GUI features  (default) |
   | environment-min.yml | Minimal CLI install with core dependencies only       |
   | environment-dev.yml | Full install plus dev tools for contributing to PySNT |

4. Install pysnt in editable/development mode

   ```bash
   mamba activate pysnt  # activate the newly created environment
   pip install -e .
   ```

5. Test that PySNT has been successfully installed, by displaying its version:

   ```bash
   mamba activate pysnt
   python -c "import pysnt; print(f'Using PySNT version: {pysnt.version()}')"
   ```

   Which should print something like:
   ```bash
   Using PySNT version: 0.0.1
   ```

6. **Optional**: Make the new `pysnt` environment available in Jupyter notebooks:

   ```bash
   mamba activate pysnt
   mamba install ipykernel # Only if you haven't done so yet (i.e., if you used environment-min.yml)
   python -m ipykernel install --user --name=pysnt
   ```

   Now, when you start jupyter (or Jupyter lab), it will show `pysnt` in the list of registered kernels. Selecting it makes all the packages installed in the `pysnt` environment available.


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
4. **Import errors**: Make sure you've activated the correct conda environment

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
