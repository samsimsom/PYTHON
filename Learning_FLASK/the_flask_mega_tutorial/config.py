
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	DEBUG = os.environ.get("DEBUG")
	FLASK_ENV = os.environ.get("FLASK_ENV")
	FLASK_APP = os.environ.get("FLASK_APP")

	SECRET_KEY = os.environ.get("SECRET_KEY")
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
	SQLALCHEMY_TRACK_MODIFICATIONS = False