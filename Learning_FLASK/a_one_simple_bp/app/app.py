
# ------------------------------------------------------------------------------
# PYTHON IMPORT
import os

# ------------------------------------------------------------------------------
# FLASK IMPORT
from flask import Flask

# ------------------------------------------------------------------------------
# EXTENSION IMPORT
from app.extensions.sqlalchemy import db
from app.extensions.migrate import migrate
from app.extensions.commands import commands

# ------------------------------------------------------------------------------
# STRUCTURE IMPORT
from app.blueprints.main.views import main
from app.blueprints.products.views import product
from app.blueprints.contact.views import contact
from app.blueprints.about.views import about
from app.blueprints.error.views import error


def create_app():

    app = Flask(__name__)
    app.config.from_object(os.environ['APP_SETTINGS'])

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(main)
    app.register_blueprint(product)
    app.register_blueprint(contact)
    app.register_blueprint(about)
    app.register_blueprint(error)
    app.register_blueprint(commands)

    return app


if __name__ == "__main__":
    create_app().run()
