from aiogram import types, Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from keyboards.reply import language_menu, main_menu
from states.user_states import UserStates
from config import config

router = Router()

@router.message(UserStates.CREATING_AD)
async def create_ad(message: types.Message, state: FSMContext):
