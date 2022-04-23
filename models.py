from enum import unique
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.Text, unique=True, nullable=False)
    ans = db.Column(db.Text, nullable= False)