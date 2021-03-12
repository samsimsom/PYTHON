
from os import environ
from flask import Flask

from app.exts.database import db


def create_app():

    app = Flask(__name__)
    app.config.from_object(environ.get('APP_CONFIG'))

    db.init_app(app)


if __name__ == '__main__':
    create_app().run()
