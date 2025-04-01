import re
import os
import requests
from JoKeRUB import l313l
from JoKeRUB.core.logger import logging
from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from . import BOTLOG_CHATID


LOGS = logging.getLogger(__name__)
cmdhd = Config.COMMAND_HAND_LER

extractor = URLExtract()

oldvars = {
    "PM_PIC": "pmpermit_pic",
    "PM_TEXT": "pmpermit_txt",
    "PM_BLOCK": "pmblock",
}

@l313l.ar_cmd(pattern="جلب (.*)")
async def getvar(event):
    input = event.pattern_match.group(1)
    if input is None:
        await edit_or_reply(event, "`ضع فار لجلب قيمته`")

        return
    if gvarstatus(input) is None:
            return await edit_delete(
                event, "**⎙ :: عزيزي المستخدم انت لم تقوم باضافه هذا الفار اصلا**"
            )
    await edit_or_reply(event, gvarstatus(input))


@l313l.ar_cmd(pattern="اضف (.*)")
async def custom_HuRe(event):
    reply = await event.get_reply_message()
    text = None
    var = None
    input_str = event.pattern_match.group(1)
    dontDo = ["جهاتي", "جهتي"]
    if input_str in dontDo:
        return
    if reply and reply.text:
        text = reply.text
    else:
        return await edit_delete(
            event, "**⌔∮ يجب عليك الرد على النص او الرابط حسب الفار الذي تضيفه **"
        )

    if input_str in ["كليشة الحماية", "كليشة الحمايه", "كليشه الحماية", "كليشه الحمايه"]:
        var = "pmpermit_txt"
    elif input_str in ["اشتراك الخاص", "اشتراك خاص"]:
        var = "pchan"
    elif input_str in ["اشتراك كروب", "اشتراك الكروب"]:
        var = "gchan"
    elif input_str in ["امر النشر", "امر نشر"]:
        var = "MUKRR_ET"
    elif input_str in ["زخرفة الارقام", "زخرفه الارقام"]:
        var = "JP_FN"
    elif input_str in ["البايو", "بايو"]:
        var = "DEFAULT_BIO"
    elif input_str in ["رمز الاسم", "علامة الاسم"]:
        var = "TIME_JEP"
    elif input_str in ["كليشة الفحص", "كليشه الفحص", "كليشه فحص"]:
        var = "ALIVE_TEMPLATE"
    elif input_str in ["كليشة الحظر", "كليشه الحظر"]:
        var = "pmblock"
    elif input_str in ["كليشة البوت", "كليشه البوت"]:
        var = "START_TEXT"
    elif input_str == "ايموجي الفحص":
        var = "ALIVE_EMOJI"
    elif input_str == "نص الفحص":
        var = "ALIVE_TEXT"
    elif input_str == "عدد التحذيرات":
        var = "MAX_FLOOD_IN_PMS"
    elif input_str in ["لون الوقتي", "لون وقتي", "لون صوره وقتيه", "لون الصوره الوقتيه", "لون"]:
        var = "digitalpiccolor"
    elif input_str in ["التخزين", "تخزين"]:
        var = "PM_LOGGER_GROUP_ID"
    elif input_str in ["كليشة الخاص", "كليشه الخاص"]:
        var = "7rB_message"
    elif input_str in ["اشعارات", "الاشعارات"]:
        var = "PRIVATE_GROUP_BOT_API_ID"
    else:
        return await edit_delete(event, "**⌔∮ الفار غير معروف، الرجاء التحقق من الاسم. **")
    
    addgvar(var, text)
    await edit_or_reply(event, f"**₰ تم بنجاح تحديث فار {input_str} 𓆰،**")
    
    if BOTLOG_CHATID:
        await event.client.send_message(
            BOTLOG_CHATID,
            f"#اضف_فار\n**{input_str}** تم تحديثه بنجاح في قاعده البيانات كـ:{var}",
        )


