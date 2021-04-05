
from flask import render_template

from app.routes.main import main


@main.route('/', methods=['GET'])
def index():
    title = 'Main'
    return render_template('main/index.html', title=title)
