

from flask import render_template
from flask_login import login_required
from app.routes.user import user
from app.models.user import User


@user.route('/<username>')
@login_required
def profile(username):

    user = User.query.filter_by(username=username).first_or_404()

    return render_template('user/profile.html',
                           user=user)
