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

@borg.on(
    admin_cmd(pattern="لايك ?(.*)")
)
async def wspr(event):
    if event.fwd_from:
        return
    l313lb = event.pattern_match.group(1)
    rrrd7 = "@like"
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    tap = await bot.inline_query(rrrd7, l313lb) 
    await tap[0].click(event.chat_id)
    await event.delete()

@borg.on(admin_cmd("م27"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("᯽︙ اوامر الهمسه واكس او \n\n⌔︙الامر  • `.همسة`\n⌔︙الاستخدام  • لكتابة همسه سرية لشخص في المجم[...]

@borg.on(admin_cmd("الهمسة"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("**᯽︙ شـرح كيـفية كـتابة همـسة سـرية**\n᯽︙ اولا اكتب الامر  .همسة  بعدها الرسالة بعدها اكتب معر[...]

@borg.on(
    admin_cmd(
       pattern="اكس او$"
    )
)
# كتابة وتعديل فريق 7rB   #@F_O_1
async def gamez(event):
    if event.fwd_from:
        return
    jmusername = "@xoBot"
    uunzz = "play"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(jmusername, uunzz)
    await tap[0].click(event.chat_id)
    await event.delete()

@l313l.on(admin_cmd(pattern="(الصوتية تشغيل|صوتية تشغيل)"))
async def enable_voice_save(event):
    if gvarstatus("savevoiceforme"):
        return await edit_delete(event, "**᯽︙حفظ الصوتيات مفعل وليس بحاجة للتفعيل مجدداً **")
    else:
        addgvar("savevoiceforme", "enabled")
        await edit_delete(event, "**᯽︙تم تفعيل ميزة حفظ الصوتيات بنجاح ✓**")

@l313l.on(admin_cmd(pattern="(الصوتية تعطيل|صوتية تعطيل)"))
async def disable_voice_save(event):
    if gvarstatus("savevoiceforme"):
        delgvar("savevoiceforme")
        return await edit_delete(event, "**᯽︙تم تعطيل حفظ الصوتيات بنجاح ✓**")
    else:
        await edit_delete(event, "**᯽︙انت لم تفعل حفظ الصوتيات لتعطيلها!**")

@l313l.on(admin_cmd(pattern="اكتب (.+)"))
async def write_text_letter_by_letter(event):
    text = event.pattern_match.group(1)
    result = ""
    for char in text:
        result += char
        await event.edit(result)
        await asyncio.sleep(0.20)  # إضافة تأخير بسيط بين كل حرف وآخر

@l313l.on(admin_cmd(pattern="تشغيل الاونلاين"))
async def enable_online(event):
    addgvar("always_online", "true")
    await event.edit("**تم تفعيل ميزة البقاء أونلاين ✓**")
    while gvarstatus("always_online"):
        await bot.send_read_acknowledge(event.chat_id)
        await asyncio.sleep(0)  # تكرار كل دقيقة

@l313l.on(admin_cmd(pattern="ايقاف الاونلاين"))
async def disable_online(event):
    if gvarstatus("always_online"):
        delgvar("always_online")
        await event.edit("**تم تعطيل ميزة البقاء أونلاين ✓**")
    else:
        await event.edit("**ميزة البقاء أونلاين غير مفعلة!**")

import openai

@l313l.on(admin_cmd(pattern="رسم مربع (\d+)"))
async def draw_square(event):
    try:
        size = int(event.pattern_match.group(1).strip())
        if size < 1:
            return await event.edit("يرجى توفير حجم أكبر من 0.")

        square = ""
        for i in range(size):
            square += "█" * size + "\n"

        await event.edit(f"تم رسم مربع بحجم {size}:\n\n{square}")
    except ValueError:
        await event.edit("يرجى توفير حجم صحيح.")

from telethon import events

@l313l.on(admin_cmd(pattern="(تشغيل الرد التلقائي)"))
async def enable_auto_respond(event):
    addgvar("auto_respond_enabled", "enabled")
    await event.edit("**تم تفعيل ميزة الرد التلقائي ✓**")

@l313l.on(admin_cmd(pattern="(ايقاف الرد التلقائي)"))
async def disable_auto_respond(event):
    if gvarstatus("auto_respond_enabled"):
        delgvar("auto_respond_enabled")
        await event.edit("**تم تعطيل ميزة الرد التلقائي ✓**")
    else:
        await event.edit("**ميزة الرد التلقائي غير مفعلة!**")

@l313l.on(events.NewMessage(pattern=r"^اول من يكتب (.+)$"))
async def auto_respond(event):
    if gvarstatus("auto_respond_enabled"):
        word_to_type = event.pattern_match.group(1).strip()
        await event.reply(word_to_type)  # الرد على الرسالة

# إضافة أوامر إضافية
@l313l.on(events.NewMessage(pattern=r"^اول شخص يكتب (.+)$"))
async def auto_respond_alternative1(event):
    if gvarstatus("auto_respond_enabled"):
        word_to_type = event.pattern_match.group(1).strip()
        await event.reply(word_to_type)  # الرد على الرسالة

@l313l.on(events.NewMessage(pattern=r"^أول من يكتب (.+)$"))
async def auto_respond_alternative2(event):
    if gvarstatus("auto_respond_enabled"):
        word_to_type = event.pattern_match.group(1).strip()
        await event.reply(word_to_type)  # الرد على الرسالة

@l313l.on(events.NewMessage(pattern=r"^اول واحد يكتب (.+)$"))
async def auto_respond_alternative1(event):
    if gvarstatus("auto_respond_enabled"):
        word_to_type = event.pattern_match.group(1).strip()
        await event.reply(word_to_type)  # الرد على الرسالة

@l313l.on(events.NewMessage(pattern=r"^اول بشر يكتب (.+)$"))
async def auto_respond_alternative1(event):
    if gvarstatus("auto_respond_enabled"):
        word_to_type = event.pattern_match.group(1).strip()
        await event.reply(word_to_type)  # الرد على الرسالة

@l313l.on(events.NewMessage(pattern=r"^أول شخص يكتب (.+)$"))
async def auto_respond_alternative1(event):
    if gvarstatus("auto_respond_enabled"):
        word_to_type = event.pattern_match.group(1).strip()
        await event.reply(word_to_type)  # الرد على الرسالة

@l313l.on(events.NewMessage(pattern=r"^أول بشر يكتب (.+)$"))
async def auto_respond_alternative1(event):
    if gvarstatus("auto_respond_enabled"):
        word_to_type = event.pattern_match.group(1).strip()
        await event.reply(word_to_type)  # الرد على الرسالة

@l313l.on(events.NewMessage(pattern=r"^أول من يكتب (.+)$"))
async def auto_respond_alternative1(event):
    if gvarstatus("auto_respond_enabled"):
        word_to_type = event.pattern_match.group(1).strip()
        await event.reply(word_to_type)  # الرد على الرسالة

@l313l.on(events.NewMessage(pattern=r"^أول واحد يكتب (.+)$"))
async def auto_respond_alternative1(event):
    if gvarstatus("auto_respond_enabled"):
        word_to_type = event.pattern_match.group(1).strip()
        await event.reply(word_to_type)  # الرد على الرسالة

from telethon import events
from JoKeRUB.utils import admin_cmd
import asyncio

# متغير عالمي لتتبع حالة النسخ
is_copying = False

from telethon.tl.types import MessageService

@l313l.on(admin_cmd(pattern="تسريب (.+)"))
async def copy_posts(event):
    global is_copying
    if is_copying:
        await event.edit("عملية التسريب جارية بالفعل.")
        return

    source_channel_username = event.pattern_match.group(1).strip()

    try:
        source_channel = await bot.get_entity(source_channel_username)
        destination_channel = await event.get_input_chat()

        posts_count = 0
        is_copying = True
        messages = []
        async for message in bot.iter_messages(source_channel, limit=None):
            if isinstance(message, MessageService):
                continue
            messages.append(message)

        for message in reversed(messages):
            if not is_copying:
                await event.edit(f"تم إيقاف عملية التسريب بعد تسريب {posts_count} منشور.")
                return
            await bot.send_message(destination_channel, message)
            posts_count += 1
            if posts_count >= 4000:
                break

        is_copying = False
        await event.edit(f"تم تسريب {posts_count} منشور بنجاح من {source_channel_username} إلى القناة الحالية.")
    except Exception as e:
        is_copying = False
        await event.edit(f"حدث خطأ: {str(e)}")

@l313l.on(admin_cmd(pattern="إيقاف التسريب"))
async def stop_copying(event):
    global is_copying
    is_copying = False
    await event.edit("تم إيقاف عملية التسريب.")