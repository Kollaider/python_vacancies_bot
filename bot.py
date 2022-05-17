import config
import telebot

bot = telebot.TeleBot(config.token)

from hh_parsing import parse_data

from handler_data import handler, prepare_mes

data = handler(parse_data())
messages_data = prepare_mes(data)



@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):  # Название функции не играет никакой роли
    for i, v in messages_data.items():
        bot.send_message(message.chat.id, '\n'.join(v))


if __name__ == '__main__':
    bot.infinity_polling()
