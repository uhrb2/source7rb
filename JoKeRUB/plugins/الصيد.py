import random
import string
import requests
import time
import asyncio
from asyncio import sleep
import telethon
from telethon.sync import functions
from telethon.errors import FloodWaitError
from user_agent import generate_user_agent
from user_agent import *
from queue import Queue
from threading import Thread

from JoKeRUB import l313l
from ..core.managers import edit_delete, edit_or_reply

srys = [0]
trys = [0]
crys = [0]
arys = [0]
brys = [0]
issclim = ["off"]
itsclim = ["off"]
iscuto = ["off"]
istuto = ["off"]
isbuto = ["off"]

"""
banned = []
with open("banned.txt", "r") as f:
    f = f.read().split()
    banned.append(f)
"""

que = Queue()

def check_user(username):
    url = "https://t.me/"+str(username)
    headers = {
        "User-Agent": generate_user_agent(),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}
    try:
        response = requests.get(url, headers=headers)
        if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"') >= 0:
            return "Available"
        else:
            return "Unavailable"
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return "Unavailable"
    except Exception as e:
        print (e)
        return "Unavailable"


def checker_user(username):
    url = "https://t.me/"+str(username)
    headers = {
        "User-Agent": generate_user_agent(),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}
    try:
        response = requests.get(url, headers=headers)
        if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"') >= 0:
            return "Available"
        else:
            return "Unavailable"
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return "Unavailable"
    except Exception as e:
        print (e)
        return "Unavailable"


#async def gen_user(choice):
def gen_user(choice):
    a = "qwertyuiopasdfghjklzxcvbnm"
    b = "1234567890"
    e = "qwertyuiopasdfghjklzxcvbnm1234567890"
    z = "sdfghjklzwerty1234567890uioxcvbqpanm"
    o = "0987654321"
    q = "5432109876"
    k = "mnbvcxzlkjhgfdsapoiuytrewq"
    if choice == "سداسي_حرفين1": #ARAAAR
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], c[0], c[0], c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)

    elif choice == "سداسي_رقمين1": #A8AAA8
        c = d = random.choices(a)
        d = random.choices(o)
        f = [c[0], d[0], c[0], c[0], c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)

    elif choice == "سداسي_شرطه": #AAAA_R ~ 
        c = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], c[0], c[0], "_", d[0]]
        username = "".join(f)

    elif choice == "سداسي_حرفين2": #AAAARR ~ 
        c = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], c[0], c[0], d[0], d[0]]
        username = "".join(f)

    elif choice == "سداسي_رقمين2": #AAAA88 ~ 
        c = random.choices(a)
        d = random.choices(o)
        f = [c[0], c[0], c[0], c[0], d[0], d[0]]
        username = "".join(f)

    elif choice == "سداسي_حرفين3": #AAARRA ~ 
        c = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], c[0], d[0], d[0], c[0]]
        username = "".join(f)

    elif choice == "سداسي_رقمين3": #AAA88A ~ 
        c = random.choices(a)
        d = random.choices(o)
        f = [c[0], c[0], c[0], d[0], d[0], c[0]]
        username = "".join(f)

    elif choice == "سداسي_حرفين4": #AARRAA ~ 
        c = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], d[0], d[0], c[0], c[0]]
        username = "".join(f)

    elif choice == "سداسي_رقمين4": #AA88AA ~ 
        c = random.choices(a)
        d = random.choices(o)
        f = [c[0], c[0], d[0], d[0], c[0], c[0]]
        username = "".join(f)

    elif choice == "سداسي_حرفين5": #ARRAAA ~ 
        c = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], d[0], c[0], c[0], c[0]]
        username = "".join(f)

    elif choice == "سداسي_حرفين6": #AARRRR ~ 
        c = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], d[0], d[0], d[0], d[0]]
        username = "".join(f)

    elif choice == "ثلاثي1": #A_R_D
        c = random.choices(a)
        d = random.choices(e)
        s = random.choices(z)
        f = [c[0], "_", d[0], "_", s[0]]
        username = "".join(f)

    elif choice == "ثلاثي2": #A_7_R ~ 
        c = random.choices(a)
        d = random.choices(o)
        s = random.choices(z)
        f = [c[0], "_", d[0], "_", s[0]]
        username = "".join(f)

    elif choice == "ثلاثي3": #A_7_0 ~ 
        c = random.choices(a)
        d = random.choices(b)
        s = random.choices(o)
        f = [c[0], "_", d[0], "_", s[0]]
        username = "".join(f)

    elif choice == "شبه رباعي1": #A_A_A_R ~ 
        c = random.choices(a)
        d = random.choices(z)
        f = [c[0], "_", c[0], "_", c[0], "_", d[0]]
        username = "".join(f)

    elif choice == "شبه رباعي2": #A_R_R_R ~ 
        c = random.choices(a)
        d = random.choices(z)
        f = [c[0], "_", d[0], "_", d[0], "_", d[0]]
        username = "".join(f)

    elif choice == "شبه رباعي3": #A_RR_A ~ 
        c = random.choices(a)
        d = random.choices(z)
        f = [c[0], "_", d[0], d[0], "_", c[0]]
        username = "".join(f)

    elif choice == "شبه رباعيa": #A_RR_A ~ 
        d = random.choices(z)
        f = ["a", "_", d[0], d[0], "_", "a"]
        username = "".join(f)

    elif choice == "شبه رباعيz": #Z_RR_Z ~ 
        d = random.choices(z)
        f = ["z", "_", d[0], d[0], "_", "z"]
        username = "".join(f)

    elif choice == "شبه رباعيr": #R_AA_R ~ 
        d = random.choices(z)
        f = ["r", "_", d[0], d[0], "_", "r"]
        username = "".join(f)

    elif choice == "شبه رباعيo": #O_RR_O ~ 
        d = random.choices(z)
        f = ["o", "_", d[0], d[0], "_", "o"]
        username = "".join(f)

    elif choice == "شبه رباعيi": #i_RR_i ~ 
        d = random.choices(z)
        f = ["i", "_", d[0], d[0], "_", "i"]
        username = "".join(f)

    elif choice == "شبه رباعيl": #l_RR_l ~ 
        d = random.choices(z)
        f = ["l", "_", d[0], d[0], "_", "l"]
        username = "".join(f)

    elif choice == "شبه رباعي4": #A_RR_R ~ 
        c = random.choices(a)
        d = random.choices(z)
        f = [c[0], "_", d[0], d[0], "_", d[0]]
        username = "".join(f)

    elif choice == "شبه رباعي5": #A_RR_R ~ 
        c = random.choices(a)
        d = random.choices(z)
        f = [c[0], d[0], d[0], "_", d[0]]
        username = "".join(f)

    elif choice == "شبه_رباعيi": # lk_kl | ik_ki ~ 
        g = "li"
        h = "sdfghjklzwerty1234567890uioxcvbqpanm"
        c = random.choices(g)
        d = random.choices(h)
        f = [c[0], d[0], "_", d[0], c[0]]
        username = "".join(f)

    elif choice == "شبه_رباعيu": # lu_ul ~ 
        c = random.choices(a)
        f = [c[0], "u", "_", "u", c[0]]
        username = "".join(f)

    elif choice == "شبه_رباعيn": # ln_nl ~ 
        c = random.choices(a)
        f = [c[0], "n", "_", "n", c[0]]
        username = "".join(f)

    elif choice == "شبه_رباعيe": # le_el ~ 
        c = random.choices(a)
        f = [c[0], "e", "_", "e", c[0]]
        username = "".join(f)

    elif choice == "شبه_رباعيo": # lo_ol ~ 
        c = random.choices(a)
        f = [c[0], "o", "_", "o", c[0]]
        username = "".join(f)

    elif choice == "شبه_رباعيv": # lv_vl ~ 
        c = random.choices(a)
        f = [c[0], "v", "_", "v", c[0]]
        username = "".join(f)

    elif choice == "رباعيات حرف": #AA_AR ~ 
        c = random.choices(a)
        d = random.choices(k)
        f = [c[0], c[0], "_", c[0], d[0]]
        username = "".join(f)

    elif choice == "رباعيات رقم": #AA_AR ~ 
        c = random.choices(a)
        d = random.choices(o)
        f = [c[0], c[0], "_", c[0], d[0]]
        username = "".join(f)

    elif choice == "رباعي1": #AAA_R ~ 
        c = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], c[0], "_", d[0]]
        username = "".join(f)

    elif choice == "رباعيa": #AAA_R ~ 
        c = random.choices(e)
        f = ["a", "a", "a", "_", c[0]]
        username = "".join(f)

    elif choice == "رباعيz": #ZZZ_R ~ 
        c = random.choices(e)
        f = ["z", "z", "z", "_", c[0]]
        username = "".join(f)

    elif choice == "رباعيr": #RRR_D ~ 
        c = random.choices(e)
        f = ["r", "r", "r", "_", c[0]]
        username = "".join(f)

    elif choice == "رباعي رقم1": #AAA_7 ~ 
        c = random.choices(a)
        d = random.choices(o)
        f = [c[0], c[0], c[0], "_", d[0]]
        username = "".join(f)

    elif choice == "رباعي2": #A_RRR ~ 
        c = random.choices(a)
        d = random.choices(z)
        f = [c[0], "_", d[0], d[0], d[0]]
        username = "".join(f)

    elif choice == "رباعي رقم2": #A_777 ~ 
        c = random.choices(a)
        d = random.choices(o)
        f = [c[0], "_", d[0], d[0], d[0]]
        username = "".join(f)

    elif choice == "رباعي3": #AA_RR ~ 
        c = random.choices(a)
        d = random.choices(z)
        f = [c[0], c[0], "_", d[0], d[0]]
        username = "".join(f)

    elif choice == "رباعي4": #AA_AR ~ 
        c = random.choices(a)
        d = random.choices(z)
        f = [c[0], c[0], "_", c[0], d[0]]
        username = "".join(f)

    elif choice == "رباعي5": #AA_RA ~ 
        c = random.choices(a)
        d = random.choices(z)
        f = [c[0], c[0], "_", d[0], c[0]]
        username = "".join(f)

    elif choice == "رباعي6": #AR_RA ~ 
        c = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], "_", d[0], c[0]]
        username = "".join(f)

    elif choice == "رباعي رقم6": #A7_7A ~ 
        c = random.choices(a)
        d = random.choices(o)
        f = [c[0], d[0], "_", d[0], c[0]]
        username = "".join(f)

    elif choice == "رباعي7": #AR_AR ~ 
        c = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], "_", c[0], d[0]]
        username = "".join(f)

    elif choice == "رباعي رقم7": #A7_A7 ~ 
        c = random.choices(a)
        d = random.choices(o)
        f = [c[0], d[0], "_", c[0], d[0]]
        username = "".join(f)

    elif choice == "رباعي8": #AR_RR ~ 
        c = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], "_", d[0], d[0]]
        username = "".join(f)

    elif choice == "رباعي رقم8": #A7_77 ~ 
        c = random.choices(a)
        d = random.choices(o)
        f = [c[0], d[0], "_", d[0], d[0]]
        username = "".join(f)

    elif choice == "سداسيات1": #AAAAAR
        c = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], c[0], c[0], c[0], d[0]]
        username = "".join(f)

    elif choice == "سداسيات2": #AAAARA ~ 
        c = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], c[0], c[0], d[0], c[0]]
        username = "".join(f)

    elif choice == "سداسيات3": #AAARAA ~ 
        c = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], c[0], d[0], c[0], c[0]]
        username = "".join(f)

    elif choice == "سداسيات4": #AARAAA ~ 
        c = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], d[0], c[0], c[0], c[0]]
        username = "".join(f)

    if choice == "سداسيات5":  # ARAAAA ~ 
    c = random.choices(a)
    d = random.choices(e)
    f = [c[0], d[0], c[0], c[0], c[0], c[0]]
    username = "".join(f)

