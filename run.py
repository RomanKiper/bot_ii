from aiogram import Bot, Dispatcher
import os
import asyncio
from dotenv import load_dotenv

async def main():
    load_dotenv()
    bot = Bot(token=os.getenv('TOKEN'))
    dp = Dispatcher()
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
        print("БОТ ВКЛЮЧЕН")
    except KeyboardInterrupt:
        print("БОТ ВЫКЛЮЧЕН")
