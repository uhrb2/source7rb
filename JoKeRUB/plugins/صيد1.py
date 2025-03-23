import random
import requests
import asyncio
from asyncio import sleep
from telethon.sync import functions
from telethon.errors import FloodWaitError
from user_agent import generate_user_agent
from JoKeRUB import l313l
from ..core.managers import edit_or_reply

# Add Gemini AI functionality
API_GEMINI = 'AIzaSyA5pzOpKVcMGm6Aek82KoB3Pk94dYg3LX4'

async def use_gemini_ai(question):
    url = f"https://api.gemini.com/v1/ai_query?question={question}&key={API_GEMINI}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['answer']
    else:
        return "Error: Unable to get a response from Gemini AI"

# Example function to use the AI
async def handle_question(event, question):
    answer = await use_gemini_ai(question)
    await event.reply(f"ذكاء + سؤالك: {answer}")

# Add your existing functions and logic here random
import requests
import asyncio
from asyncio import sleep
from telethon.sync import functions
from telethon.errors import FloodWaitError
from user_agent import generate_user_agent
from JoKeRUB import l313l
from ..core.managers import edit_or_reply

