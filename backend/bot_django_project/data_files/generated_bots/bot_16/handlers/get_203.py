
from aiogram import types
from loader import dp
from state import States
from keyboards import keyboard_for_message_id_203


@dp.message_handler(lambda message: message.text == 'two', state=States.ramashechka_message_201)
async def handler_message_ramashechka_message_203(message: types.Message):
    await States.ramashechka_message_203.set()  # set state
    await message.answer(text='sun', reply_markup=keyboard_for_message_id_203)  # send message