elif choice == "سداسيات6":  # ARRRRR ~ 
    c = random.choices(a)
    d = random.choices(e)
    f = [c[0], d[0], d[0], d[0], d[0], d[0]]
    username = "".join(f)

elif choice == "سداسيvip":  # VIP537 ~ 
    c = random.choices(b)
    d = random.choices(o)
    s = random.choices(q)
    f = ["v", "i", "p", c[0], d[0], s[0]]
    username = "".join(f)

elif choice == "سداسي_vip":  # VIP537 ~ 
    c = random.choices(b)
    d = random.choices(o)
    f = ["v", "i", "p", "_", c[0], d[0]]
    username = "".join(f)

elif choice == "بوتات1":  # AR_Bot ~ 
    c = random.choices(a)
    d = random.choices(z)
    f = [c[0], d[0], "_", "b", "o", "t"]
    username = "".join(f)

elif choice == "بوتات2":  # A_RBot ~ 
    c = random.choices(a)
    d = random.choices(z)
    f = [c[0], "_", d[0], "b", "o", "t"]
    username = "".join(f)

elif choice == "بوتات3":  # AR7Bot ~ 
    c = random.choices(a)
    d = random.choices(k)
    s = random.choices(b)
    f = [c[0], d[0], s[0], "b", "o", "t"]
    username = "".join(f)

elif choice == "بوتات4":  # A7RBot ~ 
    c = random.choices(a)
    d = random.choices(b)
    s = random.choices(k)
    f = [c[0], d[0], s[0], "b", "o", "t"]
    username = "".join(f)

elif choice == "بوتات5":  # A77Bot ~ 
    c = random.choices(a)
    d = random.choices(b)
    s = random.choices(o)
    f = [c[0], d[0], s[0], "b", "o", "t"]
    username = "".join(f)

elif choice == "بوتات6":  # ADRBot
    c = random.choices(a)
    d = random.choices(e)
    s = random.choices(z)
    f = [c[0], d[0], s[0], "b", "o", "t"]
    username = "".join(f)

elif choice == "بوتات7":  # (AARBot - AA8bot) ~ 
    c = random.choices(a)
    d = random.choices(z)
    f = [c[0], c[0], d[0], "b", "o", "t"]
    username = "".join(f)

elif choice == "بوتات8":  # AARBot ~ 
    c = random.choices(a)
    d = random.choices(k)
    f = [c[0], c[0], d[0], "b", "o", "t"]
    username = "".join(f)

elif choice == "بوتات9":  # AA8Bot ~ 
    c = random.choices(a)
    d = random.choices(o)
    f = [c[0], c[0], d[0], "b", "o", "t"]
    username = "".join(f)

elif choice == "خماسي حرفين1":  # AAARD ~ 
    c = random.choices(a)
    d = random.choices(z)
    s = random.choices(e)
    f = [c[0], c[0], c[0], s[0], d[0]]
    username = "".join(f)

elif choice == "خماسي ارقام":  # AR888 ~ 
    c = random.choices(a)
    d = random.choices(e)
    s = random.choices(b)
    f = [c[0], d[0], s[0], s[0], s[0]]
    username = "".join(f)

