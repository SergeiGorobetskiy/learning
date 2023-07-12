import telebot
from extensions import APIException, Convertor
from config import TOKEN, exchanges
import traceback

# bot name is 'GSV_Cur_conv_SK_bot'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message: telebot.types.Message):
    text = "Hello! \n \
This is a bot for which you can find out the exchange rate \n \
and calculate the amount in the currency you need! \n \
If you want to start, give the command    /start \n \
If you need a hint    /help"
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['help'])
def start(message: telebot.types.Message):
    text = "To get started,  \n \
enter the currency you want to transfer from ___ \n \
the currency you want to convert to ___.  \n \
and <amount of transferred>  \n \
To see the list of available currencies: /values"
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Available currencies:'
    for i in exchanges.keys():
        text = '\n'.join((text, i))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def converter(message: telebot.types.Message):
    values = message.text.split(' ')
    try:
        if len(values) != 3:
            raise APIException('Invalid number of parameters!')

        amount, base, sym = values
        answer = Convertor.get_price(amount, base, sym)
    except APIException as e:
        bot.reply_to(message, f"Command error:\n{e}")
    except Exception as e:
        traceback.print_tb(e.__traceback__)
        bot.reply_to(message, f"Unknown error:\n{e}")
    else:
        bot.send_message(message.chat.id, answer)
        #bot.reply_to(message, answer)


bot.polling()
