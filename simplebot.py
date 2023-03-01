from pyrogram import Client, filters, idle

# Create a new Pyrogram client instance
app = Client(
    "my_bot",
    bot_token="", 
    api_id=12345,
    api_hash="0123456789abcdef0123456789abcdef"
)

# Define a handler for the /start command
@app.on_message(filters.command("start", prefixes="/"))
def start_command(client, message):
    client.send_message(message.chat.id, "Hi! I'm a simple bot. Nice to meet you! I do nothing!!🙂😂")

# Start the client
app.run()
idle() 
