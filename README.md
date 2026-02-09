<p align="center"><img src="./docs/_static/snt_logo.svg" alt="SNT" width="150"></p>
<h1 align="center">PySNT</h1>
<h2 align="center">Python wrapper for SNT, the framework for quantification of neuronal anatomy</h2>
<div align="center">
  <!-- License -->
  <a href="https://github.com/morphonets/SNT/blob/master/LICENSE.txt">
    <img alt="GitHub license" src="https://img.shields.io/github/license/morphonets/SNT">
  </a>
  <!-- Forum -->
  <a href="https://forum.image.sc/tags/snt">
    <img alt="Forum.sc topics" src="https://img.shields.io/badge/dynamic/json.svg?label=forum&url=https%3A%2F%2Fforum.image.sc%2Ftag%2Fsnt.json&query=%24.topic_list.tags.0.topic_count&suffix=%20topics">
  </a>
  <!-- Issues -->
  <a href="https://github.com/morphonets/pysnt/issues">
    <img alt="Open issues" src="https://img.shields.io/github/issues/morphonets/pysnt">
  </a>
  <a href="https://github.com/morphonets/pysnt/issues">
    <img alt="Closed issues" src="https://img.shields.io/github/issues-closed/morphonets/pysnt">
  </a>
</div>
<div align="center">
  <h3>
    <a href="https://pysnt.readthedocs.io/en/latest/install.html">
      Installation
    </a>
    <span style="margin:.5em">|</span>
    <a href="https://pysnt.readthedocs.io/en/latest/index.html">
       Documentation
    </a>
    <span style="margin:.5em">|</span>
    <a href="https://forum.image.sc/tag/SNT">
      Support
    </a>
  </h3>
</div>


## Technical Features

- **Complete Java Bridge**: Full programmatic access to SNT's neuroanatomy toolkit from Python (via JPype and ScyJava),
  enabling integration of advanced tracing, analysis, and visualization capabilities into Python workflows
  
- **Consistent API**: 1:1 correspondence with SNT's Java API while maintaining Python conventions, allowing developers
  familiar with either language to work efficiently

- **Full Type Annotation**: Type hints for all methods and classes, enabling static type checking with mypy and improved
  code reliability
  
- **IDE Integration**: Autocomplete, inline documentation, and parameter hints in VS Code, PyCharm, Spyder, and Jupyter
  notebooks through type stubs and docstrings
  
- **Performant**: Lazy class loading minimizes initialization overhead, loading only required SNT components on demand

- **Native Python Converters**: Automatic conversion between SNT objects and Python-native types:
    
    | SNT/ImgLib2 Java Object | PySNT Python Object              |
    |-------------------------|----------------------------------|
    | SNTChart                | matplotlib Figure                |
    | SNTGraph                | NetworkX graph                   |
    | SNTTable                | xarray Dataset; pandas DataFrame |
    | ImgPlus/RAI             | xarray; numpy                    |
    | ImagePlus               | xarray; numpy (via ScyJava)      |
    | Collections             | lists/dicts, etc. (via ScyJava)  |



## Limitations
- **Bleeding Edge**: Requires building SNT from the main branch (stable release integration planned for SNT v5.0)

- **Early Stage Software**: Limited test coverage and community validation: Expect potential bugs and breaking API changes

