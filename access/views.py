from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response

from interviews.models import *
from users.models import *

from interviews.serializer import *
from users.serializer import *
from .serializer import *

from .permission import *
class InterviewForInterviewerListView(generics.ListAPIView):
    serializer_class = InterviewSerializer
    authentication_classes = (
        TokenAuthentication,
    )

    def get_permissions(self):
        return (permissions.IsAuthenticated(), AccessToInterview())

    def get_queryset(self):
        user = self.request.user
        try:
            interviewer = user.interviewer
        except:
            queryset = Interview.objects.all()
            return queryset
        else:
            queryset = Interview.objects.filter(interviewer=interviewer)
            if len(queryset) == 0:
                return self.permission_denied(self.request)
            else:
                return queryset



class ApplicantForInterviewerListView(generics.ListAPIView):
    serializer_class = InterviewApplicantSerializer
    authentication_classes = (
        TokenAuthentication,
    )

    def get_permissions(self):
        return (permissions.IsAuthenticated(), AccessToInterview())

    def get_queryset(self):
        user = self.request.user
        try:
            interviewer = user.interviewer
        except:
            queryset = Interview.objects.all()
            return queryset
        else:
            queryset = Interview.objects.filter(interviewer=interviewer)
            if len(queryset) == 0:
                return self.permission_denied(self.request)
            else:
                return queryset


class FeedbackCreateAPI(generics.CreateAPIView):
    serializer_class = FeedbackSerializer
    authentication_classes = (
        TokenAuthentication,
    )

    def get_queryset(self):
        user = self.request.user
        try:
            interviewer = user.interviewer
        except:
            queryset = Interview.objects.all()
            return queryset
        else:
            queryset = Interview.objects.filter(interviewer=interviewer)
            if len(queryset) == 0:
                return self.permission_denied(self.request)
            else:
                return queryset
    def get_permissions(self):
        return (permissions.IsAuthenticated(), AccessToInterview())

    def perform_create(self, serializer):
        try:
            instance = self.get_object()
        except:
            return self.permission_denied(self.request)
        else:
            serializer.save(interview=instance)
class FeedbackRetriveAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FeedbackSerializer
    authentication_classes = (
        TokenAuthentication,
    )
    def get_permissions(self):
        return (permissions.IsAuthenticated(), AccessToInterview())
    def get_queryset(self):
        user = self.request.user
        try:
            interviewer = user.interviewer
        except:
            return Interview.objects.all()
        else:
            queryset = Interview.objects.filter(interviewer=interviewer)
            if len(queryset) == 0:
                return self.permission_denied(self.request)
            else:
                return queryset
    def get(self, request, *args, **kwargs):
        try:
            interview = self.get_object()
        except:
            return self.permission_denied(self.request)
        else:
            instance = Feedback.objects.get(interview=interview)
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        try:
            interview = self.get_object()
        except:
            return self.permission_denied(self.request)
        else:
            instance = Feedback.objects.get(interview=interview)
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
    def delete(self, request, *args, **kwargs):
        try:
            interview = self.get_object()
        except:
            return self.permission_denied(self.request)
        else:
            instance = Feedback.objects.get(interview=interview)
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)


class CommentCreateAPI(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    authentication_classes = (
        TokenAuthentication,
    )

    def get_queryset(self):
        user = self.request.user
        try:
            interviewer = user.interviewer
        except:
            queryset = Interview.objects.all()
            return queryset
        else:
            queryset = Interview.objects.filter(interviewer=interviewer)
            if len(queryset) == 0:
                return self.permission_denied(self.request)
            else:
                return queryset
    def get_permissions(self):
        return (permissions.IsAuthenticated(), AccessToInterview())

    def perform_create(self, serializer):
        try:
            instance = self.get_object()
        except:
            return self.permission_denied(self.request)
        else:
            serializer.save(interview=instance)
    def list(self, request, *args, **kwargs):
        try:
            comment_set = Comment.objects.filter(interview=self.get_object())[0]
        except:
            return self.permission_denied(self.request)
        else:
            queryset = self.filter_queryset(queryset=Comment.objects.filter(interview=self.get_object()))
            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)