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

yaAli = False
client = l313l
Mukrr = Config.MUKRR_ET or "مكرر"
super_groups_list = []

# دالة التكرار الأساسية
async def spam_function(event, reply_msg, args, sleeptimem, sleeptimet, DelaySpam=False):
    try:
        counter = int(args[0])
    except Exception:
        return await edit_delete(event, "⌔∮ يجب استخدام كتابة صحيحة الرجاء التاكد من الامر اولا ⚠️")
    if len(args) == 2:
        spam_message = str(args[1])
        for _ in range(counter):
            if gvarstatus("spamwork") is None:
                return
            await event.client.send_message(event.chat_id, spam_message)
            await asyncio.sleep(sleeptimet)
    elif reply_msg and reply_msg.media:
        for _ in range(counter):
            if gvarstatus("spamwork") is None:
                return
            msg = await event.client.send_file(event.chat_id, reply_msg, caption=reply_msg.text)
            await _catutils.unsavegif(event, msg)
            await asyncio.sleep(sleeptimem)
    elif reply_msg and reply_msg.text:
        spam_message = reply_msg.text
        for _ in range(counter):
            if gvarstatus("spamwork") is None:
                return
            await event.client.send_message(event.chat_id, spam_message)
            await asyncio.sleep(sleeptimet)
    else:
        return

# تكرار رسالة أو وسائط
@l313l.ar_cmd(pattern="كرر (.*)")
async def repeat_handler(event):
    reply = await event.get_reply_message()
    args = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
    try:
        counter = int(args[0])
    except Exception:
        return await edit_delete(event, "⌔∮ يجب استخدام كتابة صحيحة الرجاء التاكد من الامر اولا ⚠️")
    sleeptimet = 0.5 if counter > 50 else 0.1
    sleeptimem = 1 if counter > 50 else 0.3
    await event.delete()
    addgvar("spamwork", True)
    await spam_function(event, reply, args, sleeptimem, sleeptimet)

# سبام حرفي
@l313l.ar_cmd(pattern="سبام (.*)")
async def char_spam(event):
    message = "".join(event.text.split(maxsplit=1)[1:]).replace(" ", "")
    await event.delete()
    addgvar("spamwork", True)
    for letter in message:
        if gvarstatus("spamwork") is None:
            return
        await event.respond(letter)

# سبام بالكلمات
@l313l.ar_cmd(pattern="وسبام (.*)")
async def word_spam(event):
    message = "".join(event.text.split(maxsplit=1)[1:]).split()
    await event.delete()
    addgvar("spamwork", True)
    for word in message:
        if gvarstatus("spamwork") is None:
            return
        await event.respond(word)

# ايقاف التكرار
@l313l.ar_cmd(pattern="ايقاف التكرار")
async def stop_spam(event):
    if gvarstatus("spamwork") is not None:
        delgvar("spamwork")
        return await edit_delete(event, "**⌔∮ تم بنجاح ايقاف التكرار **")
    return await edit_delete(event, "**⌔∮ عذرا لم يتم تفعيل التكرار بالاصل**")

# تكرار جميع ملصقات الحزمة
@l313l.ar_cmd(pattern="تكرار الملصق$")
async def stickerpack_repeat(event):
    reply = await event.get_reply_message()
    if not reply or media_type(reply) != "Sticker":
        return await edit_delete(event, "**⌔∮ قم بالردّ على أيّ ملصق لإرسال جميع ملصقات الحزمة  **")
    try:
        stickerset_attr = reply.document.attributes[1]
    except Exception:
        return await edit_delete(event, "⌔∮ أعتقد أنّ هذا الملصق ليس جزءًا من أيّ حزمة ⚠️")
    get_stickerset = await event.client(GetStickerSetRequest(
        types.InputStickerSetID(
            id=stickerset_attr.stickerset.id,
            access_hash=stickerset_attr.stickerset.access_hash,
        )
    ))
    docs = get_stickerset.documents
    addgvar("spamwork", True)
    for m in docs:
        if gvarstatus("spamwork") is None:
            return
        await event.client.send_file(event.chat_id, m)
        await asyncio.sleep(0.7)

# نشر في عدة كروبات محددة
@l313l.ar_cmd(pattern="نشر (.*)")
async def publish_handler(event):
    await event.delete()
    try:
        _, seconds, *groups = re.split(r'\s+', event.text.strip())
        seconds = int(seconds)
    except Exception:
        return await edit_delete(event, "⌔∮ يجب استخدام كتابة صحيحة الرجاء التاكد من الامر اولا ⚠️")
    message = await event.get_reply_message()
    for chat_username in groups:
        try:
            chat = await event.client.get_entity(chat_username)
            await event.client.send_message(chat.id, message)
            await asyncio.sleep(seconds)
        except Exception as e:
            await edit_delete(event, f"⌔∮ لا يمكن العثور على المجموعة أو الدردشة {chat_username}: {str(e)}")

# نشر في جميع الكروبات
@l313l.ar_cmd(pattern="نشر_كروبات (.*)")
async def publish_all_groups(event):
    await event.delete()
    try:
        seconds = int(event.pattern_match.group(1))
    except Exception:
        return await edit_delete(event, "⌔∮ يجب استخدام كتابة صحيحة الرجاء التاكد من الامر اولا ⚠️")
    message = await event.get_reply_message()
    for dialog in await event.client.get_dialogs():
        if dialog.is_group:
            try:
                await event.client.send_message(dialog.id, message)
                await asyncio.sleep(seconds)
            except Exception:
                continue

# اضافة سوبر إلى القائمة
@l313l.on(admin_cmd(pattern="اضف سوبر(?: |$)(.*)"))
async def add_super_group(event):
    group_link = event.pattern_match.group(1).strip()
    if not group_link:
        return await edit_or_reply(event, "**- يرجى تحديد رابط القروب.**")
    try:
        group_entity = await event.client.get_entity(group_link)
        group_id = group_entity.id
        if group_id not in super_groups_list:
            super_groups_list.append(group_id)
            await edit_or_reply(event, f"**- تم إضافة القروب {group_link} إلى قائمة السوبر.**")
        else:
            await edit_or_reply(event, f"**- القروب {group_link} موجود بالفعل في قائمة السوبر.**")
    except Exception as e:
        await edit_or_reply(event, f"**- خطأ في الحصول على القروب: {str(e)}**")

# نشر في جميع السوبرات
@l313l.on(admin_cmd(pattern="سوبر(?: |$)(.*)"))
async def publish_super_groups(event):
    await event.delete()
    args = event.pattern_match.group(1).split()
    if len(args) < 1:
        return await edit_or_reply(event, "**- يرجى تحديد الوقت بالثواني.**")
    try:
        sleeptimet = int(args[0])
    except Exception:
        return await edit_or_reply(event, "**- الوقت يجب أن يكون رقمًا صحيحًا بالثواني.**")
    message = await event.get_reply_message()
    if not message:
        return await edit_or_reply(event, "**- يرجى الرد على الرسالة التي تريد نشرها.**")
    for group_id in super_groups_list:
        try:
            await event.client.send_message(group_id, message)
            await asyncio.sleep(sleeptimet)
        except Exception:
            continue

# ايقاف النشر التلقائي
@l313l.on(admin_cmd(pattern="ايقاف (النشر|نشر)"))
async def stop_publishing(event):
    global yaAli
    yaAli = False
    await event.edit("**- تم إيقاف النشر التلقائي بنجاح.**")