import requests
import telebot
from keys import my_first_bot_token, weather_API_KEY

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
        "Список доступных команд:\n/start - начать работу с ботом\n/help - получить справку о доступных командах\n/perevorot \"текст\" - перевернуть введенный текст\n/caps \"текст\" - преобразовать введенный текст в заглавные буквы\n/remove_vowels \"текст\" - удалить гласные из введенного текста\n/remove_consonants \"текст\" - удалить согласные из введенного текста\n/weather \"город\" - получить погоду в вашем городе"
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


def get_weather(city):
    API_KEY = weather_API_KEY
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&lang=ru&appid={API_KEY}&units=metric"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temperature = round(data['main']['temp'], 1)
        description = data['weather'][0]['description']
        return f"В городе {city} температура составляет {temperature}°C, {description}"
    else:
        return "Невозможно получить данные о погоде"


# Обработка команды /weather
# @bot.message_handler(commands=['weather'])
# def handle_weather(message):
#     city = message.text.split(' ', 1)[1]  # Получаем город
#     # city = "Moscow"
#     weather = get_weather(city)
#     # Ваш код обработки команды /weather здесь
#     bot.send_message(message.chat.id, weather)


@bot.message_handler(commands=['weather'])
def handle_weather(message):
    bot.send_message(message.chat.id, "Введите название города:")
    bot.register_next_step_handler(message, get_city)


def get_city(message):
    city = message.text
    weather = get_weather(city)
    bot.send_message(message.chat.id, weather)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(
        message,
        "Список доступных команд:\n/start - начать работу с ботом\n/help - получить справку о доступных командах\n/perevorot \"текст\" - перевернуть введенный текст\n/caps \"текст\" - преобразовать введенный текст в заглавные буквы\n/remove_vowels \"текст\" - удалить гласные из введенного текста\n/remove_consonants \"текст\" - удалить согласные из введенного текста\n/weather \"город\" - получить погоду в вашем городе"
    )


# Пример использования
# city = "Moscow"
# weather_info = get_weather(city)
# print(weather_info)

###

# def weather(update, context):
#     # Получаем город из сообщения пользователя
#     city = update.message.text.split(' ', 1)[1]

#     # Формируем запрос к API погоды
#     url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_API_KEY&units=metric'

#     # Отправляем запрос и получаем данные о погоде
#     response = requests.get(url)
#     data = response.json()

#     # Проверяем, получены ли данные о погоде
#     if data['cod'] == 200:
#         # Извлекаем нужную информацию о погоде
#         weather_description = data['weather'][0]['description']
#         temperature = data['main']['temp']

#         # Отправляем сообщение с информацией о погоде
#         update.message.reply_text(f'The weather in {city} is {weather_description} with a temperature of {temperature}°C')
#     else:
#         update.message.reply_text('Could not retrieve weather information for this city')

# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#     bot.reply_to(
#         message,
#         "Список доступных команд:\n/start - начать работу с ботом\n/help - получить справку о доступных командах"
#     )

# Запускаем бота
bot.polling()
