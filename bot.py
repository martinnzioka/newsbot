import telebot
import requests
from telegram.ext import Updater, CommandHandler
import json

bot_token = '801181582:AAH1l-ObFWI8jOCj5XLqNW6hCdQ4k4lL0Ys'

updater = Updater(bot_token)

api_key = 'https://api.nytimes.com/svc/news/v3/content/all/business.json?api-key=iSGhSpHqogB4GVxC6hWBHCIQ6F3e4mp4'

#data handle module.
#start
response = requests.get(api_key)
raw_data = response.text #coverting into text format
data = json.loads(raw_data) # converting JSON data to python dict.
article = data['results'] # making article an object to be used in data manipulation

#data manipulation.
def auto_refresh():
    while 1: #auto refreshing logic
        for message in article: #if message  'business': #to make sure the article doesn't repeat and add more content.

            print(message['section'], "\n")
            print(message['title'], "\n")
            print(message['abstract'], "\n")
            print(message['url'], "\n")
            print(message['byline'], "\n")

        time.sleep(30)

    return True

def news(bot, update):

        update.message.reply_text('Latest news for you {}'.format(update.message.from_user.first_name))
#end


updater.dispatcher.add_handler(CommandHandler('latest news', news))


print(response) #to show on the server side, API is running well.



updater.start_polling()

updater.idle()
