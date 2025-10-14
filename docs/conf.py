# -- Project information -----------------------------------------------------
project = "PySNT"
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
    "sphinx_copybutton",            # Copy-to-clipboard buttons for code blocks
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

# Custom MyST substitutions for FontAwesome icons
myst_substitutions = {
    "fa-microscope": '<i class="fas fa-microscope"></i>',
    "fa-download": '<i class="fas fa-download"></i>',
    "fa-book": '<i class="fas fa-book"></i>',
    "fa-rocket": '<i class="fas fa-rocket"></i>',
    "fa-github": '<i class="fab fa-github"></i>',
    "fa-code": '<i class="fas fa-code"></i>',
    "fa-chart-bar": '<i class="fas fa-chart-bar"></i>',
}

# Copy button configuration
copybutton_prompt_text = r">>> |\.\.\. |\$ |In \[\d*\]: | {2,5}\.\.\.: | {5,8}: "
copybutton_prompt_is_regexp = True
copybutton_only_copy_prompt_lines = True
copybutton_remove_prompts = True
copybutton_copy_empty_lines = False

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
html_title = "PySNT"
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
    "announcement": "🚧 Experimental project - <a href='https://github.com/morphonets/pysnt/issues' target='_blank'>feedback welcome</a>! 🚧"
}

# Images produced by notebooks
nb_render_image_options = {"align": "center"}
