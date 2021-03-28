
import os
from dotenv import load_dotenv

app_base_dir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(app_base_dir, '.env'))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')

    # Mongoengine
    MONGODB_DB = os.environ.get('MONGODB_DB')
    MONGODB_HOST = os.environ.get('MONGODB_HOST')
    MONGODB_PORT = int(os.environ.get('MONGODB_PORT'))
    MONGODB_USERNAME = os.environ.get('MONGODB_USERNAME')
    MONGODB_PASSWORD = os.environ.get('MONGODB_PASSWORD')
