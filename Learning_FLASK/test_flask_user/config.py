
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
    SQLALCHEMY_TRACK_MODIFICATIONS = environ.get(
        'SQLALCHEMY_TRACK_MODIFICATIONS')
    SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')

    # Flask-Mail SMTP server settings
    MAIL_SERVER = environ.get('MAIL_SERVER')
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'info.cgsource@gmail.com'
    MAIL_PASSWORD = 'zskehcijholkqzqz'
    MAIL_DEFAULT_SENDER = environ.get('MAIL_DEFAULT_SENDER')

    # Flask-User settings
    USER_APP_NAME = environ.get('USER_APP_NAME')
    USER_ENABLE_EMAIL = environ.get('USER_ENABLE_EMAIL')
    USER_ENABLE_USERNAME = environ.get('USER_ENABLE_USERNAME')
    USER_EMAIL_SENDER_NAME = environ.get('USER_EMAIL_SENDER_NAME')
    USER_EMAIL_SENDER_EMAIL = environ.get('USER_EMAIL_SENDER_EMAIL')


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
