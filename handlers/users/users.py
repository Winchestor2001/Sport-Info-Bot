import datetime
import os

from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import *

from api.backend_api import *
from keyboards.default.users_btn import start_menu_btn, settings_btn
from keyboards.inline.users_btn import liga_btn, liga_info_btn
from utils.misc.draw_img import draw_table
from utils.misc.usefull_funcs import get_text_ratio, check_user_selected_liga
from context import context


async def bot_start(message: Message):
    user_id = message.from_user.id
    username = message.from_user.username
    await add_user_api(user_id, username)
    lang = await get_user_lang_api(user_id)
    btn = await start_menu_btn(lang['language'])
    text = context[lang['language']]['start_text']
    await message.answer(text, reply_markup=btn)
    await get_text_ratio('Barcelona', 'Barselona')


async def show_liga_handler(message: Message):
    user_id = message.from_user.id
    user = await get_user_lang_api(user_id)
    liga = await get_liga_api()
    btn = await liga_btn(liga)
    text = context[user['language']]['ligs']
    await message.answer(text, reply_markup=btn)


async def show_liga_info_callback(c: CallbackQuery):
    user_id = c.from_user.id
    cd = c.data.split(":")[-1]
    user = await get_user_lang_api(user_id)
    text = await check_user_selected_liga(c.message.reply_markup.inline_keyboard, c.data)
    btn = await liga_info_btn(cd, user['language'])
    await c.message.edit_text(text, reply_markup=btn)


async def back_liga_callback(c: CallbackQuery):
    user_id = c.from_user.id
    liga = await get_liga_api()
    user = await get_user_lang_api(user_id)
    btn = await liga_btn(liga)
    text = context[user['language']]['ligs']
    await c.message.edit_text(text, reply_markup=btn)


async def show_teams_callback(c: CallbackQuery):
    await c.answer()
    user_id = c.from_user.id
    user = await get_user_lang_api(user_id)
    cd = c.data.split(":")[-1]
    teams = await get_liga_table_api(int(cd))
    table_img = await draw_table(teams, context[user['language']]['team'])
    old_text = c.message.text
    old_btn = c.message.reply_markup
    today = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')

    await c.message.delete()
    await c.message.answer_photo(InputFile(table_img), caption=f"{today}")
    await c.message.answer(old_text, reply_markup=old_btn)
    os.unlink(table_img)


async def settings_handler(message: Message):
    user_id = message.from_user.id
    user = await get_user_lang_api(user_id)
    btn = await settings_btn(user['language'])
    text = context[user['language']]['settings']
    await message.answer(text, reply_markup=btn)


def register_users_py(dp: Dispatcher):
    dp.register_message_handler(bot_start, commands=['start'])
    dp.register_message_handler(show_liga_handler, text='🏆 Ligalar')
    dp.register_message_handler(settings_handler, text='⚙️ Sozlamalar')
    dp.register_message_handler(bot_start, text='🔙 Назад')
    dp.register_message_handler(bot_start, text='🔙 Ortga')

    dp.register_callback_query_handler(back_liga_callback, text='back_liga')
    dp.register_callback_query_handler(show_liga_info_callback, text_contains='liga:')
    dp.register_callback_query_handler(show_teams_callback, text_contains='teams:')
