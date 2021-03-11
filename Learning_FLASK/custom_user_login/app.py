
# ------------------------------------------------------------------------------
# IMPORT
from flask import (Flask, render_template, redirect, url_for)
from flask_sqlalchemy import SQLAlchemy


# ------------------------------------------------------------------------------
# CONFIG
app = Flask(__name__)
app.config['SECREY_KEY'] = 'secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# ------------------------------------------------------------------------------
# ROUTE
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/logout')
def logout():
    return redirect(url_for('index'))
