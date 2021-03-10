

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_app(application):
    db.init_app(app=application)
