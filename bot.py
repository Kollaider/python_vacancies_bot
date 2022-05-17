import telebot
import config

bot = telebot.TeleBot(config.token)

from hh_parsing import parse_data
from handler_data import handler, prepare_mes


list_data = []


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    first_message = True
    global list_data

    parsed_data = parse_data()
    list_data, data = handler(list_data, parsed_data)
    messages_data = prepare_mes(data)

    if not data:
        bot.send_message(message.chat.id, 'Нет новых данных')

    if not first_message:
        for i, v in messages_data.items():
            bot.send_message(message.chat.id, '\n'.join(v))


if __name__ == '__main__':
    bot.infinity_polling()
