import random
import requests
import asyncio
from asyncio import sleep
from telethon.sync import functions
from telethon.errors import FloodWaitError
from user_agent import generate_user_agent
from JoKeRUB import l313l
from ..core.managers import edit_or_reply

trys, crys, arys, brys = [0], [0], [0], [0]
itsclim, iscuto, istuto, isbuto = ["off"], ["off"], ["off"], ["off"]

async def check_user(username):
    url = f"https://t.me/{username}"
    headers = {"User-Agent": generate_user_agent(),
               "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
               "Accept-Encoding": "gzip, deflate, br",
               "Accept-Language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}
    response = requests.get(url, headers=headers)
    if 'If you have <strong>Telegram</strong>' in response.text:
        return True
    return False

async def gen_user(choice):
    chars = {"a": "qwertyuiopasdfghjklzxcvbnm", "b": "1234567890", "e": "qwertyuiopasdfghjklzxcvbnm1234567890"}
    patterns = {
        "سداسي_حرفين1": [chars["a"][0]]*4 + [chars["e"][0]]*2,
        "سداسي_شرطه": [chars["a"][0]]*4 + ["_"] + [chars["e"][0]],
        "سداسي_حرفين2": [chars["a"][0]]*4 + [chars["e"][0]]*2,
        "سداسي_حرفين3": [chars["a"][0]]*3 + [chars["e"][0]]*2 + [chars["a"][0]],
        "سداسي_حرفين4": [chars["a"][0]]*2 + [chars["e"][0]]*2 + [chars["a"][0]]*2,
        "سداسي_حرفين5": [chars["a"][0]]*2 + [chars["e"][0]]*2 + [chars["a"][0]]*2,
        "سداسي_حرفين6": [chars["a"][0]]*2 + [chars["e"][0]]*2 + [chars["b"][0]]*2,
        "ثلاثي1": [chars["a"][0], "_", chars["e"][0], "_", chars["e"][0]],
        "ثلاثي2": [chars["a"][0], "_", chars["b"][0], "_", chars["e"][0]],
        "ثلاثي3": [chars["a"][0], "_", chars["b"][0], "_", chars["b"][0]],
        "شبه رباعي1": [chars["a"][0], "_", chars["a"][0], "_", chars["a"][0], "_", chars["e"][0]],
        "شبه رباعي2": [chars["a"][0], "_", chars["e"][0], "_", chars["e"][0], "_", chars["e"][0]],
        "شبه رباعي3": [chars["a"][0], "_", chars["e"][0], "_", chars["e"][0], "_", chars["a"][0]],
        "شبه رباعي4": [chars["a"][0], "_", chars["e"][0], "_", chars["e"][0], "_", chars["e"][0]],
        "رباعي1": [chars["a"][0]]*3 + ["_"] + [chars["e"][0]],
        "رباعي2": [chars["a"][0], "_", chars["e"][0]]*3,
        "رباعي3": [chars["a"][0]]*2 + ["_"] + [chars["e"][0]]*2,
        "رباعي4": [chars["a"][0]]*2 + ["_"] + [chars["a"][0], chars["e"][0]],
        "رباعي5": [chars["a"][0]]*2 + ["_"] + [chars["e"][0], chars["a"][0]],
        "رباعي6": [chars["a"][0], chars["e"][0]] + ["_"] + [chars["e"][0]]*2,
        "رباعي7": [chars["a"][0], chars["e"][0]] + ["_"] + [chars["a"][0], chars["e"][0]],
        "بوتات1": [chars["a"][0], chars["e"][0], "_", "b", "o", "t"],
        "بوتات2": [chars["a"][0], "_", chars["e"][0], "b", "o", "t"],
        "بوتات3": [chars["a"][0], chars["e"][0], chars["b"][0], "b", "o", "t"],
        "بوتات4": [chars["a"][0], chars["b"][0], chars["e"][0], "b", "o", "t"],
        "بوتات5": [chars["a"][0], chars["b"][0], chars["b"][0], "b", "o", "t"],
        "بوتات6": [chars["a"][0], chars["e"][0], chars["e"][0], "b", "o", "t"],
        "بوتات7": [chars["a"][0]]*2 + [chars["e"][0], "b", "o", "t"],
        "بوتات8": [chars["a"][0]]*2 + [chars["e"][0], "b", "o", "t"],
        "بوتات9": [chars["a"][0]]*2 + [chars["b"][0], "b", "o", "t"],
        "خماسي حرفين1": [chars["a"][0]]*3 + [chars["e"][0], chars["e"][0]],
        "خماسي ارقام": [chars["a"][0], chars["e"][0], chars["b"][0]]*2,
        "خماسي حرفين2": [chars["a"][0], chars["b"][0], chars["e"][0]]*2,
        "خماسي حرفين3": [chars["a"][0], chars["e"][0]]*3,
        "سباعيات1": [chars["a"][0]]*5 + [chars["e"][0], chars["e"][0]],
        "سباعيات2": [chars["a"][0]]*5 + [chars["e"][0], chars["a"][0]],
        "سباعيات3": [chars["a"][0]]*4 + [chars["e"][0], chars["a"][0], chars["a"][0]],
        "سباعيات4": [chars["a"][0]]*3 + [chars["e"][0], chars["a"][0], chars["a"][0], chars["a"][0]],
        "سباعيات5": [chars["a"][0]]*2 + [chars["e"][0], chars["a"][0], chars["a"][0], chars["a"][0], chars["a"][0]],
        "سباعيات6": [chars["a"][0], chars["e"][0], chars["a"][0]]*3,
        "سباعيات7": [chars["a"][0], chars["e"][0]]*6,
        "متاح": [chars["a"][0], chars["e"][0]]*6 + [chars["a"][0], chars["e"][0]]
    }

    if choice in patterns:
        random.shuffle(patterns[choice])
        return "".join(patterns[choice])
    elif choice == "ايقاف":
        return "stop"
    return "error"

@l313l.ar_cmd(pattern="(الصيد|التثبيت)")
async def cmd(hrrrblll):
):
    choice = str(event.pattern_match.group(1))
    replly = await event.get_reply_message()
    if not choice:
        return await edit_or_reply(event, "**⛔️│الأمر غير صحيح .. يرجى مراجعة أوامر الصيد المتاحة.**\n\n"
                                           "**✅│للاطلاع على الأوامر العامة، أرسل:** `.الصيد`\n"
                                           "**📋│لمعرفة أنواع اليوزرات، أرسل:** `.الأنواع`")
    try:
        if replly and replly.text.startswith('@'):
            ch = replly.text
            await edit_or_reply(event, f"**✅│تم بدء عملية الصيد بنجاح!**\n\n"
                                       f"🔹 **النوع المحدد:** {choice}\n"
                                       f"🔹 **القناة المستهدفة:** {ch}\n\n"
                                       "**📊│لمتابعة حالة عملية الصيد، أرسل:** `.حالة الصيد`\n"
                                       "**⛔️│لإيقاف عملية الصيد، أرسل:** `.صيد ايقاف`")
        else:
            rub = f"@{l313l.me.username}" if l313l.me.username else ""
            ch = await l313l(functions.channels.CreateChannelRequest(
                title="صيـد روبن",
                about=f"This channel to hunt username by - @RobinUserBot | {rub}",
            ))
            ch = ch.updates[1].channel_id if hasattr(ch.updates[1], 'channel_id') else ch.chats[0].id
            await edit_or_reply(event, f"**✅│تم بدء عملية الصيد بنجاح!**\n\n"
                                       f"🔹 **النوع المحدد:** {choice}\n\n"
                                       "**📊│لمتابعة حالة عملية الصيد، أرسل:** `.حالة الصيد`\n"
                                       "**⛔️│لإيقاف عملية الصيد، أرسل:** `.صيد ايقاف`")
    except Exception as e:
        await l313l.send_message(event.chat_id, f"**⛔️│عذرًا، حدث خطأ أثناء إنشاء القناة.**\n\n"
                                                f"🔹 **تفاصيل الخطأ:**\n`{str(e)}`")

    itsclim[0] = "on"
    vedmod = True
    while vedmod:
        username = await gen_user(choice)
        if username == "stop":
            itsclim[0] = "off"
            trys[0] = 0
            await edit_or_reply(event, "**✅│تم إيقاف عملية الصيد بن!**")
            break
        if username == "error":
            await edit_or_reply(event, fذرًا عزيزي، لا يوجد النوع:** {choiceلعواع المتاحة، أرسل:** `.الأنواع`")
        = await check try                await l.UpdateRequest=username))
 await.send_id│تم بن\n" **المعرف:** @{                                                               f **:**User f"اول:**0].send_message1 f│ج!**"
                                                         :**}\n"
 **واسطةBot\n🔹 ** {tr}")
                ved break
