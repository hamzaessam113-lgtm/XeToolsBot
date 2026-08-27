import os
import telebot

# استدعاء التوكن الذي قمنا بتخزينه في إعدادات الأمان
TOKEN = os.getenv('TELEGRAM_TOKEN')

if not TOKEN:
    print("Error: TELEGRAM_TOKEN is missing!")
    exit(1)

bot = telebot.TeleBot(TOKEN)

# رد على أي رسالة نصية يرسلها المستخدم
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "أهلاً بك يا حمزة! البوت يعمل بنجاح على جيثب 🚀")

print("Bot is running...")
bot.infinity_polling()

