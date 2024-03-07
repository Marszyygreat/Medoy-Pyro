from math import ceil
from traceback import format_exc

from Ubot.core.db import *
from pyrogram.errors import MessageNotModified
from pyrogram.types import (
    InlineKeyboardButton,
    InlineQueryResultArticle,
    InputTextMessageContent,
)

from Medoy import ids as list_users

looters = None

    
def paginate_help(page_number, loaded_modules, prefix):
    number_of_rows = 4
    number_of_cols = 2
    global looters
    looters = page_number
    helpable_modules = [p for p in loaded_modules if not p.startswith("_")]
    helpable_modules = sorted(helpable_modules)
    modules = [
        InlineKeyboardButton(
            text="{}".format(x),
            callback_data=f"ub_modul_{x}",
        )
        for x in helpable_modules
    ]
    pairs = list(zip(modules[::number_of_cols], modules[1::number_of_cols]))
    if len(modules) % number_of_cols == 1:
        pairs.append((modules[-1],))
    max_num_pages = ceil(len(pairs) / number_of_rows)
    modulo_page = page_number % max_num_pages
    if len(pairs) > number_of_rows:
        pairs = pairs[
            modulo_page * number_of_rows : number_of_rows * (modulo_page + 1)
        ] + [
            (
                InlineKeyboardButton(
                    text="❮", callback_data=f"{prefix}_prev({modulo_page})"
                ),
                InlineKeyboardButton(
                    text="❯", callback_data=f"{prefix}_next({modulo_page})"
                ),
            ),
        ]
    return pairs


def cb_wrapper(func):
    async def wrapper(client, cb):
        users = list_users
        if cb.from_user.id not in users:
            await cb.answer(
                "Hanya Pengguna Premium Yang Dapat Mengakses Tombol Ini, Beli Sekarang di @RosePremiumBot",
                cache_time=0,
                show_alert=True,
            )
        else:
            try:
                await func(client, cb)
            except MessageNotModified:
                await cb.answer("🤔🧐")
            except Exception:
                print(format_exc())
                await cb.answer(
                    f"Oh Tidak, Ada yang Tidak Beres. Silakan Periksa Log!",
                    cache_time=0,
                    show_alert=True,
                )

    return wrapper


def inline_wrapper(func):
    async def wrapper(client, inline_query):
        users = list_users
        if inline_query.from_user.id not in users:
            await client.answer_inline_query(
                inline_query.id,
                cache_time=1,
                results=[
                    (
                        InlineQueryResultArticle(
                            title="✗ Rose-Userbot ✗",
                            description="Rose - UserBot | Pyogram",
                            url="https://t.me/RoseUserbot24",
                            thumb_url="https://telegra.ph//file/ec983785eea22d7a6c77d.jpg",
                            input_message_content=InputTextMessageContent(
                                "You cannot access this Bot"
                            ),
                        )
                    )
                ],
            )
        else:
            await func(client, inline_query)

    return wrapper
