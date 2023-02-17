import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

EASYSKY_API_KEY = 'your_easysky_api_key'
TELEGRAM_BOT_TOKEN = 'your_telegram_bot_token'
TELEGRAM_API_ID = 'your_telegram_api_id'
TELEGRAM_API_HASH = 'your_telegram_api_hash'

def shorten_url(long_url):
    url = f'https://easysky.in/api/shorten?url={long_url}&apikey={EASYSKY_API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['shortenedUrl']
    else:
        return None

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hi! Send me a URL and I will shorten it for you.')

def shorten(update: Update, context: CallbackContext) -> None:
    long_url = update.message.text
    shortened_url = shorten_url(long_url)
    if shortened_url is not None:
        update.message.reply_text(shortened_url)
    else:
        update.message.reply_text('Sorry, an error occurred while shortening the URL.')

def main() -> None:
    updater = Updater(TELEGRAM_BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("shorten", shorten))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
