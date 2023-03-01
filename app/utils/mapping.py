"""File contains types of columns in csv files."""

from app.utils.type_annotations import MovieFiles

files: MovieFiles = {
    "movie": [
        "mov_id",
        "mov_title",
        "mov_year",
        "mov_time",
        "mov_lang",
        "mov_dt_rel",
        "mov_rel_country",
    ],
    "actor_table": ["act_id", "act_fname", "act_lname", "act_gender"],
    "movie_cast": ["act_id", "mov_id", "role"],
    "director": ["dir_id", "dir_fname", "dir_lname"],
    "movie_direction": ["dir_id", "mov_id"],
    "genres": ["gen_id", "gen_title"],
    "movie_genres": ["mov_id", "gen_id"],
    "reviewer": ["rev_id", "rev_name"],
    "rating": ["mov_id", "rev_id", "rev_stars", "num_o_ratings"],
}

numeric_columns_map = {
    "movie": [
        "mov_id",
        "mov_year",
        "mov_time",
    ],
    "actor_table": ["act_id"],
    "movie_cast": ["act_id", "mov_id"],
    "director": ["dir_id"],
    "movie_direction": ["dir_id", "mov_id"],
    "genres": ["gen_id"],
    "movie_genres": ["mov_id", "gen_id"],
    "rating": ["mov_id", "rev_id", "rev_stars", "num_o_ratings"],
    "reviewer": ["rev_id"],
}

date_columns_map = {"movie": ["mov_dt_rel"]}

pk_columns_map = {
    "movie": ["mov_id"],
    "actor_table": ["act_id"],
    "movie_cast": ["act_id", "mov_id", 'role'],
    "director": ["dir_id"],
    "movie_direction": ["dir_id", "mov_id"],
    "genres": ["gen_id"],
    "movie_genres": ["mov_id", "gen_id"],
    "reviewer": ["rev_id"],
}