from pyrogram import Client, filters

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
    print("START COMMAND")

@GOUTHAM.on_message(filters.command("help"))
async def help_cmd(client, message):
    print("HELP COMMAND")
     




print("BOT STARTED")

GOUTHAM.run()
