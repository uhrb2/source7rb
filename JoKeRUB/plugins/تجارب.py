from telethon import events
from JoKeRUB.utils import admin_cmd, edit_delete
from JoKeRUB import l313l
from ..sql_helper.globals import addgvar, delgvar, gvarstatus

@l313l.on(admin_cmd(pattern="(الصوتية تشغيل|صوتية تشغيل)"))
async def enable_voice_save(event):
    if gvarstatus("savevoiceforme"):
        return await edit_delete(event, "᯽︙حفظ الصوتيات مفعل بالفعل.")
    addgvar("savevoiceforme", "enabled")
    await edit_delete(event, "᯽︙تم تفعيل حفظ الصوتيات.")

@l313l.on(admin_cmd(pattern="(الصوتية تعطيل|صوتية تعطيل)"))
async def disable_voice_save(event):
    if gvarstatus("savevoiceforme"):
        delgvar("savevoiceforme")
        return await edit_delete(event, "᯽︙تم تعطيل حفظ الصوتيات.")
    await edit_delete(event, "᯽︙الحفظ غير مفعل سابقًا.")

# الكود الذي يرسل الصوتيات المؤقتة الى الرسائل المحفوظة
@l313l.on(events.NewMessage(incoming=True))
async def forward_temp_voice_to_saved(event):
    if not gvarstatus("savevoiceforme"):
        return
    # تحقق أن الرسالة صوتية مؤقتة
    if event.voice and event.media and getattr(event.media, "ttl_seconds", None):
        try:
            # تحميل الصوتية مؤقتاً
            file_path = await event.download_media()
            # إرسال الصوتية للرسائل المحفوظة
            await event.client.send_file(
                "me",
                file_path,
                caption="تم حفظ صوتية مؤقتة تلقائياً"
            )
        except Exception as e:
            await event.reply(f"حدث خطأ أثناء إرسال الصوتية للمحفوظات: {e}")