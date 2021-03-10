

from flask_mail import Mail

mail = Mail()


def init_app(application,):
    mail.init_app(app=application)
