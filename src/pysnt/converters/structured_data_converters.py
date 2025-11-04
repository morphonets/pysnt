"""
Structured data conversion logic for the converters module.

This module handles conversion of SNT structured (tabular-like) data objects
(SNTTable, Path, ImagePlus) to xarray datasets and metadata extraction, including:
- Structured data predicate functions for type detection
- Converter functions for tabular data (SNTTable)
- Path conversion functions for SNT Path coordinate sequences
- ImagePlus metadata extraction utilities

Dependencies: core.py
"""

from typing import Any

import xarray  # noqa

from .core import (
    logger,
    HAS_PANDAS,
    ERROR_MISSING_PANDAS,
    JavaTypeDetector,
    _create_converter_result,
    _create_error_result,
    _create_standard_error_message,
    pd,
    SNTObject,
)


def _is_snt_table(obj: Any) -> bool:
    """Check if object is an SNT Table."""
    try:
        return JavaTypeDetector.matches_pattern(
            obj,
            class_patterns=['SNTTable'],
            required_methods=['getColumnCount', 'getRowCount', 'getColumnHeader']
        )
    except (AttributeError, TypeError, RuntimeError) as e:
        logger.debug(f"SNTTable predicate: FAILED for {type(obj)} - {e}")
        return False


def _convert_snt_table(table: Any, **kwargs) -> SNTObject:
    """
    Convert SNT Table to a SNTObject containing a xarray Dataset.

    Parameters
    ----------
    table : SNT Table
        The table object to convert
    **kwargs
        Additional conversion options:
        - include_metadata: bool, whether to include table metadata (default: True)
        - column_names: list, custom column names (default: use table's column names)

    Returns
    -------
    dict
        Dictionary containing table information and xarray Dataset
    """

    try:
        # Check if pandas are available
        if not HAS_PANDAS:
            return _create_error_result(
                data_type=type(xarray.Dataset),
                error=ImportError(ERROR_MISSING_PANDAS),
                source_type='SNTTable'
            )

        # Get table dimensions
        try:
            row_count = table.getRowCount()
            col_count = table.getColumnCount()
            logger.info(f"Converting SNTTable with {row_count} rows and {col_count} columns")
        except Exception as e:
            logger.error(f"Failed to get table dimensions: {e}")
            return _create_error_result(type(xarray.Dataset), e, 'SNTTable')

        # Get column names
        column_names = kwargs.get('column_names', None)
        if column_names is None:
            try:
                column_names = []
                for col_idx in range(col_count):
                    col_name = table.getColumnHeader(col_idx)
                    if col_name is None or col_name == "":
                        col_name = f"Column_{col_idx}"
                    column_names.append(str(col_name))
            except Exception as e:
                # Fallback to generic column names
                column_names = [f"Column_{i}" for i in range(col_count)]
                logger.warning(f"Could not get column headers, using generic names: {e}")

        # Extract table data
        try:
            data_dict = {}
            for col_idx in range(col_count):
                col_name = column_names[col_idx]
                col_data = []

                # Extract data for this column
                for row_idx in range(row_count):
                    try:
                        cell_value = table.get(col_name, row_idx)
                        col_data.append(cell_value)

                    except Exception as cell_e:
                        logger.debug(f"Error getting cell value at ({row_idx}, {col_idx}): {cell_e}")
                        col_data.append(None)

                data_dict[col_name] = col_data

            # Convert to pandas DataFrame first (easier data type handling)
            df = pd.DataFrame(data_dict)

            # Convert to xarray Dataset
            import xarray as xr # noqa
            xr_dataset = xr.Dataset.from_dataframe(df)

            # Add row index as a coordinate
            xr_dataset = xr_dataset.assign_coords(index=range(row_count))

            # Prepare metadata
            metadata = {
                'row_count': row_count,
                'column_count': col_count,
                'column_names': column_names
            }
            
            # Get additional table metadata if available
            include_metadata = kwargs.get('include_metadata', True)
            if include_metadata:
                try:
                    metadata['title'] = table.getTitle()
                    # Add data types for each column
                    metadata['dtypes'] = {col: str(df[col].dtype) for col in df.columns}
                except Exception as e:
                    logger.debug(f"Could not extract table metadata: {e}")

            logger.info(f"Successfully converted SNTTable to xarray Dataset with shape {xr_dataset.dims}")
            return _create_converter_result(xr_dataset, 'SNTTable', **metadata)

        except Exception as e:
            logger.error(_create_standard_error_message("extract table data", e, "SNTTable"))
            return _create_error_result(type(xarray.Dataset), e, 'SNTTable')

    except Exception as e:
        logger.error(_create_standard_error_message("convert SNTTable", e, "SNTTable"))
        return _create_error_result(type(xarray.Dataset), e, 'SNTTable')


