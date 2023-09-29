from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Events(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), index=True, unique=True, nullable=False)
    description = db.Column(db.Text(), index=True, nullable=False)
    date = db.Column(db.DateTime(timezone=True))
