

import os
import click
from app.extensions.database import db


def register(app):
    @app.cli.group()
    def database():
        """Database commands."""
        pass

    @database.command('create')
    def create_db():
        """Create Databese"""
        db.create_all()
        print('Database created.')
