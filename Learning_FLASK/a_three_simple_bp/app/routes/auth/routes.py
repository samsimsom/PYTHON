

from flask import render_template
from app.routes.auth import auth


@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('auth/index.html')
