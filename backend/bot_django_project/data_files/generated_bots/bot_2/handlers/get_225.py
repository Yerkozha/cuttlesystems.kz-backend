
from aiogram import types
from loader import dp
from state import States



@dp.callback_query_handler(text = 'dsa', state=States.ramashechka_message_217)
async def handler_message_ramashechka_message_225(callback: types.CallbackQuery):
    await States.ramashechka_message_225.set()  # set state
    await callback.message.answer(text='dasda')  # send message
    await callback.answer(callback.data)





@dp.callback_query_handler(text = 'ewq', state=States.ramashechka_message_232)
async def handler_message_ramashechka_message_225(callback: types.CallbackQuery):
    await States.ramashechka_message_225.set()  # set state
    await callback.message.answer(text='dasda')  # send message
    await callback.answer(callback.data)
