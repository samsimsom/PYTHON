

from flask import render_template
from app.routes.about import about


@about.route('/')
def index():
    return render_template('about/index.html')
