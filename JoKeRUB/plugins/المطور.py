from TNT_HUNTER.__config import *
from TNT_HUNTER.__xtelethon import *
from telethon import events

@TNT.on(events.NewMessage(outgoing=True, pattern=r".مطور"))
async def _(event):
    await event.edit("تم التجربة بنجاح")
    await TNT.send_file(
                event.chat_id,
                file="https://t.me/floative/9",
                caption=f"""
Robin OWNER   : @F_O_1
Robin Channel : @RobinUserBot
Robin VERSION : `1.8`
""",
                link_preview=False,
                force_document=False,
                parse_mode=CustomParseMode('markdown'),
            )

