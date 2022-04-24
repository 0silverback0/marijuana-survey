from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key= True)
    email = db.Column(db.Text, unique=True, nullable=False)
    smoker = db.Column(db.Text, nullable= False)
    started = db.Column(db.Text, nullable=False)
    frequency = db.Column(db.Text, nullable=False)
    reason = db.Column(db.Text, nullable=False)
    condition = db.Column(db.Text)
    type = db.Column(db.Text, nullable=False)