from config import TOKEN as tk
import logging
from aiogram import Bot,Dispatcher,executor,types
bot =Bot(token=tk)
dp=Dispatcher(bot)
from config import *
path = '//home//uroot//Documents//py//tch//test.db'

#910595136
@dp.message_handler(commands=['start'])
async def process_hello(message:types.message):
	c=conv(message.text)
	for r in range(int(max_id(path))):
		await bot.send_message(int(und(path,r+1)),str(message.from_user.first_name)+' is joined)')
	await message.reply("You joined!\nWrite something to this group)")
	nm(message.from_user.id,message.from_user.first_name,message.text,path)
	
@dp.message_handler(content_types=['text'])
async def tgm(message:types.message):
	c=conv(message.text)
	mid=max_id(path)
	for r in range(int(mid)):
		await bot.send_message(int(und(path,r+1)),str(message.from_user.first_name)+' >>\n\n '+c)
	add(path,message.from_user.id,message.text)
	await bot.delete_message(message.chat.id, message.message_id)
        


if __name__=="__main__":
	connect(path)
	executor.start_polling(dp,skip_updates=False)