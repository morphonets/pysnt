"""
Image format utilities for pysnt.

This module provides functions for loading various image formats for use with SNT.
Supports both bioformats2raw and OME-NGFF layouts.
"""

import logging
from pathlib import Path
from typing import Union, Optional, Tuple

logger = logging.getLogger(__name__)

# Layout constants
LAYOUT_BIOFORMATS2RAW = "bioformats2raw"
LAYOUT_OME_NGFF = "ome-ngff"
LAYOUT_UNKNOWN = "unknown"


def detect_zarr_layout(path: Union[str, Path]) -> str:
    """
    Detect the OME-ZARR layout type.

    Parameters
    ----------
    path : str or Path
        Path or URL to the OME-ZARR directory

    Returns
    -------
    str
        Layout type: 'bioformats2raw', 'ome-ngff', or 'unknown'

    Examples
    --------
    >>> from pysnt.io import detect_zarr_layout
    >>> layout = detect_zarr_layout('/path/to/image.ome.zarr')
    >>> print(layout)  # 'bioformats2raw' or 'ome-ngff'
    """
    import zarr

    path_str = str(path)

    # Handle file:// URLs
    if path_str.startswith('file://'):
        path_str = path_str[7:]

    try:
        z = zarr.open(path_str)

        # Check root attributes
        root_attrs = dict(z.attrs) if hasattr(z, 'attrs') else {}

        # bioformats2raw explicitly declares its layout
        if 'bioformats2raw.layout' in root_attrs:
            return LAYOUT_BIOFORMATS2RAW

        # OME-NGFF has multiscales at root
        if 'multiscales' in root_attrs:
            return LAYOUT_OME_NGFF

        # Check for /0 group with multiscales (bioformats2raw structure)
        if '0' in z:
            series_attrs = dict(z['0'].attrs) if hasattr(z['0'], 'attrs') else {}
            if 'multiscales' in series_attrs:
                return LAYOUT_BIOFORMATS2RAW

        return LAYOUT_UNKNOWN

    except Exception as e:
        logger.warning(f"Failed to detect layout: {e}")
        return LAYOUT_UNKNOWN


def get_dataset_path(layout: str, level: int, series: int = 0) -> str:
    """
    Get the N5/Zarr dataset path for a given layout and level (standard layouts only).

    For non-standard layouts, use get_dataset_path_from_metadata() instead.

    Parameters
    ----------
    layout : str
        Layout type ('bioformats2raw' or 'ome-ngff')
    level : int
        Resolution level (0 = full resolution)
    series : int, optional
        Series index for multi-series datasets. Default: 0

    Returns
    -------
    str
        Dataset path string (e.g., '/0/0' for bioformats2raw or '/0' for ome-ngff)
    """
    if layout == LAYOUT_BIOFORMATS2RAW:
        return f"/{series}/{level}"
    else:
        # OME-NGFF: levels at root
        return f"/{level}"


