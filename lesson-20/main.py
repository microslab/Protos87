import os

from keyboards import generate_language
import sqlite3
from pogoda import *

from dotenv import *
from aiogram import Bot, Dispatcher, executor
from aiogram import types
from aiogram.types import Message
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

load_dotenv()
TOKEN = os.getenv('TOKEN')
bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class Questions(StatesGroup):
    one = State()
    two = State()


@dp.message_handler(commands=['start', 'help', 'about', 'history'])
async def command_start(message: Message):
    if message.text == '/start':
        await message.answer('Здравствуйте, вас приветствует бот Погоды\nВведите название города')
        await start_questions(message)
    elif message.text == '/help':
        await message.answer('Если у вас возникли проблемы то есть команды /start, /about, /history')
    elif message.text == '/about':
        await message.answer('Данный бот был создан в учебных целях micros')
        await start_questions(message)
    elif message.text == '/history':
        await get_history(message)


async def get_history(message):
    chat_id = message.chat.id
    database = sqlite3.connect('bot.db')
    cursor = database.cursor()

    cursor.execute('''
    SELECT city_name, description, temp, wind, sunrise, sunset FROM history
    WHERE telegram_id = ?
    ''', (chat_id,))

    history = cursor.fetchall()
    history = history[::-1]
    for city_name, description, temp, wind, sunrise, sunset in history[:10]:
        await bot.send_message(chat_id, f'''Вы запрашивали погоду в:
В городе {city_name} сейчас {description}
Температура: {temp} ℃\nСкорость ветра: {wind} м/c
Рассвет: {sunrise}\nЗакат: {sunset}
''')

    database.close()
    await start_questions(message)


@dp.message_handler(content_types=['text'], state=Questions.one)
async def start_questions(message: types.Message):
    await Questions.one.set()
    await message.answer('Введите город, в котором хотите узнать погоду:', reply_markup=generate_language())
    await Questions.next()


@dp.message_handler(content_types=['text'], state=Questions.two)
async def Ppogoda22(message: Message, state: FSMContext):
    if message.text in ['/help', '/about', '/history']:
        await state.finish()
        await command_start(message)
    else:
        pogodas(message.text)
        data_pogoda = pogodas(message.text)
        await message.answer(f'''В городе {data_pogoda["city_name"]} сейчас {data_pogoda["description"]}
Температура: {data_pogoda["temp"]} ℃\nСкорость ветра: {data_pogoda["wind"]} м/c
Рассвет: {data_pogoda["sunrise"]}\nЗакат: {data_pogoda["sunset"]}''', reply_markup=generate_language())
        chat_id = message.chat.id
        database = sqlite3.connect('bot.db')
        cursor = database.cursor()
        cursor.execute('''
        INSERT INTO history(telegram_id, city_name, description, temp, wind, sunrise, sunset)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (chat_id, data_pogoda["city_name"], data_pogoda["description"], data_pogoda["temp"], data_pogoda["wind"], data_pogoda["sunrise"], data_pogoda["sunset"]))
        database.commit()
        database.close()
        await state.finish()
        await start_questions(message)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
