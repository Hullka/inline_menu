from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_datas import buy_callback

menu1 = InlineKeyboardMarkup(row_width=1)
smart = InlineKeyboardButton(text='Смартфоны',
                             callback_data=buy_callback.new(category="smartfon",
                                                            item_name=["apple", "samsung"],
                                                            product=["iphone_13", "iphone_12"]))
menu1.insert(smart)
exit_button = InlineKeyboardButton(text="Выход", callback_data="exit")
menu1.insert(exit_button)

back_button = InlineKeyboardButton(text="Назад", callback_data="back")

menu2 = InlineKeyboardMarkup(row_width=2)
apple = InlineKeyboardButton(text='Apple', callback_data="apple")
menu2.insert(apple)
samsung = InlineKeyboardButton(text='Samsung', callback_data="samsung")
menu2.insert(samsung)
menu2.insert(back_button)

apple_menu = InlineKeyboardMarkup(row_width=2)
iphone_13 = InlineKeyboardButton(text='Iphone 13', callback_data="iphone_13")
apple_menu.insert(iphone_13)
iphone_12 = InlineKeyboardButton(text='Iphone 12', callback_data="iphone_12")
apple_menu.insert(iphone_12)
back_button = InlineKeyboardButton(text="Назад", callback_data="back_to_menu2")
apple_menu.insert(back_button)

apple_12 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='iPhone 12', url='https://www.citrus.ua/smartfony/iphone-12-128gb-purple-apple-688604.html?app=nextgen')]
])
apple_13 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='iPhone 13', url='https://www.citrus.ua/smartfony/iphone-13-128gb-red-apple-696631.html')]
])

samsung_menu = InlineKeyboardMarkup(row_width=2)
Z3 = InlineKeyboardButton(text='Galaxy Z Fold 3', callback_data="Z3")
samsung_menu.insert(Z3)
ZF3 = InlineKeyboardButton(text='Galaxy Z Flip 3', callback_data="ZF3")
samsung_menu.insert(ZF3)
back_button = InlineKeyboardButton(text="Назад", callback_data="back_to_menu2")
samsung_menu.insert(back_button)

samsung_z3 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Galaxy Z Fold 3', url='https://www.citrus.ua/smartfony/f926b-zkd-galaxy-z-fold-3-phantom-black-samsung-12256gb-694351.html')]
])
samsung_zf4 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Galaxy Z Flip 3', url='https://www.citrus.ua/smartfony/f711b-zka-galaxy-z-flip-3-phantom-black-samsung-8128gb-694359.html')]
])
