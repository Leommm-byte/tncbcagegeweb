from website import db
from datetime import datetime, date
from flask_login import UserMixin

class Events(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), index=True, unique=True, nullable=False)
    description = db.Column(db.Text(), index=True, nullable=False)
    date = db.Column(db.Date)
    time = db.Column(db.Time)
    location = db.Column(db.String(256))
    

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    # email_id = db.Column(db.String(100), index=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

