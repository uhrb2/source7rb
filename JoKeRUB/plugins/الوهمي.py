import asyncio
import time

import aiohttp
from telethon.errors import ChatAdminRequiredError as no_admin
from telethon.tl.functions.messages import ExportChatInviteRequest

from l313l.razan.resources.strings import *
from JoKeRUB import l313l
from JoKeRUB.utils import admin_cmd

from ..core.managers import edit_or_reply
from ..core.managers import edit_or_reply as eod
from ..helpers import get_user_from_event
from . import *


@l313l.on(admin_cmd(pattern="كتابة(?: |$)(.*)"))
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("**- يجب كتابة الامر بشكل صحيح**")
    await event.edit(f"**تم بدء وضع الكتابة الوهمية لـ {t} من الثوانـي**")
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(t)


@l313l.on(admin_cmd(pattern="صوتية(?: |$)(.*)"))
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("**- يجب كتابة الامر بشكل صحيح**")
    await event.edit(f"**تم بدء وضع ارسال الصوتية الوهمية لـ {t} من الثوانـي**")
    async with event.client.action(event.chat_id, "record-audio"):
        await asyncio.sleep(t)


@l313l.on(admin_cmd(pattern="فيد(?: |$)(.*)"))
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("**- يجب كتابة الامر بشكل صحيح**")
    await event.edit(f"**تم بدء وضع ارسال الفيديو الوهمي لـ {t} من الثوانـي**")
    async with event.client.action(event.chat_id, "record-video"):
        await asyncio.sleep(t)


@l313l.on(admin_cmd(pattern="لعبة(?: |$)(.*)"))
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("**- يجب كتابة الامر بشكل صحيح**")
    await event.edit(f"**تم بدء وضع اللعب الوهمي لـ {t} من الثوانـي**")
    async with event.client.action(event.chat_id, "game"):
        await asyncio.sleep(t)


@l313l.on(admin_cmd(pattern="الرابط$"))
async def _(e):
    rr = await edit_or_reply(e, "**يتم جلب الرابط انتظر **")
    try:
        r = await e.client(
            ExportChatInviteRequest(e.chat_id),
        )
    except no_admin:
        return await eod(rr, "عذرا انت لست مشرف في هذه الدردشة", time=10)
    await eod(rr, f"- رابط الدردشة\n {r.link}")


@l313l.on(admin_cmd(pattern="للكل تاك$"))
async def listall(JoKeRUB):
    if JoKeRUB.fwd_from:
        return
    mentions = "- هذه هي قائمة جميع الاعضاء هنا: "
    chat = await bot.get_input_chat()
    async for x in borg.iter_participants(chat, 2000):
        mentions += f" \n[{x.first_name}](tg://user?id={x.id})"
    await JoKeRUB.reply(mentions)
    await JoKeRUB.delete()

R = (
    "┈┈╱▔▔▔▔▔▔▔▔▔▔▔▏\n"
    "┈╱╭▏╮╭┻┻╮╭┻┻╮╭▏ \n"
    "▕╮╰▏╯┃╭╮┃┃╭╮┃╰▏ \n"
    "▕╯┈▏┈┗┻┻┛┗┻┻┻╮▏ \n"
    "▕╭╮▏╮┈┈┈┈┏━━━╯▏\n"
    "▕╰╯▏╯╰┳┳┳┳┳┳╯╭▏ \n"
    "▕┈╭▏╭╮┃┗┛┗┛┃┈╰▏ \n"
    "▕┈╰▏╰╯╰━━━━╯┈┈▏\n"
)


@l313l.on(admin_cmd(pattern=r"سبونج"))
async def kerz(kerz):
    await kerz.edit(R)

M = (
    "╭━┳━╭━╭━╮╮\n"
    "┃┈┈┈┣▅╋▅┫┃\n"
    "┃┈┃┈╰━╰━━━━━━╮\n"
    "╰┳╯┈┈┈┈┈┈┈┈┈◢▉◣\n"
    "╲┃┈┈┈┈┈┈┈┈┈┈▉▉▉\n"
    "╲┃┈┈┈┈┈┈┈┈┈┈◥▉◤\n"
    "╲┃┈┈┈┈╭━┳━━━━╯\n"
    "╲┣━━━━━━┫\n"
)


@l313l.on(admin_cmd(pattern=r"كلب"))
async def dog(dog):
    await dog.edit(M)
Z = (
    "┈┏━╮╭━┓┈╭━━━━╮\n"
    "┈┃┏┗┛┓┃╭┫ⓞⓘⓝⓚ┃\n"
    "┈╰┓▋▋┏╯╯╰━━━━╯\n"
    "╭━┻╮╲┗━━━━╮╭╮┈\n"
    "┃▎▎┃╲╲╲╲╲╲┣━╯┈\n"
    "╰━┳┻▅╯╲╲╲╲┃┈┈┈\n"
    "┈┈╰━┳┓┏┳┓┏╯┈┈┈\n"
    "┈┈┈┈┗┻┛┗┻┛┈┈┈┈\n"
)


