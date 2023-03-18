from fuzzywuzzy import fuzz
from aiogram.types import ReplyKeyboardMarkup


async def get_text_ratio(text1: str, text2: str):
    text1, text2 = text1.lower(), text2.lower()
    result = fuzz.ratio(text1, text2)
    if result >= 80:
        return True
    return False


async def check_user_selected_liga(markup, selected: str):
    for kb in markup:
        for i in kb:
            if i['callback_data'] == selected:
                return i['text']

