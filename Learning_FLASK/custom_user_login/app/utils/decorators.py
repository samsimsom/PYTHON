

from functools import wraps
from flask import g, request, redirect, url_for


# FIXME:
# TODO: Login sonrasi yonlendirme!
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user is None:
            return redirect(url_for('auth.login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function
