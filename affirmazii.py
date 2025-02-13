import telebot
from openai import OpenAI
from gtts import gTTS
import os

API_TOKEN = '7949247063:AAHRtic45-Q-sBc_LLq46KjdFGTSrmLmKHo'
bot = telebot.TeleBot(API_TOKEN)

client = OpenAI(
    api_key="sk-eojihWMYuwlwO4oNjNMX8DbkkkBtLg7I",
    base_url="https://api.proxyapi.ru/openai/v1",
)

# Инициализация списка сообщений для контекста
messages = []
voice_gender = "female"  # "male" для мужского голоса, "female" для женского

def generate_voice(text):
    """Функция для генерации аудиофайла с использованием gTTS в зависимости от выбранного голоса."""
    tts = gTTS(text=text, lang='ru', slow=False)
    audio_file = 'affirmation.mp3'
    tts.save(audio_file)
    return audio_file

@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = "Добро пожаловать! Я ваш виртуальный помощник. Нажмите кнопку 'Новая аффирмация', чтобы получить аффирмации на день."
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = telebot.types.KeyboardButton("Новая аффирмация")
    markup.add(button)
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup)

@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = "Вы можете запросить новые аффирмации, нажав кнопку 'Новая аффирмация'."
    bot.reply_to(message, help_text)

@bot.message_handler(func=lambda message: message.text == "Новая аффирмация")
def send_affirmation(message):
    global messages

    # Генерация 4 аффирмаций с помощью нейросети
    affirmations = []
    for _ in range(4):
        chat_completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": "Сгенерируй положительную аффирмацию."}]
        )
        affirmation = chat_completion.choices[0].message.content
        affirmations.append(affirmation)

    # Форматирование аффирмаций с нумерацией
    affirmation_message = "\n".join([f"{i + 1}. {affirmation}" for i, affirmation in enumerate(affirmations)])

    # Создание аудиофайла с использованием функции generate_voice
    audio_file = generate_voice(affirmation_message)

    # Отправка аффирмаций и аудиофайла пользователю
    bot.send_message(message.chat.id, affirmation_message)
    with open(audio_file, 'rb') as audio:
        bot.send_audio(message.chat.id, audio)

    # Удаление аудиофайла после отправки
    os.remove(audio_file)

@bot.message_handler(func=lambda message: True)
def respond_to_message(message):
    global messages

    # Добавление сообщения пользователя в список сообщений
    messages.append({"role": "user", "content": message.text})

    # Отправка запроса к нейросети
    chat_completion = client.chat.completions.create(
        model="gpt-4o-mini", messages=messages
    )
    
    # Получение ответа от нейросети
    response_content = chat_completion.choices[0].message.content

    # Отправка ответа обратно пользователю
    bot.reply_to(message, response_content)

    # Добавление ответа нейросети в список сообщений для контекста
    messages.append({"role": "assistant", "content": response_content})

if __name__ == "__main__":
    print("Бот запущен!")
    bot.polling(none_stop=True)