from aiogram import types
from misc import dp,bot
import asyncio
import random
import datetime
import pytz
from .sqlit import get_caption,reg_user
reg_user(1)
content_id = -1001656498705

link0 = -1001472593713 #СУКА ЗАЕБАЛИ
link1 = -1001625021061 #РАЙСКОЕ НАСЛАЖДЕНИЕ 3.0
link2 = -1001187956064 #НЕ ШKOЛЬNИЦЫ
link3 = -1001305402192 #Твои подруги 🥰
link4 = -1001556066317 #🍌После уроков🍌
link5 = -1001598151302 #СУЧKA💓
link6 = -1001500270712 #Русские шалости

channels = [link0,link1,link2,link3,link4,link5,link6]


time0 = "7:59"
time1 = "12:59"
time2 = "13:59"
time3 = "17:59"
time4 = "20:59"

async def posting():
    for chaneel in channels:
            await bot.copy_message(caption = get_caption()[0][0],from_chat_id=content_id,chat_id= chaneel,message_id = random.randint(1,189 - 1),parse_mode='html')
    print('Выложил посты во все каналы. Скрипт спит 30 минут')


def second_time(finish_data):
    hours_f = int(finish_data[0:2]) #Часы финиша
    min_f = int(finish_data[3:]) #Минуты финиша
    second_f = 0

    hours_now = datetime.datetime.now(pytz.timezone('Europe/Moscow')).hour
    min_now = datetime.datetime.now(pytz.timezone('Europe/Moscow')).minute
    seconf_now = datetime.datetime.now(pytz.timezone('Europe/Moscow')).second


    time_now = datetime.datetime(year = 2022,month = 1,day = 1, hour = hours_now,minute = min_now,second = seconf_now)
    time_finish = datetime.datetime(year = 2022,month = 1,day = 1, hour = hours_f,minute = min_f,second = second_f)

    delta = (time_finish-time_now).seconds
    return delta



async def sender():
    while True:
        await asyncio.sleep(5)
        hours_now = datetime.datetime.now(pytz.timezone('Europe/Moscow')).hour

        if hours_now == 7 or hours_now == 12 or hours_now == 13 or hours_now == 17 or hours_now == 20:
            if hours_now == 7:
                t = second_time("07:59")
                print(f"Спим {t} секунд")
                await asyncio.sleep(t)
                await posting()

            elif hours_now == 12:
                t = second_time("12:59")
                print(f"Спим {t} секунд")
                await asyncio.sleep(t)
                await posting()

            elif hours_now == 13:
                t = second_time("13:59")
                print(f"Спим {t} секунд")
                await asyncio.sleep(t)
                await posting()

            elif hours_now == 17:
                t = second_time("17:59")
                print(f"Спим {t} секунд")
                await asyncio.sleep(t)
                await posting()

            elif hours_now == 20:
                t = second_time("20:59")
                print(f"Спим {t} секунд")
                await asyncio.sleep(t)
                await posting()


        await asyncio.sleep(1800) #Проверяем каждые 30 минут

