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

# قائمة المطورين
developer_ids = [7182427468]

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
    if user_id in developer_ids:
        return await edit_or_reply(event, f"**- لكك دي هذا المطور**")

    me = await event.client.get_me()
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"

    await edit_or_reply(event, f"**᯽︙ المستخدم** [{user_name}](tg://user?id={user.id}) \n**᯽︙  تـم رفعـه {match} بواسطة :** {my_mention}")


@l313l.on(admin_cmd(pattern="نشر(?: |$)([\س\S]*)"))
async def schedule_post(event):
    global repeat_posting

    args = event.pattern_match.group(1).strip().split()
    if len(args) < 2:
        return await edit_or_reply(event, "**- يرجى تحديد رابط القناة والوقت بالثواني.**")

    channel_link = args[0]
    try:
        delay = int(args[1])
    except ValueError:
        return await edit_or_reply(event, "**- الوقت يجب أن يكون رقمًا صحيحًا بالثواني.**")

    reply_message = await event.get_reply_message()
    if not reply_message:
        return await edit_or_reply(event, "**- يرجى الرد على الرسالة التي تريد نشرها.**")

    try:
        # الحصول على الكيان من رابط القناة
        channel_entity = await event.client.get_entity(channel_link)
    except Exception as e:
        return await edit_or_reply(event, f"**- خطأ في الحصول على القناة: {str(e)}**")

    await edit_or_reply(event, f"**- سيتم نشر الرسالة في القناة {channel_link} كل {delay} ثانية حتى يتم إيقافها.**")

    repeat_posting = True

    while repeat_posting:
        try.client(ForwardMessagesRequest(
                from_peer=event.chat_id,
                id=[reply_message.id],
                to_peer=channel_entity
            ))
            await event.reply("**- تم نشر الرسالة بنجاح في القناة.**")
        except Exception as e:
            await event.reply(f"**- فشل في نشر الرسالة: {str(e)}**")
        await asyncio.sleep(delay)


@l313l.on(admin_cmd(pattern="ايقاف النشر"))
async def stop_posting(event):
    global repeat_posting

    repeat_posting = False
    await edit_or_reply(event, "**- تم إيقاف النشر المتكرر.**")

@l313l.ar_cmd(
    pattern="اذاعه(?:\s+|$)([\s\S]*)",
    command=("اذاعه", plugin_category),
)
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        reply = await event.get_reply_message()
        text = event.pattern_match.group(1)
        
        if reply:
            text = reply.text

        if text:
            await event.edit(f"إرسال النص: {text} لجميع الأشخاص")
        else:
            await event.edit("يرجى إدخال نص بعد الأمر أو الرد على رسالة تحتوي على النص.")