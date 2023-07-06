
from aiogram import types
from loader import dp
from state import States



@dp.message_handler(lambda message: message.text == 're', state=States.ramashechka_message_197)
async def handler_message_ramashechka_message_199(message: types.Message):
    await States.ramashechka_message_199.set()  # set state
    await message.answer(text='test1')  # send message


from keyboards import keyboard_for_message_id_199


@dp.message_handler(lambda message: message.text == 'gg', state=States.ramashechka_message_198)
async def handler_message_ramashechka_message_199(message: types.Message):
    await States.ramashechka_message_199.set()  # set state
    await message.answer(text='test1', reply_markup=keyboard_for_message_id_199)  # send message
