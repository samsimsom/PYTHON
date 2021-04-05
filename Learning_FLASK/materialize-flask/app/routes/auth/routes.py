from flask import (render_template,
                   redirect,
                   url_for)

from app.routes.auth import auth
from app.forms.auth import LoginForm


@auth.route('/login')
def login():
    title = 'Login'
    form = LoginForm()
    return render_template('auth/login.html',
                           title=title,
                           form=form)


@auth.route('/register')
def register():
    return render_template('auth/register.html')


@auth.route('/logout')
def logout():
    return redirect(url_for('main.index'))
