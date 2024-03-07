from pyrogram.types import InlineKeyboardButton, WebAppInfo
from Medoy import CMD_HELP, CMD_HANDLER 

class Data:
    
   num_basic_modules = len(CMD_HELP)

   text_help_menu = (
        f"**Help Menu**   "
    )
   reopen = [[InlineKeyboardButton("Open", callback_data="reopen")]]
