import requests
import json
import os

url = "https://api.groupme.com/v3/groups?token=4RBEXfcfeke2TByTMwviZJQDo7ebLuwTr2puwiLe"
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


if response['name'] != 'Safety Bot Test':
    msg = '{}, you sent "{}".'.format(data['name'], data['text'])
    send_message(msg)