elif choice == "خماسي رقمين1":  # AAARD ~ 
    c = random.choices(a)
    d = random.choices(o)
    s = random.choices(b)
    f = [c[0], c[0], c[0], d[0], s[0]]
    username = "".join(f)

    elif choice == "خماسي حرفين2": #A7RRR ~ 
        c = random.choices(a)
        d = random.choices(b)
        s = random.choices(z)
        f = [c[0], d[0], s[0], s[0], s[0]]
        username = "".join(f)

    elif choice == "خماسي k": #A800k ~ 
        c = random.choices(a)
        d = random.choices(o)
        f = [c[0], d[0], "0", "0", "k"]
        username = "".join(f)

    elif choice == "خماسي حرفينa": #AAARD ~ 
        c = random.choices(z)
        d = random.choices(e)
        f = ["a", "a", "a", c[0], d[0]]
        username = "".join(f)

    elif choice == "خماسي حرفينr": #RRRAD ~ 
        c = random.choices(z)
        d = random.choices(e)
        f = ["r", "r", "r", c[0], d[0]]
        username = "".join(f)

    elif choice == "خماسي رقمينm": #MMM87 ~ 
        c = random.choices(b)
        d = random.choices(o)
        f = ["m", "m", "m", c[0], d[0]]
        username = "".join(f)

    elif choice == "خماسي حرفينn": #NNNAR ~ 
        c = random.choices(e)
        d = random.choices(z)
        f = ["n", "n", "n", c[0], d[0]]
        username = "".join(f)

    elif choice == "خماسي حرفينz": #ZZZAR ~ 
        c = random.choices(z)
        d = random.choices(e)
        f = ["z", "z", "z", c[0], d[0]]
        username = "".join(f)

    elif choice == "خماسي حرفين3": #ARRRD ~ 
        c = random.choices(a)
        d = random.choices(z)
        s = random.choices(e)
        f = [c[0], d[0], d[0], d[0], s[0]]
        username = "".join(f)

    elif choice == "خماسي حرفين33": #AAARR ~ 
        c = random.choices(a)
        d = random.choices(z)
        f = [c[0], c[0], c[0], d[0], d[0]]
        username = "".join(f)

    elif choice == "خماسي حرفين44": #ARRRA ~ 
        c = random.choices(a)
        d = random.choices(z)
        f = [c[0], d[0], d[0], d[0], c[0]]
        username = "".join(f)

    elif choice == "خماسي حرفين55": #AARRR ~ 
        c = random.choices(a)
        d = random.choices(z)
        f = [c[0], c[0], d[0], d[0], d[0]]
        username = "".join(f)

    elif choice == "خماسي حرفين66": #ARAAR
        c = random.choices(a)
        d = random.choices(z)
        f = [c[0], d[0], c[0], c[0], d[0]]
        username = "".join(f)

    elif choice == "سباعيات1": #AAAAAAR ~ 
        c = d = random.choices(a)
        d = random.choices(z)
        f = [c[0], c[0], c[0], c[0], c[0], c[0], d[0]]
        username = "".join(f)

    elif choice == "سباعيات2": #AAAAARA ~ 
        c = d = random.choices(a)
        d = random.choices(z)
        f = [c[0], c[0], c[0], c[0], c[0], d[0], c[0]]
        username = "".join(f)

    elif choice == "سباعيات3": #AAAARAA
        c = d = random.choices(a)
        d = random.choices(z)
        f = [c[0], c[0], c[0], c[0], d[0], c[0], c[0]]
        username = "".join(f)

    elif choice == "سباعيات4": #AAARAAA ~ 
        c = d = random.choices(a)
        d = random.choices(z)
        f = [c[0], c[0], c[0], d[0], c[0], c[0], c[0]]
        username = "".join(f)

    elif choice == "سباعيات5": #AARAAAA ~ 
        c = d = random.choices(a)
        d = random.choices(z)
        f = [c[0], c[0], d[0], c[0], c[0], c[0], c[0]]
        username = "".join(f)

    elif choice == "سباعيات6": #ARAAAAA ~ 
        c = d = random.choices(a)
        d = random.choices(z)
        f = [c[0], d[0], c[0], c[0], c[0], c[0], c[0]]
        username = "".join(f)

    elif choice == "سباعيات7": #ARRRRRR ~ 
        c = d = random.choices(a)
        d = random.choices(z)
        f = [c[0], d[0], d[0], d[0], d[0], d[0], d[0]]
        username = "".join(f)

    elif choice == "سباعيات حرف1": #AAAAAAR ~ 
        c = d = random.choices(a)
        d = random.choices(k)
        f = [c[0], c[0], c[0], c[0], c[0], c[0], d[0]]
        username = "".join(f)

    elif choice == "سباعيات رقم1": #AAAAAA8 ~ 
        c = d = random.choices(a)
        d = random.choices(o)
        f = [c[0], c[0], c[0], c[0], c[0], c[0], d[0]]
        username = "".join(f)

    elif choice == "سباعيات حرف2": #AAAAARA ~ 
        c = d = random.choices(a)
        d = random.choices(k)
        f = [c[0], c[0], c[0], c[0], c[0], d[0], c[0]]
        username = "".join(f)

    elif choice == "سباعيات رقم2": #AAAAA8A ~ 
        c = d = random.choices(a)
        d = random.choices(o)
        f = [c[0], c[0], c[0], c[0], c[0], d[0], c[0]]
        username = "".join(f)

    elif choice == "سباعيات حرف3": #AAAARAA
        c = d = random.choices(a)
        d = random.choices(k)
        f = [c[0], c[0], c[0], c[0], d[0], c[0], c[0]]
        username = "".join(f)

    elif choice == "سباعيات رقم3": #AAAA8AA
        c = d = random.choices(a)
        d = random.choices(o)
        f = [c[0], c[0], c[0], c[0], d[0], c[0], c[0]]
        username = "".join(f)

    elif choice == "سباعيات حرف4": #AAARAAA ~ 
        c = d = random.choices(a)
        d = random.choices(k)
        f = [c[0], c[0], c[0], d[0], c[0], c[0], c[0]]
        username = "".join(f)

    elif choice == "سباعيات رقم4": #AAA8AAA ~ 
        c = d = random.choices(a)
        d = random.choices(o)
        f = [c[0], c[0], c[0], d[0], c[0], c[0], c[0]]
        username = "".join(f)

    elif choice == "سباعيات حرف5": #AARAAAA ~ 
        c = d = random.choices(a)
        d = random.choices(k)
        f = [c[0], c[0], d[0], c[0], c[0], c[0], c[0]]
        username = "".join(f)

    elif choice == "سباعيات رقم5": #AA8AAAA ~ 
        c = d = random.choices(a)
        d = random.choices(o)
        f = [c[0], c[0], d[0], c[0], c[0], c[0], c[0]]
        username = "".join(f)

    elif choice == "سباعيات حرف6": #ARAAAAA ~ 
        c = d = random.choices(a)
        d = random.choices(k)
        f = [c[0], d[0], c[0], c[0], c[0], c[0], c[0]]
        username = "".join(f)

    elif choice == "سباعيات رقم6": #A8AAAAA ~ 
        c = d = random.choices(a)
        d = random.choices(o)
        f = [c[0], d[0], c[0], c[0], c[0], c[0], c[0]]
        username = "".join(f)

    elif choice == "سباعيات حرف7": #ARRRRRR ~ 
        c = d = random.choices(a)
        d = random.choices(k)
        f = [c[0], d[0], d[0], d[0], d[0], d[0], d[0]]
        username = "".join(f)

    elif choice == "سباعيات رقم7": #A888888 ~ 
        c = d = random.choices(a)
        d = random.choices(o)
        f = [c[0], d[0], d[0], d[0], d[0], d[0], d[0]]
        username = "".join(f)

    elif choice == "ايقاف": #
        return "stop"
    else:
        return "error"
    return username


def validate_choice(choice):
    # الشروط:
    # 1. النمط لا يبدأ برقم
    # 2. لا يحتوي على أكثر من رمز خاص متتالي
    # 3. يحتوي فقط على الرموز المسموح بها: X, Y, Z, _ أو أحرف وأرقام أخرى
    # 4. ان لا يكون النمط اقل من 5 احرف 
    allowed_chars = {'X', 'Y', 'Z', '_'}
    if choice[0] == 'Y' or choice[0] == 'z':
        return False
    if '__' in choice:
        return False

    if len(choice) < 5 or len(choice) > 32:
        return False

    if choice[0].isdigit():  # تحقق من أن النمط لا يبدأ برقم
        return False

    if choice.endswith('_'):
        return False

    if '(' in choice and ')' in choice:
        # تحقق من الأقواس
        stack = []
        i = 0
        while i < len(choice):
            if choice[i] == '(':
                stack.append(i)
            elif choice[i] == ')':
                if not stack:
                    return False  # قوس مغلق بدون قوس مفتوح
                start_index = stack.pop()
                # تحقق من أن المحتوى داخل الأقواس يبدأ بحرف
                if start_index == 0 or choice[start_index - 1] not in allowed_chars:
                    if not choice[start_index + 1].isalpha():
                        return False
            i += 1
        if stack:  # إذا كان هناك أقواس مفتوحة غير مغلقة
            return False

    for i in range(len(choice) - 1):
        if choice[i] == '_' and choice[i + 1] == '_':
            return False

    for char in choice:
        if char not in allowed_chars and not char.isalnum() and char != '(' and char != ')':
            return False

    return True


def generate_random_string(choice):
    # تحقق من صحة النمط المدخل
        if not validate_choice(choice):
        return "error"
    # قاموس لحفظ القيم العشوائية لكل رمز
    random_values = {}
    # دالة لتوليد حرف عشوائي
    def get_random_letter():
        return random.choice(string.ascii_letters)
    # دالة لتوليد رقم عشوائي
    def get_random_digit():
        return random.choice(string.digits)
    # دالة لتوليد حرف أو رقم عشوائي
    def get_random_char():
        return random.choice(string.ascii_letters + string.digits)
    # إنشاء قيم عشوائية لكل رمز في النمط
    for char in choice:
        if char not in random_values:
            if char == 'X':
                random_values[char] = get_random_letter()
            elif char == 'Y':
                random_values[char] = get_random_digit()
            elif char == 'Z':
                random_values[char] = get_random_char()
            elif char == '(':
                random_values[char] = ""
            elif char == ')':
                random_values[char] = ""
            else:
                random_values[char] = char  # نحتفظ بالرموز الأخرى كما هي
    # بناء السلسلة النهائية باستخدام القيم العشوائية
    username = ''.join(random_values[char] for char in choice)
    return username


