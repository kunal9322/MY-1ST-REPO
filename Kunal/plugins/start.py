from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@Client.on_message(filters.command(["start", "shuru","."]) & filters.private) 
async def _(app:Client, message):
      await message.reply_text("Hello Bro \n I am in now Developing Stage \ntype /clone for clone this bot.. \nfor more information type /help") 


reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Kunal",
                        
                    ),
                ],
            ],
        ),
