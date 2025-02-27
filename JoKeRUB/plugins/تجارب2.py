from telethon import events
import random, re
from JoKeRUB.utils import admin_cmd
import asyncio 
from JoKeRUB import l313l
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
import os
import datetime
from JoKeRUB import *
import openai

@l313l.on(admin_cmd(pattern="رسم مربع (\d+)"))
async def draw_square(event):
    try:
        size = int(event.pattern_match.group(1).strip())
        if size < 1:
            return await event.edit("يرجى توفير حجم أكبر من 0.")

        square = ""
        for i in range(size):
            square += "█" * size + "\n"

        await event.edit(f"تم رسم مربع بحجم {size}:\n\n{square}")
    except ValueError:
        await event.edit("يرجى توفير حجم صحيح.")

# متغير عالمي لتتبع حالة النسخ
is_copying = False

from telethon.tl.types import MessageService

@l313l.on(admin_cmd(pattern="تسريب (.+)"))
async def copy_posts(event):
    global is_copying
    if is_copying:
        await event.edit("عملية التسريب جارية بالفعل.")
        return

    source_channel_username = event.pattern_match.group(1).strip()

    try:
        source_channel = await bot.get_entity(source_channel_username)
        destination_channel = await event.get_input_chat()

        posts_count = 0
        is_copying = True
        messages = []
        async for message in bot.iter_messages(source_channel, limit=None):
            if isinstance(message, MessageService):
                continue
            messages.append(message)

        for message in reversed(messages):
            if not is_copying:
                await event.edit(f"تم إيقاف عملية التسريب بعد تسريب {posts_count} منشور.")
                return
            await bot.send_message(destination_channel, message)
            posts_count += 1
            if posts_count >= 4000:
                break

        is_copying = False
        await event.edit(f"تم تسريب {posts_count} منشور بنجاح من {source_channel_username} إلى القناة الحالية.")
    except Exception as e:
        is_copying = False
        await event.edit(f"حدث خطأ: {str(e)}")

@l313l.on(admin_cmd(pattern="إيقاف التسريب"))
async def stop_copying(event):
    global is_copying
    is_copying = False
    await event.edit("تم إيقاف عملية التسريب.")