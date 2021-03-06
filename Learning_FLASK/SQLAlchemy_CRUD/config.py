

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = os.environ.get('DEBUG')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    FLASK_APP = os.environ.get('FLASK_APP')
    SECRET_KEY = 'secret-key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:////app.db'
