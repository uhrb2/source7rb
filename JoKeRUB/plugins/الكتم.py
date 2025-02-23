import base64
import asyncio
from datetime import datetime
from telethon import events
from telethon.errors import BadRequestError, UserAdminInvalidError
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import ChatBannedRights
from telethon.utils import get_display_name

from JoKeRUB import l313l

from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import _format
from ..sql_helper import gban_sql_helper as gban_sql
from ..sql_helper.mute_sql import is_muted, mute, unmute
from . import BOTLOG, BOTLOG_CHATID, admin_groups, get_user_from_event

plugin_category = "admin"
joker_users = []
import os

file_path = '7rB Mute.txt'

if not os.path.isfile(file_path):
    open(file_path, 'w').close()

def add_to_mute_list(user):
    with open(file_path, 'a') as file:
        file.write(f"{user.id}\n")

def remove_from_mute_list(user_id):
    global file_path  # Ensure you are modifying the global file_path
    file_path = [id for id in file_path if id != str(user_id)]

#=================== الكـــــــــــــــتم  ===================  #

@l313l.ar_cmd(pattern=f"كتم(?:\s|$)([\s\S]*)")
async def mutejep(event):
    if event.is_private:
        replied_user = await event.client.get_entity(event.chat_id)
        if is_muted(event.chat_id, event.chat_id):  # Corrected this line
            return await event.edit(
                "**- هـذا المسـتخـدم مڪتـوم . . سـابقـاً **"
            )
        if event.chat_id == l313l.uid:
            return await edit_delete(event, "**𖡛... . لمـاذا تࢪيـد كتم نفسـك؟  ...𖡛**")
        if event.chat_id in [7182427468, 5616315677, 7944932338, 6248359289, 5931765554]:
            return await edit_delete(event, "** دي . . لا يمڪنني كتـم مطـور السـورس  ╰**")
        try:
            mute(event.chat_id, event.chat_id)  # Corrected this line
            add_to_mute_list(replied_user)
        except Exception as e:
            await event.edit(f"**- خطــأ : **`{e}`")
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#كتــم_الخــاص\n"
                f"**- الشخـص  :** [{replied_user.first_name}](tg://user?id={event.chat_id})\n",
            )
    else:
        args = event.pattern_match.group(1).strip()
        user = None

        if event.reply_to_msg_id:
            replied_message = await event.get_reply_message()
            user = await event.client.get_entity(replied_message.from_id)
        elif args:
            try:
                user = await event.client.get_entity(args)
            except Exception as e:
                return await event.edit(f"**- خطــأ : **`{e}`")

        if not user:
            return await event.edit("**- يرجى تقديم المعرف أو اسم المستخدم، أو الرد على رسالة المستخدم**")

        chat = await event.get_chat()
        admin = chat.admin_rights
        creator = chat.creator
        if not admin and not creator:
            return await edit_or_reply(
                event, "** أنـا لسـت مشـرف هنـا ؟!! .**"
            )
        if user.id == l313l.uid:
            return await edit_or_reply(event, "**𖡛... . لمـاذا تࢪيـد كتم نفسـك؟  ...𖡛**")
        if user.id == 7182427468:
            return await edit_or_reply(event, "** دي . . لا يمڪنني كتـم مطـور السـورس  ╰**")
        if is_muted(user.id, event.chat_id): 
            return await edit_or_reply(
                event, "**عــذراً .. هـذا الشخـص مكتــوم سـابقــاً هنـا**"
            )
        result = await event.client.get