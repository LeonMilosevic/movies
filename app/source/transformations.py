"""File will contain transformations functions for data."""

import logging
from typing import Callable

from pandas import to_datetime, to_numeric

from app.utils.mapping import date_columns_map, numeric_columns_map, pk_columns_map
from app.utils.type_annotations import ColumnTypeMap, DataFrameMap
from app.utils.validations import validate_pk

LOGGER = logging.getLogger(__name__)


def apply_transformations(dfs: DataFrameMap) -> DataFrameMap:
    """Apply transformations to dataframes and returns a list of dataframes.

    Args:
        dfs: Dictionary with file name as key and DataFrame as value.

    Returns:
        List of DataFrames.
    """
    _convert_columns(dfs=dfs, columns=numeric_columns_map, convert_fn=to_numeric, errors="coerce")
    _convert_columns(
        dfs=dfs,
        columns=date_columns_map,
        convert_fn=to_datetime,
        errors="coerce",
        format="%Y-%m-%d",
    )
    validate_pk(dfs, pk_columns_map)
    LOGGER.info("Transformations applied successfully.")
    return dfs


def _convert_columns(
    dfs: DataFrameMap, columns: ColumnTypeMap, convert_fn: Callable, **kwargs
) -> None:
    """Convert columns to specified type in place.

    Args:
        dfs: Dictionary with file name as key and DataFrame as value.
        columns: Dictionary with file name as key and list of column names as value.
        convert_fn: Function to convert columns.
        **kwargs: Keyword arguments to pass to convert_fn.
    """
    for df_name, df in dfs.items():
        if df_name in columns:
            columns_to_convert = columns[df_name]
            df[columns_to_convert] = df[columns_to_convert].apply(convert_fn, **kwargs)
