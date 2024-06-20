import telebot
from keys import my_first_bot_token

# Укажите токен вашего бота
TOKEN = 'my_first_bot_token'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот. Как я могу вам помочь?")


@bot.message_handler(func=lambda message: message.text.lower() == 'привет')
def reply_hello(message):
    bot.reply_to(message, "Привет!")


@bot.message_handler(func=lambda message: message.text.lower() == 'как дела?')
def reply_how_are_you(message):
    bot.reply_to(message, "У меня все отлично, спасибо! Как у вас?")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.polling()
