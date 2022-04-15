import telebot
bot = telebot.TeleBot("5203945905:AAHCRXdcGiTI94PbR_n0qSrOGkfQbVkro50", parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, 'Привет \nДавай попробуем найти тебе задание на сегодня')

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

    bot.infinity_polling()