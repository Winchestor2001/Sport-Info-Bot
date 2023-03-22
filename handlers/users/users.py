import datetime
import json
import os

from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import *

from api.backend_api import *
from data.config import BOT_USERNAME
from keyboards.default.users_btn import start_menu_btn, settings_btn, remove_btn, cancel_btn, langs
from keyboards.inline.users_btn import liga_btn, liga_info_btn, choose_lang_btn, choose_teams_btn, tours_btn, back_btn, \
    edit_my_team_btn
from utils.misc.draw_img import draw_table
from utils.misc.usefull_funcs import get_text_ratio, check_user_selected_liga, make_tour_context, make_top_teams_context
from context import context
from states.AllStates import UserStates


async def bot_start(message: Message, state: FSMContext):
    user_id = message.from_user.id
    username = message.from_user.username
    await add_user_api(user_id, username)
    user = await get_user_info_api(user_id)

    if user['team'] is None:
        await message.answer(context[user['language']]['select_team'])
        await state.update_data(lang=user['language'])
        await UserStates.select_team.set()
        return
    btn = await start_menu_btn(user['language'])
    text = context[user['language']]['start_text']
    await message.answer(text, reply_markup=btn)


async def show_liga_handler(message: Message):
    user_id = message.from_user.id
    user = await get_user_info_api(user_id)
    liga = await get_liga_api()
    btn = await liga_btn(liga)
    text = context[user['language']]['ligs']
    await message.answer(text, reply_markup=btn)


async def show_liga_info_callback(c: CallbackQuery):
    user_id = c.from_user.id
    cd = c.data.split(":")[-1]
    user = await get_user_info_api(user_id)
    text = await check_user_selected_liga(c.message.reply_markup.inline_keyboard, c.data)
    btn = await liga_info_btn(cd, user['language'])
    await c.message.edit_text(text, reply_markup=btn)


async def back_liga_callback(c: CallbackQuery):
    user_id = c.from_user.id
    liga = await get_liga_api()
    user = await get_user_info_api(user_id)
    btn = await liga_btn(liga)
    text = context[user['language']]['ligs']
    await c.message.edit_text(text, reply_markup=btn)


async def show_teams_callback(c: CallbackQuery):
    await c.answer()
    user_id = c.from_user.id
    user = await get_user_info_api(user_id)
    cd = c.data.split(":")[-1]
    teams = await get_liga_table_api(int(cd))
    table_img = await draw_table(teams, context[user['language']]['team'])
    old_text = c.message.text
    old_btn = c.message.reply_markup
    today = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')

    await c.message.delete()
    await c.message.answer_photo(InputFile(table_img), caption=f"🕰 {today}")
    await c.message.answer(old_text, reply_markup=old_btn)
    os.unlink(table_img)


async def settings_handler(message: Message):
    user_id = message.from_user.id
    user = await get_user_info_api(user_id)
    btn = await settings_btn(user['language'])
    text = context[user['language']]['settings']
    await message.answer(text, reply_markup=btn)


async def change_language_handler(message: Message):
    user_id = message.from_user.id
    user = await get_user_info_api(user_id)
    btn = await choose_lang_btn()
    await message.answer(context[user['language']]['choose_lang'], reply_markup=btn)


async def selected_lang_callback(c: CallbackQuery):
    await c.answer()
    user_id = c.from_user.id
    lang = c.data.split(":")[-1]
    await update_user_lang_api(user_id, lang)
    await c.message.delete()
    lang = await get_user_info_api(user_id)
    btn = await start_menu_btn(lang['language'])
    text = context[lang['language']]['start_text']
    await c.message.answer(text, reply_markup=btn)


async def select_team_state(message: Message, state: FSMContext):
    team = message.text
    teams = await get_teams_api()
    lang = await state.get_data()
    check_team = await get_text_ratio(teams, team)
    if check_team:
        btn = await choose_teams_btn(check_team)
        await message.answer(context[lang['lang']]['search_result'], reply_markup=btn)
        await state.finish()
    else:
        await message.answer(context[lang['lang']]['invalid_team'])


async def selected_team_callback(c: CallbackQuery):
    await c.answer()
    user_id = c.from_user.id
    team = c.data.split(":")[-1]
    await update_user_team_api(user_id, team)

    user = await get_user_info_api(user_id)
    await c.message.edit_text(context[user['language']]['team_save'])
    btn = await start_menu_btn(user['language'])
    text = context[user['language']]['start_text']
    await c.message.answer(text, reply_markup=btn)


