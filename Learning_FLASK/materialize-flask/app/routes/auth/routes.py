from flask import (render_template,
                   redirect,
                   url_for,
                   make_response,
                   jsonify,
                   request)

from app.routes.auth import auth
from app.forms.auth import LoginForm


@auth.route('/login', methods=['GET', 'POST'])
def login():
    title = 'Login'
    form = LoginForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            content = request.get_json(force=True)
            print(content)
            print('------------------------------')
            print(request.headers)
            print(request.form)
            print('------------------------------')
            return make_response(jsonify({'Success': 42}))

    return render_template('auth/login.html',
                           title=title,
                           form=form)


@auth.route('/register')
def register():
    return render_template('auth/register.html')


@auth.route('/logout')
def logout():
    return redirect(url_for('main.index'))
