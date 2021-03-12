

import os
import click
from app.exts.database import db
from app.models.user import User


def register(app):
    @app.cli.group()
    def database():
        """Database commands."""
        pass

    @database.command('drop-collection')
    def drop_colection():
        """Drop Collection"""
        User.drop_collection()
        print('All Users Record DELETED.')

    @database.command('register-user')
    @click.argument('username')
    @click.argument('email')
    @click.argument('password')
    def register_user(username, email, password):
        """Add New User"""
        u = User()
        u.username = username
        u.email = email
        u.password = u.set_password(password)
        u.save()

        print(f'User | {u.username} > document created.')

    @database.command('login-user')
    @click.argument('email')
    @click.argument('password')
    def login_user(email, password):
        """Login User"""
        u = User.objects.get(email=email)
        if (u is None) or not (u.check_password(password)):
            print('Invalid credentials.')
            return

        print('Login.')
