

import click
from flask import Blueprint
from database.database import db
from models.model import Model

commands = Blueprint('commands', __name__)


@commands.cli.command('create')
def create_db():
    """Creates database"""
    db.create_all()
    print('Database Created...')


@commands.cli.command('drop')
def drop_db():
    """Drop / Clean database"""
    db.drop_all()
    print('Database Droped All...')


@commands.cli.command('model')
def create_model_table():
    """Create table model in the database"""
    Model.__table__.create(db.engine)
    print('Table Created...')


@commands.cli.command('param')
@click.argument('param')
def create_a_record(param):
    """ Creates a record """
    record = Model(parameter=param)
    db.session.add(record)
    db.session.commit()
    print("Record created...")
