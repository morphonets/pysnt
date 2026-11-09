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

## Requirements

PySNT needs Python 3.11+ and Java 21+ (a JDK). The *pixi* and *conda/mamba* routes below install both for you; with
*pip*, PySNT can offer to download a JDK if none is found (see `ensure_java` below). SNT itself is downloaded
automatically the first time you call `pysnt.initialize()`, so no Fiji installation is required (unless
[you want to use a local Fiji](#attaching-to-snt)). The native *cairo* library is optional: it is only needed for SVG
chart conversion (see [Optional: SVG chart conversion](#optional-svg-chart-conversion)).

```{tip}
**New to Python?** Open a terminal (*Terminal* on macOS/Linux, *PowerShell* on Windows) and follow the *pixi* tab
below: it installs Python, Java and native libraries for you in one go. To get pixi, run
`curl -fsSL https://pixi.sh/install.sh | sh` (macOS/Linux) or
`powershell -ExecutionPolicy ByPass -c "irm -useb https://pixi.sh/install.ps1 | iex"` (Windows), then reopen the
terminal. See [pixi.sh](https://pixi.sh) for details.
```

## Install

```{important}
**Read this section before installing.** PySNT is not a regular Python package: it runs SNT, a Java application, inside your Python process (via JPype). Besides the Python package it needs a JDK 21+ (PySNT can offer to download one), so a bare `pip install pysnt` into an existing environment may not work. Install into a *fresh, dedicated* environment: PySNT pulls in a large Java/Python stack that could conflict with other packages.
```

```{note}
PySNT is available on [PyPI](https://pypi.org/project/pysnt/). To try unreleased changes instead, replace `pysnt[all]` in the commands below with `pysnt[all] @ git+https://github.com/morphonets/pysnt` (requires [git](https://git-scm.com/downloads)). Keep the quotes around the whole requirement, e.g. `pixi run pip install "pysnt[all] @ git+https://github.com/morphonets/pysnt"` (without them, PowerShell fails on the `@`). To get a specific version, append `@<tag or branch>` to the URL (e.g., `.../pysnt@dev`).
```

::::{tab-set}

:::{tab-item} pixi (recommended)
[pixi](https://pixi.sh) installs Python and a JDK from conda-forge and records the environment in a lock file.
If you have not installed pixi yet, see the tip above (and reopen the terminal afterwards).

```bash
pixi init pysnt-project
cd pysnt-project
pixi add python=3.12 openjdk=21 pip cairo jupyterlab
pixi run pip install "pysnt[all]"
pixi shell
```

`pixi shell` activates the environment: run `python` or `jupyter lab` from there. On Windows PowerShell, if it fails
with "running scripts is disabled on this system", run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` once
and retry.

**Coming back later?** Open a terminal and re-enter the environment:

```bash
cd pysnt-project
pixi shell
```

Alternatively, `pixi run jupyter lab` (from the `pysnt-project` folder) starts Jupyter directly.
:::

:::{tab-item} conda / mamba
```bash
mamba create -n pysnt -c conda-forge python=3.12 openjdk=21 pip cairo jupyterlab
mamba activate pysnt
python -m pip install "pysnt[all]"
```

Use `conda` in place of `mamba` if you do not have mamba. Next time, run `mamba activate pysnt` before using PySNT.
:::

:::{tab-item} pip
Use a dedicated virtual environment (Python 3.11+; JDK 21+ installed, or let PySNT download one, see below).
Create it:

```bash
python -m venv pysnt-env
```

Activate it:

- macOS/Linux: `source pysnt-env/bin/activate`
- Windows (PowerShell): `pysnt-env\Scripts\Activate.ps1`
- Windows (cmd): `pysnt-env\Scripts\activate.bat`
- Windows (Git Bash): `source pysnt-env/Scripts/activate`

Install PySNT:

```bash
python -m pip install "pysnt[all]"
```

Next time, activate the environment again before using PySNT. Notes:

- If `python` is not found, use `python3` (macOS/Linux) or `py` (Windows).
- If PowerShell refuses to run `Activate.ps1`, run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` once and
  retry.
- `pysnt[all]` includes all optional features except `napari` (heavy, Qt-based). For the basic, core install, use
  `pysnt` instead. Or pick extras individually: `display`, `gui`, `java`, `info`, `napari`.
- [uv](https://docs.astral.sh/uv/) users can run the same commands with `uv venv` and `uv pip install`.

```{note}
No JDK? Leave `ensure_java=True` (the default) in `pysnt.initialize()`: if no suitable JDK is found, PySNT offers
to download one.
```

```{note}
The optional `display` extra (SVG chart conversion) needs the native *cairo* library, which pip cannot install.
See [Optional: SVG chart conversion](#optional-svg-chart-conversion) below.
```
:::

::::

```{seealso}
To contribute to PySNT, see the
[Install Instructions for Developers](https://github.com/morphonets/pysnt?tab=readme-ov-file#getting-started-for-developers).
```

### Optional: SVG chart conversion

SVG chart conversion (via [CairoSVG](https://cairosvg.org)) needs the native *cairo* library. Without it PySNT
still works, but SVG-based chart conversion is unavailable.

```{important}
**Using pixi or conda/mamba? There is nothing to do:** the commands above already install *cairo* into the
environment. The instructions below are only for pip installs.
```

With pip, install *cairo* for your platform:

::::{tab-set}

:::{tab-item} Windows
CairoSVG relies on the external `libcairo` DLLs. The easiest way to get them on Windows is via pixi/conda/mamba (see
the *pixi* tab above). If you need to install them manually, you likely need the
[GTK runtime for Windows](https://cairosvg.org/documentation/).
:::

:::{tab-item} macOS
Install it with [Homebrew](https://brew.sh):

```bash
brew install cairo
```
:::

:::{tab-item} Linux
```bash
sudo apt install libcairo2      # Debian/Ubuntu
sudo dnf install cairo          # Fedora
sudo pacman -S cairo            # Arch
```
:::

::::

## Try it

### 1. Check the installation

With the environment active, run this in a terminal:

```bash
pysnt doctor
```

It should end with `0 failure(s)` (warnings, e.g. about the optional cairo library, are fine). The first run downloads
SNT and can take several minutes; this happens only once. Prefer to stay in Python? `pysnt.doctor()` prints the same
report. For a quick check that does not start Java, use `pysnt doctor --no-sanity-test`. If something fails, each
line comes with a hint (see also [Troubleshooting](#troubleshooting)).

### 2. Display a neuron

```python
import pysnt
pysnt.initialize()                 # First run downloads SNT: be patient (it could take a while)
print(f"PySNT version: {pysnt.version()}")

from pysnt import SNTService
tree = SNTService().demoTree("fractal")   # a toy neuron
pysnt.display(tree)                # Displays the reconstruction in a matplotlib figure
```

Run it in whichever front-end you prefer, with the environment active:

::::{tab-set}

:::{tab-item} Jupyter
Start JupyterLab, create a notebook that uses the environment's kernel, and paste the code in a cell. The figure
appears below the cell.

```bash
jupyter lab
```

JupyterLab is included in the pixi and conda/mamba commands above. With pip, install it first:
`python -m pip install jupyterlab`. For existing Jupyter installations and IDEs, see
[Choosing an interpreter](#choosing-an-interpreter-ides-and-notebooks).
:::

:::{tab-item} IPython / Python console
Start `ipython` (installed with `pysnt[all]`) or plain `python`, and paste the code. The figure opens in a
matplotlib window.
:::

:::{tab-item} Script
Save the code in a file, e.g. `try_pysnt.py`, and run it:

```bash
python try_pysnt.py
```

The figure opens in a matplotlib window. On Windows, use `py` instead of `python` if `python` is not found.
:::

::::

If a neuron is displayed, you are all set. By default PySNT runs headless, so `tree.show()` prints an ASCII rendering
in the console instead. Run `pysnt.info()` for a report of your Python, Java and SNT setup.

```{note}
SNT windows (e.g., the 3D viewer opened by `tree.show3D()`) need extra settings. See
[Interactive Viewers](limitations.md#interactive-viewers).
```

::::{dropdown} Messages printed during the first initialization

The first `pysnt.initialize()` may print lines such as:

```console
No version available for dependency org.jogamp.jogl:jogl-all:jar:natives-macosx-aarch64
No version available for dependency org.lwjgl:lwjgl:jar:${lwjgl.natives}:test
```

They come from the dependency resolver, which looks up platform-specific or test-only artifacts that SNT does not
need, and they appear only the first time: the result is cached, so later runs are silent. In our tests they were
harmless and can be ignored. If an SNT window fails to open, see [Troubleshooting](#troubleshooting) instead.
::::

### Choosing an Interpreter (IDEs and Notebooks)

Whatever you use, the one thing to get right is that it runs the Python of the environment above (and that
`JAVA_HOME`, if set, points to a JDK 21+).

**Jupyter** is the simplest way to follow the [tutorials](notebooks/index.md). With the environment active:

```bash
python -m pip install jupyterlab   # not needed with the pixi or conda/mamba setups above
jupyter lab
```

::::{dropdown} Other IDEs, or an Existing Jupyter Installation

- **Existing Jupyter**: `python -m pip install ipykernel` in the environment, then
  `python -m ipykernel install --user --name=pysnt` and select the `pysnt` kernel.
- **VS Code**: install the Python and Jupyter extensions, press `Ctrl/Cmd+Shift+P`, run *Python: Select
  Interpreter* and pick the environment (for notebooks, use the kernel picker at the top right).
- **PyCharm**: *Settings > Project > Python Interpreter > Add Interpreter > Existing*, and select the
  environment's `python`.
- **Spyder**: install `spyder-kernels` in the environment, then in *Preferences > Python interpreter* choose
  *Use the following interpreter* and select the environment's `python`.
::::

```{note}
The JVM can only be started once per Python process. If you change `initialize()` settings (heap size, source,
version), restart the kernel/console. In Spyder and Jupyter this means restarting the kernel. A second
`initialize()` call that asks for a different source (Maven vs. Fiji) logs a warning and is otherwise ignored.
```

### Attaching to SNT

By default, `pysnt.initialize()` downloads SNT from [Maven](limitations.md#maven-and-other-java-tooling)
([maven.scijava.org](https://maven.scijava.org/)) the first time and caches it for later runs. `pysnt.snt_version()` returns the version in use.

::::{dropdown} Advanced: using a local Fiji, or a specific SNT version

To use a local Fiji instead (e.g., to access your plugins or update sites), provide its path. PySNT picks the
first source that applies:

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
| `extras=[...]` | Maven only: additional Maven endpoints; `[]` skips the defaults (BigVolumeViewer). The JogAmp natives for your platform (needed by `Viewer3D`) are always added |

The Fiji location can also be configured from the command line:

```console
pysnt setup               # interactive setup
pysnt setup --auto-detect # search common locations and save the first valid one
pysnt setup --status      # show the current configuration
```

PySNT warns if the loaded SNT differs in major.minor from the version it was written for (e.g., an outdated
Fiji): classes or methods may then be missing. For a Fiji install, subscribe to the
[NeuroAnatomy update site](https://imagej.net/SNT#install) and run the Updater so that SNT is current.

Developing against a local snapshot of SNT (`mvn install`, which requires
[Maven](limitations.md#maven-and-other-java-tooling))? To make sure the new jar is used, clear the cache:

```{warning}
`rm -rf ~/.jgo ~/.cache/jgo` permanently deletes the cached SNT/jgo downloads. This is safe, but the next
`pysnt.initialize()` has to download everything again (several minutes).
```
::::

## Troubleshooting

**First step for any problem: run the doctor.** With the environment active, run this in a terminal (or
`pysnt.doctor()` in Python):

```bash
pysnt doctor
```

It checks Python, the required packages, Java (including whether Python and Java share the same architecture),
network access to the Maven repository and the optional cairo library. It also runs a sanity test in a separate
process (initialize PySNT, load a demo tree, render it), which downloads SNT on the first run. Use
`pysnt doctor --no-sanity-test` for a quick check that does not start Java. Each problem comes with a hint on how to
fix it. If you ask for help on the [forum](https://forum.image.sc/tag/snt), please paste the full report.
Interactive viewers (e.g., `Viewer3D`) are not tested.

| Symptom | Fix |
|---|---|
| `pixi: command not found` (or `'pixi' is not recognized`) | Close and reopen the terminal after installing pixi, so that it is on your `PATH` |
| `... cannot be loaded because running scripts is disabled on this system` (Windows PowerShell, e.g., from `Activate.ps1` or `pixi shell`) | Run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` once, then activate the environment again |
| `initialize()` seems stuck on first run | It is downloading SNT and its dependencies. This only happens once: subsequent runs use the cache |
| `IllegalArgumentException: Offscreen canvas cannot be displayed` when opening `Viewer3D`, `tree.show3D()`, etc. | PySNT starts in headless mode by default, in which SNT windows cannot open (PySNT prints a hint after the error). Initialize with `pysnt.initialize(mode='interactive')`; on macOS, also open the window with `pysnt.run_on_edt()` (see [GUI Threading Issues](limitations.md#gui-threading-issues)) |
| `GLException: Unable to determine GraphicsConfiguration` when opening `Viewer3D`, `tree.show3D()`, etc. | The 3D viewers need a working OpenGL driver. This is typical of virtual machines and remote desktops without GPU acceleration: install/update the graphics driver, or run PySNT on a machine with a GPU. In a VM without OpenGL support the 3D viewers may simply not be available. Static plots (e.g., `pysnt.display(tree)`) do not need OpenGL |
| `initialize()` hangs or fails with a network or SSL error | Check that your network (proxy/firewall) allows access to <https://maven.scijava.org>, and retry |
| JVM not found or cannot be loaded, although Java is installed | Python and the JDK must share the same architecture (e.g., both arm64 on Apple Silicon). The pixi and conda/mamba routes keep them consistent |
| `ModuleNotFoundError: pysnt`, or other import errors | Your shell/IDE is not using the environment PySNT was installed into. Activate it, or see [Choosing an interpreter](#choosing-an-interpreter-ides-and-notebooks). Use `python -m pip` rather than bare `pip` |
| `pip install` from GitHub fails with a `git` error | Install [git](https://git-scm.com/downloads), reopen the terminal and retry (only needed when installing the development version from GitHub) |
| Java not found, or wrong version | Leave `ensure_java=True` so PySNT offers to download a JDK, or install JDK 21+ and point `JAVA_HOME` to it (see below) |
| `java.lang.OutOfMemoryError` | Increase the heap: `pysnt.initialize(max_heap="8g")` |
| Changed `initialize()` settings have no effect | The JVM starts only once per session: restart the kernel/console |
| "Fiji not found" (only when a Fiji is requested explicitly) | Check the path passed to `fiji_path` or the `FIJI_PATH` environment variable. Omit both to use Maven instead |
| SVG chart conversion unavailable | Install the native *cairo* library (see [Optional: SVG chart conversion](#optional-svg-chart-conversion)) |
| `no library called cairo was found`, although cairo is installed with Homebrew (macOS) | Python may not search Homebrew's library folder. Run `export DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib` in the terminal before starting Python (or add it to your shell profile) |

::::{dropdown} Checking and fixing Java from Python

```python
from pysnt.java_utils import print_java_status, ensure_java_available
print_java_status()                           # Shows the Java in use (version, JAVA_HOME, vendor)
ensure_java_available(required_version=21)    # Makes sure Java 21+ is available
```

An interactive wizard is also available (experimental): `from pysnt.java_utils import setup_java_environment`,
then `setup_java_environment()`.
::::

Other diagnostics: `pysnt.show_version()`, `pysnt.info()`, `pysnt.show_config_status()` and `pysnt.list_classes()`
(lists the SNT classes available).

```{tip}
Do [reach out](https://forum.image.sc/tag/snt) if you run into issues!
```

## Next Steps

1. **[Quickstart](quickstart.md)**: Learn essential workflows and concepts
2. **[PySNT Overview](overview.md)**: Dive deeper into core functionality and patterns
3. **[Tutorials](notebooks/index.md)**: Worked examples as Jupyter notebooks
4. **[API Reference](api.md)**: Documentation of all functions and classes
