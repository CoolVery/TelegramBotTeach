import asyncio
import os

from aiogram import Bot, Dispatcher, F
from dotenv import load_dotenv

from config import TOKEN
from app.handlers import router

async def main():
    load_dotenv()
    #Bot - это сам экземпляр нашего бота
    bot = Bot(token=os.getenv('TOKEN'))
    #Dispatcher - Главный роутер, через него все происходит
    dp = Dispatcher()
    #Подключаем роутер к диспетчеру
    dp.include_router(router)
    #Эта функция отправляет запросы тг серверам и возвращает ответы
    await dp.start_polling(bot)

if __name__ == '__main__':
    #Это для завершении работы бота
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')