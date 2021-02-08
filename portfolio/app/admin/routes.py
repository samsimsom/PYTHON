#///////////////////////////////////////////////////////
# ADMIN // routes.py
#///////////////////////////////////////////////////////

from flask import render_template
from app.admin import bp


'''------------------------------------------------------------------'''
# ADMIN / DASHBOARD
@bp.route('/', methods=['GET', 'POST'])
def dashboard():

    title = 'admin panel'

    return render_template('admin/dashboard.html',
                            title=title)


'''------------------------------------------------------------------'''
# ADMIN / PORTFOLIO / NEW POST
@bp.route('/portfolio/new_post/', methods=['GET', 'POST'])
def new_post():

    title = 'new post'

    return render_template('portfolio/new_post.html',
                            title=title)


'''------------------------------------------------------------------'''
# ADMIN / PORTFOLIO / EDIT POST
@bp.route('/portfolio/edit_post/', methods=['GET', 'POST'])
def edit_post():

    title = 'edit post'

    return render_template('portfolio/edit_post.html',
                            title=title)