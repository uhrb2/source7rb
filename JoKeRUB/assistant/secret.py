import json
import os
import re

from telethon.events import CallbackQuery

from JoKeRUB import l313l

@l313l.tgbot.on(CallbackQuery(data=re.compile(b"secret_(.*)")))
async def on_plug_in_callback_query_handler(event):
    timestamp = int(event.pattern_match.group(1).decode("UTF-8"))
    uzerid = gvarstatus("hmsa_id")
    ussr = int(uzerid) if uzerid.isdigit() else uzerid
    try:
        zzz = await l313l.get_entity(ussr)
    except ValueError:
        zzz = await l313l(GetUsersRequest(ussr))
    if os.path.exists("./zira/secret.txt"):
        jsondata = json.load(open("./zira/secret.txt"))
        try:
            message = jsondata[f"{timestamp}"]
            userid = message["userid"]
            ids = [userid, l313l.uid, zzz.id]
            if event.query.user_id in ids:
                encrypted_tcxt = message["text"]
                reply_pop_up_alert = encrypted_tcxt
            else:
                reply_pop_up_alert = "هذه الرسالة ليست مخصصة لك 🦓 - حقوق: uhrb2"
        except KeyError:
            reply_pop_up_alert = "- عذراً .. هذه الرسالة لم تعد موجودة في البوت - حقوق: uhrb2"
    else:
        reply_pop_up_alert = "- عذراً .. هذه الرسالة لم تعد موجودة في البوت - حقوق: uhrb2"
    await event.answer(reply_pop_up_alert, cache_time=0, alert=True)