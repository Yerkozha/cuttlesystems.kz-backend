
from aiogram import types
from loader import dp
from state import States
from keyboards import keyboard_for_message_id_178


@dp.message_handler(lambda message: message.text == 'll', state=States.ramashechka_message_192)
async def handler_message_ramashechka_message_178(message: types.Message):
    await States.ramashechka_message_178.set()  # set state
    await message.answer(text='ewq', reply_markup=keyboard_for_message_id_178)  # send message


from keyboards import keyboard_for_message_id_178


@dp.message_handler(lambda message: message.text == 'das', state=States.ramashechka_message_193)
async def handler_message_ramashechka_message_178(message: types.Message):
    await States.ramashechka_message_178.set()  # set state
    await message.answer(text='ewq', reply_markup=keyboard_for_message_id_178)  # send message
