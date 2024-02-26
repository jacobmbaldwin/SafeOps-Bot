import requests
import json
import os
API_KEY = os.getenv('API_KEY')
url = f"https://api.groupme.com/v3/groups?token={API_KEY}"
response = requests.get(url)
data = response.json()
print(response.status_code)


def send_message(msg):
    bot_url = 'https://api.groupme.com/v3/bots/post'

    data = {
        'bot_id': os.getenv('GROUPME_BOT_ID'),
        'text': msg,
    }
    message = requests.post(url, json=data)


if data['name'] != 'Safety Bot Test':
    msg = '{}, you sent "{}".'.format(data['name'], data['text'])
    send_message(msg)
