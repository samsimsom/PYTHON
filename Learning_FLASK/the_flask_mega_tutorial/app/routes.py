

from flask import (render_template,
                   flash,
                   redirect,
                   url_for)
from flask_login import login_user, current_user
from app import app
from app.forms import LoginForm
from app.models import User


@app.route('/')
@app.route('/index')
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


@app.route('/login', methods=['GET', 'POST'])
def login():

    if current_user.is_authenticated:
        return redirect(url_for('index'))

    title = 'Login'
    form = LoginForm()

    if form.validate_on_submit():

        user = User.query.filter_by(username=form.username.data).first()

        if (user is None) or (user.check_password(form.password.data)):
            flash('Invalid username or password')
            return redirect(url_for('login'))

        login_user(user, remember=form.remember_me.data)
        return redirect('/index')

    return render_template('login.html',
                           title=title,
                           form=form)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return 'Contact'
