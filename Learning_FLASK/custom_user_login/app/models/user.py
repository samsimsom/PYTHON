

from hashlib import md5
from werkzeug.security import (generate_password_hash,
                               check_password_hash)
from app.exts.database import db


class Role(db.Document):
    name = db.StringField(required=True, unique=True)


class User(db.Document):
    username = db.StringField(max_length=120, required=True, unique=True)
    email = db.StringField(max_length=120, required=True, unique=True)
    password_hash = db.StringField(max_length=128, required=True)
    role = db.ReferenceField(Role, reverse_delete_rule=db.CASCADE)

    meta = {'collection': 'user', 'indexes': ['username', 'email']}

    def __repr__(self) -> str:
        return f'<User | username: {self.username}, email: {self.email}>'

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password) -> bool:
        return check_password_hash(self.password_hash, password)
