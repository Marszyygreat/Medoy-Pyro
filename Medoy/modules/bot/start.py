import random
from Medoy import *
from pyrogram import filters
from config import CHANNEL, GROUP
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

alive_logo = "https://telegra.ph//file/cd9e19d64d6aa7cd695a9.jpg"

@app.on_message(filters.command("start") & filters.private)
async def start(app, message):
    chat_id = message.chat.id
    file_id = alive_logo
    caption = "Yoo, saya Medoy Userbot, gada yang spesial dari saya\ntapi boong..."
    reply_markup = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Channel", url="https://t.me/KegabutanDoy"),
            InlineKeyboardButton("Group", url="https://t.me/mutualanonlyone"),
        ],
    ])

    await app.send_photo(chat_id, file_id, caption=caption, reply_markup=reply_markup)
