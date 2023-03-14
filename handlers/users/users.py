from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import *

from api.backend_api import *
from keyboards.default.users_btn import start_menu_btn
from keyboards.inline.users_btn import liga_btn, liga_info_btn
from utils.misc.draw_img import draw_table


async def bot_start(message: Message):
    user_id = message.from_user.id
    username = message.from_user.username
    await add_user_api(user_id, username)
    btn = await start_menu_btn()
    await message.answer(f"Salom", reply_markup=btn)


async def show_liga_handler(message: Message):
    liga = await get_liga_api()
    btn = await liga_btn(liga)
    await message.answer("🏆 Ligalar:", reply_markup=btn)


async def show_liga_info_callback(c: CallbackQuery):
    cd = c.data.split(":")[-1]
    btn = await liga_info_btn(cd)
    await c.message.edit_text("🇪🇸 LaLiga:", reply_markup=btn)


async def back_liga_callback(c: CallbackQuery):
    liga = await get_liga_api()
    btn = await liga_btn(liga)
    await c.message.edit_text("🏆 Ligalar:", reply_markup=btn)


async def show_teams_callback(c: CallbackQuery):
    await c.answer()
    cd = c.data.split(":")[-1]
    teams = await get_liga_table_api(int(cd))
    table_img = await draw_table(teams)


def register_users_py(dp: Dispatcher):
    dp.register_message_handler(bot_start, commands=['start'])
    dp.register_message_handler(show_liga_handler, text='🏆 Ligalar')

    dp.register_callback_query_handler(back_liga_callback, text='back_liga')
    dp.register_callback_query_handler(show_liga_info_callback, text_contains='liga:')
    dp.register_callback_query_handler(show_teams_callback, text_contains='teams:')

