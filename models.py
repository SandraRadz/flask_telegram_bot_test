from app import db


class Number(db.Models):
    __tablename__ = "numbers"
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Numeric, nullable=False)
