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

PySNT needs Python 3.11+ and Java 21+ (a JDK). SNT itself is downloaded automatically the first time you call
`pysnt.initialize()`, so no Fiji installation is required. Any Python environment manager works; we document pixi
and pip.

```{tip}
**New to Python?** Open a terminal (*Terminal* on macOS/Linux, *PowerShell* on Windows) and follow the *pixi* tab
below: it installs Python, Java and native libraries for you in one go. To get pixi, run
`curl -fsSL https://pixi.sh/install.sh | sh` (macOS/Linux) or
`powershell -ExecutionPolicy ByPass -c "irm -useb https://pixi.sh/install.ps1 | iex"` (Windows), then reopen the
terminal. See [pixi.sh](https://pixi.sh) for details.
```

## Install

Install into a *fresh, dedicated* environment: PySNT pulls in a large Java/Python stack and mixing it with other
projects invites version conflicts.

```{warning}
PySNT will be available on PyPI. Until then, install it straight from GitHub: in the
commands below, replace `pysnt[all]` with `pysnt[all] @ git+https://github.com/morphonets/pysnt`. This requires
[git](https://git-scm.com/downloads) to be installed. To get a specific version, append `@<tag or branch>` to the
URL (e.g., `.../pysnt@dev`).
```

::::{tab-set}

:::{tab-item} pixi
[pixi](https://pixi.sh) installs Python, a JDK and Maven from conda-forge and records the environment in a lock file.

```bash
pixi init pysnt-project
cd pysnt-project
pixi add python=3.12 openjdk=21 maven pip cairo jupyterlab
pixi run pip install "pysnt[all]" # pixi run pip install "pysnt[all] @ git+https://github.com/morphonets/pysnt"
pixi shell
```

Already use conda or mamba? Create an environment with the same `python`, `openjdk=21`, `maven` and `cairo`
packages from conda-forge, then run `pip install "pysnt[all]"` inside it.
:::

:::{tab-item} pip
Use a dedicated virtual environment (Python 3.11+, JDK 21+ installed or let PySNT download one, see below):

```bash
python -m venv pysnt-env
source pysnt-env/bin/activate      # Windows: pysnt-env\Scripts\activate
python -m pip install "pysnt[all]" # python -m pip install "pysnt[all] @ git+https://github.com/morphonets/pysnt"
```

On macOS/Linux, use `python3` if `python` is not found. `pysnt[all]` includes all optional features except `napari` (heavy, Qt-based). For the basic,
core install, use `pysnt` instead. Or pick extras individually: `display`, `gui`, `java`, `zarr`, `info`, `napari`.
[uv](https://docs.astral.sh/uv/) users can run the same commands with `uv venv` and `uv pip install`.

```{note}
No JDK? Leave `ensure_java=True` (the default) in `pysnt.initialize()`: if no suitable JDK is found, PySNT offers
to download one.
```

```{note}
The optional `display` extra (SVG chart conversion) needs the native *cairo* library, which pip cannot install: use
`brew install cairo` (macOS) or `apt install libcairo2` (Linux). Without it PySNT still works, but SVG-based chart
conversion is unavailable.
```
:::

::::

To contribute to PySNT (editable install from a clone), see
[Install Instructions for Developers](https://github.com/morphonets/pysnt?tab=readme-ov-file#getting-started-for-developers).

## Try it

With the environment active, run the following in Python (or paste it in a notebook cell):

```python
import pysnt
pysnt.initialize()                 # First run downloads SNT: this may take several minutes
print(f"PySNT version: {pysnt.version()}")

from pysnt import SNTService
tree = SNTService().demoTree("fractal")   # a toy neuron
pysnt.display(tree)                # Displays the reconstruction in a matplotlib figure
```

If a neuron is displayed, you are all set. Because SNT runs headless, `tree.show()` prints an ASCII rendering in the
console instead. Run `pysnt.info()` for a report of your Python, Java and SNT setup.

### Choosing an Interpreter (IDEs and Notebooks)

Whatever you use, the one thing to get right is that it runs the Python of the environment above (and that
`JAVA_HOME`, if set, points to a JDK 21+).

**Jupyter** is the simplest way to follow the [tutorials](notebooks/index.md). With the environment active:

```bash
python -m pip install jupyterlab   # not needed with the pixi setup above
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

By default, `pysnt.initialize()` downloads SNT from [Maven](https://maven.scijava.org/) the first time and caches
it for later runs. `pysnt.snt_version()` returns the version in use.

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

Developing against a local snapshot of SNT (`mvn install`)? Clear the cached environment so that the new jar is
used: `rm -rf ~/.jgo ~/.cache/jgo`
::::

## Troubleshooting

| Symptom | Fix |
|---|---|
| `initialize()` seems stuck on first run | It is downloading SNT and its dependencies (several minutes). Subsequent runs use the cache |
| `ModuleNotFoundError: pysnt`, or other import errors | Your shell/IDE is not using the environment PySNT was installed into. Activate it, or see [Choosing an interpreter](#choosing-an-interpreter-ides-and-notebooks). Use `python -m pip` rather than bare `pip` |
| `pip install` from GitHub fails with a `git` error | Install [git](https://git-scm.com/downloads), reopen the terminal and retry (only needed until PySNT is on PyPI) |
| Java not found, or wrong version | Leave `ensure_java=True` so PySNT offers to download a JDK, or install JDK 21+ and point `JAVA_HOME` to it (see below) |
| `java.lang.OutOfMemoryError` | Increase the heap: `pysnt.initialize(max_heap="8g")` |
| Changed `initialize()` settings have no effect | The JVM starts only once per session: restart the kernel/console |
| "Fiji not found" (only when a Fiji is requested explicitly) | Check the path passed to `fiji_path` or the `FIJI_PATH` environment variable. Omit both to use Maven instead |
| SVG chart conversion unavailable | Install the native *cairo* library (see the pip tab above) |

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
