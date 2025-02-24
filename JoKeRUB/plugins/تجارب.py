import json, os, sys, re
import asyncio
from telethon import TelegramClient, events, Button
from telethon.sessions import StringSession

API_ID = 24347380 
API_HASH = "1ad5dea4dfdddfed44df611dcd0d1736"
BOT_TOKEN = "7579264023:AAEia_w_rfEiadOSBdOmH4ohT0KhnXCiExI"
DB_FILE = "users.json" 

ADMIN_USERNAME = "@F_O_1"
def load_data(file_path):
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_data(file_path, data):
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)
users = load_data(DB_FILE)
bot = TelegramClient("bot", API_ID, API_HASH).start(bot_token=BOT_TOKEN)

@bot.on(events.NewMessage(pattern='تحديث'))
async def restart(event):
    if event.sender.username != ADMIN_USERNAME.strip('@'):
        return
    await event.reply("تم اعادة تشغيل البوت")
    os.execv(sys.executable, ['python3'] + sys.argv)

@bot.on(events.CallbackQuery(data=b'login'))
async def add_account(event):
    user_id = str(event.sender_id)
    if not users.get(user_id, {}).get('is_vip', False):
        return
    await event.edit("**⌔︙ قم بإرسال كود التيرمكس **")
    
    @bot.on(events.NewMessage(from_users=event.sender_id))
    async def receive_session(evt):
        if evt.sender_id != event.sender_id:
            return
        session_string = evt.text.strip()
        if not session_string:
            await evt.reply("**⌔︙ الرجاء ارسال كود تيرمكس صالح**")
            return
        try:
            temp_client = TelegramClient(StringSession(session_string), API_ID, API_HASH)
            await temp_client.connect()

            if not await temp_client.is_user_authorized():
                await evt.reply("**⌔︙ كود التيرمكس غير صالح الرجاء إرسال كود صالح**")
                await temp_client.disconnect()
                return
            buttons = [[Button.inline('اضف جلسة اخرى', b'login')]]
            if 'sessions' not in users.get(user_id, {}):
                users[user_id] = {'sessions': [], 'is_vip': True}
            if session_string not in users[user_id]['sessions']:
                users[user_id]['sessions'].append(session_string)
                save_data(DB_FILE, users)
                await evt.reply("**⌔︙ تم إضافة كود التيرمكس بنجاح أستمتع بالبوت 🤍**", buttons=buttons)
            else:
                await evt.reply("**⌔︙ هذا الكود مضاف مسبقًا**", buttons=buttons)

        except Exception as e:
            print(f"خطأ أثناء التحقق من الجلسة: {e}")
            await evt.reply("**⌔︙ كود التيرمكس غير صالح الرجاء إرسال كود صالح**")
        finally:
            bot.remove_event_handler(receive_session, events.NewMessage)


from telethon.tl.functions.channels import JoinChannelRequest

from telethon.tl.functions.channels import JoinChannelRequest

async def wait_for_response(client, user_id, timeout=30):
    future = asyncio.Future()

    async def response_handler(event):
        if event.sender_id == int(user_id):
            future.set_result(event)

    client.add_event_handler(response_handler, events.NewMessage)

    try:
        return await asyncio.wait_for(future, timeout=timeout)
    except asyncio.TimeoutError:
        return None
    finally:
        client.remove_event_handler(response_handler, events.NewMessage)


@bot.on(events.CallbackQuery(data=b'vote'))
async def vote(event):
    user_id = str(event.sender_id)
    if not users.get(user_id, {}).get('is_vip', False):
        return
    if 'sessions' not in users[user_id] or not users[user_id]['sessions']:
        await event.edit("**⌔︙ ماعندك حسابات ضايفهن استخدم زر اضف حساب**")
        return

    await event.edit("**⌔︙ ارسل رابط المنشور الذي يحتوي على تصويت\n عندك ٣٠ ثانية للأرسال استعجل**")
    post_link_event = await wait_for_response(bot, user_id, timeout=30)
    if not post_link_event:
        await event.respond("**⌔︙ انتهى الوقت، يرجى إعادة المحاولة**")
        return
    post_link = post_link_event.text.strip()

    await event.respond("**⌔︙ الان ارسل الايموجي الموجود في الزر \n عندك ٣٠ ثانية للأرسال استعجل**")
    emoji_event = await wait_for_response(bot, user_id, timeout=30)
    if not emoji_event:
        await event.respond("**⌔︙ انتهى الوقت، يرجى إعادة المحاولة**")
        return
    emoji = emoji_event.text.strip()

    try:
        parts = post_link.split("/")
        channel_username = parts[-2]
        message_id = int(parts[-1])

        await event.respond("**⌔︙ جاري تنفيذ التصويت لجميع الحسابات...**")

        for session_string in users[user_id]['sessions']:
            try:
                temp_client = TelegramClient(StringSession(session_string), API_ID, API_HASH)
                await temp_client.connect()

                try:
                    await temp_client(JoinChannelRequest(channel_username))
                except Exception:
                    pass
                message = await temp_client.get_messages(channel_username, ids=message_id)

                if message.buttons:
                    for row in message.buttons:
                        for button in row:
                            await button.click()

                await temp_client.disconnect()

                await asyncio.sleep(240)

            except Exception:
                pass

        await event.respond("**⌔︙ تم التصويت بنجاح  ✓ **")
    except Exception:
        await event.respond("**⌔︙ حدث خطأ**")
        
