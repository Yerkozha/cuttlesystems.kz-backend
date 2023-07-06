
from aiogram import types
from loader import dp
from state import States
from keyboards import keyboard_for_message_id_202


@dp.message_handler(lambda message: message.text == 'one', state=States.ramashechka_message_201)
async def handler_message_ramashechka_message_202(message: types.Message):
    await States.ramashechka_message_202.set()  # set state
    await message.answer(text='bla', reply_markup=keyboard_for_message_id_202)  # send message
