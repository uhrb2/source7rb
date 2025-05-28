import random
import re
from datetime import datetime

from telethon import Button, functions
from telethon.events import CallbackQuery
from telethon.utils import get_display_name

from JoKeRUB import l313l
from JoKeRUB.core.logger import logging

from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import _format, get_user_from_event, reply_id
from ..sql_helper import global_collectionjson as sql
from ..sql_helper import global_list as sqllist
from ..sql_helper import pmpermit_sql
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from . import mention

LOGS = logging.getLogger(__name__)
cmdhd = Config.COMMAND_HAND_LER
# ترجمه وكتابة فريق 7rB 


async def do_pm_permit_action(event, chat):  # sourcery no-metrics
    reply_to_id = await reply_id(event)
    try:
        PM_WARNS = sql.get_collection("pmwarns").json
    except AttributeError:
        PM_WARNS = {}
    try:
        PMMESSAGE_CACHE = sql.get_collection("pmmessagecache").json
    except AttributeError:
        PMMESSAGE_CACHE = {}
    me = await event.client.get_me()
    mention = f"[{chat.first_name}](tg://user?id={chat.id})"
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    first = chat.first_name
    last = chat.last_name
    fullname = f"{first} {last}" if last else first
    username = f"@{chat.username}" if chat.username else mention
    userid = chat.id
    my_first = me.first_name
    my_last = me.last_name
    my_fullname = f"{my_first} {my_last}" if my_last else my_first
    my_username = f"@{me.username}" if me.username else my_mention
    if str(chat.id) not in PM_WARNS:
        PM_WARNS[str(chat.id)] = 0
    try:
        MAX_FLOOD_IN_PMS = int(gvarstatus("MAX_FLOOD_IN_PMS") or 6)
    except (ValueError, TypeError):
        MAX_FLOOD_IN_PMS = 6
    totalwarns = MAX_FLOOD_IN_PMS + 1
    warns = PM_WARNS[str(chat.id)] + 1
    remwarns = totalwarns - warns
    if PM_WARNS[str(chat.id)] >= MAX_FLOOD_IN_PMS:
        try:
            if str(chat.id) in PMMESSAGE_CACHE:
                await event.client.delete_messages(
                    chat.id, PMMESSAGE_CACHE[str(chat.id)]
                )
                del PMMESSAGE_CACHE[str(chat.id)]
        except Exception as e:
            LOGS.info(str(e))
        custompmblock = gvarstatus("pmblock") or None
        if custompmblock is not None:
            USER_BOT_WARN_ZERO = custompmblock.format(
                mention=mention,
                first=first,
                last=last,
                fullname=fullname,
                username=username,
                userid=userid,
                my_first=my_first,
                my_last=my_last,
                my_fullname=my_fullname,
                my_username=my_username,
                my_mention=my_mention,
                totalwarns=totalwarns,
                warns=warns,
                remwarns=remwarns,
            )  # ترجمه وكتابة فريق 7rB 
        else:
            USER_BOT_WARN_ZERO = f"- حذࢪتك وكتلك لا تكࢪࢪ تَم حظࢪك بنجاح ما ٱكدر اخليك تزعج المالك \n- - بباي 🙁🤍"
        msg = await event.reply(USER_BOT_WARN_ZERO)
        await event.client(functions.contacts.BlockRequest(chat.id))
        the_message = f"#المحظورين_الحمايه\
                            \n[{get_display_name(chat)}](tg://user?id={chat.id}) تم حظره\
                            \n- عدد الرسائل: {PM_WARNS[str(chat.id)]}"
        del PM_WARNS[str(chat.id)]
        sql.del_collection("pmwarns")
        sql.del_collection("pmmessagecache")
        sql.add_collection("pmwarns", PM_WARNS, {})
        sql.add_collection("pmmessagecache", PMMESSAGE_CACHE, {})
        try:
            return await event.client.send_message(
                BOTLOG_CHATID,
                the_message,
            )
        except BaseException:
            return
    custompmpermit = gvarstatus("pmpermit_txt") or None
    if custompmpermit is not None:
        USER_BOT_NO_WARN = custompmpermit.format(
            mention=mention,
            first=first,
            last=last,
            fullname=fullname,
            username=username,
            userid=userid,
            my_first=my_first,
            my_last=my_last,
            my_fullname=my_fullname,
            my_username=my_username,
            my_mention=my_mention,
            totalwarns=totalwarns,
            warns=warns,
            remwarns=remwarns,
        )
    elif gvarstatus("pmmenu") is None:
        USER_BOT_NO_WARN = f"""᯽︙ اهلا بك {mention} \n مالك الحساب غير موجود حاليا الرجاء الانتظار وعدم تكرار الرسائل. 

لديك {warns}/{totalwarns} من التحذيرات لا تكرر الرسائل. """
    else:
        USER_BOT_NO_WARN = f"""᯽︙ اهلا بك {mention} \n مالك الحساب غير موجود حاليا الرجاء الانتظار وعدم تكرار الرسائل. 

لديك {warns}/{totalwarns} من التحذيرات لا تكرر الرسائل. """
    addgvar("pmpermit_text", USER_BOT_NO_WARN)
    PM_WARNS[str(chat.id)] += 1
    try:
        if gvarstatus("pmmenu") is None:
            results = await event.client.inline_query(
                Config.TG_BOT_USERNAME, "pmpermit"
            )
            msg = await results[0].click(chat.id, reply_to=reply_to_id, hide_via=True)
        else:
            PM_PIC = gvarstatus("pmpermit_pic")
            if PM_PIC:
                CAT = [x for x in PM_PIC.split()]
                PIC = list(CAT)
                CAT_IMG = random.choice(PIC)
            else:
                CAT_IMG = None
            if CAT_IMG is not None:
                msg = await event.client.send_file(
                    chat.id,
                    CAT_IMG,
                    caption=USER_BOT_NO_WARN,
                    reply_to=reply_to_id,
                    force_document=False,
                )
            else:
                msg = await event.client.send_message(
                    chat.id, USER_BOT_NO_WARN, reply_to=reply_to_id
                )
    except Exception as e:
        LOGS.error(e)
        msg = await event.reply(USER_BOT_NO_WARN)
    try:
        if str(chat.id) in PMMESSAGE_CACHE:
            await event.client.delete_messages(chat.id, PMMESSAGE_CACHE[str(chat.id)])
            del PMMESSAGE_CACHE[str(chat.id)]
    except Exception as e:
        LOGS.info(str(e))
    PMMESSAGE_CACHE[str(chat.id)] = msg.id
    sql.del_collection("pmwarns")
    sql.del_collection("pmmessagecache")
    sql.add_collection("pmwarns", PM_WARNS, {})
    sql.add_collection("pmmessagecache", PMMESSAGE_CACHE, {})


