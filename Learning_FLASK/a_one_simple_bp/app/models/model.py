

from app.extensions.sqlalchemy import db


class Model(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    parameter = db.Column(db.Text, nullable=False)
    email = db.Column(db.String(120), index=True, unique=True)
    first_name = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f"Parameter model: {self.parameter}, created at {self.date_created}"
