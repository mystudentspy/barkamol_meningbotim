from aiogram import Router, types
from aiogram.types import reply_markup_union

rt = Router()
@rt.message()
async def dice(msg: types.Message):

