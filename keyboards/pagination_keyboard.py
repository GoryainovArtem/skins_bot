from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

pagination_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="/prev_skins"),
            KeyboardButton(text="/next_skins")
        ],
        [
            KeyboardButton(text="/other_categories")
        ]
    ],
    resize_keyboard=True
)