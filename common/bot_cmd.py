from aiogram.types import BotCommand

private_cmds = [
    BotCommand(command="start", description="Стартовая команда"),
    BotCommand(command="inventory", description="Мой инвентарь"),
    BotCommand(command="deals", description="Мои сделки"),
    BotCommand(command="store", description="Магазин предметов"),
    BotCommand(command="library", description="Библиотека скинов"),
    BotCommand(command="menu", description="Посмотреть меню"),
    BotCommand(command="about", description="Описание бота")
]