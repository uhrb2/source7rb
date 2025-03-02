import html
import os
import random
from requests import get
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.utils import get_input_location
from JoKeRUB import l313l
from random import choice
from l313l.razan.resources.strings import *
from telethon import events
from ..Config import Config
from ..core.managers import edit_or_reply
from ..helpers import get_user_from_event, reply_id
from . import spamwatch
from telethon.utils import get_display_name
from ..helpers.utils import reply_id, _catutils, parse_pre, yaml_format, install_pip, get_user_from_event, _format

plugin_category = "utils"

@l313l.on(admin_cmd(pattern="رفع(?: |$)([\س\S]*)"))
async def promote_user(event):
    match = event.pattern_match.group(1).strip()
    if not match:
        return await edit_or_reply(event, "**- يرجى تحديد الدور المطلوب**")

    user, custom = await get_user_from_event(event)
    if not user:
        return await edit_or_reply(event, "**- لـم استطـع العثــور ع الشخــص**")

    user_id = user.id
    user_name = user.first_name.replace("\u2060", "") if user.first_name else user.username

    # تحقق من عدم رفع المطور
    if user_id in [7182427468]:
        return await edit_or_reply(event, f"**- لكك دي هذا المطور**")

    me = await event.client.get_me()
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"

    await edit_or_reply(event, f"**᯽︙ المستخدم** [{user_name}](tg://user?id={user.id}) \n**᯽︙  تـم رفعـه {match} بواسطة :** {my_mention}")


from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.messages import GetMessagesRequest, ForwardMessagesRequest

@l313l.on(admin_cmd(pattern="نسخ(?: |$)([\س\S]*)"))
async def copy_restricted_posts(event):
    links = event.pattern_match.group(1).strip().split()
    if not links:
        return await event.edit("**- يرجى تحديد الروابط المراد نسخها**")
    
    saved_messages_peer = await event.client.get_input_entity("me")
    
    for link in links:
        try:
            post_id = int(link.split('/')[-1])
            chat = link.split('/')[-2]
            message = await event.client(GetMessagesRequest(chat_id=chat, id=[post_id]))
            if message and message.messages[0].restricted:
                await event.client(ForwardMessagesRequest(
                    from_peer=chat,
                    id=[post_id],
                    to_peer=saved_messages_peer,
                    silent=True,
                    with_my_score=True
                ))
            else:
                await event.edit(f"**- لم أتمكن من نسخ المنشور: {link}**")
        except Exception as e:
            await event.edit(f"**- حدث خطأ أثناء نسخ المنشور: {link}\nالخطأ: {str(e)}**")

    await event.delete()

import openai

# إعدادات مكتبة OpenAI
openai.api_key = "YOUR_API_KEY"

@l313l.on(admin_cmd(pattern="اسأل(?: |$)([\س\S]*)"))
async def ask_ai(event):
    question = event.pattern_match.group(1).strip()
    if not question:
        return await event.edit("**- يرجى تحديد السؤال المراد إرساله**")

    try:
        response = openai.Completion.create(
            engine="davinci",
            prompt=question,
            max_tokens=50
        )
        answer = response.choices[0].text.strip()
        await event.edit(f"**سؤالك:** {question}\n**الإجابة:** {answer}")
    except Exception as e:
        await event.edit(f"**- حدث خطأ أثناء معالجة السؤال:\nالخطأ: {str(e)}**")