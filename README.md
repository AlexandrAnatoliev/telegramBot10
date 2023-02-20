# telegramBot10

[Ru] эхо-бот на iogram - эхо‑бот будет получать от пользователя текстовое сообщение и возвращать его.

Взят https://www.youtube.com/watch?v=viM3oWSUDQI&list=PLe-iIMbo5JOJm6DRTjhleHojroS-Bbocr&index=2

## Требования:

* $ pip install -r requirements.txt
* создать файл config.py, в котором будут храниться токен для доступа к боту в виде

```python 
token = "1234567890:ASDFGHH..."
```

## Где взять token?

* https://xakep.ru/2021/11/28/python-telegram-bots/

## Примеры использования

#### Добавляем библиотеки

```python
from aiogram import Bot, Dispatcher, types, executor
from config import TOKEN_API
```

Замечания:

* Бот - сервер, который будет взаимодействовать с API телеграмма
* API это часть телеграмм, служит для взаимодействия со сторонними приложениями.
* Dispatcher - класс отвечающий обработку входящих сообщений в бот
* executor - класс для запуска бота
* types - вероятно обрабатывает типы сообщений (текст, картинка)

#### Создаем экземпляр класса Bot

```python
bot = Bot(TOKEN_API)
```

#### Создаем экземпляр класса Dispatcher

```python
dp = Dispatcher(bot)
```

#### Запуск бота
```python
if __name__ == '__main__':
    executor.start_polling(dp)
```

#### Обрабатываем входящие сообщения, посылаем пользователю тектовую часть сообщения

```python
@dp.message_handler()  # обрабатываем входящие сообщения
async def echo_upper(message: types.Message):  # объект message класса message
    await message.answer(message.text)  # написать сообщение ("текст" из входящего message, эмодзи тоже возвращает!)
```