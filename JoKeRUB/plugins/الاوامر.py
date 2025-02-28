# WRITE  BY JoKeRUB
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

from telethon.tl.types import InputStickerSetShortName

# قائمة لتعابير تليجرام المميزة
custom_emojis = {}

@l313l.ar_cmd(pattern="اضافة تعبير(?:\s|$)([\s\S]*)")
async def add_custom_emoji(event):
    input_str = event.pattern_match.group(1)
    if not input_str:
        await event.edit("يرجى إدخال التعبير و ID الخاص بالتعبير.")
        return
    try:
        emoji, emoji_id = input_str.split(',')
        custom_emojis[emoji.strip()] = emoji_id.strip()
        await event.edit(f"تم إضافة التعبير {emoji.strip()} برقم ID {emoji_id.strip()}.")
    except ValueError:
        await event.edit("صيغة الإدخال غير صحيحة. يرجى استخدام الصيغة: تعبير, ID")

@l313l.ar_cmd(pattern="عرض تعبير(?:\s|$)([\s\S]*)")
async def get_custom_emoji(event):
    emoji = event.pattern_match.group(1).strip()
    if emoji in custom_emojis:
        await event.edit(f"ID الخاص بالتعبير {emoji} هو {custom_emojis[emoji]}.")
    else:
        await event.edit(f"التعبير {emoji} غير موجود.")

# تعديل الدالة الحالية لإضافة التعبير المميز في نهاية كلمة "سورس"
@l313l.ar_cmd(pattern="الاوامر(?:\s|$)([\s\S]*)")
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        F_O_1 = random.choice(rehu)
        emoji_id = custom_emojis.get("سورس", "❓")  # استخدم التعبير المميز إذا كان موجودًا
        await event.edit(
            f"✦ **⦑ قائمة اوامر سورس {✨,  10024} Robin ⦒** ✦\n\n"
            "1. **أوامر الادمن**\n"
            "   - `.م1`\n"
            "2. **أوامر المجموعة**\n"
            "   - `.م2`\n"
            "3. **أوامر الترحيب والردود**\n"
            "   - `.م3`\n"
            "4. **أوامر حماية الخاص والتلكراف**\n"
            "   - `.م4`\n"
            "5. **أوامر المنشن والانتحال**\n"
            "   - `.م5`\n"
            "6. **أوامر التحميل والترجمة**\n"
            "   - `.م6`\n"
            "7. **أوامر القفل والمنع**\n"
            "   - `.م7`\n"
            "8. **أوامر التكرار والتنظيف**\n"
            "   - `.م8`\n"
            "9. **أوامر التخصيص والفارات**\n"
            "   - `.م9`\n"
            "10. **أوامر الوقتي والتشغيل**\n"
            "    - `.م10`\n"
            "11. **أوامر الكشف والروابط**\n"
            "    - `.م11`\n"
            "12. **أوامر المساعدة**\n"
            "    - `.م12`\n"
            "13. **أوامر الارسال**\n"
            "    - `.م13`\n"
            "14. **أوامر الملصقات وكوكل**\n"
            "    - `.م14`\n"
            "15. **أوامر التسلية والتحشيش**\n"
            "    - `.م15`\n"
            "16. **أوامر تحويل الصيغ والجهات**\n"
            "    - `.م16`\n"
            "17. **أوامر التمبلر**\n"
            "    - `.م17`\n"
            "18. **أوامر الحساب والترفيه**\n"
            "    - `.م18`\n"
        )

