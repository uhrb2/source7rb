import html
import os
import random
from requests import get
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

plugin_category = "utils"

# قائمة لحفظ رتب المستخدمين
user_ranks = {}

@l313l.on(admin_cmd(pattern="رفع(?: |$)([\s\S]*)"))
async def promote_user(event):
    match = event.pattern_match.group(1).strip()
    if not match:
        return await event.respond("**- يرجى تحديد الدور المطلوب**")
    
    user, custom = await get_user_from_event(event)
    if not user:
        return await event.respond("**- لـم استطـع العثــور ع الشخــص**")

    user_id = user.id
    user_name = user.first_name.replace("\u2060", "") if user.first_name else user.username

    # تحقق من عدم رفع المطور
    if user_id in [7182427468]:
        return await event.respond(f"**- لكك دي هذا المطور**")
    
    me = await event.client.get_me()
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"

    # تحديث رتبة المستخدم
    user_ranks[user_id] = match

    await event.respond(f"**᯽︙ المستخدم** [{user_name}](tg://user?id={user.id}) \n**᯽︙  تـم رفعـه {match} بواسطة :** {my_mention}")