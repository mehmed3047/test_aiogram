#......
TOKEN = "5252631688:AAHpRtKzJCZL2-KjD48dtE8s0DLvTxDcHKA"
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


@dp.message_handler(chat_type=[ChatType.SUPERGROUP, ], commands=['.'])
async def cmd_start(message: types.Message):
    await bot.send_message(-1001571458368, time_now)


@dp.message_handler(chat_type=[ChatType.SUPERGROUP, ], commands=['start'])
async def cmd_start(message: types.Message):
    await bot.send_message(-1001571458368, text=time_now)

    while True:
        try:
            kar1 = kar2 = 1
            excs = ['bitfinex', 'bitmart', 'bitmex', 'bitget', 'bittrex', 'btcTurk', 'bybit', 'hitbtc','gateio','huobi', 'hotbit','lbank', 'mexc', 'okx', 'polo', 'yobit', 'ztb', 'xt', 'exmo']
            excs = ['binance','pionex','bitfinex', 'bitmart', 'bitmex', 'bitget', 'bittrex', 'btcTurk', 'bybit', 'hitbtc','huobi', 'lbank', 'mexc', 'okx', 'polo',]
            excs = ['bitmart','polo','lbank','bitfinex']          
            excs.sort()
            for i in excs:
                exc1 = 'bitmart'
                exc2 = 'kucoin'

                fonk1, fonk2 = exc.fonksiyonlar(exc1, exc2)

                yon1 = f'{fonk1.__name__[6:]}deAl_{fonk2.__name__[6:]}deSat'
                yon2 = f'{fonk2.__name__[6:]}deAl_{fonk1.__name__[6:]}deSat'

                def fonk1deAl_fonk2deSat(coin=None):
                    url_1 = fonk1(coin=coin, al_sat='al')
                    url_2 = fonk2(coin=coin, al_sat='sat')
                    return exc.trade_func(url_1=url_1, url_2=url_2, kar_orani=kar1)

                def fonk2deAl_fonk1deSat(coin=None):
                    url_1 = fonk2(coin=coin, al_sat='al')
                    url_2 = fonk1(coin=coin, al_sat='sat')
                    return exc.trade_func(url_1=url_1, url_2=url_2, kar_orani=kar2)

                async def  fonk_1(i):
                    oran1, total1, buy1, sell1 = fonk1deAl_fonk2deSat(coin=i.upper())
                    if oran1:
                        kar1 = f'{total1 * (sell1 - buy1):.1f}'
                        if float(kar1) > 2 :
                            text1 = f'{int((float(kar1) // 10)) *"⚡"}\n{yon1}_{i}\nkar_{kar1}    oran_{oran1:.1f}\nt_{total1}\nb_{buy1}\ns_{sell1}'
                            await bot.send_message(-1001571458368, text=text1)

                async def fonk_2(i):
                    oran2, total2, buy2, sell2 = fonk2deAl_fonk1deSat(coin=i.upper())
                    if oran2:
                        kar2 = f'{total2 * (sell2 - buy2):.1f}'
                        if float(kar2) > 2:
                            text2 = f'{int((float(kar2) // 10))*"⚡"}\n{yon2}_{i}\nkar_{kar2}    oran_{oran2:.1f}\nt_{total2}\nb_{buy2}\ns_{sell2}'
                            await bot.send_message(-1001571458368, text=text2)

                async def new_coin():
                    try:
                        trade_listesi = trade_list(exc1, exc2)
                        for coin in trade_listesi:
                            try:
                                await fonk_1(coin)
                                await fonk_2(coin)
                            except Exception as e:
                                print(74, e)
                                continue
                    except Exception as e:
                        print(77, e)
                        time.sleep(2)

                await new_coin()

        except Exception as e:
            await bot.send_message(-1001571458368, text=f'hata 2 {e}')
            print(84, e)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
