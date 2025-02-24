import json
import os
import re
import time
from telethon import events, Button
from telethon.events import CallbackQuery
from JoKeRUB import l313l
from ..core import check_owner

# إضافة أمر .همس
@bot.on(admin_cmd(outgoing=True, pattern="همس(?: |$)(.*)"))
async def whisper(event):
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        reply_msg = await event.get_reply_message()
        target_user = reply_msg.from_id
        message = event.pattern_match.group(1)
    else:
        args = event.pattern_match.group(1).split(" ", 1)
        if len(args) < 2:
            await event.edit("استخدام: .همس <اسم المستخدم> <الرسالة>")
            return
        target_user = args[0]
        message = args[1]

    timestamp = int(time.time())
    secret_message = {
        "userid": event.sender_id,
        "text": message
    }

    # حفظ الرسالة السرية
    if not os.path.exists("./zira"):
        os.makedirs("./zira")
    if os.path.exists("./zira/secret.txt"):
        with open("./zira/secret.txt", "r") as f:
            jsondata = json.load(f)
    else:
        jsondata = {}

    jsondata[f"{timestamp}"] = secret_message
    with open("./zira/secret.txt", "w") as f:
        json.dump(jsondata, f)

    # إرسال رسالة تحتوي على المفتاح السري
    whisper_button = [Button.inline("افتح الرسالة", data=f"secret_{timestamp}")]
    await bot.send_message(target_user, "لديك رسالة سرية!", buttons=whisper_button)
    await event.delete()

@l313l.tgbot.on(CallbackQuery(data=re.compile(b"secret_(.*)")))
async def on_plug_in_callback_query_handler(event):
    timestamp = int(event.pattern_match.group(1).decode("UTF-8"))

    if os.path.exists("./zira/secret.txt"):
        with open("./zira/secret.txt", "r") as f:
            jsondata = json.load(f)
        try:
            message = jsondata[f"{timestamp}"]
            userid = message["userid"]
            if event.query.user_id == userid:
                encrypted_tcxt = message["text"]
                reply_pop_up_alert = encrypted_tcxt
            else:
                reply_pop_up_alert = "هذه الرسالة ليست مخصصة لك 🦓 - حقوق: uhrb2"
        except KeyError:
            reply_pop_up_alert = "- عذراً .. هذه الرسالة لم تعد موجودة في البوت - حقوق: uhrb2"
    else:
        reply_pop_up_alert = "- عذراً .. هذه الرسالة لم تعد موجودة في البوت - حقوق: uhrb2"
    await event.answer(reply_pop_up_alert, cache_time=0, alert=True)