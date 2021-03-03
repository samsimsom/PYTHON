
from flask import (render_template,
                   flash,
                   redirect,
                   url_for)
from app import app		# app package (directory) import app variable
from app.forms import LoginForm


@app.route('/')			# decorator from flask - URL
@app.route('/index')  	# more URL
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

    title = 'Login'
    form = LoginForm()

    if form.validate_on_submit():
        flash(f'Login requested for User: {form.username.data}, '
              f'Remember Me: {form.remember_me.data}')

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
