
from aiogram import types
from loader import dp
from state import States
from keyboards import keyboard_for_message_id_279


@dp.callback_query_handler(text = 'dsa', state=States.ramashechka_message_277)
async def handler_message_ramashechka_message_279(callback: types.CallbackQuery):
    await States.ramashechka_message_279.set()  # set state
    await callback.message.answer(text='das', reply_markup=keyboard_for_message_id_279)  # send message
    await callback.answer(callback.data)