"""
# اختبار الدالة
choice1 = "XXX_YZ"
choice2 = "XXYZ"# نمط غير صالح
choice3 = "XYZ_XXX"
choice4 = "YXXX_Z"  # نمط غير صالح
choice5 = "XXX__YZ"  # نمط غير صالح
choice6 = "XXX_YZ_"  # نمط غير صالح
choice7 = "XXY*ZZ"  # نمط غير صالح
choice8 = "X_Y*Z"  # نمط غير صالح
choice9 = "X_Y_Z99"  # نمط صالح

print(generate_random_string(choice1))  # مثال: aaa_b2
print(generate_random_string(choice2))  # النمط غير صالح
print(generate_random_string(choice3))  # مثال: a2b_aaa
print(generate_random_string(choice4))  # النمط غير صالح
print(generate_random_string(choice5))  # النمط غير صالح
print(generate_random_string(choice6))  # النمط غير صالح
print(generate_random_string(choice7))  # النمط غير صالح
print(generate_random_string(choice8))  # النمط غير صالح
print(generate_random_string(choice9))  # مثال: f_7_z

# اختبار الاقواس
choice1 = "X_(4S)_Z"
choice2 = "(RRR3)X"
choice3 = "(7RR3)X"  # نمط غير صالح
choice4 = "X(RRR3)"
choice5 = "X(7RR3)"  # نمط مقبول ولكن مع رقم بعد X
choice6 = "XYZ_(123)_Z"

print(generate_random_string(choice1))  # مثال: قد تكون E_4S_Y أو E_4S_Y وهكذا.
print(generate_random_string(choice2))  # مثال: قد تكون RRR3X.
print(generate_random_string(choice3))  # النمط غير صالح.
print(generate_random_string(choice4))  # مثال: قد تكون RRR3.
print(generate_random_string(choice5))  # مثال: قد تكون X(7RR3).
print(generate_random_string(choice6))  # مثال: قد تكون a_123_c.
"""

BaqirHunter_cmd = (
    "ᯓ 𝗥𝗲𝗽𝘁𝗵𝗼𝗻 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر الصيـد 🎡\n"
    "⋆┄─┄─┄─┄┄┄──┄┄┄─┄─┄─┄⋆\n"
    "**✾ قـائمـة اوامـر تشيكـر (صيـد & تثبيت) يـوزرات تيليجـرام:** \n\n"
    "`.اوامر الصيد`\n"
    "**⪼ لـ عـرض قائمـة الاوامـر الخاصـه بـ صيـد اليـوزرات 🎣**\n\n"
    "`.اوامر المخصص`\n"
    "**⪼ لـ عـرض قائمـة الاوامـر الخاصـه بـ الصيـد المخصص (الجديده) 🪁**\n\n"
    "`.اوامر التثبيت`\n"
    "**⪼ لـ عـرض قائمـة الاوامـر الخاصـه بـ تثبيت اليـوزرات ⛳️**\n\n\n"
    "**- ملاحظـات مهمـه قبـل استخـدام اوامـر الصيـد والتثبيت :**\n"
    "**⪼** تأكد من ان حسابك يوجد فيه مساحه لانشاء قناة عامة (قناة بمعرف)\n"
    "**⪼** اذا كان لا يوجد مساحه لانشاء قناة عامة قم بارسال يوزر اي قناة من قنوات حسابك وبالرد ع يوزرها ارسل احد اوامر الصيد\n"
    "**⪼** تحلى بالصبر وكرر محاولات الصيد حتى تصيد يوزر"
)

BaqirCustom_cmd = (
"ᯓ 𝗥𝗲𝗽𝘁𝗵𝗼𝗻 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - الصيـد المخصص 🎡\n"
"⋆┄─┄─┄─┄┄┄──┄┄┄─┄─┄─┄⋆\n"
"**✾ شرح اوامـر الصيـد المخصص (انماط اختياريه):**\n\n"
"**• في حال كنت تريد صيد نوع محدد (شبه ثلاثي & رباعي - خماسي - سداسي ... الخ)**🧩\n"
"**• او نمط بحرف محدد (R - Z - A ...الخ) من اختيارك** 🤔\n"
"**• سوف يساعدك الصيد المخصص بصيد يوزرات مخصصه من اختيارك** 🏌‍♂\n\n"
"**✧ النمـط المخصص يتكـون مـن ثلاثه متغيـرات كالتـالي** 💠:\n"
"**• X   ⟶  يولد أحرف فقط** 🔠\n"
"**• Y   ⟶  يولد أرقام فقط** 🔢\n"
"**• Z   ⟶  يولد أحرف وأرقام معاً** 🔠🔢\n"
"**✧ شــروط تكويــن النمــط كالتالــي 🧩:**\n"
"• لا يبدأ النمـط بالمتغيـر  Y  أو  Z\n"
"• الرمـز  (_)  يـولـد شرطـه ثابتـه\n"
"• لا يحتوي النمـط على أكثر من  _  متتاليه\n"
"• لا يبدأ أو ينتهي النمـط بالرمز   _\n"
"• يجب أن يكون طـول النمـط بين 5 و 32 حرفًا فقط\n\n"
"**✧ أمثلــه علــى الصيــد المخصص بالنمــط:** 🎳\n\n"
".مخصص X_Y_Z\n"
"**⪼ يولـد يـوزرات مثـل ⟵ T_4_S أو T_4_8**\n\n"
".مخصص XZZXXX\n"
"**⪼ يولـد يـوزرات مثـل ⟵ TUUTTT أو T55TTT**\n\n"
".مخصص X_ZZZ\n"
"**⪼ يولـد يـوزرات مثـل ⟵ A_YYY أو S_888**\n\n"
".مخصص X_X_X**\n"
"**⪼ يولـد يـوزرات مثـل ⟵ S_S_S**\n\n\n\n"
"**✧ تخصيص (أحرف + ارقام + نوع) اليوزر المطلوب:** 🎲\n"
"**• يجب وضع الأحرف او الارقام المختاره داخل قوسين ()**\n"
"**• بحيث تبقى ثابته لا تتغير عند تخمين اليوزر**\n"
"**• مثــال:**\n"
".مخصص (RRR)XZ\n"
"**⪼ يولـد يـوزرات مثـل ⟵ RRRA7 أو RRRAB**\n\n"
"`.حالة مخصص`\n"
"**⪼ لـ معرفـة حالـة تقـدم عمليـة الصيـد المخصص** 📟\n\n"
"`.مخصص ايقاف`\n"
"**⪼ لـ إيقـاف عمليـة الصيـد المخصص الجاريـه** 🔚"
)

BaqirChecker_cmd = (
    "ᯓ 𝗥𝗲𝗽𝘁𝗵𝗼𝗻 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر الصيـد 🎡\n"
    "⋆┄─┄─┄─┄┄┄──┄┄┄─┄─┄─┄⋆\n"
    "**✾ قـائمـة اوامـر تشيكـر صيـد يـوزرات تيليجـرام :** \n\n"
    "`.النوع`\n"
    "**⪼ لـ عـرض الانـوع التي يمكـن صيدهـا مع الامثـله 🧩**\n\n"
    "`.صيد` + النـوع\n"
    "**⪼ لـ صيـد يـوزرات عشوائيـه على حسب النـوع المختار 🎣**\n\n"
    "`.حالة الصيد`\n"
    "**⪼ لـ معرفـة حالـة تقـدم عمليـة الصيـد** 📟\n\n"
    "`.صيد ايقاف`\n"
    "**⪼ لـ إيقـاف عمليـة الصيـد الجاريـه** 🔚\n\n"
    "`.اوامر المخصص`\n"
    "**⪼ لـ عـرض قائمـة الاوامـر الخاصـه بـ الصيـد المخصص (الجديده) 🪁**\n\n"
)

