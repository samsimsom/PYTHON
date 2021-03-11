
# ------------------------------------------------------------------------------
# IMPORT
from os import environ
from flask import (Flask, render_template, redirect, url_for)
from flask_mongoengine import MongoEngine
from os.path import abspath, join, dirname
from dotenv import load_dotenv

app_base_dir = abspath(dirname(__file__))
load_dotenv(join(app_base_dir, '.env'))

# ------------------------------------------------------------------------------
# CONFIG
app = Flask(__name__)
app.config['SECREY_KEY'] = 'secret-key'

app.config['MONGODB_DB'] = environ.get('MONGODB_DB')
app.config['MONGODB_HOST'] = environ.get('MONGODB_HOST')
app.config['MONGODB_PORT'] = int(environ.get('MONGODB_PORT'))
app.config['MONGODB_USERNAME'] = environ.get('MONGODB_USERNAME')
app.config['MONGODB_PASSWORD'] = environ.get('MONGODB_PASSWORD')

db = MongoEngine(app)


class User(db.Document):
    email = db.StringField(required=True)
    first_name = db.StringField(max_length=50)
    last_name = db.StringField(max_length=50)

# ------------------------------------------------------------------------------
# ROUTE


@app.route('/')
def index():

    a = User.objects(first_name='John')

    return render_template('index.html', a=a)


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/logout')
def logout():
    return redirect(url_for('index'))
