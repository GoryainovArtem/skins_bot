from aiogram import Router
from aiogram import types
from aiogram.filters import Command

from managers import api_manager

deal_router = Router()


@deal_router.message(Command(""))
async def cmd_skins_handler(message: types.Message) -> None:
    """
    Обработчик команды /skins для получения информации обо
    всех существующих скинах на оружие, ножи и перчатки.
    """
    skins_list = api_manager.get_skins_list()
    await message.answer(str(skins_list))
