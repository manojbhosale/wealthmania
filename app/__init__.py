from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import os

wealthApp = Flask(__name__)
wealthApp.config.from_object(Config)
db = SQLAlchemy(wealthApp)
migrate = Migrate(wealthApp, db)
login = LoginManager(wealthApp)
login.login_view = 'login'
wealthApp.config['UPLOAD_FOLDER']='static\\portfolios\\'
wealthApp.config['MAX_CONTENT_PATH']=1000
appPath=os.path.abspath(os.path.dirname(__file__))

from app import routes, models

