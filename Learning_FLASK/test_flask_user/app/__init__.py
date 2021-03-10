
from os import environ
from flask import Flask

from app.extensions.database import db
from app.extensions.user_manager import user_manager
from app.extensions.mail import mail
from app.extensions.migrate import migrate


def create_app():

    # Application Creation
    app = Flask(__name__)
    app.config.from_object(environ.get('APP_CONFIG'))

    # Extension Initialization
    db.init_app(app)
    user_manager.init_app(app)
    mail.init_app(app)
    migrate.init_app(app, db)

    # Blueprint Registration
    from app.routes import (main)

    app.register_blueprint(main)

    return app


if __name__ == '__main__':
    create_app().run()
