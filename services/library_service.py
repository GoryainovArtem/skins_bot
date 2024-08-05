from aiogram.types import InputMediaPhoto

from keyboards.inline import get_library_btns, get_library_skins_buttons, get_library_card_buttons


async def library_menu(level: int, menu_name: str):
    """
    Сформировать разметку контента и кнопок для экрана 'Библиотека'.
    """
    image = InputMediaPhoto(media="https://www.bleepstatic.com/content/hl-images/2023/12/11/counter-strike-2.jpg",
                            caption="В библиотеке скинов доступна вся информация о предметах CS 2")
    library_kb = await get_library_btns(level=level, sizes=(1,))
    return image, library_kb


async def library_card(level: int, menu_name: str, category: int | None = None):
    """
    Сформировать разметку контента и кнопок для экрана 'Карточка объекта библиотеки'.
    """

    image = InputMediaPhoto(media="https://www.bleepstatic.com/content/hl-images/2023/12/11/counter-strike-2.jpg",
                            caption="В библиотеке скинов доступна вся информация о скинах CS 2")
    library_card_kb = await get_library_card_buttons(level=level, category=1, page=1, pagination_buttons={}, item_id=1,
                                                     sizes=(1,))

    return image, library_card_kb


async def library_skins(level: int, menu_name: str):
    """
    Сформировать разметку контента и кнопок для экрана 'Библиотека: скины'.
    """
    image = InputMediaPhoto(media="https://www.bleepstatic.com/content/hl-images/2023/12/11/counter-strike-2.jpg",
                            caption="В библиотеке скинов доступна вся информация о скинах CS 2")
    library_skins_kb = await get_library_skins_buttons(level=level, sizes=(2,))
    return image, library_skins_kb
