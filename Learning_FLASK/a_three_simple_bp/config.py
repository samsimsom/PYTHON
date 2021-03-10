
from os import environ
from os.path import abspath, join, dirname
from dotenv import load_dotenv

app_base_dir = abspath(dirname(__file__))
load_dotenv(join(app_base_dir, '.env'))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = environ.get('SQLA_TRACK_MODIFICATIONS')
    SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
