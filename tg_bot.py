import asyncio
import google.generativeai as genai
import aiogram
from aiogram import Dispatcher,Bot
from aiogram.types import Message
from aiogram.filters import Command

# Бот
bot = Bot(token='7757625794:AAG6oHFqthk3IfRbcCQMmDKBCMu1wQEHaF4')

# Диспетчер
dp = Dispatcher()

# Прием сообщений

@dp.message(Command('start'))
async def start_command(message: Message):
    await message.answer('ку')

@dp.message(Command('help'))
async def help_command(message: Message):
    await message.answer('/help - список команд, /start - начать работу с ботом, /ask_bot - спросить у бота')

@dp.message()
async def ask_command(message: Message):
    otvet = await query_lim(message.text)
    await message.answer(otvet)

# Настройка Gemini

genai.configure(api_key='AIzaSyCrr6zPIn3NGzZv4guTIuiGeA-eU0ejYvs')

async def on_startup():
    print('Бот запущен')

async def query_lim(user_message: str) -> str:
    try:
        model = genai.GenerativeModel('gemini-2.0-pro-exp-02-05')
        otvet = model.generate_content(user_message)
        return otvet.text.strip()
    except Exception as e:
        return f"Ошибка: {e}"

async def main():
    await on_startup()
    await bot.delete_webhook(drop_pending_updates = True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())