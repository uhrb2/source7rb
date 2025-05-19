#    جميع الحقوق لمطوري سورس روبن حصريا لهم فقط
#    اذا تخمط الملف اذك الحقوق وكاتبيه ومطوريه لا تحذف الحقوق وتصير فاشل 👍
#    كتابة الشسد 
import asyncio
import io
import re
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

from telethon.tl.types import MessageEntityCustomEmoji
from userbot.events import admin_cmd
from userbot import l313l  # تأكد من أن هذا هو اسم الـ client عندك

from telethon.tl.types import MessageEntityCustomEmoji
from userbot.events import admin_cmd
from userbot import l313l  # تأكد من اسم الكلاينت
from userbot.utils import getgvar

from telethon.tl.types import MessageEntityCustomEmoji
from userbot import l313l
from userbot.events import admin_cmd
from userbot.utils import getgvar

@l313l.on(admin_cmd(pattern="(هلو)"))
async def hello_handler(event):
    if getgvar("auto_respond_enabled", "disabled") == "enabled":
        await event.edit(
            "🎙 هلوات",
            entities=[
                MessageEntityCustomEmoji(
                    offset=0,
                    length=1,
                    document_id=5776309943116241193  # هذا هو ID الإيموجي المميز
                )
            ]
        )