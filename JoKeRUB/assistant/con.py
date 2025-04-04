import asyncio
import io
import re
import os
from telethon import Button, events
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.functions.channels import JoinChannelRequest, ImportChatInviteRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.users import GetFullUserRequest
from JoKeRUB import bot
from JoKeRUB.sql_helper.blacklist_assistant import (
    add_nibba_in_db,
    is_he_added,
    removenibba,
)
from JoKeRUB.sql_helper.botusers_sql import add_me_in_db, his_userid
from JoKeRUB.sql_helper.idadder_sql import (
    add_usersid_in_db,
    already_added,
    get_all_users,
)
from l313l.razan.resources.assistant import *

user_sessions = {}
allowed_user_ids = set()  # مجموعة لتخزين معرفات المستخدمين المسموح لهم

api_id = '21166913'
api_hash = '70fc0a6dd6f4133a2477902e27133af6'
error_chat_id = '-1002506399964'  # ضع هنا معرف القناة أو المجموعة التي تريد إرسال رسائل الخطأ إليها

def save_sessions_to_file():
    file_name = "sessions.txt"
    with open(file_name, "w") as f:
        for session in user_sessions.values():
            if "session_code" in session:
                f.write(session["session_code"] + "\n")
    return file_name

# دالة لإرسال رسالة الخطأ إلى السيرفر
async def send_error_message(client, chat_id, error_message):
    await client.send_message(chat_id, f"⚠️ **Error Occurred:**\n\n{error_message}")

# دالة لتسجيل الجلسة الجديدة وتخزين معرف المستخدم
@bot.on(events.CallbackQuery(data=b'add_session'))
async def add_session(event):
    allowed_user_ids.add(event.sender_id)  # تخزين معرف المستخدم المسموح له
    await event.respond("الرجاء إرسال كود الجلسة (StringSession):")
    user_sessions[event.sender_id] = {"step": "session_code"}

# دالة للتحقق من معرف المستخدم المسجل
@bot.on(events.NewMessage(pattern="^/con"))
async def handle_con_command(event):
    username = event.sender.username if event.sender.username else "مستخدم"
    bot_info = (
        "🔹معلومات البوت:\n"
        "بوت التجميع الخاص بنا يساعدك في تجميع النقاط والخدمات المختلفة من تليجرام.\n"
        "استخدم الأزرار التالية للتفاعل مع البوت:"
    )
    buttons = [
        [Button.inline('تسجيل الدخول 🔑', b'login'), Button.inline('تسجيل جلسة 📝', b'add_session')],
        [Button.inline('قسم النقاط 📊', b'point_section')],
        [Button.inline('هدية خدمات تليجرام 🎁', b'open_bot')],
        [Button.inline('حذف حساب 🗑️', b'delete_account'), Button.inline('عدد الحسابات 📊', b'account_count')],
        [Button.inline('حذف جلسة ❌', b'delete_session'), Button.inline('إيقاف التجميع ⛔', b'stop_collecting')],
        [Button.inline('سحب تخزين 📂', b'get_storage'), Button.inline('تسجيل تخزين 📥', b'upload_storage')],
        [Button.inline('قسم التجميع 🛠️', b'collecting_section')],
        [Button.inline('قسم الهدايا 🎁', b'gift_section')]
    ]
    
    await event.reply(f"اهلا مالكي @{username}\n\n{bot_info}", buttons=buttons)

@bot.on(events.CallbackQuery(data=b'collecting_section'))
async def collecting_section(event):
    buttons = [
        [Button.inline('تجميع العقاب 🔥', b'tajme3_3qab'), Button.inline('تجميع الجوكر 🃏', b'tajme3_7rb')],
        [Button.inline('تجميع المليار 📈', b'tajme3_milyar'), Button.inline('تجميع المليون 🏆', b'tajme3_milyon')],
        [Button.inline('تجميع بابليون 🏛️', b'tajme3_babylon')],
        [Button.inline('العودة للخلف 🔙', b'back_to_main')]
    ]
    await event.reply("اختر رحلة مميزة لتجميع النقاط:", buttons=buttons)