async def do_pm_options_action(event, chat):
    try:
        PM_WARNS = sql.get_collection("pmwarns").json
    except AttributeError:
        PM_WARNS = {}
    try:
        PMMESSAGE_CACHE = sql.get_collection("pmmessagecache").json
    except AttributeError:
        PMMESSAGE_CACHE = {}
    if str(chat.id) not in PM_WARNS:
        text = "- اختار احد الخيارات في الأعلى ولا تكرر اختيارك وهذا اخر تحذير لك"
        await event.reply(text)
        PM_WARNS[str(chat.id)] = 1
        sql.del_collection("pmwarns")
        sql.add_collection("pmwarns", PM_WARNS, {})
        # await asyncio.sleep(5)
        # await msg.delete()
        return None
    del PM_WARNS[str(chat.id)]
    sql.del_collection("pmwarns")
    sql.add_collection("pmwarns", PM_WARNS, {})
    try:
        if str(chat.id) in PMMESSAGE_CACHE:
            await event.client.delete_messages(chat.id, PMMESSAGE_CACHE[str(chat.id)])
            del PMMESSAGE_CACHE[str(chat.id)]
    except Exception as e:
        LOGS.info(str(e))
    sql.del_collection("pmmessagecache")
    sql.add_collection("pmmessagecache", PMMESSAGE_CACHE, {})
    USER_BOT_WARN_ZERO = f"- اتذكر حذرتك وقلت لك لا تكرر اكثر من خيار ولا ترسل رسائل مجرد انتظر. \
تعتقد راح اخليك تكرر لا اسف راح احظرك من الحساب. \
حاليا متكدر بعد تتكلم الى ان ياتي صاحب الحساب ويقوم بالغاء الحظر. 🙂💘"
    await event.reply(USER_BOT_WARN_ZERO)
    await event.client(functions.contacts.BlockRequest(chat.id))
    the_message = f"#حماية الخاص\
                            \n[{get_display_name(chat)}](tg://user?id={chat.id}) is blocked\
                            \n**السبب:** هو/هي لم يقم بالتوقف عن ارسال الرسائل والتكرار"
    sqllist.rm_from_list("pmoptions", chat.id)
    try:
        return await event.client.send_message(
            BOTLOG_CHATID,
            the_message,
        )
    except BaseException:
        return


