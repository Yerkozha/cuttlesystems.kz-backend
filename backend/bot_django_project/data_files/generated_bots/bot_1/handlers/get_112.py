
from aiogram import types
from loader import dp
from state import States



@dp.callback_query_handler(text = 'gfd', state=States.ramashechka_message_277)
async def handler_message_ramashechka_message_112(callback: types.CallbackQuery):
    await States.ramashechka_message_112.set()  # set state
    await callback.message.answer(text='cds')  # send message
    await callback.answer(callback.data)
