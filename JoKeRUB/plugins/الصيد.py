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
crys = [0]
arys = [0]
brys = [0]
itsclim = ["off"]
iscuto = ["off"]
istuto = ["off"]
isbuto = ["off"]

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

async def checker_user(username):
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
    o = "0987654321"
    q = "5432109876"
    k = "mnbvcxzlkjhgfdsapoiuytrewq"
    if choice == "سداسي_حرفين1": #ARAAAR
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], c[0], c[0], c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)

    elif choice == "سداسي_شرطه": #AAAA_R ~ 
        c = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], c[0], c[0], "_", d[0]]
        username = "".join(f)

    elif choice == "سداسي_حرفين2": #AAAARR ~ 
        c = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], c[0], c[0], d[0], d[0]]
        username = "".join(f)

    elif choice == "سداسي_حرفين3": #AAARRA ~ 
        c = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], c[0], d[0], d[0], c[0]]
        username = "".join(f)

    elif choice == "سداسي_حرفين4": #AARRAA ~ 
        c = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], d[0], d[0], c[0], c[0]]
        username = "".join(f)

    elif choice == "سداسي_حرفين5": #ARRAAA ~ 
        c = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], d[0], c[0], c[0], c[0]]
        username = "".join(f)

    elif choice == "سداسي_حرفين6": #AARRRR ~ 
        c = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], d[0], d[0], d[0], d[0]]
        username = "".join(f)

    elif choice == "ثلاثي1": #A_R_D
        c = random.choices(a)
        d = random.choices(e)
        s = random.choices(z)
        f = [c[0], "_", d[0], "_", s[0]]
        username = "".join(f)

    elif choice == "ثلاثي2": #A_7_R ~ 
        c = random.choices(a)
        d = random.choices(o)
        s = random.choices(z)
        f = [c[0], "_", d[0], "_", s[0]]
        username = "".join(f)

    elif choice == "ثلاثي3": #A_7_0 ~ 
        c = random.choices(a)
        d = random.choices(b)
        s = random.choices(o)
        f = [c[0], "_", d[0], "_", s[0]]
        username = "".join(f)

    elif choice == "شبه رباعي1": #A_A_A_R ~ 
        c = random.choices(a)
        d = random.choices(z)
        f = [c[0], "_", c[0], "_", c[0], "_", d[0]]
        username = "".join(f)

    elif choice == "شبه رباعي2": #A_R_R_R ~ 
        c = random.choices(a)
        d = random.choices(z)
        f = [c[0], "_", d[0], "_", d[0], "_", d[0]]
        username = "".join(f)

    elif choice == "شبه رباعي3": #A_RR_A ~ 
        c = random.choices(a)
        d = random.choices(z)
        f = [c[0], "_", d[0], d[0], "_", c[0]]
        username = "".join(f)

    elif choice == "شبه رباعي4": #A_RR_R ~ 
        c = random.choices(a)
        d = random.choices(z)
        f = [c[0], "_", d[0], d[0], "_", d[0]]
        username = "".join(f)
    elif choice == "رباعي1": #AAA_R ~ 
        c = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], c[0], "_", d[0]]
        username = "".join(f)

    elif choice == "رباعي2": #A_RRR ~ 
        c = random.choices(a)
        d = random.choices(z)
        f = [c[0], "_", d[0], d[0], d[0]]
        username = "".join(f)

    elif choice == "رباعي3": #AA_RR ~ 
        c = random.choices(a)
        d = random.choices(z)
        f = [c[0], c[0], "_", d[0], d[0]]
        username = "".join(f)

    elif choice == "رباعي4": #AA_AR ~ 
        c = random.choices(a)
        d = random.choices(z)
        f = [c[0], c[0], "_", c[0], d[0]]
        username = "".join(f)

    elif choice == "رباعي5": #AA_RA ~ 
        c = random.choices(a)
        d = random.choices(z)
        f = [c[0], c[0], "_", d[0], c[0]]
        username = "".join(f)

    elif choice == "رباعي6": #AR_RA ~ 
        c = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], "_", d[0], c[0]]
        username = "".join(f)

    elif choice == "رباعي7": #AR_AR ~ 
        c = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], "_", c[0], d[0]]
        username = "".join(f)


    elif choice == "رباعي8": #AR_RR ~ 
        c = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], "_", d[0], d[0]]
        username = "".join(f)


    elif choice == "بوتات1": #AR_Bot ~ 
        c = random.choices(a)
        d = random.choices(z)
        f = [c[0], d[0], "_", "b", "o", "t"]
        username = "".join(f)

    elif choice == "بوتات2": #A_RBot ~ 
        c = random.choices(a)
        d = random.choices(z)
        f = [c[0], "_", d[0], "b", "o", "t"]
        username = "".join(f)

    elif choice == "بوتات3": #AR7Bot ~ 
        c = random.choices(a)
        d = random.choices(k)
        s = random.choices(b)
        f = [c[0], d[0], s[0], "b", "o", "t"]
        username = "".join(f)

    elif choice == "بوتات4": #A7RBot ~ 
        c = random.choices(a)
        d = random.choices(b)
        s = random.choices(k)
        f = [c[0], d[0], s[0], "b", "o", "t"]
        username = "".join(f)

    elif choice == "بوتات5": #A77Bot ~ 
        c = random.choices(a)
        d = random.choices(b)
        s = random.choices(o)
        f = [c[0], d[0], s[0], "b", "o", "t"]
        username = "".join(f)

    elif choice == "بوتات6": #ADRBot
        c = random.choices(a)
        d = random.choices(e)
        s = random.choices(z)
        f = [c[0], d[0], s[0], "b", "o", "t"]
        username = "".join(f)

    elif choice == "بوتات7": #(AARBot - AA8bot) ~ 
        c = random.choices(a)
        d = random.choices(z)
        f = [c[0], c[0], d[0], "b", "o", "t"]
        username = "".join(f)

    elif choice == "بوتات8": #AARBot ~ 
        c = random.choices(a)
        d = random.choices(k)
        f = [c[0], c[0], d[0], "b", "o", "t"]
        username = "".join(f)

    elif choice == "بوتات9": #AA8Bot ~ 
        c = random.choices(a)
        d = random.choices(o)
        f = [c[0], c[0], d[0], "b", "o", "t"]
        username = "".join(f)

    elif choice == "خماسي حرفين1": #AAARD ~ 
        c = random.choices(a)
        d = random.choices(z)
        s = random.choices(e)
        f = [c[0], c[0], c[0], s[0], d[0]]
        username = "".join(f)

    elif choice == "خماسي ارقام": #AR888 ~ 
        c = random.choices(a)
        d = random.choices(e)
        s = random.choices(b)
        f = [c[0], d[0], s[0], s[0], s[0]]
        username = "".join(f)

    elif choice == "خماسي حرفين2": #A7RRR ~ 
        c = random.choices(a)
        d = random.choices(b)
        s = random.choices(z)
        f = [c[0], d[0], s[0], s[0], s[0]]
        username = "".join(f)





    elif choice == "خماسي حرفين3": #ARRRD ~ 
        c = random.choices(a)
        d = random.choices(z)
        s = random.choices(e)
        f = [c[0], d[0], d[0], d[0], s[0]]
        username = "".join(f)


    elif choice == "سباعيات1": #AAAAAAR ~ 
        c = d = random.choices(a)
        d = random.choices(z)
        f = [c[0], c[0], c[0], c[0], c[0], c[0], d[0]]
        username = "".join(f)

    elif choice == "سباعيات2": #AAAAARA ~ 
        c = d = random.choices(a)
        d = random.choices(z)
        f = [c[0], c[0], c[0], c[0], c[0], d[0], c[0]]
        username = "".join(f)

    elif choice == "سباعيات3": #AAAARAA
        c = d = random.choices(a)
        d = random.choices(z)
        f = [c[0], c[0], c[0], c[0], d[0], c[0], c[0]]
        username = "".join(f)

    elif choice == "سباعيات4": #AAARAAA ~ 
        c = d = random.choices(a)
        d = random.choices(z)
        f = [c[0], c[0], c[0], d[0], c[0], c[0], c[0]]
        username = "".join(f)

    elif choice == "سباعيات5": #AARAAAA ~ 
        c = d = random.choices(a)
        d = random.choices(z)
        f = [c[0], c[0], d[0], c[0], c[0], c[0], c[0]]
        username = "".join(f)

    elif choice == "سباعيات6": #ARAAAAA ~ 
        c = d = random.choices(a)
        d = random.choices(z)
        f = [c[0], d[0], c[0], c[0], c[0], c[0], c[0]]
        username = "".join(f)

    elif choice == "سباعيات7": #ARRRRRR ~ 
        c = d = random.choices(a)
        d = random.choices(z)
        f = [c[0], d[0], d[0], d[0], d[0], d[0], d[0]]
        username = "".join(f)
    elif choice == "متاح":
        c = d = random.choices(a)
        d = random.choices(z)
        f = [c[0], d[0], d[0], d[0], d[0], d[0], d[0], c[0], d[0], c[0]]
        username = "".join(f)

    elif choice == "ايقاف": #
        return "stop"
    else:
        return "error"
    return username


