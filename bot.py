from flask import Flask, request
import telepot
import time

try:
    from Queue import Queue
except ImportError:
    from queue import Queue

app = Flask(__name__)
TOKEN = '1023777751:AAE6YfdkFZH9rQgEQC1mAc-0YUWzMlXmw6E'#os.environ['PP_BOT_TOKEN']  # put your token in heroku app as environment variable
SECRET = '/bot' + TOKEN
URL = 'https://welcomeuwubot.herokuapp.com' #  paste the url of your application

UPDATE_QUEUE = Queue()
BOT = telepot.Bot(TOKEN)

def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    BOT.sendMessage(chat_id, 'hello!')

BOT.message_loop({'chat': on_chat_message}, source=UPDATE_QUEUE)  # take updates from queue

@app.route(SECRET, methods=['GET', 'POST'])
def pass_update():
    UPDATE_QUEUE.put(request.data)  # pass update to bot
    return 'OK'
    
while True:
    time.sleep(1000)

BOT.setWebhook(URL + SECRET) # unset if was set previously

