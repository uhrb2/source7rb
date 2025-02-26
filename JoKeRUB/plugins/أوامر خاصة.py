from telethon import events
import random, re
from JoKeRUB.utils import admin_cmd
import asyncio 
from JoKeRUB import l313l
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
import os
import datetime
from JoKeRUB import *

@borg.on(
    admin_cmd(pattern="لايك ?(.*)")
)
async def wspr(event):
    if event.fwd_from:
        return
    l313lb = event.pattern_match.group(1)
    rrrd7 = "@like"
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    tap = await bot.inline_query(rrrd7, l313lb) 
    await tap[0].click(event.chat_id)
    await event.delete()

@borg.on(admin_cmd("م27"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("᯽︙ اوامر الهمسه واكس او \n\n⌔︙الامر  • `.همسة`\n⌔︙الاستخدام  • لكتابة همسه سرية لشخص في المجم[...]