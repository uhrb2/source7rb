import asyncio
import base64
import io
import urllib.parse
import os
from pathlib import Path
import ytc
from ShazamAPI import Shazam
from telethon import types
from telethon.errors.rpcerrorlist import YouBlockedUserError, ChatSendMediaForbiddenError
from telethon.tl.functions.contacts import UnblockRequest as unblock
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from validators.url import url

from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.functions import delete_conv, name_dl, song_dl, video_dl, yt_search
from ..helpers.tools import media_type
from ..helpers.utils import _catutils, reply_id
from . import l313l

plugin_category = "utils"
LOGS = logging.getLogger(__name__)

# =========================================================== #
#                           STRINGS                           #
# =========================================================== #
SONG_SEARCH_STRING = "<code>يجؤة الانتظار قليلا يتم البحث على المطلوب</code>"
SONG_NOT_FOUND = "<code>عذرا لا يمكنني ايجاد اي اغنيه مثل هذه</code>"
SONG_SENDING_STRING = "<code>جارِ الارسال انتظر قليلا...</code>"
# =========================================================== #
#                                                             #
# =========================================================== #

import os
import time
import requests
from yt_dlp import YoutubeDL
from youtube_search import YoutubeSearch

def time_to_seconds(time_str):
    parts = time_str.strip().split(':')
    parts = list(map(int, parts))
    if len(parts) == 3:
        return parts[0] * 3600 + parts[1] * 60 + parts[2]
    elif len(parts) == 2:
        return parts[0] * 60 + parts[1]
    elif len(parts) == 1:
        return parts[0]
    return 0

@l313l.on(admin_cmd(pattern="بحث"))
async def handler(event):
    text = event.message.text
    chat_id = event.chat_id
    user_id = event.sender_id
    try:
        query = text.split(None, 1)[1]
    except IndexError:
        return await event.reply("⌔︙أكتب اسم الأغنية بعد الأمر")

    joker_hussein = f"**⌔︙ اصبر عمري، انزلك الأغنية الي طلبتها `{query}`**"
    wait_message = await event.edit(joker_hussein)

    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        res = results[0]
        title = res['title']
        video_id = res['id']
        duration = int(time_to_seconds(res['duration']))
        duration_string = time.strftime('%M:%S', time.gmtime(duration))

        if duration > 1500:
            return await event.edit("**⌔︙ صوت فوك 25 دقيقة ما اكدر انزله**")

        url = f'https://youtu.be/{video_id}'
        ydl_opts = {
            "format": "bestaudio[ext=m4a]",
            "forceduration": True,
"cookiefile": "cookies.txt"
        }

        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            audio_file = ydl.prepare_filename(info)

            if audio_file.endswith('.m4a'):
                new_audio_file = audio_file.replace('.m4a', '.mp3')
                os.rename(audio_file, new_audio_file)
                audio_file = new_audio_file

            title = info.get('title', 'عنوان غير متوفر')
            length = info.get('duration', 0)
            duration_string = time.strftime('%M:%S', time.gmtime(length))

            thumb_url = info.get('thumbnail', '')
            thumb_path = ''
            if thumb_url:
                response = requests.get(thumb_url)
                if response.status_code == 200:
                    safe_title = title.replace("/", "-").replace("\\", "-")
                    thumb_path = f"{safe_title}.jpg"
                    with open(thumb_path, 'wb') as f:
                        f.write(response.content)

            if thumb_path and os.path.exists(thumb_path):
                await event.client.send_file(
                    chat_id,
                    audio_file,
                    title=title,
                    thumb=thumb_path,
                    caption=f'@aljokeruserbot ~ {duration_string} ⏳',
                )
            else:
                await event.client.send_file(
                    chat_id,
                    audio_file,
                    title=title,
                    caption=f'@aljokeruserbot ~ {duration_string} ⏳',
                )

            os.remove(audio_file)
            if thumb_path:
                os.remove(thumb_path)

            await wait_message.delete()

    except Exception as e:
        await wait_message.delete()
        return await event.reply(f"حدث خطأ: {e}")

