# PLUGIN FOR JoKeRUB
# @RobinUserBot

from telethon import events
import random, re
from ..Config import Config

from JoKeRUB.utils import admin_cmd

import asyncio
from JoKeRUB import l313l
from random import choice

from ..core.managers import edit_or_reply
from ..sql_helper.globals import gvarstatus

plugin_category = "extra"

rehu = [
    "᯽︙هـذه هي قائـمة الأوامر الخاصة بسورس Robin",
]

@l313l.ar_cmd(pattern="الاوامر(?:\s|$)([\س\S]*)")
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        F_O_1 = random.choice(rehu)
        await event.edit(
            f"✦ **⦑ قائمة اوامر سورس Robin ⦒** ✦\n\n"
            "1. **أوامر الادمن**\n"
            "   - `.م1` - عرض أوامر الأدمن مثل الحظر والكتم والتثبيت.\n"
            "2. **أوامر المجموعة**\n"
            "   - `.م2` - عرض الأوامر الخاصة بإدارة المجموعة مثل التفليش وإدارة الأعضاء.\n"
            "3. **أوامر الترحيب والردود**\n"
            "   - `.م3` - عرض الأوامر المتعلقة بالترحيب والردود التلقائية.\n"
            "4. **أوامر حماية الخاص والتلكراف**\n"
            "   - `.م4` - عرض الأوامر الخاصة بحماية الرسائل الخاصة والتلكراف.\n"
            "5. **أوامر المنشن والانتحال**\n"
            "   - `.م5` - عرض الأوامر الخاصة بالمنشن وانتحال الهوية.\n"
            "6. **أوامر التحميل والترجمة**\n"
            "   - `.م6` - عرض الأوامر المتعلقة بتحميل الملفات وترجمتها.\n"
            "7. **أوامر القفل والمنع**\n"
            "   - `.م7` - عرض الأوامر الخاصة بقفل ومنع الأوامر أو الوسائط.\n"
            "8. **أوامر التكرار والتنظيف**\n"
            "   - `.م8` - عرض الأوامر الخاصة بتكرار الرسائل وتنظيف الدردشة.\n"
            "9. **أوامر التخصيص والفارات**\n"
            "   - `.م9` - عرض الأوامر الخاصة بتخصيص الإعدادات والفارات.\n"
            "10. **أوامر الوقتي والتشغيل**\n"
            "    - `.م10` - عرض الأوامر الخاصة بالتحكم الزمني وتشغيل الأوامر تلقائيًا.\n"
            "11. **أوامر الكشف والروابط**\n"
            "    - `.م11` - عرض الأوامر الخاصة بالكشف عن الروابط وإدارتها.\n"
            "12. **أوامر المساعدة**\n"
            "    - `.م12` - عرض الأوامر التي تساعد في استخدام البوت.\n"
            "13. **أوامر الارسال**\n"
            "    - `.م13` - عرض الأوامر الخاصة بإرسال الرسائل والملفات.\n"
            "14. **أوامر الملصقات وكوكل**\n"
            "    - `.م14` - عرض الأوامر المتعلقة بإرسال الملصقات واستخدام محرك بحث كوكل.\n"
            "15. **أوامر التسلية والتحشيش**\n"
            "    - `.م15` - عرض الأوامر المسلية والمضحكة.\n"
            "16. **أوامر تحويل الصيغ والجهات**\n"
            "    - `.م16` - عرض الأوامر الخاصة بتحويل صيغ الملفات وإدارة الجهات.\n"
            "17. **أوامر التمبلر**\n"
            "    - `.م17` - عرض الأوامر الخاصة باستخدام تمبلر.\n"
            "18. **أوامر الحساب والترفيه**\n"
            "    - `.م18` - عرض الأوامر الخاصة بالحسابات والترفيه.\n"
        )

@l313l.ar_cmd(
    pattern="م1$",
    command=("م1", plugin_category),
)
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            "** قائمة اوامر الادمن لسورس Robin  **:\n"
            "• `.اوامر الحظر` - أوامر لحظر الأعضاء.\n"
            "• `.اوامر الكتم` - أوامر لكتم الأعضاء.\n"
            "• `.اوامر التثبيت` - أوامر لتثبيت الرسائل.\n"
        )

@l313l.ar_cmd(
    pattern="م2$",
    command=("م2", plugin_category),
)
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            "** قائمة اوامر المجـموعه لسورس Robin  **:\n"
            "• `.اوامر التفليش` - أوامر لتفليش الرسائل.\n"
            "• `.اوامر المحذوفين` - أوامر لإدارة الأعضاء المحذوفين.\n"
            "• `.اوامر الكروب` - أوامر لإدارة المجموعة.\n"
        )

@l313l.ar_cmd(
    pattern="م3$",
    command=("م3", plugin_category),
)
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            "** قائمة اوامر الـترحيب والـردود **:\n"
            "• `.اوامر الترحيب` - أوامر لإدارة رسائل الترحيب.\n"
            "• `.اوامر الردود` - أوامر لإدارة الردود التلقائية.\n"
        )

