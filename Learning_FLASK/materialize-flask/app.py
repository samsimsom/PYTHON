
import os
from datetime import datetime
from flask import Flask, render_template
from flask_mongoengine import MongoEngine
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = MongoEngine(app)


class Tasks(db.Document):
    task = db.StringField(max_length=64, required=True)
    creation_date = db.DateTimeField(default=datetime.utcnow())

    meta = {'collection': 'tasks', 'indexes': ['task',
                                               '-creation_date']}

    def __repr__(self) -> str:
        return f'<Task: {self.task}, Date: {self.creation_date}>'


@app.route('/')
def index():
    title = 'Main'

    task = Tasks()
    task.task = 'Test Task'
    task.save()

    return render_template('index.html',
                           title=title)


@app.route('/todo', methods=['GET', 'POST'])
def todo():
    title = 'ToDo'

    return render_template('/todo.html',
                           title=title)


if __name__ == '__main__':
    app.run()