def _convert_path_to_xarray(path: Any):
    """Convert SNT Path object to xarray Dataset."""
    import xarray as xr # noqa
    import numpy as np # noqa

    # Collect all coordinates at once
    coords = [(node.x, node.y, node.z) for node in path.getNodes()]
    coords_array = np.array(coords)

    # Create xarray Dataset
    ds = xr.Dataset(
        {
            "x": (["node"], coords_array[:, 0]),
            "y": (["node"], coords_array[:, 1]),
            "z": (["node"], coords_array[:, 2]),
        },
        coords={"node": np.arange(len(coords))},
    )
    return ds


def _extract_imageplus_metadata(imageplus: Any, **kwargs) -> dict:
    """
    Extract metadata from an ImagePlus object without triggering conversion.
    
    This function extracts ImagePlus metadata including RGB type information and title
    for use in display functions.

    Parameters
    ----------
    imageplus : ImagePlus
        The ImagePlus object to extract metadata from
    **kwargs
        Additional options:
        - frame, t, time, timepoint : int, optional
            Frame/timepoint to display (default: 1). Parameter names are case-insensitive.

    Returns
    -------
    dict
        Dictionary containing ImagePlus metadata
    """
    try:
        logger.debug(f"Extracting ImagePlus metadata: {imageplus.getTitle()}")
        
        # Extract ImagePlus metadata
        image_type = imageplus.getType()
        image_title = imageplus.getTitle() or "Untitled Image"
        width = imageplus.getWidth()
        height = imageplus.getHeight()
        
        # Determine if this is an RGB image based on ImagePlus type
        # ImagePlus.COLOR_RGB = 4, ImagePlus.COLOR_256 = 1, ImagePlus.GRAY8 = 0, etc.
        is_rgb = image_type == 4  # ImagePlus.COLOR_RGB
        
        # Check if this is a binary image
        is_binary = False
        try:
            processor = imageplus.getProcessor()
            if processor is not None and hasattr(processor, 'isBinary'):
                is_binary = processor.isBinary()
                logger.debug(f"Binary detection: {is_binary}")
        except Exception as e:
            logger.debug(f"Could not check binary status: {e}")
            is_binary = False
        
        logger.debug(f"ImagePlus metadata: type={image_type}, title='{image_title}', "
                    f"size={width}x{height}, is_rgb={is_rgb}, is_binary={is_binary}")
        
        # Extract frame parameter (supports frame=, t=, time=, case-insensitive)
        kwargs_lower = {k.lower(): v for k, v in kwargs.items()}
        frame = None
        for key in ['frame', 't', 'time', 'timepoint']:
            if key in kwargs_lower:
                try:
                    frame = int(kwargs_lower[key])
                    break
                except (ValueError, TypeError):
                    pass
        frame = frame if frame is not None else 1
        
        # Return some useful metadata
        metadata = {
            'source_type': 'ImagePlus',
            'image_type': image_type,
            'image_title': image_title,
            'is_rgb': is_rgb,
            'is_binary': is_binary,
            'width': width,
            'height': height,
            'frame': frame
        }
        
        image_type_desc = 'RGB' if is_rgb else ('binary' if is_binary else 'grayscale')
        logger.debug(f"Extracted metadata for '{image_title}': {image_type_desc}")
        return metadata
        
    except Exception as e:
        logger.error(f"Failed to extract ImagePlus metadata: {e}")
        return {}
