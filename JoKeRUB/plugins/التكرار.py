# By JoKeRUB 2021-2023
import asyncio
import base64
import re
from telethon.tl import functions, types
from telethon.tl.functions.messages import GetStickerSetRequest
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.utils import get_display_name
from JoKeRUB import l313l
from telethon import events
from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.tools import media_type
from ..helpers.utils import _catutils
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from . import BOTLOG, BOTLOG_CHATID
from telethon import events
import asyncio

bot = l313l  # غيّرها إذا كان اسم المتغير مختلف

# متغير عالمي لتعقب حالة التكرار
repeat_active = {}

@bot.on(events.NewMessage(pattern=r"\.مكرر (\d+)\s+(.+)"))
async def timed_repeat_handler(event):
    try:
        sleep_time = int(event.pattern_match.group(1))
        message = event.pattern_match.group(2).strip()
        if not message:
            await event.reply("❌ يرجى كتابة كلمة أو جملة بعد الوقت.")
            return
        if sleep_time < 0:
            await event.reply("❌ الوقت يجب أن يكون رقمًا موجبًا.")
            return

        chat_id = event.chat_id
        repeat_active[chat_id] = True  # تفعيل التكرار
        await event.delete()
        while repeat_active.get(chat_id, False):
            await event.respond(message)
            await asyncio.sleep(sleep_time)
    except Exception as e:
        await event.reply(f"حدث خطأ: {e}")

@bot.on(events.NewMessage(pattern=r"\.ايقاف المكرر"))
async def stop_repeat_handler(event):
    chat_id = event.chat_id
    repeat_active[chat_id] = False
    await event.reply("✅ تم إيقاف التكرار بنجاح.")

# أمر سبام حرفي .سبام
@bot.on(events.NewMessage(pattern=r"\.سبام (.+)"))
async def char_spam_handler(event):
    try:
        message = event.pattern_match.group(1).replace(" ", "")
        if not message:
            await event.reply("❌ يرجى كتابة نص بعد الأمر.")
            return
        await event.delete()
        for letter in message:
            await event.respond(letter)
            await asyncio.sleep(0.05)
    except Exception as e:
        await event.reply(f"حدث خطأ: {e}")

# أمر سبام بالكلمات .وسبام
@bot.on(events.NewMessage(pattern=r"\.وسبام (.+)"))
async def word_spam_handler(event):
    try:
        message = event.pattern_match.group(1)
        words = message.split()
        if not words:
            await event.reply("❌ يرجى كتابة نص بعد الأمر.")
            return
        await event.delete()
        for word in words:
            await event.respond(word)
            await asyncio.sleep(0.1)
    except Exception as e:
        await event.reply(f"حدث خطأ: {e}")

# أمر إيقاف التكرار (للتوافق والرسالة فقط)
@bot.on(events.NewMessage(pattern=r"\.ايقاف التكرار"))
async def stop_spam_handler(event):
    await event.reply("تم إيقاف جميع أوامر التكرار، يمكنك استخدام الأوامر مجدداً متى شئت.")