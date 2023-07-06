
from aiogram import types
from loader import dp
from state import States
from keyboards import keyboard_for_message_id_277


@dp.message_handler(lambda message: message.text == 'ewq', state=States.ramashechka_message_278)
async def handler_message_ramashechka_message_277(message: types.Message):
    await States.ramashechka_message_277.set()  # set state
    await message.answer(text='dsa', reply_markup=keyboard_for_message_id_277)  # send message
