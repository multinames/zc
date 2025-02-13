import telebot
from gtts import gTTS
import os

API_TOKEN = '7949247063:AAHRtic45-Q-sBc_LLq46KjdFGTSrmLmKHo'
bot = telebot.TeleBot(API_TOKEN)

# Глобальная переменная для хранения выбранного голоса
voice_gender = 'female'  # По умолчанию женский голос

@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = "Добро пожаловать! Выберите голос для озвучивания сообщений:\n" \
                   "/male - Мужской голос\n" \
                   "/female - Женский голос\n" \
                   "Отправьте любое сообщение, и я озвучу его."
    bot.reply_to(message, welcome_text)

@bot.message_handler(commands=['male'])
def set_male_voice(message):
    global voice_gender
    voice_gender = 'male'
    bot.reply_to(message, "Вы выбрали мужской голос.")

@bot.message_handler(commands=['female'])
def set_female_voice(message):
    global voice_gender
    voice_gender = 'female'
    bot.reply_to(message, "Вы выбрали женский голос.")

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    # Генерация аудиофайла с использованием gTTS
    tts = gTTS(text=message.text, lang='ru', slow=False)
    audio_file = 'message.mp3'
    tts.save(audio_file)

    # Отправка аудиофайла пользователю
    with open(audio_file, 'rb') as audio:
        bot.send_audio(message.chat.id, audio)

    # Удаление аудиофайла после отправки
    os.remove(audio_file)

if __name__ == "__main__":
    print("Бот запущен!")
    bot.polling(none_stop=True)