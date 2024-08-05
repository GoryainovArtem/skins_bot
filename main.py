import asyncio

from aiogram import Bot, Dispatcher
from aiogram.types.bot_command_scope_all_private_chats import BotCommandScopeAllPrivateChats
from aiogram.enums import ParseMode
from aiogram.client.bot import DefaultBotProperties

from config import access_token
from routers.common_router import user_private_router
# from app.routers.store_router import store_router
# from app.routers.library_router import library_router
from common.bot_cmd import private_cmds


dp = Dispatcher()
dp.include_router(user_private_router)
# dp.include_router(store_router)
# dp.include_router(library_router)


async def main():
    bot = Bot(access_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await bot.set_my_commands(commands=private_cmds,
                              scope=BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
