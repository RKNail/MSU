from aiogram import Router
from . import user

router = Router()

router.include_router(user.router)

__all__ = ["router"]