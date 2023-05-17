from .database import db

class Data(db.Model):
    __tablename__ = 'data'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)