import telebot
from openai import OpenAI
from gtts import gTTS
import os
from pathlib import Path

API_TOKEN = '7859201529:AAH9t_j-xTyUdT8nTDrbFJRhPhQq1FZO-H8'
bot = telebot.TeleBot(API_TOKEN)

client = OpenAI(
    api_key="sk-eojihWMYuwlwO4oNjNMX8DbkkkBtLg7I",
    base_url="https://api.proxyapi.ru/openai/v1",
)

# Инициализация списка сообщений для контекста
messages = []

@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = "Добро пожаловать! Я ваш виртуальный помощник. Как я могу вам помочь?"
    bot.reply_to(message, welcome_text)

@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = "Вы можете задать мне любые вопросы, и я постараюсь на них ответить. Просто напишите ваше сообщение!"
    bot.reply_to(message, help_text)

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

    # Добавление ответа нейросети в список сообщений для контекста
    messages.append({"role": "assistant", "content": response_content})

    # Создание аудиофайла с ответом
    audio_file_path = Path(f"audio/{message.chat.id}.mp3")
    os.makedirs(audio_file_path.parent, exist_ok=True)
    
    tts = gTTS(text=response_content, lang='ru')  # Укажите язык, например 'ru' для русского
    tts.save(str(audio_file_path))

    # Отправка ответа обратно пользователю в текстовом виде
    bot.reply_to(message, response_content)

    # Отправка аудиофайла обратно пользователю
    with open(audio_file_path, 'rb') as audio_file:
        bot.send_audio(message.chat.id, audio_file)

    # Удаление аудиофайла после отправки
    os.remove(audio_file_path)

if __name__ == "__main__":
    print("Бот запущен!")
    bot.polling(none_stop=True)
