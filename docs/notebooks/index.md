# Computational Neuroanatomy with PySNT

```{raw} html
<style>.bd-article h1:first-of-type { display: none; }</style>
<header class="paper-header">
  <h1 class="paper-title">Computational Neuroanatomy with PySNT</h1>
  <p class="paper-subtitle">A Hands-on, Self-paced Curriculum for Neuroanatomy in Python</p>
  <p class="paper-authors">
    Tiago A. Ferreira<sup>1,<a href="https://orcid.org/0000-0001-6866-1540" target="_blank" rel="noopener" title="ORCID" class="orcid-link"><i class="fa-brands fa-orcid"></i></a></sup>,
    <a href="https://github.com/morphonets/pysnt/graphs/contributors">PySNT</a>, and 
    <a href="https://github.com/morphonets/snt/graphs/contributors">SNT </a> contributors
  </p>
  <p class="paper-affiliations"><sup>1</sup>Janelia Research Campus, Howard Hughes Medical Institute</p>
  <div class="paper-abstract">
    <p>This curriculum is a curated series of self-contained, runnable notebooks, each with explicit
    learning objectives, an estimated completion time, and real data. Ordered by increasing complexity, 
    the series covers the full path from a single reconstruction to atlas-scale analysis and ML-ready
    ground truth.</p>
  </div>
</header>
```

## Preface