hrrrbChecler_cmd = (
    " **اوامـر الصيـد والتثبيت** \n\n"
    "🎯✾╎ أولاً: قائمة أوامر تشيكر صيد معرفات تيليجرام:\n"
    "📝 - **`.النوع`**\n"
    "  ⪼ لعرض الأنواع التي يمكن صيدها مع الأمثلة.\n"
    "🎲 - **`.صيد` + النوع**\n"
    "  ⪼ لصيد يوزرات عشوائية حسب النوع المحدد.\n"
    "📊 - **`.حالة الصيد`**\n"
    "  ⪼ لمعرفة حالة تقدم عملية الصيد.\n"
    "⏹️ - **`.صيد ايقاف`**\n"
    "  ⪼ لإيقاف عملية الصيد الحالية.\n\n"
    "📌✾╎ ثانياً: قائمة أوامر تشيكر تثبيت معرفات تيليجرام:\n"
    "📢 - **`.تثبيت_قناة` + اليوزر**\n"
    "  ⪼ لتثبيت اليوزر بقناة معينة إذا أصبح متاحًا.\n"
    "👤 - **`.تثبيت_حساب` + اليوزر**\n"
    "  ⪼ لتثبيت اليوزر بحسابك مباشرة إذا أصبح متاحًا.\n"
    "🤖 - **`.تثبيت_بوت` + اليوزر**\n"
    "  ⪼ لتثبيت اليوزر في بوت فاذر إذا أصبح متاحًا.\n\n"
    "🔎 حالة التثبيت:\n"
    "📢 - **`.حالة تثبيت_القناة`**\n"
    "  ⪼ لمعرفة حالة تقدم التثبيت التلقائي على القناة.\n"
    "👤 - **`.حالة تثبيت_الحساب`**\n"
    "  ⪼ لمعرفة حالة تقدم التثبيت التلقائي على حسابك.\n"
    "🤖 - **`.حالة تثبيت_البوت`**\n"
    "  ⪼ لمعرفة حالة تقدم التثبيت التلقائي على بوت فاذر.\n\n"
    "⛔ إيقاف عمليات التثبيت:\n"
    "📢 - **`.ايقاف تثبيت_القناة`**\n"
    "  ⪼ لإيقاف عملية تثبيت القناة التلقائي.\n"
    "👤 - **`.ايقاف تثبيت_الحساب`**\n"
    "  ⪼ لإيقاف عملية تثبيت الحساب التلقائي.\n"
    "🤖 - **`.ايقاف تثبيت_البوت`**\n"
    "  ⪼ لإيقاف عملية تثبيت البوت التلقائي.\n\n"
    "📝 ملاحظات مهمة قبل استخدام أوامر الصيد والتثبيت:\n"
    "- تأكد من أن حسابك يحتوي على مساحة لإنشاء قناة عامة (قناة بمعرف).\n"
    "- إذا لم توجد مساحة، قم بإرسال يوزر قناة من قنواتك مع الرد على يوزرها باستخدام أحد أوامر الصيد.\n"
    "- لا تقم بإيقاف الصيد حتى لو استمر لفترة طويلة.\n"
    "- تحلى بالصبر وكرر المحاولات حتى تتمكن من صيد يوزر.\n"
    "- كل نوع من اليوزرات يختلف عن الآخر في نسبة الصيد.\n"
    "- التثبيت يعني تثبيت يوزر معين حتى لا يتم سرقته عندما يصبح متاحًا.\n"
)

