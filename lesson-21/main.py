from os import getenv
from database import select_categories, check_category_name, get_image_links, get_image_id, get_image
from keyboards import generate_categories, generate_download_button
from random import randint
import re

from aiogram import executor, Bot, Dispatcher
from aiogram.types import Message, CallbackQuery
from dotenv import load_dotenv

load_dotenv()
TOKEN = getenv('TOKEN')
bot = Bot(TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def command_start(message: Message):
    await message.answer('Добро пожалолвать в наш тг бот')
    await show_categories(message)


async def show_categories(message: Message):
    chat_id = message.chat.id
    categories = select_categories()
    await message.answer('Выберите категорию', reply_markup=generate_categories(categories))

@dp.message_handler(content_types=['text'])
async def get_image_by_category(message: Message):
    category_name = message.text
    if category_id := check_category_name(category_name):
        image_links = get_image_links(category_id[0])
        random_index = randint(0, len(image_links) - 1)
        random_image_link = image_links[random_index][0]
        resolution = re.search( '[0-9]+x[0-9]+', random_image_link)[0]
        image_id = get_image_id(random_image_link)
        try:
            await message.answer_photo(photo=random_image_link,
                                       caption=f'Разрешение {resolution}',
                                       reply_markup=generate_download_button(image_id))
        except Exception as e:
            print(e.__class__)
            print(e.__class__.__name__)
            resize_link = random_image_link.replace(resolution, '1920x1080')
            await message.answer_photo(photo=resize_link,
                                       caption=f'Разрешение {resolution} try',
                                       reply_markup=generate_download_button(image_id))

    else:
        await message.answer('Просто нажмите на кнопку')
        await show_categories(message)


@dp.callback_query_handler(lambda call: 'download' in call.data)
async def download_finction(call: CallbackQuery):
    chat_id = call.message.chat.id
    _, image_id = call.data.split('_')
    image_link = get_image(image_id)
    try:
        await bot.send_document(chat_id, image_link)
    except:
        await bot.send_message(chat_id, f'Скачай сам {image_link}')







if __name__ == '__main__':
    executor.start_polling(dp)
