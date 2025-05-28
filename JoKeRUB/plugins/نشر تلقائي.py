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

async def get_user_from_event(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        user_object = await event.client.get_entity(previous_message.sender_id)
    else:
        user = event.pattern_match.group(1)
        if user.isnumeric():
            user = int(user)
        if not user:
            user_object = await event.client.get_me()
            user = user_object.id
        if event.message.entities:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        if isinstance(user, int) or user.startswith("@"):
            user_obj = await event.client.get_entity(user)
            return user_obj
        try:
            user_object = await event.client.get_entity(user)
        except (TypeError, ValueError) as err:
            await event.edit(str(err))
            return None
    return user_object

@l313l.on(admin_cmd(pattern="(نشر_تلقائي|النشر_التلقائي)"))
async def _(event):
    if event.is_private or event.is_group:
        return await edit_or_reply(event, "**᯽︙ عـذراً .. النشر التلقائي خـاص بالقنـوات فقـط**")
    jok = event.pattern_match.group(1)
    if not jok:
        return await edit_or_reply(event, "**᯽︙ عـذراً .. قـم بـ إضـافة معـرف/ايـدي القنـاة الى الامـر اولاً**")
    if jok.startswith("@"):
        JoKeRUB = jok
    elif jok.startswith("https://t.me/"):
        JoKeRUB = jok.replace("https://t.me/", "@")
    elif str(jok).startswith("-100"):
        JoKeRUB = str(jok).replace("-100", "")
    else:
        try:
            JoKeRUB = int(jok)
        except BaseException:
            return await edit_or_reply(event, "**᯽︙ عـذراً .. معـرف/ايـدي القنـاة غيـر صـالح**\n**✾╎الرجـاء التـأكـد مـن المعـرف/الايـدي**")
    try:
        JoKeRUB = (await event.client.get_entity(JoKeRUB)).id
    except BaseException:
        return await edit_or_reply(event, "**᯽︙ عـذراً .. معـرف/ايـدي القنـاة غيـر صـالح**\n**✾╎الرجـاء التـأكـد مـن المعـرف/الايـدي**")
    if is_post(str(JoKeRUB), event.chat_id):
        return await edit_or_reply(event, f"**᯽︙ النشـر التلقـائي من القنـاة ** `{jok}` **مفعـل مسبقـاً ✓**")
    add_post(str(JoKeRUB), event.chat_id)
    await edit_or_reply(event, f"**᯽︙ تم تفعيـل النشـر التلقـائي من القنـاة ** `{jok}` **بنجـاح ✓**")


@l313l.on(admin_cmd(pattern="(ايقاف_نشر|ايقاف_النشر)"))
async def _(event):
    if event.is_private or event.is_group:
        return await edit_or_reply(event, "**᯽︙ عـذراً .. النشر التلقائي خـاص بالقنـوات فقـط**")
    jok = event.pattern_match.group(1)
    if not jok:
        return await edit_or_reply(event, "**᯽︙ عـذراً .. قـم بـ إضـافة معـرف/ايـدي القنـاة الى الامـر اولاً**")
    if jok.startswith("@"):
        JoKeRUB = jok
    elif jok.startswith("https://t.me/"):
        JoKeRUB = jok.replace("https://t.me/", "@")
    elif str(jok).startswith("-100"):
        JoKeRUB = str(jok).replace("-100", "")
    else:
        try:
            JoKeRUB = int(jok)
        except BaseException:
            return await edit_or_reply(event, "**᯽︙ عـذراً .. معـرف/ايـدي القنـاة غيـر صـالح**\n**✾╎الرجـاء التـأكـد مـن المعـرف/الايـدي**")
    try:
        JoKeRUB = (await event.client.get_entity(JoKeRUB)).id
    except BaseException:
        return await edit_or_reply(event, "**᯽︙ عـذراً .. معـرف/ايـدي القنـاة غيـر صـالح**\n**✾╎الرجـاء التـأكـد مـن المعـرف/الايـدي**")
    if not is_post(str(JoKeRUB), event.chat_id):
        return await edit_or_reply(event, "**᯽︙ تم تعطيـل النشر التلقـائي لهـذه القنـاة هنـا .. بنجـاح ✓**")
    remove_post(str(JoKeRUB), event.chat_id)
    await edit_or_reply(event, f"**᯽︙ تم ايقـاف النشـر التلقـائي من** `{jok}`")


@l313l.ar_cmd(incoming=True, forword=None)
async def _(event):
    if event.is_private:
        return
    chat_id = str(event.chat_id).replace("-100", "")
    channels_set  = get_all_post(chat_id)
    if channels_set == []:
        return
    for chat in channels_set:
        if event.media:
            await event.client.send_file(int(chat), event.media, caption=event.text)
        elif not event.media:
            await l313l.send_message(int(chat), event.message)

from asyncio import sleep

@l313l.on(admin_cmd(pattern="نشر\+(\d+)\+([^\+]+)\+(\d+)$"))
async def auto_spam_publish(event):
    if not event.reply_to_msg_id:
        return await edit_or_reply(event, " يجب الرد على الرسالة التي تريد نشرها.")
    try:
        args = event.pattern_match
        seconds = int(args.group(1))
        target = args.group(2)
        count = int(args.group(3))
        if target.startswith("@"):
            target_id = target
        elif target.startswith("https://t.me/"):
            target_id = target.replace("https://t.me/", "@")
        else:
            try:
                target_id = int(target)
            except Exception:
                return await edit_or_reply(event, " صيغة الآيدي/الرابط/اليوزر غير صحيحة.")
        msg = await event.get_reply_message()
        sent = 0
        for i in range(count):
            if msg.media:
                await event.client.send_file(target_id, msg.media, caption=msg.text or "")
            else:
                await event.client.send_message(target_id, msg.text or "")
            sent += 1
            await sleep(seconds)
        await edit_or_reply(event, f"✅ تم نشر الرسالة {sent} مرة في {target_id}.")
    except Exception as e:
        await edit_or_reply(event, f"حدث خطأ: {str(e)}")

auto_publish_status = {}

@l313l.on(admin_cmd(pattern="ايقاف نشر مكرر$"))
async def stop_auto_spam_publish(event):
    chat_id = event.chat_id
    msg_id = event.reply_to_msg_id
    key = f"{chat_id}:{msg_id}"
    auto_publish_status[key] = False
    await edit_or_reply(event, "✅ تم إيقاف النشر المكرر لهذه الرسالة.")