
from aiogram import types
from loader import dp
from state import States
from keyboards import keyboard_for_message_id_190


@dp.message_handler(lambda message: message.text == 'fds', state=States.ramashechka_message_192)
async def handler_message_ramashechka_message_190(message: types.Message):
    await States.ramashechka_message_190.set()  # set state
    await message.answer(text='dsa', reply_markup=keyboard_for_message_id_190)  # send message
