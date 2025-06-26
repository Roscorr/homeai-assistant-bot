from aiogram import Dispatcher, types
import json

def register_handlers(dp: Dispatcher):
    @dp.message_handler(commands=["start"])
    async def start_handler(message: types.Message):
        await message.answer("Привет! Я — ассистент проекта HomeAI. Пиши /help для команд.")

    @dp.message_handler(commands=["help"])
    async def help_handler(message: types.Message):
        await message.answer("/start — запуск\n/status — статус проекта\n/idea — отправить идею\n/help — помощь")

    @dp.message_handler(commands=["status"])
    async def status_handler(message: types.Message):
        with open("data/status.json", "r", encoding="utf-8") as f:
            status = json.load(f)
        reply = "\n".join([f"{'✔️' if s['done'] else '🔄'} {s['task']}" for s in status])
        await message.answer(f"📊 Статус проекта:\n{reply}")

    @dp.message_handler(commands=["idea"])
    async def idea_handler(message: types.Message):
        await message.answer("Отправь свою идею одним сообщением.")

    @dp.message_handler(lambda m: not m.text.startswith("/") and m.reply_to_message and "идею" in m.reply_to_message.text.lower())
    async def save_idea(message: types.Message):
        with open("data/ideas.txt", "a", encoding="utf-8") as f:
            f.write(f"- {message.from_user.username or message.from_user.full_name}: {message.text}\n")
        await message.answer("Спасибо, идея сохранена!")