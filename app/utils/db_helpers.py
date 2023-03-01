"""Helper functions used to upload data."""

import logging
from typing import List

from sqlalchemy import Engine, text

LOGGER = logging.getLogger(__name__)


def truncate_tables(engine: Engine, table_names: List[str]) -> None:
    """Truncates all tables in PostgreSQL database.

    Args:
        engine: SQLAlchemy engine to connect to PostgreSQL database.
        table_names: List of table names to be truncated.
    """
    connection = engine.connect()
    for table_name in reversed(table_names):
        connection.execute(text(f"TRUNCATE {table_name} CASCADE;"))
        connection.commit()
    LOGGER.info("Truncated all tables.")
