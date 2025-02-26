from telethon import events
import random, re
from JoKeRUB.utils import admin_cmd
import asyncio 
from JoKeRUB import l313l
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
import os
import datetime
from JoKeRUB import *
import openai

@l313l.on(admin_cmd(pattern="رسم مربع (\d+)"))
async def draw_square(event):
    try:
        size = int(event.pattern_match.group(1).strip())
        if size < 1:
            return await event.edit("يرجى توفير حجم أكبر من 0.")

        square = ""
        for i in range(size):
            square += "█" * size + "\n"

        await event.edit(f"تم رسم مربع بحجم {size}:\n\n{square}")
    except ValueError:
        await event.edit("يرجى توفير حجم صحيح.")
