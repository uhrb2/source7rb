import random, re 

from telethon import Button
from telethon.events import CallbackQuery, InlineQuery

from JoKeRUB import CMD_HELP, l313l

# 𝗧𝗲𝗹𝗲𝗚𝗿𝗮𝗠 : @robinuserbot  ~ @F_O_1
from ..core.decorators import check_owner

CALC = {}
plugin_category = "utils"
m = [
    "AC",
    "C",
    "⌫",
    "%",
    "7",
    "8",
    "9",
    "+",
    "4",
    "5",
    "6",
    "-",
    "1",
    "2",
    "3",
    "x",
    "00",
    "0",
    ".",
    "÷",
]
tultd = [Button.inline(f"{x}", data=f"calc{x}") for x in m]
lst = list(zip(tultd[::4], tultd[1::4], tultd[2::4], tultd[3::4]))
lst.append([Button.inline("=", data="calc=")])


@l313l.on(admin_cmd(pattern="حاسبة(?:\s|$)([\s\S]*)"))
async def icalc(e):
    if e.client._bot:
        return await e.reply(
            "**الحـاسبة العـلمية لسـورس Robin \n @RobinUserBot**", buttons=lst
        )
    results = await e.client.inline_query(Config.TG_BOT_USERNAME, "calc")
    await results[0].click(e.chat_id, silent=True, hide_via=True)
    await e.delete()


@l313l.tgbot.on(InlineQuery)
async def inlinecalc(event):
    query_user_id = event.query.user_id
    query = event.text
    string = query.lower()
    if (
        query_user_id == Config.OWNER_ID or query_user_id in Config.SUDO_USERS
    ) and string == "calc":
        event.builder
        calc = event.builder.article(
            "Calc", text="**الحـاسبة العـلمية لسـورس Robin \n @RobinUserBot**", buttons=lst
        )
        await event.answer([calc])


# 𝗧𝗲𝗹𝗲𝗚𝗿𝗮𝗠 : @RobinUserBot  ~ @F_O_1
@l313l.tgbot.on(CallbackQuery(data=re.compile(b"calc(.*)")))
@check_owner
async def _(e):  # sourcery no-metrics
    x = (e.data_match.group(1)).decode()
    user = e.query.user_id
    get = None
    if x == "AC":
        if CALC.get(user):
            CALC.pop(user)
        await e.edit(
            "**الحـاسبة العـلمية لسـورس Robin \n @RobinUserBot**",
            buttons=[Button.inline("افتح مره اخرى", data="recalc")],
        )
    elif x == "C":
        if CALC.get(user):
            CALC.pop(user)
        await e.answer("تم الحذف")
    elif x == "⌫":
        if CALC.get(user):
            get = CALC[user]
        if get:
            CALC.update({user: get[:-1]})
            await e.answer(str(get[:-1]))
    elif x == "%":
        if CALC.get(user):
            get = CALC[user]
        if get:
            CALC.update({user: get + "/100"})
            await e.answer(str(get + "/100"))
    elif x == "÷":
        if CALC.get(user):
            get = CALC[user]
        if get:
            CALC.update({user: get + "/"})
            await e.answer(str(get + "/"))
    elif x == "x":
        if CALC.get(user):
            get = CALC[user]
        if get:
            CALC.update({user: get + "*"})
            await e.answer(str(get + "*"))
    elif x == "=":
        if CALC.get(user):
            get = CALC[user]
        if get:
            if get.endswith(("*", ".", "/", "-", "+")):
                get = get[:-1]
            out = eval(get)
            try:
                num = float(out)
                await e.answer(f"▾∮ الجـواب : {num}", cache_time=0, alert=True)
            except BaseException:
                CALC.pop(user)
                await e.answer("خـطأ", cache_time=0, alert=True)
        await e.answer("غير معروف")
    else:
        if CALC.get(user):
            get = CALC[user]
        if get:
            CALC.update({user: get + x})
            return await e.answer(str(get + x))
        CALC.update({user: x})
        await e.answer(str(x))


# 𝗧𝗲𝗹𝗲𝗚𝗿𝗮𝗠 : @RobinUserBot  ~ @F_O_1
@l313l.tgbot.on(CallbackQuery(data=re.compile(b"recalc")))
@check_owner
async def _(e):
    m = [
        "AC",
        "C",
        "⌫",
        "%",
        "7",
        "8",
        "9",
        "+",
        "4",
        "5",
        "6",
        "-",
        "1",
        "2",
        "3",
        "x",
        "00",
        "0",
        ".",
        "÷",
    ]
    tultd = [Button.inline(f"{x}", data=f"calc{x}") for x in m]
    lst = list(zip(tultd[::4], tultd[1::4], tultd[2::4], tultd[3::4]))
    lst.append([Button.inline("=", data="calc=")])
    await e.edit("**الحـاسبة العـلمية لسـورس Robin \n @RobinUserBot**", buttons=lst)

CMD_HELP.update(
    {"الحسابة": ".حاسبة" "\n فقط اكتب الامر لعرض حاسبة علميه تحتاج الى تفعيل وضع الانلاين اولا\n\n"}
)


import tkinter as tk
import math

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.expression = ""
        self.input_text = tk.StringVar()

        # إنشاء واجهة المستخدم
        self.create_ui()

    def create_ui(self):
        input_frame = tk.Frame(self.root, width=400, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
        input_frame.pack(side=tk.TOP)

        input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=self.input_text, width=50, bg="#eee", bd=0, justify=tk.RIGHT)
        input_field.grid(row=0, column=0)
        input_field.pack(ipady=10)

        buttons_frame = tk.Frame(self.root, width=400, height=450, bg="grey")
        buttons_frame.pack()

        # أزرار الأرقام
        buttons = [
            '7', '8', '9', '/', 'C',
            '4', '5', '6', '*', 'sin',
            '1', '2', '3', '-', 'cos',
            '0', '.', '=', '+', 'tan'
        ]

        row = 0
        col = 0
        for button in buttons:
            tk.Button(buttons_frame, text=button, width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                      command=lambda x=button: self.on_button_click(x)).grid(row=row, column=col, padx=1, pady=1)
            col += 1
            if col > 4:
                col = 0
                row += 1

    def on_button_click(self, button):
        if button == 'C':
            self.expression = ""
            self.input_text.set("")
        elif button == '=':
            try:
                result = str(eval(self.expression))
                self.input_text.set(result)
                self.expression = result
            except Exception as e:
                self.input_text.set("خطأ")
                self.expression = ""
        elif button in ['sin', 'cos', 'tan']:
            try:
                result = str(getattr(math, button)(math.radians(float(self.expression))))
                self.input_text.set(result)
                self.expression = result
            except Exception as e:
                self.input_text.set("خطأ")
                self.expression = ""
        else:
            self.expression += button
            self.input_text.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = ScientificCalculator(root)
    root.mainloop()