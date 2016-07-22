#flaskr2.py
#flaskr.py had some weird error so am starting over

import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

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


def connect_db():                                                       #http://flask.pocoo.org/docs/0.11/tutorial/setup/
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row                                        #allows us to treat the rows as if they were dictionaries instead of tuples.
    return rv


def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    init_db()
    print 'Initialized the database.'

def insert(info, json):
    with app.app_context():
        # g.db is the database connection
        g.db = get_db()
        cur = g.db.cursor()
       # query = ('INSERT INTO entries (info_type, json) VALUES (%s, %s)' % (info, json))
        format_str = """INSERT INTO entries (info_type, json) VALUES ("{info_type}", '{json}');"""
        sql_command = format_str.format(info_type = info, json = str(json))
        print sql_command
        cur.execute(sql_command)
       # print query
        #cur.execute(query)
        g.db.commit()
        id = cur.lastrowid
        cur.close()
        return id

#print all entries from table
def retrieve(info):
    with app.app_context():
        print "retrieve()"
        db = get_db()
        sql_command = 'SELECT * FROM entries' # WHERE info_type = %s;' %info
        print sql_command
        cur = db.execute(sql_command) #'SELECT json FROM entries WHERE info_type=%s', %info)
        
        entries = cur.fetchall()
        for entry in entries:
            if entry[1] == info:
                print entry
        db.close()
        return entries


#insert('hello',  '"{"eno16777984": {"ip_address": "192.168.80.36","link": true,"mac_address": "00:50:56:99:3e:8f","speed": 10.0},"eno33557248": {"ip_address": "192.168.0.6","link": true,"mac_address": "00:50:56:99:5d:3e","speed": 10.0},"lo": {"ip_address": "127.0.0.1","link": true,"mac_address": "00:00:00:00:00:00","speed": 0.0},"virbr0": {"ip_address": "192.168.122.1","link": true,"mac_address": "52:54:00:4a:ef:c3","speed": 0.0},"virbr0-nic": {"ip_address": "52:54:00:4a:ef:c3","link": false,"mac_address": "52:54:00:4a:ef:c3","speed": 0.01}}')
#retrieve ('hello')


