"""File will get movies data."""

import logging
from typing import Dict

from pandas import DataFrame, read_csv

from app.utils.type_annotations import FileName, MovieFiles

LOGGER = logging.getLogger(__name__)


def get_data(data_path: str, files: MovieFiles) -> Dict[FileName, DataFrame]:
    """Get Data from csv files.

    Args:
        data_path: Path to data folder.
        files: Dictionary with file name as key and list of column names as value.

    Returns:
        List of DataFrames containing data from csv files.
    """
    LOGGER.info("Reading data from csv files.")
    return {
        file_name: read_csv(
            f"{data_path}/{file_name}.csv",
            header=None,
            names=column_names,
        )
        for file_name, column_names in files.items()
    }
