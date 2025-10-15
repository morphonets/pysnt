```{raw} html
<div class="hero-header" style="margin: 2rem 0;">
    <div style="display: flex; align-items: center; gap: 2rem; margin-bottom: 1.5rem;">
        <div style="flex-shrink: 0;">
            <img src="_static/snt_logo.svg" alt="SNT Logo" class="hero-logo" style="height: 120px; width: auto;">
        </div>
        <div style="flex: 1;">
            <h1 style="margin: 0 0 0.5rem 0; font-size: 3rem; font-weight: 700;">PySNT</h1>
            <h2 style="margin: 0; font-size: 1.5rem; font-weight: 300; color: #666;">Trace, analyze, and quantify neuronal morphology — from Python.</h2>
        </div>
    </div>
    <p style="margin: 0; font-size: 1.1rem; line-height: 1.6;">PySNT brings <a href="https://github.com/morphonets/SNT" target="_blank">SNT</a>'s tracing tools and neuroanatomy analytics to Python. Use it interactively in notebooks or to automate large-scale studies.</p>
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
:img-top: _static/AA0100skel2d.png

Set up your environment and launch your first script with step-by-step guidance.
::::

::::{grid-item-card} <i class="fa-solid fa-calculator"></i> Analysis Tools  
:link: notebooks/2_convex_hull
:link-type: doc
:img-top: _static/convexhull.png

Comprehensive morphological analysis.
::::

::::{grid-item-card} <i class="fa-solid fa-chart-bar"></i> Visualizations
:link: notebooks/index
:link-type: doc
:img-top: _static/intersection-overview.png

Create publication-ready plots and interactive visualizations of neuronal data.
::::

::::{grid-item-card} <i class="fa-solid fa-gauge-high"></i> Performance
:link: notebooks/index
:link-type: doc
:img-top: _static/AA0100annot.png

Optimized algorithms for large-scale morphological analysis and batch processing.
::::

::::{grid-item-card} <i class="fa-solid fa-brain"></i> Atlas Analysis
:link: notebooks/index 
:link-type: doc
:img-top: _static/group0exemplars.png

Specialized tools for public datasets.
::::

::::{grid-item-card} <i class="fa-solid fa-boxes-stacked"></i> Much More
:link: notebooks/index
:link-type: doc
:img-top: _static/snt-growth-analysis.png

Single cell morphometry, Population Comparisons, Neurite growth analys, ...
::::

:::::

---

## Quick Links

```{raw} html
<div style="display: flex; gap: 1rem; flex-wrap: wrap; margin: 2rem 0;">
    <a href="api.html" style="text-decoration: none; color: #2980b9; font-weight: 500;">
        <i class="fas fa-code"></i> Python API Reference
    </a>
    <a href="notebooks/index.html" style="text-decoration: none; color: #2980b9; font-weight: 500;">
        <i class="fas fa-book"></i> Tutorials
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
notebooks/index
api
```
