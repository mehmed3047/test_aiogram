import time,requests
"""
TOKEN = "5413252425:AAHvDoAQm8OGCKI6KnnGqCJG-Mk1vwrBIU8"
# @ finder_new_coins_bot
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import ChatType
import time,requests #threading
import trade_exchanges as exc
from exchange_lists import listeler,trade_list
from block_tokens import block_coin

bot= Bot(token=TOKEN)
logging.basicConfig(level=logging.WARNING)
dp = Dispatcher(bot)


localtime = time.localtime(time.time()+10800)
time_now=f'بسم الله الرحمن الرحيم\n{localtime.tm_mday}/{localtime.tm_mon}/{localtime.tm_year}  {localtime.tm_hour}:{localtime.tm_min}'


@dp.message_handler(chat_type=[ChatType.SUPERGROUP, ], commands=['finder'])
async def cmd_start(message: types.Message):
    t= '@finder_new_coins_bot'
    await bot.send_message(-1001571458368, text=t)






if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True) """


def my_bot(text=None):
	url ='https://api.telegram.org/bot5252631688:AAHi2zgDYfItn01qXs36gfOHZOsMrllKbmk/sendmessage?chat_id=-1001571458368&amp;text=Sample'
	data ={'text':text}
	r= requests.get(url,params=data)

while 1:
    my_bot(text='merhama mehmed')
    time.sleep(8)


