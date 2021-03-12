

from flask import render_template

from app.routes.about import about    # Blueprint
from app.utils.decorators import login_required


@about.route('/')
@login_required
def index():
    return render_template('about/index.html')
