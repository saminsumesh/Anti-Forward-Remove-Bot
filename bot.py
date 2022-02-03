import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import time 

Bot = Client(
    "Forward remove bot",
    bot_token=os.environ.get("BOT_TOKEN"),
    api_id=int(os.environ.get("API_ID")),
    api_hash=os.environ.get("API_HASH")
)

START_TXT = """Hello {},
__Iam a simple Auto Forward Tag message remover bot__
➣ Just add me to your groups and make me as admin.
➣ I will only remove message with forward tag!

**Made by @XD_Botz**
"""

START_BUTTONS = InlineKeyboardMarkup(
    [[
        InlineKeyboardButton("Add me to your group", url="https://t.me/forwardremoveXDbot?startgroup=true")
    ]]
)

@Bot.on_message(filters.command("start"))
async def start(bot, message):
    m=await message.reply_text("▰▱▱")
    n=await m.edit("▰▰▱")
    o=await n.edit("▰▰▰")
    await o.edit(
        text=START_TXT.format(message.from_user.mention),
        reply_markup=START_BUTTONS,
    )

@Bot.on_message(filters.forwarded)
async def forward(bot, message):
    await message.delete("This group doesn't allow forward messages")
    await message.delete
Bot.run()
