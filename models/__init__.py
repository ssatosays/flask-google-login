from datetime import datetime

from flask_login import UserMixin

from app import database as db


class User(UserMixin):
    def __init__(self, id_):
        self.id = id_


class Log(db.Model):
    __tablename__ = 'logs'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    update_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    comment = db.Column(db.String(255), nullable=False)
