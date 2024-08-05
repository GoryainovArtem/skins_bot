from aiogram import Router, types
from aiogram.filters import Command

store_router = Router()


@store_router.message(Command("all_items"))
async def command_all_items_handler(message: types.Message) -> None:

    await message.answer("Привет")