def get_dataset_path_from_metadata(path: Union[str, Path], level: int = 0, series: int = 0) -> Tuple[str, dict]:
    """
    Get the actual dataset path by reading OME-ZARR metadata.

    This handles non-standard layouts where dataset paths are not simply '0', '1', etc.

    Parameters
    ----------
    path : str or Path
        Path or URL to the OME-ZARR directory
    level : int, optional
        Resolution level (0 = full resolution). Default: 0
    series : int, optional
        Series index for multi-series datasets. Default: 0

    Returns
    -------
    tuple
        (dataset_path, scale_info) where:
        - dataset_path: the actual path to the dataset (e.g., '/scale0/marmoset_neurons')
        - scale_info: dict with 'scale' and 'translation' arrays, or None

    Raises
    ------
    ValueError
        If metadata cannot be read or level is out of range
    """
    import zarr

    path_str = str(path)
    if path_str.startswith('file://'):
        path_str = path_str[7:]

    z = zarr.open(path_str)
    layout = detect_zarr_layout(path_str)

    # Get multiscales metadata based on layout
    multiscales = None
    if layout == LAYOUT_BIOFORMATS2RAW:
        if str(series) in z and 'multiscales' in z[str(series)].attrs:
            multiscales = z[str(series)].attrs['multiscales']
    else:
        # OME-NGFF or unknown - check root
        root_attrs = dict(z.attrs) if hasattr(z, 'attrs') else {}
        multiscales = root_attrs.get('multiscales')
        # Also check for ome.multiscales (v0.5 style)
        if not multiscales and 'ome' in root_attrs:
            multiscales = root_attrs['ome'].get('multiscales')

    if not multiscales or len(multiscales) == 0:
        raise ValueError(f"No multiscales metadata found in {path_str}")

    # Get datasets array
    ms = multiscales[0]
    datasets = ms.get('datasets', [])

    if level >= len(datasets):
        raise ValueError(f"Level {level} out of range. Available levels: 0-{len(datasets) - 1}")

    # Get the actual path from metadata
    ds = datasets[level]
    ds_path = ds.get('path', str(level))

    # Ensure path starts with /
    if not ds_path.startswith('/'):
        ds_path = '/' + ds_path

    # For bioformats2raw, prepend series
    if layout == LAYOUT_BIOFORMATS2RAW:
        ds_path = f"/{series}{ds_path}"

    # Extract scale info from coordinateTransformations
    scale_info = None
    transforms = ds.get('coordinateTransformations', [])
    for t in transforms:
        if t.get('type') == 'scale':
            scale_info = {'scale': t.get('scale')}
            break

    # Also get translation if present
    if scale_info:
        for t in transforms:
            if t.get('type') == 'translation':
                scale_info['translation'] = t.get('translation')
                break

    return ds_path, scale_info


def get_zattrs_path(layout: str, zarr_path: str, series: int = 0) -> str:
    """
    Get the path to .zattrs containing multiscales metadata.

    Parameters
    ----------
    layout : str
        Layout type ('bioformats2raw' or 'ome-ngff')
    zarr_path : str
        Root zarr path
    series : int, optional
        Series index for multi-series datasets. Default: 0

    Returns
    -------
    str
        Path to .zattrs file
    """
    if zarr_path.endswith('/'):
        zarr_path = zarr_path[:-1]

    if layout == LAYOUT_BIOFORMATS2RAW:
        return f"{zarr_path}/{series}/.zattrs"
    else:
        # OME-NGFF: metadata at root
        return f"{zarr_path}/.zattrs"


def get_available_levels(path: Union[str, Path], series: int = 0) -> list:
    """
    Get available resolution levels in an OME-ZARR dataset.

    Parameters
    ----------
    path : str or Path
        Path or URL to the OME-ZARR directory
    series : int, optional
        Series index for multi-series datasets. Default: 0

    Returns
    -------
    list
        List of available level indices with their dimensions

    Examples
    --------
    >>> from pysnt.io import get_available_levels
    >>> levels = get_available_levels('/path/to/image.ome.zarr')
    >>> for level in levels:
    ...     print(f"Level {level['level']}: {level['shape']}")
    """
    import zarr

    path_str = str(path)
    if path_str.startswith('file://'):
        path_str = path_str[7:]

    layout = detect_zarr_layout(path_str)
    z = zarr.open(path_str)

    levels = []

    # Get the group containing resolution levels
    if layout == LAYOUT_BIOFORMATS2RAW:
        if str(series) in z:
            level_group = z[str(series)]
            attrs_source = level_group
        else:
            logger.warning(f"Series {series} not found")
            return levels
    else:
        level_group = z
        attrs_source = z

    # Get multiscales metadata - check both standard and ome.multiscales (v0.5)
    multiscales = None
    if 'multiscales' in attrs_source.attrs:
        multiscales = attrs_source.attrs['multiscales']
    elif 'ome' in attrs_source.attrs and 'multiscales' in attrs_source.attrs['ome']:
        multiscales = attrs_source.attrs['ome']['multiscales']

    if multiscales:
        ms = multiscales[0]
        datasets = ms.get('datasets', [])

        for level_idx, ds in enumerate(datasets):
            level_path = ds.get('path', str(level_idx))

            # Navigate to the array - handle nested paths like 'scale0/marmoset_neurons'
            try:
                arr = level_group
                for part in level_path.split('/'):
                    if part and part in arr:
                        arr = arr[part]

                # Check if we got an actual array
                if not hasattr(arr, 'shape'):
                    continue

                # Get scale info from coordinateTransformations
                scale = None
                for t in ds.get('coordinateTransformations', []):
                    if t.get('type') == 'scale':
                        scale = t.get('scale')
                        break

                levels.append({
                    'level': level_idx,
                    'path': level_path,
                    'shape': arr.shape,
                    'dtype': str(arr.dtype),
                    'scale': scale
                })
            except (KeyError, AttributeError) as e:
                logger.debug(f"Could not access level {level_idx} at path {level_path}: {e}")
                continue

    levels.sort(key=lambda x: x['level'])
    return levels


