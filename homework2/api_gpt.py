from openai import OpenAI

client = OpenAI(
    api_key="sk-eojihWMYuwlwO4oNjNMX8DbkkkBtLg7I",
    base_url="https://api.proxyapi.ru/openai/v1",
)

def chat_with_neural_network():
    print("Добро пожаловать в чат с нейросетью! Чтобы выйти, введите 'exit'.")
    
    # Инициализация списка сообщений
    messages = []

    while True:
        user_input = input("Вы: ")

        # Выход из чата
        if user_input.lower() == 'exit':
            print("Вы вышли из чата.")
            break

        # Добавление сообщения пользователя в список сообщений
        messages.append({"role": "user", "content": user_input})

        # Отправка запроса к нейросети
        chat_completion = client.chat.completions.create(
            model="gpt-3.5-turbo-1106", messages=messages
        )
        
        # Получение ответа от нейросети
        response_content = chat_completion.choices[0].message.content
        
        # Вывод ответа
        print("Нейросеть: " + response_content)
        
        # Добавление ответа нейросети в список сообщений для контекста
        messages.append({"role": "assistant", "content": response_content})

if __name__ == "__main__":
    chat_with_neural_network()
