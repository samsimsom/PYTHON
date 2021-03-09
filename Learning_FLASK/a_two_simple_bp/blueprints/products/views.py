

from flask import Blueprint, render_template

product = Blueprint('product', __name__,
                    template_folder='templates',
                    url_prefix='/product')


@product.route('/')
def index():
    return render_template('product/index.html')


@product.route('/list-of-clothes')
def list_of_clothes():
    return render_template('product/clothes.html')


@product.route('/list-of-shoes')
def list_of_shoes():
    return render_template('product/clothes.html')