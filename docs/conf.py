# -- Project information -----------------------------------------------------
project = "pySNT"
author = "SNT contributors"
copyright = ""

# -- General configuration ---------------------------------------------------
extensions = [
    "myst_nb",                      # Notebooks as first-class docs pages
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "sphinx.ext.githubpages",
    "sphinx_design",
]

# Do NOT execute notebooks on RTD builds; use stored outputs instead
# To pre-execute notebooks via CI switch to "cache" and commit cached artifacts so RTD renders them instantly
nb_execution_mode = "off"

# MyST configuration
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "substitution",
]

# Intersphinx (cross-links to PyImageJ docs, etc.)
intersphinx_mapping = {
    "pyimagej": ("https://py.imagej.net/en/latest/", None),
}

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------
html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]
html_title = "pySNT"
html_logo = "_static/snt-logo.png"

html_theme_options = {
    "github_url": "https://github.com/morphonets/pysnt",
    "navigation_with_keys": True,
    "show_prev_next": True,
}

# Images produced by notebooks
nb_render_image_options = {"align": "center"}

# If you use relative links to notebooks, ensure paths are correct:
# (We keep notebooks under docs/notebooks/)