from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

DSApp = Flask(__name__)
DSApp.config.from_object(Config)
db = SQLAlchemy(DSApp)
migrate = Migrate(DSApp, db)

from DSApp import routes, models
