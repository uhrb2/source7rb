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