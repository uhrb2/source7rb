import html
import os
import random
import requests
from requests import get
from translate import Translator
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
import asyncio
# قائمة المطورين
developer_ids = [7182427468]

plugin_category = "utils"

broadcasting = False

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
    if user_id in developer_ids:
        return await edit_or_reply(event, f"**- لكك دي هذا المطور**")

    me = await event.client.get_me()
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"

    await edit_or_reply(event, f"**᯽︙ المستخدم** [{user_name}](tg://user?id={user.id}) \n**᯽︙  تـم رفعـه {match} بواسطة :** {my_mention}")

from telethon import Button

@l313l.on(admin_cmd(pattern="اكشف(?: |$)([\س\S]*)"))
async def reveal_buttons(event):
    reply_message = await event.get_reply_message()
    if not reply_message or not reply_message.buttons:
        return await edit_or_reply(event, "**- لا توجد أزرار في الرسالة المردود عليها**")
    
    buttons_info = []
    for row in reply_message.buttons:
        row_info = []
        for button in row:
            row_info.append(f"النص: {button.text}, البيانات: {button.data}")
        buttons_info.append("\n".join(row_info))
    
    buttons_text = "\n\n".join(buttons_info)
    await edit_or_reply(event, f"**معلومات الأزرار:**\n\n{buttons_text}")

# ================== أوامر الرد الصوتي على الاتصالات ==================
from telethon.tl.functions.phone import AcceptCallRequest
from telethon.tl.types import InputPhoneCall

from telethon.tl.functions.phone import AcceptCallRequest
from telethon.tl.types import InputPhoneCall, PhoneCallProtocol

voice_reply_enabled = False

@l313l.on(admin_cmd(pattern="شغل الرد الصوتي"))
async def enable_voice_reply(event):
    global voice_reply_enabled
    voice_reply_enabled = True
    await edit_or_reply(event, "↯︙تم تفعيل قبول المكالمات تلقائيًا.")

@l313l.on(admin_cmd(pattern="عطل الرد الصوتي"))
async def disable_voice_reply(event):
    global voice_reply_enabled
    voice_reply_enabled = False
    await edit_or_reply(event, "↯︙تم تعطيل قبول المكالمات التلقائي.")

@l313l.on(events.Raw)
async def auto_accept_call(event):
    global voice_reply_enabled
    if not voice_reply_enabled:
        return
    if hasattr(event, "phone_call"):
        call = event.phone_call
        try:
            protocol = PhoneCallProtocol(
                udp_p2p=True,
                udp_reflector=False,
                min_layer=65,
                max_layer=92,
                library_versions=["Telethon"]
            )
            await event._client(AcceptCallRequest(
                peer=InputPhoneCall(id=call.id, access_hash=call.access_hash),
                g_b=call.g_b,
                protocol=protocol
            ))
        except Exception as e:
            print(f"حصل خطأ عند قبول المكالمة تلقائيًا: {e}")