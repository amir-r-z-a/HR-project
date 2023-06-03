from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import *
from django.contrib.auth import get_user_model

class ApplicantSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=200, write_only=True)
    password = serializers.CharField(max_length=200, write_only=True)

    def save(self, **kwargs):
        user_model = get_user_model()
        username = self.validated_data.pop('username')
        password = self.validated_data.pop('password')
        try:
            user = User.objects.filter(username=username)[0]
        except:
            user = user_model.objects.create_user(username=username, password=password, )
            token = Token.objects.create(user=user)
        applicant = super().save(user=user, **kwargs)
        return applicant

    class Meta:
        model = Applicant
        fields = (
            'username',
            'password',
            'name',
            'telegram_id',
            'resume',
            'linkedin_address',
            'age',
            'sex',
            'status'
        )


class InterviewerSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=200,write_only=True)
    password = serializers.CharField(max_length=200,write_only=True)
    def save(self, **kwargs):
        user_model = get_user_model()
        username = self.validated_data.pop('username')
        password = self.validated_data.pop('password')
        try:
            user = User.objects.filter(username=username)[0]
        except:
            user = user_model.objects.create_user(username=username, password=password, )
            token = Token.objects.create(user=user)
        interviewer = super().save(user=user, **kwargs)
        return interviewer

    class Meta:
        model = Interviewer
        fields = (
            'username',
            'password',
            'telegram_id',
        )
