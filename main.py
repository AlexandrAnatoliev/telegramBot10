# TelegramBot10
# эхо-бот на aiogram
# https://www.youtube.com/watch?v=viM3oWSUDQI&list=PLe-iIMbo5JOJm6DRTjhleHojroS-Bbocr&index=2
# ПРАКТИКА:
# 1. Напишите бота, который будет отправлять пользователю его же сообщение, переведенное в верхний регистр
# 2. Напишите бота, который будет отправлять пользователю его же сообщение, при условии,
# что предложение состоит более чем из двух слов

from aiogram import Bot, Dispatcher, types, executor
from config import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


@dp.message_handler()  # обрабатываем входящие сообщения
async def echo_upper(message: types.Message):  # объект message класса message
    """
    Возвращает сообщение пользователю в верхнем регистре, если число слов в предложении больше двух

    :param message: сообщение
    :return: тектовое сообщение пользователю в верхнем регистре, если число слов в предложении больше двух
    """
    answ = message.text.upper()  # сообщение пользователю в верхнем регистре
    if len(answ.split()) < 3:  # возвращает сообщение пользователю, если число слов в предложении больше двух
        answ = "Слишком короткое сообщение"
    await message.answer(answ)  # написать сообщение ("текст" из входящего message, эмодзи тоже возвращает!)


if __name__ == '__main__':
    executor.start_polling(dp)
