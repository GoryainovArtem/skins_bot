from aiogram import types, Router
from aiogram.filters import CommandStart

# from ..keyboards.reply import store_kb, deals_kb, del_kb
# from app.keyboards.common_keyboard import item_type_select_kb
# from app.keyboards.inline import get_user_main_btns
from routers.menu_processing import get_menu_content
from keyboards.inline import MenuCallBack

user_private_router = Router()


@user_private_router.message(CommandStart())
async def cmd_start_handler(message: types.Message) -> None:
    media, reply_markup = await get_menu_content(level=0, menu_name="main")
    await message.answer_photo(media.media, caption=media.caption, reply_markup=reply_markup)


@user_private_router.callback_query(MenuCallBack.filter())
async def user_menu(callback: types.CallbackQuery, callback_data: MenuCallBack):
    print("Вызов хэндлера", callback_data)
    media, reply_markup = await get_menu_content(level=callback_data.level,
                                                 menu_name=callback_data.menu_name)
    await callback.message.edit_media(media, reply_markup=reply_markup)
    await callback.answer()


# @user_private_router.message(CommandStart())
# async def command_start_handler(message: types.Message) -> None:
#     text_msg = f"Добро пожаловать в {service_name}"
#     await message.answer(text_msg, reply_markup=start_kb)


# @user_private_router.message(Command("inventory"))
# async def store_command(message: types.Message) -> None:
#     await message.answer(text="Выберите интересующий раздел", reply_markup=del_kb)
#
#
# @user_private_router.message(Command(commands=("deals", )))
# async def store_command(message: types.Message) -> None:
#     await message.answer(text="Выберите интересующий раздел", reply_markup=deals_kb)
#
#
# @user_private_router.message(Command(commands=("store", )))
# async def store_command(message: types.Message) -> None:
#     await message.answer(text="Выберите интересующий раздел", reply_markup=store_kb)
#
#
# @user_private_router.message(Command(commands=("library", "other_categories")))
# async def store_command(message: types.Message) -> None:
#     await message.answer(text="Выберите интересующий раздел", reply_markup=item_type_select_kb)


# async def function(callback: types.CallbackQuery):
#     number = int(callback.data.split("_")[1])
#     await callback.message.edit_text(
#         text=f"Нажатия - {number}",
#         reply_markup=get_callback_btns({"Нажми еше раз": f"some_{number+1}"})
#     )
