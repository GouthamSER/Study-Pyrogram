from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import datetime

    

bot = Client(
    name = "Pyrogram Studiyng",
    api_id = "18979569",
    api_hash = "45db354387b8122bdf6c1b0beef93743",
    bot_token = "6228122908:AAEKGwokHIjvYsH6qgthcz5G-sOdL3Aq45o"
)

print("BOT STARTED")

START_TXT = """{}
HI  I am Goutham Ser Bot

This is MAde From Pyrogram and i am studying this language

All CopyRights TO Goutham Josh
 
@im_goutham_josh
"""

HELP_TXT="""
This is a studiying pyrogram bot
<u>developed by Profile Photo Ittekunavan</u>

"""

ABOUT_TXT="""
✯ Cʀᴇᴀᴛᴏʀ: Gᴏᴜᴛʜᴀᴍ Sᴇʀ
✯ Lɪʙʀᴀʀʏ: Pʏʀᴏɢʀᴀᴍ
✯ Lᴀɴɢᴜᴀɢᴇ: Pʏᴛʜᴏɴ 3
✯ Bᴏᴛ Sᴇʀᴠᴇʀ: RAILWAY
"""

@bot.on_message(filters.command("start"))
async def start(client, message):
    
    button= [[
    InlineKeyboardButton("HELP✨", callback_data="help"),
    InlineKeyboardButton('About', callback_data="about")
]]
    
    
    m=datetime.datetime.now()
    time=m.hour
    if time < 12:
        get="GoodMorning"
    elif time <16:
        get="Good Evening"
    else:
        get="Good Night"
    
    await message.reply_text(
        text=START_TXT.format(get,  message.from_user.mention),
        reply_markup=InlineKeyboardMarkup(button)
    )

@bot.on_callback_query()
async def start(client, msg):
    
    if msg.data == "start":
        await msg.message.edit(
            text=START_TXT,
            reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton("Help✨", callback_data="help"),
                InlineKeyboardButton("About", callback_data="about")
            ]]
            )
        )

    elif msg.data == "help":
        await msg.message.edit(
            text=HELP_TXT,
            reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton("Back", callback_data="start")
            ]]
            )
        )
    elif msg.data == "about":
        await msg.message.edit(
            text=ABOUT_TXT,
            reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton('Back', callback_data="start")
            ]]
            )
        )


@bot.on_message(filters.command("help"))
async def help(client, message):
    await message.reply_text(
        text=HELP_TXT
    )
    
@bot.on_message(filters.command("about"))
async def about(client, message):
    await message.reply_text(
        text=ABOUT_TXT
    )
    
@bot.on_message(filters.command("id"))
async def idgroup(client, msg):
    text=f"""
    Title : {msg.chat.title}
User Name : <code> @{msg.from_user.username} </code>
Your ID : <code> {msg.from_user.id} </code>
Group ID : <code> {msg.chat.id} </code>
"""
    await msg.reply_text(text=text)


bot.run()
