from django.urls import path
from .views import *

urlpatterns = [
    path('', InterviewCreateView.as_view()),
    path('<int:pk>/', InterviewRetrieveView.as_view()),
]
