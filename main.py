from pyrogram import Client, filters, idle

API_ID= int(16743442) 
API_HASH= "12bbd720f4097ba7713c5e40a11dfd2a"
BOT_TOKEN= "6105281766:AAHPNFllRa3kscRfeswDNO85_3NDxWYYp_0"

app= Client(name"kunal", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN, in_memory=True) 

#bot filter
@app.on_message(filters.command(["start", "shuru"]) & filters.private) 
async def _(app.message):
      await message.reply_text("Hello Bro") 

#starting the bot.. 

app.start() 
    idle() 
