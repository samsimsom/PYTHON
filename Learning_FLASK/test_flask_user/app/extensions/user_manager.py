

from flask_user import UserManager, SQLAlchemyAdapter
from app.extensions.database import db
from app.models.user import User

db_adapter = SQLAlchemyAdapter(db, User)
user_manager = UserManager(db_adapter)


def init_app(application,):
    user_manager.init_app(app=application)
