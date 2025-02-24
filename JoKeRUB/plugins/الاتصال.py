import html
import os
from requests import get
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.utils import get_input_location
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from JoKeRUB import l313l
from JoKeRUB.core.logger import logging
from ..Config import Config
from ..core.managers import edit_or_reply
from ..helpers import get_user_from_event, reply_id
from . import spamwatch


@l313l.on(admin_cmd(pattern="رفع مساعد(?: |$)(.*)",
    command=("رفع مساعد", plugin_category),
    info={
        "header": "لـ رفع مستخدم كـ مطور مساعد",
        "الاستـخـدام": " {tr}رفع مساعد بالـرد او {tr}رفع مساعد + معـرف/ايـدي الشخص",
    },
)
async def promote_assistant(event):
    "Promotes a user to assistant developer"
    replied_user = await get_user_from_event(event)
    if not replied_user:
        return await edit_or_reply(event, "**- لـم استطـع العثــور ع الشخــص**")
    user_id = replied_user.id
    assistant_developers = gvarstatus("assistant_developers") or ""
    if str(user_id) in assistant_developers.split():
        return await edit_or_reply(event, "**- المستخدم هـو مطور مساعد بالفعل**")
    assistant_developers += f" {user_id}"
    addgvar("assistant_developers", assistant_developers.strip())
    await edit_or_reply(event, f"**- تـم رفـع {replied_user.first_name} كـ مطور مساعد بنجاح**")

@l313l.on(admin_cmd(pattern="تنزيل مساعد(?: |$)(.*)",
    command=("تنزيل مساعد", plugin_category),
    info={
        "header": "لـ تنزيل مستخدم من مطور مساعد",
        "الاستـخـدام": " {tr}تنزيل مساعد بالـرد او {tr}تنزيل مساعد + معـرف/ايـدي الشخص",
    },
)
async def demote_assistant(event):
    "Demotes a user from assistant developer"
    replied_user = await get_user_from_event(event)
    if not replied_user:
        return await edit_or_reply(event, "**- لـم استطـع العثــور ع الشخــص**")
    user_id = replied_user.id
    assistant_developers = gvarstatus("assistant_developers") or ""
    if str(user_id) not in assistant_developers.split():
        return await edit_or_reply(event, "**- المستخدم لـيس مطور مساعد**")
    updated_assistant_developers = " ".join([uid for uid in assistant_developers.split() if uid != str(user_id)])
    addgvar("assistant_developers", updated_assistant_developers.strip())
    await edit_or_reply(event, f"**- تـم تنزيل {replied_user.first_name} من مطور مساعد بنجاح**")

# بقية الأكواد...