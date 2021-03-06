import logging
from telegram import ParseMode
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler
import os




# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
TOKEN = os.environ['PP_BOT_TOKEN']
PORT = int(os.environ.get('PORT', 5000))
BOT_URL = os.environ['BOT_URL']

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):    
    update.message.reply_text('Este bot envia um gif de bem vindo quando o grupo ganha novos integrantes!')    

def echo(update, context):    
    bot = context.bot
    url = '(https://i.imgur.com/lw7Z1mL.mp4)'
    user_id_mention = '(tg://user?id=' + str(update.message.new_chat_members[0].id) + ')'
    text = 'Welcome, ['+ update.message.new_chat_members[0].first_name +']' + user_id_mention + ', [UwU]' + url + '!'
    update.message.reply_text(text, parse_mode=ParseMode.MARKDOWN)    

def welcomeCommand(update, context):
    bot = context.bot
    url = '(https://i.imgur.com/lw7Z1mL.mp4)'    
    text = '[UwU]' + url + '!'
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

    # on Welcome command
    dp.add_handler(CommandHandler("welcome", welcomeCommand))    

    # Start the Bot
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook(BOT_URL + TOKEN)

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()