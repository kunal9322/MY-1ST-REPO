import pyshorteners
from pyrogram import Client, filters
from pyrogram.types import Message

# Set up the easysky.in shortener
api_id = "16743442"
api_hash = "12bbd720f4097ba7713c5e40a11dfd2a"
shortener = pyshorteners.Shortener('easysky', api_key=f"{api_id}:{api_hash}")

# Set up the Pyrogram client
api_key = "26900f01070d5c9fcdd9ece883701597c9b302c1"
api_hash = "12bbd720f4097ba7713c5e40a11dfd2a"
bot_token = "5815404727:AAGeLb-faQDcZYhkbI32VMof3upWR0YB2bc"
app = Client("my_bot", api_id=api_key, api_hash=api_hash, bot_token=bot_token)

# Define a command handler for the "/shorten" command
@app.on_message(filters.command("shorten"))
def shorten_command_handler(client: Client, message: Message):
    # Get the link to be shortened from the user input
    original_link = message.text.split(" ", 1)[1]
    
    # Shorten the link using easysky.in
    short_link = shortener.short(original_link)
    
    # Send the shortened link to the user
    message.reply_text(short_link)

# Start the bot
app.run()
