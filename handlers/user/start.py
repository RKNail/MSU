from aiogram import types, Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from keyboards.reply import language_menu, main_menu
from states.user_states import UserStates
from config import config
router = Router()

@router.message(CommandStart())
async def greeting(message : types.Message, state: FSMContext):
    await state.set_state(UserStates.CHOOSING_LANGUAGE)
    await message.answer(
        """Приветствую, это бот HotWheels Uzbekistan для продажи и обмена моделей HotWheels!\n
Greetings, it's HotWheels Uzbekistan bot for traiding and selling HotWheels models!\n
Assalomu alaykum, bu HotWheels Uzbekistan boti HotWheels modellarini almashish va sotish uchun.\n      
Выберите язык / Choose language / Tilni tanlang:""",
        reply_markup=language_menu()
    )

@router.message(UserStates.CHOOSING_LANGUAGE)
async def choose_language(message: types.Message, state: FSMContext):
    print(message.from_user.id)
    lang_map = {
        "🇷🇺 Русский": "ru",
        "🇺🇿 O'zbek": "uz",
        "🇬🇧 English": "en"
    }
    lang = lang_map[message.text]

    # сохраняем выбранный язык в FSMContext
    await state.update_data(language=lang)

    # переходим в главное меню
    await state.set_state(UserStates.MAIN_MENU)
    await message.answer(
        text=config[lang]["main_menu"]["title"] ,
        reply_markup=main_menu(config[lang]["main_menu"]["buttons"])
    )