@l313l.ar_cmd(
    pattern="م1$",
    command=("م1", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر الادمن لسورس Robin  **:\n • ( `.اوامر الحظر` )\n • (  `.اوامر الكتم` )\n • ( `.اوامر التثبيت` )\n • ( `.اوامر الاشراف` )\n︙CH : @RobinUserBot"
)
		
@l313l.ar_cmd(
    pattern="م2$",
    command=("م2", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر المجـموعه لسورس Robin  **:\n • ( `.اوامر التفليش` )\n • ( `.اوامر المحذوفين` )\n • ( `.اوامر الكروب` )\n︙CH : @RobinUserBot"
)

@l313l.ar_cmd(
    pattern="م3$",
    command=("م3", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر الـترحيب والـردود **:\n ★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الترحيب` )\n- ( `.اوامر الردود` )\n★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n⌔︙CH : @RobinUserBot"
)
@l313l.ar_cmd(
    pattern="م4$",
    command=("م4", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر حـماية الخاص والتلكراف **:\n ★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الحماية` )\n- ( `.اوامر التلكراف` ) \n★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n⌔︙CH : @RobinUserBot"
)
@l313l.ar_cmd(
    pattern="م5$",
    command=("م5", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر الـمنشن والانتحال **:\n ★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الانتحال` )\n- ( `.اوامر التقليد` )\n- ( `.اوامر المنشن` ) \n★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n⌔︙CH : @RobinUserBot"
)

@l313l.ar_cmd(
    pattern="م6$",
    command=("م6", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر التحميل والترجمه **:\n ★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر النطق` )\n- ( `.اوامر التحميل` )\n- ( `.اوامر الترجمة` ) \n★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n⌔︙CH : @RobinUserBot"
)

@l313l.ar_cmd(
    pattern="م7$",
    command=("م7", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر القفل والمنع **:\n★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر القفل` )\n- ( `.اوامر الفتح` )\n- ( `.اوامر المنع` ) \n★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n⌔︙CH : @RobinUserBot"
)

@l313l.ar_cmd(
    pattern="م8$",
    command=("م8", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر التكرار والتنظيف **:\n★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر التكرار` )\n- ( `.اوامر السبام` )\n- ( `.اوامر التنظيف` ) \n- ( `.اوامر المسح` ) \n★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n⌔︙CH : @RobinUserBot"
)

@l313l.ar_cmd(
    pattern="م9$",
    command=("م9", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة التخصيص والفارات **:\n ★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر التخصيص` )\n لتغير الصور والكلايش كل من الحماية والفحص والبنك\n- ( `.اوامر الفارات` )\n - لتغير الاسم وزخرفة الوقت والصورة الوقتية والمنطقة الزمنية ورمز الاسم والبايو الوقتي وغيرها\n★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n⌔︙CH : @RobinUserBot"
		)

@l313l.ar_cmd(
    pattern="م10$",
    command=("م10", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر الوقتي والتشغيل **:\n ★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الاسم` )\n- ( `.اوامر البايو` )\n- ( `.اوامر الكروب الوقتي` )\n- ( `.اوامر التشغيل` ) \n- ( `.اوامر الاطفاء` ) \n★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n⌔︙CH : @RobinUserBot"
)	

@l313l.ar_cmd(
    pattern="م11$",
    command=("م11", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر الكـشف و الروابط **:\n ★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الكشف` )\n- ( `.اوامر الروابط` ) \n\n ★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n⌔︙CH : @RobinUserBot"
)
@l313l.ar_cmd(
    pattern="م12$",
    command=("م12", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر المساعدة  **:\n ★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الوقت والتاريخ` )\n- ( `.اوامر كورونا` )\n- ( `.اوامر الصلاة` ) \n- ( `.اوامر مساعدة` )\n- ( `.اوامر الاذاعه` ) \n★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n⌔︙CH : @RobinUserBot"
)
@l313l.ar_cmd(
    pattern="م13$",
    command=("م13", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر الارسال **:\n ★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.امر الصورة الذاتية` )\n- ( `.اوامر التحذيرات` )\n- ( `.اوامر اللستة` )\n- ( `.اوامر الملكية` ) \n- ( `.اوامر السليب` ) \n- ( `.اوامر الاذكار` )\n★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n⌔︙CH : @RobinUserBot"
)
@l313l.ar_cmd(
    pattern="م14$",
    command=("م14", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر الملصقات وكوكل **:\n ★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الملصقات` )\n- ( `.اوامر كوكل` )\n★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n⌔︙CH : @RobinUserBot"
)

@l313l.ar_cmd(
    pattern="م15$",
    command=("م15", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر التسلية والتحشيش **:\n ★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر التسلية` )\n- ( `.اوامر التحشيش` )\n- ( `.اوامر الميمز` )\n★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n⌔︙CH : @RobinUserBot"
)

@l313l.ar_cmd(
    pattern="م16$",
    command=("م16", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر تحويل الصيغ و الجهات **:\n ★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر التحويل` )\n- ( `.اوامر الجهات` ) \n★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n⌔︙CH : @RobinUserBot"
)

@l313l.ar_cmd(
    pattern="م18$",
    command=("م18", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر الحساب و الترفيه **:\n ★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الترفيه` )\n- ( `.اوامر الحساب` ) \n★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n⌔︙CH : @RobinUserBot"

)


@l313l.ar_cmd(
    pattern="م25$",
    command=("م25", plugin_category),
)
async def _(event):
        if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
                await event.edit(
          "** قائمة الأوامر المدفوعة لسورس Robin**\n 1 - `.امر اول تم`\n 2 - `.أمر الذاتية`\n 3 - `.أمر النسخ`"
)