@l313l.on(admin_cmd(pattern="فيديو"))
async def video_handler(event):
    text = event.message.text
    chat_id = event.chat_id
    try:
        query = text.split(None, 1)[1]
    except IndexError:
        return await event.reply("⌔︙أكتب اسم الفيديو بعد الأمر")

    wait_message = await event.edit(f"⌔︙ انتظر قليلاً، يتم جلب الفيديو `{query}`")

    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        res = results[0]
        title = res['title']
        video_id = res['id']
        duration = int(time_to_seconds(res['duration']))
        duration_string = time.strftime('%M:%S', time.gmtime(duration))

        if duration > 1500:
            return await event.edit("⌔︙ الفيديو أكثر من 25 دقيقة لا يمكن تحميله")

        url = f'https://youtu.be/{video_id}'
        ydl_opts = {
            "format": "bestvideo+bestaudio[ext=m4a]/best[ext=mp4]/best",
            "merge_output_format": "mp4",
            "cookiefile": ytc.youtube()
        }

        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            video_file = ydl.prepare_filename(info)

            if not video_file.endswith('.mp4'):
                new_video_file = video_file.rsplit('.', 1)[0] + '.mp4'
                os.rename(video_file, new_video_file)
                video_file = new_video_file

            title = info.get('title', 'عنوان غير متوفر')
            length = info.get('duration', 0)
            duration_string = time.strftime('%M:%S', time.gmtime(length))

            thumb_url = info.get('thumbnail', '')
            thumb_path = ''
            if thumb_url:
                response = requests.get(thumb_url)
                if response.status_code == 200:
                    safe_title = title.replace("/", "-").replace("\\", "-")
                    thumb_path = f"{safe_title}.jpg"
                    with open(thumb_path, 'wb') as f:
                        f.write(response.content)

            if thumb_path and os.path.exists(thumb_path):
                await event.client.send_file(
                    chat_id,
                    video_file,
                    caption=f'@RobinSource ~ {duration_string} ⏳',
                    thumb=thumb_path,
                    supports_streaming=True,
                )
            else:
                await event.client.send_file(
                    chat_id,
                    video_file,
                    caption=f'@RobinSource ~ {duration_string} ⏳',
                    supports_streaming=True,
                )

            os.remove(video_file)
            if thumb_path:
                os.remove(thumb_path)

            await wait_message.delete()

    except Exception as e:
        await wait_message.delete()
        return await event.reply(f"حدث خطأ: {e}")

@l313l.ar_cmd(pattern="اسم الاغنية$")
async def shazamcmd(event):
    reply = await event.get_reply_message()
    mediatype = media_type(reply)
    if not reply or not mediatype or mediatype not in ["Voice", "Audio"]:
        return await edit_delete(
            event, "⌔∮ يرجى الرد على مقطع صوتي او بصمه للبحث عنها"
        )
    catevent = await edit_or_reply(event, "**⌔∮ يتم معالجه المقطع الصوتي  .**")
    try:
        for attr in getattr(reply.document, "attributes", []):
            if isinstance(attr, types.DocumentAttributeFilename):
                name = attr.file_name
        dl = io.FileIO(name, "a")
        await event.client.fast_download_file(
            location=reply.document,
            out=dl,
        )
        dl.close()
        mp3_fileto_recognize = open(name, "rb").read()
        shazam = Shazam(mp3_fileto_recognize)
        recognize_generator = shazam.recognizeSong()
        track = next(recognize_generator)[1]["track"]
    except Exception as e:
        LOGS.error(e)
        return await edit_delete(
            catevent, f"**⌔∮ لقد حدث خطأ ما اثناء البحث عن اسم الاغنيه:**\n__{e}__"
        )

    image = track["images"]["background"]
    song = track["share"]["subject"]
    await event.client.send_file(
        event.chat_id, image, caption=f"**الاغنية:** `{song}`", reply_to=reply
    )
    await catevent.delete()

@l313l.ar_cmd(
    pattern="بحث2(?:\s|$)([\s\S]*)",
    command=("بحث2", plugin_category),
    info={
        "header": "To search songs and upload to telegram",
        "description": "Searches the song you entered in query and sends it quality of it is 320k",
        "usage": "{tr}song2 <song name>",
        "examples": "{tr}song2 memories song",
    },
)
async def _(event):
    "To search songs"
    song = event.pattern_match.group(1)
    chat = "@songdl_bot"
    reply_id_ = await reply_id(event)
    catevent = await edit_or_reply(event, SONG_SEARCH_STRING, parse_mode="html")
    async with event.client.conversation(chat) as conv:
        try:
            purgeflag = await conv.send_message("/start")
        except YouBlockedUserError:
            await edit_or_reply(
                catevent, "**Error:** Trying to unblock & retry, wait a sec..."
            )
            await catub(unblock("songdl_bot"))
            purgeflag = await conv.send_message("/start")
        await conv.get_response()
        await conv.send_message(song)
        hmm = await conv.get_response()
        while hmm.edit_hide is not True:
            await asyncio.sleep(0.1)
            hmm = await event.client.get_messages(chat, ids=hmm.id)
        baka = await event.client.get_messages(chat)
        if baka[0].message.startswith(
            ("I don't like to say this but I failed to find any such song.")
        ):
            await delete_conv(event, chat, purgeflag)
            return await edit_delete(
                catevent, SONG_NOT_FOUND, parse_mode="html", time=5
            )
        await catevent.edit(SONG_SENDING_STRING, parse_mode="html")
        await baka[0].click(0)
        await conv.get_response()
        await conv.get_response()
        music = await conv.get_response()
        await event.client.send_read_acknowledge(conv.chat_id)
        await event.client.send_file(
            event.chat_id,
            music,
            caption=f"<b>Title :- <code>{song}</code></b>",
            parse_mode="html",
            reply_to=reply_id_,
        )
        await catevent.delete()
        await delete_conv(event, chat, purgeflag)
