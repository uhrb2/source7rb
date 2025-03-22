import html
import os
import random
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

# قائمة VIP
vip_ids = set()

plugin_category = "utils"

@l313l.on(admin_cmd(pattern="رفع(?: |$)([\س\S]*)"))
async def promote_user(event):
    if event.sender_id not in developer_ids and event.sender_id not in vip_ids:
        return await event.reply("**- ليس لديك الصلاحية لاستخدام هذا الأمر.**")

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

@l313l.on(admin_cmd(pattern="/vip(?: |$)"))
async def add_vip(event):
    if event.sender_id not in developer_ids:
        return await event.reply("**- ليس لديك الصلاحية لاستخدام هذا الأمر.**")

    reply_message = await event.get_reply_message()
    if not reply_message:
        return await event.reply("**- يرجى الرد على رسالة المستخدم المراد إضافته إلى قائمة الـVIP.**")

    user = await event.client(GetFullUserRequest(reply_message.from_id))
    if not user:
        return await edit_or_reply(event, "**- لـم استطـع العثــور ع الشخــص**")

    vip_ids.add(user.user.id)
    await edit_or_reply(event, f"**تم مطوري فعلتله الاوامر المدفوعة لازم يعيد تشغيل هسة**")

from telethon.tl.functions.messages import SendReactionRequest

# قائمة التعبيرات
emojis = ['😊', '😂', '😍', '😢', '😡', '👍', '👎', '❤️', '🔥', '🎉']

# حالة التفعيل
reactions_enabled = False

@l313l.on(admin_cmd(pattern="تفعيل التعبيرات"))
async def enable_reactions(event):
    if event.sender_id not in developer_ids and event.sender_id not in vip_ids:
        return await event.reply("**- ليس لديك الصلاحية لاستخدام هذا الأمر.**")

    global reactions_enabled
    reactions_enabled = True
    await edit_or_reply(event, "**تم تفعيل التفاعل بالتعبيرات**")

@l313l.on(admin_cmd(pattern="ايقاف التعبيرات"))
async def disable_reactions(event):
    if event.sender_id not in developer_ids and event.sender_id not in vip_ids:
        return await event.reply("**- ليس لديك الصلاحية لاستخدام هذا الأمر.**")

    global reactions_enabled
    reactions_enabled = False
    await edit_or_reply(event, "**تم ايقاف التفاعل بالتعبيرات**")

@l313l.on(events.NewMessage(pattern=None))
async def react_to_message(event):
    if reactions_enabled:
        emoji = random.choice(emojis)
        await event.client(SendReactionRequest(peer=event.chat_id, msg_id=event.id, reaction=emoji))

# قائمة اللغات ورموزها
languages = {
    "ar": "Arabic",
    "en": "English",
    "fr": "French",
    "es": "Spanish",
    "de": "German",
    "it": "Italian",
    "ja": "Japanese",
    "ko": "Korean",
    "zh-cn": "Chinese (Simplified)",
    "zh-tw": "Chinese (Traditional)",
    # أضف المزيد من اللغات حسب الحاجة
}

# دالة لعرض قائمة اللغات
@l313l.on(admin_cmd(pattern="لغات(?: |$)([\س\S]*)"))
async def list_languages(event):
    languages_list = "\n".join([f"{code}: {name}" for code, name in languages.items()])
    await edit_or_reply(event, f"**قائمة اللغات المتاحة:**\n\n{languages_list}")

# دالة الترجمة
@l313l.on(admin_cmd(pattern="ترجم(?: |$)([\س\S]*)"))
async def translate_text(event):
    if event.sender_id not in developer_ids and event.sender_id not in vip_ids:
        return await event.reply("**- ليس لديك الصلاحية لاستخدام هذا الأمر.**")

    text_to_translate = event.pattern_match.group(1).strip()
    if not text_to_translate:
        return await edit_or_reply(event, "**- يرجى تحديد النص المطلوب ترجمته**")

    target_language = "ar"  # تغيير "ar" إلى رمز اللغة المطلوبة
    translator = Translator(to_lang=target_language)
    translation = translator.translate(text_to_translate)
    await edit_or_reply(event, f"**النص المترجم إلى {languages[target_language]}:**\n\n{translation}")

import asyncio
from telethon.tl.functions.messages import ForwardMessagesRequest

# متغير للتحكم في حالة التكرار
repeat_posting = False

@l313l.on(admin_cmd(pattern="نشر(?: |$)([\س\S]*)"))
async def schedule_post(event):
    global repeat_posting
    if event.sender_id not in developer_ids and event.sender_id not in vip_ids:
        return await event.reply("**- ليس لديك الصلاحية لاستخدام هذا الأمر.**")

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
        try:
            await event.client(ForwardMessagesRequest(
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
    if event.sender_id not in developer_ids and event.sender_id not in vip_ids:
        return await event.reply("**- ليس لديك الصلاحية لاستخدام هذا الأمر.**")

    repeat_posting = False
    await edit_or_reply(event, "**- تم إيقاف النشر المتكرر.**")