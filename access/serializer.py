from rest_framework import serializers

from users.models import *
from interviews.models import *
from users.serializer import *
class InterviewApplicantSerializer(serializers.ModelSerializer):
    applicant = ApplicantSerializer(read_only=True)

    class Meta:
        model = Interview
        fields = (
            'applicant',
        )


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'comment_text',
        )


class FeedbackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Feedback
        fields = (
            'feedback_text',
        )