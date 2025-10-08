from aiogram import Dispatcher, Bot, Router
from environs import Env

from handler import user_router
import logging 
import asyncio 

dp = Dispatcher() 

env = Env() 
env.read_env()

TOKEN = env.str("TOKEN")

async def main(): 
	bot = Bot(token=TOKEN)
	dp.include_router(user_router)
	await dp.start_polling(bot) 


if __name__ == "__main__": 
	logging.basicConfig(level=logging.INFO) 
	asyncio.run(main()) 

