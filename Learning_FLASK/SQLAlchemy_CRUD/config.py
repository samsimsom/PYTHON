

import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    # FLASK
    DEBUG = os.environ.get('DEBUG')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    FLASK_APP = os.environ.get('FLASK_APP')
    SECRET_KEY = 'secret-key'

    # SQLALCHEMY
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
