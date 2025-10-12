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
html_css_files = [
    "custom.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css"
]
html_js_files = [
    "theme-toggle.js"
]
html_title = "pySNT"
html_logo = "_static/snt-logo.png"

html_theme_options = {
    "logo": {
        "image_light": "_static/snt-logo.png",
        "image_dark": "_static/snt-logo.png",
    },
    "navigation_with_keys": True,
    "show_prev_next": True,
    "navbar_start": ["navbar-logo"],
    "navbar_center": [],
    "navbar_end": [],
    "show_toc_level": 2,
    "navigation_depth": 3,
    "show_version_warning_banner": False,
    "article_header_start": [],
    "article_header_end": [],
    "article_footer_items": [],
    "content_footer_items": [],
    "secondary_sidebar_items": [],
    "primary_sidebar_end": [],
    # Work in progress banner
    "announcement": "🚧 Documentation in progress - <a href='https://github.com/morphonets/pysnt/issues' target='_blank'>feedback welcome</a>!"
}

# Images produced by notebooks
nb_render_image_options = {"align": "center"}
