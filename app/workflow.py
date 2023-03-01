"""This file contains the workflow of the project,
ETL to import movies data to PostgreSQL database"""

from sqlalchemy import Engine, create_engine

from app.models.load_models import load_models
from app.source.get_data import get_data
from app.source.transformations import apply_transformations
from app.source.upload_data import load_data_to_postgres
from app.utils.mapping import files
from app.utils.secrets import db_secrets
from app.utils.type_annotations import Json


def run_etl(engine: Engine) -> None:
    """Imports data from csv files to PostgreSQL database."""
    movies_data = get_data("source/data", files)
    movies_data = apply_transformations(movies_data)
    load_data_to_postgres(engine, movies_data)


if __name__ == "__main__":
    secrets: Json = db_secrets
    sql_engine = create_engine(
        f"postgresql://"
        f"{secrets['username']}:"
        f"{secrets['password']}"
        f"@{secrets['host']}"
        f":{secrets['port']}/{secrets['database']}"
    )
    run_etl(sql_engine)
    load_models(sql_engine)
