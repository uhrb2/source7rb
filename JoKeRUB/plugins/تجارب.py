from telethon import events
import random, re
from JoKeRUB.utils import admin_cmd
import asyncio
from JoKeRUB import l313l
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
import os
import datetime
from JoKeRUB import *

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

# --- الكود الجديد لحفظ الصوتيات ---
@l313l.on(events.NewMessage(incoming=True))
async def save_voice_message(event):
    # التأكد أن الحفظ مفعل وأن الرسالة تحتوي على صوتية
    if not gvarstatus("savevoiceforme"):
        return
    if not event.voice:
        return
    # إنشاء مجلد للحفظ إذا لم يكن موجود
    save_dir = "voice_notes"
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    # تسمية الملف بناءً على رقم الرسالة وتاريخ اليوم
    date_str = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"{save_dir}/voice_{event.id}_{date_str}.ogg"
    try:
        await event.download_media(file=file_name)
        # يمكنك إرسال رسالة تأكيد أو بدونها حسب رغبتك
        # await event.reply(f"تم حفظ الصوتية باسم {file_name}")
    except Exception as e:
        await event.reply(f"حدث خطأ أثناء حفظ الصوتية: {e}")