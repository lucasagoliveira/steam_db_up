--Run "sqlite3 steam_db_up.bd" in the terminal to create the database

----------------------------------------------
-- CREATE DATABASE IF NOT EXISTS steam_db_up

.open steam_db_up.db

-- Create 'company' table
CREATE TABLE IF NOT EXISTS company (
    company_id INT(255) NOT NULL,
    name VARCHAR(255) NOT NULL,
    released_games INT(255) NOT NULL,
    unreleased_games INT(255) NOT NULL,
    total_revenue INT(255) NOT NULL,
    avgrevenue_pergame VARCHAR(255),
    medrevenue_pergame VARCHAR(255),
    hq_country INT(255),
    PRIMARY KEY (company_id)
);

-- Create 'kind' table
CREATE TABLE IF NOT EXISTS kind (
    kind_id INT(255) NOT NULL,
    name VARCHAR(255) NOT NULL,
    PRIMARY KEY (kind_id)
);

-- Create 'product' table
CREATE TABLE IF NOT EXISTS product (
    product_id INT(255) NOT NULL,
    kind_id INT(255) NOT NULL,
    name VARCHAR(255) NOT NULL,
    required_age INT(255) NOT NULL,
    achievements INT(255),
    release_date DATE,
    coming_soon BOOLEAN,
    price DOUBLE NOT NULL,
    review_score DOUBLE NOT NULL,
    total_positive DOUBLE NOT NULL,
    total_negative DOUBLE NOT NULL,
    rating DOUBLE NOT NULL,
    owners VARCHAR(255),
    average_forever DOUBLE NOT NULL,
    median_forever DOUBLE NOT NULL,
    tags JSON,
    sported_audio JSON,
    categories JSON,
    genres JSON,
    platforms JSON,
    packages JSON,
    supported_lang JSON,
    publishers_id JSON NOT NULL,
    developers_id JSON NOT NULL,
    PRIMARY KEY (product_id),
    FOREIGN KEY (kind_id) REFERENCES kind(kind_id)
);

-- Create 'game' table
CREATE TABLE IF NOT EXISTS game (
    product_id INT(255) NOT NULL,
    PRIMARY KEY (product_id),
    FOREIGN KEY (product_id) REFERENCES product(product_id)
);

-- Create 'dlc' table
CREATE TABLE IF NOT EXISTS dlc (
    game_id INT(255) NOT NULL,
    product_id INT(255) NOT NULL,
    PRIMARY KEY (product_id),
    FOREIGN KEY (product_id) REFERENCES product(product_id),
    FOREIGN KEY (game_id) REFERENCES game(product_id)
);

-- Create 'music' table
CREATE TABLE IF NOT EXISTS music (
    game_id INT(255) NOT NULL,
    product_id INT(255) NOT NULL,
    PRIMARY KEY (product_id),
    FOREIGN KEY (product_id) REFERENCES product(product_id),
    FOREIGN KEY (game_id) REFERENCES game(product_id)
);