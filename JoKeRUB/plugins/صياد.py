import random
import requests
import asyncio
from asyncio import sleep
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
    if 'If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"' in response.text:
        return True
    return False

async def gen_meaningful_user():
    words = ["happy", "joy", "love", "peace", "kind", "brave", "smart", "cool", "fun", "hero"]
    username = random.choice(words) + str(random.randint(100, 999))
    return username

@l313l.ar_cmd(pattern="صيد معنى")
async def meaningful_hunt(event):
    try:
        rub = f"@{l313l.me.username}" if l313l.me.username else ""
        ch = await l313l(functions.channels.CreateChannelRequest(
            title="صيد معنى",
            about=f"This channel is to hunt meaningful usernames by - @MeaningfulHuntBot | {rub}",
        ))
        ch_id = ch.updates[1].channel_id if len(ch.updates) > 1 else ch.chats[0].id

        await edit_or_reply(event, 
                            "**✅│تم بدء عملية الصيد بنجاح!**\n\n"
                            "**📊│لمتابعة حالة عملية الصيد، أرسل:** `.حالة الصيد`\n"
                            "**⛔️│لإيقاف عملية الصيد، أرسل:** `.صيد ايقاف`")
    except Exception as e:
        await l313l.send_message(event.chat_id, 
                                 f"**⛔️│عذرًا، حدث خطأ أثناء إنشاء القناة.**\n\n"
                                 f"🔹 **تفاصيل الخطأ:**\n`{str(e)}`")
        return

    itsclim[0] = "on"
    while itsclim[0] == "on":
        username = await gen_meaningful_user()
        if username == "stop":
            itsclim[0] = "off"
            trys[0] = 0
            await edit_or_reply(event, "**✅│تم إيقاف عملية الصيد بنجاح!**")
            break
        isav = await check_user(username)
        if isav:
            try:
                await l313l(functions.channels.UpdateUsernameRequest(channel=ch_id, username=username))
                await event.client.send_message(event.chat_id,
                                                f"**✅│تم الصيد بنجاح!**\n\n"
                                                f"🔹 **المعرف:** @{username}\n"
                                                f"🔹 **بواسطة:** @MeaningfulHuntBot\n"
                                                f"🔹 **عدد المحاولات:** {trys[0]}")
                itsclim[0] = "off"
                break
            except FloodWaitError as e:
                await sleep(e.seconds + 10)
            except Exception as e:
                if "too many public channels" in str(e):
                    await l313l.send_message(event.chat_id,
                                             f"**⛔️│خطأ أثناء محاولة صيد المعرف:** @{username}\n\n"
                                             "**🔹│سبب الخطأ:**\n"
                                             "لقد تجاوزت الحد المسموح به لإنشاء القنوات العامة.\n"
                                             "**🔧│الحل:** قم بحذف قناة عامة واحدة أو أكثر من قنواتك الحالية لتتمكن من صيد هذا المعرف.")
                    break
        trys[0] += 1
        await sleep(1)
    trys[0] = 0
    if itsclim[0] == "off":
        await event.client.send_message(event.chat_id, "**✅│تم الانتهاء من عملية الصيد بنجاح!**")

# Existing functions and commands

@l313l.ar_cmd(pattern="حالة الصيد")
async def hunt_status(event):
    if itsclim[0] == "on":
        await edit_or_reply(event, f"**✅│عملية الصيد جارية!**\n**🔹│وصلت إلى** {trys[0]} **من المحاولات.**")
    elif itsclim[0] == "off":
        await edit_or_reply(event, "**⛔️│لا توجد عملية صيد جارية حاليًا.**\n**📅│يرجى المحاولة لاحقًا.**")

@l313l.ar_cmd(pattern="صيد ايقاف")
async def stop_hunt(event):
    itsclim[0] = "off"
    trys[0] = 0
    await edit_or_reply(event, "**✅│تم إيقاف عملية الصيد بنجاح!**")

hrrrbChecler_cmd = (
    "🔺 اوامـر الصيـد والتثبيت 🔻\n\n"
    "🟢╎ أولاً: قائمة أوامر تشيكـر صيد معرفات تيليجرام:\n"
    "- **`.النوع`**\n"
    "  ⪼ لعرض الأنواع التي يمكن صيدها مع الأمثلة.\n"
    "- **`.صيد` + النوع**\n"
    "  ⪼ لصيد يوزرات عشوائية حسب النوع المحدد.\n"
    "- **`.حالة الصيد`**\n"
    "  ⪼ لمعرفة حالة تقدم عملية الصيد.\n"
    "- **`.صيد ايقاف`**\n"
    "  ⪼ لإيقاف عملية الصيد الحالية.\n\n"
    "🔴╎ ثانياً: قائمة أوامر تشيكـر تثبيت معرفات تيليجرام:\n"
    "- **`.تثبيت_قناة` + اليوزر**\n"
    "  ⪼ لتثبيت اليوزر بقناة معينة إذا أصبح متاحًا.\n"
    "- **`.تثبيت_حساب` + اليوزر**\n"
    "  ⪼ لتثبيت اليوزر بحسابك مباشرة إذا أصبح متاحًا.\n"
    "- **`.تثبيت_بوت` + اليوزر**\n"
    "  ⪼ لتثبيت اليوزر في بوت فاذر إذا أصبح متاحًا.\n\n"
    "🟡╎ اوامر حالة التثبيت :\n"
    "- **`.حالة تثبيت_القناة`**\n"
    "  ⪼ لمعرفة حالة تقدم التثبيت التلقائي على القناة.\n"
    "- **`.حالة تثبيت_الحساب`**\n"
    "  ⪼ لمعرفة حالة تقدم التثبيت التلقائي على حسابك.\n"
    "- **`.حالة تثبيت_البوت`**\n"
    "  ⪼ لمعرفة حالة تقدم التثبيت التلقائي على بوت فاذر.\n\n"
    "🟠╎ اوامر أيقاف التثبيت :\n"
    "- **`.ايقاف تثبيت_القناة`**\n"
    "  ⪼ لإيقاف عملية تثبيت القناة التلقائي.\n"
    "- **`.ايقاف تثبيت_الحساب`**\n"
    "  ⪼ لإيقاف عملية تثبيت الحساب التلقائي.\n"
    "- **`.ايقاف تثبيت_البوت`**\n"
    "  ⪼ لإيقاف عملية تثبيت البوت التلقائي.\n\n"
    "🚨 ملاحظات مهمة قبل استخدام أوامر الصيد والتثبيت:\n"
    "- تأكد من أن حسابك يحتوي على مساحة لإنشاء قناة عامة (قناة بمعرف).\n"
    "- إذا لم توجد مساحة، قم بإرسال يوزر قناة من قنواتك مع الرد على يوزرها باستخدام أحد أوامر الصيد.\n"
    "- لا تقم بإيقاف الصيد حتى لو استمر لفترة طويلة.\n"
    "- تحلى بالصبر وكرر المحاولات حتى تتمكن من صيد يوزر.\n"
    "- كل نوع من اليوزرات يختلف عن الآخر في نسبة الصيد.\n"
    "- التثبيت يعني تثبيت يوزر معين حتى لا يتم سرقته عندما يصبح متاحًا.\n"
)

@l313l.ar_cmd(pattern="الصيد")
async def show_hrrrbChecler_cmd(event):
    await edit_or_reply(event, hrrrbChecler_cmd)