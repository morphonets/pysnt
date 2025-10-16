"""
Template for PySNT module __init__.py files.

This template provides the standard structure for PySNT submodules that use
the common_module functionality for class management and placeholder generation.

Usage:
1. Copy this template to your new module directory as __init__.py
2. Update the module docstring and package information
3. Edit CURATED_CLASSES and EXTENDED_CLASSES lists

4. Run `python scripts/generate_placeholders.py` to generate placeholder classes
5. Test your module with `python -c "import src.pysnt.your_module"`

Example:
    For a new "morphology" analysis module:
    1. Create src/pysnt/analysis/morphology/__init__.py from this template
    2. Set package_name = "sc.fiji.snt.analysis.morphology"
    3. Add your classes to CURATED_CLASSES and EXTENDED_CLASSES
    4. Generate placeholders and test
"""

# =============================================================================
# MODULE CONFIGURATION - EDIT THESE SECTIONS
# =============================================================================

"""
This module provides convenient access to
`SNT's [MODULE_NAME] classes <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/[PACKAGE_PATH]/package-summary.html>`__.

Replace [MODULE_NAME] and [PACKAGE_PATH] with your module information.
Examples:
- MODULE_NAME: "morphology analysis", "tracing algorithm", "utility"
- PACKAGE_PATH: "analysis/morphology", "tracing", "util"
"""

import logging
import scyjava
from typing import Dict, Any, List

from ..common_module import setup_module_classes  # Adjust import path as needed

logger = logging.getLogger(__name__)

# =============================================================================
# CLASS LISTS - EDIT THESE FOR YOUR MODULE
# =============================================================================

# Curated classes - always available for direct import
# These are the most commonly used classes that users will import directly
CURATED_CLASSES = [
    # Add your most important classes here
    # Example: "MorphologyAnalyzer", "ShapeMetrics", "BranchAnalyzer"
]

# Extended classes - available via get_class() after discovery
# These are less commonly used classes that are loaded on-demand
EXTENDED_CLASSES = [
    # Add your extended classes here
    # Example: "AdvancedMorphology", "DetailedMetrics", "InternalUtils"
]

# =============================================================================
# MODULE SETUP - USUALLY NO CHANGES NEEDED
# =============================================================================

# Setup common module functionality
_module_funcs = setup_module_classes(
    package_name="sc.fiji.snt.[PACKAGE_PATH]",  # Edit this: e.g., "sc.fiji.snt.analysis.morphology"
    curated_classes=CURATED_CLASSES,
    extended_classes=EXTENDED_CLASSES,
    globals_dict=globals(),
    # Optional parameters (uncomment and modify if needed):
    # discovery_packages=["sc.fiji.snt", "sc.fiji.snt.util"],  # Search multiple packages
    # include_interfaces=True,  # Include Java interfaces (useful for tracing modules)
)

# Import functions into module namespace
get_available_classes = _module_funcs['get_available_classes']
get_class = _module_funcs['get_class']
list_classes = _module_funcs['list_classes']
get_curated_classes = _module_funcs['get_curated_classes']
get_extended_classes = _module_funcs['get_extended_classes']

# Create module-level __getattr__ and __dir__
__getattr__ = _module_funcs['create_getattr']('pysnt.[MODULE_PATH]')  # Edit this: e.g., 'pysnt.analysis.morphology'
__dir__ = _module_funcs['create_dir']()

# =============================================================================
# MODULE EXPORTS - EDIT IF YOU HAVE SUBMODULES
# =============================================================================

# Static __all__ with curated classes always available
# This ensures IDEs know these symbols are available for import
__all__ = [
    # Functions (standard for all modules)
    "get_available_classes",
    "get_class", 
    "list_classes",
    "get_curated_classes",
    "get_extended_classes",
    # Constants (standard for all modules)
    "CURATED_CLASSES",
    "EXTENDED_CLASSES",
    # Curated classes (will be populated by placeholder generation)
    # The placeholder generation script will automatically add your curated classes here
] + CURATED_CLASSES

# =============================================================================
# SUBMODULE IMPORTS - ADD IF YOUR MODULE HAS SUBMODULES
# =============================================================================

# Uncomment and modify if your module has submodules:
# from . import submodule1, submodule2
# 
# # Update __getattr__ to handle submodules:
# __getattr__ = _module_funcs['create_getattr']('pysnt.[MODULE_PATH]', submodules=['submodule1', 'submodule2'])

# =============================================================================
# TEMPLATE CHECKLIST
# =============================================================================

"""
Before using this template, make sure to:

□ Update the module docstring with correct MODULE_NAME and PACKAGE_PATH
□ Set the correct package_name in setup_module_classes()
□ Add your classes to CURATED_CLASSES and EXTENDED_CLASSES
□ Update the __getattr__ module path
□ Add submodule imports if needed
□ Remove this checklist section
□ Run `python scripts/generate_placeholders.py` to generate placeholder classes
□ Test with `python -c "import src.pysnt.your_module; print('Success!')"`

Example completed configuration for morphology analysis:

```python
# Module docstring
\"\"\"
This module provides convenient access to
`SNT's morphology analysis classes <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/analysis/morphology/package-summary.html>`__.
\"\"\"

# Class lists
CURATED_CLASSES = [
    "MorphologyAnalyzer", "ShapeMetrics", "BranchAnalyzer"
]

EXTENDED_CLASSES = [
    "AdvancedMorphology", "DetailedMetrics", "InternalUtils"
]

# Setup
_module_funcs = setup_module_classes(
    package_name="sc.fiji.snt.analysis.morphology",
    curated_classes=CURATED_CLASSES,
    extended_classes=EXTENDED_CLASSES,
    globals_dict=globals(),
)

# Module path
__getattr__ = _module_funcs['create_getattr']('pysnt.analysis.morphology')
```
"""