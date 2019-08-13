import os

from flask import Flask

from app.main import main_blueprint


def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://'+os.getenv("DB_USER")+':'+os.getenv("DB_PASSWORD")+'@SandraRadz.mysql.pythonanywhere-services.com/'+os.getenv("DB_NAME")
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://SandraRadz:rootroot@SandraRadz.mysql.pythonanywhere-services.com/SandraRadz$flask_test'

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    app.register_blueprint(main_blueprint)
    return app
