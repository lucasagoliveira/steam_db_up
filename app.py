import warnings
warnings.filterwarnings('ignore', category=FutureWarning)
from flask import abort, render_template, Flask
import logging
import db

APP = Flask(__name__)

#Start page
@APP.route('/')
def index():
    stats = {}
    stats = db.execute('''
        SELECT * FROM
            (SELECT COUNT(*) n_cathegory FROM CATHEGORY)
        JOIN
            (SELECT COUNT(*) n_company FROM COMPANY)
        JOIN
            (SELECT COUNT(*) n_developer FROM DEVELOPER)
        JOIN
            (SELECT COUNT(*) n_dlc FROM DLC)
        JOIN
            (SELECT COUNT(*) n_game FROM GAME)
        JOIN
            (SELECT COUNT(*) n_music FROM MUSIC)
        JOIN
            (SELECT COUNT(*) n_product FROM PRODUCT)
        JOIN
            (SELECT COUNT(*) n_publisher FROM PUBLISHER)
    ''').fetchone()
    logging.info(stats)
    return render_template('index.html', stats = stats)

# DLCs
@APP.route('/dlcs/')
def list_dlcs():
    dlcs = db.execute('''
        SELECT app_id, dlc_id, game_id, kind_id, name, required_age, achievements, release_date, coming_soon, price, review_score, total_positive, total_positive, rating, owners, average_forever, median_forever, tags, sported_audio, categories, genres, platforms, packages, supported_lang
        FROM DLC
        NATURAL JOIN PRODUCT
        ORDER BY name
    ''').fetchall()
    return render_template('dlc-list.html', dlcs=dlcs)

# Games
@APP.route('/games/')
def list_games():
    games = db.execute('''
        SELECT app_id, game_id, kind_id, name, required_age, achievements, release_date, coming_soon, price, review_score, total_positive, total_positive, rating, owners, average_forever, median_forever, tags, sported_audio, categories, genres, platforms, packages, supported_lang
        FROM GAME
        NATURAL JOIN PRODUCT
        ORDER BY name
    ''').fetchall()
    return render_template('game-list.html', games=games)

# Musics
@APP.route('/musics/')
def list_musics():
    musics = db.execute('''
        SELECT app_id, game_id, kind_id, name, required_age, achievements, release_date, coming_soon, price, review_score, total_positive, total_positive, rating, owners, average_forever, median_forever, tags, sported_audio, categories, genres, platforms, packages, supported_lang
        FROM MUSIC
        NATURAL JOIN PRODUCT
        ORDER BY name
    ''').fetchall()
    return render_template('music-list.html', musics=musics)

@APP.route('/musics/<int:id>')
def get_movie(id):
    music = db.execute('''
         SELECT app_id, game_id, kind_id, name, required_age, achievements, release_date, coming_soon, price, review_score, total_positive, total_positive, rating, owners, average_forever, median_forever, tags, sported_audio, categories, genres, platforms, packages, supported_lang
         FROM MUSIC
         NATURAL JOIN PRODUCT
         WHERE app_id = ?     
    ''', [id]).fetchone()
    
    if music is None:
        abort(404, 'Music id {} does not exist.'.format(id))
        
    publisher = db.execute('''
                           
    ''')