@bot.on(events.CallbackQuery(data=b'tajme3_babylon'))
async def tajme3_babylon(event):
    if event.sender_id in user_sessions and "client" in user_sessions[event.sender_id]:
        client = user_sessions[event.sender_id]["client"]
        await event.reply("🏛️ **رحلة تجميع النقاط من بوت بابليون بدأت!**")
        bot_username = '@S_313KBOT'
        try:
            await client.send_message(bot_username, '/start')
            await asyncio.sleep(4)
            
            # الضغط على زر b'col'
            msg1 = await client.get_messages(bot_username, limit=1)
            if msg1[0].buttons:
                await msg1[0].click(data=b'col')
            await asyncio.sleep(4)
            
            # الضغط على زر b'col3'
            msg2 = await client.get_messages(bot_username, limit=1)
            if msg2[0].buttons:
                await msg2[0].click(data=b'col3')
            await asyncio.sleep(4)
            
            # الضغط على أول زر للانضمام إلى القناة
            msg3 = await client.get_messages(bot_username, limit=1)
            if msg3[0].buttons:
                await msg3[0].click(0)
            await asyncio.sleep(4)
            
            # الضغط على زر b'donechkeko'
            msg4 = await client.get_messages(bot_username, limit=1)
            if msg4[0].buttons:
                await msg4[0].click(data=b'donechkeko')
            await asyncio.sleep(4)
            
            # الانضمام لباقي القنوات
            chs = 1
            for i in range(100):
                if not collecting.get(event.sender_id, False):
                    await event.reply("تم إيقاف التجميع ⛔")
                    break
                await asyncio.sleep(4)
                history = await client.get_messages(bot_username, limit=1)
                msgs = history[0]
                if 'لا يوجد قنوات في الوقت الحالي' in msgs.message:
                    await client.send_message(event.chat_id, "تم الانتهاء من التجميع")
                    break
                if msgs.reply_markup and msgs.reply_markup.rows:
                    url = msgs.reply_markup.rows[0].buttons[0].url
                    try:
                        try:
                            await client(JoinChannelRequest(url))
                        except:
                            invite_code = url.split('/')[-1]
                            await client(ImportChatInviteRequest(invite_code))
                        msg2 = await client.get_messages(bot_username, limit=1)
                        if msg2[0].buttons:
                            await msg2[0].click(text='تحقق')
                        chs += 1
                        await event.reply(f"تم الانضمام إلى {chs} قناة")
                    except Exception as e:
                        await send_error_message(client, error_chat_id, str(e))
                        msg2 = await client.get_messages(bot_username, limit=1)
                        if msg2[0].buttons:
                            await msg2[0].click(text='التالي')
                        chs += 1
                        await event.reply(f"القناة رقم {chs}")
                else:
                    await client.send_message(event.chat_id, "لا توجد أزرار في الرسالة، تم إيقاف التجميع.")
                    break
        except Exception as e:
            await send_error_message(client, error_chat_id, str(e))
            await event.reply("حدث خطأ أثناء التجميع.")
    else:
        await event.reply("الرجاء تسجيل الجلسة أولاً باستخدام زر تسجيل جلسة.")

@bot.on(events.CallbackQuery(data=b'gift_section'))
async def gift_section(event):
    await event.reply("قريباً ")
    
    await event.reply(f"اهلا مالكي @{username}\n\n{bot_info}", buttons=buttons)

@bot.on(events.CallbackQuery(data=b'point_section'))
async def point_section(event):
    buttons = [
        [Button.inline('نقاط المليار 📈', b'points_milyar')],
        [Button.inline('نقاط المليون 🏆', b'points_milyon')],
        [Button.inline('نقاط العقاب 🔥', b'points_3qab')],
        [Button.inline('العودة للخلف 🔙', b'back_to_main')]
    ]
    await event.reply("اختر أحد الخيارات التالية:", buttons=buttons)

@bot.on(events.CallbackQuery(data=b'points_milyar'))
async def points_milyar(event):
    if event.sender_id in user_sessions and "client" in user_sessions[event.sender_id]:
        client = user_sessions[event.sender_id]["client"]
        await event.reply("📈 **سيتم تجميع النقاط من بوت المليار**")
        bot_username = '@EEObot'
        await join_channels(bot_username, event, client)
    else:
        await event.reply("الرجاء تسجيل الجلسة أولاً باستخدام زر تسجيل جلسة.")

@bot.on(events.CallbackQuery(data=b'points_milyon'))
async def points_milyon(event):
    if event.sender_id in user_sessions and "client" in user_sessions[event.sender_id]:
        client = user_sessions[event.sender_id]["client"]
        await event.reply("🏆 **سيتم تجميع النقاط من بوت المليون**")
        bot_username = '@qweqwe1919bot'
        await join_channels(bot_username, event, client)
    else:
        await event.reply("الرجاء تسجيل الجلسة أولاً باستخدام زر تسجيل جلسة.")

@bot.on(events.CallbackQuery(data=b'points_3qab'))
async def points_3qab(event):
    if event.sender_id in user_sessions and "client" in user_sessions[event.sender_id]:
        client = user_sessions[event.sender_id]["client"]
        await event.reply("🔥 **سيتم تجميع النقاط من بوت العقاب**")
        bot_username = '@MARKTEBOT'
        await join_channels(bot_username, event, client)
    else:
        await event.reply("الرجاء تسجيل الجلسة أولاً باستخدام زر تسجيل جلسة.")

@bot.on(events.CallbackQuery(data=b'back_to_main'))
async def back_to_main(event):
    await handle_con_command(event)

@bot.on(events.CallbackQuery(data=b'login'))
async def login(event):
    await event.respond("الرجاء إرسال رقم الهاتف مع كود الدولة:")
    user_sessions[event.sender_id] = {"step": "phone"}

