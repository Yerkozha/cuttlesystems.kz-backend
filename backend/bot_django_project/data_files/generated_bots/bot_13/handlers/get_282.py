
from aiogram import types
from loader import dp
from state import States
from keyboards import keyboard_for_message_id_282


@dp.callback_query_handler(text = 'fds', state=States.ramashechka_message_280)
async def handler_message_ramashechka_message_282(callback: types.CallbackQuery):
    await States.ramashechka_message_282.set()  # set state
    await callback.message.answer(text='fds', reply_markup=keyboard_for_message_id_282)  # send message
    await callback.answer(callback.data)
