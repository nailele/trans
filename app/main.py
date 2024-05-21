from fastapi import FastAPI, HTTPException

from app.services import delete_word, get_all_words, get_word_details

app = FastAPI()


@app.get("/word/{word}")
async def read_word(word: str, source: str = 'auto', dest: str = "en"):
    details = await get_word_details(word, source, dest)
    if details is None:
        raise HTTPException(detail="Word not found", status_code=404)
    return details


@app.get("/words")
async def read_words(skip: int = 0, limit: int = 10):
    words = await get_all_words(skip, limit)
    return words


@app.delete("/word/{word}")
async def delete_word_endpoint(word: str):
    success = await delete_word(word)
    if not success:
        raise HTTPException(status_code=404, detail="Word not found")
    return {"detail": "Word deleted"}
