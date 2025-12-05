# <i class="fas fa-book"></i>&hairsp;Tutorials

### Running Notebooks Locally
1. **Install PySNT** following the [installation guide](../install.md)
2. **Download notebooks**: Find them in the `./docs/notebooks/` directory of PySNT's source code, or use the download button (↓) at the top of each notebook page
3. **Open in Jupyter Lab** or your preferred IDE within your pysnt environment

```{note}
If you haven't installed PySNT's GUI dependencies, you'll need to install `ipykernel` first:
```bash
pip install ipykernel # or mamba install -n pysnt ipykernel
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
5_persistence_landscape
```

```{important}
🚧 **Work in Progress:** This notebook collection is being updated for SNT v5. 🚧

- <i class="fas fa-star"></i> **Updated** — Compatible with SNT v5 and the latest pysnt version
- <i class="fas fa-clock-rotate-left"></i> **Legacy** — Not yet updated and use outdated syntax

Check the icon at the top of each notebook to verify its status.
```