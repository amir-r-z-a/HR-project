from ftplib import ftpcp
import telebot
import requests
import json
#from ..users.models import *
# from .tasks import *
# token for @ProjAlertBot
# API_TOKEN = "5774491533:AAHhtnS7yn2GEqsXyvwzcpZe-T6lpFLxK5g"
# token for @yektanetaptptojbot
API_TOKEN = '5339827015:AAFiBhkiSk1hRcZnNrDxY44cJvHhs7ylmzQ'

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    username = message.from_user.username
    chat_id = message.chat.id
    response = requests.get(f"http://127.0.0.1:8000/users/telegram/{username}/")
    if response.status_code == 231:
        requests.get(f"http://127.0.0.1:8000/users/interviewers/telegram/{username}/{chat_id}/")
        bot.send_message(chat_id=chat_id,text=f"""you have been singed in as an interviewer""")
    else:
        response = requests.get(f"http://127.0.0.1:8000/users/applicants/telegram/{username}/{chat_id}/")
        bot.send_message(chat_id=chat_id,text=f"""you have been singed in as an applicant""")
        #bot.reply_to(message, f"""this is your interview date : {response.json()}""")
@bot.message_handler()
def echo_message(message):
    bot.reply_to(message, message)


bot.infinity_polling()
