#///////////////////////////////////////////////////////
# PORTFOLIO // routes.py
#///////////////////////////////////////////////////////

from flask import render_template
from app.portfolio import bp


'''------------------------------------------------------------------'''
# PORTFOLIO / INDEX
@bp.route('/', methods=['GET', 'POST'])
def index():
    title = '3D Character Artist & Modeler'

    dummy_data = {
        'images':[
            'https://mdbootstrap.com/img/Photos/Others/image06.jpg',
            'https://mdbootstrap.com/img/Photos/Others/image008.jpg',
            'https://mdbootstrap.com/img/Photos/Others/image005.jpg',
            'https://mdbootstrap.com/img/Photos/Others/image010.jpg',
            'https://mdbootstrap.com/img/Photos/Others/image18.jpg',
            'https://mdbootstrap.com/img/Photos/Others/image17.jpg',
            'https://mdbootstrap.com/img/Photos/Others/image008.jpg',
            'https://mdbootstrap.com/img/Photos/Others/image02.jpg',
            'https://mdbootstrap.com/img/Photos/Others/image06.jpg',
            'https://mdbootstrap.com/img/Photos/Others/image008.jpg',
            'https://mdbootstrap.com/img/Photos/Others/image005.jpg',
            'https://mdbootstrap.com/img/Photos/Others/image010.jpg',
            'https://mdbootstrap.com/img/Photos/Others/food3.jpg',
            'https://mdbootstrap.com/img/Photos/Others/image010.jpg',
            'https://mdbootstrap.com/img/Photos/Others/image18.jpg',
            'https://mdbootstrap.com/img/Photos/Others/image06.jpg',
            'https://mdbootstrap.com/img/Photos/Others/image005.jpg',
            'https://mdbootstrap.com/img/Photos/Others/image18.jpg'
        ]
    }

    return render_template('portfolio/index.html',
                            title=title,
                            dummy_data=dummy_data)


'''------------------------------------------------------------------'''
# PORTFOLIO / SINGLE PAGE
@bp.route('/portfolio/<post_id>', methods=["GET", "POST"])
def single_page(post_id):
    title = "title"

    return render_template("portfolio/single_page.html",
                            title=title)