def imgplus_from_zarr(path: Union[str, Path], level: int = 0, series: int = 0):
    """
    Load an OME-ZARR image as a calibrated ImgPlus from local or remote sources.
    Supports both bioformats2raw and OME-NGFF layouts.

    Parameters
    ----------
    path : str or Path
        Path or URL to the OME-ZARR directory. Supports:
        - Local paths: '/path/to/image.ome.zarr'
        - HTTP/HTTPS URLs: 'https://example.com/data/image.ome.zarr'
        - S3 URLs: 's3://bucket-name/path/to/image.ome.zarr'
    level : int, optional
        Resolution level to load (0 = full resolution). Default: 0
    series : int, optional
        Series index for multi-series datasets (bioformats2raw). Default: 0

    Returns
    -------
    ImgPlus
        Calibrated ImgPlus with axis metadata from OME-ZARR

    Raises
    ------
    FileNotFoundError
        If the zarr path does not exist (local paths only)
    ValueError
        If the zarr lacks valid OME metadata or requested level
    ImportError
        If required dependencies are not available

    Examples
    --------
    >>> from pysnt.io import imgplus_from_zarr
    >>>
    >>> # Local file (full resolution)
    >>> img = imgplus_from_zarr('/path/to/image.ome.zarr')
    >>>
    >>> # Load downsampled level
    >>> img = imgplus_from_zarr('/path/to/image.ome.zarr', level=2)
    >>>
    >>> # Multi-series dataset (bioformats2raw)
    >>> img = imgplus_from_zarr('/path/to/image.ome.zarr', series=1)
    >>>
    >>> # HTTP URL
    >>> img = imgplus_from_zarr('https://example.com/data/image.ome.zarr')
    >>>
    >>> # S3 URL (requires s3fs)
    >>> img = imgplus_from_zarr('s3://my-bucket/data/image.ome.zarr')

    Notes
    -----
    For S3 access, you may need to configure AWS credentials.

    The function automatically detects the layout type (bioformats2raw vs OME-NGFF)
    and reads calibration metadata from the appropriate location.
    """
    # Check if pysnt is initialized
    from .. import core
    if not core.is_initialized():
        raise RuntimeError(
            "PySNT not initialized. Call pysnt.initialize() before using imgplus_from_zarr()."
        )

    # Import ImageJ classes (only available after JVM startup)
    try:
        import scyjava
        ImgPlus = scyjava.jimport("net.imagej.ImgPlus")
        Axes = scyjava.jimport("net.imagej.axis.Axes")
        DefaultLinearAxis = scyjava.jimport("net.imagej.axis.DefaultLinearAxis")
    except Exception as e:
        raise ImportError(
            "ImageJ classes not available. Make sure pysnt.initialize() was called and completed successfully."
        ) from e

    # Determine if path is local or remote
    path_str = str(path)
    is_remote = path_str.startswith(('http://', 'https://', 's3://'))

    # Try N5 readers first for all URLs (local, S3, HTTP) - much faster when available
    try:
        return _imgplus_from_zarr_n5(path_str, level, series)
    except Exception as n5_error:
        logger.warning(f"N5 readers failed: {n5_error}, falling back to Python zarr")
        raise