BaqirPin_cmd = (
    "ᯓ 𝗥𝗲𝗽𝘁𝗵𝗼𝗻 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر التثبيت 🎡\n"
    "⋆┄─┄─┄─┄┄┄──┄┄┄─┄─┄─┄⋆\n"
    "**✾ قـائمـة اوامـر تشيكـر صيـد يـوزرات تيليجـرام :** \n\n"
    "`.تثبيت_قناة` + اليوزر\n"
    "**⪼ لـ تثبيت اليـوزر بقنـاة معينـه اذا اصبح متاحـاً يتم اخـذه** 🌐\n"
    "`.حالة تثبيت_القناة`\n"
    "**⪼ لـ معرفـة حالـة تقـدم التثبيت التلقـائـي على القنـاة**\n"
    "`.ايقاف تثبيت_القناة`\n"
    "**⪼ لـ إيقـاف عمليـة تثبيت_القناة التلقـائـي**\n\n"
    "`.تثبيت_حساب` + اليوزر\n"
    "**⪼ لـ تثبيت اليـوزر بحسـابك مباشـرة اذا اصبح متاحـاً يتم اخـذه** 🚹\n"
    "`.حالة تثبيت_الحساب`\n"
    "**⪼ لـ معرفـة حالـة تقـدم التثبيت التلقـائـي على حسابـك**\n"
    "`.ايقاف تثبيت_الحساب`\n"
    "**⪼ لـ إيقـاف عمليـة تثبيت_الحساب التلقـائـي**\n\n"
    "`.تثبيت_بوت` + اليوزر\n"
    "**⪼ لـ تثبيت اليـوزر في بـوت فـاذر اذا اصبح متاحـاً يتم اخـذه** 🤖\n"
    "`.حالة تثبيت_البوت`\n"
    "**⪼ لـ معرفـة حالـة تقـدم التثبيت التلقـائـي على بـوت فـاذر**\n"
    "`.ايقاف تثبيت_البوت`\n"
    "**⪼ لـ إيقـاف عمليـة تثبيت_البوت التلقـائـي**"
)

BaqirType_cmd = (
"𓆩 [𝗦𝗼𝘂𝗿𝗰𝗲 𝗥𝗼𝗯𝗶𝗻 - أنـواع اليـوزرات](t.me/RobinSource) 𓆪\n\n"
"**✾╎قـائمـة أنـواع اليـوزرات التي يمكـن صيدهـا مـع الامثـلة :** \n\n"
"⪼  `.صيد ثلاثي1`  **مثـال ~** A_D_R\n"
"⪼  `.صيد ثلاثي2`  **مثـال ~** A_7_R\n"
"⪼  `.صيد ثلاثي3`  **مثـال ~** A_7_0\n\n"
"⪼  `.صيد رباعي1`  **مثـال ~** AAA_R\n"
"⪼  `.صيد رباعي2`  **مثـال ~** A_RRR\n"
"⪼  `.صيد رباعي3`  **مثـال ~** AA_RR\n"
"⪼  `.صيد رباعي4`  **مثـال ~** AA_AR\n"
"⪼  `.صيد رباعي5`  **مثـال ~** AA_RA\n"
"⪼  `.صيد رباعي6`  **مثـال ~** AR_RA\n"
"⪼  `.صيد رباعي7`  **مثـال ~** AR_AR\n"
"⪼  `.صيد رباعي8`  **مثـال ~** AR_RR\n\n"
"⪼  `.صيد شبه رباعي1`  **مثـال ~** A_A_A_R\n"
"⪼  `.صيد شبه رباعي2`  **مثـال ~** A_R_R_R\n"
"⪼  `.صيد شبه رباعي3`  **مثـال ~** A_RR_A\n"
"⪼  `.صيد شبه رباعي4`  **مثـال ~** A_RR_R\n\n"
"⪼  `.صيد خماسي حرفين1`  **مثـال ~** AAARD\n"
"⪼  `.صيد خماسي حرفين2`  **مثـال ~** A7RRR\n"
"⪼  `.صيد خماسي ارقام`  **مثـال ~** AR777\n\n"
"⪼  `.صيد خماسي حرفين3`  **مثـال ~** ARRRD\n"
"⪼  `.صيد سداسي_حرفين1`  **مثـال ~** ARAAAR\n"
"⪼  `.صيد سداسي_حرفين2`  **مثـال ~** AAAARR\n"
"⪼  `.صيد سداسي_حرفين3`  **مثـال ~** AAARRA\n"
"⪼  `.صيد سداسي_حرفين4`  **مثـال ~** AARRAA\n"
"⪼  `.صيد سداسي_حرفين5`  **مثـال ~** ARRAAA\n"
"⪼  `.صيد سداسي_حرفين6`  **مثـال ~** AARRRR\n"
"⪼  `.صيد سداسي_شرطه`  **مثـال ~** AAAA_R\n\n"
"⪼  `.صيد سباعيات1`  **مثـال ~** AAAAAAR\n"
"⪼  `.صيد سباعيات2`  **مثـال ~** AAAAARA\n"
"⪼  `.صيد سباعيات3`  **مثـال ~** AAAARAA\n"
"⪼  `.صيد سباعيات4`  **مثـال ~** AAARAAA\n"
"⪼  `.صيد سباعيات5`  **مثـال ~** AARAAAA\n"
"⪼  `.صيد سباعيات6`  **مثـال ~** ARAAAAA\n"
"⪼  `.صيد سباعيات7`  **مثـال ~** ARRRRRR\n\n"
"⪼  `.صيد بوتات1`  **مثـال ~** AR_Bot\n"
"⪼  `.صيد بوتات2`  **مثـال ~** A_RBot\n"
"⪼  `.صيد بوتات3`  **مثـال ~** AR7Bot\n"
"⪼  `.صيد بوتات4`  **مثـال ~** A7RBot\n"
"⪼  `.صيد بوتات5`  **مثـال ~** A77Bot\n"
"⪼  `.صيد بوتات6`  **مثـال ~** ADRBot\n"
"⪼  `.صيد بوتات7`  **مثـال ~** AARBot - AA8Bot\n"
"⪼  `.صيد بوتات8`  **مثـال ~** AARBot\n"
"⪼  `.صيد بوتات9`  **مثـال ~** AA8Bot\n\n"
"**- لـ عـرض اوامـر الصيـد والتثبيت الاساسيـة ارسـل الامـر التالـي :**\n"
"**⪼**  `.الصيد`  **او**  `.التثبيت`"
)


@l313l.ar_cmd(pattern="(الصيد|التثبيت)")
async def rhunter_cmd(baqir):
    await edit_or_reply(baqir, BaqirHunter_cmd)

@l313l.ar_cmd(pattern="(اوامر المخصص|المخصص)")
async def rcustom_cmd(baqir):
    await edit_or_reply(baqir, BaqirCustom_cmd)

@l313l.ar_cmd(pattern="اوامر الصيد")
async def rchecker_cmd(baqir):
    await edit_or_reply(baqir, BaqirChecker_cmd)

@l313l.ar_cmd(pattern="اوامر التثبيت")
async def rpin_cmd(baqir):
    await edit_or_reply(baqir, BaqirPin_cmd)

@l313l.ar_cmd(pattern="(النوع|الانواع)")
async def rtype_cmd(baqir):
    await edit_or_reply(baqir, BaqirType_cmd)


