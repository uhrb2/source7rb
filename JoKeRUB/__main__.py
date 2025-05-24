import sys
import contextlib
import JoKeRUB
from JoKeRUB import BOTLOG_CHATID, HEROKU_APP, PM_LOGGER_GROUP_ID
from .Config import Config
from .core.logger import logging
from .core.session import l313l
from .utils import (
    add_bot_to_logger_group,
    install_externalrepo,
    load_plugins,
    setup_bot,
    mybot,
    startupmessage,
    verifyLoggerGroup,
    saves,
)
from colorama import init, Fore, Style
from pyfiglet import Figlet
import asyncio

init(autoreset=True)

LOGS = logging.getLogger("JoKeRUB")

# طباعة اسم - 7rB . بشكل كبير جداً ومميز باللون الأزرق
f = Figlet(font='big')  # يمكنك تجربة خطوط أخرى مثل 'slant'، 'block' إلخ
big_text = f.renderText('- 7rB .')
print(Fore.BLUE + big_text + Style.RESET_ALL)

print(JoKeRUB.__copyright__)
print("Licensed under the terms of the " + JoKeRUB.__license__)
cmdhr = Config.COMMAND_HAND_LER

try:
    LOGS.info("جارِ بدء بوت 7rB  ✓")
    l313l.loop.run_until_complete(setup_bot())
    LOGS.info("تم اكتمال تنصيب البوت ✓")
except Exception as e:
    LOGS.error(f"{str(e)}")
    sys.exit()

try:
    LOGS.info("يتم تفعيل وضع الانلاين")
    l313l.loop.run_until_complete(mybot())
    LOGS.info("تم تفعيل وضع الانلاين بنجاح ✓")
except Exception as jep:
    LOGS.error(f"- {jep}")
    sys.exit()

async def startup_process():
    await verifyLoggerGroup()
    await load_plugins("plugins")
    await load_plugins("assistant")
    print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
    print("᯽︙بـوت 7rB  يعـمل بـنجاح ")
    print(
        f"تم تشغيل الانلاين تلقائياً ارسل {cmdhr}الاوامر لـرؤيـة اوامر السورس\
        \nللمسـاعدة تواصـل  https://t.me/k_jj_jSupport"
    )
    print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
    await verifyLoggerGroup()
    await saves()
    await add_bot_to_logger_group(BOTLOG_CHATID)
    if PM_LOGGER_GROUP_ID != -100:
        await add_bot_to_logger_group(PM_LOGGER_GROUP_ID)
    await startupmessage()
    return

async def externalrepo():
    if Config.VCMODE:
        await install_externalrepo("https://github.com/k_jj_jiq/JepVc", "jepvc", "k_jj_jvc")

l313l.loop.run_until_complete(externalrepo())
l313l.loop.run_until_complete(startup_process())

# إذا كان لديك جلسة aiohttp وتحتاج إغلاقها، استخدم الطريقة الآمنة التالية
if hasattr(l313l, 'session') and l313l.session is not None:
    close_coro = getattr(l313l.session, "close", None)
    if close_coro is not None and callable(close_coro):
        coro = l313l.session.close()
        if asyncio.iscoroutine(coro):
            l313l.loop.run_until_complete(coro)

if len(sys.argv) in {1, 3, 4}:
    with contextlib.suppress(ConnectionError):
        l313l.run_until_disconnected()
else:
    l313l.disconnect()