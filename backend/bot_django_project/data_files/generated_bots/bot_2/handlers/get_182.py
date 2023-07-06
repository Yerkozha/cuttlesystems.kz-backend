
from aiogram import types
from loader import dp
from state import States
from keyboards import keyboard_for_message_id_182


@dp.message_handler(lambda message: message.text == 'dsa', state=States.ramashechka_message_176)
async def handler_message_ramashechka_message_182(message: types.Message):
    await States.ramashechka_message_182.set()  # set state
    await message.answer(text='gfd', reply_markup=keyboard_for_message_id_182)  # send message


from keyboards import keyboard_for_message_id_182


@dp.message_handler(lambda message: message.text == 'dqw', state=States.ramashechka_message_178)
async def handler_message_ramashechka_message_182(message: types.Message):
    await States.ramashechka_message_182.set()  # set state
    await message.answer(text='gfd', reply_markup=keyboard_for_message_id_182)  # send message
