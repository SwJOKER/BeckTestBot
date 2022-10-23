from aiogram.utils.keyboard import KeyboardButton, ReplyKeyboardBuilder, ReplyKeyboardMarkup, InlineKeyboardBuilder, InlineKeyboardButton, InlineKeyboardMarkup
from string_vars import *

def avaible_commands_keyboard()-> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text='/start')
    kb.button(text='/depress')
    return kb.as_markup(resize_keyboard=True)

def get_yes_no_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text='Да')
    kb.button(text='Нет')
    kb.adjust(2)
    return kb.as_markup(resize_keyboard = True)

def make_row_keyboard(items: list[str]) -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    keys_row = [KeyboardButton(text = item) for item in items]
    builder.row(*keys_row)
    builder.button(text=EXIT_TEST_MSG)
    builder.button(text=TEST_RESTART_MSG)
    builder.adjust(1)
    return builder.as_markup(resize_keyboard=True)

def get_number_kb(key_count: int) -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    for i in range(key_count):
        kb.button(text=str(i + 1))
    return kb.as_markup(resize_keyboard = True)
