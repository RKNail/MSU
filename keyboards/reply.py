from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def language_menu():
    keyboard = ReplyKeyboardMarkup(
        keyboard = [
            [KeyboardButton(text="🇷🇺 Русский")],
            [KeyboardButton(text="🇬🇧 English")],
            [KeyboardButton(text="🇺🇿 O'zbek")]
        ],
        resize_keyboard=True,
        one_time_keyboard=True,
    )
    return keyboard

def main_menu(buttons : list) :
    keyboard = ReplyKeyboardMarkup(
        keyboard = [[KeyboardButton(text=b)] for b in buttons],
        resize_keyboard=True,
        one_time_keyboard=False,
    )
    return keyboard


