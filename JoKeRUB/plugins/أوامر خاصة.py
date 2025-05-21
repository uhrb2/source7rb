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

client.parse_mode = AaycoBot()

from telethon import events

@bot.on(events.NewMessage(pattern=r'\.هلو'))
async def hello_3yoon(event):
    event.reply('[🫥](tg://emoji?id=6327735399770752519)')