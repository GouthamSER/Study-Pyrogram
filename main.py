from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

bot = Client(
    name = "Pyrogram Studiyng",
    api_id = "18979569",
    api_hash = "45db354387b8122bdf6c1b0beef93743",
    bot_token = "6228122908:AAEKGwokHIjvYsH6qgthcz5G-sOdL3Aq45o"
)

print("BOT STARTED")

button= [[
    InlineKeyboardButton("Owner", url=f't.me/wudixh13/4'),
    InlineKeyboardButton("Join", url=f't.me/wudixh')
]]

START_TXT = """
HI  I am Goutham Ser Bot
This is MAde For Studying Purpose ONly
All CopyRights TO Goutham Josh
 
@im_goutham_josh
"""

HELP_TXT="""
/demo = Show Detail of Account

"""

ABOUT_TXT="""
✯ Cʀᴇᴀᴛᴏʀ: Gᴏᴜᴛʜᴀᴍ Sᴇʀ
✯ Lɪʙʀᴀʀʏ: Pʏʀᴏɢʀᴀᴍ
✯ Lᴀɴɢᴜᴀɢᴇ: Pʏᴛʜᴏɴ 3
✯ Bᴏᴛ Sᴇʀᴠᴇʀ: RAILWAY
"""

@bot.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_photo(
        photo="https://telegra.ph/file/88435ada3fd2a838ccd59.jpg",
        caption=START_TXT,
        reply_markup=InlineKeyboardMarkup(button)
    )

@bot.on_message(filters.command("help"))
async def help(client, message):
    await message.reply_text(
        text=HELP_TXT
    )
    
@bot.on_message(filters.command("about"))
async def help(client, message):
    await message.reply_text(
        text=ABOUT_TXT
    )

@bot.on_message(filters.command("idpm"))
async def idpm(client, msg):
    text=f"""
    First Name : {msg.from_user.first_name}
Last Name : {msg.from_user.last_name}
User Name : <code> {msg.from_user.username} </code>
ID : <code> {msg.from_user.id} </code>
Mention : {msg.from_user.mention}
    """
    await msg.reply_text(text=text)
    
@bot.on_message(filters.command("idgroup"))
async def idgroup(client, msgs):
    text=f"""
    Title : {msgs.chat.title}
User Name : <code> @{msgs.from_user.username} </code>
Your ID : <code> {msgs.from_user.id} </code>
Group ID : <code> {msgs.chat.id} </code>
"""
    await msgs.reply_text(text=text)


bot.run()
