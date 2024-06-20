import telebot
from keys import my_first_bot_token

# Указываем токен вашего бота
TOKEN = my_first_bot_token

# Создаем объект бота
bot = telebot.TeleBot(TOKEN)


# Обработка команды /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(
        message.chat.id,
        "Привет! Я бот. Для списка доступных команд используйте /help")


# Обработка команды /help
@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.send_message(
        message.chat.id,
        "Список доступных команд:\n/start - начать работу с ботом\n/help - получить справку о доступных командах\n/perevorot - перевернуть введенный текст\n/caps - преобразовать введенный текст в заглавные буквы\n/remove_vowels - удалить гласные из введенного текста\n/remove_consonants - удалить согласные из введенного текста"
    )


# Обработка команды /perevorot
@bot.message_handler(commands=['perevorot'])
def handle_perevorot(message):
    text = message.text.split(' ',
                              1)[1]  # Получаем текст после команды /perevorot
    reversed_text = text[::-1]  # Переворачиваем текст
    bot.send_message(message.chat.id, reversed_text)


# Обработка команды /caps
@bot.message_handler(commands=['caps'])
def handle_caps(message):
    text = message.text.split(' ', 1)[1]  # Получаем текст после команды /caps
    caps_text = text.upper()  # Преобразуем текст в заглавные буквы
    bot.send_message(message.chat.id, caps_text)


# Функция для удаления гласных из текста
def remove_vowels(text):
    vowels = "aeiouAEIOUаеёиоуыэюяАЕЁИОУЫЭЮЯ"
    return ''.join(char for char in text if char not in vowels)


# Функция для удаления согласных из текста
def remove_consonants(text):
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZбвгджзклмнпрстфхцчшщБВГДЖЗКЛМНПРСТФХЦЧШЩ"
    return ''.join(char for char in text if char not in consonants)


# Обработка команды /remove_vowels
@bot.message_handler(commands=['remove_vowels'])
def handle_remove_vowels(message):
    text = message.text.split(
        ' ', 1)[1]  # Получаем текст после команды /remove_vowels
    text_without_vowels = remove_vowels(text)
    bot.send_message(message.chat.id, text_without_vowels)


# Обработка команды /remove_consonants
@bot.message_handler(commands=['remove_consonants'])
def handle_remove_consonants(message):
    text = message.text.split(
        ' ', 1)[1]  # Получаем текст после команды /remove_consonants
    text_without_consonants = remove_consonants(text)
    bot.send_message(message.chat.id, text_without_consonants)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(
        message,
        "Список доступных команд:\n/start - начать работу с ботом\n/help - получить справку о доступных командах\n/perevorot - перевернуть введенный текст\n/caps - преобразовать введенный текст в заглавные буквы\n/remove_vowels - удалить гласные из введенного текста\n/remove_consonants - удалить согласные из введенного текста"
    )


# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#     bot.reply_to(
#         message,
#         "Список доступных команд:\n/start - начать работу с ботом\n/help - получить справку о доступных командах"
#     )

# Запускаем бота
bot.polling()
