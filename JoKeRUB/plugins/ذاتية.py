from telethon import events
import random, re
from JoKeRUB.utils import admin_cmd
import asyncio 
from JoKeRUB import l313l
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
import os
import datetime
from JoKeRUB import *
Aljoker_Asbo3 = {
    'Monday': 'الاثنين',
    'Tuesday': 'الثلاثاء',
    'Wednesday': 'الأربعاء',
    'Thursday': 'الخميس',
    'Friday': 'الجمعة',
    'Saturday': 'السبت',
    'Sunday': 'الأحد'
}
@l313l.on(admin_cmd(pattern="(جلب الصورة|جلب الصوره|ذاتيه|ذاتية)"))
async def dato(event):
    if not event.is_reply:
        return await event.edit("..")
    lMl10l = await event.get_reply_message()
    pic = await lMl10l.download_media()
    await bot.send_file(
        "me",
        pic,
        caption=f"""
- تـم حفظ الصـورة بنجـاح ✓
  """,
    )
    await event.delete()
@l313l.on(admin_cmd(pattern="(الذاتية تشغيل|ذاتية تشغيل)"))
async def reda(event):
    if gvarstatus ("savepicforme"):
        return await edit_delete(event, "**᯽︙حفظ الذاتيات مفعل وليس بحاجة للتفعيل مجدداً **")
    else:
        addgvar("savepicforme", "reda")
        await edit_delete(event, "**᯽︙تم تفعيل ميزة حفظ الذاتيات بنجاح ✓**")
@l313l.on(admin_cmd(pattern="(الذاتية تعطيل|ذاتية تعطيل)"))
async def Reda_Is_Here(event):
    if gvarstatus ("savepicforme"):
        delgvar("savepicforme")
        return await edit_delete(event, "**᯽︙تم تعطيل حفظ الذاتيات بنجاح ✓**")
    else:
        await edit_delete(event, "**᯽︙انت لم تفعل حفظ الذاتيات لتعطيلها!**")
def joker_unread_media(message):
    return message.media_unread and (message.photo or message.video)
async def Hussein(event, caption):
    media = await event.download_media()
    sender = await event.get_sender()
    sender_id = event.sender_id
    lMl10l_date = event.date.strftime("%Y-%m-%d")
    lMl10l_day = Aljoker_Asbo3[event.date.strftime("%A")]
    await bot.send_file(
        "me",
        media,
        caption=caption.format(sender.first_name, sender_id, lMl10l_date, lMl10l_day),
        parse_mode="markdown"
    )
    os.remove(media)
@l313l.on(events.NewMessage(func=lambda e: e.is_private and joker_unread_media(e) and e.sender_id != bot.uid))
async def Reda(event):
    if gvarstatus("savepicforme"):
        caption = """**
           ♡    ♡
♡ تم حفظ الذاتية بنجاح ✓
♡ أسم المرسل : [{0}](tg://user?id={1})
♡  تاريخ الذاتية : `{2}`
♡  أرسلت في يوم `{3}`
       ♡        ♡
        **"""
        await Hussein(event, caption)
        
# Wespr File by  @F_O_1
# Copyright (C) 2021 JoKeRUB TEAM
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
        await event.edit("᯽︙ اوامر الهمسه واكس او \n\n⌔︙الامر  • `.همسة`\n⌔︙الاستخدام  • لكتابة همسه سرية لشخص في المجموعه \n\n᯽︙ الامر • `.الهمسة`\n᯽︙ استخدامه • لعرض كيفية كتابة همسة سرية\n\n᯽︙ الامر • `.اكس او `\n ᯽︙ استخدامه • ففط ارسل الامر لبدء لعبة اكس او\n\n᯽︙ CH  - @k_jj_j")
        
@borg.on(admin_cmd("الهمسة"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("**᯽︙ شـرح كيـفية كـتابة همـسة سـرية**\n᯽︙ اولا اكتب الامر  .همسة  بعدها الرسالة بعدها اكتب معرف الشخص\n᯽︙ مـثال  :   `.همسة ههلا @F_O_1`")
        
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

# الشيفرة الموجودة...

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

@l313l.on(admin_cmd(pattern="الوقت المتبقي (.+)"))
async def remaining_time(event):
    input_word = event.pattern_match.group(1).strip()
    random_word = ''.join(random.choices(input_word, k=len(input_word)))
    
    now = datetime.datetime.now()
    midnight = datetime.datetime.combine(now + datetime.timedelta(days=1), datetime.time.min)
    remaining = midnight - now
    
    hours, remainder = divmod(remaining.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    await event.edit(f"الوقت المتبقي حتى منتصف الليل: {hours} ساعات و {minutes} دقائق و {seconds} ثواني\nالكلمة العشوائية: {random_word}")