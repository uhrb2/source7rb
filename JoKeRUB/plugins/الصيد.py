import random
import requests
import time
import asyncio
from asyncio import sleep
import telethon
from telethon.sync import functions
from telethon.errors import FloodWaitError
from user_agent import generate_user_agent
from JoKeRUB import l313l
from ..core.managers import edit_or_reply

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

    elif choice == "سداسيات5": #ARAAAA ~ 
        c = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], c[0], c[0], c[0], c[0]]
        username = "".join(f)

    elif choice == "سداسيات6": #ARRRRR ~ 
        c = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], d[0], d[0], d[0], d[0]]
        username = "".join(f)

    elif choice == "سداسيvip": #VIP537 ~ 
        c = random.choices(b)
        d = random.choices(o)
        s = random.choices(q)
        f = ["v", "i", "p", c[0], d[0], s[0]]
        username = "".join(f)

    elif choice == "سداسي_vip": #VIP537 ~ 
        c = random.choices(b)
        d = random.choices(o)
        f = ["v", "i", "p", "_", c[0], d[0]]
        username = "".join(f)

    elif choice == "بوتات1": #AR_Bot ~ 
        c = random.choices(a)
        d = random.choices(z)
        f = [c[0], d[0], "_", "b", "o", "t"]
        username = "".join(f)

    elif choice == "بوتات2": #A_RBot ~ 
        c = random.choices(a)
        d = random.choices(z)
        f = [c[0], "_", d[0], "b", "o", "t"]
        username = "".join(f)

    elif choice == "بوتات3": #AR7Bot ~ 
        c = random.choices(a)
        d = random.choices(k)
        s = random.choices(b)
        f = [c[0], d[0], s[0], "b", "o", "t"]
        username = "".join(f)

    elif choice == "بوتات4": #A7RBot ~ 
        c = random.choices(a)
        d = random.choices(b)
        s = random.choices(k)
        f = [c[0], d[0], s[0], "b", "o", "t"]
        username = "".join(f)

    elif choice == "بوتات5": #A77Bot ~ 
        c = random.choices(a)
        d = random.choices(b)
        s = random.choices(o)
        f = [c[0], d[0], s[0], "b", "o", "t"]
        username = "".join(f)

    elif choice == "بوتات6": #ADRBot
        c = random.choices(a)
        d = random.choices(e)
        s = random.choices(z)
        f = [c[0], d[0], s[0], "b", "o", "t"]
        username = "".join(f)

    elif choice == "بوتات7": #(AARBot - AA8bot) ~ 
        c = random.choices(a)
        d = random.choices(z)
        f = [c[0], c[0], d[0], "b", "o", "t"]
        username = "".join(f)

    elif choice == "بوتات8": #AARBot ~ 
        c = random.choices(a)
        d = random.choices(k)
        f = [c[0], c[0], d[0], "b", "o", "t"]
        username = "".join(f)

    elif choice == "بوتات9": #AA8Bot ~ 
        c = random.choices(a)
        d = random.choices(o)
        f = [c[0], c[0], d[0], "b", "o", "t"]
        username = "".join(f)

    elif choice == "خماسي حرفين1": #AAARD ~ 
        c = random.choices(a)
        d = random.choices(z)
        s = random.choices(e)
        f = [c[0], c[0], c[0], s[0], d[0]]
        username = "".join(f)

        elif choice == "خماسي ارقام": #AR888 ~ 
        c = random.choices(a)
        d = random.choices(e)
        s = random.choices(b)
        f = [c[0], d[0], s[0], s[0], s[0]]
        username = "".join(f)

    elif choice == "خماسي رقمين1": #AAARD ~ 
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