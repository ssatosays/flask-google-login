from flask_migrate import Migrate

from app import app, database
from models import *  # noqa: F403 F401

migrate = Migrate(app, database)
