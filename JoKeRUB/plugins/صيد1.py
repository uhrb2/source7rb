import random
import requests
import asyncio
from asyncio import sleep
from telethon.sync import functions
from telethon.errors import FloodWaitError
from user_agent import generate_user_agent
from JoKeRUB import l313l
from ..core.managers import edit_or_reply

# قائمة الأحرف التي سيتم استخدامها
characters = 'abcdefghijklmnopqrstuvwxyz0123456789'

# دالة لإنشاء الأسماء الثلاثية والرباعية والخماسية
def generate_usernames(length):
    return [''.join(random.choices(characters, k=length)) for _ in range(1000)]

# دالة لفحص توافر الاسم
async def check_username_availability(client, username):
    try:
        result = await client(functions.contacts.ResolveUsernameRequest(username))
        return False  # إذا تم العثور على المستخدم
    except:
        return True  # إذا لم يتم العثور على المستخدم

# دالة لصيد الأسماء
async def catch_usernames(event, length):
    client = event.client
    available_usernames = []
    usernames = generate_usernames(length)

    for username in usernames:
        if await check_username_availability(client, username):
            available_usernames.append(username)
            if len(available_usernames) >= 10:  # توقف عن البحث بعد العثور على 10 أسماء متاحة
                break

    await edit_or_reply(event, f"Available usernames: {', '.join(available_usernames)}")

# دالة لصيد تجربة
async def catch_any_username(event):
    client = event.client
    available_usernames = []
    usernames = generate_usernames(3)  # توليد أسماء ثلاثية

    for username in usernames:
        if await check_username_availability(client, username):
            available_usernames.append(username)
            break

    if available_usernames:
        await edit_or_reply(event, f"Available username for testing: {available_usernames[0]}")
    else:
        await edit_or_reply(event, "No available usernames found for testing.")

# مثال على استخدام الدالة في حدث لصيد ثلاثي
@l313l.on(events.NewMessage(pattern="صيد ثلاثي"))
async def handler(event):
    await catch_usernames(event, 3)

# مثال على استخدام الدالة في حدث لصيد رباعي
@l313l.on(events.NewMessage(pattern="صيد رباعي"))
async def handler(event):
    await catch_usernames(event, 4)

# مثال على استخدام الدالة في حدث لصيد خماسي
@l313l.on(events.NewMessage(pattern="صيد خماسي"))
async def handler(event):
    await catch_usernames(event, 5)

# مثال على استخدام الدالة في حدث لصيد تجربة
@l313l.on(events.NewMessage(pattern="صيد تجربة"))
async def handler(event):
    await catch_any_username(event)