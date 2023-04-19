from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

# from .config import Config Add a config file later

app = Flask(__name__)

# Replace this with the database we choose
# app.config.from_object(Config)
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)

from . import routes
