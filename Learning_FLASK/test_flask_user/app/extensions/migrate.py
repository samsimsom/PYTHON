

from flask_migrate import Migrate

migrate = Migrate()


def init_app(application, database):
    migrate.init_app(app=application, db=database)
