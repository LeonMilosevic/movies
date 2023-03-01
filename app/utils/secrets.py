"""Mocking secret file."""

from app.utils.type_annotations import Json

db_secrets: Json = {
    "username": "postgres",
    "password": "postgres",
    "host": "172.17.0.2",
    "port": 5432,
    "database": "movies",
}
