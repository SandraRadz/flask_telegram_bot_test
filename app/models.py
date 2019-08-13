from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Number(db.Model):
    __tablename__ = "numbers"
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(15))


def number_to_db(number):
    try:
        num_bd = Number(number=number)
        db.session.add(num_bd)
        db.session.commit()
    except:
        print("error")


