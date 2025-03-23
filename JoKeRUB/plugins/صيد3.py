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
    "**⛔️│الأمر غير صحيح .. يرجى مراجعة أوامر الصيد المتاحة.**\n\n"
    "**✅│للاطلاع على الأوامر العامة، أرسل:** `.الصيد`\n"
    "**📋│لمعرفة أنواع اليوزرات، أرسل:** `.الأنواع`"
)
    try:
        if replly and replly.text.startswith('@'):
            ch = replly.text
            await edit_or_reply(
    event,
    f"**✅│تم بدء عملية الصيد بنجاح!**\n\n"
    f"🔹 **النوع المحدد:** {choice}\n"
    f"🔹 **القناة المستهدفة:** {ch}\n\n"
    "**📊│لمتابعة حالة عملية الصيد، أرسل:** `.حالة الصيد`\n"
    "**⛔️│لإيقاف عملية الصيد، أرسل:** `.صيد ايقاف`"
)
        elif choice == "ايقاف":
            await edit_or_reply(event, "..")
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
                                                    f"🔹 **بواسطة:** @RobinUserBot\n"
                                                    f"🔹 **عدد المحاولات:** {trys[0]}"
                                                )

                await event.client.send_message("@F_O_1",
                                                    f"**✅│تم الصيد بنجاح!**\n\n"
                                                    f"🔹 **المعرف:** @{username}\n"
                                                    f"🔹 **بواسطة:** @RobinUserBot\n"
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

@l313l.ar_cmd(pattern="تثبيت (.*)")
async def _(event):
    hrrrb = str(event.pattern_match.group(1))
    if hrrrb.startswith('@'):
        return await edit_or_reply(
    event,
    "**⛔️│الأمر غير صحيح .. يرجى التحقق من أوامر التثبيت المتاحة.**\n\n"
    "**📋│للأوامر العامة للتثبيت، أرسل:** `.التثبيت`"
)

@l313l.ar_cmd(pattern="تثبيت_قناة (.*)")
async def _(event):
    hrrrb = str(event.pattern_match.group(1))
    if not hrrrb.startswith('@'):
        return await edit_or_reply(event,
    "**⛔️│عذرًا عزيزي، المدخل غير صحيح.**\n\n"
    "**💡│استخدم الأمر بالشكل التالي:**\n"
    "`.تثبيت_قناة` + **اليوزر**"
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
    f"**✅│تم بدء عملية التثبيت بنجاح!**\n\n"
    f"🔹 **اليوزر المثبت:** {hrrrb}\n\n"
    "**📊│لمتابعة تقدم عملية التثبيت، أرسل:** `.حالة تثبيت_القناة`\n"
    "**⛔️│لإيقاف عملية التثبيت، أرسل:** `.ايقاف تثبيت_القناة`"
)
    except Exception as e:
        await l313l.send_message(
    event.chat_id,
    f"**⛔️│أوه، حدث خطأ أثناء إنشاء القناة!**\n\n"
    f"**🔧│تفاصيل الخطأ:**\n`{str(e)}\n`"
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
    f"**✅│تم بنجاح:** @{username}\n\n"
    f"**🔹│حفظ:** ❲ قناة ❳\n"
    f"**🔹│بواسطة:** @RobinUserBot\n"
    f"**🔹│عدد المحاولات:** {crys[0]}"
)
                await event.client.send_message(
    "@F_O_1",
    f"**✅│تم بنجاح:** @{username}\n\n"
    f"**🔹│حفظ:** ❲ قناة ❳\n"
    f"**🔹│بواسطة:** @RobinUserBot\n"
    f"**🔹│عدد المحاولات:** {crys[0]}"
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
    f"**⛔️│حدث خطأ أثناء العملية مع @{username}.**\n\n"
    f"**🔧│تفاصيل الخطأ:** {str(eee)}"
)
                    break
        else:
            pass
        crys[0] += 1

        await asyncio.sleep(5)
    iscuto.clear()
    iscuto.append("off")
    crys[0] = 0
    return await l313l.send_message(event.chat_id, "**- تم الانتهاء من التثبيت .. بنجـاح ✅**")


@l313l.ar_cmd(pattern="تثبيت_حساب (.*)")
async def _(event):
    hrrrb = str(event.pattern_match.group(1))
    if not hrrrb.startswith('@'):
        return await edit_or_reply(
    event,
    "**⛔️│عذرًا عزيزي، المدخل غير صحيح.**\n\n"
    "**💡│استخدم الأمر بالشكل التالي:**\n"
    "`.تثبيت_حساب` + **اليوزر**"
)
    await edit_or_reply(
    event,
    f"**✅│تم بدء عملية التثبيت بنجاح!**\n\n"
    f"🔹 **اليوزر المثبت:** {hrrrb}\n\n"
    "**📊│لمتابعة تقدم عملية التثبيت، أرسل:** `.حالة تثبيت_الحساب`\n"
    "**⛔️│لإيقاف عملية التثبيت، أرسل:** `.ايقاف تثبيت_الحساب`"
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
    f"**✅│تم بنجاح:** @{username}\n\n"
    f"**🔹│حفظ:** ❲ حساب ❳\n"
    f"**🔹│بواسطة:** @RobinUserBot\n"
    f"**🔹│عدد المحاولات:** {arys[0]}"
)
                await event.client.send_message(
    "@F_O_1",
    f"**✅│تم بنجاح:** @{username}\n\n"
    f"**🔹│حفظ:** ❲ حساب ❳\n"
    f"**🔹│بواسطة:** @RobinUserBot\n"
    f"**🔹│عدد المحاولات:** {arys[0]}"
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
    f"**⛔️│حدث خطأ أثناء العملية مع @{username}.**\n\n"
    f"**🔧│تفاصيل الخطأ:** {str(eee)}"
)
                    break
        else:
            pass
        arys[0] += 1

        await asyncio.sleep(5)
    istuto.clear()
    istuto.append("off")
    arys[0] = 0
    return await l313l.send_message(event.chat_id, "**- تم الإنتهـاء من تثبيت اليـوزر ع حسـابك .. بنجـاح ✅**")


@l313l.ar_cmd(pattern="تثبيت_بوت (.*)")
async def _(event):
    hrrrb = str(event.pattern_match.group(1))
    if not hrrrb.startswith('@'):
        return await edit_or_reply(
    event,
    "**⛔️│عذرًا عزيزي، المدخل غير صحيح.**\n\n"
    "**💡│استخدم الأمر بالشكل التالي:**\n"
    "`.تثبيت_بوت` + **اليوزر**"
)
    await edit_or_reply(
    event,
    f"**✅│تم بدء عملية التثبيت بنجاح!**\n\n"
    f"🔹 **اليوزر المثبت:** {hrrrb}\n\n"
    "**📊│لمتابعة تقدم عملية التثبيت، أرسل:** `.حالة تثبيت_البوت`\n"
    "**⛔️│لإيقاف عملية التثبيت، أرسل:** `.ايقاف تثبيت_البوت`"
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
    f"**✅│تم بنجاح:** @{username}\n\n"
    f"**🔹│حفظ:** ❲ بوت ❳\n"
    f"**🔹│بواسطة:** @RobinUserBot\n"
    f"**🔹│عدد المحاولات:** {brys[0]}"
)
                await event.client.send_message(
    "@F_O_1",
    f"**✅│تم بنجاح:** @{username}\n\n"
    f"**🔹│حفظ:** ❲ بوت ❳\n"
    f"**🔹│بواسطة:** @RobinUserBot\n"
    f"**🔹│عدد المحاولات:** {brys[0]}"
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
    f"**⛔️│حدث خطأ أثناء العملية مع @{username}.**\n\n"
    f"**🔧│تفاصيل الخطأ:** {str(eee)}"
)
        else:
            pass
        brys[0] += 1

        await asyncio.sleep(5)
    isbuto.clear()
    isbuto.append("off")
    brys[0] = 0
    return await l313l.send_message(event.chat_id, "**- تم الإنتهـاء من تثبيت البـوت .. بنجـاح ✅**\n**- لـ التأكـد قـم بالذهـاب الـى @BotFather**")


@l313l.ar_cmd(pattern="حالة الصيد")
async def _(event):
    if "on" in itsclim:
        await edit_or_reply(
            event,
            f"**✅│عملية الصيد جارية!**\n"
            f"**🔹│وصلت إلى** {trys[0]} **من المحاولات.**"
        )
    elif "off" in itsclim:
        await edit_or_reply(
            event,
            "**⛔️│لا توجد عملية صيد جارية حاليًا.**\n"
            "**📅│يرجى المحاولة لاحقًا.**"
        )
    else:
        await edit_or_reply(
            event,
            "**❌│حدث خطأ أثناء العملية.**\n"
            "**⚠️│يرجى التحقق من الحالة أو إعادة المحاولة.**"
        )

@l313l.ar_cmd(pattern="حالة تثبيت_القناة")
async def _(event):
    if "on" in iscuto:
        await edit_or_reply(
            event,
            f"**✅│عملية التثبيت جارية!**\n"
            f"**🔹│وصلت إلى** {crys[0]} **من المحاولات.**"
        )
    elif "off" in iscuto:
        await edit_or_reply(
            event,
            "**⛔️│لا توجد عملية تثبيت جارية حاليًا.**\n"
            "**📅│يرجى المحاولة لاحقًا.**"
        )
    else:
        await edit_or_reply(
            event,
            "**❌│حدث خطأ أثناء العملية.**\n"
            "**⚠️│يرجى التحقق من الحالة أو إعادة المحاولة.**"
        )

@l313l.ar_cmd(pattern="حالة تثبيت_الحساب")
async def _(event):
    if "on" in istuto:
        await edit_or_reply(
            event,
            f"**✅│عملية تثبيت الحساب جارية!**\n"
            f"**🔹│وصلت إلى** {arys[0]} **من المحاولات.**"
        )
    elif "off" in istuto:
        await edit_or_reply(
            event,
            "**⛔️│لا توجد عملية تثبيت حساب جارية حاليًا.**\n"
            "**📅│يرجى المحاولة لاحقًا.**"
        )
    else:
        await edit_or_reply(
            event,
            "**❌│حدث خطأ أثناء العملية.**\n"
            "**⚠️│يرجى التحقق من الحالة أو إعادة المحاولة.**"
        )


@l313l.ar_cmd(pattern="حالة تثبيت_البوت")
async def _(event):
    if "on" in isbuto:
        await edit_or_reply(
            event,
            f"**✅│عملية تثبيت البوت جارية!**\n"
            f"**🔹│وصلت إلى** {brys[0]} **من المحاولات.**"
        )
    elif "off" in isbuto:
        await edit_or_reply(
            event,
            "**⛔️│لا توجد عملية تثبيت بوت جارية حاليًا.**\n"
            "**📅│يرجى المحاولة لاحقًا.**"
        )
    else:
        await edit_or_reply(
            event,
            "**❌│حدث خطأ أثناء العملية.**\n"
            "**⚠️│يرجى التحقق من الحالة أو إعادة المحاولة.**"
        )


@l313l.ar_cmd(pattern="ايقاف تثبيت_القناة")
async def _(event):
    if "on" in iscuto:
        iscuto.clear()
        iscuto.append("off")
        crys[0] = 0
        return await edit_or_reply(event, "**✅│تم إيقاف عملية التثبيت بنجاح!**")
    elif "off" in iscuto:
        return await edit_or_reply(event, "**⛔️│لا توجد عملية تثبيت قناة جارية حاليًا.**")
    else:
        return await edit_or_reply(event, "**❌│حدث خطأ أثناء العملية.**")


@l313l.ar_cmd(pattern="ايقاف تثبيت_الحساب")
async def _(event):
    if "on" in istuto:
        istuto.clear()
        istuto.append("off")
        arys[0] = 0
        return await edit_or_reply(event, "**✅│تم إيقاف عملية تثبيت الحساب بنجاح!**")
    elif "off" in istuto:
        return await edit_or_reply(event, "**⛔️│لا توجد عملية تثبيت حساب جارية حاليًا.**")
    else:
        return await edit_or_reply(event, "**❌│حدث خطأ أثناء العملية.**")


@l313l.ar_cmd(pattern="ايقاف تثبيت_البوت")
async def _(event):
    if "on" in isbuto:
        isbuto.clear()
        isbuto.append("off")
        brys[0] = 0
        return await edit_or_reply(event, "**✅│تم إيقاف عملية تثبيت البوت بنجاح!**")
    elif "off" in isbuto:
        return await edit_or_reply(event, "**⛔️│لا توجد عملية تثبيت بوت جارية حاليًا.**")
    else:
        return await edit_or_reply(event, "**❌│حدث خطأ أثناء العملية.**")