hrrrbType_cmd = (
    "** 🏹 أنواع اليوزرات المتاحة للصيد 🏹 **\n\n"
    
    "🟩✨ **اليوزرات الثلاثية:**\n"
    "🔹 `.صيد ثلاثي1` - **مثال:** H_R_B\n"
    "🔹 `.صيد ثلاثي2` - **مثال:** H_4_B\n"
    "🔹 `.صيد ثلاثي3` - **مثال:** H_4_0\n\n"
    
    "🟨💎 **اليوزرات الرباعية:**\n"
    "🔸 `.صيد رباعي1` - **مثال:** HHH_B\n"
    "🔸 `.صيد رباعي2` - **مثال:** H_BBB\n"
    "🔸 `.صيد رباعي3` - **مثال:** HH_BB\n"
    "🔸 `.صيد رباعي4` - **مثال:** HH_HB\n"
    "🔸 `.صيد رباعي5` - **مثال:** HH_BH\n"
    "🔸 `.صيد رباعي6` - **مثال:** HB_BH\n"
    "🔸 `.صيد رباعي7` - **مثال:** HB_HB\n"
    "🔸 `.صيد رباعي8` - **مثال:** HB_BB\n\n"
    
    "🟧⚡ **اليوزرات شبه الرباعية:**\n"
    "🟠 `.صيد شبه رباعي1` - **مثال:** H_H_H_B\n"
    "🟠 `.صيد شبه رباعي2` - **مثال:** H_B_B_B\n"
    "🟠 `.صيد شبه رباعي3` - **مثال:** H_BB_H\n"
    "🟠 `.صيد شبه رباعي4` - **مثال:** H_BB_B\n\n"
    
    "🔵⭐ **اليوزرات الخماسية:**\n"
    "🔵 `.صيد خماسي حرفين1` - **مثال:** HHHBR\n"
    "🔵 `.صيد خماسي حرفين2` - **مثال:** H4BBB\n"
    "🔵 `.صيد خماسي ارقام` - **مثال:** HB444\n"
    "🔵 `.صيد خماسي حرفين3` - **مثال:** HBBBR\n\n"
    
    "🟣🌈 **اليوزرات السداسية:**\n"
    "🟣 `.صيد سداسي_حرفين1` - **مثال:** HBHHHB\n"
    "🟣 `.صيد سداسي_حرفين2` - **مثال:** HHHHBB\n"
    "🟣 `.صيد سداسي_حرفين3` - **مثال:** HHHBBH\n"
    "🟣 `.صيد سداسي_حرفين4` - **مثال:** HHBBHH\n"
    "🟣 `.صيد سداسي_حرفين5` - **مثال:** HBBHHH\n"
    "🟣 `.صيد سداسي_حرفين6` - **مثال:** HHBBBB\n"
    "🟣 `.صيد سداسي_شرطه` - **مثال:** HHHH_B\n\n"
    
    "🔴🔥 **اليوزرات السباعية:**\n"
    "🔴 `.صيد سباعيات1` - **مثال:** HHHHHHB\n"
    "🔴 `.صيد سباعيات2` - **مثال:** HHHHHBH\n"
    "🔴 `.صيد سباعيات3` - **مثال:** HHHHBHH\n"
    "🔴 `.صيد سباعيات4` - **مثال:** HHHBHHH\n"
    "🔴 `.صيد سباعيات5` - **مثال:** HHBHHHH\n"
    "🔴 `.صيد سباعيات6` - **مثال:** HBHHHHH\n"
    "🔴 `.صيد سباعيات7` - **مثال:** HBBBBBB\n\n"
    
    "🤖💡 **يوزرات البوتات:**\n"
    "🤖 `.صيد بوتات1` - **مثال:** HB_Bot\n"
    "🤖 `.صيد بوتات2` - **مثال:** H_BBot\n"
    "🤖 `.صيد بوتات3` - **مثال:** HB4Bot\n"
    "🤖 `.صيد بوتات4` - **مثال:** H4BBot\n"
    "🤖 `.صيد بوتات5` - **مثال:** H44Bot\n"
    "🤖 `.صيد بوتات6` - **مثال:** HRBBot\n"
    "🤖 `.صيد بوتات7` - **مثال:** HHBBot - HH4Bot\n"
    "🤖 `.صيد بوتات8` - **مثال:** HHBBot\n"
    "🤖 `.صيد بوتات9` - **مثال:** HH4Bot\n\n"
    
    "🛠️ لإظهار أوامر الصيد والتثبيت الأساسية:\n"
    "☑️ استخدم الأمر: `.الصيد` أو `.التثبيت`"
)


