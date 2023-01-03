from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


def generate_categories(categories):
    markup = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    buttons = []
    for category in categories:
        btn = KeyboardButton(text=category[0])
        buttons.append(btn)
    markup.add(*buttons)
    return markup

def generate_download_button(image_id):
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton(text='Скачать изображение', callback_data=f'download_{image_id[0]}')
    markup.add(button)
    return markup