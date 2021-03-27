

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    title = 'Main'
    return render_template('index.html',
                           title=title)


@app.route('/todo', methods=['GET', 'POST'])
def todo():
    title = 'ToDo'

    return render_template('/todo.html',
                           title=title)


if __name__ == '__main__':
    app.run()
