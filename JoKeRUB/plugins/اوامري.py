import re
from telethon import Button, events
from telethon.events import CallbackQuery
from l313l.razan.resources.assistant import *
from l313l.razan.resources.mybot import *
from JoKeRUB import l313l
from ..core import check_owner
from ..Config import Config

JEP_IC = "https://i.top4top.io/p_3341a91a10.jpg"
ROE = f"☆┊لـَوحـة أوامـِر RobinUserBot الشفـافَـة\n☆┊المستخـِدم ↶ {mention} \n\n "

if Config.TG_BOT_USERNAME is not None and tgbot is not None:

   from telethon import events, Button

@tgbot.on(events.InlineQuery)
async def inline_handler(event):
    builder = event.builder
    query = event.text
    await bot.get_me()

    if query.startswith("اوامري") and event.query.user_id == bot.uid:
        buttons = [
            [Button.url("🌐 قناة السورس", "https://t.me/RobinUserBot")],
            [Button.inline("🤖 أوامر البوت", data="bot_commands")],
            [Button.inline("📋 الأوامر", data="main_commands")],
        ]
        await event.answer(
            results=[
                builder.article(
                    title="اوامري",
                    text="اختر أحد الخيارات من القائمة:",
                    buttons=buttons,
                    link_preview=False
                )
            ],
            cache_time=0
        )

@tgbot.on(events.CallbackQuery(data="bot_commands"))
async def bot_commands_handler(event):
    buttons = [[Button.inline("🔙 رجوع", data="back_to_main")]]
    await event.edit(
        text="🤖 وظائف أوامر البوت:\n- وظيفة 1\n- وظيفة 2\n- وظيفة 3",
        buttons=buttons
    )

@tgbot.on(events.CallbackQuery(data="main_commands"))
async def main_commands_handler(event):
    buttons = [
        [Button.inline("أمر 1", data="command_1"), Button.inline("أمر 2", data="command_2")],
        [Button.inline("أمر 3", data="command_3"), Button.inline("أمر 4", data="command_4")],
        [Button.inline("🔙 رجوع", data="back_to_main")]
    ]
    await event.edit(
        text="📋 قائمة الأوامر:",
        buttons=buttons
    )

@tgbot.on(events.CallbackQuery(data="back_to_main"))
async def back_to_main_handler(event):
    buttons = [
        [Button.url("🌐 قناة السورس", "https://t.me/RobinUserBot")],
        [Button.inline("🤖 أوامر البوت", data="bot_commands")],
        [Button.inline("📋 الأوامر", data="main_commands")],
    ]
    await event.edit(
        text="اختر أحد الخيارات من القائمة:",
        buttons=buttons
    )

            if JEP_IC and JEP_IC.endswith((".jpg", ".png", "gif", "mp4")):
                result = builder.photo(
                    JEP_IC, text=ROE, buttons=buttons, link_preview=False
                )
            elif JEP_IC:
                result = builder.document(
                    JEP_IC,
                    title="JoKeRUB",
                    text=ROE,
                    buttons=buttons,
                    link_preview=False,
                )
            else:
                result = builder.article(
                    title="JoKeRUB",
                    text=ROE,
                    buttons=buttons,
                    link_preview=False,
                )
            await event.answer([result] if result else None)


@bot.on(admin_cmd(outgoing=True, pattern="اوامري"))
async def repo(event):
    if event.fwd_from:
        return
    F_O_1 = Config.TG_BOT_USERNAME
    if event.reply_to_msg_id:
        await event.get_reply_message()
    try:
        response = await bot.inline_query(F_O_1, "اوامري")
        await response[0].click(event.chat_id)
    except telethon.errors.rpcerrorlist.BotResponseTimeoutError:
        await event.reply("البوت لم يستجب في الوقت المحدد. يرجى المحاولة مرة أخرى لاحقًا.")
    finally:
        await event.delete()


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"l313l0")))
@check_owner
async def _(event):
    buttons = [
    [
      Button.inline("⏭️ التالي", data="jrzst"),
      Button.inline("🏠 القائمة الرئيسية", data="ROE"),]]
    await event.edit(ROZADM, buttons=buttons)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"jrzst")))
@check_owner
async def _(event):
    butze = [
    [
     Button.inline("⏭️ التالي", data="tslrzj"),
     Button.inline("↩️ رجوع", data="l313l0")]]
    await event.edit(GRTSTI, buttons=butze)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"tslrzj")))
@check_owner
async def _(event):
    buttons = [
    [
     Button.inline("⏭️ التالي", data="krrznd"),
     Button.inline("↩️ رجوع", data="jrzst")]]
    await event.edit(JMAN, buttons=buttons)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"krrznd")))
@check_owner
async def _(event):
    buttons = [
    [
      Button.inline("⏭️ التالي", data="rozbot"),
      Button.inline("↩️ رجوع", data="tslrzj")]]
    await event.edit(TKPRZ, buttons=buttons)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"rozbot")))
@check_owner
async def _(event):
    buttons = [
    [
     Button.inline("⏭️ التالي", data="Jmrz"),
     Button.inline("↩️ رجوع", data="krrznd")]]
    await event.edit(ROZBOT, buttons=buttons)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"Jmrz")))
@check_owner
async def _(event):
    buttons = [
    [
     Button.inline("⏭️ التالي", data="r7brz"),
     Button.inline("↩️ رجوع", data="rozbot")]]
    await event.edit(JROZT, buttons=buttons)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"r7brz")))
@check_owner
async def _(event):
    buttons = [
    [
     Button.inline("⏭️ التالي", data="sejrz"),
     Button.inline("↩️ رجوع", data="Jmrz")]]
    await event.edit(JMTRD, buttons=buttons)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"sejrz")))
@check_owner
async def _(event):
    buttons = [
    [
     Button.inline("⏭️ التالي", data="gro"),
     Button.inline("↩️ رجوع", data="r7brz")]]
    await event.edit(ROZSEG, buttons=buttons)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"gro")))
@check_owner
async def _(event):
    buttons = [
    [
     Button.inline("⏭️ التالي", data="grrz"),
     Button.inline("↩️ رجوع", data="sejrz")]]
    await event.edit(JMGR1,buttons=buttons)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"grrz")))
@check_owner
async def _(event):
    buttons = [
    [
     Button.inline("⏭️ التالي", data="iiers"),
     Button.inline("↩️ رجوع", data="gro")]]
    await event.edit(ROZPRV, buttons=buttons)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"iiers")))
@check_owner
async def _(event):
    buttons = [
    [
     Button.inline("⏭️ التالي", data="rfhrz"),
     Button.inline("↩️ رجوع", data="grrz")]]
    await event.edit(HERP, buttons=buttons)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"rfhrz")))
@check_owner
async def _(event):
    buttons = [
    [
     Button.inline("⏭️ التالي", data="uscuxrz"),
     Button.inline("↩️ رجوع", data="iiers")]]
    await event.edit(T7SHIZ, buttons=buttons)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"uscuxrz")))
@check_owner
async def _(event):
    buttons = [[Button.inline("↩️ رجوع", data="l313l0"),]]
    await event.edit(CLORN, buttons=buttons)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"source_channels")))
@check_owner
async def _(event):
    await event.edit("📺 قنوات السورس:\n1. قناة 1\n2. قناة 2\n3. قناة 3")