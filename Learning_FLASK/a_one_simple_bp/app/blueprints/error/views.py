

from flask import Blueprint, render_template
from app.extensions.sqlalchemy import db

error = Blueprint('error', __name__,
                  template_folder='templates',
                  url_prefix='/error')


@error.app_errorhandler(404)
def page_not_found(error):
    return render_template('error/404.html'), 404


@error.app_errorhandler(500)
def internal_server_error(error):
    db.session.rollback()
    return render_template('error/500.html'), 500
