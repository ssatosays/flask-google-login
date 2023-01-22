from flask_migrate import Migrate

from app import app, db
from models import *  # noqa: F401 F403

migrate = Migrate(app, db)
