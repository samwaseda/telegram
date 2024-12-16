import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

with open("BOT_API", "r") as f:
    TELEGRAM_TOKEN = f.read().split("\n")[0]

bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=["start"])
def get_review(message):
    bot.send_message(message.chat.id, message.text)


bot.infinity_polling()
