from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from Kunal import app


@app.on_message(filters.command(["imdb", "tmdb"]))
async def imdb(_, message):
    if len(message.command) < 2:
        return await message.reply_text("Give me some Movie Name\n\nEx. `/imdb Kgf`")
    text = (
        message.text.split(None, 1)[1]
        if len(message.command) < 3
        else message.text.split(None, 1)[1].replace(" ", "%20")
    )
    url = message.get(f"https://api.safone.me/tmdb?query={text}").json()["results"][0]
    await message.reply_photo(
        photo=url["poster"],
        caption=f"""**IMDB Movie Details :**
**Title :** {url["title"]}
**Description :** {url["overview"]}
**Rating :** {url["rating"]}
**Release-Date :** {url["releaseDate"]}
**Popularity :** {url["popularity"]}
**Runtime :** {url["runtime"]}
**Status :** {url["status"]}
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="IMDB Link",
                        url=url["imdbLink"],
                    ),
                ],
            ],
        ),
    )

