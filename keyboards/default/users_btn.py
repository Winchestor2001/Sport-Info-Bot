from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup

remove_btn = ReplyKeyboardRemove()

langs = {
    'uz': {
        'liga': '🏆 Ligalar', 'about': '📑 Bot Xaqida', 'settings': '⚙️ Sozlamalar',
        'lang': '🌐 Tilni o`zgartirish', 'my_team': '⚽️ Mening Jamoam', 'back': '🔙 Ortga',
        'top_teams': '🥇 Top jamoalar', 'cancel': '❌ Bekor qilish',
    },
    'ru': {
        'liga': '🏆 Лиги', 'about': '📑 О боте', 'settings': '⚙️ Настройки',
        'lang': '🌐 Изменить язык', 'my_team': '⚽️ Мой клуб', 'back': '🔙 Назад',
        'top_teams': '🥇 Топ команды', 'cancel': '❌ Отменить',
    },
}


async def start_menu_btn(lang: str):
    btn = ReplyKeyboardMarkup(resize_keyboard=True)
    btn.row(langs[lang]['liga'])
    btn.row(langs[lang]['top_teams'])
    btn.row(langs[lang]['about'], langs[lang]['settings'])
    return btn


async def settings_btn(lang: str):
    btn = ReplyKeyboardMarkup(resize_keyboard=True)
    btn.row(langs[lang]['lang'], langs[lang]['my_team'])
    btn.row(langs[lang]['back'])
    return btn


async def cancel_btn(lang: str):
    btn = ReplyKeyboardMarkup(resize_keyboard=True)
    btn.row(langs[lang]['cancel'])
    return btn

