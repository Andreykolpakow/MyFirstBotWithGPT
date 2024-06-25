import telebot
from gtts import gTTS
import os
from openai import OpenAI
from keys import my_first_bot_token, ai_con_api_key

# Указываем токен вашего бота
TOKEN = my_first_bot_token

# Создаем объект бота
bot = telebot.TeleBot(TOKEN)

# Обработка команды /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Привет! Я бот. Напиши мне что-нибудь!")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    client = OpenAI(
        api_key=ai_con_api_key,
        base_url="https://api.proxyapi.ru/openai/v1",
    )

    user_input = message.text
    if user_input.lower() == 'exit':
        bot.send_message(message.chat.id, "До свидания!")
    else:
        messages = [{
            "role": "user",
            "content": user_input
        }, {
            "role": "system",
            "content": "отвечай подробно и понятно"
        }]

        chat_completion = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=messages)

        response = chat_completion.choices[0].message.content

        # Озвучиваем ответ нейросети
        tts = gTTS(text=response, lang='ru')
        tts.save("response.mp3")

        bot.send_message(message.chat.id, "Нейросеть отвечает:")
        audio = open("response.mp3", "rb")
        bot.send_voice(message.chat.id, audio)

        # Удаляем временный файл с ответом
        os.remove("response.mp3")


if __name__ == "__main__":
    bot.polling(none_stop=True)
