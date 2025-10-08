from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import CommandStart 
from aiogram.fsm.context import FSMContext

from states import Todo
from buttons import main_kb,level_kb, skip_kb,inline_button
from database import save_user_task, user_task_from_chat_id

user_router = Router() 


@user_router.message(CommandStart())
async def start_handler(message: Message): 
	await message.answer(f"Assalomu alaykum {message.from_user.first_name}, Kerakli bo'limni tanlang.  ",reply_markup=main_kb) 

@user_router.message(F.text == "➕ Add task") 
async def add_task_handler(message: Message, state: FSMContext): 
	await state.set_state(Todo.task_name) 
	await message.reply("Task nomini kiriting: ",reply_markup=ReplyKeyboardRemove()) 


@user_router.message(Todo.task_name)
async def get_level_handler(message: Message, state: FSMContext):
	task_name_input = message.text 
	await state.update_data(task_name = task_name_input)
	await state.set_state(Todo.level)
	await message.answer("Muhimlik darajasini kiriting", reply_markup=level_kb)


@user_router.message(Todo.level) 
async def get_desC(message: Message, state:FSMContext): 
	level_input = message.text 
	await state.update_data(level = level_input)
	await state.set_state(Todo.desc) 
	await message.answer("Tavsif kiriting. (Ixtiyoriy)",reply_markup=skip_kb)


@user_router.message(Todo.desc)
async def save_all_task(message: Message, state: FSMContext):
	text = message.text 


	if text == "O'tazib yuborish ⏩":
		description = None
	else: 
		description = text

	await state.update_data(desc = description) 

	data =  await state.get_data() 
	chat_id = message.from_user.id 
	task = data.get('task_name')
	level  = data.get('level')
	descrip = data.get('desc') 	

	if not (task and level):
		await message.answer("Kerakli ma'lumotlar to'liq kiritilmadi.")
		return

	try: 
		save_user_task(chat_id, task, level, descrip) 
		await message.answer("✅ Vazifa muvaffaqiyatli bazaga saqlandi.",reply_markup=main_kb)
		await state.clear() 
	except Exception as e: 
		await message.answer(f"Xatolik {e}")


@user_router.message(F.text == "📄 All task")
async def get_tasks(message: Message):
	tasks = user_task_from_chat_id(message.from_user.id)
	if not tasks:
			await message.answer("Sizda hali birorta task yo‘q\n➕ Add task tugmasini bosib task qo'shing!")
	else:
			text = "<b>📋 Sizning vazifalaringiz:</b>\n\n"
			for i, (task, level, desc) in enumerate(tasks, start=1):
					text += (
							f"<b>{i}.</b> <b>{task}</b>\n"
							f"Daraja: <i>{level}</i>\n"
							f"Tavsif: {desc or 'yo‘q'}\n\n"
					)
			await message.answer(text, parse_mode="HTML", reply_markup=inline_button)
