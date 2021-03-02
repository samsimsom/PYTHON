
import os

class Config(object):
	DEBUG = os.environ.get("DEBUG")
	FLASK_ENV = os.environ.get("FLASK_ENV")
	FLASK_APP = os.environ.get("FLASK_APP")
	SECRET_KEY = os.environ.get("SECRET_KEY")