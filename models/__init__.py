from datetime import datetime

from flask_login import UserMixin

from app import database as db


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    update_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    sub = db.Column(db.Integer)

    def __init__(self, sub):
        self.sub = sub


class Log(db.Model):
    __tablename__ = 'logs'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    update_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    comment = db.Column(db.String(255), nullable=False)
