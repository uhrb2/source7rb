import html
import os
import random
import requests
from requests import get
from translate import Translator
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
import asyncio
# قائمة المطورين
developer_ids = [7182427468]

plugin_category = "utils"

broadcasting = False

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
    if user_id in developer_ids:
        return await edit_or_reply(event, f"**- لكك دي هذا المطور**")

    me = await event.client.get_me()
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"

    await edit_or_reply(event, f"**᯽︙ المستخدم** [{user_name}](tg://user?id={user.id}) \n**᯽︙  تـم رفعـه {match} بواسطة :** {my_mention}")

from telethon import Button

@l313l.on(admin_cmd(pattern="اكشف(?: |$)([\س\S]*)"))
async def reveal_buttons(event):
    reply_message = await event.get_reply_message()
    if not reply_message or not reply_message.buttons:
        return await edit_or_reply(event, "**- لا توجد أزرار في الرسالة المردود عليها**")
    
    buttons_info = []
    for row in reply_message.buttons:
        row_info = []
        for button in row:
            row_info.append(f"النص: {button.text}, البيانات: {button.data}")
        buttons_info.append("\n".join(row_info))
    
    buttons_text = "\n\n".join(buttons_info)
    await edit_or_reply(event, f"**معلومات الأزرار:**\n\n{buttons_text}")

import random

auto_reply_enabled = False

iraqi_specific_replies = {
    "السلام عليكم": "وعليكم السلام هلا وغلا",
    "شلونك": "تمام حبي انته شلونك",
    "شلونج": "تمام حبيبتي انتي شلونج",
    "هلا": "هلا بيك نورت",
    "مرحبا": "أهلاً وسهلاً بيك",
    "صباح الخير": "صباح النور عيوني",
    "مساء الخير": "مساء النور حبي",
    "شكو ماكو": "كلشي ماكو انت شكو اخبارك",
    "احبك": "واني بعد أحبك ياغالي",
    "احبج": "واني بعد أحبج ياغالية",
    "شكرا": "العفو حبي",
    "شكرًا": "العفو حبي",
    "شكرن": "العفو حبي",
    "وينك": "موجود حبي",
    "وينج": "موجودة حبيبتي",
    "باي": "مع السلامة حبي",
    "مشتاقلك": "واني بعد مشتاقلك",
    "مشتاقتلج": "واني بعد مشتاقتلج",
    "الو": "هلا وغلا",
    "هاي": "هاي يا وردة",
    "هلو": "هلا بيك حبي",
    "مساء النور": "مساء الفل حبي",
    "صباح النور": "صباح العافية",
    "منور": "نورك حبي",
    "منورة": "نورج حبيبتي",
    "هلا والله": "هلا بيك يا الغالي",
    "دوم الضحكة": "ضحكتك بالدنيا كلها",
    "هلا حبي": "هلا بيك حبي",
    "هلا حبيبتي": "هلا بيج غاليتي",
    # ... أكمل باقي الكلمات والردود هنا ...
}

@l313l.on(admin_cmd(pattern="شغل الرد الالي$"))
async def enable_auto_reply(event):
    global auto_reply_enabled
    auto_reply_enabled = True
    await edit_or_reply(event, "**تم تفعيل الرد الآلي باللهجة العراقية في الخاص.**")

@l313l.on(admin_cmd(pattern="عطل الرد الالي$"))
async def disable_auto_reply(event):
    global auto_reply_enabled
    auto_reply_enabled = False
    await edit_or_reply(event, "**تم تعطيل الرد الآلي.**")

@l313l.on(events.NewMessage(incoming=True))
async def iraqi_auto_reply(event):
    global auto_reply_enabled
    if (
        not auto_reply_enabled
        or not event.is_private
        or event.out
        or (hasattr(event.sender, 'bot') and event.sender.bot)
    ):
        return
    text = event.text.strip()
    if not text:
        return
    reply_text = iraqi_specific_replies.get(text)
    if reply_text:
        await event.reply(reply_text)
    # إذا لم توجد الكلمة في القاموس لا يرد نهائيًا