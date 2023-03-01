"""Functions to load data into PostgreSQL database."""

import logging

from sqlalchemy import Engine

from app.utils.db_helpers import truncate_tables
from app.utils.type_annotations import DataFrameMap

LOGGER = logging.getLogger(__name__)


def load_data_to_postgres(engine: Engine, dfs: DataFrameMap) -> None:
    """Loads data from Dataframes to PostgreSQL database.

    Args:
        engine: SQLAlchemy engine to connect to PostgreSQL database.
        dfs: Dictionary with file name as key and DataFrame as value.
    """
    ordered_data = _order_tables(dfs)
    table_names = list(ordered_data.keys())

    truncate_tables(engine, table_names)
    _insert_to_table(engine, ordered_data)

    LOGGER.info("Data loaded to PostgreSQL database.")


def _order_tables(dfs: DataFrameMap) -> DataFrameMap:
    """Orders tables in correct order to avoid FK dependency errors.

    Args:
        dfs: Dictionary with file name as key and DataFrame as value.

    Returns:
        Ordered dictionary with table name as key and DataFrame as value.
    """
    return {
        "movie": dfs["movie"],
        "actor": dfs["actor_table"],
        "movie_cast": dfs["movie_cast"],
        "director": dfs["director"],
        "movie_direction": dfs["movie_direction"],
        "genres": dfs["genres"],
        "movie_genres": dfs["movie_genres"],
        "reviewer": dfs["reviewer"],
        "rating": dfs["rating"],
    }


def _insert_to_table(engine: Engine, table_data: DataFrameMap) -> None:
    """Inserts data from Dataframes to PostgreSQL database.

    Args:
        engine: SQLAlchemy engine to connect to PostgreSQL database.
        table_data: Dictionary with table name as key and DataFrame as value.
    """
    for table_name, df in table_data.items():
        df.to_sql(table_name, engine, if_exists="append", index=False)
        LOGGER.info(f"Inserted {len(df)} rows into {table_name} table.")
