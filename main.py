import asyncio
from aiogram import Bot, Dispatcher
from handlers import user

async def main():
    bot = Bot(token='8738202781:AAGyUhiO4vJndwj8X2p_03vdxhnRfxYiGWI')
    dp = Dispatcher()
    dp.include_router(user)  # ← просто user, без .user
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass