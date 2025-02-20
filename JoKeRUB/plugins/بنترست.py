from JoKeRUB import l313l
import requests
import json
import os
import re
from bs4 import BeautifulSoup
from urllib.parse import quote

headers = {
    'authority': 'pinterestvideodownloader.com',
    'content-type': 'application/x-www-form-urlencoded',
}

def search_pinterest(query):
    url = f"https://www.pinterest.com/resource/BaseSearchResource/get/"
    params = {
        "source_url": f"/search/pins/?q={query}&rs=typed",
        "data": json.dumps({"options": {"query": query, "scope": "pins"}})
    }
    r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, params=params)
    try:
        data = r.json()
        images = [item["images"]["orig"]["url"] for item in data["resource_response"]["data"]["results"] if "images" in item and "orig" in item["images"]]
        return images
    except (json.JSONDecodeError, KeyError):
        return []

def download_pinterest_video(url):
    data = {'url': url}
    response = requests.post('https://pinterestvideodownloader.com/download.php', headers=headers, data=data).text
    result = re.findall(r'<video src="(.*?)"', response)
    return result[0] if result else None

@l313l("ابحث")
def handle_search(event):
    query = event.text.replace(".ابحث ", "").strip()
    images = search_pinterest(query)
    if images:
        for img_url in images[:5]:
            event.reply(img_url)
    else:
        event.reply("❌ لم أجد صورًا متعلقة بهذا البحث.")

@l313l("تحميل من بنترس")
def handle_download(event):
    url = event.text.replace(".تحميل من بنترس ", "").strip()
    video_url = download_pinterest_video(url)
    if video_url:
        event.reply(video_url)
    else:
        event.reply("❌ لم أتمكن من تحميل الفيديو.")