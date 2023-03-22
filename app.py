import asyncio
from aiogram import executor
from handlers.users.users import register_users_py
from loader import dp, bot
import middlewares, filters, handlers
from utils.set_bot_commands import set_default_commands
from schedule_tasks import *


async def on_startup(dispatcher):
    await set_default_commands(dispatcher)

    register_users_py(dispatcher)
    tasks()


if __name__ == '__main__':
    scheduler.start()
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
