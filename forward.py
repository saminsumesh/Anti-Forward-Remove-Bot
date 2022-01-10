import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

Auto = Client(
 "Auto forward Remove Bot",
 bot_token=os.environ.get("BOT_TOKEN"),
 api_id=int(os.environ.get("API_ID")),
 api_hash=os.environ.get("API_HASH")
  )
  
@Auto.on_message(filters.command("start"))
async def start(bot, message):
    m=await message.reply_edit("Processing...")
    n=await edit.m(
    text=START_TXT.format(message.from_user.mention),
    reply_markup=START_BUTTONS,
    )
    
    
@Auto.on_message(filters.forward)
async def forward(bot, message):
    if forward in message:
        await message.reply_text(
        text=f"This message is forwarded from another chat")
         try:
             await message.delete()
             
 Auto.run()
