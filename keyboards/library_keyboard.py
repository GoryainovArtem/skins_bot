from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


detailed_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="/detailed_skin_info")
    ]
],
    resize_keyboard=True
)
