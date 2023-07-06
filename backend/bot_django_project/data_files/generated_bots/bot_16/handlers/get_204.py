
from aiogram import types
from loader import dp
from state import States



@dp.message_handler(lambda message: message.text == 'wolf', state=States.ramashechka_message_203)
async def handler_message_ramashechka_message_204(message: types.Message):
    await States.ramashechka_message_204.set()  # set state
    await message.answer(text='tr')  # send message
