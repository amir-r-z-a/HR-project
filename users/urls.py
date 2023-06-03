from django.urls import path

from .views import *
from interviews.views import *
urlpatterns = [
    path('applicants/', ApplicantCreateView.as_view()),
    path('applicants/<int:pk>/', ApplicantRetrieveView.as_view()),
    path('interviewers/', InterviewerCreateView.as_view()),
    path('interviewers/<int:pk>/', InterviewerRetrieveView.as_view()),
    path('telegram/<str:username>/',telegram_detrmine),
    path('applicants/telegram/<str:username>/<int:chat_id>/', applicant_telegram),
    path('interviewers/telegram/<str:username>/<int:chat_id>/', interviewer_telegram),
]
