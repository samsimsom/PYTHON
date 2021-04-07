
from flask import Flask
from config import Config

from app.exts.database import db, sessison_interface
from app.exts.csrf import csrf


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.session_interface = sessison_interface(db)

    db.init_app(app)
    csrf.init_app(app)

    from app.routes.main import main
    app.register_blueprint(main)

    from app.routes.auth import auth
    app.register_blueprint(auth)

    from app.routes.todo import todo
    app.register_blueprint(todo)

    return app


if __name__ == '__main__':
    create_app().run()
