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
from ..sql_helper.globals import gvarstatus
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
        return await edit_or_reply(event, "**᯽︙ عـذراً .. يجب تحديد القناة والرسالة**")

    channel = args[0]
    message = await event.get_reply_message()

    if not message:
        return await edit_or_reply(event, "**᯽︙ عـذراً .. يجب الرد على الرسالة المراد نشرها**.startswith("https://t.me/"):
        channel = channel.replace("https://t.me/", "@")
    elif str(channel).startswith("-100"):
        channel = str(channel).replace("-100", "")
    else:
        try:
            channel = int(channel)
        except BaseException:
            return await edit_or_reply(event, "**᯽︙ عـذراً .. معـرف/ايـدي القنـاة غيـر صـالح**\n**✾╎الرجـاء التـأكـد مـن المعـرف/الايدي**")

    try:
        channel_id = (await event.client.get_entity(channel)).id
    except BaseException:
        return await edit_or_reply(event, "**᯽︙ عـذراً .. معـرف/ايـدي القنـاة غيـر صـالح**\n**✾╎الرجـاء التـأكـد مـن المعـرف/الايدي**")

    alternating_bold = False
    def alternating_job():
        nonlocal alternating_bold
        caption = f"**{message.text}**" if alternating_bold else message.text
        alternating_bold = not alternating_bold
        if message.media:
            event.client.send_file(channel_id, message.media, caption=caption)
        else:
            event.client.send_message(channel_id, caption)

    job_id = schedule.every(10).seconds.do(alternating_job)
    if not hasattr(event.chat, 'jobs'):
        event.chat.jobs = []
    event.chat.jobs.append(job_id)
    await edit_or_reply(event, f"**᯽︙ تم جدولة النشـر التلقـائي في القنـاة ** `{channel}`_cmd(pattern="ايقاف نشر"))
async def stop_scheduled_posts(event):
    if not hasattr(event.chat, 'jobs'):
        event.chat.jobs = []
    for job in event.chat.jobs:
        schedule.cancel_job(job)
    event.chat.jobs = []
    await edit_or_reply(event, "**᯽︙ تم إيقاف جميع الجداول بنجاح ✓**")