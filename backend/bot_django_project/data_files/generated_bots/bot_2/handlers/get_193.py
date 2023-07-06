
from aiogram import types
from loader import dp
from state import States
from keyboards import keyboard_for_message_id_193


@dp.message_handler(lambda message: message.text == 'ewq', state=States.ramashechka_message_190)
async def handler_message_ramashechka_message_193(message: types.Message):
    await States.ramashechka_message_193.set()  # set state
    await message.answer(text='dsa', reply_markup=keyboard_for_message_id_193)  # send message


from keyboards import keyboard_for_message_id_193


@dp.callback_query_handler(text = 'dsa', state=States.ramashechka_message_232)
async def handler_message_ramashechka_message_193(callback: types.CallbackQuery):
    await States.ramashechka_message_193.set()  # set state
    await callback.message.answer(text='dsa', reply_markup=keyboard_for_message_id_193)  # send message
    await callback.answer(callback.data)
