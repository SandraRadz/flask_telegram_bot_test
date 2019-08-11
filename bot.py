import telebot

from app.models import user_to_db

bot = telebot.TeleBot("984967282:AAH2oy2_VNrUQefzJ9LNCXd2muikSFLPCQU")


@bot.message_handler(commands=['start'])
def start(message):
    user_to_db(message.from_user.id)
    bot.send_message(message.chat.id, 'Привет, ' + message.from_user.first_name + " " + message.from_user.last_name)

