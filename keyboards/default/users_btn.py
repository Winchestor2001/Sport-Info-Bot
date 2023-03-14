from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup


async def start_menu_btn():
    btn = ReplyKeyboardMarkup(resize_keyboard=True)
    btn.row("🏆 Ligalar")
    btn.row("📑 Bot Xaqida", "⚙️ Til o`zgartirish")
    return btn

