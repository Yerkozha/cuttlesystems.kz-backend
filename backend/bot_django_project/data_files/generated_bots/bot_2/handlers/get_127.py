
from aiogram import types
from loader import dp
from state import States
from keyboards import keyboard_for_message_id_127


@dp.callback_query_handler(text = 'k', state=States.ramashechka_message_216)
async def handler_message_ramashechka_message_127(callback: types.CallbackQuery):
    await States.ramashechka_message_127.set()  # set state
    await callback.message.answer(text='re', reply_markup=keyboard_for_message_id_127)  # send message
    await callback.answer(callback.data)
