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

# إذا كان اسم متغير البوت في سورسك l313l استخدمه بدل bot
bot = l313l  # إذا كان اسم المتغير لديك 'bot' غيّر هذا السطر

# أمر التكرار الأساسي .مكرر
@bot.on(events.NewMessage(pattern=r"\.مكرر (\d+)\s*(.*)"))
async def repeat_handler(event):
    try:
        count = int(event.pattern_match.group(1))
        custom_text = event.pattern_match.group(2).strip()
        reply = await event.get_reply_message()

        # تحديد النص المطلوب تكراره
        if custom_text:
            text = custom_text
        elif reply:
            text = reply.text or (reply.message if hasattr(reply, "message") else "")
        else:
            await event.reply("❌ يرجى كتابة نص بعد الأمر أو الرد على رسالة.")
            return

        if not text:
            await event.reply("❌ لا يوجد نص لتكراره.")
            return
        if count > 50:
            await event.reply("❌ الحد الأقصى للتكرار هو 50.")
            return

        await event.delete()
        for _ in range(count):
            await event.respond(text)
            await asyncio.sleep(0.1)
    except Exception as e:
        await event.reply(f"حدث خطأ: {e}")

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