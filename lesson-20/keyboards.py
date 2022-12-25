from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from configs import *


def generate_language():
    """Функция для выбора языка"""
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    button = []
    for lang in LANGUAGES.values():
        btn = KeyboardButton(text=lang)
        button.append(btn)

    markup.add(*button)

    return markup
