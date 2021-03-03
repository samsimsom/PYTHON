

from flask import (request,
                   render_template,
                   flash,
                   redirect,
                   url_for)
from werkzeug.urls import url_parse
from flask_login import (current_user,
                         login_user,
                         logout_user,
                         login_required)
from app import app, db
from app.forms import LoginForm, RegistrationForm
from app.models import User


@app.route('/')
@app.route('/index')
@login_required
def index():

    title = 'Home'

    # FAKE DATA
    user = {'username': 'Firat'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Ankara!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The X-Man movie was so cool!'
        },
        {
            'author': {'username': 'Jessica'},
            'body': 'I\'m so Hot!'
        }
    ]

    return render_template('index.html',
                           title=title,
                           user=user,
                           posts=posts)


# ------------------------------------------------------------------------------
# LOGIN
@app.route('/login', methods=['GET', 'POST'])
def login():

    if current_user.is_authenticated:
        return redirect(url_for('index'))

    title = 'Login'
    form = LoginForm()

    if form.validate_on_submit():

        user = User.query.filter_by(username=form.username.data).first()

        if (user is None) or not (user.check_password(form.password.data)):
            flash('Invalid username or password')
            return redirect(url_for('login'))

        next_page = request.args.get('next')
        if not next_page or (url_parse(next_page).netloc != ''):
            next_page = url_for('index')

        login_user(user, remember=form.remember_me.data)
        return redirect('/index')

    return render_template('login.html',
                           title=title,
                           form=form)


# ------------------------------------------------------------------------------
# REGISTER
@app.route('/register', methods=['GET', 'POST'])
def register():

    if current_user.is_authenticated:
        return redirect(url_for('index'))

    title = 'Register'
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))

    return render_template('register.html',
                           title=title,
                           form=form)


# ------------------------------------------------------------------------------
# ABOUT
@app.route('/about')
def about():
    return render_template('about.html')


# ------------------------------------------------------------------------------
# CONTACT
@app.route('/contact')
def contact():
    return 'Contact'


# ------------------------------------------------------------------------------
# LOGOUT
@app.route('/logut')
def logout():
    logout_user()
    return redirect('index')
