from openai import OpenAI
from keys import ai_con_api_key


def main():
    client = OpenAI(
        api_key=ai_con_api_key,
        base_url="https://api.proxyapi.ru/openai/v1",
    )

    while True:
        user_input = input("Вы: ")  # Пользователь вводит запрос
        if user_input.lower() == 'exit':
            print("До свидания!")
            break

        chat_completion = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=[{
                "role": "user",
                "content": user_input
            }])

        response = chat_completion.choices[0].message.content
        print(f"Нейросеть: {response}")  # Выводим ответ нейросети


if __name__ == "__main__":
    main()
