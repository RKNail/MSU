from .start import router as starter
from aiogram import Router

router = Router()

router.include_routers(starter)


__all__ = ["router"]