@bot.on(events.NewMessage(pattern="/start"))
async def start(event):
    user_id = str(event.sender_id)
    if user_id not in users or not users[user_id].get('is_vip', False):
        await event.reply(
            "**⌔︙ للأسف، أنت بحاجة للاشتراك من المطور للحصول على عضوية VIP**\n"
            "**⌔︙ اضغط على الزر أدناه للتواصل مع المطور**",
            buttons=[
                [Button.url("المطور", 'https://t.me/F_O_1')]
            ]
        )
        return
    if user_id not in users:
        users[user_id] = {'sessions': [], 'is_vip': True}
        save_data(DB_FILE, users)

    await event.reply(
        "**⌔︙ هلا بيك، اختر من الأزرار التالية:**",
        buttons=[
            [Button.inline("اضف حساب", b'login')],
            [Button.inline("تصويت", b'vote')],
        ]
    )

#------------------ اوامر الادمن👇🏻----------------#

@bot.on(events.CallbackQuery(data=b'enable_vip'))
async def enable_vip(event):
    if event.sender.username != ADMIN_USERNAME.strip('@'):
        return
    await event.edit("**⌔︙ ارسل يوزر المستخدم او الايدي حتى تفعل اله عضوية VIP**")
    user_id = str(event.sender_id)
    response = await wait_for_response(bot, user_id, timeout=60)

    if not response:
        await event.respond("**⌔︙ انتهى الوقت، لم يتم استلام أي استجابة**")
        return

    target = response.text.strip()
    if target.isdigit(): 
        user_id = target
    else: 
        try:
            user = await bot.get_entity(target)
            user_id = str(user.id)
        except Exception:
            await event.respond("**⌔︙ مالگيت هذا المستخدم تأكد من اليوزر او الايدي**")
            return

    if user_id not in users:
        await event.respond("**⌔︙ هذا المستخدم ليس مسجلاً في قاعدة البيانات**")
        return

    users[user_id]['is_vip'] = True
    save_data(DB_FILE, users)
    await event.respond(f"**⌔︙ تم تفعيل العضوية للمستخدم {target} بنجاح**")

@bot.on(events.CallbackQuery(data=b'disable_vip'))
async def disable_vip(event):
    if event.sender.username != ADMIN_USERNAME.strip('@'):
        return
    await event.edit("**⌔︙ارسل يوزر المستخدم او الايدي حتى تعطل اله عضوية VIP**")
    user_id = str(event.sender_id)
    response = await wait_for_response(bot, user_id, timeout=60)

    if not response:
        await event.respond("**⌔︙ انتهى الوقت، لم يتم استلام أي استجابة**")
        return

    target = response.text.strip()
    if target.isdigit(): 
        user_id = target
    else:
        try:
            user = await bot.get_entity(target)
            user_id = str(user.id)
        except Exception:
            await event.respond("**⌔︙ مالگيت هذا المستخدم تأكد من اليوزر او الايدي**")
            return

    if user_id not in users:
        await event.respond("**⌔︙ هذا المستخدم ليس مسجلاً في قاعدة البيانات**")
        return

    users[user_id]['is_vip'] = False
    save_data(DB_FILE, users)
    await event.respond(f"**⌔︙ تم تعطيل العضوية للمستخدم {target} بنجاح**")

@bot.on(events.NewMessage(pattern='/admin'))
async def admin(event):
    if event.sender.username != ADMIN_USERNAME.strip('@'):
        return
    await event.reply(
        "**⌔︙ حياك الله يالادمن هاي لوحة لتفعيل وتعطيل العضوية من المستخدمين**",
        buttons=[
            [Button.inline("تفعيل VIP", b'enable_vip')],
            [Button.inline("تعطيل VIP", b'disable_vip')]
        ]
    )

print("⌔︙ البوت يعمل الآن...")

bot.run_until_disconnected()