import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from app.main import main_blueprint

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = os.environ.get('SECRET_KEY')

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/flask_test'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(main_blueprint)
    return app
