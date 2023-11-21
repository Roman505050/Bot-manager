import os
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher

from handlers import basic,synchronizer

load_dotenv()
TOKEN = os.getenv('TOKEN')

async def start():
    bot = Bot(token=TOKEN,parse_mode='HTML')
    dp = Dispatcher()

    dp.include_routers(basic.router)

    await dp.start_polling(bot)