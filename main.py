from config import token_tg
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot=Bot(token=token_tg)
dp=Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply('Здаров.\nНапиши что-то')


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply('Ты пишешь мне сообщение и я его тебе же отправляю')    


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)


if __name__=="__main__":
    executor.start_polling(dp)



