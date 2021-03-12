
from os import environ
from os.path import abspath, join, dirname
from dotenv import load_dotenv

app_base_dir = abspath(dirname(__file__))
load_dotenv(join(app_base_dir, '.env'))


class Config(object):
    # Flask
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = environ.get('SECRET_KEY')

    # Mongoengine
    MONGODB_DB = environ.get('SECRET_KEY')
    MONGODB_HOST = environ.get('SECRET_KEY')
    MONGODB_PORT = int(environ.get('SECRET_KEY'))
    MONGODB_USERNAME = environ.get('SECRET_KEY')
    MONGODB_PASSWORD = environ.get('SECRET_KEY')


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
