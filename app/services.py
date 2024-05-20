# services.py
import json

#from deep_translator import GoogleTranslator
#from langdetect import detect
from googletrans import Translator

import httpx
import redis

r = redis.Redis(host='localhost', port=6379, db=0)


def translate_word(word):
    try:
        return Translator().translate(word).text
    except Exception as e:
        print(f"Error: {e}")
        return None



async def get_word_details(word: str):
    if r.exists(word):
        return json.loads(r.get(word))
    else:
        details = translate_word(word)
        if details:
            r.set(word, json.dumps(details))
        return details


async def get_all_words(skip: int, limit: int):
    keys = r.keys()[skip:skip+limit]
    words = [json.loads(r.get(key)) for key in keys]
    return words


async def delete_word(word: str):
    if r.exists(word):
        r.delete(word)
        return True
    return False
