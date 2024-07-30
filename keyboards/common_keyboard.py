from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


item_type_select_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="/all_categories")
        ],
        [
            KeyboardButton(text="/skins")
        ],
        [
            KeyboardButton(text="/cases")
        ],
        [
            KeyboardButton(text="/stickers")
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите подходяющую категорию предметов"
)
