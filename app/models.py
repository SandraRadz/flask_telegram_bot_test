from app import db

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)


class Number(db.Model):
    __tablename__ = "numbers"
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Numeric, nullable=False)


def user_to_db(user):
    try:
        user_id = User(user_id=user)
        db.session.add(user_id)
        db.session.commit()
        print("OK")
    except:
        print("error. Maybe user already in db")


def number_to_db(number):
    try:
        num_bd = Number(number=number)
        db.session.add(num_bd)
        db.session.commit()
    except:
        print("error")
