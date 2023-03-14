from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def liga_btn(data):
    btn = InlineKeyboardMarkup(row_width=2)
    btn.add(
        *[InlineKeyboardButton(f"{item['stiker']} {item['name']}", callback_data=f"liga:{item['id']}") for item in data]
    )
    return btn


async def liga_info_btn(liga):
    btn = InlineKeyboardMarkup(row_width=2)
    btn.add(
        InlineKeyboardButton("Jamoalar Jadvali", callback_data=f"teams:{liga}"),
        InlineKeyboardButton("O`yinchilar Jadvali", callback_data=f"players:{liga}"),
        InlineKeyboardButton("Ortga", callback_data=f"back_liga"),
    )
    return btn

