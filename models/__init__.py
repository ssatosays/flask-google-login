from datetime import datetime

from flask_login import UserMixin

from app import db


class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    update_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    sub = db.Column(db.Integer)
    email = db.Column(db.String(255), nullable=False)
    picture = db.Column(db.String(255), nullable=False)
    given_name = db.Column(db.String(255), nullable=False)

    def __init__(self, sub, email, picture, given_name):
        self.sub = sub
        self.email = email
        self.picture = picture
        self.given_name = given_name


class Log(db.Model):
    __tablename__ = "logs"

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    update_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    comment = db.Column(db.String(255), nullable=False)
