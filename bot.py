import telepot

TOKEN_BOT = '1023777751:AAE6YfdkFZH9rQgEQC1mAc-0YUWzMlXmw6E'

bot = telepot.Bot(TOKEN_BOT)

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if 'new_chat_member' in msg:        
        new_user = msg['new_chat_member']['id']
        user_name = msg['new_chat_member']['first_name']
        inline_user_mention = '<a href="tg://user?id=' + str(new_user) +'">'+ user_name +'</a>'        
        senko_san_link = '<a href="https://i.imgur.com/lw7Z1mL.mp4">UwU</a>'        
        reply_text = 'Welcome, ' + inline_user_mention + ' ' + senko_san_link + '!!'

        bot.sendMessage(chat_id, reply_text, 'HTML', False, False, msg['message_id'])

bot.message_loop(handle)

while True:
    pass