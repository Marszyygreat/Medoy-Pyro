from pyrogram.types import InlineKeyboardButton, WebAppInfo
from Medoy import CMD_HELP 

class Data:
    
   num_basic_modules = len(CMD_HELP)

   text_help_menu = (
        f"**Help Menu**\n     **Modules:** {num_basic_modules}"
    )
   reopen = [[InlineKeyboardButton("Open", callback_data="reopen")]]
