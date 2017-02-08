import telebot
import serial


ardu = serial.Serial('/dev/cu.usbmodem1411')
ardu.baudrate = 9600

bot = telebot.TeleBot('317057242:AAF4onY33YE0HAjUG58so1z5JC71aUFRK38')
print(bot.get_me())
user_times = {}
datebase = {}



@bot.message_handler(commands=['start', 'help'])
def handle_text(message):
    bot.send_message(message.chat.id, 'I am the bot that will help you to drive your feeder. Make sure that feeder is connected to your PC. /time hh:mm - this coomand will tell you the time to feed the pet. You can send it more than once. /delete - this command will delete the list of thime when the feeder needs to feed your cat. /seetime - this coomand will help you to know, when bot will feed your cat. /feed yse this coomand if you want to feed your pat immediatly.')


@bot.message_handler(commands=['time'])
def handle_text(message):
    myfile = open('list.txt', 'w')
    usertimes = message.text.replace('/time ', '')
    try:
        user_times[message.chat.id].append(usertimes)
        datebase[usertimes] = False
    except AttributeError:
        user_times[message.chat.id] = []
        user_times[message.chat.id].append(usertimes)
        datebase[usertimes] = False
    except KeyError:
        user_times[message.chat.id] = []
        user_times[message.chat.id].append(usertimes)
        datebase[usertimes] = False
    print(usertimes, user_times[message.chat.id])

    ans = ' '
    if len(user_times[message.chat.id]) < 2:
        ans = ans.join(user_times[message.chat.id])
    else:
        ans = ' and '.join(user_times[message.chat.id])
    print( 'ans.join =', ans)
    ans = 'I will feed your cat at ' + ans
    print('ans =', ans)
    bot.send_message(message.chat.id, ans)
    myfile.write(str(user_times[message.chat.id]))
    myfile.close()

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

@bot.message_handler(commands=['feed'])
def handle_text(message):
    bot.send_message(message.chat.id, 'feeding...')
    ardu.write(b'1')



bot.polling(none_stop=True, interval=0)