from telethon import events
import random, re
from JoKeRUB.utils import admin_cmd
import asyncio
from JoKeRUB import l313l
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
import os
import datetime
from JoKeRUB import *
import aiohttp

@l313l.on(admin_cmd(pattern="تحميل قصة (.+)"))
async def download_story(event):
    url = event.pattern_match.group(1)
    await event.edit("**᯽︙جاري تحميل القصة ...**")

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    file_path = "story.mp4"
                    with open(file_path, "wb") as file:
                        while True:
                            chunk = await response.content.read(1024)
                            if not chunk:
                                break
                            file.write(chunk)

                    await event.client.send_file("me", file_path)
                    await event.edit("**᯽︙تم تحميل القصة وإرسالها إلى الرسائل المحفوظة بنجاح ✓**")
                    os.remove(file_path)
                else:
                    await event.edit("**᯽︙حدث خطأ أثناء تحميل القصة ✗**")
    except Exception as e:
        await event.edit(f"**᯽︙حدث خطأ: {str(e)} ✗**")

