

from app.exts.database import db


class User(db.Document):
    username = db.StringField(max_length=120, required=True, unique=True)
    email = db.StringField(max_length=120, required=True, unique=True)
    password = db.StringField(max_length=120, required=True, unique=True)

    def __repr__(self) -> str:
        return f'<User | username: {self.username}, id: {self.id}, \
                 email: {self.email}>'
