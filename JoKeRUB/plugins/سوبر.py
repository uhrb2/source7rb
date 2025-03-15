import schedule
import time
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
 import gvarstatus
from . import BOTLOG, BOTLOG_CHATID
from . import *

def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)

threading.Thread(target=run_schedule).start()

@l313l.on(admin_cmd(pattern="نشر (.+)"))
async def schedule_post(event):
    args = event.pattern_match.group(1).split()
    if len(args) < 1:
        return await edit_or_reply(event, "**᯽︙ عـذراً .. يجب تحديد الكروب والرسالة**")

    chat = args[0]
    message = await event.get_reply_message()

    if not message:
        return await edit_or_reply(event, "**᯽︙ عـذراً .. يجب الرد على الرسالة المراد نشرها**")

    if chat.startswith("@"):
        chat = chat
    elif chat.startswith("https://t.me/"):
        chat = chat.replace("https://t.me/", "@")
    elif str(chat).startswith("-100"):
        chat = str(chat).replace("-100", "")
    else:
        try:
            chat = int(chat)
        except BaseException:
            return await edit_or_reply(event, "**᯽︙ عـذراً .. معـرف/ايـدي الكروب غيـر صـالح**\n**✾╎الرجـاء التـأكـد مـن المعـرف/الايدي**")

    try:
        chat_id = (await event.client.get_entity(chat)).id
    except BaseException:
        return await edit_or_reply(event, "**᯽︙ عـذراً .. معـرف/ايـدي الكروب غيـر صـالح**\n**✾╎الرجـاء التـأكـد مـن المعـرف/الايدي**")

    alternating_bold = False
    async def alternating_job():
        nonlocal alternating_bold
        caption = f"**{message.text}**" if alternating_bold else message.text
        alternating_bold = not alternating_bold
        if message.media:
            await event.client.send_file(chat_id, message.media, caption=caption)
        else:
            await event.client.send_message(chat_id, caption)

    job_id = schedule.every(500).seconds.do(lambda: asyncio.run(alternating_job()))
    if not hasattr(event.chat, 'jobs'):
        event.chat.jobs = []
    event.chat.jobs.append(job_id)
    await edit_or_reply(event, f"**᯽︙ تم جدولة النشـر التلقـائي في الكروب ** `{chat}` ** بوقـت 500 ثانية بنجـاح ✓**")

@l313l.on(admin_cmd(pattern="ايقاف نشر"))
async def stop_scheduled_posts(event):
    if not hasattr(event.chat, 'jobs'):
        event.chat.jobs = []
    for job in event.chat.jobs:
        schedule.cancel_job(job)
    event.chat.jobs = []
    await edit_or_reply(event, "**᯽︙ تم إيقاف جميع الجداول بنجنا بتحديث الرسائل لتشير إلى الكروب بدلاً من القناة.
2. قمنا بتعديل التحقق من معرف/رابط الكروب.
3. استخدمنا `event.client.send_message` و `event.client.send_file` لنشر الرسالة في الكروب المحدد.

الآن يجب أن يقوم الأمر بنشر الرسالة في الكروب المحدد كل 500 ثانية بالتناوب بين الخط العريض والعادي.