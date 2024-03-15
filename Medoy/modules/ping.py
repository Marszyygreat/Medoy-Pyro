# Ported By @Siid0yyy & @Mhmmdd23
# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
# ReCode by @mrismanaziz
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de


import time
from datetime import datetime

from speedtest import Speedtest

from . import (
     StartTime,
     Medoy_cmd,
     DEVLIST,
     eor,
     humanbytes,
     devs_cmd,
     )
from time import sleep


async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "Jam", "Hari"]

    while count < 4:
        count += 1
        remainder, result = divmod(
            seconds, 60) if count < 3 else divmod(
            seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += f"{time_list.pop()}, "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


@Medoy_cmd(pattern=r"^pink$", incoming=True, from_users=DEVLIST)
@devs_cmd(incoming=True, from_users=DEVLIST, pattern=r"^Cpink$")
async def _(ping):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    ping = await eor(ping, "✧")
    await ping.edit("✧✧")
    await ping.edit("✧✧✧")
    await ping.edit("✧✧✧✧")
    await ping.edit("✧✧✧✧✧")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user = await ping.client.get_me()
    await ping.edit("⚡")
    sleep(3)
    await ping.edit(
        f"✧ Medoy 𝚄serbot ✧\n\n"
        f"✧ 𝙿𝙸𝙽𝙶𝙴𝚁 : %sms\n"
        f"✧ 𝚄𝙿𝚃𝙸𝙼𝙴 : {uptime} \n"
        f"✧ 𝙾𝚆𝙽𝙴𝚁 : [{user.first_name}](tg://user?id={user.id})" % (duration)
    )


@Medoy_cmd(pattern="ping$")
@devs_cmd(incoming=True, from_users=DEVLIST, pattern=r"^Cping$")
async def _(ping):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    xping = await eor(ping, "Pinging....")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await xping.edit(
        f"PONG!! 🍭\nPing : %sms\nBot Uptime : {uptime}🕛" % (duration)
    )


@Medoy_cmd(pattern="lping$")
@devs_cmd(incoming=True, from_users=DEVLIST, pattern=r"^Lping$")
async def _(ping):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    lping = await eor(ping, "★ PING ★")
    await lping.edit("★★ PING ★★")
    await lping.edit("★★★ PING ★★★")
    await lping.edit("★★★★ PING ★★★★")
    await lping.edit("✦҈͜͡➳ PONG!")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user = await ping.client.get_me()
    await lping.edit(
        f"❃ Ping !! "
        f"%sms \n"
        f"❃ Uptime - "
        f"{uptime} \n"
        f"✦҈͜͡➳ Master : [{user.first_name}](tg://user?id={user.id})" % (duration)
    )


@Medoy_cmd(pattern="keping$")
@devs_cmd(incoming=True, from_users=DEVLIST, pattern=r"^Kping$")
async def _(pong):
    await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    kopong = await eor(pong, "『⍟𝐊𝐎𝐍𝐓𝐎𝐋』")
    await kopong.edit("◆◈𝐊𝐀𝐌𝐏𝐀𝐍𝐆◈◆")
    await kopong.edit("𝐏𝐄𝐂𝐀𝐇𝐊𝐀𝐍 𝐁𝐈𝐉𝐈 𝐊𝐀𝐔 𝐀𝐒𝐔")
    await kopong.edit("☬𝐒𝐈𝐀𝐏 𝐊𝐀𝐌𝐏𝐀𝐍𝐆 𝐌𝐄𝐍𝐔𝐌𝐁𝐔𝐊 𝐀𝐒𝐔☬")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user = await pong.client.get_me()
    await kopong.edit(
        f"✲ 𝙺𝙾𝙽𝚃𝙾𝙻 𝙼𝙴𝙻𝙴𝙳𝚄𝙶 "
        f"\n ⫸ 𝙺𝙾𝙽𝚃𝙾𝙻 %sms \n"
        f"✲ 𝙱𝙸𝙹𝙸 𝙿𝙴𝙻𝙴𝚁 "
        f"\n ⫸ 𝙺𝙰𝙼𝙿𝙰𝙽𝙶『[{u
