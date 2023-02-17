import telegram
from telegram.ext import CommandHandler, MessageHandler, Filters, Updater

# Set up Telegram bot client
bot = telegram.Bot(token="5815404727:AAGeLb-faQDcZYhkbI32VMof3upWR0YB2bc")
updater = Updater(token="5815404727:AAGeLb-faQDcZYhkbI32VMof3upWR0YB2bc")
dispatcher = updater.dispatcher

# Define function to handle incoming messages
def mute_user(update, context):
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id
    if update.message.text == "/mute":
        context.bot.restrict_chat_member(chat_id=chat_id, user_id=user_id, until_date=2147483647)
        context.bot.send_message(chat_id=chat_id, text="You have been muted in this group.")
    elif update.message.text == "/unmute":
        context.bot.restrict_chat_member(chat_id=chat_id, user_id=user_id, until_date=0)
        context.bot.send_message(chat_id=chat_id, text="You have been unmuted in this group.")
    elif update.message.text.startswith("/ban"):
        try:
            user_id = update.message.text.split()[1]
            context.bot.kick_chat_member(chat_id=chat_id, user_id=user_id)
            context.bot.send_message(chat_id=chat_id, text="User has been banned from the group.")
        except:
            context.bot.send_message(chat_id=chat_id, text="Please specify a user to ban.")
    elif update.message.text.startswith("/unban"):
        try:
            user_id = update.message.text.split()[1]
            context.bot.unban_chat_member(chat_id=chat_id, user_id=user_id)
            context.bot.send_message(chat_id=chat_id, text="User has been unbanned from the group.")
        except:
            context.bot.send_message(chat_id=chat_id, text="Please specify a user to unban.")
    elif update.message.text == "/help":
        help_text = "Available commands:\n/mute - mute yourself in the group\n/unmute - unmute yourself in the group\n/ban [user_id] - ban a user from the group\n/unban [user_id] - unban a user from the group\n/help - display this help message"
        context.bot.send_message(chat_id=chat_id, text=help_text)
    else:
        context.bot.send_message(chat_id=chat_id, text="I don't understand that command.")

# Set up command handlers
mute_handler = CommandHandler("mute", mute_user)
unmute_handler = CommandHandler("unmute", mute_user)
ban_handler = CommandHandler("ban", mute_user)
unban_handler = CommandHandler("unban", mute_user)
help_handler = CommandHandler("help", mute_user)
dispatcher.add_handler(mute_handler)
dispatcher.add_handler(unmute_handler)
dispatcher.add_handler(ban_handler)
dispatcher.add_handler(unban_handler)
dispatcher.add_handler(help_handler)

# Start the Telegram bot
updater.start_polling()
