from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup

API_ID = "18979569"
API_HASH = "45db354387b8122bdf6c1b0beef93743"
BOT_TOKEN = "5530146236:AAGs0pJc11GSk6uxFZ3eYuVcP2DOXMWTlB4"

GOUTHAM = Client(
     name="Pyrogram Bot",
     api_id=API_ID,
     api_hash=API_HASH,
     bot_token=BOT_TOKEN
)


@GOUTHAM.on_message(filters.command("start"))
async def start_cmd(client, message):
     await message.reply_text(
          text="HELLO I AM PYROGRAM BOT \n MADE BY GOUTHAM SER",
          reply_markup=ReplyKeyboardMarkup(
              [[
                  "START🥰", "HELP🙄", "ABOUT😁"
              ],[
                   
                  "JOIN MY MOVIE BOT GROUP🤪"
              ]],
              resize_keyboard=True,
              one_time_keyboard=True
          )
     )
     
@GOUTHAM.on_message(filters.regex("START🥰"))
async def start_keyboard(client, message):
     await message.reply_text(
          text="HI IAM PYROGRAM STUDING BOT \n\n MADE WITH PYTHON LANGUAGE\n\n\nDEVELPOED BY GOUTHAM SER🤍 ❤️"
     )

     


print("I am Pyrogram Study Bot Now I am STARTED WITH NO ERRORS😋 ")

GOUTHAM.run()
