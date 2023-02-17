import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

EASYSKY_API_KEY = '26900f01070d5c9fcdd9ece883701597c9b302c1'
TELEGRAM_BOT_TOKEN = '5815404727:AAGeLb-faQDcZYhkbI32VMof3upWR0YB2bc'
TELEGRAM_API_ID = 16743442
TELEGRAM_API_HASH = '12bbd720f4097ba7713c5e40a11dfd2a'

def shorten_url(long_url, alias=None):
    url = f'https://easysky.in/api/shorten?url={long_url}&apikey={EASYSKY_API_KEY}'
    if alias:
        url += f'&custom={alias}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['shortenedUrl']
    else:
        return None

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hi! Send me a URL and I will shorten it for you.')

def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Commands:\n/start - Start the bot\n/shorten - Shorten a URL\n/stats - Get statistics\n/about - About the bot')

def shorten(update: Update, context: CallbackContext) -> None:
    args = context.args
    if len(args) == 0:
        update.message.reply_text('Please provide a URL to shorten.')
    else:
        long_url = args[0]
        alias = args[1] if len(args) > 1 else None
        shortened_url = shorten_url(long_url, alias)
        if shortened_url is not None:
            update.message.reply_text(shortened_url)
        else:
            update.message.reply_text('Sorry, an error occurred while shortening the URL.')

def stats(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Sorry, statistics are not available yet.')

def about(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('This bot was created by John Doe.')

def main() -> None:
    updater = Updater(TELEGRAM_BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("shorten", shorten))
    dispatcher.add_handler(CommandHandler("stats", stats))
    dispatcher.add_handler(CommandHandler("about", about))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
