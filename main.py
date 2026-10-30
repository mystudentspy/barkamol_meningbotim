import asyncio
from aiogram import Bot, Dispatcher
from config.settings import BOT_TOKEN
from handlers.dise import rt as dise

dp = Dispatcher()
async def main():
    bot = Bot(BOT_TOKEN)
    dp.include_router(dise)

    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        print("Starting bot...")
        asyncio.run(main())
    except KeyboardInterrupt:
        print("bot to'xtadi")
print(5624)