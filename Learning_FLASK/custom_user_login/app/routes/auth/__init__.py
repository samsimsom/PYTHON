

from flask import Blueprint

auth = Blueprint('auth', __name__, template_folder='templates',
                 url_prefix='/auth')

from app.routes.auth import routes