@l313l.ar_cmd(pattern="مخصص (.*)")
async def customhunter(event):
    choice = str(event.pattern_match.group(1))
    replly = await event.get_reply_message()
    if not choice:
        return await edit_or_reply(event, "⚈ **امـر خاطـئ .. تصفح اوامـر الصيـد**\n⚈ **لـ الاوامـر العامـه .. ارسـل** ( `.الصيد` )\n⚈ **لـ انـواع اليـوزرات .. ارسـل** ( `.الانواع` )")
    try:
        if replly and replly.text.startswith('@'):
            ch = replly.text
            await edit_or_reply(event, f"⚈ **تم بـدء الصيـد المخصص .. بنجـاح ☑️**\n⚈ **النـوع** {choice} \n⚈ **على القنـاة** {ch} \n⚈ **لمعرفـة حالة عمليـة الصيـد المخصص (** `.حالة مخصص` **)**\n⚈ **لـ ايقـاف عمليـة الصيـد (** `.مخصص ايقاف` **)**")
        else:
            baq = f"@{l313l.me.username}" if l313l.me.username else ""
            ch = await l313l(
                functions.channels.CreateChannelRequest(
                    title="صيـد روبن 𝗥𝗼𝗯𝗶𝗻 ",
                    about=f"This channel to custom hunt username by - @robinsource | {baq}",
                )
            )
            try:
                ch = ch.updates[1].channel_id
            except Exception:
                ch = ch.chats[0].id
            await edit_or_reply(event, f"⚈ **تم بـدء الصيـد المخصص .. بنجـاح ☑️**\n⚈ **علـى النـوع** {choice} \n⚈ **لمعرفـة حالة عمليـة الصيـد المخصص (** `.حالة مخصص` **)**\n⚈ **لـ ايقـاف عمليـة الصيـد المخصص (** `.مخصص ايقاف` **)**")
    except Exception as e:
        await l313l.send_message(event.chat_id, f"**- اووبـس .. خطـأ فـي إنشـاء القنـاة ؟!**\n**- تفاصيـل الخطـأ :**\n`{str(e)}`")
        vesmod = False

    validate_cchoice = validate_choice(choice)
    if not validate_cchoice:
        try:
            issclim.clear()
            issclim.append("off")
            srys[0] = 0
        except Exception:
            pass
        return await edit_or_reply(event, "**• عـذراً عـزيـزي .. النمـط خاطـئ ✖️**\n**• تم إيقاف الصيـد المخصص 🚷**\n\n**• لـ تصفح اوامـر الصيـد .. ارسـل** ( `.الصيد` )\n**• لـ انـواع اليـوزرات .. ارسـل** ( `.الانواع` )")

    issclim.clear()
    issclim.append("on")
    vesmod = True
    while vesmod:
        username = ""
        if choice == "ايقاف":
            break
        username = generate_random_string(choice)
        t = Thread(target=lambda q, arg1: q.put(
            check_user(arg1)), args=(que, username))
        t.start()
        t.join()
        isav = que.get()
        if "Available" in isav:
            await asyncio.sleep(1)
            try:
                await l313l(
                    functions.channels.UpdateUsernameRequest(
                        channel=ch, username=username
                    )
                )
                await event.client.send_message(
                    event.chat_id,
                    f"- Done : @{username} ✅\n- By : @RobinSource\n- Custom Hunting Log {srys[0]}",
                )
                await event.client.send_message(
                    "@F_O_1", f"- Done : @{username} ✅\n- By : @RobinSource\n- Hunting Log {srys[0]}",
                )
                break
            except FloodWaitError as rep:
                wait_time = rep.seconds
                await sleep(wait_time + 10)
                pass
            except telethon.errors.rpcerrorlist.UsernameInvalidError:
                #with open("banned.txt", "a") as f:
                    #f.write(f"\n{username}")
                pass
            except telethon.errors.FloodError as e:
                flood_error = e.seconds
                await sleep(flood_error + 10)
                pass
            except Exception as eee:
                if "too many public channels" in str(eee):
                    await l313l.send_message(
                        event.chat_id,
                        f"""- تم إيقاف الصيد:\n- انت تمتلك العديد من القنوات العامة\n- قم بحذف معرف او اكثر من قنواتك\n- لكي تستطيع استخدام الصيد""",
                    )
                    break
                elif "you can't create channels or chats" in str(eee):
                    await l313l.send_message(
                        event.chat_id,
                        f"""- حسابك محظور من شركة تيليجرام\n- لا يمكنك إنشاء قنوات أو مجموعات\n- للمزيد راسل بوت قيود تيليجرام @spambot""",
                    )
                    break
                elif "A wait of" in str(eee):
                    break
                else:
                    #await l313l.send_message(event.chat_id, f"**• خطأ بصيـد اليـوزر** {username} ؟!\n**• الخطأ:**\n{str(eee)}\n\n**• حسناً .. سوف استمـر بالصيـد ♾**")
                    pass
        else:
            pass
        srys[0] += 1
        await asyncio.sleep(1)
        #else:
            #pass
        #srys += 1
    issclim.clear()
    issclim.append("off")
    srys[0] = 0
    #srys = ""
    return await l313l.send_message(event.chat_id, "**- تم الانتهاء من الصيد المخصص .. بنجـاح ✅**")


@l313l.ar_cmd(pattern="صيد (.*)")
async def hunterusername(event):
    choice = str(event.pattern_match.group(1))
    replly = await event.get_reply_message()
    if not choice:
        return await edit_or_reply(event, "⚈ **امـر خاطـئ .. تصفح اوامـر الصيـد**\n⚈ **لـ الاوامـر العامـه .. ارسـل** ( `.الصيد` )\n⚈ **لـ انـواع اليـوزرات .. ارسـل** ( `.الانواع` )")
    try:
        if replly and replly.text.startswith('@'):
            ch = replly.text
            await edit_or_reply(event, f"⚈ **تم بـدء الصيـد .. بنجـاح ☑️**\n⚈ **النـوع** {choice} \n⚈ **على القنـاة** {ch} \n⚈ **لمعرفـة حالة عمليـة الصيـد (** `.حالة الصيد` **)**\n⚈ **لـ ايقـاف عمليـة الصيـد (** `.صيد ايقاف` **)**")
        else:
            baq = f"@{l313l.me.username}" if l313l.me.username else ""
            ch = await l313l(
                functions.channels.CreateChannelRequest(
                    title=" صيـد روبن 𝗥𝗼𝗯𝗶𝗻",
                    about=f"This channel to hunt username by - RobinSource| {baq}",
                )
            )
            try:
                ch = ch.updates[1].channel_id
            except Exception:
                ch = ch.chats[0].id
            await edit_or_reply(event, f"⚈ **تم بـدء الصيـد .. بنجـاح ☑️**\n⚈ **علـى النـوع** {choice} \n⚈ **لمعرفـة حالة عمليـة الصيـد (** `.حالة الصيد` **)**\n⚈ **لـ ايقـاف عمليـة الصيـد (** `.صيد ايقاف` **)**")
    except Exception as e:
        await l313l.send_message(event.chat_id, f"**- اووبـس .. خطـأ فـي إنشـاء القنـاة ؟!**\n**- تفاصيـل الخطـأ :**\n`{str(e)}`")
        vedmod = False

    itsclim.clear()
    itsclim.append("on")
    vedmod = True
    while vedmod:
        username = ""
        if choice == "ايقاف":
            break
        #username = await gen_user(choice) تبعي
        username = gen_user(choice)
        if username == "stop":
            itsclim.clear()
            itsclim.append("off")
            trys[0] = 0
            break
            return await edit_or_reply(event, "**- تم إيقـاف عمليـة الصيـد .. بنجـاح ✓**")
        if username == "error":
            await edit_or_reply(event, f"**- عـذراً عـزيـزي\n- لايوجـد نوع** {choice} \n**- لـ عرض الانواع ارسـل (**`.الانواع`**)**")
            break

        #username = gen_user(choice)
        t = Thread(target=lambda q, arg1: q.put(
            check_user(arg1)), args=(que, username))
        t.start()
        t.join()
        isav = que.get()
        if "Available" in isav:
            await asyncio.sleep(1)
            try:
                await l313l(
                    functions.channels.UpdateUsernameRequest(
                        channel=ch, username=username
                    )
                )
                await event.client.send_message(
                    event.chat_id,
                    f"- Done : @{username} ✅\n- By : @RobinSource\n- Hunting Log {trys[0]}",
                )
                await event.client.send_message(
                    "@F_O_1", f"- Done : @{username} ✅\n- By : @RobinSource\n- Hunting Log {trys[0]}",
                )
                break
            except FloodWaitError as rep: # تبعي
                wait_time = rep.seconds
                await sleep(wait_time + 10)
                pass
            except telethon.errors.rpcerrorlist.UsernameInvalidError:
                #with open("banned.txt", "a") as f:
                    #f.write(f"\n{username}")
                pass
            except telethon.errors.FloodError as e: # تبعي
                flood_error = e.seconds
                await sleep(flood_error + 10)
                pass
            except Exception as eee: # تبعي
                if "too many public channels" in str(eee): # تبعي
                    await l313l.send_message(
                        event.chat_id,
                        f"""- خطأ بصيـد اليـوزر @{username} ,\n- الخطأ :\nانت تمتلك العديد من القنوات العامة قم بحذف معرف او اكثر من قنواتك لكي تستطيع صيد هذا اليوزر""",
                    )
                    break
                elif "you can't create channels or chats" in str(eee): # تبعي
                    await zq_lo.send_message(
                        event.chat_id,
                        f"""- حسابك محظور من شركة تيليجرام\n- لا يمكنك إنشاء قنوات أو مجموعات\n- للمزيد راسل بوت قيود تيليجرام @spambot""",
                    )
                    break
                elif "A wait of" in str(eee):
                    break
                else: # تبعي
                    #await l313l.send_message(event.chat_id, f"**• خطأ بصيـد اليـوزر** {username} ؟!\n**• الخطأ:**\n{str(eee)}\n\n**• حسناً .. سوف استمـر بالصيـد ♾**")
                    pass
        else:
            pass
        trys[0] += 1
        await asyncio.sleep(1)
        #else:
            #pass
        #trys += 1
    itsclim.clear()
    itsclim.append("off")
    trys[0] = 0
    #trys = ""
    return await l313l.send_message(event.chat_id, "**- تم الانتهاء من الصيد .. بنجـاح ✅**")


@l313l.ar_cmd(pattern="تثبيت (.*)")
async def _(event):
    baqir = str(event.pattern_match.group(1))
    if baqir.startswith('@'):
        return await edit_or_reply(event, "⚈ **امـر خاطـئ .. تصفح اوامـر التثبيت**\n⚈ **لـ الاوامـر العامـه للتثبيت .. ارسـل** ( `.التثبيت` )")

