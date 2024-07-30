from aiogram import types, Router
from aiogram.filters import CommandStart, Command
from aiogram import F

from keyboards.reply import start_kb, store_kb, deals_kb, del_kb
from keyboards.common_keyboard import item_type_select_kb
from config import service_name


user_private_router = Router()


@user_private_router.message(CommandStart())
async def command_start_handler(message: types.Message) -> None:
    text_msg = f"Добро пожаловать в {service_name}"
    await message.answer(text_msg, reply_markup=start_kb)


@user_private_router.message(Command("inventory"))
async def store_command(message: types.Message) -> None:
    await message.answer(text="Выберите интересующий раздел", reply_markup=del_kb)


@user_private_router.message(Command(commands=("deals", )))
async def store_command(message: types.Message) -> None:
    await message.answer(text="Выберите интересующий раздел", reply_markup=deals_kb)


@user_private_router.message(Command(commands=("store", )))
async def store_command(message: types.Message) -> None:
    await message.answer(text="Выберите интересующий раздел", reply_markup=store_kb)


@user_private_router.message(Command(commands=("library", "other_categories")))
async def store_command(message: types.Message) -> None:
    await message.answer(text="Выберите интересующий раздел", reply_markup=item_type_select_kb)