@l313l.ar_cmd(pattern="حذف (.*)")
async def custom_HuRe(event):
    input_str = event.pattern_match.group(1)
    if (
        input_str == "كليشة الحماية"
        or input_str == "كليشة الحمايه"
        or input_str == "كليشه الحماية"
        or input_str == "كليشه الحمايه"
    ):
        if gvarstatus("pmpermit_txt") is None:
            return await edit_delete(
                event, "**⎙ :: عزيزي المستخدم انت لم تقوم باضافه هذا الفار اصلا**"
            )
        delgvar("pmpermit_txt")
    if input_str == "كليشة الفحص" or input_str == "كليشه الفحص" or input_str == "كليشه فحص" or input_str == "كليشه فحص":
        if gvarstatus("ALIVE_TEMPLATE") is None:
            return await edit_delete(
                event, "**⎙ :: عزيزي المستخدم انت لم تقوم باضافه هذا الفار اصلا**"
            )
        delgvar("ALIVE_TEMPLATE")
    if input_str == "كليشة الحظر" or input_str == "كليشه الحظر":
        if gvarstatus("pmblock") is None:
            return await edit_delete(
                event, "**⎙ :: عزيزي المستخدم انت لم تقوم باضافه هذا الفار اصلا**"
            )
        delgvar("pmblock")
    if (
        input_str == "صورة الحماية"
        or input_str == "صورة الحمايه"
        or input_str == "صوره الحماية"
        or input_str == "صوره الحمايه"
    ):
        if gvarstatus("pmpermit_pic") is None:
            return await edit_delete(
                event, "**⎙ :: عزيزي المستخدم انت لم تقوم باضافه هذا الفار اصلا**"
            )
        delgvar("pmpermit_pic")
    if (
        input_str == "لون الوقتي"
        or input_str == "لون وقتي"
        or input_str == "لون صوره وقتيه"
        or input_str == "لون الصوره الوقتيه"
    ):
        if gvarstatus("digitalpiccolor") is None:
            return await edit_delete(
                event, "**لم تضيف الفار اصلاً**"
            )
        delgvar("digitalpiccolor")
    if input_str == "صورة الفحص" or input_str == "صوره الفحص":
        if gvarstatus("ALIVE_PIC") is None:
            return await edit_delete(
                event, "**⎙ :: عزيزي المستخدم انت لم تقوم باضافه هذا الفار اصلا**"
            )
        delgvar("ALIVE_PIC")
    if input_str == "كليشة البوت" or input_str == "كليشه البوت":
        if gvarstatus("START_TEXT") is None:
            return await edit_delete(
                event, "**⎙ :: عزيزي المستخدم انت لم تقوم باضافه هذا الفار اصلا**"
            )
        delgvar("START_TEXT")
    if input_str == "ايموجي الفحص":
        if gvarstatus("ALIVE_EMOJI") is None:
            return await edit_delete(
                event, "**⎙ :: عزيزي المستخدم انت لم تقوم باضافه هذا الفار اصلا**"
            )
        delgvar("ALIVE_EMOJI")
    if input_str == "التخزين" or input_str == "تخزين":
    	if gvatstatus("PM_LOGGER_GROUP_ID") is None:
    	    return await edit_delete(event, "**⎙ :: عزيزي المستخدم انت لم تقوم باضافه هذا الفار اصلا**")
    	delgvar("PM_LOGGER_GROUP_ID")
    if input_str == "اشعارات" or input_str == "الاشعارات":
    	if gvatstatus("PRIVATE_GROUP_BOT_API_ID") is None:
    	    return await edit_delete(event, "**⎙ :: عزيزي المستخدم انت لم تقوم باضافه هذا الفار اصلا**")
    	delgvar("PRIVATE_GROUP_BOT_API_ID")
    if input_str == "نص الفحص":
        if gvarstatus("ALIVE_TEXT") is None:
            return await edit_delete(
                event, "**⎙ :: عزيزي المستخدم انت لم تقوم باضافه هذا الفار اصلا**"
            )
        delgvar("ALIVE_TEXT")
    if input_str == "زخرفة الارقام" or input_str == "زخرفه الارقام":
        if gvarstatus("JP_FN") is None:
            return await edit_delete(
                event, "**⎙ :: عزيزي المستخدم انت لم تقوم باضافه هذا الفار اصلا**"
            )
        delgvar("JP_FN")
    if input_str == "بايو" or input_str == "البايو":
        if gvarstatus("DEFAULT_BIO") is None:
            return await edit_delete(
                event, "**⎙ :: عزيزي المستخدم انت لم تقوم باضافه هذا الفار اصلا**"
            )
        delgvar("DEFAULT_BIO")
    if input_str == "رمز الاسم":
        if gvarstatus("TIME_JEP") is None:
            return await edit_delete(
                event, "**⎙ :: عزيزي المستخدم انت لم تقوم باضافه هذا الفار اصلا**"
            )
        delgvar("TIME_JEP")
    if input_str == "عدد التحذيرات":
        if gvarstatus("MAX_FLOOD_IN_PMS") is None:
            return await edit_delete(
                event, "**⎙ :: عزيزي المستخدم انت لم تقوم باضافه هذا الفار اصلا**"
            )
        delgvar("MAX_FLOOD_IN_PMS")
    if input_str == "صورة البنك" or input_str == "صوره البنك":
        if gvarstatus("PING_PIC") is None:
            return await edit_delete(
                event, "**⎙ :: عزيزي المستخدم انت لم تقوم باضافه هذا الفار اصلا**"
            )
        delgvar("PING_PIC")
    await edit_or_reply(
        event, f"₰ هذا الفار تم حذفه بنجاح وارجاع قيمته الى القيمه الاصلية ✅"
    )
    if BOTLOG_CHATID:
        await event.client.send_message(
            BOTLOG_CHATID,
            f"#حذف_فار\
                    \n**فار {input_str}** تم حذفه من قاعده البيانات",
        )
