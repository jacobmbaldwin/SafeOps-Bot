import requests
import json

url = "https://api.groupme.com/v3/groups?token=4RBEXfcfeke2TByTMwviZJQDo7ebLuwTr2puwiLe"
response = requests.get(url)
print(response.status_code)


def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


# jprint(response.json())

botURL = "https://api.groupme.com/v3/bots/post"
botTestMessage = {
    "bot_id": "ddc1285520851d732617ead80d",
    "text": "This message is to test attachments.",
    "attachments":
        [{
            "type": "image",
            "url": "https://i.groupme.com/somethingsomething.large"
        }]
}

x = requests.post(botURL, json=botTestMessage)

print(x.text)