def _imgplus_from_zarr_n5(path_str: str, level: int = 0, series: int = 0):
    """
    Load OME-ZARR using N5Factory - unified approach for all protocols (local, S3, HTTP).
    Supports both bioformats2raw and OME-NGFF layouts, including non-standard dataset paths.
    """
    import scyjava

    # Import N5 classes
    N5Utils = scyjava.jimport("org.janelia.saalfeldlab.n5.imglib2.N5Utils")
    ImgPlus = scyjava.jimport("net.imagej.ImgPlus")
    ImgView = scyjava.jimport("net.imglib2.img.ImgView")

    logger.info(f"Loading OME-ZARR: {path_str}, level={level}, series={series}")

    # Store original path for metadata lookup
    original_path = path_str

    n5_reader = None

    try:
        # Get the actual dataset path from metadata BEFORE modifying path_str
        try:
            dataset_path, scale_info = get_dataset_path_from_metadata(original_path, level, series)
            logger.debug(f"Dataset path from metadata: {dataset_path}")
            if scale_info:
                logger.debug(f"Scale info: {scale_info}")
        except Exception as meta_error:
            logger.warning(f"Could not read metadata paths: {meta_error}, falling back to standard layout")
            layout = detect_zarr_layout(original_path)
            dataset_path = get_dataset_path(layout, level, series)
            scale_info = None

        # Ensure proper URL format for N5Factory
        if not path_str.startswith(('s3://', 'http://', 'https://', 'file://')):
            # Local path - add file:// prefix
            from pathlib import Path
            abs_path = Path(path_str).resolve()
            path_str = f"file://{abs_path}"
            logger.debug(f"Converted to file URL: {path_str}")

        # Try N5Factory from n5-universe first (best S3 + OME-ZARR support)
        try:
            N5Factory = scyjava.jimport("org.janelia.saalfeldlab.n5.universe.N5Factory")
            factory = N5Factory()
            n5_reader = factory.openReader(path_str)
            logger.debug("✔ n5-universe N5Factory reader created")

        except Exception as universe_error:
            logger.debug(f"n5-universe N5Factory failed: {universe_error}")

            # Fallback to standard N5Factory
            try:
                N5Factory = scyjava.jimport("org.janelia.saalfeldlab.n5.N5Factory")
                factory = N5Factory()
                n5_reader = factory.openReader(path_str)
                logger.debug("✔ Standard N5Factory reader created")

            except Exception as standard_error:
                logger.debug(f"Standard N5Factory failed: {standard_error}")

                # Final fallback to N5ZarrReader for local files only
                if path_str.startswith('file://'):
                    try:
                        local_path = path_str[7:]  # Remove 'file://' prefix
                        N5ZarrReader = scyjava.jimport("org.janelia.saalfeldlab.n5.zarr.N5ZarrReader")
                        n5_reader = N5ZarrReader(local_path)
                        logger.debug("✔ N5ZarrReader fallback created")
                    except Exception as zarr_error:
                        logger.debug(f"N5ZarrReader fallback failed: {zarr_error}")
                        raise ValueError(f"All N5 readers failed: {zarr_error}")
                else:
                    raise ValueError(f"Failed to open remote OME-ZARR with N5Factory: {standard_error}")

        if n5_reader is None:
            raise ValueError("Failed to create any N5 reader")

        # Check if the dataset exists
        attrs = n5_reader.getDatasetAttributes(dataset_path)
        if attrs is None:
            raise ValueError(f"Dataset level {level} not found at path {dataset_path}")

        logger.debug(f"Dataset found: {dataset_path}")
        logger.debug(f"  Dimensions: {list(attrs.getDimensions())}")
        logger.debug(f"  Data type: {attrs.getDataType()}")

        # Read the image data
        img_data = N5Utils.open(n5_reader, dataset_path)
        logger.debug(f"Image data loaded: {type(img_data)}")

        # Wrap as Img and create ImgPlus
        img_view = ImgView.wrap(img_data)
        img = ImgPlus(img_view)

        # Adjust axes with level-specific calibration
        OmeAxisUtils = scyjava.jimport("sc.fiji.snt.io.OmeAxisUtils")
        OmeAxisUtils.setAxesFromZarr(img, path_str, level, series)

        # Set name
        from pathlib import Path
        if path_str.startswith(('s3://', 'http://', 'https://')):
            # For remote URLs, extract a reasonable name
            name = Path(path_str).stem or "remote_zarr"
        else:
            # For local files (including file:// URLs)
            local_path = path_str[7:] if path_str.startswith('file://') else path_str
            name = Path(local_path).stem

        # Append level info if not level 0
        if level > 0:
            name = f"{name}_level{level}"
        img.setName(name)

        logger.info(f"Successfully loaded OME-ZARR: {img}")

        return img

    finally:
        if n5_reader is not None:
            try:
                n5_reader.close()
            except Exception as close_error:
                logger.debug(f"Error closing N5 reader: {close_error}")


