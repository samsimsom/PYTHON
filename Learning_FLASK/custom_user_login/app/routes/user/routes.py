

from flask import render_template
from app.routes.user import user


@user.route('/<username>')
def profile(username):
    return render_template('user/profile.html')
