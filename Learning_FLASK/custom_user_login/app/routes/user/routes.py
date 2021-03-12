

from flask import render_template
from app.routes.user import user
from app.utils.decorators import login_required


@user.route('/<username>')
@login_required
def profile(username):
    return render_template('user/profile.html')
