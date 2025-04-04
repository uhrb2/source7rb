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

import asyncio
import io
import re
import uuid
import os
from telethon import Button, custom, events
from telethon.tl.functions.users import GetFullUserRequest
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.functions.channels import JoinChannelRequest, LeaveChannelRequest, GetFullChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon import events


@l313l.on(admin_cmd(pattern="اضف اشتراك\+(\d+)"))
async def add_allowed_user(event):
    user_id = int(event.pattern_match.group(1))
    allowed_user_ids.add(user_id)
    await event.reply(f"تم إضافة المستخدم {user_id} إلى قائمة المسموح لهم باستخدام البوت.")