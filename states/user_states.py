from aiogram.fsm.state import StatesGroup, State

class UserStates(StatesGroup):
    CHOOSING_LANGUAGE = State()
    MAIN_MENU = State()
    CREATING_AD = State()
