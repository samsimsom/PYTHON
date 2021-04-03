

from flask import Blueprint

todo = Blueprint('todo', __name__, url_prefix='/todo')

from app.routes.todo import routes
