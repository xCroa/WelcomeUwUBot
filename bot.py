import logging
from telegram import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler
from telegram.utils import helpers
import os




# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
TOKEN = '1023777751:AAE6YfdkFZH9rQgEQC1mAc-0YUWzMlXmw6E'
PORT = int(os.environ.get('PORT', 5000))

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):    
    update.message.reply_text('Este bot envia um gif de bem vindo quando o grupo ganha novos integrantes!')
    print(os.environ)

def echo(update, context):    
    bot = context.bot
    url = '(https://i.imgur.com/lw7Z1mL.mp4)'#helpers.create_deep_linked_url(bot.get_me().username, USING_ENTITIES)        
    user_id_mention = '(tg://user?id=' + str(update.message.new_chat_members[0].id) + ')'
    text = 'Welcome, ['+ update.message.new_chat_members[0].first_name +']' + user_id_mention + ', [UwU]' + url + '!'
    update.message.reply_text(text, parse_mode=ParseMode.MARKDOWN)    

def main():
    #"""Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))    

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, echo))

    # Start the Bot
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook('https://welcomeuwubot.herokuapp.com/' + TOKEN)

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()