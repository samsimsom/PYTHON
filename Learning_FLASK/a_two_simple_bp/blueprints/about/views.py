

from flask import Blueprint, render_template

about = Blueprint('about', __name__,
                  template_folder='templates',
                  url_prefix='/about')


@about.route('/')
def index():
    return render_template("about/index.html")
