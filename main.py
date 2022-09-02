import telebot

bot = telebot.TeleBot("5765132106:AAE55pDXF2czj2MRmeNrOJtXxpqFG2JCRCw")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет!', parse_mode='html')



bot.polling(none_stop=True)