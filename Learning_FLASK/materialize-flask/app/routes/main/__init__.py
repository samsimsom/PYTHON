

from flask import Blueprint

main = Blueprint('main', __name__)

from app.routes.main import routes
