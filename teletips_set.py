import os
import pyrogram
import requests

TOKEN = os.environ.get("BOT_TOKEN")
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")

app = pyrogram.Client(
    "link_shorten_bot",
    bot_token=TOKEN,
    api_id=API_ID,
    api_hash=API_HASH
)


@app.on_message(pyrogram.filters.command("start"))
def start(client, message):
    message.reply_text(
        "Hi! I'm a link shortener bot. Send me a URL and I'll shorten it for you."
    )


@app.on_message(pyrogram.filters.command("help"))
def help(client, message):
    message.reply_text(
        "To shorten a link, simply send me a message with the URL you want to shorten."
    )


@app.on_message(pyrogram.filters.regex(r"https?://[^\s]+"))
def shorten(client, message):
    url = message.text
    response = requests.post("https://easysky.in/api/create", data={"url": url})
    if response.status_code == 200:
        shortened_url = response.json().get("result").get("short_link")
        message.reply_text(shortened_url)
    else:
        message.reply_text("Sorry, an error occurred while trying to shorten the link.")


app.run()
