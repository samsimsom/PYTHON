
from flask import render_template

from app.routes.todo import todo


@todo.route('/todo')
def index():
    title = 'Todo'
    return render_template('todo/index.html', title=title)
