from aiogram import Router
from aiogram.filters import Command
from aiogram import types

from managers import api_manager
from utils.file_utils import read_html_file
from utils.message_templates import card_content
from keyboards.pagination_keyboard import pagination_kb
from keyboards.reply import del_kb
from keyboards.library_keyboard import detailed_kb

library_router = Router()


def format_library_skin_card_data(card_template: str, data) -> str:
    print("data", data)
    format_template = {
        "name_eng": data["name_rus"],
        "name_rus": data["name_eng"],
        "description": "Тестовое описание",
        "game_item_type": data.get("game_item").get("game_item_type", {}).get("name_rus"),
        "case_name": data.get("case_type", {}).get("name_rus"),
        "stattrack_available": "Да",  # Временное решение
    }
    return card_template.format(**format_template)


@library_router.message(Command("skins"))
async def cmd_all_handler(message: types.Message) -> None:
    card_content_list = api_manager.get_skins_list()
    caption_template = '''
        <b>{name_eng}</b>\n
        <b>{name_rus}</b>\n
        <i>{description}</i>\n
        Тип оружия: {game_item_type}\n
        Кейс: {case_name}\n
        Stattrack: {stattrack_available}\n
    '''

    for card_data in card_content_list[:5]:
        caption = format_library_skin_card_data(caption_template, card_data)
                                          # title_eng="AK-47 Wasteland rebel",
                                          # title_rus="AK-47 Пустынный повстанец",
                                          # description="Описание",
                                          # item_type="Винтовка",
                                          # case_name="Кейс операции Браво",
                                          # stattrack_available="Да")
        await message.answer_photo(
            photo="https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_ak47_cu_tribute_ak47_light_large.f0ccfeea8a432a82cf4fb7f0411a724dbb43459a.png",
            caption=caption,
            reply_markup=pagination_kb
        )
