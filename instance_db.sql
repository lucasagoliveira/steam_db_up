CREATE DATABASE IF NOT EXISTS steam_db_up;

USE steam_db_up;

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

-- Create 'cathegory' table
CREATE TABLE IF NOT EXISTS cathegory (
    cathegory_id INT(255) NOT NULL,
    name VARCHAR(50) NOT NULL,
    PRIMARY KEY (cathegory_id)
);

-- Create 'publishers' table
CREATE TABLE IF NOT EXISTS publishers (
    company_id INT(255) NOT NULL,
    name VARCHAR(50) NOT NULL,
    FOREIGN KEY (company_id) REFERENCES company(company_id)
);

-- Create 'developers' table
CREATE TABLE IF NOT EXISTS developers (
    company_id INT(255) NOT NULL,
    name VARCHAR(50) NOT NULL,
    FOREIGN KEY (company_id) REFERENCES company(company_id)
);

-- Create 'product' table
CREATE TABLE IF NOT EXISTS product (
    app_id INT(255) NOT NULL,
    cathegory_id INT(255) NOT NULL,
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
    FOREIGN KEY (cathegory_id) REFERENCES cathegory(cathegory_id)
);

-- Create 'game' table
CREATE TABLE IF NOT EXISTS game (
    game_id INT(255) NOT NULL,
    cathegory_id INT(255) NOT NULL,
    app_id INT(255) NOT NULL,
    name VARCHAR(50) NOT NULL,
    PRIMARY KEY (game_id),
    FOREIGN KEY (cathegory_id) REFERENCES cathegory(cathegory_id),
    FOREIGN KEY (app_id) REFERENCES product(app_id)
);

-- Create 'dlc' table
CREATE TABLE IF NOT EXISTS dlc (
    dlc_id INT(255) NOT NULL,
    name VARCHAR(50) NOT NULL,
    cathegory_id INT(255) NOT NULL,
    game_id INT(255) NOT NULL,
    PRIMARY KEY (dlc_id),
    FOREIGN KEY (cathegory_id) REFERENCES cathegory(cathegory_id),
    FOREIGN KEY (game_id) REFERENCES game(game_id)
);

-- Create 'music' table
CREATE TABLE IF NOT EXISTS music (
    music_id INT(255) NOT NULL,
    name VARCHAR(50) NOT NULL,
    cathegory_id INT(255) NOT NULL,
    game_id INT(255) NOT NULL,
    PRIMARY KEY (music_id),
    FOREIGN KEY (cathegory_id) REFERENCES cathegory(cathegory_id),
    FOREIGN KEY (game_id) REFERENCES game(game_id)
);