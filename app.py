import aioschedule
import asyncio

from aiogram import executor

from handlers.users.users import register_users_py
from loader import dp
import middlewares, filters, handlers
from utils.set_bot_commands import set_default_commands
from utils.misc.liga_parsers import laliga


async def liga_task():
    aioschedule.every(5).seconds.do(laliga)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


async def on_startup(dispatcher):
    await set_default_commands(dispatcher)

    register_users_py(dispatcher)

    asyncio.create_task(liga_task())


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
