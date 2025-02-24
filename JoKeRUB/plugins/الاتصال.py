from telethon import events
from telethon.tl.types import InputPhoneCall
from telethon.tl.functions.phone import DiscardCall
from ..Config import Config
from JoKeRUB.utils import admin_cmd
from JoKeRUB import l313l
import os

# Initialize variables
voice_message_path = "default_voice_message.ogg"
feature_enabled = True

@l313l.on(admin_cmd(pattern="تفعيل الرسالة الصوتية"))
async def enable_voice_message(event):
    global feature_enabled
    feature_enabled = True
    await event.edit("تم تفعيل الرسالة الصوتية عند عدم الرد.")

@l313l.on(admin_cmd(pattern="تعطيل الرسالة الصوتية"))
async def disable_voice_message(event):
    global feature_enabled
    feature_enabled = False
    await event.edit("تم تعطيل الرسالة الصوتية عند عدم الرد.")

@l313l.on(admin_cmd(pattern="إضافة بصمة صوتية"))
async def add_voice_message(event):
    if not event.is_reply:
        return await event.edit("يرجى الرد على الرسالة الصوتية لإضافتها.")
    reply_message = await event.get_reply_message()
    voice = await reply_message.download_media()
    global voice_message_path
    voice_message_path = voice
    await event.edit("تم إضافة البصمة الصوتية بنجاح.")

@l313l.on(admin_cmd(pattern="تغيير بصمة صوتية"))
async def change_voice_message(event):
    if not event.is_reply:
        return await event.edit("يرجى الرد على الرسالة الصوتية لتغييرها.")
    reply_message = await event.get_reply_message()
    voice = await reply_message.download_media()
    global voice_message_path
    voice_message_path = voice
    await event.edit("تم تغيير البصمة الصوتية بنجاح.")

# Function to handle unanswered calls
@l313l.on(events.Raw)
async def unanswered_call_handler(event):
    if feature_enabled and isinstance(event, InputPhoneCall):
        sender = await event.get_sender()
        await event.client(DiscardCall(call=event))
        await event.client.send_file(sender.id, voice_message_path, caption="هذه رسالة صوتية تلق