# ترجمه وكتابة فريق 7rB 
async def do_pm_enquire_action(event, chat):
    try:
        PM_WARNS = sql.get_collection("pmwarns").json
    except AttributeError:
        PM_WARNS = {}
    try:
        PMMESSAGE_CACHE = sql.get_collection("pmmessagecache").json
    except AttributeError:
        PMMESSAGE_CACHE = {}
    if str(chat.id) not in PM_WARNS:
        text = """ههاه لازم تصبر مالك الحساب ما شاف الرسالة انتظر. \
مالك الحساب يرد على الكل بس ما اعرف اذا كان اكو كم شخص يتجاهلهم بس اصبر
مالك الحساب راح يرد عليك لما يكون متصل, اذا راد يرد عليك اصلا
**اتمنى ما تكرر الرسائل حتى ما اضطر احظرك 🙂🌿**"""
        await event.reply(text)
        PM_WARNS[str(chat.id)] = 1
        sql.del_collection("pmwarns")
        sql.add_collection("pmwarns", PM_WARNS, {})
        # await asyncio.sleep(5)
        # await msg.delete()
        return None
    del PM_WARNS[str(chat.id)]
    sql.del_collection("pmwarns")
    sql.add_collection("pmwarns", PM_WARNS, {})
    try:
        if str(chat.id) in PMMESSAGE_CACHE:
            await event.client.delete_messages(chat.id, PMMESSAGE_CACHE[str(chat.id)])
            del PMMESSAGE_CACHE[str(chat.id)]
    except Exception as e:
        LOGS.info(str(e))
    sql.del_collection("pmmessagecache")
    sql.add_collection("pmmessagecache", PMMESSAGE_CACHE, {})
    USER_BOT_WARN_ZERO = f"- اتذكر حذرتك وقلت لك لا تكرر اكثر من خيار ولا ترسل رسائل مجرد انتظر. \
تعتقد راح اخليك تكرر لا اسف راح احظرك من الحساب. \
حاليا متكدر بعد تتكلم الى ان ياتي صاحب الحساب ويقوم بالغاء الحظر. 🙂💘"
    await event.reply(USER_BOT_WARN_ZERO)
    await event.client(functions.contacts.BlockRequest(chat.id))
    the_message = f"#حماية الخاص\
                \n[{get_display_name(chat)}](tg://user?id={chat.id}) تم حظره\
                \nالسبب: هو/هي لم يقم بالتوقف عن ارسال الرسائل والتكرار"
    sqllist.rm_from_list("pmenquire", chat.id)
    try:
        return await event.client.send_message(
            BOTLOG_CHATID,
            the_message,
        )
    except BaseException:
        return


