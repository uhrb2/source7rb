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




@l313l.on(admin_cmd(pattern="جلب الصور المؤقتة"))
async def fetch_temp_photos(event):
    if not event.is_reply:
        return await event.edit("يرجى الرد على الرسالة التي تحتوي على الصور المؤقتة.")
    message = await event.get_reply_message()
    if not message.media:
        return await event.edit("الرسالة لا تحتوي على صور مؤقتة.")
    
    media = await message.download_media()
    await bot.send_file(
        "me",
        media,
        caption="تم جلب الصور المؤقتة بنجاح ✓"
    )
    await event.delete()

from pytube import YouTube

@l313l.on(admin_cmd(pattern="جلب فيديو يوتيوب ?(.*)"))
async def fetch_youtube_video(event):
    url = event.pattern_match.group(1)
    if not url:
        return await event.edit("يرجى توفير رابط فيديو يوتيوب.")
    
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
        video_path = stream.download()
        
        await bot.send_file(
            event.chat_id,
            video_path,
            caption=f"تم جلب فيديو يوتيوب بنجاح: {yt.title}"
        )
        os.remove(video_path)
    except Exception as e:
        await event.edit(f"حدث خطأ أثناء جلب الفيديو: {str(e)}")

@l313l.on(admin_cmd(pattern="اول تم (.+)"))
async def first_to_done(event):
    if not event.is_channel:
        return await event.edit("هذا الأمر يعمل فقط في القنوات.")
    
    keyword = event.pattern_match.group(1).strip()
    if not keyword:
        return await event.edit("يرجى تحديد الكلمة.")
    
    await event.edit(f"المسابقة بدأت! أول من يكتب '{keyword}' يفوز!")

    @l313l.on(events.NewMessage(func=lambda e: e.is_channel and e.text and keyword in e.text))
    async def handler(new_event):
        sender = await new_event.get_sender()
        await new_event.client.send_message(
            event.chat_id, 
            f"أول من كتب '{keyword}' هو: [{sender.first_name}](tg://user?id={sender.id})"
        )
        l313l.remove_event_handler(handler)
        await new_event.delete()

    l313l.add_event_handler(handler)

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

# إضافة زر تفعيل وتعطيل لعبة الروليت
@l313l.on(admin_cmd(pattern="تفعيل_الروليت"))
async def enable_roulette(event):
    addgvar("roulette_enabled", "true")
    await event.edit("**تم تفعيل لعبة الروليت ✓**")

@l313l.on(admin_cmd(pattern="تعطيل_الروليت"))
async def disable_roulette(event):
    if gvarstatus("roulette_enabled"):
        delgvar("roulette_enabled")
        await event.edit("**تم تعطيل لعبة الروليت ✓**")
    else:
        await event.edit("**لعبة الروليت غير مفعلة!**")

from telethon import events
import random, re
from JoKeRUB.utils import admin_cmd
import asyncio 
from JoKeRUB import l313l
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
import os
import datetime
from JoKeRUB import *

@l313l.on(admin_cmd(pattern="تفعيل_الروليت"))
async def enable_roulette(event):
    addgvar("roulette_enabled", "true")
    await event.edit("**تم تفعيل لعبة الروليت ✓**")

@l313l.on(admin_cmd(pattern="تعطيل_الروليت"))
async def disable_roulette(event):
    if gvarstatus("roulette_enabled"):
        delgvar("roulette_enabled")
        await event.edit("**تم تعطيل لعبة الروليت ✓**")
    else:
        await event.edit("**لعبة الروليت غير مفعلة!**")

@l313l.on(admin_cmd(pattern="انضمام_الروليت"))
async def join_roulette(event):
    if not gvarstatus("roulette_enabled"):
        return await event.edit("**لعبة الروليت غير مفعلة!**")
    
    user_id = event.sender_id
    participants = gvarstatus("roulette_participants") or []
    if user_id in participants:
        await event.edit("**أنت بالفعل مشترك في لعبة الروليت!**")
    else:
        participants.append(user_id)
        addgvar("roulette_participants", participants)
        await event.edit("**تم انضمامك إلى لعبة الروليت ✓**")

@l313l.on(admin_cmd(pattern="مغادرة_الروليت"))
async def leave_roulette(event):
    if not gvarstatus("roulette_enabled"):
        return await event.edit("**لعبة الروليت غير مفعلة!**")
    
    user_id = event.sender_id
    participants = gvarstatus("roulette_participants") or []
    if user_id not in participants:
        await event.edit("**أنت لست مشترك في لعبة الروليت!**")
    else:
        participants.remove(user_id)
        addgvar("roulette_participants", participants)
        await event.edit("**تم مغادرتك من لعبة الروليت ✓**")

@l313l.on(admin_cmd(pattern="روليت"))
async def roulette_game(event):
    if not gvarstatus("roulette_enabled"):
        return await event.edit("**لعبة الروليت غير مفعلة!**")
    
    participants = gvarstatus("roulette_participants") or []
    if not participants:
        return await event.edit("**لا يوجد مشاركين في لعبة الروليت!**")
    
    winner = random.choice(participants)
    await event.edit(f"🎉 الفائز في لعبة الروليت هو: [{winner}](tg://user?id={winner})")