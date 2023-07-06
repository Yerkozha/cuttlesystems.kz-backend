
from aiogram import types
from loader import dp
from state import States
from aiogram.dispatcher.filters import Command
from keyboards import keyboard_for_message_id_280


@dp.message_handler(Command('start'))
async def handler_message_ramashechka_message_280(message: types.Message):
    await States.ramashechka_message_280.set()  # set state
    await message.answer(text='sd', reply_markup=keyboard_for_message_id_280)  # send message


from keyboards import keyboard_for_message_id_280


@dp.message_handler(Command('restart'), state='*')
async def handler_message_ramashechka_message_280(message: types.Message):
    await States.ramashechka_message_280.set()  # set state
    await message.answer(text='sd', reply_markup=keyboard_for_message_id_280)  # send message