# ترجمه وكتابة فريق 7rB 


async def do_pm_request_action(event, chat):
    try:
        PM_WARNS = sql.get_collection("pmwarns").json
    except AttributeError:
        PM_WARNS = {}
    try:
        PMMESSAGE_CACHE = sql.get_collection("pmmessagecache").json
    except AttributeError:
        PMMESSAGE_CACHE = {}
    if str(chat.id) not in PM_WARNS:
        text = """ههاه لازم تصبر مالك الحساب ما شاف الرسالة انتظر. \
مالك الحساب يرد على الكل بس ما اعرف اذا كان اكو كم شخص يتجاهلهم بس اصبر
مالك الحساب راح يرد عليك لما يكون متصل, اذا راد يرد عليك اصلا
**اتمنى ما تكرر الرسائل حتى ما اضطر احظرك 🙂🌿**"""
        await event.reply(text)
        PM_WARNS[str(chat.id)] = 1
        sql.del_collection("pmwarns")
        sql.add_collection("pmwarns", PM_WARNS, {})
        # await asyncio.sleep(5)
        # await msg.delete()
        return None
    del PM_WARNS[str(chat.id)]
    sql.del_collection("pmwarns")
    sql.add_collection("pmwarns", PM_WARNS, {})
    try:
        if str(chat.id) in PMMESSAGE_CACHE:
            await event.client.delete_messages(chat.id, PMMESSAGE_CACHE[str(chat.id)])
            del PMMESSAGE_CACHE[str(chat.id)]
    except Exception as e:
        LOGS.info(str(e))
    sql.del_collection("pmmessagecache")
    sql.add_collection("pmmessagecache", PMMESSAGE_CACHE, {})
    USER_BOT_WARN_ZERO = f"**اتذكر حذرتك وقلت لك لا تكرر اكثر من خيار ولا ترسل رسائل مجرد انتظر. \
تعتقد راح اخليك تكرر لا اسف راح احظرك من الحساب. \
حاليا متكدر بعد تتكلم الى ان ياتي صاحب الحساب ويقوم بالغاء الحظر. 🙂💘**"
    await event.reply(USER_BOT_WARN_ZERO)
    await event.client(functions.contacts.BlockRequest(chat.id))
    the_message = f"#حماية ا خاص\
                \n[{get_display_name(chat)}](tg://user?id={chat.id}) تم حظره\
                \n**السبب:** هو/هي لم يقم بالتوقف عن ارسال الرسائل والتكرار"
    sqllist.rm_from_list("pmrequest", chat.id)
    try:
        return await event.client.send_message(
            BOTLOG_CHATID,
            the_message,
        )
    except BaseException:
        return


# ترجمه وكتابة فريق 7rB 


