"""File contains functions to validate data."""

import logging

from app.utils.type_annotations import ColumnTypeMap, DataFrameMap

LOGGER = logging.getLogger(__name__)


def validate_primary_keys(dfs: DataFrameMap, pk_fk_columns: ColumnTypeMap) -> None:
    """Validate primary keys by checking for null and duplicate values.

    Args:
        dfs: Dictionary with file name as key and DataFrame as value.
        pk_fk_columns: Dictionary with file name as key and list of column names as value.
    """
    for df_name, df in dfs.items():
        if df_name in pk_fk_columns:
            LOGGER.info(f"Validating primary and foreign keys for {df_name}")

            initial_count = df.shape[0]
            columns_to_check = pk_fk_columns[df_name]

            df.dropna(subset=columns_to_check, inplace=True)
            df.drop_duplicates(subset=columns_to_check, inplace=True)

            validated_count = df.shape[0]
            if validated_count != initial_count:
                LOGGER.warning(
                    f"Discrepancy in primary and foreign keys for {df_name}, "
                    f"initial count: {initial_count}, validated count: {validated_count}"
                )


def check_if_unexpected_date_range():
    pass
