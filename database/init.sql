CREATE DATABASE movies;

\c movies;

CREATE TABLE IF NOT EXISTS movie (
    mov_id INT NOT NULL PRIMARY KEY,
    mov_title VARCHAR(50),
    mov_year INT,
    mov_time INT,
    mov_lang VARCHAR(50),
    mov_dt_rel DATE,
    mov_rel_country VARCHAR(5)
);

CREATE TABLE IF NOT EXISTS actor (
    act_id INT NOT NULL PRIMARY KEY,
    act_fname VARCHAR(20),
    act_lname VARCHAR(20),
    act_gender VARCHAR(1)
);

CREATE TABLE IF NOT EXISTS movie_cast (
    mov_id INT NOT NULL,
    act_id INT NOT NULL,
    role VARCHAR(30),
    PRIMARY KEY (mov_id, act_id, role),
    FOREIGN KEY (mov_id) REFERENCES movie(mov_id),
    FOREIGN KEY (act_id) REFERENCES actor(act_id)
);

CREATE TABLE IF NOT EXISTS director (
    dir_id INT NOT NULL PRIMARY KEY,
    dir_fname VARCHAR(20),
    dir_lname VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS movie_direction (
    dir_id INT NOT NULL,
    mov_id INT NOT NULL,
    PRIMARY KEY (dir_id, mov_id),
    FOREIGN KEY (dir_id) REFERENCES director(dir_id),
    FOREIGN KEY (mov_id) REFERENCES movie(mov_id)
);

CREATE TABLE IF NOT EXISTS genres (
    gen_id INT NOT NULL PRIMARY KEY,
    gen_title VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS movie_genres (
    mov_id INT NOT NULL,
    gen_id INT NOT NULL,
    PRIMARY KEY (mov_id, gen_id),
    FOREIGN KEY (mov_id) REFERENCES movie(mov_id),
    FOREIGN KEY (gen_id) REFERENCES genres(gen_id)
);

CREATE TABLE IF NOT EXISTS reviewer (
    rev_id INT NOT NULL PRIMARY KEY,
    rev_name VARCHAR(30)
);

CREATE TABLE IF NOT EXISTS rating (
    mov_id INT NOT NULL,
    rev_id INT NOT NULL,
    rev_stars INT,
    num_o_ratings INT,
    PRIMARY KEY (mov_id, rev_id),
    FOREIGN KEY (mov_id) REFERENCES movie(mov_id),
    FOREIGN KEY (rev_id) REFERENCES reviewer(rev_id)
);

CREATE TABLE IF NOT EXISTS movies_per_year (
    release_year INT,
    num_of_movies INT
);

CREATE TABLE IF NOT EXISTS number_of_actors_per_movie (
    mov_id INT,
    num_of_actors INT
);

CREATE TABLE IF NOT EXISTS number_of_different_movie_genres (
    num_of_genres INT
);


