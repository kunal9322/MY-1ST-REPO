import random, os
from pyrogram import Client, filters
from Kunal import app, API_ID, API_HASH

@app.on_message(filters.private & filters.command("gen"))
async def _(app, message):    
    reply = await message.reply('`Processing...`')    
    try:
        if len(update.text.split()) > 1:
            keys, limit = update.text.split()[1], int(update.text.split()[0])
        else:
            keys = "abcdefghijklmnopqrstuvwxyz"+"1234567890"+"!@#$%^&*()_+".lower()
            limit = int(update.text)
    except:
        await message.edit_text('Something wrong')
        return    
    if limit > 100 or limit <= 0:
        text = "Sorry... Failed To Create Password, Because Limit is 1 to 100."
    else:
        random_value = "".join(random.sample(password, limit))
        text = f"**Limit :-** `{str(limit)}`.\n**Password :-** `{random_value}`**\n\ndone"   
    await message.edit_text(text, True)

