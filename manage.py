from flask_migrate import Migrate

from app import app, database
from models import *  # noqa: F401 F403

migrate = Migrate(app, database)
