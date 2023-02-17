import telegram
import requests
from telegram.ext import CommandHandler, Updater

# Set the Telegram API token and the easysky.in API credentials
TOKEN = '6105281766:AAHPNFllRa3kscRfeswDNO85_3NDxWYYp_0'
API_ID = '16743442'
API_HASH = '12bbd720f4097ba7713c5e40a11dfd2a'
API_ENDPOINT = 'https://easysky.in/26900f01070d5c9fcdd9ece883701597c9b302c1'

# Create the bot and add the command handlers
bot = telegram.Bot(token=TOKEN)
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Define the /start command handler
def start_handler(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to the URL shortener bot! Use /help to see the available commands.")

# Define the /help command handler
def help_handler(update, context):
    help_text = "Available commands:\n\n"
    help_text += "/start - Start the bot.\n"
    help_text += "/help - Show the available commands.\n"
    help_text += "/ping - Check if the bot is online.\n"
    help_text += "/shorten <url> - Shorten a URL using easysky.in."
    context.bot.send_message(chat_id=update.effective_chat.id, text=help_text)

# Define the /ping command handler
def ping_handler(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Pong!")

# Define the /shorten command handler
def shorten_handler(update, context):
    # Extract the URL from the command arguments
    args = context.args
    if len(args) == 0:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Please provide a URL to shorten.")
        return
    url = args[0]

    # Call the easysky.in API to shorten the URL
    params = {'api_id': API_ID, 'api_hash': API_HASH, 'url': url}
    response = requests.post(API_ENDPOINT, data=params)
    if response.status_code != 200:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Error shortening the URL.")
        return
    short_url = response.text

    # Send the shortened URL to the user
    context.bot.send_message(chat_id=update.effective_chat.id, text=short_url)

# Add the command handlers to the dispatcher
start_handler = CommandHandler('start', start_handler)
dispatcher.add_handler(start_handler)

help_handler = CommandHandler('help', help_handler)
dispatcher.add_handler(help_handler)

ping_handler = CommandHandler('ping', ping_handler)
dispatcher.add_handler(ping_handler)

shorten_handler = CommandHandler('shorten', shorten_handler)
dispatcher.add_handler(shorten_handler)

# Start the bot
updater.start_polling()
