
from aiogram import types
from loader import dp
from state import States



@dp.callback_query_handler(text = 'das', state=States.ramashechka_message_277)
async def handler_message_ramashechka_message_107(callback: types.CallbackQuery):
    await States.ramashechka_message_107.set()  # set state
    await callback.message.answer(text='gfd')  # send message
    await callback.answer(callback.data)