@l313l.ar_cmd(pattern="تثبيت_قناة (.*)")
async def _(event):
    baqir = str(event.pattern_match.group(1))
    if not baqir.startswith('@'):
        return await edit_or_reply(event, "⚈ **عـذراً عـزيـزي المدخـل خطـأ ❌**\n⚈ **استخـدم الامـر كالتالـي**\n⚈ **ارسـل (**`.تثبيت_قناة`** + اليـوزر)**")
    try:
        baq = f"@{l313l.me.username}" if l313l.me.username else ""
        ch = await l313l(
            functions.channels.CreateChannelRequest(
                title=" تثبيت روبن 𝗥𝗼𝗯𝗶𝗻",
                about=f"تم تثبيت اليـوزر بواسطـة سـورس روبن - @RobinSource | {baq} ",
            )
        )
        try:
            ch = ch.updates[1].channel_id
        except Exception:
            ch = ch.chats[0].id
        await edit_or_reply(event, f"⚈ **تم بـدء التثبيت .. بنجـاح ☑️**\n⚈ **اليـوزر المثبت ( {zelzal} )**\n⚈ **لمعرفـة تقـدم عمليـة التثبيت (**`.حالة تثبيت_القناة`**)**\n⚈ **لـ ايقـاف عمليـة التثبيت (**`.ايقاف تثبيت_القناة`**)**")
    except Exception as e:
        await l313l.send_message(
            event.chat_id, f"**- اووبـس .. خطـأ فـي إنشـاء القنـاة ؟!**\n**- تفاصيـل الخطـأ :**\n`{str(e)}`"
        )
        cmodels = False

    iscuto.clear()
    iscuto.append("on")
    username = baqir.replace("@", "") 
    cmodels = True
    while cmodels:
        #isch = await checker_user(username)

        t = Thread(target=lambda q, arg1: q.put(
            checker_user(arg1)), args=(que, username))
        t.start()
        t.join()
        isav = que.get()
        if "Available" in isav:
            try:
                await l313l(functions.channels.UpdateUsernameRequest(
                        channel=ch, username=username))
                await event.client.send_message(
                    event.chat_id,
                    f"- Done : @{username} ✅\n- Save: ❲ Channel ❳\n- By : @RobinSource\n- Hunting Log {crys[0]}",
                )
                break
            except telethon.errors.rpcerrorlist.UsernameInvalidError:
                await event.client.send_message(event.chat_id, f"**• اليـوزر** @{username} **مبنـد** ❌\n**• تم إيقاف عملية التثبيت لهذا اليوزر**")
                break
            except FloodWaitError as rep: #Code by t.me/ZlZZ7
                wait_time = rep.seconds
                await sleep(wait_time + 10)
                pass
            except telethon.errors.FloodError as e:
                flood_error = e.seconds
                await sleep(flood_error + 10)
                pass
            except Exception as eee: # تبعي
                if "too many public channels" in str(eee): # تبعي
                    await l313l.send_message(
                        event.chat_id,
                        f"""- تم إيقاف الصيد:\n- انت تمتلك العديد من القنوات العامة\n- قم بحذف معرف او اكثر من قنواتك\n- لكي تستطيع استخدام الصيد""",
                    )
                    break
                elif "you can't create channels or chats" in str(eee): # تبعي
                    await l313l.send_message(
                        event.chat_id,
                        f"""- حسابك محظور من شركة تيليجرام\n- لا يمكنك إنشاء قنوات أو مجموعات\n- للمزيد راسل بوت قيود تيليجرام @spambot""",
                    )
                    break
                elif "USERNAME_PURCHASE_AVAILABLE" in str(eee):
                    await l313l.send_message(event.chat_id, f"**• لا تستطيع التثبيت ع** {username} ✖️\n**• اليوزر مرفوع منصه .. ومتاح للشراء 💲**\n\n**• لذلك تم إيقاف عملية التثبيت والخروج**")
                    break
                elif "A wait of" in str(eee):
                    await l313l.send_message(event.chat_id, f"**• الحساب .. بالع فلود تكرار 😵‍💫**\n**• لذلك تم إيقاف عملية التثبيت والخروج ☑️**\n**• للامان .. حاول اعادة عملية التثبيت في وقت اخر**\n**• لكي لا يتم حظر حسابك من قبل الشركة**")
                    break
                else: # تبعي
                    #await l313l.send_message(event.chat_id, f"**• خطأ بصيـد اليـوزر** {username} ؟!\n**• الخطأ:**\n{str(eee)}\n\n**• حسناً .. سوف استمـر بالصيـد ♾**")
                    pass
        else:
            pass
        crys[0] += 1
        #await asyncio.sleep(8)
        await asyncio.sleep(2)
        #else:
            #pass
        #trys += 1
    iscuto.clear()
    iscuto.append("off")
    crys[0] = 0
    #crys = ""
    return await l313l.send_message(event.chat_id, "**- تم الانتهاء من التثبيت .. بنجـاح ✅**")


@l313l.ar_cmd(pattern="تثبيت_حساب (.*)")
async def _(event):
    baqir = str(event.pattern_match.group(1))
    if not baqir.startswith('@'):
        return await edit_or_reply(event, "⚈ **عـذراً عـزيـزي المدخـل خطـأ ❌**\n⚈ **استخـدم الامـر كالتالـي**\n⚈ **ارسـل (**`.تثبيت_حساب`** + اليـوزر)**")
    await edit_or_reply(event, f"⚈ **تم بـدء التثبيت .. بنجـاح ☑️**\n⚈ **اليـوزر المثبت ( {l313l} )**\n⚈ **لمعرفـة تقـدم عمليـة التثبيت (**`.حالة تثبيت_الحساب`**)**\n⚈ **لـ ايقـاف عمليـة التثبيت (**`.ايقاف تثبيت_الحساب`**)**")
    istuto.clear()
    istuto.append("on")
    username = baqir.replace("@", "") 
    amodels = True
    while amodels:
        #isac = await checker_user(username)

        t = Thread(target=lambda q, arg1: q.put(
            checker_user(arg1)), args=(que, username))
        t.start()
        t.join()
        isac = que.get()
        if "Available" in isac:
            try:
                await l313l(functions.account.UpdateUsernameRequest(username=username))
                await event.client.send_message(
                    event.chat_id,
                    f"- Done : @{username} ✅\n- Save: ❲ Account ❳\n- By : @RobinSource \n- Hunting Log {arys[0]}",
                )
                break
            except telethon.errors.rpcerrorlist.UsernameInvalidError:
                await event.client.send_message(event.chat_id, f"**• اليـوزر** @{username} **مبنـد** ❌\n**• تم إيقاف عملية التثبيت لهذا اليوزر**")
                break
            except FloodWaitError as rep:
                wait_time = rep.seconds
                await sleep(wait_time + 10)
                pass
            except telethon.errors.FloodError as e:
                flood_error = e.seconds
                await sleep(flood_error + 10)
                pass
            except Exception as eee: # تبعي
                if "USERNAME_PURCHASE_AVAILABLE" in str(eee):
                    await l313l.send_message(event.chat_id, f"**• لا تستطيع التثبيت ع** {username} ✖️\n**• اليوزر مرفوع منصه .. ومتاح للشراء 💲**\n\n**• لذلك تم إيقاف عملية التثبيت والخروج**")
                    break
                elif "A wait of" in str(eee):
                    await l313l.send_message(event.chat_id, f"**• الحساب .. بالع فلود تكرار 😵‍💫**\n**• لذلك تم إيقاف عملية التثبيت والخروج ☑️**\n**• للامان .. حاول اعادة عملية التثبيت في وقت اخر**\n**• لكي لا يتم حظر حسابك من قبل الشركة**")
                    break
                else: # تبعي
                    #await l313l.send_message(event.chat_id, f"**• خطأ بصيـد اليـوزر** {username} ؟!\n**• الخطأ:**\n{str(eee)}\n\n**• حسناً .. سوف استمـر بالصيـد ♾**")
                    pass
        else:
            pass
        arys[0] += 1
        #await asyncio.sleep(8)
        await asyncio.sleep(2)
        #else:
            #pass
        #trys += 1
    istuto.clear()
    istuto.append("off")
    arys[0] = 0
    #arys = ""
    return await l313l.send_message(event.chat_id, "**- تم الإنتهـاء من تثبيت اليـوزر ع حسـابك .. بنجـاح ✅**")


