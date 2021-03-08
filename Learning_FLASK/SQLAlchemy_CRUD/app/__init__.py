

from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_moment import Moment
from config import Config


app = Flask(__name__)
app.config.from_object(Config)

csrf = CSRFProtect(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
moment = Moment(app)


from app import routes, models
