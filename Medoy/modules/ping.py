# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

from prettytable import PrettyTable
from pyrogram import Client, enums, filters
from pyrogram.types import Message

from Medoy.helpers.PyroHelpers import ReplyCheck
from config import CMD_HANDLER
from Medoy import CMD_HELP, app
from Medoy.helpers.basic import edit_or_reply
from Medoy.helpers.utility import split_list
from Medoy import *
from config import *

@Client.on_message(filters.command("help", CMD_HANDLER) & filters.me)
async def module_help(client: Client, message: Message):
    cmd = message.command
    help_arg = ""
    bot_username = (await app.get_me()).username
    if len(cmd) > 1:
        help_arg = " ".join(cmd[1:])
    elif not message.reply_to_message and len(cmd) == 1:
        try:
            nice = await client.get_inline_bot_results(bot=bot_username, query="helper")
            await asyncio.gather(
                message.delete(),
                client.send_inline_bot_result(
                    message.chat.id, nice.query_id, nice.results[0].id
                ),
            )
        except BaseException as e:
            print(f"{e}")
            ac = PrettyTable()
            ac.header = False
            ac.title = "Medoy Userbot Plugins"
            ac.align = "l"
            for x in split_list(sorted(CMD_HELP.keys()), 2):
                ac.add_row([x[0], x[1] if len(x) >= 2 else None])
            xx = await client.send_message(
                message.chat.id,
                f"{str(ac)}\n• Medoy Userbot •",
                reply_to_message_id=ReplyCheck(message),
            )
            await xx.reply(
                f"Usage: {CMD_HANDLER}help broadcast To View Module Information"
            )
            return

    if help_arg:
        if help_arg in CMD_HELP:
            commands: dict = CMD_HELP[help_arg]
            this_command = f"Help For {str(help_arg).upper()}\n\n"
            for x in commands:
                this_command += f"Command: {str(x)}\nFunction: {str(commands[x])}\n\n"
            this_command += "© Medoy Userbot"
            await edit_or_reply(
                message, this_command, parse_mode=enums.ParseMode.MARKDOWN
            )
        else:
            await edit_or_reply(
                message,
                f"{help_arg} tidak ada dalam list modul.",
            )



def add_command_help(module_name, commands):
    if module_name in CMD_HELP.keys():
        command_dict = CMD_HELP[module_name]
    else:
        command_dict = {}

    for x in commands:
        for y in x:
            if y is not x:
                command_dict[x[0]] = x[1]

    CMD_HELP[module_name] = command_dict
