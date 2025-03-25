import time
import threading
import random
from telethon import *
from telethon.tl import functions, types
from telethon.tl.functions.channels import GetParticipantRequest, GetFullChannelRequest
from telethon.errors.rpcerrorlist import UserNotParticipantError
from telethon.tl.functions.messages import ExportChatInviteRequest
from telethon.tl.functions.users import GetFullUserRequest

from JoKeRUB import l313l

from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply
from ..sql_helper.autopost_sql import add_post, get_all_post, is_post, remove_post
from JoKeRUB.core.logger import logging
from ..sql_helper.globals import gvarstatus
from . import BOTLOG, BOTLOG_CHATID
from . import *

# متغير لتفعيل أو تعطيل الأمر
restricted_links_enabled = False

@l313l.on(admin_cmd(pattern="تفعيل مقيد"))
async def enable_restricted_links(event):
    global restricted_links_enabled
    restricted_links_enabled = True
    await edit_or_reply(event, "**᯽︙ تم تفعيل جلب الفيديوهات المقيدة بنجاح**")

@l313l.on(admin_cmd(pattern="تعطيل مقيد"))
async def disable_restricted_links(event):
    global restricted_links_enabled
    restricted_links_enabled = False
    await edit_or_reply(event, "**᯽︙ تم تعطيل جلب الفيديوهات المقيدة بنجاح**")

@l313l.on(admin_cmd(pattern="جلب فيديوهات مقيدة"))
async def fetch_restricted_videos(event):
    if not restricted_links_enabled:
        return await edit_or_reply(event, "**᯽︙ الأمر معطل حالياً. قم بتفعيله باستخدام الأمر `تفعيل مقيد`**")

    message = await event.get_reply_message()
    if not message or not message.text:
        return await edit_or_reply(event, "**᯽︙ يجب الرد على رسالة تحتوي على الروابط لجلب الفيديوهات المقيدة**")

    links = message.text.split()
    if not links:
        return await edit_or_reply(event, "**᯽︙ لم يتم العثور على أي روابط في الرسالة المردود عليها**")

    for link in links:
        await event.respond(f"**᯽︙ جاري جلب الفيديو من الرابط ** `{link}`")
        # هنا تضع كود لجلب الفيديو من الرابط
        # سأفترض وجود دالة fetch_video(link) تقوم بجلب الفيديو من الرابط
        await fetch_video(link)
        await event.respond(f"**᯽︙ تم جلب الفيديو من الرابط ** `{link}`")
        time.sleep(20)  # الانتظار لمدة 20 ثانية بين كل رابط والآخر

async def fetch_video(link):
    # هنا تضع الكود الفعلي لجلب الفيديو من الرابط
    pass