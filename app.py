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
            (SELECT COUNT(*) n_kind FROM kind)
        JOIN
            (SELECT COUNT(*) n_company FROM company)
        JOIN
            (SELECT COUNT(*) n_dlc FROM dlc)
        JOIN
            (SELECT COUNT(*) n_game FROM game)
        JOIN
            (SELECT COUNT(*) n_music FROM music)
        JOIN
            (SELECT COUNT(*) n_product FROM PRODUCT)
    ''').fetchone()
    logging.info(stats)
    return render_template('index.html', stats = stats)


# Products
@APP.route('/products')
def list_products():
    products = db.execute('''
        SELECT *
        FROM product
        ORDER BY name                      
    ''').fetchall()
    return render_template('products.html', products = products)


# DLCs
@APP.route('/dlcs/')
def list_dlcs():
    dlcs = db.execute('''
        SELECT *
        FROM dlc
        NATURAL JOIN product
        ORDER BY name
    ''').fetchall()
    return render_template('dlc-list.html', dlcs=dlcs)

@APP.route('/dlcs/<int:id>')
def get_dlc(id):
    dlc = db.execute('''
        SELECT *
        FROM dlc
        NATURAL JOIN product
        WHERE product_id = ?
    ''', [id]).fetchone()
    
    if dlc is None:
        abort(404, 'Dlc id {} does not exist.'.format(id))
        
    publishers_id = db.execute('''
        SELECT publishers_id
        FROM dlc
        NATURAL JOIN product
        WHERE product_id = ?
    ''', [id]).fetchone()
    
    aux = str(publishers_id[0]).split(';')
    publishers = {}
    for publisher in aux:
        publishers[publisher] = db.execute('''
            SELECT name
            FROM company
            WHERE company_id = ?
        ''', [publisher]).fetchone()[0]
    
    developers_id = db.execute('''
        SELECT developers_id
        FROM dlc
        NATURAL JOIN product
        WHERE product_id = ?
    ''', [id]).fetchone()
    
    aux = str(developers_id[0]).split(';')
    developers = {}
    for developer in aux:
        developers[developer] = db.execute('''
            SELECT name
            FROM company
            WHERE company_id = ?
        ''', [developer]).fetchone()[0]
    
    return render_template('dlc.html', dlc = dlc, publishers = publishers, developers = developers)


# Games
@APP.route('/games/')
def list_games():
    games = db.execute('''
        SELECT *
        FROM game
        NATURAL JOIN product
        ORDER BY name
    ''').fetchall()
    return render_template('game-list.html', games=games)

@APP.route('/games/<int:id>')
def get_game(id):
    game = db.execute('''
        SELECT *
        FROM game
        NATURAL JOIN product
        WHERE product_id = ?    
    ''', [id]).fetchone()
    
    if game is None:
        abort(404, 'Game id {} does not exist.'.format(id))
        
    publishers_id = db.execute('''
        SELECT publishers_id
        FROM game
        NATURAL JOIN product
        WHERE product_id = ?
    ''', [id]).fetchone()
    
    aux = str(publishers_id[0]).split(';')
    publishers = {}
    for publisher in aux:
        publishers[publisher] = db.execute('''
            SELECT name
            FROM company
            WHERE company_id = ?
        ''', [publisher]).fetchone()[0]
    
    developers_id = db.execute('''
        SELECT developers_id
        FROM game
        NATURAL JOIN product
        WHERE product_id = ?
    ''', [id]).fetchone()
    
    aux = str(developers_id[0]).split(';')
    developers = {}
    for developer in aux:
        developers[developer] = db.execute('''
            SELECT name
            FROM company
            WHERE company_id = ?
        ''', [developer]).fetchone()[0]
    
    return render_template('game.html', game = game, publishers = publishers, developers = developers)


# Musics
@APP.route('/musics/')
def list_musics():
    musics = db.execute('''
        SELECT *
        FROM music
        NATURAL JOIN product
        ORDER BY name
    ''').fetchall()
    return render_template('music-list.html', musics=musics)

@APP.route('/musics/<int:id>')
def get_music(id):
    music = db.execute('''
        SELECT *
        FROM music
        NATURAL JOIN product
        WHERE product_id = ?     
    ''', [id]).fetchone()
    
    if music is None:
        abort(404, 'Music id {} does not exist.'.format(id))
        
    publishers_id = db.execute('''
        SELECT publishers_id
        FROM music
        NATURAL JOIN product
        WHERE product_id = ?
    ''', [id]).fetchone()
    
    aux = str(publishers_id[0]).split(';')
    publishers = {}
    for publisher in aux:
        publishers[publisher] = db.execute('''
            SELECT name
            FROM company
            WHERE company_id = ?
        ''', [publisher]).fetchone()[0]
    
    developers_id = db.execute('''
        SELECT developers_id
        FROM music
        NATURAL JOIN product
        WHERE product_id = ?
    ''', [id]).fetchone()
    
    aux = str(developers_id[0]).split(';')
    developers = {}
    for developer in aux:
        developers[developer] = db.execute('''
            SELECT name
            FROM company
            WHERE company_id = ?
        ''', [developer]).fetchone()[0]
    
    return render_template('music.html', music = music, publishers = publishers, developers = developers)


# Companies
@APP.route('/companies/')
def list_companies():
    companies = db.execute('''
        SELECT *
        FROM company
        ORDER BY name
    ''').fetchall()
    return render_template('company-list.html', companies = companies)

@APP.route('/companies/<int:id>')
def get_company(id):
    company = db.execute('''
        SELECT *
        FROM company
        WHERE company_id = ?     
    ''', [id]).fetchone()
    
    if company is None:
        abort(404, 'Company id {} does not exist.'.format(id))
        
    return render_template('company.html', company = company)


# Kinds
@APP.route('/kinds/')
def list_kinds():
    kinds = db.execute('''
        SELECT *
        FROM kind
        ORDER BY kind_id
    ''').fetchall()
    return render_template('kind-list.html', kinds = kinds)

@APP.route('/kinds/<int:id>')
def get_kind(id):
    kind = db.execute('''
        SELECT *
        FROM kind
        WHERE kind_id = ?     
    ''', [id]).fetchone()
    
    if kind is None:
        abort(404, 'Kind id {} does not exist.'.format(id))
        
    return render_template('kind.html', kind = kind)

# DLCs per Game
@APP.route('/dlcs-per-game/')
def get_dlcs_per_game():
    table = db.execute('''
        SELECT name, COUNT(*) as number_of_dlcs
        FROM dlc
        JOIN game
        JOIN product
        WHERE dlc.game_id = game.product_id and game.product_id = product.product_id
        GROUP BY game_id
    ''').fetchone()
    
    return render_template('dlcs-per-game.html', table = table)

# Musics per Game
@APP.route('/musics-per-game/')
def get_musics_per_game():
    table = db.execute('''
        SELECT name, COUNT(*) as number_of_musics
        FROM music
        JOIN game
        JOIN product
        WHERE music.game_id = game.product_id and game.product_id = product.product_id
        GROUP BY game_id
    ''').fetchone()
    
    return render_template('musics-per-game.html', table = table)
    
# Products like %text%
@APP.route('/products/like/<text>')
def get_products_like(text):
    text = '%'+text+'%'
    table = db.execute('''
        SELECT *
        FROM products
        where name like ? 
    ''', [text]).fetchall()
    
    if table is None:
        abort(404, 'There is no product with {} in its name'.format(text))
        
    return render_template('product-like.html', table = table)