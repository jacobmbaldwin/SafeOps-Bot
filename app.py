import requests
import json
import os


def send_message(msg):
    bot_url = 'https://api.groupme.com/v3/bots/post'

    data = {
        'bot_id': os.getenv('GROUPME_BOT_ID'),
        'text': msg
    }
    return requests.post(bot_url, json=data)


def main():
    API_KEY = os.getenv('API_KEY')
    url = f"https://api.groupme.com/v3/groups?token={API_KEY}"
    response = requests.get(url)
    data = response.json()
    print(response.status_code)
    # print(data)

    response_list = data['response']
    first_item = response_list[0]
    print('First Item: ', first_item)
    botTestGroup = first_item['group_id']
    print(botTestGroup)

    # if first_item['messages']['preview']['nickname'] != 'Safety Bot Test':
    #     msg = '{}, you sent "{}".'.format(first_item['messages']['preview']['nickname'],
    #                                       first_item['messages']['preview']['text'])
    #     send_message(msg)

    if first_item['messages']['preview']['text'] == '!help':
        msg = 'Only God can help the likes of you, son.'
        return send_message(msg)

    if first_item['messages']['preview']['text'] == '!jake':
        msg = 'Jake is a great guy. Should probably stay off that ankle, tho...'
        return send_message(msg)
    

main()
