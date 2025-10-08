from aiogram.fsm.context import FSMContext 
from aiogram.fsm.state import State, StatesGroup


class Todo(StatesGroup):
	task_name = State() 
	level = State() 
	desc = State() 
