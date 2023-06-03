from rest_framework import generics, permissions, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response

from .serializer import *
from .permission import IsHRPermission, AccessToInterview
from .tasks import *
from datetime import datetime, timedelta
from users.models import *

import telebot

# token for @ProjAlertBot
# API_TOKEN = "5774491533:AAHhtnS7yn2GEqsXyvwzcpZe-T6lpFLxK5g"
# token for @yektanetaptptojbot
API_TOKEN = '5339827015:AAFiBhkiSk1hRcZnNrDxY44cJvHhs7ylmzQ'

bot = telebot.TeleBot(API_TOKEN)


class InterviewCreateView(generics.ListCreateAPIView):
    serializer_class = InterviewSerializer
    authentication_classes = (
        TokenAuthentication,
    )
    queryset = Interview.objects.all()

    def get_permissions(self):
        return (permissions.IsAuthenticated(), IsHRPermission())

    def perform_create(self, serializer):
        serializer.save()
        interview:Interview = Interview.objects.all()[len(Interview.objects.all())-1]
        interviewer:Interviewer = interview.interviewer
        applicant:Applicant = interview.applicant
        #bot.send_message(chat_id=interviewer.chat_id,text=f"""hello your interview with {applicant.name} is a {interview.interview_type} type interview and it's on {interview.date}""")
        send_info_massage.delay(interviewer.chat_id,applicant.name,interview.interview_type,interview.date)

class InterviewRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = InterviewSerializer
    queryset = Interview.objects.all()
    authentication_classes = (
        TokenAuthentication,
    )

    def get_permissions(self):
        return (permissions.IsAuthenticated(), IsHRPermission())


        



