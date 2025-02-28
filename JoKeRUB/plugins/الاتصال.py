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

import youtube_dl
from telethon.tl.types import DocumentAttributeAudio

# Command to play music
@l313l.on(admin_cmd(pattern="شغل(?: |$)([\س\S]*)"))
async def play_music(event):
    query = event.pattern_match.group(1).strip()
    if not query:
        return await event.edit("**- يرجى تحديد اسم الأغنية أو الرابط**")

    await event.edit("**جارٍ البحث عن الأغنية...**")
    
    # Download music from YouTube
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': '/tmp/%(title)s.%(ext)s',
        'quiet': True,
        'cookiefile': 'path/to/cookies.txt',  # مسار ملف cookies.txt
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(query, download=True)
        file_name = ydl.prepare_filename(info_dict)
        file_name = file_name.replace(".webm", ".mp3")

    # Send the audio file
    await event.client.send_file(
        event.chat_id,
        file_name,
        attributes=[DocumentAttributeAudio(
            duration=info_dict.get('duration'),
            title=info_dict.get('title'),
            performer=info_dict.get('uploader')
        )],
        caption=f"**🎵 {info_dict.get('title')} 🎵**"
    )
    await event.delete()

    # Delete the downloaded file
    os.remove(file_name)

