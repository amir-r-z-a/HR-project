from ast import Str
from datetime import timedelta
import datetime
from celery import shared_task
import telebot


# token for @ProjAlertBot
# API_TOKEN = "5774491533:AAHhtnS7yn2GEqsXyvwzcpZe-T6lpFLxK5g"
# token for @yektanetaptptojbot
API_TOKEN = '5339827015:AAFiBhkiSk1hRcZnNrDxY44cJvHhs7ylmzQ'

bot = telebot.TeleBot(API_TOKEN)

@shared_task
def send_timed_massage(chat_id,name,date):
    bot.send_message(chat_id=chat_id,text=f"""hello {name} your interview is in an hour""")
    print("massage sent")

@shared_task
def send_info_massage(chat_id,applicant_name,interview_type,date):
    date=date.replace('T',' ')
    date=date.replace('Z','')
    date=date.replace('-','/')
    date_datetime = datetime.datetime.strptime(date,"%Y/%m/%d %H:%M:%S")
    date_datetime= date_datetime+timedelta(hours=4,minutes=30)
    interview_date = date_datetime.strftime("%Y/%m/%d %H:%M:%S")
    bot.send_message(chat_id=chat_id,text=f"""hello your interview with {applicant_name} is a {interview_type} interview and it's on {interview_date}""")
    print("info massage")

