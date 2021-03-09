

from flask import Blueprint, render_template

contact = Blueprint('contact', __name__,
                    template_folder='templates',
                    url_prefix='/contact')


@contact.route('/')
def index():
    return render_template("contact/index.html")
