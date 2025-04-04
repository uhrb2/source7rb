#    جميع الحقوق لمطوري سورس روبن حصريا لهم فقط
#    اذا تخمط الملف اذك الحقوق وكاتبيه ومطوريه لا تحذف الحقوق وتصير فاشل 👍
#    كتابة الشسد 
import asyncio
import io
import re

from telethon import Button, custom, events
from telethon.tl.functions.users import GetFullUserRequest
from JoKeRUB import bot
from JoKeRUB.sql_helper.blacklist_assistant import (
    add_nibba_in_db,
    is_he_added,
    removenibba,
)
from JoKeRUB.sql_helper.botusers_sql import add_me_in_db, his_userid
from JoKeRUB.sql_helper.idadder_sql import (
    add_usersid_in_db,
    already_added,
    get_all_users,
)
from l313l.razan.resources.assistant import *

# start
@tgbot.on(events.NewMessage(pattern="^/con"))
async def handle_con_command(event):
    buttons = [
        [Button.inline("تقليد", data="mimic")]
    ]
    await event.reply("اختر أحد الأزرار:", buttons=buttons)

@tgbot.on(events.CallbackQuery(data="mimic"))
async def handle_mimic_button(event):
    await event.edit("سوف أقوم بتقليدك الآن، ارسل أي رسالة.")
    tgbot.add_event_handler(mimic_user, events.NewMessage(from_users=event.sender_id))

async def mimic_user(event):
    await event.reply(event.text)