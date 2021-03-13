

from flask import render_template
from app.routes.user import user    # Blueprint
from app.models.user import User
from app.utils.decorators import login_required


@user.route('/<username>')
@login_required
def profile(username):

    user = User.objects.get_or_404(username=username)

    return render_template('user/profile.html')
