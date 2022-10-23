import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from routers.becktestrouter import router
import os

TOKEN = os.getenv('BotToken')

async def main():
    logging.basicConfig(level="INFO")
    bot = Bot(TOKEN, parse_mode='HTML')
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())