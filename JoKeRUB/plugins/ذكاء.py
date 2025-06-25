from JoKeRUB import l313l
import requests
import json
import random
from telethon import events
from gtts import gTTS
import os

GEMINI_API_KEY = 'AIzaSyC9F7-JJ2jHd4SA4Qo90AwzKhrgHBpPn0A'

GIRL_RESPONSES = [
    "هلا! معك رسن بنت السعودية، وش تبي؟",
    "يوه يا زينك! وش سوالفك اليوم؟",
    "أبشر، رسن هنا دايمًا معك.",
    "وش عندك سؤال؟ ترى أحب الضحك والمزح.",
]

UNKNOWN_RESPONSES = [
    "ما فهمت، عيد السؤال.",
    "فيه مشكلة بالاتصال، حاول بعدين.",
]

async def chat_with_gemini_girl(question: str) -> str:
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
                    girl_intro = random.choice(GIRL_RESPONSES)
                    gemini_reply = candidate['content']['parts'][0].get('text', random.choice(UNKNOWN_RESPONSES))
                    return f"{girl_intro}. {gemini_reply}"
                else:
                    return random.choice(UNKNOWN_RESPONSES)
            else:
                return random.choice(UNKNOWN_RESPONSES)
        else:
            return "فيه مشكلة بالسيرفر، حاول بعدين."
    except requests.exceptions.RequestException:
        return "الاتصال خرب، جرب مرة ثانية."

async def send_voice(event, text):
    tts = gTTS(text, lang='ar')
    file_path = "rasan_voice.mp3"
    tts.save(file_path)
    await event.respond(file=file_path, reply_to=event.id)
    os.remove(file_path)

@l313l.on(events.NewMessage(pattern=r"^\.ذكاء (.+)"))
async def ai_girl_handler(event):
    question = event.pattern_match.group(1)
    response = await chat_with_gemini_girl(question)
    await send_voice(event, response)

@l313l.on(events.NewMessage(pattern=r"^\.رسن (.+)"))
async def robin_girl_handler(event):
    question = event.pattern_match.group(1)
    response = await chat_with_gemini_girl(question)
    await send_voice(event, response)