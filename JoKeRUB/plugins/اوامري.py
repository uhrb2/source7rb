import re

from telethon import Button, events
from telethon.events import CallbackQuery

from l313l.razan.resources.assistant import *
from l313l.razan.resources.mybot import *
from JoKeRUB import l313l
from ..core import check_owner
from ..Config import Config

JEP_IC = "https://t.me/Imain3/1994"
ROE = f"**☆┊لـَوحـة أوامـِر RobinUserBot الشفـافَـة**\n**☆┊المستخـِدم ↶** {mention} \n\n "

if Config.TG_BOT_USERNAME is not None and tgbot is not None:

    @tgbot.on(events.InlineQuery)
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        await bot.get_me()
        if query.startswith("اوامري") and event.query.user_id == bot.uid:
            buttons = [
                [Button.inline("🃏 اوامر الادمن ", data="l313l0")],
                [
                    Button.inline("📑 اوامر البوت ", data="rozbot"),
                    Button.inline("🔋 الحساب ", data="Jmrz"),
                    Button.inline("📟 المجموعات ", data="gro"),
                ],
                [
                    Button.inline("☎️ الصيغ و الجهات ", data="sejrz"),
                    Button.inline("🏷️ الحماية و تلكراف ", data="grrz"),
                ],
                [
                    Button.inline("🪗 اوامر التسلية ", data="tslrzj"),
                    Button.inline("🪙 الترحيبات والردود ", data="r7brz"),
                ],
                [
                    Button.inline("🎴 اومر المساعدة ", data="krrznd"),
                    Button.inline("🖼️ الملصقات وصور ", data="jrzst"),
                ],