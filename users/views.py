from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.response import Response

from interviews.tasks import *

from .serializer import *
from .permission import IsHRPermission, AccessToInterview

from datetime import datetime, timedelta

# from ..interviews.models import *
from interviews.models import *


class ApplicantCreateView(generics.ListCreateAPIView):
    serializer_class = ApplicantSerializer
    queryset = Applicant.objects.all()
    authentication_classes = (
        TokenAuthentication,
    )

    def get_permissions(self):
        return permissions.IsAuthenticated(), IsHRPermission()


class ApplicantRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer
    authentication_classes = (
        TokenAuthentication,
    )

    def get_permissions(self):
        return permissions.IsAuthenticated(), IsHRPermission()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object().user
        self.perform_destroy(instance=instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class InterviewerCreateView(generics.ListCreateAPIView):
    serializer_class = InterviewerSerializer
    queryset = Interviewer.objects.all()
    authentication_classes = (
        TokenAuthentication,
    )

    def get_permissions(self):
        return permissions.IsAuthenticated(), IsHRPermission()


class InterviewerRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Interviewer.objects.all()
    serializer_class = InterviewerSerializer
    authentication_classes = (
        TokenAuthentication,
    )

    def get_permissions(self):
        return permissions.IsAuthenticated(), IsHRPermission()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object().user
        self.perform_destroy(instance=instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(('GET',))
def applicant_telegram(request, username, chat_id):
    queryset = Applicant.objects.filter(telegram_id=username)
    applicant: Applicant = Applicant.objects.filter(telegram_id=username)[0]
    applicant.chat_id = chat_id
    applicant.save()
    interview: Interview = Interview.objects.filter(applicant=applicant)[0]
    date = interview.date
    time_to_execute = date - timedelta(hours=1)
    send_timed_massage.apply_async((chat_id, applicant.name, date), eta=time_to_execute)
    return Response(data=date, status=201)

@api_view(('GET',))
def interviewer_telegram(request, username, chat_id):
    interviewer:Interviewer=Interviewer.objects.filter(telegram_id=username)[0]
    interviewer.chat_id = chat_id
    interviewer.save()
    return Response(status=200)
@api_view(('GET',))
def telegram_detrmine(request,username):
    try:
        interviewer = Interviewer.objects.get(telegram_id=username)
    except:
        return Response(status=230)
    else:
        return Response(status=231)

