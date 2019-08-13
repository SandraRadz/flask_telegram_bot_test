import requests
from flask import request, abort, jsonify, render_template, current_app
import telebot

from . import main_blueprint


@main_blueprint.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        number = request.form["number"]
        try:
            from app.models import number_to_db
            number_to_db(number)
        except:
            return abort(404)
        send_message_to_bot("Нове замовлення", "-1001439919350", number)
        return jsonify({'success': True}), 200, {'ContentType': 'application/json'}
    return render_template("base.html")


def send_message_to_bot(bot_message, bot_chatID, number):
    from manage import bot
    markup = telebot.types.InlineKeyboardMarkup()
    button = telebot.types.InlineKeyboardButton(text='Прийняти', callback_data=number)
    markup.add(button)
    bot.send_message(chat_id=bot_chatID, text=bot_message, reply_markup=markup)


