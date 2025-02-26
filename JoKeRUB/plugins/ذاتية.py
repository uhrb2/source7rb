
@borg.on(
    admin_cmd(pattern="لايك ?(.*)")
)
async def wspr(event):
    if event.fwd_from:
        return
    l313lb = event.pattern_match.group(1)
    rrrd7 = "@like"
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    tap = await bot.inline_query(rrrd7, l313lb) 
    await tap[0].click(event.chat_id)
    await event.delete()

@borg.on(admin_cmd("م27"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("᯽︙ اوامر الهمسه واكس او \n\n⌔︙الامر  • `.همسة`\n⌔︙الاستخدام  • لكتابة همسه سرية لشخص في المجم[...]

@borg.on(admin_cmd("الهمسة"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("**᯽︙ شـرح كيـفية كـتابة همـسة سـرية**\n᯽︙ اولا اكتب الامر  .همسة  بعدها الرسالة بعدها اكتب معر[...]

@borg.on(
    admin_cmd(
       pattern="اكس او$"
    )
)
# كتابة وتعديل فريق 7rB   #@F_O_1
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



from telethon import events
from JoKeRUB.utils import admin_cmd
import asyncio

# متغير عالمي لتتبع حالة النسخ
is_copying = False

from telethon.tl.types import MessageService

@l313l.on(admin_cmd(pattern="تسريب (.+)"))
async def copy_posts(event):
    global is_copying
    if is_copying:
        await event.edit("عملية التسريب جارية بالفعل.")
        return

    source_channel_username = event.pattern_match.group(1).strip()

    try:
        source_channel = await bot.get_entity(source_channel_username)
        destination_channel = await event.get_input_chat()

        posts_count = 0
        is_copying = True
        messages = []
        async for message in bot.iter_messages(source_channel, limit=None):
            if isinstance(message, MessageService):
                continue
            messages.append(message)

        for message in reversed(messages):
            if not is_copying:
                await event.edit(f"تم إيقاف عملية التسريب بعد تسريب {posts_count} منشور.")
                return
            await bot.send_message(destination_channel, message)
            posts_count += 1
            if posts_count >= 4000:
                break

        is_copying = False
        await event.edit(f"تم تسريب {posts_count} منشور بنجاح من {source_channel_username} إلى القناة الحالية.")
    except Exception as e:
        is_copying = False
        await event.edit(f"حدث خطأ: {str(e)}")

@l313l.on(admin_cmd(pattern="إيقاف التسريب"))
async def stop_copying(event):
    global is_copying
    is_copying = False
    await event.edit("تم إيقاف عملية التسريب.")