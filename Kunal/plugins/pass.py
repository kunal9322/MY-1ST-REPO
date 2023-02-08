import random
from pyrogram import Client, filters
from Kunal import app, API_ID, API_HASH

@app.on_message(filters.private & filters.command("gen"))
async def gen_password(app, message):    
    reply = await message.reply('Processing...')    
    try:
        if len(message.text.split()) > 1:
            limit, keys = int(message.text.split()[0]), message.text.split()[1]
        else:
            keys = "abcdefghijklmnopqrstuvwxyz" + "1234567890" + "!@#$%^&*()_+".lower()
            limit = int(message.text)
    except:
        await message.edit_text('Something went wrong.')
        return    
    if limit > 100 or limit <= 0:
        text = "Sorry... Failed To Create Password, Because Limit is 1 to 100."
    else:
        random_value = "".join(random.sample(keys, limit))
        text = f"Limit :- {str(limit)}.\nPassword :- {random_value}\n\nDone."   
    await message.edit_text(text, True)
