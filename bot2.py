from aiogram.types import Message, User, KeyboardButton,InlineKeyboardMarkup, InlineKeyboardButton,CallbackQuery
from aiogram import Router, Dispatcher, Bot
from aiogram.filters.command import Command
from asyncio import run
from abc import ABC, abstractmethod
from weathers import get_date

City = InlineKeyboardMarkup(
    inline_keyboard = [
       [
InlineKeyboardButton(text='Toshkеnt',callback_data='27'),
InlineKeyboardButton(text='Andijon',callback_data='1'),
InlineKeyboardButton(text='Buxoro',callback_data='4'),],
[
InlineKeyboardButton(text='Guliston',callback_data='5'),
InlineKeyboardButton(text='Samarqand',callback_data='18'),
InlineKeyboardButton(text='Namangan',callback_data='15'),],
[
InlineKeyboardButton(text='Navoiy',callback_data='14'),
InlineKeyboardButton(text='Jizzax',callback_data='9'),
InlineKeyboardButton(text='Nukus',callback_data='16'),],
[
InlineKeyboardButton(text='Qarshi',callback_data='25'),
InlineKeyboardButton(text='Qoʻqon',callback_data='26'),
InlineKeyboardButton(text='Xiva',callback_data='21'),],
[InlineKeyboardButton(text='Margʻilon',callback_data='13')],
    
        ]
)
ortga_tugma = InlineKeyboardMarkup(
    inline_keyboard = [
      [InlineKeyboardButton(text='ortga',callback_data='back')]
    ]
)


greet = Router()

@greet.message(Command(commands=["start"]))
async def greet_message(msg: Message, bot: Bot):
    await msg.answer("Namoz vaqtlari: ",reply_markup=City)
  

@greet.callback_query()
async def namoz_time(call:CallbackQuery):

  if call.data =="back":
    await call.message.edit_text("Namoz vaqtlari: ",reply_markup=City)
  else:
    m = int(call.data)
    content = vaqti(m)
    text = f"""Bugun {content[2]} namoz vaqtlari:
bomdod: {content[3]}
quyosh: {content[4]}
peshin: {content[5]}
asr: {content[6]}
shom: {content[7]}
hufton: {content[8]}"""
    
    await call.message.edit_text(text,reply_markup=ortga_tugma)



async def start():
    dp = Dispatcher()
    bot = Bot("5317958815:AAHhKyLHDJTtAKCjEB4JIiTllufINjetIPI")
    dp.include_router(greet)
    try:
        await dp.start_polling(bot)
    except:
        await bot.session.close()

if __name__ == "__main__":
    run(start())