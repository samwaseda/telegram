import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

with open("BOT_API", "r") as f:
    TELEGRAM_TOKEN = f.read().split("\n")[0]

bot = telebot.TeleBot(TELEGRAM_TOKEN)


bot.infinity_polling()
