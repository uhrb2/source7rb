"""
JoKeRUB team ©
By Reda
sub Hussein
"""
import os
from datetime import datetime
import speech_recognition as sr
from pydub import AudioSegment

from JoKeRUB import l313l
from ..core.managers import edit_delete, edit_or_reply
from ..helpers import media_type
from ..helpers.utils import reply_id
import ocrspace

plugin_category = "utils"

#لتخمط الملف اذا انته ابن گحبة انسخ وألصق لسورسك وصيح اني مطور الملف متعوب عليه وشغل ايد

@l313l.ar_cmd(pattern="احجي(?:\s|$)([\s\S]*)",
               command=("احجي", plugin_category),
              )
async def _(event):
    "تحويل الكلام الى نص."

    start = datetime.now()
    input_str = event.pattern_match.group(1)
    reply = await event.get_reply_message()
    lan = input_str
    if not lan:
         return await edit_delete(event, "يجب ان تضع اختصار اللغة المطلوبة")

    #ted = await edit_or_reply(event, str(lan))
    if not os.path.isdir(Config.TEMP_DIR):
        os.makedirs(Config.TEMP_DIR)
    mediatype = media_type(reply)
    if not reply or (mediatype and mediatype not in ["Voice", "Audio"]):
        return await edit_delete(
            event,
            "`قم بالرد على رسالة او مقطع صوتي لتحويله الى نص.`",
        )
    jepevent = await edit_or_reply(event, "`يجري تنزيل الملف...`")
    oggfi = await event.client.download_media(reply, Config.TEMP_DIR)
    await jepevent.edit("`يجري تحويل الكلام الى نص....`")
    r = sr.Recognizer()
    #audio_data = open(required_file_name, "rb").read()
    ogg = oggfi.removesuffix('.ogg')

    AudioSegment.from_file(oggfi).export(f"{ogg}.wav", format="wav")
    user_audio_file = sr.AudioFile(f"{ogg}.wav")
    with user_audio_file as source:
         audio = r.record(source)


    try:
         text = r.recognize_google(audio, language=str(lan))
    except ValueError:
         return await edit_delete(event, "**لا يوجد كلام في المقطع الصوتي**")
    except BaseException as err:
         return await edit_delete(event, f"**!لا يوجد كلام في هذا المقطع الصوتي\n{err}**")
    end = datetime.now()
    ms = (end - start).seconds

    string_to_show = "**يگول : **`{}`".format(
            text
        )
    await jepevent.edit(string_to_show)
    # now, remove the temporary file
    os.remove(oggfi)
    os.remove(f"{ogg}.wav")

langs = {
    'عربي': 'ara',
    'بلغاري': 'bul',
    'صيني مبسط': 'chs',
    'صيني تقليدي ': 'cht',
    'كرواتي': 'hrv',
    'دنماركي': 'dan',
    'الماني': 'dut',
    'انجليزي': 'eng',
    'فنلندي': 'fin',
    'فرنسي': 'fre',
    'الماني': 'ger',
    'يوناني': 'gre',
    'هنغاري': 'hun',
    'كوري': 'kor',
    'ايطالي': 'ita',
    'ياباني': 'jpn',
    'نرويجي': 'nor',
    'بولندي': 'pol',
    'برتغالي': 'por',
    'روسي': 'rus',
    'سلوفيني': 'slv',
    'اسباني': 'spa',
    'سويدي': 'swe',
    'تركي': 'tur',
}

def to_text(pic, api):
    try:
        output = api.ocr_file(open(pic, 'rb'))
    except Exception as e:
        return "حدث الخطأ التالي:\n{e}"
    else:
        if output:
            return output
        else:
            return "حدث خطأ في النضام , حاول مجدداً"
    finally:
        os.remove(pic)

@l313l.ar_cmd(pattern="استخرج(?:\s|$)([\s\S]*)",
               command=("استخرج", plugin_category),
              )
async def _(event):
    reply = await event.get_reply_message()
    lan = event.pattern_match.group(1)
    if not reply:
     return edit_delete(event, "**᯽︙ قم بالرد على الصورة المراد استخراج النص منه**")
    pic_file = await l313l.download_media(reply, Config.TMP_DOWNLOAD_DIRECTORY)
    if not pic_file:
        return await edit_delete(event, "**᯽︙ قم بالرد على صورة**")
    else:
     if not lan:
            api = ocrspace.API()
     else:    
            try:  
             lang = langs[lan.replace(" ", "")]
             api = ocrspace.API(language=lang)
            except BaseException as er:
             return await edit_delete(event, "**᯽︙ !لا يوجد هكذا لغة**")
     await edit_or_reply(event, "**᯽︙ يجري استخراج النص...**")
     await edit_or_reply(event, to_text(pic_file, api))


import asyncio
import speech_recognition as sr
import os

active_voice_event = False
target_word = None
group_call_chatid = None
already_sent = False
joined_call = False

from .. import l313l
from telethon import events
from pytgcalls import PyTgCalls

from .. import bot
pytg = PyTgCalls(bot)

@l313l.ar_cmd(pattern="انضمام$")
async def join_call(event):
    global group_call_chatid, joined_call
    group_call_chatid = event.chat_id
    try:
        await pytg.join_group_call(group_call_chatid)
        joined_call = True
        await event.reply("تم الانضمام للاتصال الصوتي.")
    except Exception:
        await event.reply("فشل الانضمام للاتصال الصوتي.")

@l313l.ar_cmd(pattern="فعالية تشغيل (.+)$")
async def start_voice_event(event):
    global active_voice_event, target_word, already_sent, group_call_chatid
    target_word = event.pattern_match.group(1).strip()
    group_call_chatid = event.chat_id
    active_voice_event = True
    already_sent = False
    await event.reply(f"تم تفعيل الفعالية، سأراقب الاتصال وأرد بـ +{target_word} أول ما تُنطق.")
    asyncio.create_task(listen_and_recognize())

@l313l.ar_cmd(pattern="فعالية تعطيل$")
async def stop_voice_event(event):
    global active_voice_event
    active_voice_event = False
    await event.reply("تم تعطيل فعالية مراقبة الاتصال.")

async def listen_and_recognize():
    global active_voice_event, target_word, group_call_chatid, already_sent, joined_call
    while active_voice_event and not already_sent and joined_call:
        try:
            audio_file_path = "temp_voice.wav"
            if os.path.exists(audio_file_path):
                r = sr.Recognizer()
                with sr.AudioFile(audio_file_path) as source:
                    audio = r.record(source)
                text = r.recognize_google(audio, language='ar')
                if target_word in text and not already_sent:
                    already_sent = True
        except Exception:
            pass
        await asyncio.sleep(0.2)

@l313l.ar_cmd(pattern=r'^\+(.+)$')
async def plus_word(event):
    global active_voice_event, target_word, already_sent, group_call_chatid
    if active_voice_event and not already_sent and event.chat_id == group_call_chatid:
        plused = event.pattern_match.group(1).strip()
        if plused == target_word:
            await event.reply(f'+{target_word}')
            already_sent = True