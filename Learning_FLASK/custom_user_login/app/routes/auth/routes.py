

from flask import render_template, redirect, url_for, flash, request

from app.routes.auth import auth

from app.forms.form import LoginForm, RegistrationForm

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('auth/login.html', form=form)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    return render_template('auth/register.html', form=form)


@auth.route('/logout')
def logout():
    return redirect(url_for('main.index'))