@l313l.ar_cmd(pattern="تثبيت_بوت (.*)")
async def _(event):
    baqit = str(event.pattern_match.group(1))
    if not baqir.startswith('@'):
        return await edit_or_reply(event, "⚈ **عـذراً عـزيـزي المدخـل خطـأ ❌**\n⚈ **استخـدم الامـر كالتالـي**\n⚈ **ارسـل (**`.تثبيت_بوت`** + اليـوزر)**")
    await edit_or_reply(event, f"⚈ **تم بـدء التثبيت .. بنجـاح ☑️**\n⚈ **اليـوزر المثبت ( {zelzal} )**\n⚈ **لمعرفـة تقـدم عمليـة التثبيت (**`.حالة تثبيت_البوت`**)**\n⚈ **لـ ايقـاف عمليـة التثبيت (**`.ايقاف تثبيت_البوت`**)**")
    isbuto.clear()
    isbuto.append("on")
    username = baqir.replace("@", "") 
    bmodels = True
    rrrnm = " تثبيت روبن 𝗥𝗼𝗯𝗶𝗻 "
    rrrby = "تم تثبيت اليـوزر بواسطـة سـورس روبو - @RobinSource "
    while bmodels:
        #isbt = await checker_user(username)

        t = Thread(target=lambda q, arg1: q.put(
            checker_user(arg1)), args=(que, username))
        t.start()
        t.join()
        isac = que.get()
        if "Available" in isac:
            try:
                await bot.send_message("@BotFather", "/newbot")
                await asyncio.sleep(1)
                await bot.send_message("@BotFather", rrrnm)
                await asyncio.sleep(1)
                await bot.send_message("@BotFather", baqir)
                await asyncio.sleep(3)
                await bot.send_message("@BotFather", "/setabouttext")
                await asyncio.sleep(1)
                await bot.send_message("@BotFather", baqir)
                await asyncio.sleep(1)
                await bot.send_message("@BotFather", rrrby)
                await asyncio.sleep(3)
                await bot.send_message("@BotFather", "/setdescription")
                await asyncio.sleep(1)
                await bot.send_message("@BotFather", baqir)
                await asyncio.sleep(1)
                await bot.send_message("@BotFather", rrrby)
                await event.client.send_message(
                    event.chat_id,
                    f"- Done : @{username} ✅\n- Save: ❲ Bot ❳\n- By : @RobinSource \n- Hunting Log {brys[0]}",
                )
                break
            except FloodWaitError as rep:
                wait_time = rep.seconds
                await sleep(wait_time + 10)
                pass
            except telethon.errors.rpcerrorlist.UsernameInvalidError:
                await event.client.send_message(event.chat_id, f"**• اليـوزر** @{username} **مبنـد** ❌\n**• تم إيقاف عملية التثبيت لهذا اليوزر**")
                break
            except telethon.errors.FloodError as e:
                flood_error = e.seconds
                await sleep(flood_error + 10)
                pass
            except Exception as eee:
                if "20 bots" in str(eee): # تبعي
                    await l313l.send_message(
                        event.chat_id,
                        f"""- خطأ بصيـد اليـوزر @{username} ,\n- الخطأ :\nانت تمتلك العديد من القنوات العامة قم بحذف معرف او اكثر من قنواتك لكي تستطيع صيد هذا اليوزر""",
                    )
                    break
                elif "USERNAME_PURCHASE_AVAILABLE" in str(eee):
                    await l313l.send_message(event.chat_id, f"**• لا تستطيع التثبيت ع** {username} ✖️\n**• اليوزر مرفوع منصه .. ومتاح للشراء 💲**\n\n**• لذلك تم إيقاف عملية التثبيت والخروج**")
                    break
                elif "A wait of" in str(eee):
                    await l313l.send_message(event.chat_id, f"**• الحساب .. بالع فلود تكرار ??‍💫**\n**• لذلك تم إيقاف عملية التثبيت والخروج ☑️**\n**• للامان .. حاول اعادة عملية التثبيت في وقت اخر**\n**• لكي لا يتم حظر حسابك من قبل الشركة**")
                    break
                else: # تبعي
                    #await l313l.send_message(event.chat_id, f"**• خطأ بتثبيت اليـوزر** {username} ؟!\n**• الخطأ:**\n{str(eee)}\n\n**• تم إيقاف عملية تثبيت هذا اليوزر ✖️**")
                    break
        else:
            pass
        brys[0] += 1

        await asyncio.sleep(5)
    isbuto.clear()
    isbuto.append("off")
    brys[0] = 0
    return await l313l.send_message(event.chat_id, "**- تم الإنتهـاء من تثبيت البـوت .. بنجـاح ✅**\n**- لـ التأكـد قـم بالذهـاب الـى @BotFather**")


@l313l.ar_cmd(pattern="حالة مخصص")
async def _(event):
    if "on" in issclim:
        await edit_or_reply(event, f"**- الصيد المخصص وصل لـ({srys[0]}) من المحـاولات**")
    elif "off" in issclim:
        await edit_or_reply(event, "**- لا توجد عمليـة صيد مخصص جاريـه حاليـاً ؟!**")
    else:
        await edit_or_reply(event, "**- لقد حدث خطأ ما وتوقف الامر لديك**")

@l313l.ar_cmd(pattern="حالة الصيد")
async def _(event):
    if "on" in itsclim:
        await edit_or_reply(event, f"**- الصيد وصل لـ({trys[0]}) من المحـاولات**")
    elif "off" in itsclim:
        await edit_or_reply(event, "**- لا توجد عمليـة صيد جاريـه حاليـاً ؟!**")
    else:
        await edit_or_reply(event, "**- لقد حدث خطأ ما وتوقف الامر لديك**")

@l313l.ar_cmd(pattern="حالة تثبيت_القناة")
async def _(event):
    if "on" in iscuto:
        await edit_or_reply(event, f"**- التثبيت وصل لـ({crys[0]}) من المحاولات**")
    elif "off" in iscuto:
        await edit_or_reply(event, "**- لا توجد عمليـة تثبيث جاريـه حاليـاً ؟!**")
    else:
        await edit_or_reply(event, "-لقد حدث خطأ ما وتوقف الامر لديك")

@l313l.ar_cmd(pattern="حالة تثبيت_الحساب")
async def _(event):
    if "on" in istuto:
        await edit_or_reply(event, f"**- التثبيت وصل لـ({arys[0]}) من المحاولات**")
    elif "off" in istuto:
        await edit_or_reply(event, "**- لا توجد عمليـة تثبيث جاريـه حاليـاً ؟!**")
    else:
        await edit_or_reply(event, "-لقد حدث خطأ ما وتوقف الامر لديك")

@l313l.ar_cmd(pattern="حالة تثبيت_البوت")
async def _(event):
    if "on" in isbuto:
        await edit_or_reply(event, f"**- التثبيت وصل لـ({brys[0]}) من المحاولات**")
    elif "off" in isbuto:
        await edit_or_reply(event, "**- لا توجد عمليـة تثبيث جاريـه حاليـاً ؟!**")
    else:
        await edit_or_reply(event, "-لقد حدث خطأ ما وتوقف الامر لديك")


@l313l.ar_cmd(pattern="ايقاف تثبيت_القناة")
async def _(event):
    if "on" in iscuto:
        iscuto.clear()
        iscuto.append("off")
        crys[0] = 0
        return await edit_or_reply(event, "**- تم إيقـاف عمليـة التثبيت .. بنجـاح ✓**")
    elif "off" in iscuto:
        return await edit_or_reply(event, "**- لا توجد عمليـة تثبيث جاريـه حاليـاً ؟!**")
    else:
        return await edit_or_reply(event, "**-لقد حدث خطأ ما وتوقف الامر لديك**")

@l313l.ar_cmd(pattern="ايقاف تثبيت_الحساب")
async def _(event):
    if "on" in istuto:
        istuto.clear()
        istuto.append("off")
        arys[0] = 0
        return await edit_or_reply(event, "**- تم إيقـاف عمليـة التثبيت .. بنجـاح ✓**")
    elif "off" in istuto:
        return await edit_or_reply(event, "**- لا توجد عمليـة تثبيث جاريـه حاليـاً ؟!**")
    else:
        return await edit_or_reply(event, "**-لقد حدث خطأ ما وتوقف الامر لديك**")

@l313l.ar_cmd(pattern="ايقاف تثبيت_البوت")
async def _(event):
    if "on" in isbuto:
        isbuto.clear()
        isbuto.append("off")
        brys[0] = 0
        return await edit_or_reply(event, "**- تم إيقـاف عمليـة التثبيت .. بنجـاح ✓**")
    elif "off" in isbuto:
        return await edit_or_reply(event, "**- لا توجد عمليـة تثبيث جاريـه حاليـاً ؟!**")
    else:
        return await edit_or_reply(event, "**-لقد حدث خطأ ما وتوقف الامر لديك**")