def inspect_zarr(path: Union[str, Path], max_depth: int = 3) -> dict:
    """
    Inspect the structure and contents of an OME-ZARR file.

    This function provides detailed information about the zarr structure,
    including groups, datasets, dimensions, data types, and OME metadata.

    Parameters
    ----------
    path : str or Path
        Path or URL to the OME-ZARR directory
    max_depth : int, optional
        Maximum depth for recursive exploration. Default: 3

    Returns
    -------
    dict
        Dictionary containing zarr structure information including:
        - 'layout': detected layout type
        - 'resolution_levels': list of available levels with dimensions
        - 'axes': axis information from metadata
        - 'structure': hierarchical structure of the zarr

    Examples
    --------
    >>> from pysnt.io import inspect_zarr
    >>>
    >>> info = inspect_zarr('/path/to/image.ome.zarr')
    >>> print(f"Layout: {info['layout']}")
    >>> print(f"Levels: {len(info['resolution_levels'])}")
    >>> for level in info['resolution_levels']:
    ...     print(f"  Level {level['level']}: {level['shape']}")
    """
    import zarr

    path_str = str(path)
    if path_str.startswith('file://'):
        path_str = path_str[7:]

    z = zarr.open(path_str)

    # Detect layout
    layout = detect_zarr_layout(path_str)

    # Get root attributes
    root_attrs = dict(z.attrs) if hasattr(z, 'attrs') else {}

    # Get multiscales metadata location based on layout
    multiscales = None
    if layout == LAYOUT_OME_NGFF:
        multiscales = root_attrs.get('multiscales', [{}])[0] if 'multiscales' in root_attrs else None
    elif layout == LAYOUT_BIOFORMATS2RAW:
        if '0' in z and 'multiscales' in z['0'].attrs:
            multiscales = z['0'].attrs['multiscales'][0]

    # Extract axis info
    axes_info = []
    if multiscales and 'axes' in multiscales:
        for axis in multiscales['axes']:
            axes_info.append({
                'name': axis.get('name'),
                'type': axis.get('type'),
                'unit': axis.get('unit')
            })

    # Get resolution levels
    resolution_levels = get_available_levels(path_str)

    # Build structure tree
    def build_tree(group, current_depth=0):
        if current_depth >= max_depth:
            return {'type': 'max_depth'}

        result = {'type': 'group', 'attrs': dict(group.attrs) if hasattr(group, 'attrs') else {}}
        children = {}

        for key in group.keys():
            item = group[key]
            if hasattr(item, 'shape'):
                children[key] = {
                    'type': 'array',
                    'shape': item.shape,
                    'dtype': str(item.dtype),
                    'chunks': item.chunks if hasattr(item, 'chunks') else None
                }
            elif hasattr(item, 'keys'):
                children[key] = build_tree(item, current_depth + 1)

        result['children'] = children
        return result

    structure = build_tree(z)

    return {
        'path': path_str,
        'layout': layout,
        'root_attrs': root_attrs,
        'axes': axes_info,
        'resolution_levels': resolution_levels,
        'structure': structure,
        'summary': {
            'num_levels': len(resolution_levels),
            'num_series': len([k for k in z.keys() if k.isdigit()]) if layout == LAYOUT_BIOFORMATS2RAW else 1,
            'has_ome_xml': 'OME' in z if hasattr(z, 'keys') else False
        }
    }


def _inspect_zarr_n5(path_str: str, max_depth: int = 3) -> dict:
    """
    Inspect OME-ZARR using N5 readers for detailed structure analysis.

    Deprecated: Use inspect_zarr() which now uses Python zarr directly.
    """
    return inspect_zarr(path_str, max_depth)