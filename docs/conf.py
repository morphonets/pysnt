# -- RTD Environment Setup -------------------------------------------------
import os
import sys

# Set stable timezone and locale before any imports
os.environ['TZ'] = 'UTC'
os.environ['LC_ALL'] = 'C.UTF-8'
os.environ['LANG'] = 'C.UTF-8'

# Prevent timezone changes during initialization
os.environ['PYTHONDONTWRITEBYTECODE'] = '1'

# Initialize timezone early and safely
try:
    import time
    import datetime
    import locale
    
    # Set locale to C to avoid timezone issues
    try:
        locale.setlocale(locale.LC_ALL, 'C.UTF-8')
    except locale.Error:
        try:
            locale.setlocale(locale.LC_ALL, 'C')
        except locale.Error:
            pass
    
    # Initialize time module
    if hasattr(time, 'tzset'):
        time.tzset()
    
    # Pre-warm datetime
    datetime.datetime.now()
    
except Exception:
    # If anything fails, continue anyway
    pass  # Ignore any timezone initialization errors

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
    "sphinx.ext.linkcode",          # Add source code links
    "sphinx.ext.githubpages",
    "sphinx_design",
    "sphinx_copybutton",            # Copy-to-clipboard buttons for code blocks
]

# Mock imports for Read the Docs (avoid importing heavy dependencies)
import sys
from unittest.mock import MagicMock

class MockModule(MagicMock):
    @classmethod
    def __getattr__(cls, name):
        if name in ('__version__', 'version'):
            return '1.0.0'
        return MagicMock()

MOCK_MODULES = [
    'cairosvg',
    'fitz',
    'install_jdk',
    'jdk',
    'jpype',
    'matplotlib',
    'matplotlib.figure',
    'matplotlib.pyplot',
    'matplotlib.image',
    'numpy',
    'pandas',
    'pandasgui',
    'psutil',
    'pyimagej',
    'pyobjc',
    'pyobjc_core',
    'pyobjc_framework_cocoa',
    'scyjava',
    'xarray',
]

for mod_name in MOCK_MODULES:
    sys.modules[mod_name] = MockModule()

# Special handling for numpy version (pandas needs this)
sys.modules['numpy'].__version__ = '1.24.0'

# Autodoc configuration
autodoc_mock_imports = MOCK_MODULES
autodoc_default_options = {
    'members': True,
    'member-order': 'bysource',
    'special-members': '__init__',
    'undoc-members': True,
    'exclude-members': '__weakref__',
    'show-inheritance': True,
}

# More compact API documentation
autodoc_typehints = 'signature'  # Show type hints in signature, not description
autodoc_typehints_format = 'short'  # Use short form of type hints
autodoc_preserve_defaults = True  # Show actual default values
add_module_names = False  # Don't show module names in API docs

# Add the source directory to the path for autodoc
import os
sys.path.insert(0, os.path.abspath('../src'))

# Do NOT execute notebooks on RTD builds; use stored outputs instead
# To pre-execute notebooks via CI switch to "cache" and commit cached artifacts so RTD renders them instantly
nb_execution_mode = "off"
nb_execution_timeout = 30
nb_execution_allow_errors = True
nb_execution_excludepatterns = ["*"]  # Exclude all notebooks from execution

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

# Ensure proper navigation structure
master_doc = 'index'

# Global toctree for navigation - let theme handle it automatically
html_static_path = ["_static"]
html_css_files = [
    "custom.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css"
]
html_title = "PySNT"

html_theme_options = {
    "navigation_with_keys": True,
    "show_prev_next": True,
    "navbar_start": ["navbar-logo"],
    "navbar_center": ["navbar-nav"],
    "navbar_end": ["theme-switcher", "navbar-icon-links"],  # Add built-in theme switcher
    "header_links_before_dropdown": 6,
    "show_toc_level": 2,
    "navigation_depth": 3,
    "show_version_warning_banner": False,
    "article_header_start": [],
    "article_header_end": ["article-header-buttons.html"],
    "article_footer_items": [],
    "content_footer_items": [],
    # Enable secondary sidebar (right TOC) for all pages except index
    "secondary_sidebar_items": {
        "**": ["page-toc", "edit-this-page"],
        "index": [],  # No TOC on index page
    },
    "primary_sidebar_end": [],
    # External links for navbar
    "external_links": [
        {
            "name": '<i class="fas fa-book-open"></i>&hairsp;Guide',
            "url": "https://imagej.net/plugins/snt/",
        },
        {
            "name": '<i class="fa-solid fa-comment"></i>&hairsp;Forum',
            "url": "https://forum.image.sc/tag/snt",
        },
        {
            "name": '<i class="fas fa-hands-helping"></i>&hairsp;Extend',
            "url": "https://imagej.net/plugins/snt/contribute",
        },
    ],
    # Icon links for navbar end
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/morphonets/pysnt",
            "icon": "fab fa-github-square",
            "type": "fontawesome",
        },
    ],
    # Work in progress banner
    "announcement": "🚧 Experimental project - <a href='https://github.com/morphonets/pysnt/issues' target='_blank'>feedback welcome</a>! 🚧",
    # GitHub integration for edit buttons
    "use_edit_page_button": True,
}

# GitHub context for edit buttons
html_context = {
    "github_user": "morphonets",
    "github_repo": "pysnt",
    "github_version": "main",
    "doc_path": "docs",
}

# Images produced by notebooks
nb_render_image_options = {"align": "center"}

# -- Source code links configuration ----------------------------------------

def linkcode_resolve(domain, info):
    """
    Determine the URL corresponding to Python object.
    
    This function is called by sphinx.ext.linkcode to generate source code links.
    """
    if domain != 'py':
        return None
    
    if not info['module']:
        return None
    
    # Get the module and object name
    module_name = info['module']
    fullname = info['fullname']
    
    # Only link to our own modules (pysnt.*)
    if not module_name.startswith('pysnt'):
        return None
    
    # GitHub repository information
    github_user = "morphonets"
    github_repo = "pysnt"
    github_branch = "main"  # or "master" depending on your default branch
    
    try:
        # Import the module to get the source file
        import importlib
        import inspect
        
        # Handle submodules
        try:
            mod = importlib.import_module(module_name)
        except ImportError:
            return None
        
        # Get the object from the module
        obj = mod
        for part in fullname.split('.'):
            try:
                obj = getattr(obj, part)
            except AttributeError:
                return None
        
        # Get the source file and line number
        try:
            source_file = inspect.getsourcefile(obj)
            source_lines = inspect.getsourcelines(obj)
            line_number = source_lines[1]
        except (OSError, TypeError):
            return None
        
        if source_file is None:
            return None
        
        # Convert absolute path to relative path from project root
        import os
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        
        try:
            rel_path = os.path.relpath(source_file, project_root)
        except ValueError:
            # Can't make relative path (different drives on Windows, etc.)
            return None
        
        # Normalize path separators for URLs
        rel_path = rel_path.replace(os.sep, '/')
        
        # Construct GitHub URL
        github_url = (
            f"https://github.com/{github_user}/{github_repo}/blob/{github_branch}/"
            f"{rel_path}#L{line_number}"
        )
        
        return github_url
        
    except Exception:
        # If anything goes wrong, just don't provide a link
        return None
