from packages.ip_calculator import subnet_ip

from telebot import TeleBot
from telebot.types import Message

import logging
import time
import os
from dotenv import *

load_dotenv()
logging.basicConfig(filename='/var/log/ipcalc_error.log', format='%(asctime)s  ERROR %(message)s')
TOKEN = os.getenv('BOT_TOKEN')
bot = TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help', 'about'])
def command_start(message: Message):
    """Приветствие пользователя"""
    if message.text == '/start':
        bot.send_message(message.from_user.id, "Добро пожаловать в бот IP калькулятор, "
                                               "для расчёта необходимо "
                                               "отправить IP адрес в виде: 192.168.100.65/23")
    elif message.text == '/help':
        bot.send_message(message.from_user.id, "IP калькулятор, позволит вам быстро и легко "
                                               "разбить ваши сети на подсети")
    elif message.text == '/about':
        bot.send_message(message.from_user.id, "Для справки @KhasanKarabayev")


@bot.message_handler(content_types=["text"])
def subnet_address(message: Message):
    """Обработка входящего текста"""
    if ipaddress := subnet_ip(message.text):
        text = f"{ipaddress['Network']} - Network\n{ipaddress['FirstHost']} - FirstHost" \
               f"\n{ipaddress['LastHost']} - LastHost\n{ipaddress['BroadCast']} - BroadCast \n\n" \
               f"\n{ipaddress['Mask']} - Mask\n{ipaddress['WireCard']} - WireCard\n{ipaddress['Hosts']} - Hosts"
        bot.send_message(message.from_user.id, text)
    else:
        bot.send_message(message.from_user.id, "Неверные данные")


while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        logging.error(e)
        time.sleep(15)
