from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command


# Cоздадим объект Роутера
router = Router()


# Декоратор обеспечивает фильтрацию по полученному сообщению
@router.message(Command("start"))
# Асинхронный вызов ответа на команду "/start"
async def start_handler(msg: Message):
    await msg.answer("Привет! Пока что я глупый эхо-бот для отладки :)")


@router.message()
# Асинхронный вызов ответа на любое сообщение (отсутствует фильтр в декораторе)
async def message_handler(msg: Message):
    await msg.answer(msg.text)

