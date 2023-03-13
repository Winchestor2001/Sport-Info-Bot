from aiogram import Dispatcher
from aiogram.types import *

from api.backend_api import *
from loader import dp


async def bot_start(message: Message):
    user_id = message.from_user.id
    username = message.from_user.username
    await add_user_api(user_id, username)
    await message.answer(f"Salom")


def register_users_py(dp: Dispatcher):
    dp.register_message_handler(bot_start, commands=['start'])

