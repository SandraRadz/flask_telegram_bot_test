from flask_migrate import MigrateCommand, Migrate
from flask_script import Manager
import telebot
import request

from app import create_app
from app.models import Number, User, db
from bot import bot

app = create_app()
db.init_app(app)

manager = Manager(app)
manager.add_command('db', MigrateCommand)
migrate = Migrate(app, db)

secret = "GUID"
@app.route('/{}'.format(secret), methods=["POST"])
def webhook():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    print("Message")
    return "ok", 200

if __name__ == '__main__':
    manager.run()
