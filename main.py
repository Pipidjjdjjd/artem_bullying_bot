import telebot
import random
import os

# Получаем токен из переменной окружения
TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

# Имя жертвы
target_name = "Артём"

# Жесткие оскорбления
dirty_insults = [
    "Ты сын одноклеточной проститутки.",
    "Твой батя одноклеточная амеба и мать твоя такая же.",
    "Нет иди нахуй.",
    "На день рождения я подарю тебе прах твоего папы."
]

# Умные и матерные оскорбления
repetitor_insults = [
    "Ты дегроид ебаный, эволюция на тебе застопорилась.",
    "Слово 'позор' — это ты в словаре, пиздюк.",
    "Ты ошибка природы, и мать твоя это подтверждает.",
    "Да у улитки больше мозгов, чем у тебя и твоей семьи.",
    "Если бы тупость была валютой — ты бы был миллиардером, мразь.",
    "Ты родился не по любви, а по ошибке. Отрицательной."
]

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    name = message.from_user.first_name

    if target_name.lower() in name.lower():
        # 50/50 шанс — грязное или “умное” оскорбление
        if random.random() < 0.5:
            bot.reply_to(message, random.choice(dirty_insults))
        else:
            bot.reply_to(message, random.choice(repetitor_insults))

bot.infinity_polling()