--Run "sqlite3 steam_db_up.bd" in the terminal to create the database

----------------------------------------------
-- CREATE DATABASE IF NOT EXISTS steam_db_up

.open steam_db_up.db

-- Create 'company' table
CREATE TABLE IF NOT EXISTS company (
    company_id INT(255) NOT NULL,
    name VARCHAR(50) NOT NULL,
    released_games INT(255) NOT NULL,
    unreleased_games INT(255) NOT NULL,
    total_revenue INT(255) NOT NULL,
    avgrevenue_pergame VARCHAR(50),
    medrevenue_pergame VARCHAR(50),
    hq_country INT(255),
    PRIMARY KEY (company_id)
);

-- Create 'kind' table
CREATE TABLE IF NOT EXISTS kind (
    kind_id INT(255) NOT NULL,
    name VARCHAR(50) NOT NULL,
    PRIMARY KEY (kind_id)
);

-- Create 'publisher' table
CREATE TABLE IF NOT EXISTS publisher (
    company_id INT(255) NOT NULL,
    name VARCHAR(50) NOT NULL,
    FOREIGN KEY (company_id) REFERENCES company(company_id),
    FOREIGN KEY (name) REFERENCES company(name)
);

-- Create 'developer' table
CREATE TABLE IF NOT EXISTS developer (
    company_id INT(255) NOT NULL,
    name VARCHAR(50) NOT NULL,
    FOREIGN KEY (company_id) REFERENCES company(company_id),
    FOREIGN KEY (name) REFERENCES company(name)
);

-- Create 'product' table
CREATE TABLE IF NOT EXISTS product (
    app_id INT(255) NOT NULL,
    kind_id INT(255) NOT NULL,
    name VARCHAR(50) NOT NULL,
    required_age INT(255) NOT NULL,
    achievements INT(255),
    release_date DATE,
    coming_soon BOOLEAN,
    price DOUBLE NOT NULL,
    review_score DOUBLE NOT NULL,
    total_positive DOUBLE NOT NULL,
    total_negative DOUBLE NOT NULL,
    rating DOUBLE NOT NULL,
    owners VARCHAR(50),
    average_forever DOUBLE NOT NULL,
    median_forever DOUBLE NOT NULL,
    tags JSON,
    sported_audio JSON,
    categories JSON,
    genres JSON,
    platforms JSON,
    packages JSON,
    supported_lang JSON,
    PRIMARY KEY (app_id),
    FOREIGN KEY (kind_id) REFERENCES kind(kind_id)
);

-- Create 'game' table
CREATE TABLE IF NOT EXISTS game (
    game_id INT(255) NOT NULL,
    kind_id INT(255) NOT NULL,
    app_id INT(255) NOT NULL,
    name VARCHAR(50) NOT NULL,
    PRIMARY KEY (game_id),
    FOREIGN KEY (kind_id) REFERENCES kind(kind_id),
    FOREIGN KEY (app_id) REFERENCES product(app_id),
    FOREIGN KEY (name) REFERENCES product(name)
);

-- Create 'dlc' table
CREATE TABLE IF NOT EXISTS dlc (
    app_id INT(255) NOT NULL,
    dlc_id INT(255) NOT NULL,
    name VARCHAR(50) NOT NULL,
    kind_id INT(255) NOT NULL,
    game_id INT(255) NOT NULL,
    PRIMARY KEY (dlc_id),
    FOREIGN KEY (kind_id) REFERENCES kind(kind_id),
    FOREIGN KEY (game_id) REFERENCES game(game_id),
    FOREIGN KEY (app_id) REFERENCES product(app_id),
    FOREIGN KEY (name) REFERENCES product(name)
);

-- Create 'music' table
CREATE TABLE IF NOT EXISTS music (
    app_id INT(255) NOT NULL,
    music_id INT(255) NOT NULL,
    name VARCHAR(50) NOT NULL,
    kind_id INT(255) NOT NULL,
    game_id INT(255) NOT NULL,
    PRIMARY KEY (music_id),
    FOREIGN KEY (kind_id) REFERENCES kind(kind_id),
    FOREIGN KEY (app_id) REFERENCES product(app_id),
    FOREIGN KEY (game_id) REFERENCES game(game_id),
    FOREIGN KEY (name) REFERENCES product(name)
);