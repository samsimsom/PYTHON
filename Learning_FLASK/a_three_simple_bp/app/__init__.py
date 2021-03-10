
from os import environ
from pkgutil import iter_modules
from flask import Flask

from app.extensions.database import db
from app.extensions.login import login
from app.extensions.migrate import migrate


def create_app():

    # Application Creation
    app = Flask(__name__)
    app.config.from_object(environ.get('APP_CONFIG'))

    # Extension Initialization
    db.init_app(app)
    login.init_app(app)
    migrate.init_app(app, db)

    # Blueprint Registration
    from app.routes import (main,
                            auth,
                            user,
                            about,
                            contact,
                            error)
    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint(user)
    app.register_blueprint(about)
    app.register_blueprint(contact)
    app.register_blueprint(error)

    return app


if __name__ == '__main__':
    create_app().run()
