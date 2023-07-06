
from aiogram import types
from loader import dp
from state import States



@dp.message_handler(lambda message: message.text == 'te', state=States.ramashechka_message_198)
async def handler_message_ramashechka_message_200(message: types.Message):
    await States.ramashechka_message_200.set()  # set state
    await message.answer(text='test2')  # send message
