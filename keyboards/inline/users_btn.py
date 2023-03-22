from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


langs = {
    'uz': {
        'teams': '📊 Jamoalar Jadvali', 'players': '⚽️ To`p urarlar', 'back': '🔙 Ortga',
        'tours': '🔢 Turlar', 'edit_my_team': '✏️ Jamoani o`zgartirish',
    },
    'ru': {
        'teams': '📊 Таблица команд', 'players': '⚽️ Бомбардиры', 'back': '🔙 Назад',
        'tours': '🔢 Туры', 'edit_my_team': '✏️ Изменить команду',
    },
}


async def liga_btn(data):
    btn = InlineKeyboardMarkup(row_width=2)
    btn.add(
        *[InlineKeyboardButton(f"{item['stiker']} {item['name']}", callback_data=f"liga:{item['id']}") for item in data],
    )
    return btn


async def liga_info_btn(liga, lang):
    btn = InlineKeyboardMarkup(row_width=2)
    btn.row(
        InlineKeyboardButton(langs[lang]['teams'], callback_data=f"teams:{liga}"),
        InlineKeyboardButton(langs[lang]['players'], callback_data=f"players:{liga}"),
    )
    btn.row(
        InlineKeyboardButton(langs[lang]['tours'], callback_data=f"tours:{liga}"),
    )
    btn.row(
        InlineKeyboardButton(langs[lang]['back'], callback_data=f"back_liga"),
    )
    return btn


async def choose_lang_btn():
    btn = InlineKeyboardMarkup(row_width=2)
    btn.add(
        InlineKeyboardButton("🇺🇿", callback_data="lang:uz"),
        InlineKeyboardButton("🇷🇺", callback_data="lang:ru"),
    )
    return btn


async def choose_teams_btn(teams):
    btn = InlineKeyboardMarkup(row_width=2)
    btn.add(
        *[InlineKeyboardButton(f"{team}", callback_data=f"selected_team:{team}") for team in teams]
    )
    return btn


async def tours_btn(tours: int):
    btn = InlineKeyboardMarkup(row_width=5)
    btn.add(
        *[InlineKeyboardButton(f"{tour} тур", callback_data=f"tour_is:{tour}") for tour in range(1, tours+1)]
    )
    btn.row(
        InlineKeyboardButton("🔙", callback_data=f"back_liga"),
    )
    return btn


async def back_btn(liga):
    btn = InlineKeyboardMarkup()
    btn.add(
        InlineKeyboardButton("🔙", callback_data=f"tours:{liga}"),
    )
    return btn


async def edit_my_team_btn(lang, user_id):
    btn = InlineKeyboardMarkup()
    btn.add(
        InlineKeyboardButton(langs[lang]['edit_my_team'], callback_data=f"edit_team:{user_id}")
    )
    return btn



