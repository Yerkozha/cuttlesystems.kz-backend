
from aiogram import types
from loader import dp
from state import States
from keyboards import keyboard_for_message_id_198


@dp.message_handler(lambda message: message.text == 'te', state=States.ramashechka_message_197)
async def handler_message_ramashechka_message_198(message: types.Message):
    await States.ramashechka_message_198.set()  # set state
    await message.answer(text='flo', reply_markup=keyboard_for_message_id_198)  # send message
