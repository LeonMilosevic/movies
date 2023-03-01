"""File contains queries for data modeling."""

from sqlalchemy import Engine, text

from app.utils.db_helpers import truncate_tables

movies_per_year = """
CREATE TABLE IF NOT EXISTS movies_per_year AS (
SELECT EXTRACT(YEAR FROM mov_dt_rel) AS release_year, COUNT(*) AS num_of_movies
FROM movie
WHERE mov_dt_rel IS NOT NULL
GROUP BY EXTRACT(YEAR FROM mov_dt_rel)
);
"""

number_of_actors_per_movie = """
CREATE TABLE IF NOT EXISTS number_of_actors_per_movie AS (
SELECT mov_id, COUNT(act_id) AS num_of_actors
FROM movie_cast
GROUP BY mov_id
);
"""

number_of_different_movie_genres = """
CREATE TABLE IF NOT EXISTS number_of_different_movie_genres AS (
SELECT COUNT(DISTINCT gen_id) AS num_of_genres
FROM genres
);
"""

movie_reviewers = """
SELECT reviewer.rev_name, rating.rev_stars, movie.mov_title
FROM rating
LEFT JOIN reviewer ON rating.rev_id = reviewer.rev_id
LEFT JOIN movie ON rating.mov_id = movie.mov_id
WHERE rating.rev_stars > 7 AND reviewer.rev_name IS NOT NULL AND movie.mov_title IS NOT NULL
ORDER BY rating.rev_stars DESC;
"""


def execute_queries(engine: Engine) -> None:
    """Executes queries for data modeling.

    Args:
        engine: SQLAlchemy engine to connect to PostgreSQL database.
    """
    conn = engine.connect()
    tables = ["movies_per_year", "number_of_actors_per_movie", "number_of_different_movie_genres"]

    truncate_tables(engine, tables)
    queries = [
        movies_per_year,
        number_of_actors_per_movie,
        number_of_different_movie_genres,
    ]
    for query in queries:
        conn.execute(text(query))
        conn.commit()

    # execute query
    result = conn.execute(text(movie_reviewers)).fetchall()
    print(result)
