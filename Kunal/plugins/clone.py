from pyrogram import filters, Client
from Kunal import app, API_ID, API_HASH

@app.on_message(filters.private & filter.command("clone")) 
async def _(app, message):
    reply = await message.reply("This Command For Clone This Bot\nGo to bot father and send /clone <token>") 
    token = message.command [1]
    try:
        await reply.edit("Cloning Your Bot Please Wait.. ") 
        client= Client(name= "kunal", api_id= API_ID, api_hash= API_HASH, bot_token= token, in_memory=True, plugins=dict(root="Kunal/plugins"))
