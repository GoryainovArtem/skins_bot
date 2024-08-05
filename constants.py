class Constants:
    MAIN_MANU_LEVEL = 0
    INVENTORY_LEVEL = 1
    DEALS_LEVEL = 2
    STORE_LEVEL = 3
    LIBRARY_LEVEL = 4
    LIBRARY_SKINS_LEVEL = 5
    LIBRARY_CASES_LEVEL = 6
    LIBRARY_STICKERS_LEVEL = 7
    LIBRARY_CARD_LEVEL = 8
    LIBRARY_SEARCH_SKIN_LEVEL = 11
    LIBRARY_ITEMS_LEVEL = 9
    LIBRARY_COLLECTIONS_LEVEL = 10

    @staticmethod
    def as_dict() -> dict[int, str]:
        """
        Вернуть словарь с сопоставлением всех номеров уровней
        и аттрибутов класса.
        """
        return {attr_value:attr_name for attr_name, attr_value in Constants.__dict__.items() if "LEVEL" in attr_name}
