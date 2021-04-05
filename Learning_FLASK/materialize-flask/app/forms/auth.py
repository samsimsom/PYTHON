from flask_wtf import FlaskForm
from wtforms import (StringField,
                     PasswordField,
                     SubmitField)
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    email = StringField('Email',
                        id='login-email-input',
                        render_kw={
                            'class': 'form-control',
                            'placeholder': 'abc@abc.com',
                        },
                        validators=[
                            DataRequired(),
                            Email()
                        ])
    password = PasswordField('Password',
                             id='login-password-input',
                             render_kw={
                                 'class': 'form-control',
                             },
                             validators=[
                                 DataRequired()
                             ])
    submit = SubmitField('Submit',
                         id='login-submit-button',
                         render_kw={
                             'class': 'btn btn-primary',
                         })
