---
title: "PySNT: Quantification of neuronal anatomy in Python"
---

# PySNT: Quantification of neuronal anatomy in Python
````{raw} html
<style>.bd-content h1 { display: none; }</style>
````

```{raw} html
<div class="hero-header" style="margin: 2rem 0;">
    <div style="display: flex; align-items: center; gap: 2rem; margin-bottom: 1.5rem;">
        <div style="flex-shrink: 0;">
            <img src="_static/snt_logo.svg" alt="SNT Logo" class="hero-logo" style="height: 120px; width: auto;">
        </div>
        <div style="flex: 1;">
            <h1 style="margin: 0 0 0.5rem 0; font-size: 3rem; font-weight: 700;">PySNT</h1>
            <h2 style="margin: 0; font-size: 1.5rem; font-weight: 340; color: #666;">Trace, analyze, and quantify neuronal morphology — from Python.</h2>
        </div>
    </div>
    <p style="margin: 0; font-size: 1.1rem; line-height: 1.5;">
    PySNT brings <a href="https://github.com/morphonets/SNT" target="_blank">SNT</a>'s tracing tools and neuroanatomy analytics to Python, providing a unified toolkit for morphometry that works interactively in notebooks or for automating large-scale studies.
    </p>
    </div>

<style>
/* Logo styling for dark mode compatibility */
.hero-logo {
    background: transparent !important;
    mix-blend-mode: multiply;
}

/* Dark theme logo adjustments */
[data-theme="dark"] .hero-logo {
    filter: invert(1) hue-rotate(180deg);
    mix-blend-mode: normal;
}

@media (max-width: 768px) {
    .hero-header > div:first-child {
        flex-direction: column !important;
        text-align: center !important;
        gap: 1rem !important;
    }
    .hero-header h1 {
        font-size: 2.5rem !important;
    }
    .hero-header h2 {
        font-size: 1.3rem !important;
    }
    .hero-header img {
        height: 100px !important;
    }
}
</style>
```

```{raw} html
<div class="hero-buttons">
    <a href="install.html" class="btn-secondary-custom">Get Started</a>
    <a target="_blank" href="https://imagej.net/plugins/snt/#overview" class="btn-secondary-custom"> See Gallery</a>
</div>
<a href="api.html" class="api-link">
    <i class="fas fa-code"></i> See API Reference →
</a>
```
---

:::::{grid} 1 2 2 3
:gutter: 3

::::{grid-item-card} <i class="fa-solid fa-rocket"></i> Getting Started
:link: install
:link-type: doc
:img-top: _static/front_page/tutorial01a.png

Set up your environment and run your first script with step-by-step guidance.
::::

::::{grid-item-card} <i class="fa-solid fa-calculator"></i> Morphometric Analysis
:link: notebooks/01_single_cell_analysis
:link-type: doc
:img-top: _static/front_page/tutorial01b.png

Quantify, transform, and compare neuronal morphology at single-cell and population levels.
::::

::::{grid-item-card} <i class="fa-solid fa-brain"></i> Atlas & Circuit Analysis
:link: notebooks/02_hemisphere_analysis
:link-type: doc
:img-top: _static/front_page/tutorial03a.png

Integrate reference brains, atlases, public databases, and whole-brain projectomes into your analysis.
::::

::::{grid-item-card} <i class="fa-solid fa-cube"></i> 3D Visualization
:link: notebooks/03_convex_hull
:link-type: doc
:img-top: _static/intersection-overview.png

Generate publication-ready figures and interactive 3D renderings of neuronal morphology.
::::

::::{grid-item-card} <i class="fa-solid fa-ruler-combined"></i> Geometric Analysis
:link: notebooks/04_tree_intersection
:link-type: doc
:img-top: _static/martinotti_intersection.png

Measure spatial extent, arbor overlap, and three-dimensional arrangements of dendritic and axonal trees.
::::

::::{grid-item-card} <i class="fa-solid fa-plug"></i> Python Ecosystem
:link: notebooks/05_napari_viewer
:link-type: doc
:img-top: _static/op1_napari.png

Interoperability with napari, pandas, NumPy, and the broader scientific Python stack.
::::

::::{grid-item-card} <i class="fa-solid fa-sitemap"></i> Classification of Cell Types
:link: notebooks/06_persistence_landscape
:link-type: doc
:img-top: _static/landscapes_clustering.png

Cluster and classify neurons using morphometric and topological features.
::::

::::{grid-item-card} <i class="fa-solid fa-crosshairs"></i> ML Ground Truth Curation
:link: notebooks/07_curvature_optimization
:link-type: doc
:img-top: _static/front_page/op1_tubeness_fit.png

Build quality-controlled training datasets: refine traces, detect crossovers, and validate reconstructions.
::::

::::{grid-item-card} <i class="fa-solid fa-ellipsis"></i> And More
:link: https://imagej.net/plugins/snt/#overview
:img-top: _static/front_page/sankey-flow-plot-with-tooltip.png

Sholl, Strahler, persistence diagrams, graph theory, growth dynamics, and full access to the SNT/Fiji ecosystem.
::::

:::::

---

## Quick Links

```{raw} html
<div style="display: flex; gap: 1rem; flex-wrap: wrap; margin: 2rem 0;">
    <a href="api.html" style="text-decoration: none; color: #2980b9; font-weight: 500;">
        <i class="fas fa-code"></i> Python API Reference
    </a>
    <a href="api_auto/method_index.html" style="text-decoration: none; color: #2980b9; font-weight: 500;">
        <i class="fa-solid fa-list-ul"></i> Method Index
    </a>
    <a href="api_auto/class_index.html" style="text-decoration: none; color: #2980b9; font-weight: 500;">
        <i class="fas fa-list"></i> Class Index
    </a>
    <a href="https://javadoc.scijava.org/SNT" target="_blank" style="text-decoration: none; color: #2980b9; font-weight: 500;">
        <i class="fas fa-coffee"></i> SNT Java API
    </a>
</div>
```

```{toctree}
:maxdepth: 2
:hidden:

install
quickstart
notebooks/index
```
