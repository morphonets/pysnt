# <i class="fas fa-book"></i>&hairsp;Tutorials

### Running Notebooks Locally
1. **Install PySNT** following the [installation guide](../install.md)
2. **Download notebooks**: Find them in the `./docs/notebooks/` directory of PySNT's source code, or use the download button (↓) at the top of each notebook page
3. **Open in Jupyter Lab** (`jupyter lab`) or your preferred IDE, within your pysnt environment

```{note}
Jupyter Lab is included in the pixi setup of the [installation guide](../install.md). Otherwise, run
`python -m pip install jupyterlab` in your environment. For other IDEs and kernels, see
[Choosing an interpreter](../install.md#choosing-an-interpreter-ides-and-notebooks).
```

```{seealso}
- [Install](../install.md) - Installation instructions
- [Quickstart](../quickstart.md) - Get started quickly
- [Overview](../overview.md) - Tour of pysnt's architecture
- [Limitations and Quirks](../limitations.md) - Known limitations and workarounds
```

## Available Tutorials

```{toctree}
:maxdepth: 1

01_single_cell_analysis
02_hemisphere_analysis
03_convex_hull
04_tree_intersection.ipynb
05_napari_viewer.ipynb
06_persistence_landscape
07_curvature_optimization
08_crossover_detection
```