

from flask import render_template
from flask_user import login_required, roles_required
from flask_mail import Message
from app.routes.main import main
from app.extensions.mail import mail


@main.route('/')
@login_required
def index():
    return render_template('main/index.html')


@main.route('/admin')
@roles_required('ADMIN')
def admin():
    return render_template('main/index.html')


@main.route('/mail')
def send_mail():

    msg = Message("Hello",
                  sender="from@example.com",
                  recipients=["to@example.com"])

    msg.body = "testing"
    mail.send(msg)

    return render_template('main/index.html')
