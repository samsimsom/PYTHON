
from datetime import datetime

from app.exts.database import db


class Tasks(db.Document):
    task = db.StringField(max_length=64, required=True)
    creation_date = db.DateTimeField(default=datetime.utcnow())

    meta = {'collection': 'tasks', 'indexes': ['task',
                                               '-creation_date']}

    def __repr__(self) -> str:
        return f'<Task: {self.task}, Date: {self.creation_date}>'
