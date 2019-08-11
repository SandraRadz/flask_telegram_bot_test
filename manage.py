import os
import time

import telebot
from flask_migrate import MigrateCommand, Migrate
from flask_script import Manager

from app import create_app
from app.models import Number, User, db, user_to_db

app = create_app()
db.init_app(app)

manager = Manager(app)
manager.add_command('db', MigrateCommand)
migrate = Migrate(app, db)

bot = telebot.TeleBot("984967282:AAH2oy2_VNrUQefzJ9LNCXd2muikSFLPCQU", threaded=False)

bot.remove_webhook()
time.sleep(1)
bot.set_webhook(url="https://YOURNAME.pythonanywhere.com/{}".format(os.environ.get('SECRET_KEY')))


@bot.message_handler(commands=['start'])
def start(message):
    user_to_db(message.from_user.id)
    bot.send_message(message.chat.id, 'Привет, ' + message.from_user.first_name + " " + message.from_user.last_name)


if __name__ == '__main__':
    manager.run()
