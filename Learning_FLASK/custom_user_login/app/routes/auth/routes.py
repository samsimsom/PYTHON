

from flask import (make_response,
                   render_template,
                   redirect,
                   url_for,
                   flash,
                   request,
                   session,
                   g)

from werkzeug.urls import url_parse
from app.routes.auth import auth    # Blueprint
from app.forms.form import LoginForm, RegistrationForm
from app.models.user import User, Role


@auth.before_app_request
def before_app_request():
    g.user = None

    if 'user' in session:
        g.user = session['user']


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit() and request.method == 'POST':

        user = User.objects.filter(username=form.username.data).first()

        if (user is None) or not (user.check_password(form.password.data)):
            flash('Invalid username or password.')
            return redirect(url_for('auth.login'))

        # Login User
        session['user'] = user.username
        # if form.remember_me.data:
        #     r = make_response(redirect(url_for('auth.login')))
        #     r.set_cookie('username', user.username, max_age=(60 * 60 * 24 * 7))
        #     return r

        next_page = request.args.get('next')
        print(f'Next Page: {next_page}')

        if not next_page or (url_parse(next_page).netloc != ''):
            next_page = url_for('main.index')

        return redirect(next_page)

    return render_template('auth/login.html',
                           form=form)


@auth.route('/register', methods=['GET', 'POST'])
def register():

    form = RegistrationForm()

    if form.validate_on_submit() and request.method == 'POST':
        user = User()
        user.username = form.username.data
        user.email = form.email.data
        user.set_password(form.password.data)
        user.role = Role.objects.get(id='604b33c1337f0cdd73f39995')
        user.save()

        flash('Congratulations, you are now a registered user!')

        return redirect(url_for('auth.login'))

    return render_template('auth/register.html',
                           form=form)


@auth.route('/logout')
def logout():
    if 'user' in session:
        session.pop('user', None)

    return redirect(url_for('main.index'))
