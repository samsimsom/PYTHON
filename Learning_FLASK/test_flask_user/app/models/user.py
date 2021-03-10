

from flask_user import UserMixin
from app.extensions.database import db


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)

    # User Authentication fields
    email = db.Column(db.String(255), nullable=False, unique=True)
    email_confirmed_at = db.Column(db.DateTime())
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)

    # User information
    first_name = db.Column(db.String(100, collation='NOCASE'),
                           nullable=False,
                           server_default='')
    last_name = db.Column(db.String(100, collation='NOCASE'),
                          nullable=False,
                          server_default='')

    # Define the relationship to Role via UserRoles
    roles = db.relationship('Role', secondary='user_roles')

    def is_enabled(self):
        return True


# Define the Role data-model
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)


# Define the UserRoles association table
class UserRoles(db.Model):
    __tablename__ = 'user_roles'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id',
                                                    ondelete='CASCADE'))
    role_id = db.Column(db.Integer(), db.ForeignKey('roles.id',
                                                    ondelete='CASCADE'))
