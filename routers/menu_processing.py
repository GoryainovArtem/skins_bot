from constants import Constants
from services.library_service import library_menu, library_card, library_skins
from services.main_menu_service import main_menu


async def get_menu_content(level: int, menu_name: str, item_category: int | None = None):
    """
    Получить разметку для отображения контента и кнопок
    для уровня.
    """

    level_functions = {
        Constants.MAIN_MANU_LEVEL: main_menu,
        Constants.INVENTORY_LEVEL: ...,
        Constants.DEALS_LEVEL: ...,
        Constants.STORE_LEVEL: ...,
        Constants.LIBRARY_LEVEL: library_menu,
        Constants.LIBRARY_SKINS_LEVEL: library_skins,
        Constants.LIBRARY_CARD_LEVEL: library_card
    }

    return await level_functions[level](level, menu_name)


    #     return await main_menu(level, menu_name)
    # elif level == Constants.INVENTORY_LEVEL:
    #     return await inventory_menu(level, menu_name)
    #
    # elif level == Constants.LIBRARY_LEVEL:
    #     return await library_menu(level, menu_name)
    # elif level == Constants.LIBRARY_LEVEL:
    #     return await library_menu(level, menu_name)
    # elif level == Constants.LIBRARY_LEVEL:
    #     return await library_menu(level, menu_name)
    # elif level == 5:
    #     return await library_skins(level)
    # elif level == 8:
    #     return await library_card(level, menu_name)
    # # elif level == 5:
    #     return await library_card(level, menu_name, category)
