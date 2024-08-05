from aiogram.types import InputMediaPhoto

from keyboards.inline import get_user_main_btns


async def main_menu(level: int, menu_name: str, ):

    # menu_name - для передачи в url и получения картинки из s3
    image = InputMediaPhoto(media="https://www.bleepstatic.com/content/hl-images/2023/12/11/counter-strike-2.jpg",
                            caption="Welcome to CSInvest")

    # Необходим способ хранения картинок:
    # S3 + url ссылка до картинки
    # или
    # Сохранить на сервере Telegram
    menu_kb = get_user_main_btns(level=level)
    return image, menu_kb