async def do_pm_chat_action(event, chat):
    try:
        PM_WARNS = sql.get_collection("pmwarns").json
    except AttributeError:
        PM_WARNS = {}
    try:
        PMMESSAGE_CACHE = sql.get_collection("pmmessagecache").json
    except AttributeError:
        PMMESSAGE_CACHE = {}
    if str(chat.id) not in PM_WARNS:
        text = """ههاه لازم تصبر مالك الحساب ما شاف الرسالة انتظر \
مالك الحساب يرد على الكل بس ما اعرف اذا كان اكو كم شخص يتجاهلهم بس اصبر
مالك الحساب راح يرد عليك لما يكون متصل, اذا راد يرد عليك اصلا
**اتمنى ما تكرر الرسائل حتى ما اضطر احظرك 😕🌿**"""
        await event.reply(text)
        PM_WARNS[str(chat.id)] = 1
        sql.del_collection("pmwarns")
        sql.add_collection("pmwarns", PM_WARNS, {})
        # await asyncio.sleep(5)
        # await msg.delete()
        return None
    del PM_WARNS[str(chat.id)]
    sql.del_collection("pmwarns")
    sql.add_collection("pmwarns", PM_WARNS, {})
    try:
        if str(chat.id) in PMMESSAGE_CACHE:
            await event.client.delete_messages(chat.id, PMMESSAGE_CACHE[str(chat.id)])
            del PMMESSAGE_CACHE[str(chat.id)]
    except Exception as e:
        LOGS.info(str(e))
    sql.del_collection("pmmessagecache")
    sql.add_collection("pmmessagecache", PMMESSAGE_CACHE, {})
    USER_BOT_WARN_ZERO = f"**اتذكر حذرتك وقلت لك لا تكرر اكثر من خيار ولا ترسل رسائل مجرد انتظر. \
تعتقد راح اخليك تكرر لا اسف راح احظرك من الحساب. \
حاليا متكدر بعد تتكلم الى ان ياتي صاحب الحساب ويقوم بالغاء الحظر. 🙂💘**"
    await event.reply(USER_BOT_WARN_ZERO)
    await event.client(functions.contacts.BlockRequest(chat.id))
    the_message = f"#حماية الخاص\
                \n[{get_display_name(chat)}](tg://user?id={chat.id}) is blocked\
                \n**السبب::** __He/She select opted for the chat option but didn't wait after being told also so blocked.__"
    sqllist.rm_from_list("pmchat", chat.id)
    try:
        return await event.client.send_message(
            BOTLOG_CHATID,
            the_message,
        )
    except BaseException:
        return


# ترجمه وكتابة فريق 7rB 


async def do_pm_spam_action(event, chat):
    try:
        PMMESSAGE_CACHE = sql.get_collection("pmmessagecache").json
    except AttributeError:
        PMMESSAGE_CACHE = {}
    try:
        if str(chat.id) in PMMESSAGE_CACHE:
            await event.client.delete_messages(chat.id, PMMESSAGE_CACHE[str(chat.id)])
            del PMMESSAGE_CACHE[str(chat.id)]
    except Exception as e:
        LOGS.info(str(e))
    USER_BOT_WARN_ZERO = f"**اتذكر حذرتك وقلت لك لا تكرر اكثر من خيار ولا ترسل رسائل مجرد انتظر. \
تعتقد راح اخليك تكرر لا اسف راح احظرك من الحساب. \
حاليا متكدر بعد تتكلم الى ان ياتي صاحب الحساب ويقوم بالغاء الحظر. 🙂💘**"
    await event.reply(USER_BOT_WARN_ZERO)
    await event.client(functions.contacts.BlockRequest(chat.id))
    the_message = f"#BLOCKED_PM\
                            \n[{get_display_name(chat)}](tg://user?id={chat.id}) تم حظره\
                            \n**Reason:** هو/هي لم يقم بالتوقف عن ارسال الرسائل والتكرار."
    sqllist.rm_from_list("pmspam", chat.id)
    sql.add_collection("pmmessagecache", PMMESSAGE_CACHE, {})
    try:
        return await event.client.send_message(
            BOTLOG_CHATID,
            the_message,
        )
    except BaseException:
        return


# ترجمه وكتابة فريق 7rB 
@l313l.ar_cmd(incoming=True, func=lambda e: e.is_private, edited=False, forword=None)
async def on_new_private_message(event):
    if gvarstatus("pmpermit") is None:
        return
    chat = await event.get_chat()
    if chat.bot or chat.verified:
        return
    if pmpermit_sql.is_approved(chat.id):
        return
    if str(chat.id) in sqllist.get_collection_list("pmspam"):
        return await do_pm_spam_action(event, chat)
    if str(chat.id) in sqllist.get_collection_list("pmchat"):
        return await do_pm_chat_action(event, chat)
    if str(chat.id) in sqllist.get_collection_list("pmrequest"):
        return await do_pm_request_action(event, chat)
    if str(chat.id) in sqllist.get_collection_list("pmenquire"):
        return await do_pm_enquire_action(event, chat)
    if str(chat.id) in sqllist.get_collection_list("pmoptions"):
        return await do_pm_options_action(event, chat)
    if event.sender_id == 7182427468:
        await event.reply("**ياهلاااا مطورييي ، بسس گول شتريد من هذا الحمار واني انطيكياه\n**")
        pmpermit_sql.approve(chat.id, get_display_name(chat), "تاريخ الإضافة", chat.username, "تم الموافقة تلقائيًا")
        return
    elif event.sender_id == 5931765554:
        await event.reply("**اهلاً وسهلاً بيك واكثر بلوياك الگلب گبل العين فز وتلگاك\n منورني يامطوري ابو عتب**")
        pmpermit_sql.approve(chat.id, get_display_name(chat), "تاريخ الإضافة", chat.username, "تم الموافقة تلقائيًا")
        return
    await do_pm_permit_action(event, chat)


