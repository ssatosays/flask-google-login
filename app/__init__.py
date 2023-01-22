from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("app_config")
database = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

from app.views import *  # noqa: E402 F401 F403
