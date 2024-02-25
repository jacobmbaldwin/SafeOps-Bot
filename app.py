import os
import json
import requests

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import FLask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def webhook():
    data = request.get_json()

    if data['name'] != 'Safety Bot Test':
        msg = '{}, you sent "{}".'.format(data['name'], data['text'])
        send_message(msg)

    return "ok", 200


def send_message(msg):
    url = 'https://api.groupme.com/v3/bots/post'

    data = {
        'bot_id': os.getenv('GROUPME_BOT_ID'),
        'text': msg,
    }
    response = requests.post(url, json=data)
    x = urlopen(response).read().decode()