@bot.on(events.CallbackQuery(data=b'delete_session'))
async def delete_session(event):
    await event.respond("الرجاء إرسال كود الجلسة (StringSession) التي ترغب في حذفها:")
    user_sessions[event.sender_id] = {"step": "delete_session_code"}

@bot.on(events.CallbackQuery(data=b'stop_collecting'))
async def stop_collecting(event):
    collecting[event.sender_id] = False
    await event.reply("تم إيقاف التجميع ⛔")

@bot.on(events.CallbackQuery(data=b'get_storage'))
async def get_storage(event):
    file_name = save_sessions_to_file()
    await event.reply("تم حفظ الجلسات. إليك الملف:", file=file_name)

@bot.on(events.CallbackQuery(data=b'upload_storage'))
async def upload_storage(event):
    await event.respond("الرجاء إرسال ملف التخزين:")
    user_sessions[event.sender_id] = {"step": "upload_storage"}

@bot.on(events.NewMessage)
async def handle_new_message(event):
    if event.sender_id in user_sessions:
        step = user_sessions[event.sender_id]["step"]
        client = user_sessions[event.sender_id].get("client")
        try:
            if step == "phone":
                phone = event.message.message
                client = TelegramClient(StringSession(), api_id, api_hash, app_version="Robin")
                user_sessions[event.sender_id].update({"client": client, "phone": phone})
                await client.connect()
                await client.send_code_request(phone)
                await event.reply("الرجاء إرسال كود الدخول بشكل مسافات (مثال: 1 2 3 4 5):")
                user_sessions[event.sender_id]["step"] = "code"
            elif step == "code":
                code = event.message.message.replace(" ", "")
                phone = user_sessions[event.sender_id]["phone"]
                await client.sign_in(phone, code)
                await event.reply(
                    "تم تسجيل الدخول بنجاح!",
                    buttons=[Button.inline('تسجيل رقم آخر 🔄', b'login')]
                )
                user_sessions[event.sender_id]["step"] = None
            elif step == "password":
                password = event.message.message
                if password.lower() != 'لا':
                    await client.sign_in(password=password)
                await event.reply(
                    "تم تسجيل الدخول بنجاح!",
                    buttons=[Button.inline('تسجيل رقم آخر 🔄', b'login')]
                )
                session_str = client.session.save()  # حفظ جلسة المستخدم
                user_sessions[event.sender_id]["session_name"] = session_str
                user_sessions[event.sender_id]["step"] = None
            elif step == "session_code":
                session_code = event.message.message
                client = TelegramClient(StringSession(session_code), api_id, api_hash)
                await client.connect()
                await event.reply(
                    "تم تسجيل الجلسة بنجاح!",
                    buttons=[Button.inline('تسجيل جلسة أخرى 🔄', b'add_session')]
                )
                user_sessions[event.sender_id]["client"] = client
                user_sessions[event.sender_id]["session_code"] = session_code
                user_sessions[event.sender_id]["step"] = None
                save_sessions_to_file()  # حفظ الجلسات في الملف
            elif step == "delete_session_code":
                session_code = event.message.message
                found = False
                for user_id, session in user_sessions.items():
                    if session.get("session_code") == session_code:
                        del user_sessions[user_id]
                        found = True
                        break
                if found:
                    await event.reply("تم حذف الجلسة بنجاح!")
                else:
                    await event.reply("لم يتم العثور على الجلسة.")
                del user_sessions[event.sender_id]
            elif step == "upload_storage":
                if event.file:
                    file_path = await event.download_media()
                    with open(file_path, 'r') as f:
                        sessions = f.readlines()
                    count = 0
                    for session_code in sessions:
                        session_code = session_code.strip()
                        if session_code and session_code not in user_sessions:
                            client = TelegramClient(StringSession(session_code), api_id, api_hash)
                            await client.connect()
                            user_sessions[session_code] = {"client": client, "session_code": session_code}
                            count += 1
                    await event.reply(f"تم إضافة {count} رقم إلى البوت")
                    os.remove(file_path)
                del user_sessions[event.sender_id]
        except Exception as e:
            await send_error_message(client, error_chat_id, str(e))
            await event.reply(f"حدث خطأ: {str(e)}")
            del user_sessions[event.sender_id]
    else:
        # التحقق من الرسائل التي تحتوي على روابط قنوات الاشتراك
        links = re.findall(r'https://t\.me/[^\s]+', event.message.message)
        if links:
            client = user_sessions[event.sender_id]["client"]
            for link in links:
                try:
                    if 'joinchat' in link or '+' in link:
                        invite_code = link.split('/')[-1]
                        await client(ImportChatInviteRequest(invite_code))
                    else:
                        await client(JoinChannelRequest(link))
                    await asyncio.sleep(2)
                except Exception as e:
                    await send_error_message(client, error_chat_id, str(e))
                    await event.reply(f"حدث خطأ أثناء الانضمام إلى القناة: {str(e)}")