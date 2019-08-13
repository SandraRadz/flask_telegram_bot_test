from flask import request
from flask_migrate import MigrateCommand, Migrate
from flask_script import Manager
import telebot

from app import create_app
from app.models import Number, db
import os


app = create_app()
db.init_app(app)


manager = Manager(app)
manager.add_command('db', MigrateCommand)
migrate = Migrate(app, db)

token = os.getenv("TOKEN")
secret = os.getenv("SECRET_KEY")
url = 'https://SandraRadz.pythonanywhere.com/' + secret

bot = telebot.TeleBot(token, threaded=False)
bot.remove_webhook()
bot.set_webhook(url=url)



@app.route('/{}'.format(secret), methods=["POST"])
def webhook():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    print("Message")
    return "ok", 200


@bot.callback_query_handler(func=lambda call: True)
def longname(call):
    bot.send_message(call.from_user.id, text=call.data)
    bot.delete_message("-1001439919350", call.message.message_id)

if __name__ == '__main__':
    manager.run()
