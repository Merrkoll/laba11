import telebot
import webbrowser

bot = telebot.TeleBot('6506694540:AAFIcq7w4vbYJLCRa6tSf16SpEpLwc9LMXc')
@bot.message_handler(commands=['site'])
def site(message):
    webbrowser.open('https://www.championat.com/basketball/_nba/tournament/5696/table/')
@bot.message_handler(commands=['team'])
def site(message):
    webbrowser.open('https://lakersnation.com/')
@bot.message_handler(commands=['coach'])
def site(message):
    webbrowser.open('https://coachwooden.com/')
@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет, любишь баскетбол, бро?? ')
@bot.message_handler()
def info(message):
    if message.text.lower() == 'да':
        bot.send_message(message.chat.id, 'Тогда введи запрос, которой тебе больше всего интересен: турнирная таблица, лучшая баскетбольная команда, лучший тренер в баскетболе')
    elif message.text.lower() == 'турнирная таблица':
        bot.reply_to(message, 'можешь перейти на сайт, для этого введи команду /site')
    elif message.text.lower() == 'лучшая баскетбольная команда':
        bot.reply_to(message, 'LA Lakers, чтобы перейти на их сайт введи команду /team')
    elif message.text.lower() == 'лучший тренер в баскетболе':
        bot.send_message(message.chat.id,'Джон Вуден, если хочешь узнать больше о его биографии введи команду /coach')
    else:
        bot.send_message(message.chat.id,'к сожалению этот бот не может вам помочь')




bot.polling(none_stop=True)
