from aiogram.utils.keyboard import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import WebAppInfo
from aiogram import types

web_app = WebAppInfo(url='https://ahotelpoint.ru')

keyboard = ReplyKeyboardMarkup(
	keyboard=[
		[types.KeyboardButton(text='Site', web_app=web_app)]
	],
	resize_keyboard=True
)