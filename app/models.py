# models.py
from typing import List

from pydantic import BaseModel


class WordDetails(BaseModel):
    word: str
    definitions: List[str]
    synonyms: List[str]
    translations: List[str]
    examples: List[str]
