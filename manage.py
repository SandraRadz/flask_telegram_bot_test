from flask import request
from flask_migrate import MigrateCommand, Migrate
from flask_script import Manager
import telebot

from app import create_app
from app.models import Number, db


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



@bot.callback_query_handler(func=lambda call: True)
def longname(call):
    bot.send_message("-1001439919350", text=call.data)
    bot.delete_message("-1001439919350", call.message.message_id)

if __name__ == '__main__':
    manager.run()
