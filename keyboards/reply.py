from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="/inventory")
        ],
        [
            KeyboardButton(text="/deals")
        ],
        [
            KeyboardButton(text="/store")
        ],
        [
            KeyboardButton(text="/library"),
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Что вас интересует?"
)


deals_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Подтверждение покупки"),
            KeyboardButton(text="Товары на продаже"),
            KeyboardButton(text="История покупок"),
            KeyboardButton(text="Заказать покупку")

        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Что вас интересует?"
)


store_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="/all_items"),
            KeyboardButton(text="Оценить стоимость предмета")
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder="Что вас интересует?"
)


del_kb = ReplyKeyboardRemove()