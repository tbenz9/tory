
try:
    import pprint
    import json
    import os
    import sqlite3
    from flask import Flask, request, session, g, redirect, url_for, abort,render_template, flash
except ImportError:
    print 'Not all libraries are avaiable'
except:
    print 'Error found while importing libraries'

try:
    # create our little application :)                                      http://flask.pocoo.org/docs/0.11/tutorial/setup/
    app = Flask(__name__)
    app.config.from_object(__name__)

    # Load default config and override config from an environment variable  http://flask.pocoo.org/docs/0.11/tutorial/setup/
    app.config.update(dict(
        DATABASE=os.path.join(app.root_path, 'flaskr.db'),
        SECRET_KEY='development key',
        USERNAME='admin',
        PASSWORD='default'
    ))
    app.config.from_envvar('FLASKR_SETTINGS', silent=True)
except:
    print 'Error occurred while making application'

@app.route('/')
def home():
    """Default route when app.run() is called. 
    This function gets all the data from the data base and displays it to a html webpage."""
    db = connect_db()
    cur = db.execute('select * from entries')
    posts = [dict(type=row[1], json=row[2]) for row in cur.fetchall()]
    db.close()
    try:
        return render_template('index.html', posts=posts) # render a template
    except:
        return 'Problem'

def connect_db():                                                      #http://flask.pocoo.org/docs/0.11/tutorial/setup/
    """Connects to the specific database."""
    try:
        rv = sqlite3.connect(app.config['DATABASE'])
        rv.row_factory = sqlite3.Row                                        #allows us to treat the rows as if they were dictionaries instead of tuples.
        return rv
    except:
        print 'Error ocurred while connecting'

def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    try:
        if not hasattr(g, 'sqlite_db'):
            g.sqlite_db = connect_db()
        return g.sqlite_db
    except:
        print 'Error occured while getting database.'
    
def init_db():
    try:
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
    except:
        print 'Error occured while declaring database'

@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    init_db()
    print 'Initialized the database.'

@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    try:
        if hasattr(g, 'sqlite_db'):
            g.sqlite_db.close()
    except:
        print 'Error occured while closing connection'

def insert(info, json):
    with app.app_context():
        # db is the database connection
        # when data is stored, stores (id_num, info_type, json)
        try:
            db = get_db()
            cur = db.cursor()
            format_str = """INSERT INTO entries (info_type, json) VALUES ("{info_type}", '{json}');"""
            sql_command = format_str.format(info_type = info, json = str(json))
            cur.execute(sql_command)
            db.commit()
            id = cur.lastrowid
            cur.close()
            print str(info) + " info added to database."
            return id
        except:
            print 'Error occured while inserting item to database'

#print all entries from table
def retrieve(info):
    """retrieves data from database. 
    Prints all the entries from the given info type"""
    with app.app_context():
        try:
            db = get_db()
            sql_command = 'SELECT * FROM entries' 
            cur = db.execute(sql_command)
            entries = cur.fetchall()
            print ''
            for entry in entries:
                if entry[1] == info:
                    pprint.pprint(json.loads(entry[2]))
                    print ''
            db.close()
        except:
            print 'Error occured while retrieve data from database'

def run():
    app.run()

if __name__ == "__main__":
    app.run()
