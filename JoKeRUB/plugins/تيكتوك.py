import asyncio
import shutil
import requests
from requests.exceptions import JSONDecodeError
import os
import re
from bs4 import BeautifulSoup as bs
import time
from datetime import timedelta
import math
import base64
from JoKeRUB import l313l

@l313l.ar_cmd(pattern="تك")
async def tiktok_dl(event):
    ms = event.message.message
    ms = ms.replace(".تك", "")
    if event:
        if "https://tiktok.com/" in ms or "https://vm.tiktok.com/" in ms:
            await event.message.delete()
            a = await l313l.send_message(event.chat_id, 'يجري البحث عن الملف..')
            link = ms.strip()
            try:
                response = requests.get(f"https://godownloader.com/api/tiktok-no-watermark-free?url={link}&key=godownloader.com")
                data = response.json()
                video_link = data["video_no_watermark"]
                response = requests.get(video_link)
                video_data = response.content
                directory = str(round(time.time()))
                filename = str(int(time.time())) + '.mp4'
                os.mkdir(directory)
                video_filename = f"{directory}/{filename}"
                with open(video_filename, "wb") as file:
                    file.write(video_data)
            except JSONDecodeError:
                return await a.edit("الرابط غير صحيح تأكد منه!")
            except Exception as er:
                if 'video_no_watermark' in str(er):
                    return await a.edit("**رابط الفيديو غير صحيح تأكد منه واعد المحاولة**")
                return await a.edit(f"حدث خطأ قم بتوجيه الرسالة الى مطوري @rd0r0\n{er}")

            await a.edit('يجري التحميل للخادم..!\nيجري الرفع للتلجرام⏳__')
            start = time.time()
            filesize_bytes = os.path.getsize(video_filename)
            filesize = filesize_bytes / (1024 * 1024)
            await l313l.send_file(
                event.chat_id, video_filename, reply_to=event.message.id, 
                force_document=False, caption=f"**الملف : ** {filename}\n**الحجم :** {round(filesize, 1)} MB"
            )
            await a.delete()
            shutil.rmtree(directory)