async def liga_tours_callback(c: CallbackQuery, state: FSMContext):
    await c.answer()
    user_id = c.from_user.id
    liga = c.data.split(":")[-1]
    user = await get_user_info_api(user_id)
    tours = await get_liga_tours_api(liga)
    tours = list({v['tour']: v for v in tours}.values())
    await state.update_data(liga=liga)
    btn = await tours_btn(len(tours))
    await c.message.edit_text(context[user['language']]['select_tour'], reply_markup=btn)


async def selected_tour_calback(c: CallbackQuery, state: FSMContext):
    await c.answer()
    user_id = c.from_user.id
    cd = c.data.split(":")[-1]
    liga = await state.get_data()
    user = await get_user_info_api(user_id)
    tour = await get_liga_tour_api(liga['liga'], cd)
    tour = json.loads(tour)
    text = await make_tour_context(tour, context[user['language']]['tour_lang']) + f"\n{BOT_USERNAME}"
    btn = await back_btn(liga['liga'])
    await c.message.edit_text(text, reply_markup=btn)


async def show_top_teams_handler(message: Message):
    top_teams = await get_top_teams_api()
    text = await make_top_teams_context(top_teams)
    await message.answer(text)


async def show_my_team_handler(message: Message, state: FSMContext):
    user_id = message.from_user.id
    user = await get_user_info_api(user_id)
    text = context[user['language']]['my_team'].format(user['team'])
    btn = await edit_my_team_btn(user['language'], user_id)
    await message.answer(text, reply_markup=btn)
    await state.update_data(
        lang=user['language']
    )


async def edit_my_team_callback(c: CallbackQuery, state: FSMContext):
    await c.answer()
    async with state.proxy() as data:
        data['user_id'] = c.data.split(":")[-1]
        lang = data['lang']

    await c.message.delete()
    btn = await cancel_btn(lang)
    await c.message.answer(context[lang]['select_team'], reply_markup=btn)
    await UserStates.edit_team.set()


async def edit_team_state(message: Message, state: FSMContext):
    user = await state.get_data()
    text = message.text
    if text == langs[user['lang']]['cancel']:
        btn = await settings_btn(user['lang'])
        text = context[user['lang']]['settings']
        await message.answer(text, reply_markup=btn)
        await state.finish()
        return
    else:
        teams = await get_teams_api()
        lang = await state.get_data()
        check_team = await get_text_ratio(teams, text)
        if check_team:
            btn = await choose_teams_btn(check_team)
            await message.answer(context[lang['lang']]['search_result'], reply_markup=btn)
            await state.finish()
        else:
            await message.answer(context[lang['lang']]['invalid_team'])


def register_users_py(dp: Dispatcher):
    dp.register_message_handler(bot_start, commands=['start'])
    dp.register_message_handler(show_liga_handler, text='🏆 Ligalar')
    dp.register_message_handler(show_liga_handler, text='🏆 Лиги')
    dp.register_message_handler(settings_handler, text='⚙️ Sozlamalar')
    dp.register_message_handler(settings_handler, text='⚙️ Настройки')
    dp.register_message_handler(change_language_handler, text='🌐 Tilni o`zgartirish')
    dp.register_message_handler(change_language_handler, text='🌐 Изменить язык')
    dp.register_message_handler(bot_start, text='🔙 Назад')
    dp.register_message_handler(bot_start, text='🔙 Ortga')
    dp.register_message_handler(show_top_teams_handler, text='🥇 Top jamoalar')
    dp.register_message_handler(show_top_teams_handler, text='🥇 Топ команды')
    dp.register_message_handler(show_my_team_handler, text='⚽️ Mening Jamoam')
    dp.register_message_handler(show_my_team_handler, text='⚽️ Мой клуб')

    dp.register_message_handler(select_team_state, state=UserStates.select_team, content_types=['text'])
    dp.register_message_handler(edit_team_state, state=UserStates.edit_team, content_types=['text'])

    dp.register_callback_query_handler(back_liga_callback, text='back_liga')
    dp.register_callback_query_handler(selected_team_callback, text_contains='selected_team:')
    dp.register_callback_query_handler(show_liga_info_callback, text_contains='liga:')
    dp.register_callback_query_handler(show_teams_callback, text_contains='teams:')
    dp.register_callback_query_handler(selected_lang_callback, text_contains='lang:')
    dp.register_callback_query_handler(selected_tour_calback, text_contains='tour_is:')
    dp.register_callback_query_handler(liga_tours_callback, text_contains='tours:')
    dp.register_callback_query_handler(edit_my_team_callback, text_contains='edit_team:')
