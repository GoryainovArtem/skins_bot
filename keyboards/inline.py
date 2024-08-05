import dataclasses

from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton
from aiogram.filters.callback_data import CallbackData


class MenuCallBack(CallbackData, prefix="menu"):
    level: int
    menu_name: str = ""
    page: int = 1
    item_id: int | None = None


async def get_library_skins_buttons(level: int, sizes: tuple[int] = (1, )):
    """
    Сформировать клавиатуру для экрана 'Библиотека: скины'.
    """
    keyboard = InlineKeyboardBuilder()

    core_buttons = {
        "Искать скин 🔍": "search_library_skin",
        "Оружие 💥": "weapons",
        "Ножи 🗡️": "knifes",
        "Перчатки 🧤": "gloves",
        "Коллекции 📦": "library_skin_collections",
        "⬅ В библиотеку": "back_lo_library"
    }

    for text, menu_name in core_buttons.items():
        if menu_name == "search_library_skin":
            keyboard.add(InlineKeyboardButton(
                text=text,
                callback_data=MenuCallBack(level=6,
                                           menu_name=menu_name
                                           ).pack()
            ))
        elif menu_name == "weapons":
            keyboard.add(InlineKeyboardButton(
                text=text,
                callback_data=MenuCallBack(level=8,
                                           menu_name=menu_name
                                           ).pack()
            ))

        elif menu_name == "knifes":
            keyboard.add(InlineKeyboardButton(
                text=text,
                callback_data=MenuCallBack(level=6,
                                           menu_name=menu_name
                                           ).pack()
            ))

        elif menu_name == "gloves":
            keyboard.add(InlineKeyboardButton(
                text=text,
                callback_data=MenuCallBack(level=6,
                                           menu_name=menu_name
                                           ).pack()
            ))

        elif menu_name == "library_skin_collections":
            keyboard.add(InlineKeyboardButton(
                text=text,
                callback_data=MenuCallBack(level=6,
                                           menu_name=menu_name
                                           ).pack()
            ))

        elif menu_name == "back_lo_library":
            keyboard.add(InlineKeyboardButton(
                text=text,
                callback_data=MenuCallBack(level=level - 1,
                                           menu_name=menu_name
                                           ).pack()
            ))

    return keyboard.adjust(*sizes).as_markup()


async def get_library_card_buttons(level: int,
                             category: int,
                             page: int,
                             pagination_buttons: dict,
                             item_id: int = 1,
                             sizes: tuple[int] = (1,)
                             ):
    keyboard = InlineKeyboardBuilder()

    keyboard.add(InlineKeyboardButton(text="Назад",
                                      callback_data=MenuCallBack(
                                          level=level-1,
                                          menu_name="library_back"
                                      ).pack())
                 )
    keyboard.add(InlineKeyboardButton(text="Подробнее",
                                      callback_data=MenuCallBack(
                                          level=10,
                                          menu_name="library_skin_detailed"
                                      ).pack())
                 )
    keyboard.add(InlineKeyboardButton(text="Статистика продаж",
                                      callback_data=MenuCallBack(
                                          level=level-1,
                                          menu_name="statistics"
                                      ).pack())
                 )

    core_buttons = {
        "Подробнее": "library_skin_detailed",
        "Статистика продаж": "library_skin_statistics"
    }

    # for text, menu_name in core_buttons.items():
    #     if menu_name == "library_skin_detailed":
    #         keyboard.add(InlineKeyboardButton(
    #             text=text,
    #             callback_data=MenuCallBack(level=...,
    #                                        menu_name=...,
    #                                        skin_id=...
    #                                        ).pack()
    #         ))

    return keyboard.adjust(*sizes).as_markup()


def get_user_main_btns(*, level: int, sizes: tuple[int] = (2, )):
    keyboard = InlineKeyboardBuilder()

    btns = {
        "Инвентарь": "inventory",
        "Сделки": "deals",
        "Магазин": "skins_store",
        "Библиотека": "library",
        "О нас": "about"
    }
    print("btns", btns.items())
    for text, menu_name in btns.items():
        if menu_name == "inventory":
            print("Отрисовка inventory")
            keyboard.add(InlineKeyboardButton(
                text=text,
                callback_data=MenuCallBack(level=1, menu_name=menu_name).pack()
            ))
        elif menu_name == "deals":
            print("Отрисовка deals")
            keyboard.add(InlineKeyboardButton(
                text=text,
                callback_data=MenuCallBack(level=2, menu_name=menu_name).pack()
            ))
        elif menu_name == "skins_store":
            print("Отрисовка skins_store")
            keyboard.add(InlineKeyboardButton(
                text=text,
                callback_data=MenuCallBack(level=3, menu_name=menu_name).pack()
            ))
        elif menu_name == "library":
            print("Отрисовка library")
            keyboard.add(InlineKeyboardButton(
                text=text,
                callback_data=MenuCallBack(level=4, menu_name=menu_name).pack()
            ))
        else:
            print("Отрисовка about")
            keyboard.add(InlineKeyboardButton(
                text=text,
                callback_data=MenuCallBack(level=level, menu_name=menu_name).pack()
            ))

    return keyboard.adjust(*sizes).as_markup()


async def get_library_btns(level: int, sizes: tuple[int] = (2,)):
    keyboard = InlineKeyboardBuilder()

    library_buttons = {
        "Скины": "library_skins",
        "Кейсы": "library_cases",
        "Стикеры": "library_stickers",
        "Назад": "library_back"
    }

    for text, menu_name in library_buttons.items():

        if menu_name == "library_skins":
            keyboard.add(InlineKeyboardButton(
                text=text,
                callback_data=MenuCallBack(
                    level=5,
                    menu_name=menu_name).pack())
            )
        elif menu_name == "library_cases":
            keyboard.add(InlineKeyboardButton(
                text=text,
                callback_data=MenuCallBack(
                    level=6,
                    menu_name=menu_name).pack())
            )
        elif menu_name == "library_stickers":
            keyboard.add(InlineKeyboardButton(
                text=text,
                callback_data=MenuCallBack(
                    level=7,
                    menu_name=menu_name).pack())
            )
        elif menu_name == "library_back":
            keyboard.add(InlineKeyboardButton(
                text=text,
                callback_data=MenuCallBack(
                    level=0,
                    menu_name="main").pack())
            )

    return keyboard.adjust(*sizes).as_markup()
