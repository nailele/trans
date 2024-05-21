import json

import redis
from googletrans import Translator

from app.utils import extract_explanations, extract_translations

r = redis.Redis(host='localhost', port=6379, db=0)


async def get_word_details(word: str, source: str, dest: str):
    if r.exists(word):
        return json.loads(r.get(word))

    dirty_word_details = Translator().translate(text=word, dest=dest, src=source)
    word_details = parse_word_details(dirty_word_details)
    if dirty_word_details.text:
        r.set(word, json.dumps(word_details))

    return word_details


def parse_word_details(details: Translator) -> dict:
    information = {"word": details.text, "dest": details.dest, "src": details.src}

    if len(details.extra_data["parsed"]) >= 4:
        explanation_dirty = details.extra_data["parsed"][3][1]
        if explanation_dirty:
            information["explanation"] = extract_explanations(explanation_dirty)

        synonyms_dirty = details.extra_data["parsed"][3][5]
        if synonyms_dirty:
            information["synonyms"] = extract_translations(synonyms_dirty[0])
        information["pronunciation"] = details.extra_data["parsed"][3][6]

    return information


async def get_all_words(skip: int, limit: int):
    keys = r.keys()[skip:skip+limit]
    words = [json.loads(r.get(key)) for key in keys]

    return words


async def delete_word(word: str):
    if r.exists(word):
        r.delete(word)
        return True

    return False
