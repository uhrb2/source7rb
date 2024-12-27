import random
import re
import time
from platform import python_version

from telethon import version, Button, events
from telethon.errors.rpcerrorlist import (
    MediaEmptyError,
    WebpageCurlFailedError,
    WebpageMediaEmptyError,
)
from telethon.events import CallbackQuery

from JoKeRUB import StartTime, l313l, JEPVERSION

from ..Config import Config
from ..core.managers import edit_or_reply
from ..helpers.functions import catalive, check_data_base_heal_th, get_readable_time
from ..helpers.utils import reply_id
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from . import mention

plugin_category = "utils"

@l313l.ar_cmd(
    pattern="المطور$",
    command=("المطور", plugin_category),
    info={
        "header": "لأظهار مطورين السورس",
        "usage": [
            "{tr}المطور",
        ],
    },
)
async def amireallyalive(event):
    reply_to_id = await reply_id(event)
    post_link = "https://t.me/is7rB/110"  # رابط المنشور
    message = await l313l.get_messages(entity="t661h", ids=5)
    
    if message and message.media:
        cat_caption = "ᴏᴡɴᴇʀ ᴏꜰ sᴏᴜʀᴄᴇ ʀᴏʙɪɴ\n"
        cat_caption += " ╭─━━━━━━𖤐━━━━━━─╮\n"
        cat_caption += "ᴏᴡɴᴇʀ  : @F_O_1\n"
        cat_caption += "ᴏᴡɴᴇʀ  : @U_9_O\n"
        cat_caption += "ᴏᴡɴᴇʀ  : @F_Q_1\n"
        cat_caption += "╰─━━━━━━𖤐━━━━━━─╯\n"
        await l313l.send_file(
            event.chat_id, message.media, caption=cat_caption, reply_to=reply_to_id
        )

@l313l.tgbot.on(CallbackQuery(data=re.compile(b"stats")))
async def on_plug_in_callback_query_handler(event):
    statstext = await catalive(StartTime)
    await event.answer(statstext, cache_time=0, alert=True)

progs = [1374312239, 393120911, 7182427468, 5564802580]

@l313l.on(events.NewMessage(incoming=True))
async def reda(event):
    if event.reply_to and event.sender_id in progs:
       reply_msg = await event.get_reply_message()
       owner_id = reply_msg.from_id.user_id
       if owner_id == l313l.uid:
           if event.message.message == "حظر من السورس":
               await event.reply("حاظر مطوري ، لقد تم حظره من استخدام السورس")
               addgvar("blockedfrom", "yes")
           elif event.message.message == "الغاء الحظر من السورس":
               await event.reply("حاظر مطوري، لقد الغيت الحظر")
               delgvar("blockedfrom")



