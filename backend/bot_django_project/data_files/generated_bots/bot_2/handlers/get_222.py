
from aiogram import types
from loader import dp
from state import States



@dp.callback_query_handler(text = 'dsa', state=States.ramashechka_message_285)
async def handler_message_ramashechka_message_222(callback: types.CallbackQuery):
    await States.ramashechka_message_222.set()  # set state
    await callback.message.answer(text='das')  # send message
    await callback.answer(callback.data)
