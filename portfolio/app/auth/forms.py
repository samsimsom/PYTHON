#///////////////////////////////////////////////////////
# AUTH // forms.py
#///////////////////////////////////////////////////////

from flask_wtf import FlaskForm
from wtforms import SubmitField, PasswordField, StringField, BooleanField
from wtforms.fields.html5 import EmailField
from wtforms.validators import (DataRequired, Email, Length, EqualTo,
                                ValidationError)


class RegisterForm(FlaskForm):
    """
    Registeration Form
    """

    username = StringField(u"Username", validators=[DataRequired(), Length(min=4, max=25)])
    email = EmailField(u"Email", validators=[DataRequired(), Length(min=3, max=128)])
    password = PasswordField(u"Password", validators=[DataRequired(), EqualTo("confirm_password"), Length(min=3, max=80)])
    confirm_password = PasswordField(u"Confirm Password", validators=[DataRequired()])
    submit = SubmitField(u"Register")



class LoginForm(FlaskForm):
    """
    Login From
    """

    email = EmailField(u"Email", validators=[DataRequired(), Length(min=3, max=128)])
    password = PasswordField(u"Password", validators=[DataRequired(), Length(min=3, max=80)])
    remember_me = BooleanField(u"Remember Me")
    submit = SubmitField(u"Login")