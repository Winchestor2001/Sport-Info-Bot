from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup


langs = {
    'uz': {
        'liga': '🏆 Ligalar', 'about': '📑 Bot Xaqida', 'settings': '⚙️ Sozlamalar',
        'lang': '🌐 Tilni o`zgartirish', 'my_team': '⚽️ Mening Jamoam', 'back': '🔙 Ortga'
    },
    'ru': {
        'liga': '🏆 Лиги', 'about': '📑 О боте', 'settings': '⚙️ Настройки',
        'lang': '🌐 Изменить язык', 'my_team': '⚽️ Мой клуб', 'back': '🔙 Назад'
    },
}


async def start_menu_btn(lang: str):
    btn = ReplyKeyboardMarkup(resize_keyboard=True)
    btn.row(langs[lang]['liga'])
    btn.row(langs[lang]['about'], langs[lang]['settings'])
    return btn


async def settings_btn(lang: str):
    btn = ReplyKeyboardMarkup(resize_keyboard=True)
    btn.row(langs[lang]['lang'], langs[lang]['my_team'])
    btn.row(langs[lang]['back'])
    return btn

