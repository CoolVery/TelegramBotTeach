from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

#Кнопки клавиатуры - внутрь подается лист листов. Если мы хотим, чтобы кнопки были в ряд, то тогда в одном листе
#пишем несколько запятую. Т.е. один лист - это строка
main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Каталог')],
    [KeyboardButton(text='Корзина'), KeyboardButton(text='Каталог')],
],
                           #Делает кнопки меньше
                           resize_keyboard=True,
                           #Меняет текст в поле сообщения
                           input_field_placeholder='Выберите пункт меню'
                           )

#Кнопки сообщения - тоже самое, только кроме текста должны содержать доп параметр
settings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Крутой', url='https://t.me/Choto_Neznay')]
])

#Мы можем в текст кнопок передать значения списков через цикл
cars = ['Tesla', 'BMW', 'Toyta']

# async def inline_cars():
#     keyboard = ReplyKeyboardBuilder()
#     for car in cars:
#         keyboard.add(KeyboardButton(text=car))
#     return keyboard.adjust(2).as_markup()

async def inline_cars():
    keyboard = InlineKeyboardBuilder()
    for car in cars:
        keyboard.add(InlineKeyboardButton(text=car, url='https://t.me/Choto_Neznay'))
    #as_markup() всегда дописываем. adjust задает сколько элементов будет в строке, т.е. если 3 элемента в списке
    #то в одной строке будет 2 элемента, а 3 будет во всю строку
    return keyboard.adjust(2).as_markup()