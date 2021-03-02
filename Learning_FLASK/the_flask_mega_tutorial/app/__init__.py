
import os

from flask import Flask
from config import Config


app = Flask(__name__)	# app instance
app.config.from_object(Config)


# circular dependency problemi yaratmamasi icin altta import ediyorum
from app import routes	# routes moduel import