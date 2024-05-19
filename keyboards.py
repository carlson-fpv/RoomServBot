from aiogram.utils.keyboard import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import WebAppInfo
from aiogram import types

web_app = WebAppInfo(url='https://77.222.42.229/')

keyboard = ReplyKeyboardMarkup(
	keyboard=[
		[types.KeyboardButton(text='Site', web_app=web_app)]
	],
	resize_keyboard=True
)