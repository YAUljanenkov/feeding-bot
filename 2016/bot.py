import telebot
import json


bot = telebot.TeleBot('317057242:AAF4onY33YE0HAjUG58so1z5JC71aUFRK38')
print(bot.get_me())
user_times = {}
datebase = {}
feeders = {}
towrite = {}
hallo = 'I am the bot that will help you to drive your feeder. Make sure that feeder is connected to your PC. /time hh:mm - this coomand will tell you the time to feed the pet. You can send it more than once. /delete - this command will delete the list of thime when the feeder needs to feed your cat. /seetime - this coomand will help you to know, when bot will feed your cat. /feed yse this coomand if you want to feed your pat immediatly.'


@bot.message_handler(commands=['start'])
def handle_text(message):
    bot.send_message(message.chat.id, hallo)
    bot.send_message(message.chat.id, "please, write the number of your Feeder using /num. For example: /num 12345")


@bot.message_handler(commands=['num'])
def handle_text(message):
    numb = message.text.replace('/num ', '')
    feeders[numb] = str(message.chat.id)
    bot.send_message(message.chat.id, 'So, the number of your Feeder is '+numb+', if it false, write this command again.')


@bot.message_handler(commands=['help'])
def handle_text(message):
    bot.send_message(message.chat.id, hallo)



@bot.message_handler(commands=['time'])
def handle_text(message):
    usertimes = message.text.replace('/time ', ' ')
    try:
        user_times[message.chat.id].append(usertimes)

    except:
        user_times[message.chat.id] = []
        user_times[message.chat.id].append(usertimes)
    print(usertimes, user_times[message.chat.id])

    ans = ' '
    if len(user_times[message.chat.id]) < 2:
        ans = ans.join(user_times[message.chat.id])
    else:
        ans = ' and '.join(user_times[message.chat.id])
    print( 'ans.join =', ans)
    ans = 'I will feed your cat at ' + ans
    print('ans =', ans)
    fl = open('list.json', 'w')
    towrite['names'] = feeders
    towrite['times'] = user_times
    fl.write(json.dumps(towrite))
    bot.send_message(message.chat.id, ans)


@bot.message_handler(commands=['delete'])
def handle_text(message):
    user_times[message.chat.id] = []
    print('sending')
    bot.send_message(message.chat.id, 'The list of feeding is deleted. Put the time by using /time')


@bot.message_handler(commands=['seetime'])
def handle_text(message):
    ans = ' '
    try:
        if len(user_times[message.chat.id]) < 2:
            ans = ans.join(user_times[message.chat.id])
        elif len(user_times[message.chat.id]) < 1:
            bot.send_message(message.chat.id, "You haven't write any time jet")
        else:
            ans = ' and '.join(user_times[message.chat.id])
        print('ans.join =', ans)
        ans = 'I will feed your cat at ' + ans
        print('ans =', ans)
        bot.send_message(message.chat.id, ans)
    except:
        bot.send_message(message.chat.id, "You haven't write any time jet")

'''
@bot.message_handler(commands=['feed'])
def handle_text(message):
    bot.send_message(message.chat.id, 'feeding...')
    ardu.write(b'1')

'''
bot.polling(none_stop=True, interval=0)

