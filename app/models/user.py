from ..extensions import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))    
    login = db.Column(db.String(50))
    avatar = db.Column(db.String(200))
    password = db.Column(db.String(200))
    date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(50))
    