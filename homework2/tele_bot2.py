import telebot

API_TOKEN = '7859201529:AAH9t_j-xTyUdT8nTDrbFJRhPhQq1FZO-H8'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я ваш Telegram-бот. Чем могу помочь?")

@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = (
        "Доступные команды:\n"
        "/start - Приветственное сообщение\n"
        "/help - Список доступных команд\n"
        "/perevorot <текст> - Перевернуть указанный текст\n"
        "/caps <текст> - Преобразовать указанный текст в заглавные буквы\n"
        "/cut <текст> - Удалить все гласные из указанного текста\n"
        "/sum <текст> - Подсчитать количество символов в сообщении"
    )
    bot.reply_to(message, help_text)

@bot.message_handler(commands=['perevorot'])
def perevorot(message):
    # Получаем текст после команды и удаляем команду
    text = message.text[len('/perevorot '):]
    
    if text:
        # Переворачиваем текст
        reversed_text = text[::-1]
        # Отправляем перевернутый текст
        bot.reply_to(message, reversed_text)
    else:
        # Если текст не указан, отправляем сообщение об ошибке
        bot.reply_to(message, "Пожалуйста, укажите текст для переворота.")

@bot.message_handler(commands=['caps'])
def caps(message):
    # Получаем текст после команды и удаляем команду
    text = message.text[len('/caps '):]
    
    if text:
        # Преобразуем текст в заглавные буквы
        upper_text = text.upper()
        # Отправляем преобразованный текст
        bot.reply_to(message, upper_text)
    else:
        # Если текст не указан, отправляем сообщение об ошибке
        bot.reply_to(message, "Пожалуйста, укажите текст для преобразования в заглавные буквы.")

@bot.message_handler(commands=['cut'])
def cut(message):
    # Получаем текст после команды и удаляем команду
    text = message.text[len('/cut '):]
    
    if text:
        # Удаляем все гласные
        vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
        cut_text = ''.join([char for char in text if char not in vowels])
        # Отправляем текст без гласных
        bot.reply_to(message, cut_text)
    else:
        # Если текст не указан, отправляем сообщение об ошибке
        bot.reply_to(message, "Пожалуйста, укажите текст для удаления гласных.")

@bot.message_handler(commands=['sum'])
def count_characters(message):
    # Получаем текст после команды и удаляем команду
    text = message.text[len('/sum '):]
    
    if text:
        # Подсчитываем количество символов в тексте
        num_characters = len(text)
        # Отправляем количество символов
        bot.reply_to(message, f"Количество символов в вашем сообщении: {num_characters}")
    else:
        # Если текст не указан, отправляем сообщение об ошибке
        bot.reply_to(message, "Пожалуйста, укажите текст для подсчета символов.")

if __name__ == '__main__':
    print("Бот запущен!")
    bot.polling(none_stop=True)