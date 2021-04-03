
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app.exts.database import db


class User(db.Document):
    username = db.StringField(max_length=128)
    email = db.EmailField(max_length=128, required=True, unique=True)
    password_hash = db.StringField(max_length=128, required=True)
    creation_date = db.DateTimeField(default=datetime.utcnow())

    meta = {'collection': 'user', 'indexes': ['username',
                                              'email',
                                              '-creation_date']}

    def __repr__(self) -> str:
        return f'<User: username:{self.username}, emal:{self.email}>'

    def set_password(self, password) -> None:
        self.password_hash = generate_password_hash(password)

    def get_password(self, password) -> bool:
        return check_password_hash(self.password_hash, password)
