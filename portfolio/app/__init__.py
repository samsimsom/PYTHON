
#///////////////////////////////////////////////////////
# APP // __init__.py
#///////////////////////////////////////////////////////

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()
bootstrap = Bootstrap()

# Application Factory
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    bootstrap.init_app(app)

    # PORTFOLIO
    from app.portfolio import bp as portfolio_bp
    app.register_blueprint(portfolio_bp, url_prefix="/")

    # AUTH
    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix="/auth/")

    # ADMIN
    from app.admin import bp as admin_bp
    app.register_blueprint(admin_bp, url_prefix="/admin/")

    return app


# from app.auth.models import User