import telebot
import requests
import pprint

TOKEN = ''  # токен управления ботом, который выдал @BotFather
bot = telebot.TeleBot(TOKEN)  # создает новый Telegram Bot объект


@bot.message_handler(commands=['start'])  # ответ на вход пользователя
def handle_start(message):
    bot.send_message(message.chat.id, text='Мы рады приветствовать тебя в нашем паблике! '
                                           'Здесь ты сможешь узнавать расписание и заданную домашнюю '
                                           'работу на любой день. Также мы будем собирать для тебя '
                                           'самые интересные статьи, мемы и новости.')


@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.send_message(message.chat.id, text='help')


@bot.message_handler(commands=['schedule'])
def handle_schedule(message):
    pass


@bot.message_handler(commands=['memes'])
def handle_memes(message):
    r = requests.get(url_9gag)


bot.polling()  # функция, посылающая запросы на серверы Telegram для проверки новых сообщений
