from pyrogram import Client, filters

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

import os

import asyncio

from plugins.teletips_t import *

from pyrogram.errors import FloodWait, MessageNotModified

from pyrogram.raw.functions.messages import UpdatePinnedMessage

bot=Client(

    "Countdown-TeLeTiPs",

    api_id = int(os.environ["API_ID"]),

    api_hash = os.environ["API_HASH"],

    bot_token = os.environ["BOT_TOKEN"]

)

footer_message = os.environ["FOOTER_MESSAGE"]

stoptimer = False

TELETIPS_MAIN_MENU_BUTTONS = [

            [

                InlineKeyboardButton('❓ HELP', callback_data="HELP_CALLBACK")

            ],

            [

                InlineKeyboardButton('👥 SUPPORT', callback_data="GROUP_CALLBACK"),

                InlineKeyboardButton('📣 CHANNEL', url='https://t.me/little_little_hackur'),

                InlineKeyboardButton('👨‍💻 CREATOR', url='https://t.me/little_little_hackur')

            ],

            [

                InlineKeyboardButton('➕ CREATE YOUR BOT ➕', callback_data="TUTORIAL_CALLBACK")

            ]

        ]

@bot.on_message(filters.command(['start','help']) & filters.private)

async def start(client, message):

    text = START_TEXT

    reply_markup = InlineKeyboardMarkup(TELETIPS_MAIN_MENU_BUTTONS)

    await message.reply(

        text=text,

        reply_markup=reply_markup,

        disable_web_page_preview=True

    )

@bot.on_callback_query()

async def callback_query(client: Client, query: CallbackQuery):

    if query.data=="HELP_CALLBACK":

        TELETIPS_HELP_BUTTONS = [

            [

                InlineKeyboardButton("⬅️ BACK", callback_data="START_CALLBACK")

            ]

            ]

        reply_markup = InlineKeyboardMarkup(TELETIPS_HELP_BUTTONS)

        try:

            await query.edit_message_text(

                HELP_TEXT,

                reply_markup=reply_markup

            )

        except MessageNotModified:

            pass

    elif query.data=="GROUP_CALLBACK":

        TELETIPS_GROUP_BUTTONS = [

            [

                InlineKeyboardButton("🎬👻", url="https://t.me/little_little_hackur")

            ],

            [

                InlineKeyboardButton("⬅️ BACK", callback_data="START_CALLBACK"),

            ]

            ]

        reply_markup = InlineKeyboardMarkup(TELETIPS_GROUP_BUTTONS)

        try:

            await query.edit_message_text(

                GROUP_TEXT,

                reply_markup=reply_markup

            )

        except MessageNotModified:

            pass    

    elif query.data=="TUTORIAL_CALLBACK":

        TELETIPS_TUTORIAL_BUTTONS = [

            [

                InlineKeyboardButton("soon", url="https://youtube.com/@KunalG93")

            ],

            [

                InlineKeyboardButton("⬅️ BACK", callback_data="START_CALLBACK"),

            ]

            ]

        reply_markup = InlineKeyboardMarkup(TELETIPS_TUTORIAL_BUTTONS)

        try:

            await query.edit_message_text(

                TUTORIAL_TEXT,

                reply_markup=reply_markup

            )

        except MessageNotModified:

            pass      

          

    elif query.data=="START_CALLBACK":

        TELETIPS_START_BUTTONS = [

            [

                InlineKeyboardButton('❓ HELP', callback_data="HELP_CALLBACK")

            ],

            [

                InlineKeyboardButton('👥 SUPPORT', callback_data="GROUP_CALLBACK"),

                InlineKeyboardButton('📣 CHANNEL', url='https://t.me/teletipsofficialchannel'),

                InlineKeyboardButton('👨‍💻 CREATOR', url='https://t.me/teIetips')

            ],

            [

                InlineKeyboardButton('➕ CREATE YOUR BOT ➕', callback_data="TUTORIAL_CALLBACK")

            ]

        ]

        reply_markup = InlineKeyboardMarkup(TELETIPS_START_BUTTONS)

        try:

            await query.edit_message_text(

                START_TEXT,

                reply_markup=reply_markup

            )

        except MessageNotModified:

            pass    

@bot.on_message(filters.command('set'))

