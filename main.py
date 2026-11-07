main.py
import telebot
import requests

TOKEN = "9018392241:AAH6V12ql_OS7QXW3Q2gLLBC3bGy1XmcYG0"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "مرحباً بك! بوت تيك توك يعمل الآن بنجاح ومتاح 24/7.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"أهلاً بك، لقد أرسلت: {message.text}")

bot.infinity_polling()