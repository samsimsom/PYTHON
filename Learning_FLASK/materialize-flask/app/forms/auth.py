from flask_wtf import FlaskForm
from wtforms import (StringField,
                     PasswordField,
                     SubmitField)
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    email = StringField('Email',
                        id='login-email-input',
                        validators=[
                            DataRequired(),
                            Email()
                        ])
    password = PasswordField('Password',
                             id='login-password-input',
                             validators=[
                                 DataRequired()
                             ])
    submit = SubmitField('Login', id='login-submit-button')
