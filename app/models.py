from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(15), unique=True)


class Number(db.Model):
    __tablename__ = "numbers"
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(15))


def user_to_db(user):
    try:
        user_id = User(user_id=user)
        db.session.add(user_id)
        db.session.commit()
    except:
        print("error")


def number_to_db(number):
    try:
        num_bd = Number(number=number)
        db.session.add(num_bd)
        db.session.commit()
    except:
        print("error")


def get_all_user_id():
    try:
        ids = db.session.query(User.user_id).all()
    except:
        print("error")
        return None
    return ids
