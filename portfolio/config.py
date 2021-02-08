
import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY')
    WTF_CSRF_SECRET_KEY = os.getenv('WTF_CSRF_SECRET_KEY')

    DEBUG = bool(os.getenv('FLASK_DEBUG'))
    HOSTNAME = os.getenv('FLASK_RUN_HOST')

    # SQLAlchemy Settings
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')