from django.urls import path

from .views import *
from interviews.views import *

urlpatterns = [
    path('interviewers/interviews/', InterviewForInterviewerListView.as_view()),
    path('interviewers/applicants/', ApplicantForInterviewerListView.as_view()),
    path('interviewers/create/feedback/<int:pk>/', FeedbackCreateAPI.as_view()),
    path('interviewers/retrive/feedback/<int:pk>/',FeedbackRetriveAPI.as_view()),
    path('interviewers/create/comment/<int:pk>/', CommentCreateAPI.as_view()),
]