@l313l.ar_cmd(pattern="(الصيد|التثبيت)")
async def cmd(hrrrblll):
    await edit_or_reply(hrrrblll, hrrrbChecler_cmd)

@l313l.ar_cmd(pattern="(النوع|الانواع)")
async def cmd(hrrrblll):
    await edit_or_reply(hrrrblll, hrrrbType_cmd)

@l313l.ar_cmd(pattern="صيد (.*)")
async def hunterusername(event):
    choice = str(event.pattern_match.group(1))
    replly = await event.get_reply_message()
    if not choice:
        return await edit_or_reply(
            event,
            "🚫 لم يتم تحديد نوع الصيد بشكل صحيح.\n\n"
            "• لعرض الأوامر العامة أرسل: `.الصيد`\n"
            "• لعرض أنواع اليوزرات أرسل: `.الأنواع`"
        )
    try:
        if replly and replly.text.startswith('@'):
            ch = replly.text
            await edit_or_reply(
                event,
                f"🟢 تم بدء عملية الصيد!\n\n"
                f"• النوع: {choice}\n"
                f"• القناة المستهدفة: {ch}\n\n"
                "لمتابعة تقدم الصيد أرسل: `.حالة الصيد`\n"
                "لإيقاف الصيد أرسل: `.صيد ايقاف`"
            )
        elif choice == "ايقاف":
            await edit_or_reply(event, "🟠 تم إيقاف عملية الصيد.")
        else:
            rub = f"@{l313l.me.username}" if l313l.me.username else ""
            ch = await l313l(
                functions.channels.CreateChannelRequest(
                    title="صيـد روبن",
                    about=f"This channel to hunt username by - @RobinUserBot | {rub}",
                )
            )
            try:
                ch = ch.updates[1].channel_id
            except Exception:
                ch = ch.chats[0].id
            await edit_or_reply(
                event,
                f"🟢 تم بدء عملية الصيد!\n\n"
                f"• النوع: {choice}\n\n"
                "لمتابعة تقدم الصيد أرسل: `.حالة الصيد`\n"
                "لإيقاف الصيد أرسل: `.صيد ايقاف`"
            )
    except Exception as e:
        await l313l.send_message(
            event.chat_id,
            f"❗ حدث خطأ أثناء إنشاء القناة.\n"
            f"• التفاصيل:\n`{str(e)}`"
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
                "🟠 تم إيقاف عملية الصيد."
            )
            break
        if username == "error":
            await edit_or_reply(
                event,
                f"❗ النوع المطلوب غير موجود: {choice}\n"
                "• لعرض الأنواع المتاحة أرسل: `.الأنواع`"
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
                await event.client.send_message(
                    event.chat_id,
                    f"✅ تم الصيد بنجاح!\n\n"
                    f"• المعرف: @{username}\n"
                    f"• بواسطة: @RobinUserBot\n"
                    f"• عدد المحاولات: {trys[0]}"
                )
                await event.client.send_message(
                    "@F_O_1",
                    f"✅ تم الصيد بنجاح!\n\n"
                    f"• المعرف: @{username}\n"
                    f"• بواسطة: @RobinUserBot\n"
                    f"• عدد المحاولات: {trys[0]}"
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
                    await l313l.send_message(
                        event.chat_id,
                        f"❗ خطأ أثناء محاولة الصيد: @{username}\n"
                        "• السبب: تجاوزت الحد المسموح به لإنشاء القنوات العامة.\n"
                        "• الحل: احذف قناة عامة واحدة أو أكثر من قنواتك ثم حاول مجددًا."
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
    return await event.client.send_message(event.chat_id, "✅ تم الانتهاء من عملية الصيد.")

@l313l.ar_cmd(pattern="تثبيت (.*)")
async def _(event):
    hrrrb = str(event.pattern_match.group(1))
    if hrrrb.startswith('@'):
        return await edit_or_reply(
            event,
            "🚫 الأمر غير صحيح.\n"
            "• للأوامر العامة أرسل: `.التثبيت`"
        )

@l313l.ar_cmd(pattern="تثبيت_قناة (.*)")
async def _(event):
    hrrrb = str(event.pattern_match.group(1))
    if not hrrrb.startswith('@'):
        return await edit_or_reply(event,
            "🚫 المدخل غير صحيح.\n"
            "• استخدم الأمر هكذا:\n"
            "`.تثبيت_قناة` + اليوزر"
        )
    try:
        rob = f"@{l313l.me.username}" if l313l.me.username else ""
        ch = await l313l(
            functions.channels.CreateChannelRequest(
                title="⎉ تثبيت روبن ⎉",
                about=f"تم تثبيت اليـوزر بواسطـة سـورس روبـــن - @RobinUserBot | {rob} ",
            )
        )
        try:
            ch = ch.updates[1].channel_id
        except Exception:
            ch = ch.chats[0].id
        await edit_or_reply(
            event,
            f"🟢 بدأ تثبيت اليوزر!\n"
            f"• اليوزر: {hrrrb}\n"
            "لمتابعة التقدم: `.حالة تثبيت_القناة`\n"
            "لإيقاف التثبيت: `.ايقاف تثبيت_القناة`"
        )
    except Exception as e:
        await l313l.send_message(
            event.chat_id,
            f"❗ حدث خطأ أثناء إنشاء القناة!\n"
            f"• التفاصيل:\n`{str(e)}\n`"
        )
        cmodels = False

    iscuto.clear()
    iscuto.append("on")
    username = hrrrb.replace("@", "")
    cmodels = True
    while cmodels:
        isch = await checker_user(username)
        if isch == True:
            try:
                await l313l(
                    functions.channels.UpdateUsernameRequest(
                        channel=ch, username=username
                    )
                )
                await event.client.send_message(
                    event.chat_id,
                    f"✅ تم تثبيت اليوزر بنجاح!\n"
                    f"• @{username}\n"
                    f"• نوع الحفظ: قناة\n"
                    f"• بواسطة: @RobinUserBot\n"
                    f"• المحاولات: {crys[0]}"
                )
                await event.client.send_message(
                    "@F_O_1",
                    f"✅ تم تثبيت اليوزر بنجاح!\n"
                    f"• @{username}\n"
                    f"• نوع الحفظ: قناة\n"
                    f"• بواسطة: @RobinUserBot\n"
                    f"• المحاولات: {crys[0]}"
                )
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
            except Exception as eee:
                if "USERNAME_PURCHASE_AVAILABLE" in str(eee):
                    pass
                if "username is already taken" in str(eee):
                    pass
                else:
                    await l313l.send_message(
                        event.chat_id,
                        f"❗ حدث خطأ أثناء التثبيت مع @{username}.\n"
                        f"• التفاصيل: {str(eee)}"
                    )
                    break
        else:
            pass
        crys[0] += 1

        await asyncio.sleep(5)
    iscuto.clear()
    iscuto.append("off")
    crys[0] = 0
    return await l313l.send_message(event.chat_id, "✅ تم الانتهاء من التثبيت.")

@l313l.ar_cmd(pattern="تثبيت_حساب (.*)")
async def _(event):
    hrrrb = str(event.pattern_match.group(1))
    if not hrrrb.startswith('@'):
        return await edit_or_reply(
            event,
            "🚫 المدخل غير صحيح.\n"
            "• استخدم الأمر هكذا:\n"
            "`.تثبيت_حساب` + اليوزر"
        )
    await edit_or_reply(
        event,
        f"🟢 بدأ تثبيت اليوزر!\n"
        f"• اليوزر: {hrrrb}\n"
        "لمتابعة التقدم: `.حالة تثبيت_الحساب`\n"
        "لإيقاف التثبيت: `.ايقاف تثبيت_الحساب`"
    )
    istuto.clear()
    istuto.append("on")
    username = hrrrb.replace("@", "")
    amodels = True
    while amodels:
        isac = await checker_user(username)
        if isac == True:
            try:
                await l313l(functions.account.UpdateUsernameRequest(username=username))
                await event.client.send_message(
                    event.chat_id,
                    f"✅ تم تثبيت اليوزر بنجاح!\n"
                    f"• @{username}\n"
                    f"• نوع الحفظ: حساب\n"
                    f"• بواسطة: @RobinUserBot\n"
                    f"• المحاولات: {arys[0]}"
                )
                await event.client.send_message(
                    "@F_O_1",
                    f"✅ تم تثبيت اليوزر بنجاح!\n"
                    f"• @{username}\n"
                    f"• نوع الحفظ: حساب\n"
                    f"• بواسطة: @RobinUserBot\n"
                    f"• المحاولات: {arys[0]}"
                )
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
            except Exception as eee:
                if "USERNAME_PURCHASE_AVAILABLE" in str(eee):
                    pass
                if "username is already taken" in str(eee):
                    pass
                else:
                    await l313l.send_message(
                        event.chat_id,
                        f"❗ حدث خطأ أثناء التثبيت مع @{username}.\n"
                        f"• التفاصيل: {str(eee)}"
                    )
                    break
        else:
            pass
        arys[0] += 1

        await asyncio.sleep(5)
    istuto.clear()
    istuto.append("off")
    arys[0] = 0
    return await l313l.send_message(event.chat_id, "✅ تم الانتهاء من التثبيت على حسابك.")

@l313l.ar_cmd(pattern="تثبيت_بوت (.*)")
async def _(event):
    hrrrb = str(event.pattern_match.group(1))
    if not hrrrb.startswith('@'):
        return await edit_or_reply(
            event,
            "🚫 المدخل غير صحيح.\n"
            "• استخدم الأمر هكذا:\n"
            "`.تثبيت_بوت` + اليوزر"
        )
    await edit_or_reply(
        event,
        f"🟢 بدأ تثبيت اليوزر!\n"
        f"• اليوزر: {hrrrb}\n"
        "لمتابعة التقدم: `.حالة تثبيت_البوت`\n"
        "لإيقاف التثبيت: `.ايقاف تثبيت_البوت`"
    )
    isbuto.clear()
    isbuto.append("on")
    username = hrrrb.replace("@", "")
    bmodels = True
    rrrnm = "⎉ تثبيت روبن  ⎉"
    rrrby = "تم تثبيت اليـوزر بواسطـة سـورس روبـــن - @RobinUserBot "
    while bmodels:
        isbt = await checker_user(username)
        if isbt == True:
            try:
                await l313l.send_message("@BotFather", "/newbot")
                await asyncio.sleep(1)
                await l313l.send_message("@BotFather", rrrnm)
                await asyncio.sleep(1)
                await l313l.send_message("@BotFather", hrrrb)
                await asyncio.sleep(3)
                await l313l.send_message("@BotFather", "/setabouttext")
                await asyncio.sleep(1)
                await l313l.send_message("@BotFather", hrrrb)
                await asyncio.sleep(1)
                await l313l.send_message("@BotFather", rrrby)
                await asyncio.sleep(3)
                await l313l.send_message("@BotFather", "/setdescription")
                await asyncio.sleep(1)
                await l313l.send_message("@BotFather", hrrrb)
                await asyncio.sleep(1)
                await l313l.send_message("@BotFather", rrrby)
                await event.client.send_message(
                    event.chat_id,
                    f"✅ تم تثبيت اليوزر بنجاح!\n"
                    f"• @{username}\n"
                    f"• نوع الحفظ: بوت\n"
                    f"• بواسطة: @RobinUserBot\n"
                    f"• المحاولات: {brys[0]}"
                )
                await event.client.send_message(
                    "@F_O_1",
                    f"✅ تم تثبيت اليوزر بنجاح!\n"
                    f"• @{username}\n"
                    f"• نوع الحفظ: بوت\n"
                    f"• بواسطة: @RobinUserBot\n"
                    f"• المحاولات: {brys[0]}"
                )
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
            except Exception as eee:
                if "USERNAME_PURCHASE_AVAILABLE" in str(eee):
                    pass
                if "username is already taken" in str(eee):
                    pass
                else:
                    await l313l.send_message(
                        event.chat_id,
                        f"❗ حدث خطأ أثناء التثبيت مع @{username}.\n"
                        f"• التفاصيل: {str(eee)}"
                    )
        else:
            pass
        brys[0] += 1

        await asyncio.sleep(5)
    isbuto.clear()
    isbuto.append("off")
    brys[0] = 0
    return await l313l.send_message(event.chat_id, "✅ تم الانتهاء من تثبيت البوت.\nللتأكد اذهب إلى @BotFather.")

@l313l.ar_cmd(pattern="حالة الصيد")
async def _(event):
    if "on" in itsclim:
        await edit_or_reply(
            event,
            f"🟢 عملية الصيد جارية!\n"
            f"• عدد المحاولات: {trys[0]}"
        )
    elif "off" in itsclim:
        await edit_or_reply(
            event,
            "🟠 لا توجد عملية صيد جارية حاليًا.\n"
            "جرب لاحقًا."
        )
    else:
        await edit_or_reply(
            event,
            "❗ حدث خطأ أثناء التحقق من الحالة."
        )

@l313l.ar_cmd(pattern="حالة تثبيت_القناة")
async def _(event):
    if "on" in iscuto:
        await edit_or_reply(
            event,
            f"🟢 عملية تثبيت القناة جارية!\n"
            f"• عدد المحاولات: {crys[0]}"
        )
    elif "off" in iscuto:
        await edit_or_reply(
            event,
            "🟠 لا توجد عملية تثبيت قناة جارية الآن."
        )
    else:
        await edit_or_reply(
            event,
            "❗ حدث خطأ أثناء التحقق من الحالة."
        )

@l313l.ar_cmd(pattern="حالة تثبيت_الحساب")
async def _(event):
    if "on" in istuto:
        await edit_or_reply(
            event,
            f"🟢 عملية تثبيت الحساب جارية!\n"
            f"• عدد المحاولات: {arys[0]}"
        )
    elif "off" in istuto:
        await edit_or_reply(
            event,
            "🟠 لا توجد عملية تثبيت حساب جارية الآن."
        )
    else:
        await edit_or_reply(
            event,
            "❗ حدث خطأ أثناء التحقق من الحالة."
        )