import json
import os
import re

from telethon.events import CallbackQuery, NewMessage

from JoKeRUB import l313l

@l313l.tgbot.on(CallbackQuery(data=re.compile(b"rzan_(.*)")))
async def on_plug_in_callback_query_handler(event):
    timestamp = int(event.pattern_match.group(1).decode("UTF-8"))
    if os.path.exists("./JoKeRUB/secrets.txt"):
        jsondata = json.load(open("./JoKeRUB/secrets.txt"))
        try:
            message = jsondata[f"{timestamp}"]
            userid = message["userid"]
            ids = [userid, l313l.uid]
            if event.query.user_id in ids:
                encrypted_tcxt = message["text"]
                reply_pop_up_alert = encrypted_tcxt
            else:
                reply_pop_up_alert = "⌯︙عـذرا هذه الهـمسة ليست مخصصة لـك"
        except KeyError:
            reply_pop_up_alert = "⌯︙عـذرا هذه الهمسة لم تعد موجوده في سيـرفرات جـيبثون"
    else:
        reply_pop_up_alert = "⌯︙عـذرا هذه الهمسة لم تعد موجوده  "
    await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

@l313l.tgbot.on(NewMessage(pattern=r"همسة (.+)", outgoing=True))
async def whisper(event):
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        user_id = reply_message.sender_id
    else:
        parts = event.pattern_match.group(1).strip().split(" ", 1)
        if len(parts) != 2:
            await event.reply("استخدام غير صحيح. يجب أن يكون التنسيق: `همسة <النص> <اليوزر>` أو بالرد على رسالة")
            return
        user_id = parts[1]
        message = parts[0]
    
    if not user_id.isdigit():
        user = await event.client.get_entity(user_id)
        user_id = user.id
    
    await event.client.send_message(user_id, message)