
from aiogram import types
from loader import dp
from state import States
from keyboards import keyboard_for_message_id_150


@dp.message_handler(lambda message: message.text == '312', state=States.ramashechka_message_211)
async def handler_message_ramashechka_message_150(message: types.Message):
    await States.ramashechka_message_150.set()  # set state
    await message.answer(text='das', reply_markup=keyboard_for_message_id_150)  # send message
