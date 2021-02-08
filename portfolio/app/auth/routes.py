#///////////////////////////////////////////////////////
# AUTH // routes.py
#///////////////////////////////////////////////////////

from flask import render_template
from app.auth.forms import LoginForm, RegisterForm
from app.auth import bp


'''------------------------------------------------------------------'''
# AUTH / LOGIN
@bp.route('/login/', methods=['GET', 'POST'])
def login():
    title = 'login'
    form = LoginForm()

    return render_template('auth/login.html',
                            title=title,
                            form=form)


'''------------------------------------------------------------------'''
# AUTH / REGISTER
@bp.route('/register/', methods=['GET', 'POST'])
def register():
    title = 'register'
    form = RegisterForm()

    return render_template('auth/register.html',
                            title=title,
                            form=form)