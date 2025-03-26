import time
import random
import threading
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
super_links = []

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
        await fetch_video(link, event)
        await event.respond(f"**᯽︙ تم جلب الفيديو من الرابط ** `{link}`")
        time.sleep(20)  # الانتظار لمدة 20 ثانية بين كل رابط والآخر

async def fetch_video(link, event):
    # هنا تضع الكود الفعلي لجلب الفيديو من الرابط
    # مثال لجلب الفيديو باستخدام requests
    import requests

    response = requests.get(link, stream=True)
    file_name = link.split("/")[-1]

    with open(file_name, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)

    # إرسال الفيديو إلى الرسائل المحفوظة
    await event.client.send_file("me", file_name)

# إضافة متغيرات جديدة للنشر
publish_message = None
publish_interval = None
publish_thread = None
publish_active = False

@l313l.on(admin_cmd(pattern="اضف سوبر (.*)"))
async def add_super(event):
    global super_links
    link = event.pattern_match.group(1)
    super_links.append(link)
    await edit_or_reply(event, f"**تم اضافة الرابط: {link}**")

@l313l.on(admin_cmd(pattern="نشر (.*) (\d+)"))
async def publish(event):
    global publish_message, publish_interval, publish_active, publish_thread

    if not super_links:
        return await edit_or_reply(event, "**يجب اضافة الرابط أولا باستخدام أمر 'اضف سوبر'.**")

    publish_message = event.pattern_match.group(1)
    publish_interval = int(event.pattern_match.group(2))
    publish_active = True

    if publish_thread is None or not publish_thread.is_alive():
        publish_thread = threading.Thread(target=publish_to_group, args=(event,))
        publish_thread.start()

    await edit_or_reply(event, f"**سيتم نشر الرسالة كل {publish_interval} ثانية**")

def publish_to_group(event):
    global publish_message, publish_interval, publish_active

    async def send_message():
        while publish_active:
            await event.respond(f"**نشر الرسالة:** {publish_message}")
            await asyncio.sleep(publish_interval)

    event.client.loop.create_task(send_message())

@l313l.on(admin_cmd(pattern="تعطيل النشر"))
async def stop_publish(event):
    global publish_active, publish_thread
    publish_active = False
    if publish_thread is not None:
        publish_thread.join()
    await edit_or_reply(event, "**تم تعطيل النشر**")

@l313l.on(admin_cmd(pattern="حذف سوبر (.*)"))
async def remove_super(event):
    global super_links
    link_or_user = event.pattern_match.group(1)
    if link_or_user in super_links:
        super_links.remove(link_or_user)
        await edit_or_reply(event, f"**تم حذف الرابط أو اليوزر:** {link_or_user}")
    else:
        await edit_or_reply(event, f"**لم يتم العثور على الرابط أو اليوزر:** {link_or_user}")