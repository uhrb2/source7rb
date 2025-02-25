import random
import requests
import time
import asyncio
from asyncio import sleep
import telethon
from telethon.sync import functions
from telethon.errors import FloodWaitError
from user_agent import generate_user_agent
from JoKeRUB import l313l
from ..core.managers import edit_or_reply

trys = [0]
itsclim = ["off"]

async def check_user(username):
    url = "https://t.me/" + str(username)
    headers = {
        "User-Agent": generate_user_agent(),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",
    }

    response = requests.get(url, headers=headers)
    if (
        response.text.find(
            'If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"'
        )
        >= 0
    ):
        return True
    else:
        return False

async def gen_user(choice):
    a = "qwertyuiopasdfghjklzxcvbnm"
    b = "1234567890"
    e = "qwertyuiopasdfghjklzxcvbnm1234567890"
    z = "sdfghjklzwerty1234567890uioxcvbqpanm"
    if choice == "مخصص": # مثال على نوع مخصص
        c = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], c[0], d[0], d[0], c[0]]
        username = "".join(f)
    else:
        return "error"
    return username

@l313l.ar_cmd(pattern="صيد مخصص")
async def custom_hunt(event):
    choice = "مخصص"
    try:
        rub = f"@{l313l.me.username}" if l313l.me.username else ""
        ch = await l313l(
            functions.channels.CreateChannelRequest(
                title="صيـد مخصص",
                about=f"This channel to hunt username by - @CustomHuntBot | {rub}",
            )
        )
        try:
            ch = ch.updates[1].channel_id
        except Exception:
            ch = ch.chats[0].id
        
        await edit_or_reply(
            event,
            f"**✅│تم بدء عملية الصيد بنجاح!**\n\n"
            f"🔹 **النوع المحدد:** {choice}\n\n"
            "**📊│لمتابعة حالة عملية الصيد، أرسل:** `.حالة الصيد`\n"
            "**⛔️│لإيقاف عملية الصيد، أرسل:** `.صيد ايقاف`"
        )
    except Exception as e:
        await l313l.send_message(
            event.chat_id,
            f"**⛔️│عذرًا، حدث خطأ أثناء إنشاء القناة.**\n\n"
            f"🔹 **تفاصيل الخطأ:**\n`{str(e)}`"
        )
        vedmod = False

    itsclim.clear()
    itsclim.append("on")
    vedmod = True
    while vedmod:
        username = await gen_user(choice)
        if username == "stop":
            itsclim.clear()
            itsclim.append("off")
            trys[0] = 0
            await edit_or_reply(
                event,
                "**✅│تم إيقاف عملية الصيد بنجاح!**"
            )
            break
        if username == "error":
            await edit_or_reply(
                event,
                f"**⛔️│عذرًا عزيزي، لا يوجد النوع:** {choice}\n\n"
                "**📋│لعرض الأنواع المتاحة، أرسل:** `.الأنواع`"
            )
            break
        isav = await check_user(username)
        if isav == True:
            try:
                await l313l(
                    functions.channels.UpdateUsernameRequest(
                        channel=ch, username=username
                    )
                )
                await event.client.send_message(event.chat_id,
                                                f"**✅│تم الصيد بنجاح!**\n\n"
                                                f"🔹 **المعرف:** @{username}\n"
                                                f"🔹 **بواسطة:** @CustomHuntBot\n"
                                                f"🔹 **عدد المحاولات:** {trys[0]}"
                                                )
                vedmod = False
                break
            except FloodWaitError as hrb:
                wait_time = hrb.seconds
                await sleep(wait_time + 10)
                pass
            except telethon.errors.rpcerrorlist.UsernameInvalidError:
                pass
            except telethon.errors.FloodError as e:
                flood_error = e.seconds
                await sleep(flood_error + 10)
                pass
            except Exception as e:
                if "too many public channels" in str(e):
                    await l313l.send_message(event.chat_id,
                                                f"""**⛔️│خطأ أثناء محاولة صيد المعرف:** @{username}\n\n"""
                                                "**🔹│سبب الخطأ:**\n"
                                                "لقد تجاوزت الحد المسموح به لإنشاء القنوات العامة.\n"
                                                "**🔧│الحل:** قم بحذف قناة عامة واحدة أو أكثر من قنواتك الحالية لتتمكن من صيد هذا المعرف."
                                            )
                    break
                else:
                    pass
        else:
            pass
        trys[0] += 1
        await asyncio.sleep(1)

    itsclim.clear()
    itsclim.append("off")
    trys[0] = 0
    return await event.client.send_message(event.chat_id, "**✅│تم الانتهاء من عملية الصيد بنجاح!**")