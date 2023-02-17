from pyrogram import Client, filters

# Set up Pyrogram client
app = Client("5815404727:AAGeLb-faQDcZYhkbI32VMof3upWR0YB2bc")

# Define function to handle incoming messages
@app.on_message(filters.command("mute"))
def mute_user(client, message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    client.restrict_chat_member(chat_id, user_id, until_date=2147483647)
    client.send_message(chat_id, "You have been muted in this group.")

@app.on_message(filters.command("unmute"))
def unmute_user(client, message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    client.restrict_chat_member(chat_id, user_id, until_date=0)
    client.send_message(chat_id, "You have been unmuted in this group.")

@app.on_message(filters.command("ban"))
def ban_user(client, message):
    chat_id = message.chat.id
    try:
        user_id = int(message.text.split()[1])
        client.kick_chat_member(chat_id, user_id)
        client.send_message(chat_id, "User has been banned from the group.")
    except:
        client.send_message(chat_id, "Please specify a user to ban.")

@app.on_message(filters.command("unban"))
def unban_user(client, message):
    chat_id = message.chat.id
    try:
        user_id = int(message.text.split()[1])
        client.unban_chat_member(chat_id, user_id)
        client.send_message(chat_id, "User has been unbanned from the group.")
    except:
        client.send_message(chat_id, "Please specify a user to unban.")

@app.on_message(filters.command("help"))
def help_message(client, message):
    help_text = "Available commands:\n/mute - mute yourself in the group\n/unmute - unmute yourself in the group\n/ban [user_id] - ban a user from the group\n/unban [user_id] - unban a user from the group\n/help - display this help message"
    client.send_message(message.chat.id, help_text)

# Start the Pyrogram client
app.run()
