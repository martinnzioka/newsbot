import telebot
import requests
import time
import json
import config  # This file helps us to hide our keys in a separate file, and use
               # .gitignore to prevent uploading it to github,
               # Make a config.py file and api_key = "", url = ""


# authenticating the telebot library way
bot = telebot.TeleBot(config.api_key)

# serialising our json format data and analysing how the Python dict is set up
# so that we extract what we need, in this case, section and url is enough.
r = requests.get(config.url)
r_text = r.text
request = json.loads(r_text)
data = request['results']

# Iterating to make sure we have the right thing...
# Later you can disable this, it will show in your console..
for item in data:
    print(item['section'])
    print(item['url'])
