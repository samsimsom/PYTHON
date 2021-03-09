

import os
from flask import Flask


from extensions.database import db
from extensions.commands import commands
from extensions.migrate import migrate

from blueprints.main.views import main
from blueprints.products.views import product
from blueprints.contact.views import contact
from blueprints.about.views import about
from blueprints.error.views import error


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
