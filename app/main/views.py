import requests
from flask import request, abort, jsonify, render_template

from . import main_blueprint


@main_blueprint.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        number = request.form["number"]
        try:
            print("here")
            from app.models import number_to_db
            number_to_db(number)
            print("and here")
            client_arr = {""}
            #send_number_to_bot("Нове замовлення")
        except:
            return abort(404)
        return jsonify({'success': True}), 200, {'ContentType': 'application/json'}
    return render_template("base.html")


def send_number_to_bot(message, bot_chatID):
    bot_token = '984967282:AAH2oy2_VNrUQefzJ9LNCXd2muikSFLPCQU'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + message
    response = requests.get(send_text)
    return response.json()
