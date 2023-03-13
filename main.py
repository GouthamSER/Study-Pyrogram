# IMPORTING
from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import CallbackQuery
import random

from aiohttp import web as webserver
from webcode import bot_run

PORT_CODE = environ.get("PORT", "8080")

# Acoout
API_ID = "18979569"
API_HASH = "45db354387b8122bdf6c1b0beef93743"
BOT_TOKEN = "5816309562:AAHPAhIv-oRv1YxEL0X9a3MFQEYfuCw8wbk"

@Goutham = Client(
     name="Pyrogram Bot",
     api_id=API_ID,
     api_hash=API_HASH,
     bot_token=BOT_TOKEN
)

        client = webserver.AppRunner(await bot_run())
        await client.setup()
        bind_address = "0.0.0.0"
        await webserver.TCPSite(client, bind_address,
        PORT_CODE).start()


@Goutham.on_message(filters.command("start"))
async def start_cmd(client, message):
     await message.reply_text(
          text="HELLO I AM PYROGRAM BOT\t DEVELPOING.......",
          reply_markup=ReplyKeyboardMarkup(
              [[
                  "START🥰", "HELP🙄", "ABOUT😁"
              ],[
                   
                  "JOIN MY MOVIE BOT GROUP🤪"
              ]],
              resize_keyboard=True,
          )
     )
     
@Goutham.on_message(filters.regex("START🥰"))
async def start_keyboard(client, message):
     await message.reply_text(
          text="HI IAM PYROGRAM STUDING BOT"
     )

@Gouthamt.on_message(filters.regex("HELP🙄"))
async def help_keyboard(client, message):
     await message.reply_text(
          text="NOTHING🤣🤣🤣🤣🤣🤣 IN THE HELP"
     )    
     
     
@Goutham.on_message(filters.regex("ABOUT😁"))
async def about_keyboard(client, message):
     await message.reply_text(
          text="ABOUT \nMADE WITH PYTHON LANGUAGE\nServer:Heroku\n\nTHIS BOT IS MADE BY GOUTHAM SER"
     )



#button inline 
     
@Goutham.on_message(filters.command("start"))
async def start_cmd(client, message):
     button = [[
          InlineKeyboardButton("OWNER",  url="t.me/im_goutham_josh")
     ],[
     InlineKeyboardButton("Button name", callback_data="start")
     ]]
            
   



     
     
 # callback query 
@Goutham.on_callback_query()
async def Goutham_cb(client: GOUTHAM, query: CallbackQuery):
     if query.data == "start":
          await query.message.edit(
              text="Hi"
          )




print("I AM PERFECTLY ALL RIGHT🐱‍🏍🐱‍🏍🐱‍🏍🐱‍🏍👻👻👻")

@Goutham.run()
