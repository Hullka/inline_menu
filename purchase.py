from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery

from keyboards.inline.callback_datas import buy_callback
from keyboards.inline.choise_butons import menu1, menu2, apple_menu, apple_13, apple_12, samsung_menu, samsung_z3, \
    samsung_zf4
from loader import dp


@dp.message_handler(Command('items'))
async def show_items(message: types.Message):
    await message.answer(text='Выберите категорию', reply_markup=menu1)


@dp.callback_query_handler(buy_callback.filter(category="smartfon"))
async def category(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=menu2)


@dp.callback_query_handler(text="apple")
async def production_apple(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=apple_menu)


@dp.callback_query_handler(text="iphone_13")
async def buying_iphone13(call: CallbackQuery):
    await call.message.answer(f'Купить тут', reply_markup=apple_13)


@dp.callback_query_handler(text="iphone_12")
async def buying_iphone12(call: CallbackQuery):
    await call.message.answer(f'Купить тут', reply_markup=apple_12)


@dp.callback_query_handler(text="samsung")
async def production_samsung(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=samsung_menu)


@dp.callback_query_handler(text="Z3")
async def buying_z3(call: CallbackQuery):
    await call.message.answer(f'Купить тут', reply_markup=samsung_z3)


@dp.callback_query_handler(text="ZF3")
async def buying_zf3(call: CallbackQuery):
    await call.message.answer(f'Купить тут', reply_markup=samsung_zf4)


@dp.callback_query_handler(text='back')
async def cancel_buying(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=menu1)


@dp.callback_query_handler(text='back_to_menu2')
async def back(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=menu2)


@dp.callback_query_handler(text='exit')
async def exit_menu(call: CallbackQuery):
    await call.message.edit_reply_markup()
