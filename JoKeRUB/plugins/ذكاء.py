from JoKeRUB import l313l
import requests
import json
import random
from telethon import events

# مفتاح API الخاص بـ Gemini
GEMINI_API_KEY = 'AIzaSyC9F7-JJ2jHd4SA4Qo90AwzKhrgHBpPn0A'

# ردود افتراضية في حال حدوث خطأ
UNKNOWN_RESPONSES = [
    "لم أفهم سؤالك، يرجى التوضيح.",
    "هناك مشكلة في الاتصال، حاول مرة أخرى لاحقًا."
]

# دالة للتواصل مع Gemini API
async def chat_with_gemini(question: str) -> str:
    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
        headers = {'Content-Type': 'application/json'}

        payload = {
            "contents": [{
                "parts": [{"text": question}]
            }]
        }

        response = requests.post(url, headers=headers, data=json.dumps(payload))

        if response.status_code == 200:
            response_data = response.json()
            if 'candidates' in response_data and len(response_data['candidates']) > 0:
                candidate = response_data['candidates'][0]
                if 'content' in candidate and 'parts' in candidate['content']:
                    return candidate['content']['parts'][0].get('text', random.choice(UNKNOWN_RESPONSES))
                else:
                    return random.choice(UNKNOWN_RESPONSES)
            else:
                return random.choice(UNKNOWN_RESPONSES)
        else:
            return "فشل الاتصال بالخادم، حاول مرة أخرى."

    except requests.exceptions.RequestException:
        return "هناك مشكلة في الاتصال، حاول لاحقًا."

# حدث يستمع للأمر ".ذكاء + السؤال"
@l313l.on(events.NewMessage(pattern=r"^\.ذكاء (.+)"))
async def ai_handler(event):
    question = event.pattern_match.group(1)  # استخراج السؤال بعد ".ذكاء"
    await event.reply("🤖 جارٍ معالجة سؤالك بواسطة الذكاء الاصطناعي...")

    response = await chat_with_gemini(question)  # الحصول على الرد من الذكاء الاصطناعي
    await event.reply(response)  # إرسال الرد للمستخدم