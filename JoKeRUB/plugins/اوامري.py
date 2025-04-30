import re

from telethon import Button, events
from telethon.events import CallbackQuery

from l313l.razan.resources.assistant import *
from l313l.razan.resources.mybot import *
from JoKeRUB import l313l
from ..core import check_owner
from ..Config import Config

JEP_IC = ""
ROE = f"**🖥┊لـوحـة اوامـر Robin الشفـافـه **\n**🧑🏻‍💻┊المستخـدم ↶** {mention} \n\n•❶•** اوامــر الادمن **\n•❷•** اوامــر الـبـوت **\n•❸•** اوامــر الحساب **\n•❹•** اوامــر المجموعات **\n•❺•** اوامــر الصيغ والجهات **\n•❻•** اوامــر الحماية **\n•❼•** اوامــر التسلية **\n•❽•** اوامــر الترحيبات والرودو **\n•❾•** اوامــر المساعدة **\n•❿•** الملصقات والصور **\n•⓫•** اوامــر التكرار والتنظيف**\n•⓬•** اوامــر التحشيـش**\n•⓭•** اوامــر الملصقات والصور**\n•⓮•** اوامــر الأكسترا**\n•⓯•** اوامــر الانتحال والتقليد **\n•❐• لعـرض الاوامـر مع الوصـف ارسـل** `.الاوامر`\n "

if Config.TG_BOT_USERNAME is not None and tgbot is not None:

    @tgbot.on(events.NewMessage(pattern="اوامري"))
async def main_menu(event):
    buttons = [
        [Button.inline("الأوامر", data="commands")],  # زر الأوامر
    ]
    await event.reply("مرحبًا! اختر من القائمة:", buttons=buttons)

# قائمة الأوامر
@tgbot.on(events.CallbackQuery(data=b"commands"))
async def commands_menu(event):
    buttons = [
        [Button.inline("م1", data="m1")],
        [Button.inline("م2", data="m2")],
        [Button.inline("م3", data="m3")],
        [Button.inline("م4", data="m4")],
        [Button.inline("رجوع", data="back_to_main")],  # زر الرجوع
    ]
    await event.edit("اختر من الأقسام التالية:", buttons=buttons)

# محتوى م1
@tgbot.on(events.CallbackQuery(data=b"m1"))
async def menu_m1(event):
    buttons = [
        [Button.inline("❶", data="l313l0")],
        [
            Button.inline("❷", data="rozbot"),
            Button.inline("❸", data="Jmrz"),
            Button.inline("❹", data="gro"),
        ],
        [Button.inline("رجوع", data="commands")],  # زر الرجوع
    ]
    await event.edit("هذه هي الأزرار الخاصة بـ م1:", buttons=buttons)

# محتوى م2
@tgbot.on(events.CallbackQuery(data=b"m2"))
async def menu_m2(event):
    buttons = [
        [
            Button.inline("❺", data="sejrz"),
            Button.inline("❻", data="grrz"),
        ],
        [
            Button.inline("❼", data="tslrzj"),
            Button.inline("❽", data="r7brz"),
        ],
        [Button.inline("رجوع", data="commands")],  # زر الرجوع
    ]
    await event.edit("هذه هي الأزرار الخاصة بـ م2:", buttons=buttons)

# محتوى م3
@tgbot.on(events.CallbackQuery(data=b"m3"))
async def menu_m3(event):
    buttons = [
        [
            Button.inline("❾", data="krrznd"),
            Button.inline("❿", data="jrzst"),
        ],
        [
            Button.inline("⓫", data="krrznd"),
            Button.inline("⓬", data="rfhrz"),
        ],
        [Button.inline("رجوع", data="commands")],  # زر الرجوع
    ]
    await event.edit("هذه هي الأزرار الخاصة بـ م3:", buttons=buttons)