@l313l.ar_cmd(
    pattern="م4$",
    command=("م4", plugin_category),
)
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            "** قائمة اوامر حـماية الخاص والتلكراف **:\n"
            "• `.اوامر حماية الخاص` - أوامر لحماية الرسائل الخاصة.\n"
            "• `.اوامر حماية التلكراف` - أوامر لحماية التلكراف.\n"
        )

@l313l.ar_cmd(
    pattern="م5$",
    command=("م5", plugin_category),
)
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            "** قائمة اوامر الـمنشن والانتحال **:\n"
            "• `.اوامر المنشن` - أوامر لعمل منشن للأعضاء.\n"
            "• `.اوامر الانتحال` - أوامر لانتحال هوية الأعضاء.\n"
        )

@l313l.ar_cmd(
    pattern="م6$",
    command=("م6", plugin_category),
)
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            "** قائمة اوامر التحميل والترجمه **:\n"
            "• `.اوامر التحميل` - أوامر لتحميل الملفات.\n"
            "• `.اوامر الترجمة` - أوامر لترجمة النصوص.\n"
        )

@l313l.ar_cmd(
    pattern="م7$",
    command=("م7", plugin_category),
)
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            "** قائمة اوامر القفل والمنع **:\n"
            "• `.اوامر القفل` - أوامر لقفل الأوامر أو الوسائط.\n"
            "• `.اوامر المنع` - أوامر لمنع الأوامر أو الوسائط.\n"
        )

@l313l.ar_cmd(
    pattern="م8$",
    command=("م8", plugin_category),
)
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            "** قائمة اوامر التكرار والتنظيف **:\n"
            "• `.اوامر التكرار` - أوامر لتكرار الرسائل.\n"
            "• `.اوامر التنظيف` - أوامر لتنظيف الدردشة.\n"
        )

@l313l.ar_cmd(
    pattern="م9$",
    command=("م9", plugin_category),
)
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            "** قائمة التخصيص والفارات **:\n"
            "• `.اوامر التخصيص` - أوامر لتخصيص إعدادات البوت.\n"
            "• `.اوامر الفارات` - أوامر لإدارة الفارات.\n"
        )

@l313l.ar_cmd(
    pattern="م10$",
    command=("م10", plugin_category),
)
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            "** قائمة اوامر الوقتي والتشغيل **:\n"
            "• `.اوامر الوقتي` - أوامر لضبط الوقت.\n"
            "• `.اوامر التشغيل` - أوامر لتشغيل الأوامر تلقائيًا.\n"
        )

@l313l.ar_cmd(
    pattern="م11$",
    command=("م11", plugin_category),
)
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            "** قائمة اوامر الكـشف و الروابط **:\n"
            "• `.اوامر الكشف` - أوامر للكشف عن الروابط.\n"
            "• `.اوامر الروابط` - أوامر لإدارة الروابط.\n"
        )

@l313l.ar_cmd(
    pattern="م12$",
    command=("م12", plugin_category),
)
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            "** قائمة اوامر المساعدة **:\n"
            "• `.اوامر المساعدة` - أوامر للحصول على المساعدة في استخدام البوت.\n"
        )

@l313l.ar_cmd(
    pattern="م13$",
    command=("م13", plugin_category),
)
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            "** قائمة اوامر الارسال **:\n"
            "• `.اوامر الارسال` - أوامر لإرسال الرسائل والملفات.\n"
        )

@l313l.ar_cmd(
    pattern="م14$",
    command=("م14", plugin_category),
)
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            "** قائمة اوامر الملصقات وكوكل **:\n"
            "• `.اوامر الملصقات` - أوامر لإرسال الملصقات.\n"
            "• `.اوامر كوكل` - أوامر لاستخدام محرك بحث كوكل.\n"
        )

@l313l.ar_cmd(
    pattern="م15$",
    command=("م15", plugin_category),
)
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            "** قائمة اوامر التسلية والتحشيش **:\n"
            "• `.اوامر التسلية` - أوامر للأنشطة الترفيهية.\n"
            "• `.اوامر التحشيش` - أوامر للمزاح والتسلية.\n"
        )

@l313l.ar_cmd(
    pattern="م16$",
    command=("م16", plugin_category),
)
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            "** قائمة اوامر تحويل الصيغ و الجهات **:\n"
            "• `.اوامر تحويل الصيغ` - أوامر لتحويل صيغ الملفات.\n"
            "• `.اوامر الجهات` - أوامر لإدارة جهات الاتصال.\n"
        )

@l313l.ar_cmd(
    pattern="م18$",
    command=("م18", plugin_category),
)
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            "** قائمة اوامر الحساب و الترفيه **:\n"
            "• `.اوامر الحساب` - أوامر لإدارة الحسابات.\n"
            "• `.اوامر الترفيه` - أوامر للأنشطة الترفيهية.\n"
        )

@l313l.ar_cmd(
    pattern="م25$",
    command=("م25", plugin_category),
)
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            "** قائمة الأوامر المدفوعة لسورس Robin**\n"
            "1 - `.امر اول تم`\n"
            "2 - `.أمر الذاتية`\n"
            "3 - `.أمر النسخ`\n"
        )