#  -*- coding: utf-8 -*-

import telepot
import time

commands = ['settime', 'humidity']
user_times = {}
done = {}

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(chat_id)

    if msg['text'].find('settime')!=-1:
        preproc = msg['text'].replace('settime','').replace(' ', '').replace('.', '').replace(':', '')
        if len(preproc)==4:
            user_times[chat_id]=preproc
            done[chat_id]=0
            bot.sendMessage(chat_id, 'I will water your flowers at '+ str(user_times[chat_id][0:2])+':'+str(user_times[chat_id][2:4]))

        else:
            bot.sendMessage(chat_id, 'Wrong syn, maybe time missing')

    else:
        bot.sendMessage(chat_id, 'Are you sure this command exists?')

def loop():
    print(1)

TOKEN = '251302638:AAELpj_ot9pBPUbBaVP_06owxxGnhDVxrjw'

bot = telepot.Bot(TOKEN)
bot.message_loop(handle)
print('In deep thoughts')

while True:
    for date in user_times:
        if user_times[date]==time.strftime('%X')[0:5].replace(':', '') and done[date]==0:
            bot.sendMessage(date, 'Watered')
            done[date]=1

    time.sleep(5)