Quantitative neuroanatomy has outgrown the single-cell, single-software
workflow. Reconstructions now come from many sources (manual tracing, automated
pipelines, public databases), are registered to reference brains, and increasingly serve
as ground truth for machine learning. This curriculum teaches how to work with
that data in Python, using [SNT](https://imagej.net/plugins/snt/) through
PySNT alongside the standard Python tools for data analysis (NumPy, pandas, NetworkX, 
napari, scikit-learn, etc.).

**Who it is for.** Neuroscientists and image analysts who are comfortable with
basic Python and want to analyze, visualize, and curate neuronal morphology
reproducibly. No prior SNT or Java experience is needed.

**What you will learn.** How to load and measure reconstructions, place them in
annotated atlases, compare and classify cells, interoperate with the wider
scientific Python ecosystem, and build quality-controlled datasets from
volumes too large to fit in memory.

**Beyond SNT.** The concepts taught here (morphometric analysis, topological
classification, trace refinement, etc.) are independent of SNT and PySNT.
They apply equally to other reconstruction software, imaging modalities, cell types,
and organisms, and the underlying ideas transfer to any branching structure. Where a
tutorial relies on the wider Python ecosystem, the same workflow should be adaptable
to your own tools and data.

**What it does not cover.** Interactive tracing in the SNT graphical interface
is documented in the [SNT user manual](https://imagej.net/plugins/snt/), and
general Python or neuroscience background is assumed.

**How to use it.** Tutorials are self-contained notebooks ordered by
increasing complexity. Start with T01 and follow the sequence, or jump to the
track that matches your task. Each notebook states its learning objectives,
estimated time, and any extra requirements at the top.

**Navigating the site.** The sidebar on the left lists all tutorials, and each
page has a clickable outline of its sections on the right. Notebook pages offer
a download button for the `.ipynb` file, and the theme switcher in the top bar
toggles dark mode. Class and method names link to the [API reference](../api.md).

## Curriculum

:::::{grid} 1 2 2 3
:gutter: 3

::::{grid-item-card} <i class="fa-solid fa-calculator"></i> T01: Single Cell Analysis
:link: 01_single_cell_analysis
:link-type: doc
:img-top: ../_static/front_page/tutorial01b.png

Load reconstructions, measure morphology, map and plot metrics, and transform trees.

{bdg-success}`Beginner` {bdg-secondary-line}`20-30 min` {bdg-primary}`Fundamentals`
::::

::::{grid-item-card} <i class="fa-solid fa-plug"></i> T02: Visualizing Reconstructions in napari
:link: 02_napari_viewer
:link-type: doc
:img-top: ../_static/op1_napari.png

Render reconstructions in napari as centerlines, nodes, or color-coded 3D surfaces, and overlay them on images.

{bdg-success}`Beginner` {bdg-secondary-line}`10-15 min` {bdg-primary}`Interop` {bdg-info-line}`napari`
::::

::::{grid-item-card} <i class="fa-solid fa-brain"></i> T03: Hemisphere Analysis
:link: 03_hemisphere_analysis
:link-type: doc
:img-top: ../_static/front_page/tutorial03a.png

Quantify ipsilateral and contralateral projections of MouseLight neurons using the Allen CCF.

{bdg-success}`Beginner` {bdg-secondary-line}`30 min` {bdg-primary}`Fundamentals`
::::

::::{grid-item-card} <i class="fa-solid fa-cube"></i> T04: Volumetric Quantifications
:link: 04_convex_hull
:link-type: doc
:img-top: ../_static/intersection-overview.png

Convex hulls and PCA of axonal terminals, compared against brain-region volumes.

{bdg-warning}`Intermediate` {bdg-secondary-line}`30-40 min` {bdg-primary}`Fundamentals`
::::

::::{grid-item-card} <i class="fa-solid fa-ruler-combined"></i> T05: Spatial Intersection Between Trees
:link: 05_tree_intersection
:link-type: doc
:img-top: ../_static/martinotti_intersection.png

Overlap of axonal and dendritic arbors with NetworkX, trimesh, and NumPy.

{bdg-warning}`Intermediate` {bdg-secondary-line}`30-40 min` {bdg-primary}`Spatial analysis` {bdg-primary}`Interop` {bdg-info-line}`NeuroMorpho.org`
::::

::::{grid-item-card} <i class="fa-solid fa-sitemap"></i> T06: Unsupervised Classification of Projection Neurons
:link: 06_persistence_landscape
:link-type: doc
:img-top: ../_static/landscapes_clustering.png

Cluster neurons using persistent homology and persistence landscapes.

{bdg-warning}`Intermediate` {bdg-secondary-line}`40 min` {bdg-primary}`Classification` {bdg-info-line}`scikit-learn`
::::

::::{grid-item-card} <i class="fa-solid fa-crosshairs"></i> T07: Curvature Optimization with Automated Path Tracing
:link: 07_curvature_optimization
:link-type: doc
:img-top: ../_static/front_page/op1_tubeness_fit.png

Refine coarse traces and assign radii by re-tracing along image signal.

{bdg-danger}`Advanced` {bdg-secondary-line}`45 min` {bdg-primary}`Ground truth`
::::

::::{grid-item-card} <i class="fa-solid fa-code-merge"></i> T08: Crossover Detection
:link: 08_crossover_detection
:link-type: doc
:img-top: ../_static/front_page/tutorial08a.png

Find neurites that pass close without connecting, for QC of traces.

{bdg-danger}`Advanced` {bdg-secondary-line}`15-20 min` {bdg-primary}`Ground truth`
::::

::::{grid-item-card} <i class="fa-solid fa-database"></i> T09: Handling Large-Scale Neuronal Data
:link: 09_big_data
:link-type: doc

Stream and trace OME-ZARR volumes that exceed RAM, with GPU rendering.

{bdg-danger}`Advanced` {bdg-secondary-line}`30 min` {bdg-primary}`Scale` {bdg-info-line}`OME-ZARR`
::::

:::::


## Running Notebooks Locally
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

## Source Code and License

The source of every tutorial is available on
[GitHub](https://github.com/morphonets/pysnt/tree/main/docs/notebooks), along
with the PySNT code it exercises. Licensing terms are described in the
repository's [license file](https://github.com/morphonets/pysnt/blob/main/LICENSE.md).
Corrections, new tutorials, and feedback are welcome on the
[forum](https://forum.image.sc/tag/snt) or as
[issues](https://github.com/morphonets/pysnt/issues).

## Citing

To cite the series, use the following format (replace the tutorial accordingly):

> *Computational Neuroanatomy with PySNT* (T0X). In T. A. Ferreira (Ed.),
> <https://pysnt.readthedocs.io/en/latest/notebooks/index.html>

See [SNT citation](https://imagej.net/plugins/snt/faq#how-do-i-cite-snt) for details on how to properly cite SNT.

```{toctree}
:maxdepth: 1
:hidden:

Overview <self>
01_single_cell_analysis
02_napari_viewer
03_hemisphere_analysis
04_convex_hull
05_tree_intersection
06_persistence_landscape
07_curvature_optimization
08_crossover_detection
09_big_data
```
