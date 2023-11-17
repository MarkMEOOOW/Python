from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN, COMMANDS

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = Bot(TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['commands'])
async def commands(message: types.Message) -> None:
    await bot.send_message(message.chat.id, text=COMMANDS, parse_mode='html')


@dp.message_handler(commands=['start'])
async def start(message: types.Message) -> None:
    keyboard = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton(text='Информация', url='')
    button_2 = InlineKeyboardButton(text='Рандом', url='')
    button_3 = InlineKeyboardButton(text='Мем', url='')
    keyboard.add(button_1, button_2, button_3)
    await bot.send_message(message.chat.id, 'Просто текст', reply_markup=keyboard)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
