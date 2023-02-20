# TelegramBot10
# эхо-бот на aiogram
# https://www.youtube.com/watch?v=viM3oWSUDQI&list=PLe-iIMbo5JOJm6DRTjhleHojroS-Bbocr&index=2

from aiogram import Bot, Dispatcher, types, executor
from config import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


@dp.message_handler()  # обрабатываем входящие сообщения
async def echo_upper(message: types.Message):  # объект message класса message
    await message.answer(message.text)  # написать сообщение ("текст" из входящего message, эмодзи тоже возвращает!)


if __name__ == '__main__':
    executor.start_polling(dp)
