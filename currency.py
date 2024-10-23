import telebot
from telebot import types

bot = telebot.TeleBot(token="7922175837:AAHNxBLLvBzeLBimjZKVjblPlMQ9slnCt9E")

USD = 11000
EUR = 12000
RUB = 150

@bot.message_handler(commands=['start'])
def start(message):
    name = message.from_user.username
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    convert = types.KeyboardButton('Конвертировать валюту')
    markup.add(convert)
    bot.send_message(message.from_user.id, f"Добро пожаловать {name} чтобы начать нажмите кнопку снизу", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    name = message.from_user.username
    if message.text == 'Конвертировать валюту':
        suma = bot.reply_to(message, f"Введите сумму в сумах для конвертации {name}: ")
        bot.register_next_step_handler(suma, currency)

def currency(message):
    try:
        sum_amount = float(message.text)
        usd = sum_amount / USD
        eur = sum_amount / EUR
        rub = sum_amount / RUB
        bot.send_message(message.chat.id, f"Сумма в:\nДолларах: {usd:.2f} USD\nЕвро: {eur:.2f} EUR\nРублях: {rub:.2f} RUB") #.2f — это форматирование для вывода чисел с двумя знаками после запятой.
    except ValueError:
        bot.send_message(message.chat.id, "Пожалуйста, введите сумму в цифрах.")

bot.infinity_polling()