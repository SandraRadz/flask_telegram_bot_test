import os
import telebot
from flask import Flask, render_template, request, jsonify
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy

bot = telebot.TeleBot("984967282:AAH2oy2_VNrUQefzJ9LNCXd2muikSFLPCQU")
app = Flask(__name__)
manager = Manager(app)
app.config["SECRET_KEY"] = os.environ.get('SECRET_KEY')
db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        number = request.form["number"]

        return jsonify({'success': True}), 200, {'ContentType': 'application/json'}
    return render_template("base.html")


if __name__ == '__main__':
    manager.run()
