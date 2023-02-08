from pyrogram import filters, Client

@Client.on_message(filters.command("help") & filters.private) 
async def _(app:Client, message):
      await message.reply_text("Hello Bro This is Help menu\n I am in now Developing Stage \ntype /clone <token> for clone this bot.. \n😎") 