async def set_timer(client, message):

    global stoptimer

    try:

        if message.chat.id>0:

            return await message.reply('⛔️ Try this command in a **group chat**.')

        elif not (await client.get_chat_member(message.chat.id,message.from_user.id)).privileges:

            return await message.reply('👮🏻‍♂️ Sorry, **only admins** can execute this command.')    

        elif len(message.command)<3:

            return await message.reply('❌ **Incorrect format.**\n\n✅ Format should be like,\n<code> /set seconds "event"</code>\n\n**Example**:\n <code>/set 10 "10 seconds countdown"</code>')    

        else:

            user_input_time = int(message.command[1])

            user_input_event = str(message.command[2])

            get_user_input_time = await bot.send_message(message.chat.id, user_input_time)

            await get_user_input_time.pin()

            if stoptimer: stoptimer = False

            if 0<user_input_time<=10:

                while user_input_time and not stoptimer:

                    s=user_input_time%60

                    Countdown_TeLe_TiPs='{}\n\n⏳ {:02d}**s**\n\n<i>{}</i>'.format(user_input_event, s, footer_message)

                    finish_countdown = await get_user_input_time.edit(Countdown_TeLe_TiPs)

                    await asyncio.sleep(1)

                    user_input_time -=1

                await finish_countdown.edit("🚨 Beep! Beep!! **TIME'S UP!!!**")

            elif 10<user_input_time<60:

                while user_input_time>0 and not stoptimer:

                    s=user_input_time%60

                    Countdown_TeLe_TiPs='{}\n\n⏳ {:02d}**s**\n\n<i>{}</i>'.format(user_input_event, s, footer_message)   

                    finish_countdown = await get_user_input_time.edit(Countdown_TeLe_TiPs)

                    await asyncio.sleep(3)

                    user_input_time -=3

                await finish_countdown.edit("🚨 Beep! Beep!! **TIME'S UP!!!**")

            elif 60<=user_input_time<3600:

                while user_input_time>0 and not stoptimer:

                    m=user_input_time%3600//60

                    s=user_input_time%60

                    Countdown_TeLe_TiPs='{}\n\n⏳ {:02d}**m** : {:02d}**s**\n\n<i>{}</i>'.format(user_input_event, m, s, footer_message)

                    finish_countdown = await get_user_input_time.edit(Countdown_TeLe_TiPs)

                    await asyncio.sleep(3)

                    user_input_time -=3

                await finish_countdown.edit("🚨 Beep! Beep!! **TIME'S UP!!!**")

            elif 3600<=user_input_time<86400:

                while user_input_time>0 and not stoptimer:

                    h=user_input_time%(3600*24)//3600

                    m=user_input_time%3600//60

                    s=user_input_time%60

                    Countdown_TeLe_TiPs='{}\n\n⏳ {:02d}**h** : {:02d}**m** : {:02d}**s**\n\n<i>{}</i>'.format(user_input_event, h, m, s, footer_message)

                    finish_countdown = await get_user_input_time.edit(Countdown_TeLe_TiPs)

                    await asyncio.sleep(7)

                    user_input_time -=7

                await finish_countdown.edit("🚨 Beep! Beep!! **TIME'S UP!!!**")

            elif user_input_time>=86400:

                while user_input_time>0 and not stoptimer:

                    d=user_input_time//(3600*24)

                    h=user_input_time%(3600*24)//3600

                    m=user_input_time%3600//60

                    s=user_input_time%60

                    Countdown_TeLe_TiPs='{}\n\n⏳ {:02d}**d** : {:02d}**h** : {:02d}**m** : {:02d}**s**\n\n<i>{}</i>'.format(user_input_event, d, h, m, s, footer_message)

                    finish_countdown = await get_user_input_time.edit(Countdown_TeLe_TiPs)

                    await asyncio.sleep(9)

                    user_input_time -=9

                await finish_countdown.edit("🚨 Beep! Beep!! **TIME'S UP!!!**")

            else:

                await get_user_input_time.edit(f"🤷🏻‍♂️ I can't countdown from {user_input_time}")

                await get_user_input_time.unpin()

    except FloodWait as e:

        await asyncio.sleep(e.value)

@bot.on_message(filters.command('stopc'))

async def stop_timer(Client, message):

    global stoptimer

    try:

        if (await bot.get_chat_member(message.chat.id,message.from_user.id)).privileges:

            stoptimer = True

            await message.reply('🛑 Countdown stopped.')

        else:

            await message.reply('👮🏻‍♂️ Sorry, **only admins** can execute this command.')

    except FloodWait as e:

        await asyncio.sleep(e.value)

print("Countdown Timer is alive!")

bot.run()