@l313l.ar_cmd(pattern="اضف صورة (الفحص|فحص) ?(.*)")
async def alive_hrb (event):
    reply = await event.get_reply_message()
    if reply and reply.media:
        input_str = event.pattern_match.group(1)
        jokevent = await event.edit("` ⌔︙ جـار رفع الـصورة الى أمر الفحص `")
        try:
            media = await event.client.download_media(reply)
            if media.endswith((".webp")):
                resize_image(media)
            with open(media, "rb") as file:
                response = requests.post(
                    "https://uguu.se/upload.php",
                    files={"files[]": file},
                )
            
            if response.status_code == 200 and response.json().get("success"):
                url = response.json()["files"][0]["url"]
                addgvar("ALIVE_PIC", url)
                await jokevent.edit(f"** ⌔︙  تم اضافة الصورة الى الفحص ✓ **")
            else:
                await jokevent.edit(f"** ⌔︙حدث خطأ في رفع الصورة: **\n`{response.json()}`")

            os.remove(media)
        except Exception as exc:
            await event.edit(f"** ⌔︙خـطأ : **\n`{exc}`")
            if os.path.exists(media):
                os.remove(media)
    else:
        await event.edit("**᯽︙ يُرجى الرد على الصورة لطفًا**")
@l313l.ar_cmd(pattern="اضف صورة (البنك|بنك) ?(.*)")
async def ping_hrb (event):
    reply = await event.get_reply_message()
    if reply and reply.media:
        input_str = event.pattern_match.group(1)
        jokevent = await event.edit("` ⌔︙ جـار رفع الـصورة الى أمر البنك `")
        try:
            media = await event.client.download_media(reply)
            if media.endswith((".webp")):
                resize_image(media)
            with open(media, "rb") as file:
                response = requests.post(
                    "https://uguu.se/upload.php",
                    files={"files[]": file},
                )
            
            if response.status_code == 200 and response.json().get("success"):
                url = response.json()["files"][0]["url"]
                addgvar("PING_PIC", url)
                await jokevent.edit(f"** ⌔︙  تم اضافة الصورة الى البنك ✓ **")
            else:
                await jokevent.edit(f"** ⌔︙حدث خطأ في رفع الصورة: **\n`{response.json()}`")

            os.remove(media)
        except Exception as exc:
            await event.edit(f"** ⌔︙خـطأ : **\n`{exc}`")
            if os.path.exists(media):
                os.remove(media)
    else:
        await event.edit("**᯽︙ يُرجى الرد على الصورة لطفًا**")
@l313l.ar_cmd(pattern="اضف صورة (الحماية|الحمايه|حماية|حمايه) ?(.*)")
async def secu_hrb (event):
    reply = await event.get_reply_message()
    if reply and reply.media:
        input_str = event.pattern_match.group(1)
        jokevent = await event.edit("` ⌔︙ جـار رفع الـصورة الى أمر الحماية `")
        try:
            media = await event.client.download_media(reply)
            if media.endswith((".webp")):
                resize_image(media)
            with open(media, "rb") as file:
                response = requests.post(
                    "https://uguu.se/upload.php",
                    files={"files[]": file},
                )
            
            if response.status_code == 200 and response.json().get("success"):
                url = response.json()["files"][0]["url"]
                addgvar("pmpermit_pic", url)
                await jokevent.edit(f"** ⌔︙  تم اضافة الصورة الى الحماية ✓ **")
            else:
                await jokevent.edit(f"** ⌔︙حدث خطأ في رفع الصورة: **\n`{response.json()}`")

            os.remove(media)
        except Exception as exc:
            await event.edit(f"** ⌔︙خـطأ : **\n`{exc}`")
            if os.path.exists(media):
                os.remove(media)
    else:
        await event.edit("**᯽︙ يُرجى الرد على الصورة لطفًا**")


@l313l.ar_cmd(pattern="اضف صورة (الخاص|خاص) ?(.*)")
async def khas_hrb (event):
    reply = await event.get_reply_message()
    if reply and reply.media:
        input_str = event.pattern_match.group(1)
        jokevent = await event.edit("` ⌔︙ جـار رفع الـصورة الى أمر الخاص `")
        try:
            media = await event.client.download_media(reply)
            if media.endswith((".webp")):
                resize_image(media)
            with open(media, "rb") as file:
                response = requests.post(
                    "https://uguu.se/upload.php",
                    files={"files[]": file},
                )
            
            if response.status_code == 200 and response.json().get("success"):
                url = response.json()["files"][0]["url"]
                addgvar("hrb_url", url)
                await jokevent.edit(f"** ⌔︙  تم اضافة الصورة الى الخاص ✓ **")
            else:
                await jokevent.edit(f"** ⌔︙حدث خطأ في رفع الصورة: **\n`{response.json()}`")

            os.remove(media)
        except Exception as exc:
            await event.edit(f"** ⌔︙خـطأ : **\n`{exc}`")
            if os.path.exists(media):
                os.remove(media)
    else:
        await event.edit("**᯽︙ يُرجى الرد على الصورة لطفًا**")
