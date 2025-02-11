#  Эхо-бот - это бот, который повторяет то, что мы ему отправляем. 

import telebot

# Укажите токен вашего бота, который вы получили от BotFather
API_TOKEN = '7859201529:AAH9t_j-xTyUdT8nTDrbFJRhPhQq1FZO-H8'

# Создаем экземпляр бота
bot = telebot.TeleBot(API_TOKEN)

# Обработчик текстовых сообщений
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

# Запускаем бота
if __name__ == '__main__':
    print("Бот запущен...")
    bot.polling(none_stop=True)
