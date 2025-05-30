from telethon import events
import random, re
from JoKeRUB.utils import admin_cmd
import asyncio 

# Wespr File by  @F_O_1
# Copyright (C) 2021 JoKeRUB TEAM
@borg.on(admin_cmd(pattern="ميمز ?(.*)"))
async def memes_to_voice(event):
    l313lb = event.pattern_match.group(1)
    rrrd7 = "@iizbot"
    tap = await bot.inline_query(rrrd7, l313lb)
    msg = await tap[0].send(event.chat_id)
    file = await bot.download_media(msg)
    await bot.send_file(event.chat_id, file, voice_note=True)
    await event.delete()
    
@borg.on(admin_cmd("م27"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("اوامر الهمسه واكس او \n\n⌔︙الامر  • `.همسة`\n⌔︙الاستخدام  • لكتابة همسه سرية لشخص في المجموعه \n\n᯽︙ الامر • `.الهمسة`\n᯽︙ استخدامه • لعرض كيفية كتابة همسة سرية\n\n᯽︙ الامر • `.اكس او `\n ᯽︙ استخدامه • ففط ارسل الامر لبدء لعبة اكس او\n\n᯽︙ CH  - @RobinUserBot")
        
@borg.on(admin_cmd("الهمسة"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("**᯽︙ شـرح كيـفية كـتابة همـسة سـرية**\n اولا اكتب الامر  .همسة  بعدها الرسالة بعدها اكتب معرف الشخص\n مـثال  :   `.همسة ههلا @F_O_1`")
        
@borg.on(
    admin_cmd(
       pattern="اكس او$"
    )
)
# كتابة وتعديل فريق 7rB   #@F_O_1
#تم التعديل مره أخرى بواسطة برلين 
async def gamez(event):
    if event.fwd_from:
        return
    jmusername = "@xoBot"
    uunzz = "play"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(jmusername, uunzz)
    await tap[0].click(event.chat_id)
    await event.delete()


@borg.on(
    admin_cmd(pattern="همسة ?(.*)")
)
async def wspr(event):
    if event.fwd_from:
        return
    l313lb = event.pattern_match.group(1)
    rrrd7 = "@HBO0bot"
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    tap = await bot.inline_query(rrrd7, l313lb) 
    await tap[0].click(event.chat_id)
    await event.delete()

@borg.on(admin_cmd("م27"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("اوامر الهمسه واكس او \n\n⌔︙الامر  • `.همسة`\n⌔︙الاستخدام  • لكتابة همسه سرية لشخص في المجموعه \n\n᯽︙ الامر • `.الهمسة`\n᯽︙ استخدامه • لعرض كيفية كتابة همسة سرية\n\n᯽︙ الامر • `.اكس او `\n ᯽︙ استخدامه • ففط ارسل الامر لبدء لعبة اكس او\n\n᯽︙ CH  - @RobinUserBot")

@borg.on(admin_cmd("الهمسة"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("**᯽︙ شـرح كيـفية كـتابة همـسة سـرية**\n اولا اكتب الامر  .همسة  بعدها الرسالة بعدها اكتب معرف الشخص\n مـثال  :   `.همسة ههلا @F_O_1`")

@borg.on(
    admin_cmd(
       pattern="اكس او$"
    )
)
# كتابة وتعديل فريق 7rB   #@F_O_1
#تم التعديل مره أخرى بواسطة برلين 
async def gamez(event):
    if event.fwd_from:
        return
    jmusername = "@xoBot"
    uunzz = "play"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(jmusername, uunzz)
    await tap[0].click(event.chat_id)
    await event.delete()

@zedub.zed_cmd(pattern="(تفعيل البصمه الذاتيه|تفعيل البصمه الذاتية|تفعيل البصمة الذاتيه|تفعيل البصمة الذاتية)")
async def start_datea(event):
    global vocself

    if vocself:
        return await edit_or_reply(event, "**⎉╎حفظ البصمة الذاتية التلقائي 🎙**\n**⎉╎مفعلـه .. مسبقًـا ✅**")
    vocself = True
    await edit_or_reply(event, "**⎉╎تم تفعيل حفظ البصمة الذاتية 🎙**\n**⎉╎تلقائيًّـا .. بنجاح ✅**")

@zedub.zed_cmd(pattern="(ايقاف البصمه الذاتيه|ايقاف البصمه الذاتية|ايقاف البصمة الذاتيه|ايقاف البصمة الذاتية)")
async def stop_datea(event):
    global vocself

    if vocself:
        vocself = False
        return await edit_or_reply(event, "**⎉╎تم تعطيل حفظ البصمة الذاتية 🎙**\n**⎉╎الان صارت مو شغالة .. ✅**")
    await edit_or_reply(event, "**⎉╎حفظ البصمة الذاتية التلقائي 🎙**\n**⎉╎معطلـه .. مسبقـاً ✅**")

@zedub.on(events.NewMessage(func=lambda e: e.is_private and (e.audio or e.voice) and e.media_unread))
async def sddm(event):
    global vocself

    if vocself:
        sender = await event.get_sender()
        username = f"@{sender.username}" if sender.username else "لا يوجد"
        chat = await event.get_chat()
        voc = await event.download_media()
        PM_LOGGER_GROUP_ID
        await zedub.send_file(PM_LOGGER_GROUP_ID, voc, caption=f"ᯓ 𝙏𝙀𝙋𝙏𝙃𝙊𝙉 ⌁ - حفـظ البصمـة الذاتيــة 🎙\n⋆─┄─┄─┄─┄─┄─┄─⋆\n⌔ مࢪحبـًا .. عـزيـزي 🫂\n⌔ تـم حفظ البصمة الذاتية .. تلقائيًّـا ☑️ ❝\n⌔ معلومـات المـرسـل :-\n• الاسم : {_format.mentionuser(sender.first_name , sender.id)}\n• اليوزر : {username}\n• الايدي : {sender.id}")