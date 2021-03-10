

from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'info.cgsource@gmail.com'
app.config['MAIL_PASSWORD'] = 'zskehcijholkqzqz'

mail = Mail(app)


@app.route('/')
def index():
    return 'index'


@app.route('/mail')
def send_mail():
    msg = Message("Hello",
                  sender="info.cgsource@gmail.com",
                  recipients=["samsimsom@gmail.com"])
    msg.body = "testing"
    msg.html = "<b>testing</b>"
    mail.send(msg)
    return 'mail sending...'
