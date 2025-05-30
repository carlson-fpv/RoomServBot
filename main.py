import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from handlers import router
import config


async def main():
	# Создаём объект Бота с HTML разметкой и объект Диспетчера
	bot = Bot(token=config.BOT_TOKEN, parse_mode=ParseMode.HTML)
	dp = Dispatcher(storage=MemoryStorage())
	# Прдключаем к Диспетчеру обработчики router
	dp.include_router(router)

	# Удаляем обновления, пришедшие после завершения работы бота
	await bot.delete_webhook(drop_pending_updates=True)

	# Запускаем бота на поллингах
	await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
	# Запуск логгирования
	logging.basicConfig(level=logging.INFO)

	# Асинхронный запуск инициализации бота
	asyncio.run(main())
