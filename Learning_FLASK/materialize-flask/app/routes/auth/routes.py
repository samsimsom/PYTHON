from flask import (render_template,
                   redirect,
                   url_for,
                   request,
                   make_response,
                   jsonify)

from app.routes.auth import auth
from app.forms.auth import LoginForm


@auth.route('/login', methods=['GET'])
def login():
    title = 'Login'
    form = LoginForm()
    return render_template('auth/login.html',
                           title=title,
                           form=form)


@auth.route('/login-form-submit', methods=['POST'])
def login_form_submit():
    if request.method == 'POST':
        content = request.get_json(force=True)

        if content['password'] == 'asd':
            return make_response(jsonify({'Success': 42}))
        else:
            return make_response(jsonify({'Bad Credentials': 64}))


@auth.route('/register')
def register():
    return render_template('auth/register.html')


@auth.route('/logout')
def logout():
    return redirect(url_for('main.index'))
