import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from aiogram import executor

from handlers.users.users import register_users_py
from loader import dp
import middlewares, filters, handlers
from utils.set_bot_commands import set_default_commands
from utils.misc.liga_parsers import laliga


scheduler = AsyncIOScheduler(timezone='Asia/Tashkent')


async def on_startup(dispatcher):
    await set_default_commands(dispatcher)

    register_users_py(dispatcher)
    scheduler.add_job(laliga, trigger='interval', seconds=10)


if __name__ == '__main__':
    scheduler.start()
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
