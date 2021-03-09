

from flask import Blueprint, render_template

main = Blueprint('main', __name__,
                 template_folder='templates')


@main.route('/')
@main.route('/index')
def index():
    return render_template("main/index.html")