H = (
    " ╱▏┈┈┈┈┈┈▕╲▕╲┈┈┈\n"
    "▏▏┈┈┈┈┈┈▕▏▔▔╲┈┈\n"
    "▏╲┈┈┈┈┈┈╱┈▔┈▔╲┈\n"
    "╲▏▔▔▔▔▔▔╯╯╰┳━━▀\n"
    "┈▏╯╯╯╯╯╯╯╯╱┃┈┈┈\n"
    "┈┃┏┳┳━━━┫┣┳┃┈┈┈\n"
    "┈┃┃┃┃┈┈┈┃┃┃┃┈┈┈\n"
    "┈┗┛┗┛┈┈┈┗┛┗┛┈┈┈\n"
)

A = (
    "┈┈┈┈╱▔▔▔▔▔╲┈╱▔╲\n"
    "┈┈┈┈▏┈┈▏╭╮▕┈▏╳▕\n"
    "┈┈┈┈▏┈┈▏┈┈▕┈╲▂╱\n"
    "┈╱▔▔╲▂╱╲▂▂┈╲▂▏▏\n"
    "╭▏┈┈┈┈┈┈┈▏╲▂▂╱┈\n"
    "┃▏┈┈┈┈▏┈┈▏┈┈┈┈┈\n"
    "╯▏┈╲╱▔╲▅▅▏┈┈┈┈\n"
    "┈╲▅▅▏▕▔▔▔▔▏┈┈┈┈\n"
)

N = (
    "┈┈┈╭━━━━━╮┈┈┈┈┈\n"
    "┈┈┈┃┊┊┊┊┊┃┈┈┈┈┈\n"
    "┈┈┈┃┊┊╭━╮┻╮┈┈┈┈\n"
    "┈┈┈╱╲┊┃▋┃▋┃┈┈┈┈\n"
    "┈┈╭┻┊┊╰━┻━╮┈┈┈┈\n"
    "┈┈╰┳┊╭━━━┳╯┈┈┈┈\n"
    "┈┈┈┃┊┃╰━━┫┈┈┈┈\n"
    "┈┈┈┈┈┈┏━┓┈┈┈┈┈┈\n"
)



@l313l.on(admin_cmd(pattern=r"ذئب"))
async def fox(fox):
    await fox.edit(H)


@l313l.on(admin_cmd(pattern=r"فيل"))
async def elephant(elephant):
    await elephant.edit(A)


@l313l.on(admin_cmd(pattern=r"هومر"))
async def homer(homer):
    await homer.edit(N)


@l313l.on(admin_cmd(pattern=r"بك"))
async def pig(pig):
    await pig.edit(Z)

# أمر: إزالة بوتاتي
from telethon.tl.custom.button import Button
from telethon.tl.types import InputBotInlineMessageID

@l313l.on(admin_cmd(pattern="إزالة بوتاتي$"))
async def delete_all_bots_by_data(event):
    botfather = "BotFather"
    await event.edit("جاري حذف جميع البوتات بالاعتماد على أزرار البيانات... الرجاء الانتظار")
    deleted = []
    offset = 0

    while True:
        # إرسال /mybots للحصول على القائمة مع الأزرار
        mybots_msg = await event.client.send_message(botfather, "/mybots")
        await asyncio.sleep(2)
        # جلب آخر رسالة من BotFather تحتوي الأزرار
        msgs = await event.client.get_messages(botfather, limit=3)
        bot_msg = None
        for msg in msgs:
            if msg.buttons:
                bot_msg = msg
                break
        if not bot_msg or not bot_msg.buttons:
            break

        # البحث عن أزرار البوتات (callback_data يبدأ بـ b'bots/')
        bot_buttons = []
        for row in bot_msg.buttons:
            for button in row:
                if (hasattr(button, 'data')
                    and button.data
                    and button.data.startswith(b'bots/')
                    and b'/' not in button.data[5:]):  # فقط البوتات وليس أزرار next page
                    bot_buttons.append(button)
        if not bot_buttons:
            break

        for button in bot_buttons:
            # اضغط على زر البوت لفتح خياراته
            await event.client(
                functions.messages.GetBotCallbackAnswerRequest(
                    botfather,
                    bot_msg.id,
                    data=button.data
                )
            )
            await asyncio.sleep(2)
            # جلب رسالة الخيارات (فيها زر الحذف)
            msgs2 = await event.client.get_messages(botfather, limit=2)
            del_msg = None
            for msg2 in msgs2:
                if msg2.buttons:
                    del_msg = msg2
                    break
            # ابحث عن زر الحذف المناسب
            del_button = None
            for row in del_msg.buttons:
                for btn in row:
                    if hasattr(btn, 'data') and btn.data and btn.data.endswith(b'/del'):
                        del_button = btn
                        break
                if del_button:
                    break
            if not del_button:
                continue
            # اضغط على زر الحذف
            await event.client(
                functions.messages.GetBotCallbackAnswerRequest(
                    botfather,
                    del_msg.id,
                    data=del_button.data
                )
            )
            await asyncio.sleep(2)
            # تأكيد الحذف (عادة برسالة Yes, I am totally sure.)
            await event.client.send_message(botfather, "Yes, I am totally sure.")
            await asyncio.sleep(3)
            deleted.append(button.text)
        # بعد دورة واحدة أعد جلب قائمة البوتات من جديد
    await event.edit("تم حذف جميع البوتات:\n" + "\n".join(deleted) if deleted else "لم يتم العثور على بوتات أو تم حذفها جميعاً.")