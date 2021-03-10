

from flask_login import LoginManager

login = LoginManager()
login.login_view = 'auth.login'
login.login_message = 'Please log in to access this page.'


def init_app(application):
    login.init_app(app=application)
