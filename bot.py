import asyncio
from config import config
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
import handlers  # главный router, который собирает все хэндлеры

async def main():
    # создаём объект бота
    bot = Bot(token=config['bot']['token'])

    # создаём диспетчер
    dp = Dispatcher()

    # подключаем главный router (все user/admin хэндлеры)
    dp.include_router(handlers.router)

    # (опционально) задаём команды бота в Telegram
    commands = [
        BotCommand(command="start", description="Запустить бота"),
        # добавляй другие команды
    ]
    await bot.set_my_commands(commands)

    # запускаем polling
    try:
        print("Бот запущен...")
        await dp.start_polling(bot)
    finally:
        # корректно закрываем соединение
        await bot.session.close()


# точка входа
if __name__ == "__main__":
    asyncio.run(main())