Error as sleep(hr10           thonerrorlist.UsernameInvalid pass           thon.F:
 sleep(e)
 except as channels(e):
                    await(event_id,⛔️يد المعرف @{username}\n\n"
                                                            "**🔹│سبب الخطأ:**\n"
                                                            "لقد تجاوزت الحد المسموح به لإنشاء القنوات العامة.\n"
                                                            "**🔧│الحل:** قم بحذف قناة عامة واحدة أو أكثر من قنواتك الحالية "
                                                            "لتتمكن من صيد هذا المعرف.")
                    break
        trys[0] += 1
        await asyncio.sleep(1)

    itsclim[0] = "off"
    trys[0] = 0
    await event.client.send_message(event.chat_id, "**✅│تم الانتهاء من عملية الصيد بنجاح!**")

@l313l.ar_cmd(pattern="تثبيت_قناة (.*)")
async def _(event):
    hrrrb = str(event.pattern_match.group(1))
    if not hrrrb.startswith('@'):
        return await edit_or_reply(event, "**⛔️│الأمر غير صحيح .. يرجى التحقق من أوامر التثبيت المتاحة.**\n\n"
                                          "**📋│للأوامر العامة للتثبيت، أرسل:** `.التثبيت`")

@l313l.ar_cmd(pattern="تثبيت_حساب (.*)")
async def _(event):
    hrrrb = str(event.pattern_match.group(1))
    if not hrrrb.startswith('@'):
        return await edit_or_reply(event, "**⛔️│الأمر غير صحيح .. يرجى التحقق من أوامر التثبيت المتاحة.**\n\n"
                                          "**📋│للأوامر العامة للتثبيت، أرسل:** `.التثبيت`")

@l313l.ar_cmd(pattern="تثبيت_بوت (.*)")
async def _(event):
    hrrrb = str(event.pattern_match.group(1))
    if not hrrrb.startswith('@'):
        return await edit_or_reply(event, "**⛔️│الأمر غير صحيح .. يرجى التحقق من أوامر التثبيت المتاحة.**\n\n"
                                          "**📋│للأوامر العامة للتثبيت، أرسل:** `.التثبيت`")

@l313l.ar_cmd(pattern="(ايقاف تثبيت_قناة|ايقاف تثبيت_الحساب|ايقاف تثبيت_البوت)")
async def _(event):
    await edit_or_reply(event, "**✅│تم إيقاف عملية التثبيت بنجاح!**")

@l313l.ar_cmd(pattern="(حالة تثبيت_القناة|حالة تثبيت_الحساب|حالة تثبيت_البوت)")
async def _(event):
    await edit_or_reply(event, "**✅│هذه هي حالة التثبيت الحالية.**")