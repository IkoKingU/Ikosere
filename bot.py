import telebot

TOKEN = '7460029858:AAHV1QSEVeCJRopM7w8Dbzpngm-OEcEG8O8'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Majburiy obuna bo'lish tugmasi
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Obuna bo\'lish')
    bot.send_message(message.chat.id, "Assalomu alaykum! Botga xush kelibsiz.", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == 'Obuna bo\'lish':
        # Obuna bo'lgandan keyin chiqadigan 3 ta menyu
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row('Rank', 'Ban', 'Tanga')
        bot.send_message(message.chat.id, "Tanlang:", reply_markup=markup)
    elif message.text == 'Rank':
        bot.send_message(message.chat.id, "Rank menyusi")
    elif message.text == 'Ban':
        bot.send_message(message.chat.id, "Ban menyusi")
    elif message.text == 'Tanga':
        bot.send_message(message.chat.id, "Tanga menyusi")
    else:
        bot.send_message(message.chat.id, "Noma'lum buyruq.")

bot.polling()
