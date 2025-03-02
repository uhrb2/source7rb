from telethon import events
import random, re
from JoKeRUB.utils import admin_cmd
import asyncio 
from JoKeRUB import l313l
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
import os
import datetime
from JoKeRUB import *
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
الرد على الرسالة

# دالة جديدة للحصول على أوقات الصلاة
async def get_prayer_times(event, country, city):
    api_url = 'http://api.aladhan.com/v1/timingsByCity'
    params = {
        'city': city,
        'country': country,
        'method': 2  # يمكنك تغيير طريقة الحساب إذا لزم الأمر
    }
    response = requests.get(api_url, params=params)
    data = response.json()
    if response.status_code == 200 and data['code'] == 200:
        timings = data['data']['timings']
        message = f"أوقات الصلاة في {city}, {country} خلال رمضان:\n"
        for prayer, time in timings.items():
            message += f"{prayer}: {time}\n"
        await event.reply(message)
    else:
        await event.reply("فشل في جلب أوقات الصلاة.")

# الأمر الجديد
@l313l.on(events.NewMessage(pattern=r"^رمضان\+(\w+)\+(\w+)$"))
async def ramadan_prayer_times(event):
    match = re.match(r"رمضان\+(\w+)\+(\w+)$", event.text)
    if match:
        country = match.group(1)
        city = match.group(2)
        await get_prayer_times(event, country, city)
    else:
        await event.reply("الصيغة غير صحيحة. يرجى استخدام رمضان+الدولة+المكان")

if __name__ == '__main__':
    main()