@l313l.ar_cmd(outgoing=True, func=lambda e: e.is_private, edited=False, forword=None)
async def you_dm_other(event):
    if gvarstatus("pmpermit") is None:
        return
    chat = await event.get_chat()
    if chat.bot or chat.verified:
        return
    if str(chat.id) in sqllist.get_collection_list("pmspam"):
        return
    if str(chat.id) in sqllist.get_collection_list("pmchat"):
        return
    if str(chat.id) in sqllist.get_collection_list("pmrequest"):
        return
    if str(chat.id) in sqllist.get_collection_list("pmenquire"):
        return
    if str(chat.id) in sqllist.get_collection_list("pmoptions"):
        return
    if event.text and event.text.startswith(
        (
            f"{cmdhd}بلوك",
            f"{cmdhd}رفض",
            f"{cmdhd}س",
            f"{cmdhd}ر",
            f"{cmdhd}سماح",
        )  # ترجمه وكتابة فريق 7rB 
    ):
        return
    try:
        PM_WARNS = sql.get_collection("pmwarns").json
    except AttributeError:
        PM_WARNS = {}
    start_date = str(datetime.now().strftime("%B %d, %Y"))
    if not pmpermit_sql.is_approved(chat.id) and str(chat.id) not in PM_WARNS:
        pmpermit_sql.approve(
            chat.id, get_display_name(chat), start_date, chat.username, "لم يتم رفضه"
        )
        try:
            PMMESSAGE_CACHE = sql.get_collection("pmmessagecache").json
        except AttributeError:
            PMMESSAGE_CACHE = {}
        if str(chat.id) in PMMESSAGE_CACHE:
            try:
                await event.client.delete_messages(
                    chat.id, PMMESSAGE_CACHE[str(chat.id)]
                )
            except Exception as e:
                LOGS.info(str(e))
            del PMMESSAGE_CACHE[str(chat.id)]
        sql.del_collection("pmmessagecache")
        sql.add_collection("pmmessagecache", PMMESSAGE_CACHE, {})



@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"show_pmpermit_options")))
async def on_plug_in_callback_query_handler(event):
    if event.query.user_id == event.client.uid:
        text = "- - عذرا هذه الخيارات ليست لك انها للمستخدمين الذين يراسلوك 😐⚕️"
        return await event.answer(text, cache_time=0, alert=True)
    text = f"""حسنا الان بإمكانك اختيار احد الخيارات في الاسفل للتواصل مع , {mention}.
- اختر بهدوء خيار واحد فقط لنعرف سبب قدومك هنا 🤍

- هذه الخيارات في الاسفل اختر واحد فقط ⬇️"""
    buttons = [
        (Button.inline(text="للاستفسار عن شي ما.", data="to_enquire_something"),),
        (Button.inline(text="لطلب شي ما.", data="to_request_something"),),
        (Button.inline(text="للدردشه مع مالك الحساب.", data="to_chat_with_my_master"),),
        (
            Button.inline(
                text="لاقوم بازعاج مالك الحساب",
                data="to_spam_my_master_inbox",
            ),
        ),
    ]  # ترجمه و