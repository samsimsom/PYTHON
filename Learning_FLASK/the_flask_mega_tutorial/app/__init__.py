
import os

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)	# app instance
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# circular dependency problemi yaratmamasi icin altta import ediyorum
from app import routes, models	# routes moduel import