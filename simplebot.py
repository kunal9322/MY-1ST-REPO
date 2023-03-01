from pyrogram import Client, filters, idle

# Create a new Pyrogram client instance
app = Client(
    "my_bot",
    bot_token="6295293651:AAHmKMz1hIyZSu5ERf-d1rzdjpVE7V-JFdw", 
    api_id=16743442,
    api_hash="12bbd720f4097ba7713c5e40a11dfd2a"
)

# Define a handler for the /start command
@app.on_message(filters.command("start", prefixes="/"))
def start_command(client, message):
    client.send_message(message.chat.id, "Hi! I'm a simple bot. Nice to meet you! I do nothing!!🙂😂")

# Start the client
app.run()
idle() 
