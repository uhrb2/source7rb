import html
import os
import random
from requests import get
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.utils import get_input_location
from JoKeRUB import l313l
from random import choice
from l313l.razan.resources.strings import *
from telethon import events
from ..Config import Config
from ..core.managers import edit_or_reply
from ..helpers import get_user_from_event, reply_id
from . import spamwatch
from telethon.utils import get_display_name
from ..helpers.utils import reply_id, _catutils, parse_pre, yaml_format, install_pip, get_user_from_event, _format

plugin_category = "utils"

@l313l.on(admin_cmd(pattern="رفع(?: |$)([\س\S]*)"))
async def promote_user(event):
    match = event.pattern_match.group(1).strip()
    if not match:
        return await edit_or_reply(event, "**- يرجى تحديد الدور المطلوب**")

    user, custom = await get_user_from_event(event)
    if not user:
        return await edit_or_reply(event, "**- لـم استطـع العثــور ع الشخــص**")

    user_id = user.id
    user_name = user.first_name.replace("\u2060", "") if user.first_name else user.username

    # تحقق من عدم رفع المطور
    if user_id in [7182427468]:
        return await edit_or_reply(event, f"**- لكك دي هذا المطور**")

    me = await event.client.get_me()
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"

    await edit_or_reply(event, f"**᯽︙ المستخدم** [{user_name}](tg://user?id={user.id}) \n**᯽︙  تـم رفعـه {match} بواسطة :** {my_mention}")


import random

# قائمة من أنواع الخطوط
fonts = [
    "𝗕𝗼𝗹𝗱", "𝐵𝑜𝑙𝑑", "𝓑𝓸𝓵𝓭", "𝔹𝕠𝕝𝕕", "𝕭𝖔𝖑𝖉", "𝔅𝔬𝔩𝔡", "🄱🄾🄻🄳", "𝙱𝚘𝚕𝚍", "🅱🅾🅻🅳"
]

def apply_font(text, font):
    if font == "𝗕𝗼𝗹𝗱":
        return ''.join(chr(0x1d5d4 + ord(c) - ord('A')) if 'A' <= c <= 'Z' else chr(0x1d5ee + ord(c) - ord('a')) if 'a' <= c <= 'z' else c for c in text)
    elif font == "𝐵𝑜𝑙𝑑":
        return ''.join(chr(0x1d434 + ord(c) - ord('A')) if 'A' <= c <= 'Z' else chr(0x1d44e + ord(c) - ord('a')) if 'a' <= c <= 'z' else c for c in text)
    elif font == "𝓑𝓸𝓵𝓭":
        return ''.join(chr(0x1d4d0 + ord(c) - ord('A')) if 'A' <= c <= 'Z' else chr(0x1d4ea + ord(c) - ord('a')) if 'a' <= c <= 'z' else c for c in text)
    elif font == "𝔹𝕠𝕝𝕕":
        return ''.join(chr(0x1d56c + ord(c) - ord('A')) if 'A' <= c <= 'Z' else chr(0x1d586 + ord(c) - ord('a')) if 'a' <= c <= 'z' else c for c in text)
    elif font == "𝕭𝖔𝖑𝖉":
        return ''.join(chr(0x1d5a0 + ord(c) - ord('A')) if 'A' <= c <= 'Z' else chr(0x1d5ba + ord(c) - ord('a')) if 'a' <= c <= 'z' else c for c in text)
    elif font == "𝔅𝔬𝔩𝔡":
        return ''.join(chr(0x1d504 + ord(c) - ord('A')) if 'A' <= c <= 'Z' else chr(0x1d51e + ord(c) - ord('a')) if 'a' <= c <= 'z' else c for c in text)
    elif font == "🄱🄾🄻🄳":
        return ''.join(chr(0x1f150 + ord(c) - ord('A')) if 'A' <= c <= 'Z' else c for c in text)
    elif font == "𝙱𝚘𝚕𝚍":
        return ''.join(chr(0x1d63c + ord(c) - ord('A')) if 'A' <= c <= 'Z' else chr(0x1d656 + ord(c) - ord('a')) if 'a' <= c <= 'z' else c for c in text)
    elif font == "🅱🅾🅻🅳":
        return ''.join(chr(0x1f170 + ord(c) - ord('A')) if 'A' <= c <= 'Z' else c for c in text)
    else:
        return text

async def random_spam_function(event, messages, sleeptimet):
    while True:
        if gvarstatus("spamwork") is None:
            return
        random_message = random.choice(messages)
        random_font = random.choice(fonts)
        styled_message = apply_font(random_message, random_font)
        await event.client.send_message(event.chat_id, styled_message)
        await asyncio.sleep(sleeptimet)
        if BOTLOG:
            await event.client.send_message(BOTLOG_CHATID, f"**⌔∮ رسالة عشوائية أرسلت: ** `{styled_message}`")

@l313l.ar_cmd(pattern="تكرار عشوائي (.*)")
async def random_spammer(event):
    input_str = "".join(event.text.split(maxsplit=1)[1:])
    messages = input_str.split("|")
    sleeptimet = 300  # يمكنك تغيير هذا الوقت حسب الحاجة
    addgvar("spamwork", True)
    await random_spam_function(event, messages, sleeptimet)

# مراقبة الرسائل في المجموعة
@l313l.on(events.NewMessage)
async def monitor_messages(event):
    if event.is_group:
        print(f"رسالة جديدة في المجموعة: {event.text}")
