from aiogram.types import (
	ReplyKeyboardMarkup, ReplyKeyboardRemove, 
	InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton )  


main_kb = ReplyKeyboardMarkup(
	keyboard= [ 
		[		KeyboardButton(text="📄 All task"), 
	 			KeyboardButton(text="➕ Add task")
		]
		],resize_keyboard=True) 


level_kb = ReplyKeyboardMarkup(
	keyboard= [ 
		[KeyboardButton(text="Muhum  🔴"), KeyboardButton(text="O'rta 🟡"), KeyboardButton(text="Ixtiyoriy 🟢")]
	],resize_keyboard=True
)


skip_kb = ReplyKeyboardMarkup(
	keyboard= [
		[KeyboardButton(text="O'tazib yuborish ⏩")]
	],resize_keyboard=True
)

inline_button = InlineKeyboardMarkup(
	inline_keyboard= [
		[InlineKeyboardButton(text="✏️ Edit task", callback_data="edit:{task_id}"), InlineKeyboardButton(text="🪓Delate task", callback_data="delete:{task_id}")]
	]
)