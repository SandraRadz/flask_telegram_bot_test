import time

from flask import request, Flask
from flask_migrate import MigrateCommand, Migrate
from flask_script import Manager
import telebot

from app import create_app
from app.models import Number, User, db, user_to_db


# app = Flask(__name__)
app = create_app()
db.init_app(app)

manager = Manager(app)
manager.add_command('db', MigrateCommand)
migrate = Migrate(app, db)

token = "984967282:AAH2oy2_VNrUQefzJ9LNCXd2muikSFLPCQU"
secret = 'sdfn3kglf8dfdfg7sdfs8d'
url = 'https://SandraRadz.pythonanywhere.com/' + secret

bot = telebot.TeleBot(token, threaded=False)
bot.remove_webhook()
# time.sleep(1)
bot.set_webhook(url=url)

@app.route('/{}'.format(secret), methods=["POST"])
def webhook():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    print("Message")
    return "ok", 200


@bot.message_handler(commands=['start'])
def start(message):
    print("here")
    user_to_db(message.from_user.id)
    bot.send_message(message.chat.id, 'Привет, ' + message.from_user.first_name + " " + message.from_user.last_name)


if __name__ == '__main__':
    manager.run()
