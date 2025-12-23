"""
This module provides convenient access to
`SNT's io classes <https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/io/package-summary.html>`__.
"""

import logging
import scyjava
from typing import Dict, Any, List

from ..common_module import setup_module_classes  # Adjust import path as needed

logger = logging.getLogger(__name__)

# Curated classes - always available for direct import
# These are the most commonly used classes that users will import directly
CURATED_CLASSES = [
    "FlyCircuitLoader",
    "InsectBrainLoader",
    "MouseLightLoader",
    "MouseLightQuerier",
    "NeuroMorphoLoader",
    "RemoteSWCLoader",
    "WekaModelLoader",
]

# Extended classes - available via get_class() after discovery
# These are less commonly used classes that are loaded on-demand
EXTENDED_CLASSES = [
    "NDFImporter",
    "SWCExportException",
    "TracesFileFormatException",
]

# =============================================================================
# MODULE SETUP - USUALLY NO CHANGES NEEDED
# =============================================================================


# Placeholder classes for IDE support - will be replaced with Java classes
class FlyCircuitLoader:
    """
    Absurdly simple importer for retrieving SWC data from FlyCircuit.
    
    **All Methods and Attributes:** See `FlyCircuitLoader detailed documentation <../pysnt/io/flycircuitloader_doc.html>`_.
    """
    
    def __getattr__(self, name: str):
        """Dynamic attribute access for Java methods."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")
    
    def __init__(self, *args, **kwargs):
        """Placeholder constructor."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

class InsectBrainLoader:
    """
    Methods for retrieving reconstructions and annotations from the Insect Brain Database at insectbraindb.org *
    
    **All Methods and Attributes:** See `InsectBrainLoader detailed documentation <../pysnt/io/insectbrainloader_doc.html>`_.
    """
    
    def __getattr__(self, name: str):
        """Dynamic attribute access for Java methods."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")
    
    def __init__(self, *args, **kwargs):
        """Placeholder constructor."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

class MouseLightLoader:
    """
    Methods for retrieving reconstructions from MouseLight's online database at ml-neuronbrowser.janelia.org *
    
    **All Methods and Attributes:** See `MouseLightLoader detailed documentation <../pysnt/io/mouselightloader_doc.html>`_.
    """
    
    def __getattr__(self, name: str):
        """Dynamic attribute access for Java methods."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")
    
    def __init__(self, *args, **kwargs):
        """Placeholder constructor."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

class MouseLightQuerier:
    """
    Importer for retrieving reconstructions from MouseLight's online database at ml-neuronbrowser.janelia.org
    
    **All Methods and Attributes:** See `MouseLightQuerier detailed documentation <../pysnt/io/mouselightquerier_doc.html>`_.
    """
    
    def __getattr__(self, name: str):
        """Dynamic attribute access for Java methods."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")
    
    def __init__(self, *args, **kwargs):
        """Placeholder constructor."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

class NeuroMorphoLoader:
    """
    Importer for retrieving SWC data from neuromorpho.org.
    
    **All Methods and Attributes:** See `NeuroMorphoLoader detailed documentation <../pysnt/io/neuromorpholoader_doc.html>`_.
    """
    
    def __getattr__(self, name: str):
        """Dynamic attribute access for Java methods."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")
    
    def __init__(self, *args, **kwargs):
        """Placeholder constructor."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

class RemoteSWCLoader:
    """
    Importers downloading remote SWC files should extend this interface.
    
    **All Methods and Attributes:** See `RemoteSWCLoader detailed documentation <../pysnt/io/remoteswcloader_doc.html>`_.
    """
    
    def __getattr__(self, name: str):
        """Dynamic attribute access for Java methods."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")
    
    def __init__(self, *args, **kwargs):
        """Placeholder constructor."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

class WekaModelLoader:
    """
    GUI command for Loading pre-trained models from Labkit/TWS as secondary image layer.
    
    **All Methods and Attributes:** See `WekaModelLoader detailed documentation <../pysnt/io/wekamodelloader_doc.html>`_.
    """
    
    def __getattr__(self, name: str):
        """Dynamic attribute access for Java methods."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")
    
    def __init__(self, *args, **kwargs):
        """Placeholder constructor."""
        raise RuntimeError("SNT not initialized. Call pysnt.initialize() first.")

# Setup common module functionality
_module_funcs = setup_module_classes(
    package_name="sc.fiji.snt.io",
    curated_classes=CURATED_CLASSES,
    extended_classes=EXTENDED_CLASSES,
    globals_dict=globals(),
    include_interfaces=True,
)

# Import functions into module namespace
get_available_classes = _module_funcs["get_available_classes"]
get_class = _module_funcs["get_class"]
list_classes = _module_funcs["list_classes"]
get_curated_classes = _module_funcs["get_curated_classes"]
get_extended_classes = _module_funcs["get_extended_classes"]

# Create module-level __getattr__ and __dir__
__getattr__ = _module_funcs["create_getattr"]("pysnt.io")
__dir__ = _module_funcs["create_dir"]()

# Import image format utilities
from .images import (
    imgplus_from_zarr,
    inspect_zarr,
    detect_zarr_layout,
    get_available_levels,
    get_dataset_path,
    get_dataset_path_from_metadata,
    get_zattrs_path,
    # Layout constants
    LAYOUT_BIOFORMATS2RAW,
    LAYOUT_OME_NGFF,
    LAYOUT_UNKNOWN,
)

# Static __all__ with curated classes always available
# This ensures IDEs know these symbols are available for import
__all__ = [
    # Functions (standard for all modules)
    "get_available_classes",
    "get_class",
    "list_classes",
    "get_curated_classes",
    "get_extended_classes",
    # Image format utilities
    "detect_zarr_layout",
    "get_available_levels",
    "get_dataset_path",
    "get_dataset_path_from_metadata",
    "get_zattrs_path",
    "imgplus_from_zarr",
    "inspect_zarr",
    # Layout constants
    "LAYOUT_BIOFORMATS2RAW",
    "LAYOUT_OME_NGFF",
    "LAYOUT_UNKNOWN",
    # Constants (standard for all modules)
    "CURATED_CLASSES",
    "EXTENDED_CLASSES",
    # Curated classes (will be populated by placeholder generation)
] + CURATED_CLASSES
