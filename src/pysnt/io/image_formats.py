"""
Image format utilities for pysnt.

This module provides functions for loading various image formats for use with SNT.
"""

import logging
from pathlib import Path
from typing import Union

logger = logging.getLogger(__name__)


def _open_remote_zarr(url: str):
    """
    Open a remote zarr store using fsspec.
    
    Parameters
    ----------
    url : str
        Remote URL (http://, https://, or s3://)
        
    Returns
    -------
    zarr.Group
        Opened zarr store
        
    Raises
    ------
    ImportError
        If required dependencies for remote access are not available
    """
    try:
        import fsspec
    except ImportError as e:
        raise ImportError(
            f"fsspec is required for remote zarr access: {e}. "
            "Install with: pip install fsspec"
        ) from e
    
    # Handle S3 URLs
    if url.startswith('s3://'):
        try:
            import s3fs  # noqa
        except ImportError as e:
            raise ImportError(
                f"s3fs is required for S3 access: {e}. "
                "Install with: pip install s3fs"
            ) from e
        
        logger.debug(f"Opening S3 zarr store: {url}")
        # Use fsspec to create a filesystem mapper
        mapper = fsspec.get_mapper(url)
    else:
        # HTTP/HTTPS URLs
        logger.debug(f"Opening HTTP zarr store: {url}")
        mapper = fsspec.get_mapper(url)
    
    # Open zarr store using the mapper
    import zarr
    return zarr.open(mapper, mode='r')


def imgplus_from_zarr(path: Union[str, Path], level: int = 0):
    """
    Load an OME-ZARR image as a calibrated ImgPlus from local or remote sources.
    Spatial calibration and axis metadata from the OME-ZARR multiscales specification
    is preserved.
    
    Parameters
    ----------
    path : str or Path
        Path or URL to the OME-ZARR directory. Supports:
        - Local paths: '/path/to/image.ome.zarr'
        - HTTP/HTTPS URLs: 'https://example.com/data/image.ome.zarr'
        - S3 URLs: 's3://bucket-name/path/to/image.ome.zarr'
    level : int, optional
        Resolution level to load (0 = full resolution). Default: 0
        
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
    >>> # Local file
    >>> img = imgplus_from_zarr('/path/to/image.ome.zarr')
    >>> 
    >>> # HTTP URL
    >>> img = imgplus_from_zarr('https://example.com/data/image.ome.zarr')
    >>> 
    >>> # S3 URL (requires s3fs)
    >>> img = imgplus_from_zarr('s3://my-bucket/data/image.ome.zarr')
    >>> 
    >>> # Load downsampled level
    >>> img = imgplus_from_zarr('/path/to/image.ome.zarr', level=2)
    
    Notes
    -----
    This function requires the following dependencies:
    - zarr: For reading OME-ZARR files
    - imglyb: For converting numpy arrays to ImageJ ImgPlus
    - fsspec: For remote file access (HTTP/HTTPS/S3)
    - s3fs: For S3 access (optional, only needed for s3:// URLs)
    
    For S3 access, you may need to configure AWS credentials via:
    - AWS CLI: `aws configure`
    - Environment variables: AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY
    - IAM roles (when running on AWS)
    """
    try:
        import zarr
        import imglyb
    except ImportError as e:
        raise ImportError(
            f"Required dependency not found: {e}. "
            "Install with: pip install zarr imglyb"
        ) from e
    
    # Import ImageJ classes
    try:
        from net.imagej import ImgPlus
        from net.imagej.axis import Axes, DefaultLinearAxis
    except ImportError as e:
        raise ImportError(
            "ImageJ classes not available. Make sure pysnt.initialize() was called."
        ) from e
    
    # Determine if path is local or remote
    path_str = str(path)
    is_remote = path_str.startswith(('http://', 'https://', 's3://'))
    
    if is_remote:
        logger.info(f"Loading OME-ZARR from remote source: {path_str}, level {level}")
        store = _open_remote_zarr(path_str)
    else:
        # Local path handling
        path = Path(path)
        if not path.exists():
            raise FileNotFoundError(f"Zarr not found: {path}")
        
        logger.info(f"Loading OME-ZARR from local path: {path}, level {level}")
        store = zarr.open(str(path), mode='r')
    
    # Parse OME-ZARR multiscales metadata
    multiscales = store.attrs.get('multiscales', None)
    if not multiscales or len(multiscales) == 0:
        raise ValueError(f"No valid OME-ZARR multiscales metadata in {path}")
    
    ms = multiscales[0]
    datasets = ms.get('datasets', [])
    
    if level >= len(datasets):
        raise ValueError(f"Level {level} not found. Available levels: 0-{len(datasets)-1}")
    
    # Load array for requested level
    dataset_path = datasets[level].get('path', str(level))
    logger.debug(f"Loading dataset: {dataset_path}")
    
    arr = store[dataset_path][:]
    logger.info(f"Loaded array shape: {arr.shape}, dtype: {arr.dtype}")
    
    # Extract scales from coordinateTransformations
    transforms = datasets[level].get('coordinateTransformations', [])
    scales = [1.0] * arr.ndim
    
    for t in transforms:
        if t.get('type') == 'scale':
            scales = t.get('scale', scales)
            break
    
    logger.debug(f"Pixel scales: {scales}")
    
    # Parse axis metadata (OME-ZARR v0.4+)
    axes_meta = ms.get('axes', [])
    axis_map = {
        'x': Axes.X, 
        'y': Axes.Y, 
        'z': Axes.Z, 
        'c': Axes.CHANNEL, 
        't': Axes.TIME
    }
    
    # Create ImgPlus
    rai = imglyb.to_imglib(arr)
    img = ImgPlus(rai, path.stem)
    
    # Assign calibrated axes
    # OME-ZARR axes are ordered slowest-to-fastest (e.g., TCZYX)
    # imglib2/numpy are also in this order after imglyb conversion
    for i, ax_info in enumerate(axes_meta):
        ax_name = ax_info.get('name', '').lower()
        ax_unit = ax_info.get('unit', 'pixel') or 'pixel'
        ax_type = axis_map.get(ax_name, Axes.unknown())
        ax_scale = scales[i] if i < len(scales) else 1.0
        
        logger.debug(f"Axis {i}: {ax_name} ({ax_type}), scale={ax_scale}, unit={ax_unit}")
        img.setAxis(DefaultLinearAxis(ax_type, ax_unit, ax_scale), i)
    
    logger.info(f"Successfully created ImgPlus: {img}")
    return img


# Additional image format loaders could be added here in the future
#
# def imgplus_from_hdf5(path, dataset_path):
#     """Load HDF5 dataset as ImgPlus.""" 
#     pass