## Getting Started for Users
See [Install instructions](https://pysnt.readthedocs.io/en/latest/install.html).


## Getting Started for Developers

### Environment Setup
```bash
# 1. Clone the repository
git clone https://github.com/morphonets/pysnt.git
cd pysnt

# 2. Set up conda/mamba (if not already configured)
mamba config append channels conda-forge
mamba config set channel_priority strict

# 3. Create and activate the development environment
mamba env create -f environment-dev.yml
mamba activate pysnt-dev

# 4. Install PySNT in development mode
pip install -e .[dev]

# 5. Verify the setup
python -c "import pysnt; print('PySNT imported successfully!')"

# 6. Have a look at ./dev/README.md for common workflows
```

### IDE Configuration

#### PyCharm
1. Open this folder as a project in PyCharm
2. Go to File → Settings → Project → Python Interpreter
3. Select the 'pysnt' environment

#### VS Code
1. Open this folder in VS Code
2. Install recommended extensions when prompted
3. Select the 'pysnt' Python interpreter when prompted

#### Spyder
1. Make sure Spyder is installed in the 'pysnt' environment:
   ```bash
    mamba activate pysnt
    mamba install spyder
    mamba install spyder-notebook -c conda-forge # Optional: support for tutorials notebooks
    ```
2. Launch Spyder from the activated environment
3. Open this folder as a project: Projects → New Project... → Existing Directory

### Project Structure

```
pysnt/
├── src/pysnt/           # main package source
├── tests/               # test suite
├── dev/scripts/         # development scripts
├── docs/                # documentation source
├── dev/                 # development utilities and templates
├── pyproject.toml       # packaging metadata and dependency groups
├── requirements.txt     # pip core runtime dependencies
├── requirements-gui.txt # pip optional runtime extras (display/gui/java/zarr)
├── requirements-dev.txt # pip development stack (extends requirements-gui.txt)
├── environment-min.yml  # minimal conda-compatible runtime environment
├── environment.yml      # full-featured conda-compatible runtime environment
└── environment-dev.yml  # full-featured conda-compatible development environment
```

### Dependency Files and Scope
- `pyproject.toml`: canonical dependency definitions for packaging and extras
- `requirements.txt`: core pip runtime set only
- `requirements-gui.txt`: optional runtime features layered on top of core (`display`, `gui`, `java`, `zarr`)
- `requirements-dev.txt`: development/test/docs tools layered on top of `requirements-gui.txt`
- `environment-min.yml`: smallest conda-compatible runtime setup
- `environment.yml`: full runtime conda-compatible setup with optional user-facing features
- `environment-dev.yml`: full runtime plus development/test/docs tools

### Dependencies
#### Core Dependencies (Required)
- JPype1 - Python/JVM bridge used by runtime utilities
- matplotlib - Used extensively for plotting and figure creation
- numpy - Used throughout for array operations
- pyimagej - ImageJ integration
- scyjava - Core Java integration
- xarray - Dataset operations

#### Optional Dependencies (Display/Conversion Features)
- cairosvg - SNTChart SVG to matplotlib conversion
- install-jdk - Automatic OpenJDK installation helper
- ipykernel - Notebook kernel support
- pandas - DataFrame operations and SNTTable conversion
- pandasgui - Interactive DataFrame display
- networkx - SNTGraph to NetworkX graph conversion
- pyobjc-core (macOS only) - Required by PyImageJ GUI mode on macOS
- pyobjc-framework-cocoa (macOS only) - Required by PyImageJ GUI mode on macOS
- PyMuPDF - SNTChart PDF to matplotlib conversion


#### Optional Dependencies (OME-ZARR)
- fsspec - Remote filesystem access (HTTP/HTTPS/S3)
- zarr - OME-ZARR format support for local and remote data

Install examples:
- `pip install -e .` (core)
- `pip install -e .[display]`
- `pip install -e .[gui]`
- `pip install -e .[all]`
- `pip install -e .[dev]`

> macOS users: PyImageJ GUI mode requires `pyobjc-core` and
`pyobjc-framework-cocoa` (or `pyobjc`). These are included in the GUI-focused
dependency files.

### Need Help?

- 📖 **Documentation**: [pysnt.readthedocs.io](https://pysnt.readthedocs.io)
- 💬 **Forum**: [forum.image.sc/tag/snt](https://forum.image.sc/tag/snt)
- 🐛 **Issues**: [GitHub Issues](https://github.com/morphonets/pysnt/issues)
