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

# المتغيرات النصية المدعومة
SUPPORTED_VARS = {
    "كليشة الحماية": "pmpermit_txt",
    "كليشة الحمايه": "pmpermit_txt",
    "كليشه الحماية": "pmpermit_txt",
    "كليشه الحمايه": "pmpermit_txt",
    "اشتراك الخاص": "pchan",
    "اشتراك خاص": "pchan",
    "اشتراك كروب": "gchan",
    "اشتراك الكروب": "gchan",
    "امر النشر": "MUKRR_ET",
    "امر نشر": "MUKRR_ET",
    "زخرفة الارقام": "JP_FN",
    "زخرفه الارقام": "JP_FN",
    "البايو": "DEFAULT_BIO",
    "بايو": "DEFAULT_BIO",
    "رمز الاسم": "TIME_JEP",
    "علامة الاسم": "TIME_JEP",
    "كليشة الفحص": "ALIVE_TEMPLATE",
    "كليشه الفحص": "ALIVE_TEMPLATE",
    "كليشه فحص": "ALIVE_TEMPLATE",
    "كليشة الحظر": "pmblock",
    "كليشه الحظر": "pmblock",
    "كليشة البوت": "START_TEXT",
    "كليشه البوت": "START_TEXT",
    "ايموجي الفحص": "ALIVE_EMOJI",
    "نص الفحص": "ALIVE_TEXT",
    "عدد التحذيرات": "MAX_FLOOD_IN_PMS",
    "لون الوقتي": "digitalpiccolor",
    "لون وقتي": "digitalpiccolor",
    "لون صوره وقتيه": "digitalpiccolor",
    "لون الصوره الوقتيه": "digitalpiccolor",
    "لون": "digitalpiccolor",
    "التخزين": "PM_LOGGER_GROUP_ID",
    "تخزين": "PM_LOGGER_GROUP_ID",
    "كليشة الخاص": "7rB_message",
    "كليشه الخاص": "7rB_message",
    "اشعارات": "PRIVATE_GROUP_BOT_API_ID",
    "الاشعارات": "PRIVATE_GROUP_BOT_API_ID",
}

# المتغيرات الصورية المدعومة
IMG_VARS = {
    "الفحص": "ALIVE_PIC",
    "بنك": "PING_PIC",
    "البنك": "PING_PIC",
    "الحماية": "pmpermit_pic",
    "الحمايه": "pmpermit_pic",
    "حماية": "pmpermit_pic",
    "حمايه": "pmpermit_pic",
    "الخاص": "hrb_url",
    "خاص": "hrb_url",
}

# إضافة أو تحديث متغير نصي
@l313l.ar_cmd(pattern="اضف (.+)")
async def add_var(event):
    reply = await event.get_reply_message()
    input_str = event.pattern_match.group(1).strip()
    if input_str not in SUPPORTED_VARS:
        return await edit_delete(event, "**✗ المتغير غير مدعوم**")
    if reply and reply.text:
        value = reply.text
    else:
        return await edit_delete(event, "**✗ يجب الرد على نص المتغير المطلوب إضافته**")
    varname = SUPPORTED_VARS[input_str]
    addgvar(varname, value)
    await edit_or_reply(event, f"**✓ تم إضافة/تحديث `{input_str}` بنجاح.**")
    if BOTLOG_CHATID:
        await event.client.send_message(BOTLOG_CHATID, f"#اضف_فار\nتم إضافة {input_str} ({varname}) بالقيمة:\n{value}")

# حذف متغير نصي
@l313l.ar_cmd(pattern="حذف (.+)")
async def del_var(event):
    input_str = event.pattern_match.group(1).strip()
    if input_str not in SUPPORTED_VARS:
        return await edit_delete(event, "**✗ المتغير غير مدعوم**")
    varname = SUPPORTED_VARS[input_str]
    if gvarstatus(varname) is None:
        return await edit_delete(event, "**✗ هذا المتغير غير موجود مسبقاً**")
    delgvar(varname)
    await edit_or_reply(event, f"**✓ تم حذف `{input_str}` وقيمته بنجاح.**")
    if BOTLOG_CHATID:
        await event.client.send_message(BOTLOG_CHATID, f"#حذف_فار\nتم حذف {input_str} ({varname}) من القاعدة.")

# جلب قيمة متغير نصي
@l313l.ar_cmd(pattern="جلب (.+)")
async def get_var(event):
    input_str = event.pattern_match.group(1).strip()
    if input_str not in SUPPORTED_VARS:
        return await edit_delete(event, "**✗ المتغير غير مدعوم**")
    varname = SUPPORTED_VARS[input_str]
    value = gvarstatus(varname)
    if value is None:
        return await edit_delete(event, "**✗ هذا المتغير غير موجود بعد**")
    await edit_or_reply(event, f"`{value}`")

# إضافة صورة لأي متغير صوري مدعوم
@l313l.ar_cmd(pattern="اضف صورة ([^ ]+)(?: ?(.*))?")
async def add_img_var(event):
    import requests, os
    reply = await event.get_reply_message()
    img_type = event.pattern_match.group(1).strip()

    # دعم جميع الأنواع: لا نتحقق من IMG_VARS
    if not (reply and reply.media):
        return await event.edit("**✗ يجب الرد على صورة لإضافتها**")
    jokevent = await event.edit(f"`⌔︙جـار رفع الصورة إلى أمر {img_type} ...`")
    try:
        media = await event.client.download_media(reply)
        with open(media, "rb") as file:
            response = requests.post(
                "https://uguu.se/upload.php",
                files={"files[]": file},
            )
        if response.status_code == 200 and response.json().get("success"):
            url = response.json()["files"][0]["url"]
            # استخدم الاسم مباشرة كاسم المتغير
            addgvar(img_type, url)
            await jokevent.edit(f"**✓ تم إضافة الصورة إلى {img_type} بنجاح**")
            if BOTLOG_CHATID:
                await event.client.send_message(BOTLOG_CHATID, f"#اضف_صورة\nتم رفع صورة {img_type} والرابط:\n{url}")
        else:
            await jokevent.edit(f"**✗ حدث خطأ في رفع الصورة**\n`{response.json()}`")
        os.remove(media)
    except Exception as exc:
        await event.edit(f"**✗ خطأ :**\n`{exc}`")
        if os.path.exists(media):
            os.remove(media)

# حذف صورة لأي متغير صوري مدعوم
@l313l.ar_cmd(pattern="حذف صورة ([^ ]+)")
async def del_img_var(event):
    img_type = event.pattern_match.group(1).strip()
    if img_type not in IMG_VARS:
        return await edit_delete(event, "**✗ نوع الصورة غير مدعوم**")
    varname = IMG_VARS[img_type]
    if gvarstatus(varname) is None:
        return await edit_delete(event, "**✗ لم يتم تعيين صورة لهذا الأمر مسبقاً**")
    delgvar(varname)
    await edit_or_reply(event, f"**✓ تم حذف صورة `{img_type}` بنجاح.**")
    if BOTLOG_CHATID:
        await event.client.send_message(BOTLOG_CHATID, f"#حذف_صورة\nتم حذف صورة {img_type} ({varname}) من القاعدة.")

# جلب رابط صورة لأي متغير صوري مدعوم
@l313l.ar_cmd(pattern="جلب صورة ([^ ]+)")
async def get_img_var(event):
    img_type = event.pattern_match.group(1).strip()
    if img_type not in IMG_VARS:
        return await edit_delete(event, "**✗ نوع الصورة غير مدعوم**")
    varname = IMG_VARS[img_type]
    value = gvarstatus(varname)
    if value is None:
        return await edit_delete(event, "**✗ لم يتم تعيين صورة لهذا الأمر بعد**")
    await edit_or_reply(event, f"`{value}`")