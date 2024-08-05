import math

from aiogram import types

import requests
from typing import Sequence
from config import service_host, service_port
from keyboards.inline import get_library_card_buttons

def get_api_skins_list():
    url = f"http://{service_host}:{service_port}/skins/"
    response = requests.get(url, headers={"accept": "application/json"})
    return response.json()


class Paginator:
    """
    Класс для пагинации по списку объектов.
    """

    def __init__(self, items_list, items_per_page: int = 1):
        self.items_array = items_list
        self.current_page = 0
        self.items_per_page = items_per_page
        self.pages_amount = math.ceil(len(self.items_array) / self.items_per_page)

    def __get_slice(self):
        start = (self.current_page - 1) * self.items_per_page
        end = start + self.items_per_page
        return self.items_array[start:end]

    def get_page(self):
        page_items = self.__get_slice()
        return page_items

    def has_next_item(self):
        if self.current_page < self.pages_amount:
            return self.current_page + 1
        return False

    def has_prev_item(self):
        if self.current_page > 1:
            return self.current_page - 1
        return False


def get_pagination_buttons(paginator: Paginator):
    buttons = {}
    if paginator.has_next_item():
        buttons["След. >"] = "next"
    if paginator.has_prev_item():
        buttons["< Пред."] = "prev"
    return buttons


def get_items(level, category, page):
    """Получение пагинированных элементов."""

    skins_list = get_api_skins_list()
    paginator = Paginator(skins_list)
    item = paginator.get_page()[0]

    print("first item info", item)

    #  Создать картинку
    image = types.InputMediaPhoto(media="", caption="")

    pagination_buttons = get_pagination_buttons(paginator)

    keyboard = get_library_card_buttons(
        level=level,
        category="",
        pagination_buttons=pagination_buttons,
        item_id=item.get("id"),
    )

    return image, keyboard