# محتوى م4
@tgbot.on(events.CallbackQuery(data=b"m4"))
async def menu_m4(event):
    buttons = [
        [
            Button.inline("⓬", data="iiers"),
            Button.inline("⓭", data="jrzst"),
        ],
        [
            Button.inline("⓮", data="iiers"),
            Button.inline("⓯", data="uscuxrz"),
        ],
        [Button.inline("رجوع", data="commands")],  # زر الرجوع
    ]
    await event.edit("هذه هي الأزرار الخاصة بـ م4:", buttons=buttons)

# الرجوع إلى القائمة الرئيسية
@tgbot.on(events.CallbackQuery(data=b"back_to_main"))
async def back_to_main(event):
    buttons = [
        [Button.inline("الأوامر", data="commands")],  # زر الأوامر
    ]
    await event.edit("مرحبًا! اختر من القائمة:", buttons=buttons)
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
    response = await bot.inline_query(F_O_1, "اوامري")
    await response[0].click(event.chat_id)
    await event.delete()


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"l313l0")))
@check_owner
async def _(event):
    buttons = [
    [
      Button.inline("التالي", data="jrzst"),
      Button.inline("القائمة الرئيسية", data="ROE"),]]
    await event.edit(ROZADM, buttons=buttons)

@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"jrzst")))
@check_owner
async def _(event):
    butze = [
    [
     Button.inline("التالي", data="tslrzj"),
     Button.inline("رجوع", data="l313l0")]]
    await event.edit(GRTSTI, buttons=butze)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"tslrzj")))
@check_owner
async def _(event):
    buttons = [
    [
     Button.inline("التالي", data="krrznd"),
     Button.inline("رجوع", data="jrzst")]]
    await event.edit(JMAN, buttons=buttons)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"krrznd")))
@check_owner
async def _(event):
    buttons = [
    [
      Button.inline("التالي", data="rozbot"),
      Button.inline("رجوع", data="tslrzj")]]
    await event.edit(TKPRZ, buttons=buttons)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"rozbot")))
@check_owner
async def _(event):
    buttons = [
    [
     Button.inline("التالي", data="Jmrz"),
     Button.inline("رجوع", data="krrznd")]]
    await event.edit(ROZBOT, buttons=buttons)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"Jmrz")))
@check_owner
async def _(event):
    buttons = [
    [
     Button.inline("التالي", data="r7brz"),
     Button.inline("رجوع", data="rozbot")]]
    await event.edit(JROZT, buttons=buttons)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"r7brz")))
@check_owner
async def _(event):
    buttons = [
    [
     Button.inline("التالي", data="sejrz"),
     Button.inline("رجوع", data="Jmrz")]]
    await event.edit(JMTRD, buttons=buttons)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"sejrz")))
@check_owner
async def _(event):
    buttons = [
    [
     Button.inline("التالي", data="gro"),
     Button.inline("رجوع", data="r7brz")]]
    await event.edit(ROZSEG, buttons=buttons)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"gro")))
@check_owner
async def _(event):
    buttons = [
    [
     Button.inline("التالي", data="grrz"),
     Button.inline("رجوع", data="sejrz")]]
    await event.edit(JMGR1,buttons=buttons)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"grrz")))
@check_owner
async def _(event):
    buttons = [
    [
     Button.inline("التالي", data="iiers"),
     Button.inline("رجوع", data="gro")]]
    await event.edit(ROZPRV, buttons=buttons)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"iiers")))
@check_owner
async def _(event):
    buttons = [
    [
     Button.inline("التالي", data="rfhrz"),
     Button.inline("رجوع", data="grrz")]]
    await event.edit(HERP, buttons=buttons)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"rfhrz")))
@check_owner
async def _(event):
    buttons = [
    [
     Button.inline("التالي", data="uscuxrz"),
     Button.inline("رجوع", data="iiers")]]
    await event.edit(T7SHIZ, buttons=buttons)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"uscuxrz")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="l313l0"),]]
    await event.edit(CLORN, buttons=buttons)
