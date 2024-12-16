import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from hashlib import sha256

with open("BOT_API", "r") as f:
    TELEGRAM_TOKEN = f.read().split("\n")[0]

bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=["start"])
def get_review(message):
    hash_dict = {}
    with open("hash_list.txt", "r") as f:
        hash_list = f.read().split("\n")
        for h in hash_list:
            h_split = h.split()
            hash_dict[h_split[0]] = h_split[1]
    key = sha256(message.text.split()[1].encode()).hexdigest()
    name = hash_dict.pop(key, None)
    bot.send_message(message.chat.id, "You give a present to: " + name)
    with open("hash_list.txt", "w") as f:
        f.writeh("\n".join([k + " " + v for k, v in hash_dict.items()]))


bot.infinity_polling()
