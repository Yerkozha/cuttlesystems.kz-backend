
from aiogram import types
from loader import dp
from state import States



@dp.message_handler(lambda message: message.text == 'good', state=States.ramashechka_message_202)
async def handler_message_ramashechka_message_205(message: types.Message):
    await States.ramashechka_message_205.set()  # set state
    await message.answer(text='w')  # send message
