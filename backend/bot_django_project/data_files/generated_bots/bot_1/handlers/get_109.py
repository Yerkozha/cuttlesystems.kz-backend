
from aiogram import types
from loader import dp
from state import States



@dp.callback_query_handler(text = 'ds', state=States.ramashechka_message_277)
async def handler_message_ramashechka_message_109(callback: types.CallbackQuery):
    await States.ramashechka_message_109.set()  # set state
    await callback.message.answer(text='dsa')  # send message
    await callback.answer(callback.data)
