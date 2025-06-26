from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
from config import TOKEN
from handlers import register_handlers

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

register_handlers(dp)

if __name__ == "__main__":
    print("Bot is starting...")
    executor.start_polling(dp, skip_updates=True)