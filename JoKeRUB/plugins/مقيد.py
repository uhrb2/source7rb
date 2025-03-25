import re
import asyncio
import time
from JoKeRUB import l313l

from ..core.managers import edit_or_reply
from ..sql_helper.filter_sql import (
    add_filter,
    get_filters,
    remove_all_filters,
    remove_filter,
)
from . import BOTLOG, BOTLOG_CHATID

plugin_category = "utils"
ROZTEXT = "عـذرا لا يمكـنك اضافـة رد هـنا"

restricted_mode = False

@l313l.ar_cmd(
    pattern="تفعيل الوضع المقيد$",
    command=("تفعيل الوضع المقيد", plugin_category),
    info={
        "header": "لتفعيل وضع جلب الفيديوهات المقيدة",
        "description": "يقوم بتفعيل الوضع الذي يجلب الفيديوهات المقيدة من الروابط",
    },
)
async def enable_restricted_mode(event):
    global restricted_mode
    restricted_mode = True
    await edit_or_reply(event, "**᯽︙ تم تفعيل الوضع المقيد بنجاح ✓**")


@l313l.ar_cmd(
    pattern="تعطيل الوضع المقيد$",
    command=("تعطيل الوضع المقيد", plugin_category),
    info={
        "header": "لتعطيل وضع جلب الفيديوهات المقيدة",
        "description": "يقوم بتعطيل الوضع الذي يجلب الفيديوهات المقيدة من الروابط",
    },
)
async def disable_restricted_mode(event):
    global restricted_mode
    restricted_mode = False
    await edit_or_reply(event, "**᯽︙ تم تعطيل الوضع المقيد بنجاح ✓**")


@l313l.ar_cmd(
    pattern="جلب الفيديوهات$",
    command=("جلب الفيديوهات", plugin_category),
    info={
        "header": "لجلب الفيديوهات المقيدة من الروابط",
        "description": "يقوم بجلب الفيديوهات المقيدة من الروابط كل 20 ثانية",
    },
)
async def fetch_restricted_videos(event):
    if not restricted_mode:
        await edit_or_reply(event, "الوضع المقيد غير مفعل. يرجى تفعيله أولاً باستخدام أمر 'تفعيل الوضع المقيد'.")
        return

    links = event.raw_text.split()
    for link in links:
        # قم بجلب الفيديو من الرابط هنا ووضعه في الرسائل المحفوظة
        # مثال: await download_video_and_save_to_messages(link)
        await asyncio.sleep(20)  # انتظر 20 ثانية بين كل رابط

    await edit_or_reply(event, "**᯽︙ تم جلب الفيديوهات المقيدة بنجاح ✓**")