"""Functions to load models into PostgreSQL database."""

from sqlalchemy import Engine

from app.models.queries import execute_queries


def load_models(engine: Engine) -> None:
    """Loads models from PostgreSQL source tables to models.

    Args:
        engine: SQLAlchemy engine to connect to PostgreSQL database.
    """
    execute_queries(engine)
